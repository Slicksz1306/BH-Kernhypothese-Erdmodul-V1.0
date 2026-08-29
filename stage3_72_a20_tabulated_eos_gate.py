#!/usr/bin/env python3
"""Stage 3.72 / A20: tabulated-isentrope ingestion gate for the SL/BH Earth module.

Purpose
-------
This script is the direct-data counterpart to A13/A13b. It accepts a monotonic
pressure-density table, reconstructs the relativistic specific enthalpy along
the isentrope, and tests whether the table by itself spans a regular Michel
critical point.

It deliberately refuses uncontrolled extrapolation. If the critical point lies
outside the measured density range, the result is DATA RANGE INSUFFICIENT,
not a guessed Mdot.

Expected CSV columns
--------------------
rho_gcc,P_GPa

Optional columns such as T_K or uncertainties may be present; they are ignored
by the minimal solver unless a future closure explicitly uses them.

Scientific status
-----------------
- Grant et al. (2021) measured elevated liquid-Fe isentropes in the roughly
  220--398 GPa range (main robust high-pressure shot Z3155; Z3339 has a
  non-converging high-density section).
- The public record is DOI 10.5281/zenodo.4464112.
- No points from figures are digitized or invented here.
- SESAME 92141 is not redistributed by this project.
"""

from __future__ import annotations

import argparse
import csv
from dataclasses import dataclass
from math import pi, sqrt
from pathlib import Path

import numpy as np
from scipy.integrate import cumulative_trapezoid
from scipy.interpolate import PchipInterpolator
from scipy.optimize import brentq

G = 6.67430e-11
C = 299_792_458.0

# PREM center boundary used throughout A12c/A13/A13b.
RHO_INF = 13_088.48          # kg/m^3
P_INF = 3638.521e8           # Pa
T_INF = 6000.0               # K, reference sensitivity
CP_INF = 850.0               # J/kg/K
H_INF = 1.0 + (CP_INF * T_INF + P_INF / RHO_INF) / C**2


@dataclass
class CriticalState:
    rho: float
    P: float
    h: float
    dPdrho: float
    a2: float
    u: float
    r_over_M: float
    mdot: float


class TabulatedIsentrope:
    """Monotonic P(rho) isentrope with no extrapolation.

    The interpolation is shape-preserving (PCHIP). Relativistic enthalpy is
    reconstructed from

        dh = dP / (rho c^2).

    The local sound speed entering Michel is

        a^2/c^2 = (dP/drho) / (h c^2).
    """

    def __init__(self, rho_kgm3: np.ndarray, P_pa: np.ndarray,
                 h_at_first_point: float = H_INF):
        rho = np.asarray(rho_kgm3, dtype=float)
        P = np.asarray(P_pa, dtype=float)
        if rho.ndim != 1 or P.ndim != 1 or len(rho) != len(P):
            raise ValueError("rho and P must be one-dimensional arrays of equal length")
        if len(rho) < 4:
            raise ValueError("need at least four tabulated points")
        if not np.all(np.isfinite(rho)) or not np.all(np.isfinite(P)):
            raise ValueError("non-finite table entry")

        order = np.argsort(rho)
        rho, P = rho[order], P[order]
        if np.any(np.diff(rho) <= 0):
            raise ValueError("density must be strictly increasing")
        if np.any(np.diff(P) <= 0):
            raise ValueError("pressure must be strictly increasing along this isentrope")

        self.rho = rho
        self.P = P
        self._P = PchipInterpolator(rho, P, extrapolate=False)
        self._dP = self._P.derivative()

        dPdrho_nodes = self._dP(rho)
        if np.any(dPdrho_nodes <= 0):
            raise ValueError("interpolated dP/drho is non-positive")

        integrand = dPdrho_nodes / (rho * C**2)
        h_nodes = h_at_first_point + np.concatenate(
            ([0.0], cumulative_trapezoid(integrand, rho))
        )
        self._h = PchipInterpolator(rho, h_nodes, extrapolate=False)

    @property
    def rho_min(self) -> float:
        return float(self.rho[0])

    @property
    def rho_max(self) -> float:
        return float(self.rho[-1])

    def state(self, rho: float) -> tuple[float, float, float, float]:
        if not (self.rho_min <= rho <= self.rho_max):
            raise ValueError("requested density is outside tabulated range")
        P = float(self._P(rho))
        dPdrho = float(self._dP(rho))
        h = float(self._h(rho))
        a2 = dPdrho / (h * C**2)
        if not (0.0 < a2 < 1.0):
            raise ValueError(f"non-causal/invalid sound speed a2={a2}")
        return P, h, dPdrho, a2

    def critical_residual(self, rho: float) -> float:
        _, h, _, a2 = self.state(rho)
        return h / sqrt(1.0 + 3.0 * a2) - H_INF

    def critical_roots(self) -> list[float]:
        grid = np.geomspace(self.rho_min * (1.0 + 1e-12),
                            self.rho_max * (1.0 - 1e-12), 5000)
        vals = []
        for r in grid:
            try:
                vals.append(self.critical_residual(r))
            except ValueError:
                vals.append(np.nan)
        vals = np.asarray(vals)
        roots: list[float] = []
        for i in range(len(grid) - 1):
            a, b = vals[i], vals[i + 1]
            if not (np.isfinite(a) and np.isfinite(b)):
                continue
            if a == 0.0:
                roots.append(float(grid[i]))
            elif a * b < 0.0:
                root = brentq(self.critical_residual, grid[i], grid[i + 1],
                              xtol=1e-12, rtol=1e-11)
                if not roots or abs(np.log(root / roots[-1])) > 1e-8:
                    roots.append(float(root))
        return roots

    def critical_state(self, M_kg: float) -> CriticalState:
        roots = self.critical_roots()
        if len(roots) == 0:
            raise RuntimeError(
                "DATA RANGE INSUFFICIENT: no regular Michel critical root is "
                "contained inside the supplied density range; extrapolation refused"
            )
        if len(roots) != 1:
            raise RuntimeError(f"table contains {len(roots)} candidate critical roots")
        rho = roots[0]
        P, h, dPdrho, a2 = self.state(rho)
        u = sqrt(a2 / (1.0 + 3.0 * a2))
        r_over_M = (1.0 + 3.0 * a2) / (2.0 * a2)
        r = (G * M_kg / C**2) * r_over_M
        mdot = 4.0 * pi * r**2 * rho * C * u
        return CriticalState(rho, P, h, dPdrho, a2, u, r_over_M, mdot)


