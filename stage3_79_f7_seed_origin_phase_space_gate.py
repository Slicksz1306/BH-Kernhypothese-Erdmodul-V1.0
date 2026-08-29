#!/usr/bin/env python3
"""Stage 3.79 / F7 — seed-origin / solar-bound phase-space gate.

This script does NOT assume a specific primordial production mechanism. It asks
whether standard Galactic-halo PBHs, even with f_PBH=1, can populate the
terrestrial-zone phase space required by F6.

Three deliberately capture-friendly gates are evaluated:

1) Adiabatic bound-DM density around a forming Sun using the low-velocity
   phase-space formula of Oncins et al. (2022):

   rho_bd(r) = 4/(3 sqrt(pi)) * rho_h/sigma_h^3 * (G M_sun/r)^(3/2)

   with f_s=1.

2) Protostellar-cloud contraction upper bound using Eroshenko (2023)
   reference values R_i=7500 AU, t_d=6e4 yr, sigma_h=200 km/s,
   v_cap=0.5 km/s. Every low-speed geometrical entrant is counted as captured,
   and every low-speed trajectory gravitationally focused to q<1 AU is counted
   as a perfect terrestrial candidate. This is intentionally more optimistic
   than the real cloud dynamics.

3) Mature Sun+giant-planet captive phase-space density using Dehnen, Hands &
   Schoenrich (2022), their phase-space-mixed Jupiter/Saturn crossing model.
   At 1 AU we evaluate their equation (27) relative to the unbound number
   density for a Maxwellian sigma=200 km/s.

All results scale linearly with f_PBH, so f_PBH<1 only worsens the standard-halo
origin problem.
"""

from __future__ import annotations

from math import erf, exp, pi, sqrt
from scipy.integrate import quad

G = 6.67430e-11
M_SUN = 1.98847e30
M_EARTH = 5.9722e24
AU = 1.495978707e11
YR = 365.25 * 86400.0
PC = 3.085677581491367e16
MSUN_PER_PC3 = M_SUN / PC**3

# F6 reference gate
M_EMBRYO = 0.03 * M_EARTH
V_HILL = 4.212e26  # m^3, Stage 3.78 reference
MU_H_REQ_50 = 8.318
N_GLOBAL_MIN_F6 = 1.07e4  # most optimistic phase-mixed geometry in F6

# Canonical halo, deliberately allowing all DM to be PBHs.
RHO_HALO = 0.3 * 1.78266192e-27 / 1e-6  # 0.3 GeV/cm^3 -> kg/m^3
SIGMA_HALO = 200e3
F_PBH = 1.0
MASSES = (1e10, 1e11, 2e11, 5e11)


def rho_bound_adiabatic(r: float, rho_h: float = RHO_HALO,
                        sigma: float = SIGMA_HALO, f_s: float = 1.0) -> float:
    """Oncins et al. low-velocity phase-space bound-DM density."""
    return (4.0 * f_s / (3.0 * sqrt(pi)) * rho_h / sigma**3
            * (G * M_SUN / r)**1.5)


def maxwell_speed_pdf(v: float, sigma: float = SIGMA_HALO) -> float:
    return sqrt(2.0 / pi) * v*v / sigma**3 * exp(-v*v/(2.0*sigma*sigma))


def cloud_upper_counts(m_pbh: float) -> tuple[float, float]:
    """Extremely optimistic Eroshenko-like cloud upper bounds.

    Returns:
      any_low_speed_capture_upper,
      q_less_1au_candidate_upper
    """
    r_i = 7500.0 * AU
    t_d = 6e4 * YR
    v_cap = 0.5e3
    n_halo = F_PBH * RHO_HALO / m_pbh

    geom_rate_volume = quad(
        lambda v: pi * r_i*r_i * v * maxwell_speed_pdf(v), 0.0, v_cap
    )[0]

    # Point-Sun gravitational focusing is stronger than the distributed cloud
    # at the beginning of collapse, therefore this is a generous upper bound.
    inner_rate_volume = quad(
        lambda v: pi * AU*AU * (1.0 + 2.0*G*M_SUN/(AU*v*v))
                  * v * maxwell_speed_pdf(v),
        0.0, v_cap, points=[0.0]
    )[0]

    return n_halo * t_d * geom_rate_volume, n_halo * t_d * inner_rate_volume


