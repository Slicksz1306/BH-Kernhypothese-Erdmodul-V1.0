#!/usr/bin/env python3
"""Stage 3.69A-2: external regression tests for the Schwarzschild-Dirac solver.

This module does not add new physics assumptions. It checks the Stage 3.69A-1
single-particle solver against published analytic/asymptotic results:

- Unruh low-energy absorption formula, quoted as Eq. (31) by Doran et al. (2005)
- matching-radius convergence in the true far zone p*r >> 1
- current/Wronskian conservation over very long low-momentum integrations

The purpose is deliberately adversarial: a benchmark that does not converge or
misses the published limit is a solver FAIL, not a physics result for H0.

Natural units G=hbar=c=1 and M=1 are used by the radial solver.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import pi, sqrt

import numpy as np
from scipy.integrate import solve_ivp

from stage3_69a1_dirac_prototype import (
    local_flux_modes,
    normalized_horizon_initial,
    rhs,
    unruh_low_energy_dimensionless,
    wronskian,
)


@dataclass(frozen=True)
class RegressionPoint:
    alpha: float
    E_over_m: float
    px_targets: tuple[float, ...]
    unruh_rel_tol: float
    radius_rel_tol: float


def momentum_dimensionless(alpha: float, E_over_m: float) -> float:
    """pM for M=1, with particle rest mass mM=alpha."""
    if E_over_m <= 1.0:
        raise ValueError("E/m must be > 1 for an unbound state")
    return alpha * sqrt(E_over_m * E_over_m - 1.0)


def speed_from_E_over_m(E_over_m: float) -> float:
    return sqrt(1.0 - 1.0 / (E_over_m * E_over_m))


def integrate_horizon_mode_segmented(
    alpha: float,
    speed_u: float,
    kappa: int,
    x_max: float,
    *,
    phase_chunk: float = 10.0,
    rtol: float = 5.0e-13,
    atol: float = 5.0e-15,
) -> tuple[np.ndarray, dict[str, float]]:
    """Integrate to a very large matching radius without cumulative flux drift.

    At small alpha and low momentum the physically required far zone can sit at
    x >> 1e5.  A single integration over that entire interval accumulates a
    small normalization error in the conserved Wronskian.  Because the radial
    equation is linear, multiplying the two-component solution by one common
    scalar changes neither its direction nor S=A_out/A_in.  We therefore split
    the far-zone integration into finite phase intervals and restore W=-1 after
    each segment.

    Crucially, the *raw pre-renormalization drift of every segment* is retained
    as the accuracy diagnostic.  Renormalization is not counted as evidence of
    current conservation by itself.
    """
    x, U, energy, mass = normalized_horizon_initial(alpha, speed_u, kappa)
    p = alpha * speed_u / sqrt(1.0 - speed_u * speed_u)

    max_segment_W_drift = 0.0
    n_segments = 0
    nfev = 0

    while x < x_max:
        dx_phase = phase_chunk / max(p, 1.0e-300)
        # Limit geometric growth close to the horizon; in the far zone the
        # phase interval controls the segment length.
        x_next = min(x_max, max(x + 10.0, min(1.5 * x, x + dx_phase)))

        W_before = wronskian(U, x)
        sol = solve_ivp(
            lambda xx, y: rhs(xx, y, kappa, energy, mass),
            (x, x_next),
            U,
            method="DOP853",
            rtol=rtol,
            atol=atol,
        )
        if not sol.success:
            raise RuntimeError(sol.message)

        U = sol.y[:, -1]
        nfev += sol.nfev
        W_after = wronskian(U, x_next)
        if W_after >= 0.0:
            raise RuntimeError("Inward-current solution changed current sign")

        segment_drift = abs((W_after - W_before) / W_before)
        max_segment_W_drift = max(max_segment_W_drift, segment_drift)

        # Restore the chosen W=-1 normalization.  S=Aout/Ain is invariant under
        # this common real rescaling.
        U = U / sqrt(-W_after)
        x = x_next
        n_segments += 1

    return U, {
        "max_segment_W_drift": max_segment_W_drift,
        "W_final": wronskian(U, x_max),
        "n_segments": float(n_segments),
        "nfev": float(nfev),
    }


def scattering_ratio_segmented(
    alpha: float,
    speed_u: float,
    kappa: int,
    x_match: float,
) -> tuple[complex, dict[str, float]]:
    Uh, integ_diag = integrate_horizon_mode_segmented(
        alpha,
        speed_u,
        kappa,
        x_match,
    )
    Uin, Uout = local_flux_modes(alpha, speed_u, kappa, x_match)
    Ain, Aout = np.linalg.solve(np.column_stack([Uin, Uout]), Uh)
    S = Aout / Ain

    return S, {
        **integ_diag,
        "Ain_abs2": float(abs(Ain) ** 2),
        "Aout_abs2": float(abs(Aout) ** 2),
        "absorption_probability": float(1.0 - abs(S) ** 2),
    }


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
        S, diag = scattering_ratio_segmented(alpha, u, kappa, x_match=x_match)
        p_abs = 1.0 - abs(S) ** 2
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
                "max_segment_W_drift": float(diag["max_segment_W_drift"]),
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
            *(d["max_segment_W_drift"] for d in diagnostics),
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
        "max_segment_W_drift": max_w_drift,
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

    print(f"max segment W drift : {result['max_segment_W_drift']:.3e}")
    print(f"last-radius change  : {result['radius_rel_last_two']:.3e}")
    print(f"Wronskian check     : {'PASS' if result['pass_W'] else 'FAIL'}")
    print(f"Unruh check         : {'PASS' if result['pass_unruh'] else 'FAIL'}")
    print(f"radius convergence  : {'PASS' if result['pass_radius'] else 'FAIL'}")
    print(f"POINT STATUS        : {'PASS' if result['PASS'] else 'FAIL'}")


def main() -> None:
    print("Stage 3.69A-2 Schwarzschild-Dirac external regression")
    print("A failed benchmark is a solver failure, not evidence for H0.")
    print("Note: this is deliberately a slow, high-accuracy regression run.")

    # The far-zone requirement is expressed as p*x_match rather than a fixed
    # coordinate radius.  This becomes essential as alpha and p decrease.
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
