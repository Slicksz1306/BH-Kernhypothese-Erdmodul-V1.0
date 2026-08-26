#!/usr/bin/env python3
"""Stage 3.69B / A-6 reduced kinetic recycling + composition closure.

Purpose
-------
This is a reduced Earth-core bridge model between the already-calculated
single-particle/wave sink and the outer Michel/Bondi supply.

It does NOT claim a final dense-matter Mdot. Instead it tests whether a
persistent "single-pass only" suppression is self-consistent once:
- the Bondi radius is collisional,
- the flow becomes kinetic only deep inside r_B,
- missed particles can recycle,
- density pile-up shortens the local mean free path,
- Fe/Ni nuclei remain coherent at the kinetic-transition scale.

The loss-cone/recycling diagnostics follow the structure of Appendix B in
Cantiello et al. (2026), but all numerical inputs here are Earth-project
proxies and are NOT transplanted from the stellar calculation.
"""

from __future__ import annotations

from math import pi, sqrt

G = 6.67430e-11
C = 299_792_458.0
HBAR = 1.054571817e-34
EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19
M_E = 9.1093837139e-31
M_P = 1.67262192595e-27
AMU = 1.66053906660e-27

M_BH = 1.0e11
RHO_INF = 13_088.5
C_INF = 10.4355e3
GAMMA_PROXY = 5.0 / 3.0

Z_FE = 26.0
A_FE = 56.0
Z_NI = 28.0
A_NI = 58.0

MICHEL_LOW = 1.47e-8
MICHEL_HIGH = 1.46e-7
YEAR = 365.25 * 86400.0
EARTH_AGE = 4.54e9 * YEAR

MASS_FE56_U = 55.9349421
MASS_MN56_U = 55.9389094
MASS_NI58_U = 57.9353429
MASS_CO58_U = 57.9357576
U_MEV = 931.49410242


def base_scales() -> dict:
    m_ion = A_FE * AMU
    n_i = RHO_INF / m_ion
    n_e = Z_FE * n_i
    a_i = (3.0 / (4.0 * pi * n_i)) ** (1.0 / 3.0)

    # Geometric strongly-coupled/atomic collision-length proxy.
    sigma_geom = pi * a_i**2
    lambda_geom = 1.0 / (sqrt(2.0) * n_i * sigma_geom)

    # Thomas-Fermi screening scale (NOT a collision mean free path).
    k_F = (3.0 * pi**2 * n_e) ** (1.0 / 3.0)
    p_F = HBAR * k_F
    E_F = p_F**2 / (2.0 * M_E)
    lambda_TF = sqrt(2.0 * EPS0 * E_F / (3.0 * n_e * E_CHARGE**2))

    r_B = G * M_BH / C_INF**2
    r_s = 2.0 * G * M_BH / C**2
    ell_crit = 4.0 * G * M_BH / C

    return {
        "n_i": n_i,
        "n_e": n_e,
        "a_i": a_i,
        "lambda_geom": lambda_geom,
        "lambda_TF": lambda_TF,
        "E_F0": E_F,
        "r_B": r_B,
        "r_s": r_s,
        "ell_crit": ell_crit,
    }


S = base_scales()


def inner_adiabatic_proxy(r: float) -> dict:
    """Simple r << r_B adiabatic Bondi scalings used only as a bridge proxy."""
    x = S["r_B"] / r
    rho = RHO_INF * x**1.5
    c_s = C_INF * sqrt(x)
    sigma_perp = c_s / sqrt(GAMMA_PROXY)
    v_ff = sqrt(2.0 * G * M_BH / r)

    ell_typ = r * sigma_perp
    f_cap = 0.5 * (S["ell_crit"] / ell_typ) ** 2
    xi_direct = 2.0 / f_cap

    # If the unperturbed transition is defined by Kn~1 and lambda ∝ rho^-1,
    # the direct-only pile-up would imply Kn_eff~1/xi.
    kn_eff_direct = 1.0 / xi_direct

    # Degenerate-electron proxy under rho ∝ r^-3/2:
    # E_F ∝ n_e^(2/3) -> E_F(r)=E_F0*(r_B/r).
    E_F = S["E_F0"] * x

    E_grav_per_nucleon = G * M_BH * M_P / r
    shell_mass_dr_eq_r = 4.0 * pi * r**3 * rho
    t_dyn = r / v_ff

    return {
        "r": r,
        "r_over_rB": r / S["r_B"],
        "rho": rho,
        "c_s": c_s,
        "sigma_perp": sigma_perp,
        "v_ff": v_ff,
        "ell_typ": ell_typ,
        "f_cap": f_cap,
        "xi_direct": xi_direct,
        "kn_eff_direct": kn_eff_direct,
        "E_F": E_F,
        "E_grav_per_nucleon": E_grav_per_nucleon,
        "shell_mass": shell_mass_dr_eq_r,
        "t_dyn": t_dyn,
    }


