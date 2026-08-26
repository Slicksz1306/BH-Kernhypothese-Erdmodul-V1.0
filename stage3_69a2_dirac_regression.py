#!/usr/bin/env python3
"""Stage 3.69A-2: external regression tests for the Schwarzschild-Dirac solver.

This module does not add new physics assumptions. It checks the Stage 3.69A-1
single-particle solver against published analytic/asymptotic results:

- Unruh low-energy absorption formula, quoted as Eq. (31) by Doran et al. (2005)
- matching-radius convergence in the true far zone p*r >> 1
- current/Wronskian conservation inherited from Stage 3.69A-1

The purpose is deliberately adversarial: a benchmark that does not converge or
misses the published limit is a solver FAIL, not a physics result for H0.

Natural units G=hbar=c=1 and M=1 are used by the radial solver.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt

from stage3_69a1_dirac_prototype import (
    scattering_ratio,
    unruh_low_energy_dimensionless,
)


@dataclass(frozen=True)
class RegressionPoint:
    alpha: float
    E_over_m: float
    px_targets: tuple[float, ...]
    unruh_rel_tol: float
    radius_rel_tol: float


def momentum_dimensionless(alpha: float, E_over_m: float) -> float:
    """p M for M=1, with particle rest mass mM=alpha."""
    if E_over_m <= 1.0:
        raise ValueError("E/m must be > 1 for an unbound state")
    return alpha * sqrt(E_over_m * E_over_m - 1.0)


def speed_from_E_over_m(E_over_m: float) -> float:
    return sqrt(1.0 - 1.0 / (E_over_m * E_over_m))


def lowest_j_half_sigma(
    alpha: float,
    E_over_m: float,
    x_match: float,
) -> tuple[float, list[dict[str, float]]]:
    """Numerical sigma/M^2 from the two |kappa|=1 modes only.

    Doran et al. state that these modes dominate the low-energy regime in which
    Unruh's analytic approximation applies. Comparing like-for-like avoids
    contaminating the benchmark with higher partial waves outside the strict
    approximation.
    """
    u = speed_from_E_over_m(E_over_m)
    p = momentum_dimensionless(alpha, E_over_m)

    total = 0.0
    diagnostics: list[dict[str, float]] = []
    for kappa in (-1, +1):
        S, diag = scattering_ratio(alpha, u, kappa, x_match=x_match)
        p_abs = 1.0 - abs(S) ** 2
        # Tiny negative values may occur from floating-point roundoff only.
        if p_abs < -1.0e-8:
            raise RuntimeError(
                f"Unphysical absorption probability for kappa={kappa}: {p_abs}"
            )
        p_abs = max(0.0, p_abs)
        total += abs(kappa) * p_abs
        diagnostics.append(
            {
                "kappa": float(kappa),
                "P_abs": p_abs,
                "relative_W_drift": float(diag["relative_W_drift"]),
            }
        )

    return pi * total / (p * p), diagnostics


def run_point(point: RegressionPoint) -> dict[str, object]:
    p = momentum_dimensionless(point.alpha, point.E_over_m)
    u = speed_from_E_over_m(point.E_over_m)
    unruh = unruh_low_energy_dimensionless(point.alpha, u)

    rows: list[dict[str, float]] = []
    max_w_drift = 0.0
    for px in point.px_targets:
        x_match = px / p
        sigma, diagnostics = lowest_j_half_sigma(
            point.alpha,
            point.E_over_m,
            x_match=x_match,
        )
        max_w_drift = max(
            max_w_drift,
            *(d["relative_W_drift"] for d in diagnostics),
        )
        rows.append(
            {
                "p_x": px,
                "x_match": x_match,
                "sigma_numeric": sigma,
                "sigma_unruh": unruh,
                "rel_to_unruh": abs(sigma / unruh - 1.0),
            }
        )

    last = rows[-1]
    previous = rows[-2]
    radius_rel = abs(last["sigma_numeric"] / previous["sigma_numeric"] - 1.0)

    pass_w = max_w_drift < 1.0e-8
    pass_unruh = last["rel_to_unruh"] < point.unruh_rel_tol
    pass_radius = radius_rel < point.radius_rel_tol

    return {
        "point": point,
        "rows": rows,
        "max_W_drift": max_w_drift,
        "radius_rel_last_two": radius_rel,
        "pass_W": pass_w,
        "pass_unruh": pass_unruh,
        "pass_radius": pass_radius,
        "PASS": pass_w and pass_unruh and pass_radius,
    }


def print_result(result: dict[str, object]) -> None:
    point = result["point"]
    assert isinstance(point, RegressionPoint)

    print(
        f"\nalpha={point.alpha:g}, E/m={point.E_over_m:g}, "
        f"p={momentum_dimensionless(point.alpha, point.E_over_m):.9e}"
    )
    print("p*x_match        x_match        sigma_num      sigma_Unruh    rel.err")
    for row in result["rows"]:
        print(
            f"{row['p_x']:9.1f}  {row['x_match']:13.3f}  "
            f"{row['sigma_numeric']:13.8f}  {row['sigma_unruh']:13.8f}  "
            f"{row['rel_to_unruh']:9.3e}"
        )

    print(f"max relative W drift : {result['max_W_drift']:.3e}")
    print(f"last-radius change   : {result['radius_rel_last_two']:.3e}")
    print(f"Wronskian check      : {'PASS' if result['pass_W'] else 'FAIL'}")
    print(f"Unruh check          : {'PASS' if result['pass_unruh'] else 'FAIL'}")
    print(f"radius convergence   : {'PASS' if result['pass_radius'] else 'FAIL'}")
    print(f"POINT STATUS         : {'PASS' if result['PASS'] else 'FAIL'}")


def main() -> None:
    print("Stage 3.69A-2 Schwarzschild-Dirac external regression")
    print("A failed benchmark is a solver failure, not evidence for H0.")

    # These points are intentionally in the low-energy / long-wavelength regime
    # shown by Doran et al. to follow Unruh's approximation.  The far-zone
    # requirement is expressed as p*x_match rather than a fixed coordinate radius;
    # this is essential when alpha and therefore p become small.
    points = (
        RegressionPoint(
            alpha=0.01,
            E_over_m=1.10,
            px_targets=(500.0, 1000.0, 2000.0),
            unruh_rel_tol=0.03,
            radius_rel_tol=0.01,
        ),
        RegressionPoint(
            alpha=0.005,
            E_over_m=1.20,
            px_targets=(1000.0, 2000.0),
            unruh_rel_tol=0.02,
            radius_rel_tol=0.01,
        ),
    )

    results = [run_point(p) for p in points]
    for result in results:
        print_result(result)

    overall = all(bool(r["PASS"]) for r in results)
    print(f"\nOVERALL EXTERNAL REGRESSION: {'PASS' if overall else 'FAIL'}")
    if not overall:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