def read_csv(path: Path) -> tuple[np.ndarray, np.ndarray]:
    rho, P = [], []
    with path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV has no header")
        required = {"rho_gcc", "P_GPa"}
        if not required.issubset(set(reader.fieldnames)):
            raise ValueError(f"CSV must contain columns {sorted(required)}")
        for row in reader:
            rho.append(float(row["rho_gcc"]) * 1000.0)
            P.append(float(row["P_GPa"]) * 1e9)
    return np.asarray(rho), np.asarray(P)


def synthetic_regression() -> float:
    """Regression of the tabulated machinery against A13 beta=1.5.

    The expected A13 value at 1e11 kg is about 3.2237e-6 kg/s. This test
    verifies ingestion/interpolation/enthalpy/critical-root machinery without
    pretending that synthetic points are experimental Fe data.
    """
    beta = 1.5
    B0 = 14253.0e8
    rho0 = RHO_INF
    P0 = P_INF
    rho = np.geomspace(rho0, rho0 * 1e12, 5000)
    P = P0 + B0 / beta * ((rho / rho0)**beta - 1.0)
    eos = TabulatedIsentrope(rho, P)
    st = eos.critical_state(1e11)
    target = 3.22370e-6
    rel = st.mdot / target - 1.0
    print("synthetic A13 beta=1.5 regression")
    print(f"Mdot={st.mdot:.12e} kg/s target~{target:.12e} rel={rel:+.3e}")
    if abs(rel) > 2e-4:
        raise RuntimeError("tabulated-EOS regression failed")
    return rel


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("csv", nargs="?", type=Path,
                    help="CSV with rho_gcc,P_GPa columns")
    ap.add_argument("--mass", type=float, default=1e11,
                    help="BH mass in kg (default 1e11)")
    args = ap.parse_args()

    synthetic_regression()

    if args.csv is None:
        print("\nNo experimental CSV supplied.")
        print("Status: INGESTION MACHINERY PASS; RAW GRANT/SESAME DATA CLOSURE OPEN")
        return

    rho, P = read_csv(args.csv)
    eos = TabulatedIsentrope(rho, P)
    print("\ninput table")
    print(f"N={len(rho)}")
    print(f"rho={rho.min()/1000:.6f}...{rho.max()/1000:.6f} g/cm3")
    print(f"P={P.min()/1e9:.6f}...{P.max()/1e9:.6f} GPa")

    try:
        st = eos.critical_state(args.mass)
    except RuntimeError as exc:
        print(str(exc))
        print("Result: measured/tabulated range alone does not close Michel supply")
        return

    print("\nregular critical point contained in supplied table")
    print(f"rho_crit={st.rho/1000:.9e} g/cm3")
    print(f"P_crit={st.P/1e9:.9e} GPa")
    print(f"a2_crit={st.a2:.9e}")
    print(f"rcrit/M={st.r_over_M:.9e}")
    print(f"Mdot={st.mdot:.12e} kg/s")
    print("Result applies only if the supplied table is a physically appropriate continuous isentrope.")


if __name__ == "__main__":
    main()