def dehnen_bound_density_ratio_1au(sigma_kms: float = 200.0) -> float:
    """Equation (27) of Dehnen, Hands & Schoenrich 2022 at r=1 AU.

    Uses AU, yr units with G M_sun = 4 pi^2 AU^3/yr^2.
    Returns n_bound(1 AU) / n_unbound,far.
    """
    gm = 4.0*pi*pi
    r = 1.0
    a0, a1, a2 = 4.0, 20.0, 2000.0
    a_j, a_s = 5.2044, 9.5826
    kms_to_auyr = YR / (AU/1000.0)
    sig = sigma_kms * kms_to_auyr
    p0 = (2.0*pi*sig*sig)**(-1.5)

    def p(x: float) -> float:
        return max(0.0, x)

    bracket = (
        p(2/r - 1/a2)**1.5
        - p(2/r - 1/a0)**1.5
        - p(a_j*a_j/r**2 - 1.0)**0.5 * p(1/a0 - 2/(a_j+r))**1.5
        - p(1.0 - a_j*a_j/r**2)**0.5 * p(2/(a_j+r) - 1/a1)**1.5
        + p(1.0 - a_s*a_s/r**2)**0.5 * p(2/(a_s+r) - 1/a1)**1.5
        - p(1.0 - a_s*a_s/r**2)**0.5 * p(2/(a_s+r) - 1/a2)**1.5
    )
    return (4.0*pi/3.0) * gm**1.5 * p0 * bracket


def required_environment(m_pbh: float, rho_bd_canonical: float) -> tuple[float, float, float]:
    """Return phase-space boost, sigma needed at canonical rho, and rho needed at 1 km/s."""
    rho_req = MU_H_REQ_50 * m_pbh / V_HILL
    boost = rho_req / rho_bd_canonical
    merit_canonical = RHO_HALO / SIGMA_HALO**3
    merit_req = merit_canonical * boost
    sigma_req = (RHO_HALO / merit_req)**(1.0/3.0)
    rho_at_1kms = merit_req * (1e3)**3
    return boost, sigma_req, rho_at_1kms


def main() -> None:
    rho_bd = rho_bound_adiabatic(AU)
    ratio_plan = dehnen_bound_density_ratio_1au()

    print("Stage 3.79 / F7 — seed-origin phase-space gate")
    print(f"canonical halo rho = {RHO_HALO:.6e} kg/m^3")
    print(f"canonical halo sigma = {SIGMA_HALO/1e3:.1f} km/s")
    print(f"F6 required Hill occupancy mu_H,50 = {MU_H_REQ_50:.3f}")
    print(f"adiabatic rho_bd(1 AU) = {rho_bd:.6e} kg/m^3")
    print(f"Dehnen captive n_bound/n_halo at 1 AU = {ratio_plan:.6e}")
    print()

    header = (
        "Mkg,muH_adiabatic,shortfall_adiabatic,muH_planetary,shortfall_planetary,"
        "cloud_any_upper,cloud_q_lt_1AU_upper,cloud_shortfall_vs_F6_min,"
        "phase_space_boost_req,sigma_req_at_canonical_rho_m_s,"
        "rho_req_at_sigma_1kms_Msun_pc3"
    )
    print(header)

    for m in MASSES:
        n_halo = F_PBH * RHO_HALO / m
        mu_ad = rho_bd/m * V_HILL
        mu_plan = n_halo * ratio_plan * V_HILL
        cloud_any, cloud_inner = cloud_upper_counts(m)
        boost, sigma_req, rho_1 = required_environment(m, rho_bd)
        print(
            f"{m:.6e},{mu_ad:.6e},{MU_H_REQ_50/mu_ad:.6e},"
            f"{mu_plan:.6e},{MU_H_REQ_50/mu_plan:.6e},"
            f"{cloud_any:.6e},{cloud_inner:.6e},{N_GLOBAL_MIN_F6/cloud_inner:.6e},"
            f"{boost:.6e},{sigma_req:.6e},{rho_1/MSUN_PER_PC3:.6e}"
        )

    print("\nInterpretation")
    print("- standard Galactic-halo phase space misses the F6 terrestrial requirement by 8-10 orders")
    print("- protostellar collapse can bind many low-mass PBHs on wide orbits, but an extremely generous inner-1-AU upper bound still misses the minimum F6 global abundance")
    print("- mature giant-planet capture also inherits the low incoming halo phase-space density; steady captive density at 1 AU is far below F6")
    print("- a surviving origin requires a pre-existing co-moving/cold dark component with a vastly larger rho/sigma^3 than the canonical halo")
    print("- these are formation constraints only, not evidence for an Earth-centre black hole")


if __name__ == "__main__":
    main()
