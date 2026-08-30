"""Stage 3.95E - A35 closure capability audit.

This module evaluates the *release bookkeeping* for a real A35 Q_eq solver.
It does not invent closures, coefficients, or physical data.
"""

from __future__ import annotations

import csv
from pathlib import Path

ALLOWED_CLASSES = {
    "DATA-CLOSED",
    "DERIVABLE",
    "THEORY-CLOSED",
    "MODEL-DEPENDENT",
    "SENSITIVITY-ONLY",
    "CURRENTLY UNAVAILABLE",
}

DEFAULT_MATRIX = Path("research/stage3_95e_a35_closure_capability_matrix.csv")


def load_matrix(path: Path = DEFAULT_MATRIX) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as handle:
        rows = list(csv.DictReader(handle))
    if not rows:
        raise ValueError("closure matrix is empty")
    return rows


def validate_matrix(rows: list[dict[str, str]]) -> None:
    ids = [row["closure_id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("closure_id values must be unique")

    for row in rows:
        if row["current_class"] not in ALLOWED_CLASSES:
            raise ValueError(
                f"{row['closure_id']}: invalid class {row['current_class']}"
            )
        if row["mandatory_for_real_qeq"] not in {"yes", "conditional", "no"}:
            raise ValueError(f"{row['closure_id']}: invalid mandatory flag")
        if row["blocks_solver_now"] not in {"yes", "no"}:
            raise ValueError(f"{row['closure_id']}: invalid blocker flag")

    by_id = {row["closure_id"]: row for row in rows}

    # Hard anti-proxy invariants inherited from Stage 3.95B/C.
    if by_id["A35-LST"]["current_class"] in {"DATA-CLOSED", "THEORY-CLOSED"}:
        raise ValueError("A35-LST may not be promoted from self-diffusion proxies")
    if by_id["A35-ELECTRON"]["current_class"] == "DATA-CLOSED":
        raise ValueError("conductivity alone may not close the electron operator")
    if by_id["A35-MQ"]["current_class"] == "THEORY-CLOSED":
        raise ValueError("Q_bullet -> Q_m matching is not yet theory-closed")
    if by_id["A35-K"]["current_class"] == "THEORY-CLOSED":
        raise ValueError("capture/sink microphysics is not yet theory-closed")


def evaluate_solver_release(rows: list[dict[str, str]]) -> dict[str, object]:
    validate_matrix(rows)
    blockers = [
        row["closure_id"]
        for row in rows
        if row["blocks_solver_now"] == "yes"
    ]
    ready = [
        row["closure_id"]
        for row in rows
        if row["blocks_solver_now"] == "no"
    ]
    return {
        "interface_count": len(rows),
        "release_ready_interface_count": len(ready),
        "blocking_interface_count": len(blockers),
        "blocking_interfaces": blockers,
        "solver_release_gate": "PASSED" if not blockers else "NOT PASSED",
        "real_q_eq_implementation": "GO" if not blockers else "NO-GO",
        "physical_closure": "CLOSED" if not blockers else "OPEN",
        "experimental_bh_evidence": "NONE",
    }


if __name__ == "__main__":
    result = evaluate_solver_release(load_matrix())
    for key, value in result.items():
        print(f"{key}: {value}")
