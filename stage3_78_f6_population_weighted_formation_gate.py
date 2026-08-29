#!/usr/bin/env python3
"""Stage 3.78 / F6 — population-weighted formation gate.

This script folds the Stage 3.77/F5 conditional exchange-capture kernel with
an explicitly parameterized local seed abundance and encounter count.

It does NOT assume a known primordial solar-bound seed population. Instead it
inverts the problem: what seed occupancy / local number density / global seed
abundance is required to reach a chosen Earth-delivery probability?

Reference kernel
----------------
F5 STRONG persistent stable capture:
    K_F5 = 5/300 = 1.6667e-2

Reference nuisance choices (editable):
    N_enc   = 10 relevant strong embryo encounters
    S_post  = 0.5 post-capture survival/engulfment factor
    P_goal  = 0.5

The core Poisson model is
    lambda = N_enc * K_F5 * S_post * n_seed * V_H
    P_del  = 1 - exp(-lambda)

Hence the required mean number of eligible seeds inside the Proto-Earth Hill
sphere at a relevant encounter epoch is
    mu_H = -ln(1-P_goal)/(N_enc*K_F5*S_post).

For a phase-mixed 3-D population, n_seed = mu_H / V_H.
"""

from __future__ import annotations

import argparse
import math

AU = 1.495978707e11
M_SUN = 1.98847e30
M_EARTH = 5.9722e24
K_F5_STRONG = 5.0 / 300.0
K_F5_BROAD = 3.0 / 300.0
RHO_DM_GAL = 0.3 * 1.78266192e-27 / 1.0e-6  # 0.3 GeV/cm^3 -> kg/m^3
RHO_BENNU_2024 = 3.3e-15  # kg/m^3 near ~1.1 AU; smooth-profile comparison only


def hill_radius(m1_earth: float, a_au: float = 1.0) -> float:
    return a_au * AU * ((m1_earth * M_EARTH) / (3.0 * M_SUN)) ** (1.0 / 3.0)


def hill_volume(m1_earth: float, a_au: float = 1.0) -> float:
    r = hill_radius(m1_earth, a_au)
    return 4.0 * math.pi * r**3 / 3.0


def required_mu_hill(
    p_goal: float,
    n_enc: float,
    k_capture: float,
    s_post: float,
) -> float:
    return -math.log(1.0 - p_goal) / (n_enc * k_capture * s_post)


def required_local_density(
    mbh_kg: float,
    m1_earth: float,
    p_goal: float,
    n_enc: float,
    k_capture: float,
    s_post: float,
) -> tuple[float, float, float]:
    mu = required_mu_hill(p_goal, n_enc, k_capture, s_post)
    n_seed = mu / hill_volume(m1_earth)
    return mu, n_seed, n_seed * mbh_kg


def hill_duty_proxy(m1_earth: float, width_au: float, i_deg: float) -> float:
    """Geometric phase-mixed Hill occupancy proxy around a=1 AU.

    Thin-disk limit H <= r_H:
        f_H ~ pi r_H^2 / (2 pi a Delta-a) = r_H^2/(2 a Delta-a)

    3-D torus limit H > r_H, with half-thickness H=a sin(i):
        f_H ~ (4 pi r_H^3 / 3)/(4 pi a Delta-a H)
            = r_H^3/(3 a Delta-a H).

    This is a geometry proxy, not a resonant/co-orbital capture model.
    """
    r = hill_radius(m1_earth) / AU
    a = 1.0
    h = a * math.sin(math.radians(i_deg))
    if h <= r:
        f = r * r / (2.0 * a * width_au)
    else:
        f = r**3 / (3.0 * a * width_au * h)
    return min(1.0, max(0.0, f))


def required_global_seeds(
    m1_earth: float,
    width_au: float,
    i_deg: float,
    p_goal: float,
    n_enc: float,
    k_capture: float,
    s_post: float,
) -> tuple[float, float]:
    f_h = hill_duty_proxy(m1_earth, width_au, i_deg)
    n_req = -math.log(1.0 - p_goal) / (n_enc * k_capture * s_post * f_h)
    return f_h, n_req


