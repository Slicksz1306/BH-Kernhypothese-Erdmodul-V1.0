#!/usr/bin/env python3
"""Stage 3.69A-3: Earth-speed proton Dirac capture + charge scales.

This script reuses the validated Schwarzschild-Dirac prototype from
stage3_69a1_dirac_prototype.py and adds two things:

1. a flux-stable absorption probability for very weak partial waves,
   avoiding catastrophic cancellation in 1-|S_kappa|^2;
2. an Earth-speed proton mass scan plus simple electrostatic charge scales.

Scope
-----
- isolated charged/uncharged particle benchmarks only;
- Schwarzschild geometry for the Dirac scan;
- no dense Fe/Ni transport, screening, nuclear reactions or full Mdot closure;
- no charged-Dirac/RN wave equation yet.

The charge formulas are classical force/equilibrium scales, not a final
Earth-core charge solution.
"""

from __future__ import annotations

from math import pi, sqrt

from stage3_69a1_dirac_prototype import (
    G,
    C,
    HBAR,
    M_E,
    M_P,
    alpha_g,
    classical_sigma_dimensionless,
    scattering_ratio,
)

EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19

V_EARTH = 10.4355e3
U_EARTH = V_EARTH / C


def absorption_probability_flux(alpha: float, speed_u: float, kappa: int, x_match: float) -> tuple[float, dict]:
    """Flux-stable P_abs from horizon current and incoming asymptotic flux.

    The prototype normalizes the horizon mode to W_H=-1.  With asymptotic
    incoming flux W_in=-2 q |A_in|^2, q=p/(E+m), current conservation gives

        P_abs = (-W_H)/(2 q |A_in|^2).

    This avoids subtracting two nearly equal numbers in 1-|S|^2 for weakly
    absorbed higher partial waves.
    """
    _, diag = scattering_ratio(alpha, speed_u, kappa, x_match=x_match)
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    mass = alpha
    energy = alpha * gamma
    p = alpha * speed_u * gamma
    q = p / (energy + mass)
    p_abs = (-diag["W_start"]) / (2.0 * q * diag["Ain_abs2"])
    return p_abs, diag


def sigma_abs_flux_stable(alpha: float, speed_u: float, kmax: int, x_match: float) -> tuple[float, list]:
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    p = alpha * speed_u * gamma
    total = 0.0
    rows = []
    for k in range(1, kmax + 1):
        for kappa in (-k, +k):
            p_abs, diag = absorption_probability_flux(alpha, speed_u, kappa, x_match)
            total += abs(kappa) * p_abs
            rows.append(
                {
                    "kappa": kappa,
                    "P_abs_flux": p_abs,
                    "P_abs_subtraction": diag["absorption_probability"],
                    "relative_W_drift": diag["relative_W_drift"],
                }
            )
    return pi * total / p**2, rows


def physical_sigma(M_bh_kg: float, sigma_over_M2: float) -> float:
    rg = G * M_bh_kg / C**2
    return sigma_over_M2 * rg**2


def proton_force_limit(M_bh_kg: float) -> tuple[float, float]:
    """Positive charge where Coulomb repulsion balances proton gravity."""
    q_coulomb = 4.0 * pi * EPS0 * G * M_bh_kg * M_P / E_CHARGE
    return q_coulomb / E_CHARGE, q_coulomb


def electron_force_limit(M_bh_kg: float) -> tuple[float, float]:
    """Magnitude of negative charge where Coulomb repulsion balances electron gravity."""
    q_coulomb = 4.0 * pi * EPS0 * G * M_bh_kg * M_E / E_CHARGE
    return q_coulomb / E_CHARGE, q_coulomb


def zajacek_equal_temperature_qeq(M_bh_kg: float) -> tuple[float, float]:
    """Stationary spherical equal-T plasma scale from Zajacek et al. (2018)."""
    q_coulomb = 2.0 * pi * EPS0 * G * (M_P - M_E) * M_bh_kg / E_CHARGE
    return q_coulomb / E_CHARGE, q_coulomb


def extremal_rn_charge(M_bh_kg: float) -> float:
    return sqrt(4.0 * pi * EPS0 * G) * M_bh_kg


def force_ratio_for_one_e(M_bh_kg: float, particle_mass: float) -> float:
    return (E_CHARGE**2 / (4.0 * pi * EPS0)) / (G * M_bh_kg * particle_mass)


def main() -> None:
    # kmax values were explicitly convergence-checked for this project scan.
    scan = [
        (1.0e10, 3, 5.0e6),
        (1.0e11, 3, 5.0e6),
        (2.0e11, 5, 2.0e6),
        (5.0e11, 9, 1.0e6),
    ]

    classical_dim = classical_sigma_dimensionless(U_EARTH)
    print("Stage 3.69A-3 Earth-speed proton Dirac capture")
    print(f"v={V_EARTH/1e3:.4f} km/s, u={U_EARTH:.12e}")
    print()
    print("M_kg, alpha_p, kmax, x_match, sigma/sigma_classical, sigma_m2")

    for M_bh, kmax, x_match in scan:
        alpha = alpha_g(M_bh, M_P)
        sigma_dim, _ = sigma_abs_flux_stable(alpha, U_EARTH, kmax, x_match)
        ratio = sigma_dim / classical_dim
        sigma_m2 = physical_sigma(M_bh, sigma_dim)
        print(f"{M_bh:.6e}, {alpha:.12e}, {kmax:d}, {x_match:.6e}, {ratio:.9f}, {sigma_m2:.12e}")

    print("\nMatching-radius spot check: M=1e11 kg, kmax=3")
    alpha = alpha_g(1.0e11, M_P)
    for x_match in (1.0e6, 5.0e6, 1.0e7):
        sigma_dim, _ = sigma_abs_flux_stable(alpha, U_EARTH, 3, x_match)
        print(f"x_match={x_match:.3e}: sigma/sigma_classical={sigma_dim/classical_dim:.9f}")

    M_ref = 1.0e11
    qp_e, qp_c = proton_force_limit(M_ref)
    qe_e, qe_c = electron_force_limit(M_ref)
    qeq_e, qeq_c = zajacek_equal_temperature_qeq(M_ref)
    qext_c = extremal_rn_charge(M_ref)

    print("\nCharge scales at M=1e11 kg")
    print(f"F_C/F_G for Q=+e on proton   = {force_ratio_for_one_e(M_ref, M_P):.9f}")
    print(f"F_C/F_G magnitude for |Q|=e on electron = {force_ratio_for_one_e(M_ref, M_E):.9f}")
    print(f"Q_max,p = {qp_e:.9f} e = {qp_c:.12e} C")
    print(f"|Q_max,e| = {qe_e:.9f} e = {qe_c:.12e} C")
    print(f"Q_eq(equal T, Zajacek) = {qeq_e:.9f} e = {qeq_c:.12e} C")
    print(f"Q_extremal,RN = {qext_c:.12e} C")
    print(f"Q_eq/Q_extremal = {qeq_c/qext_c:.12e}")

    print("\nInterpretation limits:")
    print("- neutral Earth-speed proton capture is now numerically evaluated;")
    print("- Unruh low-energy proton extrapolation is not used as the final value at alpha~0.35;")
    print("- charge feedback is dynamically important at tiny Q but not yet self-consistently solved;")
    print("- dense Fe/Ni screening/transport and net Mdot remain OPEN;")
    print("- H+ and H0 remain separate parallel branches.")


if __name__ == "__main__":
    main()
