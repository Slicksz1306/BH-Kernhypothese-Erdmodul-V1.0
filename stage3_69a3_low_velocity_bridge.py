#!/usr/bin/env python3
"""Stage 3.69A-3: Earth low-velocity single-particle bridge.

This is a benchmark layer between the validated Schwarzschild-Dirac solver and
the dense-matter Earth closure.  It compares Unruh's low-energy spin-1/2
absorption approximation with the classical collisionless point-particle cross
section at Earth-core-like velocities.

Important scope limit:
- Results are isolated spin-1/2 single-particle benchmarks.
- They are NOT a dense Fe/Ni accretion rate.
- Bound nuclei, ionization/dissociation, collisions, screening and charge
  feedback remain separate closure problems.
"""

from __future__ import annotations

from math import expm1, log1p, pi, sqrt

from stage3_69a1_dirac_prototype import (
    C,
    M_E,
    M_P,
    alpha_g,
    unruh_low_energy_dimensionless,
)


V_REF = 10.4355e3  # m/s; project reference effective low velocity
U_REF = V_REF / C


def classical_sigma_dimensionless_stable(speed_u: float) -> float:
    """Doran et al. Eq. (3), evaluated without low-u cancellation.

    Direct evaluation of
        -1 + (1 + 8 u^2)^(3/2)
    loses precision for u << 1.  expm1/log1p keep the small difference stable.
    """
    u = speed_u
    if not (0.0 < u < 1.0):
        raise ValueError("speed_u must satisfy 0 < u < 1")
    u2 = u * u
    delta = expm1(1.5 * log1p(8.0 * u2))
    numerator = 8.0 * u2 * u2 + 20.0 * u2 + delta
    return pi * numerator / (2.0 * u2 * u2)


def single_particle_ratio(M_bh_kg: float, particle_mass_kg: float, speed_u: float = U_REF):
    alpha = alpha_g(M_bh_kg, particle_mass_kg)
    sigma_q = unruh_low_energy_dimensionless(alpha, speed_u)
    sigma_cl = classical_sigma_dimensionless_stable(speed_u)
    return alpha, sigma_q, sigma_cl, sigma_q / sigma_cl


def find_mass_for_ratio_one(
    particle_mass_kg: float,
    lo_kg: float,
    hi_kg: float,
    speed_u: float = U_REF,
    iterations: int = 100,
) -> float:
    """Bisection for sigma_Unruh/sigma_classical = 1."""
    r_lo = single_particle_ratio(lo_kg, particle_mass_kg, speed_u)[3] - 1.0
    r_hi = single_particle_ratio(hi_kg, particle_mass_kg, speed_u)[3] - 1.0
    if r_lo * r_hi > 0.0:
        raise ValueError("Bisection interval does not bracket ratio=1")

    lo = lo_kg
    hi = hi_kg
    for _ in range(iterations):
        mid = 0.5 * (lo + hi)
        r_mid = single_particle_ratio(mid, particle_mass_kg, speed_u)[3] - 1.0
        if r_lo * r_mid <= 0.0:
            hi = mid
            r_hi = r_mid
        else:
            lo = mid
            r_lo = r_mid
    return 0.5 * (lo + hi)


def main() -> None:
    print("Stage 3.69A-3 low-velocity isolated-particle bridge")
    print(f"v_ref = {V_REF/1e3:.4f} km/s, u = {U_REF:.9e}")
    print()

    masses = (1.0e11, 2.0e11, 2.832e11, 3.6e11, 4.0e11, 5.0e11)
    print(
        "M_BH[kg]        alpha_p      U/C_p       alpha_e       U/C_e"
    )
    for M in masses:
        ap, _, _, rp = single_particle_ratio(M, M_P)
        ae, _, _, re = single_particle_ratio(M, M_E)
        print(f"{M:11.4e}  {ap:11.6e}  {rp:10.6e}  {ae:11.6e}  {re:10.6e}")

    mp_cross = find_mass_for_ratio_one(M_P, 1.0e11, 6.0e11)
    me_cross = find_mass_for_ratio_one(M_E, 1.0e14, 1.0e15)

    print()
    print("sigma_Unruh / sigma_classical = 1 crossings")
    print(f"proton   : M_BH = {mp_cross:.9e} kg")
    print(f"electron : M_BH = {me_cross:.9e} kg")

    print()
    print("Interpretation boundary:")
    print("These ratios are single-particle low-energy benchmarks only.")
    print("They must not be promoted directly to dense-core net Mdot_H0.")


if __name__ == "__main__":
    main()