def probability_from_local_density(
    rho_seed: float,
    mbh_kg: float,
    m1_earth: float,
    n_enc: float,
    k_capture: float,
    s_post: float,
) -> float:
    n_seed = rho_seed / mbh_kg
    lam = n_enc * k_capture * s_post * n_seed * hill_volume(m1_earth)
    return 1.0 - math.exp(-lam)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--m1", type=float, default=0.03, help="Proto-Earth mass in Earth masses")
    ap.add_argument("--nenc", type=float, default=10.0, help="number of relevant F5-like encounters")
    ap.add_argument("--survive", type=float, default=0.5, help="post-capture survival/engulfment factor")
    ap.add_argument("--pgoal", type=float, default=0.5, help="target delivery probability")
    args = ap.parse_args()

    k = K_F5_STRONG
    r_h = hill_radius(args.m1)
    v_h = hill_volume(args.m1)
    mu = required_mu_hill(args.pgoal, args.nenc, k, args.survive)

    print("Stage 3.78 / F6 — population-weighted formation gate")
    print(f"M1 = {args.m1:.5g} M_E")
    print(f"r_H = {r_h/1e3:.6g} km")
    print(f"V_H = {v_h:.6e} m^3")
    print(f"K_F5,strong = {k:.8f}")
    print(f"N_enc = {args.nenc:g}")
    print(f"S_post = {args.survive:g}")
    print(f"P_goal = {args.pgoal:g}")
    print(f"required mean eligible seeds in Hill sphere mu_H = {mu:.6g}")

    print("\nRequired local density")
    print("M_BH_kg,n_seed_m^-3,rho_seed_kg_m^-3,overdensity_vs_0p3GeVcm3,rho_over_Bennu2024")
    for mbh in (1e10, 1e11, 2e11, 5e11):
        _, n_seed, rho = required_local_density(
            mbh, args.m1, args.pgoal, args.nenc, k, args.survive
        )
        print(f"{mbh:.6e},{n_seed:.12e},{rho:.12e},{rho/RHO_DM_GAL:.12e},{rho/RHO_BENNU_2024:.12e}")

    print("\nEncounter-count sensitivity for 50% target")
    print("N_enc,mu_H_50")
    for n_enc in (1, 3, 10, 30, 100):
        print(f"{n_enc},{required_mu_hill(0.5,n_enc,k,args.survive):.12e}")

    print("\nReference global abundance scenarios at M1=0.03 M_E")
    r_ref_au = hill_radius(0.03) / AU
    scenarios = (
        ("coorbital_razor_cold", 2.0 * r_ref_au, 0.01),
        ("ultra_cold_annulus", 0.02, 0.05),
        ("cold_inner_disk", 0.10, 0.50),
        ("warm_broad_disk", 0.50, 2.00),
    )
    print("scenario,width_AU,i_deg,f_H,N_seed_50,total_mass_if_1e11kg")
    for name, width, inc in scenarios:
        f_h, n_req = required_global_seeds(
            0.03, width, inc, 0.5, args.nenc, k, args.survive
        )
        print(f"{name},{width:.9e},{inc:.6g},{f_h:.12e},{n_req:.12e},{n_req*1e11:.12e}")

    print("\nCurrent-density comparison (NOT a primordial bound)")
    for mbh in (1e10, 1e11, 2e11, 5e11):
        p = probability_from_local_density(
            RHO_BENNU_2024, mbh, args.m1, args.nenc, k, args.survive
        )
        print(f"M={mbh:.3e} kg -> P_if_current_Bennu_density_were_primordial={p:.8f}")

    print("\nInterpretation")
    print("- F5 local exchange capture survives population folding only if a substantial eligible solar-bound seed population exists.")
    print("- Standard Galactic-halo density is far too small; the required local overdensity is mass dependent and can reach millions of times the Galactic DM density.")
    print("- Present-day ephemeris density limits are only a comparison benchmark: F6 concerns the early Solar System, and the seed population may have been depleted/ejected.")
    print("- The dominant unresolved quantity is the physical origin and phase-space distribution of the solar-bound cold seeds.")


if __name__ == "__main__":
    main()