def sonic_radius_fraction(gamma: float) -> float:
    """Classical adiabatic Bondi sonic radius r_c/r_B for 1 < gamma < 5/3."""
    return max(0.0, (5.0 - 3.0 * gamma) / 4.0)


def gamma_for_sonic_at(r_transition: float) -> float:
    """gamma where the simple Bondi sonic point equals r_transition."""
    x = r_transition / S["r_B"]
    return (5.0 - 4.0 * x) / 3.0


def force_ratio_one_bh_e(charge_number: float, mass_in_mp: float) -> float:
    """Coulomb/gravity force ratio for BH charge +e on a positive ion."""
    base = (E_CHARGE**2 / (4.0 * pi * EPS0)) / (G * M_BH * M_P)
    return base * charge_number / mass_in_mp


def q_balance_ion_e(charge_number: float, mass_in_mp: float) -> float:
    """BH charge in units e required for Coulomb repulsion = gravity."""
    return 1.0 / force_ratio_one_bh_e(charge_number, mass_in_mp)


def threshold_mev(parent_u: float, daughter_u: float) -> float:
    """Endothermic EC threshold proxy from atomic mass difference."""
    return max(0.0, (daughter_u - parent_u) * U_MEV)


def initial_mass_ratio_for_mdot_today(mdot_today: float, efficiency: float = 1.0) -> float:
    """Backward dM/dt=k M^2 stress proxy, with today's rate scaled by efficiency."""
    mdot = efficiency * mdot_today
    x = mdot * EARTH_AGE / M_BH
    return 1.0 / (1.0 + x)


