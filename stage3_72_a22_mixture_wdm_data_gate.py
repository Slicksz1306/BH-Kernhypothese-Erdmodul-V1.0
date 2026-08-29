#!/usr/bin/env python3
"""Stage 3.72 / A22: Fe-Ni-light-element WDM workbook ingestion gate.

The Liu & Asimow (2024/2025) CaltechDATA record provides raw DFT/experimental
workbooks for Fe, Fe-Ni, Fe-O, Fe-Si, Fe-S, Fe-C, Fe-H and selected ternaries.
This script inventories and validates those workbooks once locally available.

It deliberately does NOT guess workbook units or synthesize a multicomponent
EOS when required thermodynamic columns/metadata are absent. The purpose is to
turn the remaining Full-WDM mixture closure into a reproducible data pipeline.

Supported input formats:
- .xlsx via pandas/openpyxl
- .xls via pandas with an installed compatible legacy Excel engine (e.g. xlrd)

Output:
- sheet/column inventory
- numeric ranges for each column
- candidate aliases for P, T, rho/volume, energy
- coverage matrix by composition file
- explicit BLOCKED flags where units/schema cannot be established

No scientific rate is produced until a thermodynamically identified table is
available and a mixing/free-energy model is explicitly supplied.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Iterable

import numpy as np
import pandas as pd

EXPECTED_FILES = (
    "Fe11.xls",
    "Ni_Fe11.xls",
    "O_Fe11.xls",
    "Si_Fe11.xls",
    "S_Fe11.xls",
    "C_Fe11.xls",
    "H_Fe11.xls",
    "O12_Si6_Fe11.xls",
    "O6_Si12_Fe11.xls",
    "O9_Si9_Fe11.xls",
    "O32_Fe11.xls",
    "Si9_Fe11.xls",
    "Table.S.1.xlsx",
    "Table.S.2.xlsx",
    "Table.S.3.xlsx",
    "tableS4.xlsx",
    "shock_wave_data.xlsx",
)

ALIASES = {
    "pressure": ("p", "pressure", "press", "p_gpa", "pressure_gpa"),
    "temperature": ("t", "temp", "temperature", "t_k", "temperature_k"),
    "density": ("rho", "density", "rho_gcc", "density_gcc", "density_gcm3"),
    "volume": ("v", "vol", "volume", "volume_a3", "atomic_volume"),
    "energy": ("e", "energy", "u", "internal_energy", "etot", "total_energy"),
}


@dataclass
class ColumnSummary:
    name: str
    dtype: str
    numeric_count: int
    finite_min: float | None
    finite_max: float | None
    aliases: list[str]


@dataclass
class SheetSummary:
    file: str
    sheet: str
    nrows: int
    ncols: int
    columns: list[ColumnSummary]
    candidate_fields: dict[str, list[str]]
    thermodynamic_minimum: bool


def normalize_name(name: object) -> str:
    s = str(name).strip().lower()
    for c in " -/()[]{}":
        s = s.replace(c, "_")
    while "__" in s:
        s = s.replace("__", "_")
    return s.strip("_")


def aliases_for_column(name: object) -> list[str]:
    n = normalize_name(name)
    out = []
    for field, aliases in ALIASES.items():
        if n in aliases or any(a in n for a in aliases if len(a) >= 4):
            out.append(field)
    return out


def summarize_column(series: pd.Series) -> ColumnSummary:
    vals = pd.to_numeric(series, errors="coerce").to_numpy(dtype=float)
    finite = vals[np.isfinite(vals)]
    return ColumnSummary(
        name=str(series.name),
        dtype=str(series.dtype),
        numeric_count=int(finite.size),
        finite_min=float(finite.min()) if finite.size else None,
        finite_max=float(finite.max()) if finite.size else None,
        aliases=aliases_for_column(series.name),
    )


def summarize_sheet(file_name: str, sheet_name: str, df: pd.DataFrame) -> SheetSummary:
    cols = [summarize_column(df[c]) for c in df.columns]
    candidates = {k: [] for k in ALIASES}
    for c in cols:
        for a in c.aliases:
            candidates[a].append(c.name)

    # A minimal EOS state table should identify P,T and either rho or V.
    minimum = bool(candidates["pressure"] and candidates["temperature"] and
                   (candidates["density"] or candidates["volume"]))
    return SheetSummary(
        file=file_name,
        sheet=sheet_name,
        nrows=int(len(df)),
        ncols=int(len(df.columns)),
        columns=cols,
        candidate_fields=candidates,
        thermodynamic_minimum=minimum,
    )


def read_workbook(path: Path) -> list[SheetSummary]:
    try:
        xls = pd.ExcelFile(path)
    except Exception as exc:
        raise RuntimeError(
            f"cannot open {path.name}: {exc}. For legacy .xls, install an "
            "appropriate pandas Excel engine such as xlrd."
        ) from exc
    out = []
    for sheet in xls.sheet_names:
        df = pd.read_excel(path, sheet_name=sheet)
        out.append(summarize_sheet(path.name, str(sheet), df))
    return out


def inventory(directory: Path) -> dict:
    present = {p.name: p for p in directory.iterdir() if p.is_file()}
    rows: list[SheetSummary] = []
    errors: dict[str, str] = {}
    for name in EXPECTED_FILES:
        if name not in present:
            continue
        try:
            rows.extend(read_workbook(present[name]))
        except Exception as exc:
            errors[name] = str(exc)

    missing = [name for name in EXPECTED_FILES if name not in present]
    minimum_sheets = [r for r in rows if r.thermodynamic_minimum]
    return {
        "directory": str(directory),
        "expected_files": list(EXPECTED_FILES),
        "present_expected_files": [n for n in EXPECTED_FILES if n in present],
        "missing_expected_files": missing,
        "read_errors": errors,
        "sheets": [asdict(r) for r in rows],
        "thermodynamic_minimum_sheets": [f"{r.file}:{r.sheet}" for r in minimum_sheets],
        "status": (
            "SCHEMA CANDIDATES FOUND; MANUAL UNIT/METADATA VALIDATION REQUIRED"
            if minimum_sheets else
            "DATA/SCHEMA INCOMPLETE OR UNAVAILABLE; MIXTURE EOS CLOSURE OPEN"
        ),
    }


def synthetic_self_test() -> None:
    df = pd.DataFrame({
        "Pressure_GPa": [100.0, 200.0, 300.0],
        "Temperature_K": [4000.0, 5000.0, 6000.0],
        "rho_gcc": [10.0, 11.0, 12.0],
        "Energy_eV": [-8.0, -7.5, -7.0],
    })
    s = summarize_sheet("synthetic.xlsx", "Sheet1", df)
    if not s.thermodynamic_minimum:
        raise RuntimeError("synthetic schema regression failed")
    assert "Pressure_GPa" in s.candidate_fields["pressure"]
    assert "Temperature_K" in s.candidate_fields["temperature"]
    assert "rho_gcc" in s.candidate_fields["density"]
    print("synthetic workbook/schema regression: PASS")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("directory", nargs="?", type=Path,
                    help="directory containing downloaded CaltechDATA workbooks")
    ap.add_argument("--json", type=Path, help="optional JSON report path")
    args = ap.parse_args()

    synthetic_self_test()
    if args.directory is None:
        print("No workbook directory supplied.")
        print("Status: INGESTION/SCHEMA GATE READY; RAW BINARY DOWNLOAD OPEN")
        return
    if not args.directory.is_dir():
        raise SystemExit(f"not a directory: {args.directory}")

    report = inventory(args.directory)
    print(json.dumps(report, indent=2, ensure_ascii=False))
    if args.json:
        args.json.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\nScientific guardrails")
    print("- column-name matches are candidates, not unit proof")
    print("- no mixing rule/free energy is inferred automatically")
    print("- no Michel Mdot is computed from unidentified workbook columns")
    print("- Full-WDM mixture closure remains OPEN until thermodynamics are explicit")


if __name__ == "__main__":
    main()