def main() -> None:
    print("Stage 3.69B / A-6 reduced kinetic recycling + composition closure")
    print()
    print("Base scales at M=1e11 kg")
    print(f"r_B={S['r_B']:.9e} m")
    print(f"r_s={S['r_s']:.9e} m")
    print(f"a_i={S['a_i']:.9e} m")
    print(f"lambda_geom(collision proxy)={S['lambda_geom']:.9e} m")
    print(f"lambda_TF(screening only)={S['lambda_TF']:.9e} m")
    print(f"Kn_B,geom=lambda_geom/r_B={S['lambda_geom']/S['r_B']:.9e}")
    print()

    print("Transition sensitivity (collision proxy = lambda_geom/3 ... 3 lambda_geom)")
    for fac in (1.0/3.0, 1.0, 3.0):
        r = fac * S["lambda_geom"]
        p = inner_adiabatic_proxy(r)
        print(
            f"fac={fac:.3f} r={r:.9e} m r/rB={p['r_over_rB']:.6e} "
            f"f_single={p['f_cap']:.6e} xi_direct={p['xi_direct']:.6e} "
            f"Kn_eff_direct={p['kn_eff_direct']:.6e} "
            f"EF={p['E_F']/E_CHARGE/1e3:.3f} keV "
            f"Egrav/A={p['E_grav_per_nucleon']/E_CHARGE/1e3:.3f} keV"
        )
    print()

    r0 = S["lambda_geom"]
    p0 = inner_adiabatic_proxy(r0)
    gamma_crit = gamma_for_sonic_at(r0)
    print("Loss-cone / self-collisionalization diagnostic at lambda_geom")
    print(f"ell_crit={S['ell_crit']:.9e} m^2/s")
    print(f"ell_typ={p0['ell_typ']:.9e} m^2/s")
    print(f"single-pass f_cap~{p0['f_cap']:.9e}")
    print(f"direct-only recycling pile-up xi~2/f={p0['xi_direct']:.9e}")
    print(f"if Kn0~1 at transition -> Kn_eff~{p0['kn_eff_direct']:.9e}")
    print("A persistent direct-single-pass state therefore drives itself strongly back toward collisionality if missed matter remains local.")
    print()

    print("Sonic-point sensitivity")
    print(f"gamma_crit(r_sonic=r_coll)={gamma_crit:.9f}")
    for gamma in (4.0/3.0, 1.4, 1.5, 1.6, 1.65, 1.664, 5.0/3.0):
        rsf = sonic_radius_fraction(gamma)
        relation = "outside" if rsf > p0["r_over_rB"] else "inside/marginal"
        print(f"gamma={gamma:.6f}: r_sonic/rB={rsf:.6e} -> sonic point {relation} relative to r_coll")
    print()

    print("Composition thresholds at the kinetic transition")
    fe_ec = threshold_mev(MASS_FE56_U, MASS_MN56_U)
    ni_ec = threshold_mev(MASS_NI58_U, MASS_CO58_U)
    print(f"compressed electron EF proxy={p0['E_F']/E_CHARGE/1e3:.3f} keV")
    print(f"Fe56 -> Mn56 EC threshold proxy~{fe_ec:.3f} MeV")
    print(f"Ni58 -> Co58 EC threshold proxy~{ni_ec:.3f} MeV")
    print(f"gravitational energy per nucleon~{p0['E_grav_per_nucleon']/E_CHARGE/1e3:.3f} keV")
    print("These scales do not force nuclear dissociation or electron-capture neutronization at r_coll.")
    print()

    print("Charge barrier for bulk nuclei")
    qfe = q_balance_ion_e(Z_FE, A_FE)
    qni = q_balance_ion_e(Z_NI, A_NI)
    print(f"Q_balance(fully stripped Fe56)~{qfe:.3f} e")
    print(f"Q_balance(fully stripped Ni58)~{qni:.3f} e")
    print("These are well above the few-e to ~24e charge-regulation scales used in A-4 benchmarks; screening further localizes the field.")
    print()

    print("Long-time sensitivity if net Mdot is an order-unity fraction chi of Michel")
    for chi in (0.1, 0.3, 0.7, 1.0):
        low = chi * MICHEL_LOW
        high = chi * MICHEL_HIGH
        print(
            f"chi={chi:.1f}: Mdot={low:.3e}...{high:.3e} kg/s, "
            f"kg/yr={low*YEAR:.3f}...{high*YEAR:.3f}, "
            f"P=eta=1: {low*C**2/1e12:.6f}...{high*C**2/1e12:.6f} TW, "
            f"Mi/Mf(M^2 stress)={initial_mass_ratio_for_mdot_today(MICHEL_LOW,chi):.6f}..."
            f"{initial_mass_ratio_for_mdot_today(MICHEL_HIGH,chi):.6f}"
        )
    print()
    print("Status")
    print("- r_B collisionality proxy: PASS for outer fluid/supply zone (Kn_B~1.8e-3)")
    print("- persistent direct single-pass suppression: NOT self-consistent without an escape/back-pressure closure")
    print("- recycling/self-collisionalization mechanism: strongly indicated by reduced diagnostics; exact Earth suppression factor chi remains OPEN")
    print("- Fe/Ni nuclear composition at r_coll: coherent/high-ionization channel remains plausible; forced neutronization NOT established")
    print("- long-range charge barrier for bulk Fe/Ni: NOT supported by A-4/A-5 charge scales + screening")
    print("- final Earth net Mdot: leading reduced branch is a transport-corrected fraction of outer supply, but the fraction is not numerically closed")
    print("- next required solver: time-dependent 1-D radial hydro/kinetic interface with reflective/recycling inner boundary and dense-Fe EOS")


if __name__ == "__main__":
    main()
