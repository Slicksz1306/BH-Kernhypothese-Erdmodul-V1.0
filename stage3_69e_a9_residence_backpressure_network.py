#!/usr/bin/env python3
"""Stage 3.69E / A-9: reduced residence/backpressure/weak-network closure.

Purpose
-------
This solver connects the A6/A7 recycling picture to the A8 dense-matter/
weak-timescale map for the small Earth branch.  It is deliberately a
reduced closure, not a final WDM/GR-hydro simulation.

It computes:
- loss-cone encounter probability and repeated-encounter residence time;
- strong-coupling ballistic escape suppression from a collisional optical depth;
- a deliberately opposite collisionless escape bracket;
- reservoir processing capacity versus the historical Michel supply range;
- critical transition radius / BH mass for onset of backpressure sensitivity;
- plasma-response times as a quasineutrality check;
- weak-reaction timescale requirements at the A8 Ni/Fe EC threshold radii.

The main distinction is

    single-pass capture probability != stationary net-Mdot factor.

If misses remain collisional and recycle, eventual capture approaches unity.
If misses permanently escape, the same microscopic p can instead give a very
small net capture fraction.  A9 quantifies which reduced branch is internally
consistent with the current dense-Fe proxies.
"""
from __future__ import annotations

from math import pi, sqrt, exp, erfc, log10

G = 6.67430e-11
C = 299_792_458.0
EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19
M_E = 9.1093837139e-31
AMU = 1.66053906660e-27

RHO0 = 13_088.5
C_INF = 10.4355e3
GAMMA = 5.0 / 3.0
A_FE = 56.0
Z_FE = 26.0

# A7 strong-coupling/geometric mean-free-path proxy at r_B.
# This is a reduced sensitivity scale, not a first-principles WDM transport coefficient.
LAMBDA_GEOM0 = 1.1243718173803313e-10

# A8 aggressive published screened 56Fe stellar EC comparison scale.
# Liu 2013, MNRAS 433, 1108, at rho*Ye=1e11 g/cm^3, T9=3.
LAMBDA_EC_FE_FAST = 1.5916e4  # s^-1

# A8 free-Fermi threshold radii in x=r/r_B for the M-independent reduced profile.
X_NI58_EC = 1.66e-4
X_FE56_EC = 5.08e-6

# Historical project Michel/supply benchmarks.
SUPPLY = {
    1.0e10: (1.47e-10, 1.46e-9),
    1.0e11: (1.47e-8, 1.46e-7),
    2.0e11: (5.88e-8, 5.84e-7),
    5.0e11: (3.68e-7, 3.65e-6),
}

# Atomic/electronic transition-scale sensitivity bracket motivated by A5/A8.
R_TRANSITION = (3.0e-11, 1.0e-10, 2.0e-10)


def r_b(M: float) -> float:
    return G * M / C_INF**2


def r_s(M: float) -> float:
    return 2.0 * G * M / C**2


def loss_cone_cycle(M: float, x: float) -> dict:
    """A7 reduced angular-momentum/recycling encounter model."""
    rb = r_b(M)
    r = rb * x
    cs = C_INF / sqrt(x)
    sigma_perp = cs / sqrt(GAMMA)
    ell_typ = r * sigma_perp
    ell_crit = 4.0 * G * M / C
    p = min(1.0, 0.5 * (ell_crit / ell_typ) ** 2)
    vff = sqrt(2.0 * G * M / r)
    t_cycle = r / vff
    t_res_no_escape = t_cycle / p
    return {
        "r": r,
        "x": x,
        "p": p,
        "t_cycle": t_cycle,
        "t_res_no_escape": t_res_no_escape,
    }


def reservoir_mass(M: float, x_inner: float) -> float:
    """Mass between x_inner*r_B and r_B for rho=rho0*x^-3/2."""
    return (8.0 * pi / 3.0) * RHO0 * r_b(M) ** 3 * (1.0 - x_inner ** 1.5)


def strong_coupling_tau_out(M: float, x: float) -> float:
    """Optical-depth proxy to r_B for lambda=lambda0*x^(3/2)."""
    return 2.0 * r_b(M) / LAMBDA_GEOM0 * (x ** -0.5 - 1.0)


def maxwell_escape_tail() -> float:
    """3-D Maxwell speed tail above local escape speed in the A7 scaling.

    sigma_1D=cs/sqrt(gamma), vesc=sqrt(2)*cs, so a=vesc/sigma=sqrt(2 gamma).
    This is only the fraction instantaneously kinematically above escape;
    it is NOT a permanent escape fraction in a collisional medium.
    """
    a = sqrt(2.0 * GAMMA)
    return erfc(a / sqrt(2.0)) + sqrt(2.0 / pi) * a * exp(-0.5 * a * a)


F_ESCAPE_TAIL = maxwell_escape_tail()


def strong_coupling_permanent_escape(M: float, x: float) -> float:
    """Ballistic no-collision escape proxy: f_tail * exp(-tau_out)."""
    tau = strong_coupling_tau_out(M, x)
    if tau > 745.0:
        return 0.0
    return F_ESCAPE_TAIL * exp(-tau)


def eventual_capture(p: float, e_perm: float) -> float:
    """Capture p, permanent escape e, otherwise recycle exactly."""
    if p < 0.0 or e_perm < 0.0 or p + e_perm > 1.0 + 1e-12:
        raise ValueError("invalid probabilities")
    if p + e_perm == 0.0:
        return 0.0
    return p / (p + e_perm)


def plasma_response_time(x: float) -> float:
    n_i0 = RHO0 / (A_FE * AMU)
    n_e0 = Z_FE * n_i0
    n_e = n_e0 * x ** -1.5
    omega_pe = sqrt(n_e * E_CHARGE**2 / (M_E * EPS0))
    return 1.0 / omega_pe


def processing_row(M: float, r_transition: float, mdot: float) -> dict:
    rb = r_b(M)
    x = r_transition / rb
    if not (0.0 < x < 1.0):
        raise ValueError("transition radius must lie inside r_B")
    cyc = loss_cone_cycle(M, x)
    t_res = cyc["t_res_no_escape"]
    m_res = reservoir_mass(M, x)
    mdot_capacity = m_res / t_res
    xi_required = mdot / mdot_capacity
    tau = strong_coupling_tau_out(M, x)
    e_sc = strong_coupling_permanent_escape(M, x)
    chi_sc = eventual_capture(cyc["p"], e_sc)
    chi_collisionless = eventual_capture(cyc["p"], F_ESCAPE_TAIL)
    return {
        **cyc,
        "M": M,
        "r_transition": r_transition,
        "m_res": m_res,
        "mdot_capacity": mdot_capacity,
        "xi_required": xi_required,
        "tau_out": tau,
        "e_sc": e_sc,
        "chi_sc": chi_sc,
        "chi_collisionless": chi_collisionless,
        "t_plasma": plasma_response_time(x),
    }


def critical_x(M: float, mdot: float) -> float:
    """Solve xi_required=1 by bisection in x."""
    lo, hi = 1.0e-8, 0.2
    for _ in range(120):
        mid = 0.5 * (lo + hi)
        cyc = loss_cone_cycle(M, mid)
        cap = reservoir_mass(M, mid) / cyc["t_res_no_escape"]
        xi = mdot / cap
        if xi > 1.0:
            hi = mid
        else:
            lo = mid
    return 0.5 * (lo + hi)


def critical_mass_for_physical_transition(r_transition: float, xcrit: float) -> float:
    # r_B/M = G/c_inf^2.
    return r_transition / (xcrit * G / C_INF**2)


def weak_threshold_row(M: float, x: float) -> dict:
    cyc = loss_cone_cycle(M, x)
    t_res = cyc["t_res_no_escape"]
    lam_required = 1.0 / t_res
    p_fast_fe = 1.0 - exp(-LAMBDA_EC_FE_FAST * t_res)
    return {
        **cyc,
        "lambda_required": lam_required,
        "P_ec_fast_Fe_scale": p_fast_fe,
        "t_plasma": plasma_response_time(x),
    }


def main() -> None:
    print("Stage 3.69E / A-9 reduced residence/backpressure/weak-network closure")
    print(f"Maxwell instantaneous v>vesc tail = {F_ESCAPE_TAIL:.9f}")
    print("This tail is NOT permanent escape when tau_coll>>1.\n")

    print("Mass / transition-scale scan")
    print("M_kg, r_t_m, mdot_case, p, t_res_s, Mdot_capacity, xi_required, tau_out, chi_SC, chi_collisionless, t_plasma/t_res")
    for M, (mdot_lo, mdot_hi) in SUPPLY.items():
        for rt in R_TRANSITION:
            for label, mdot in (("low", mdot_lo), ("high", mdot_hi)):
                row = processing_row(M, rt, mdot)
                print(
                    f"{M:.6e}, {rt:.3e}, {label}, {row['p']:.9e}, "
                    f"{row['t_res_no_escape']:.9e}, {row['mdot_capacity']:.9e}, "
                    f"{row['xi_required']:.9e}, {row['tau_out']:.9e}, "
                    f"{row['chi_sc']:.9e}, {row['chi_collisionless']:.9e}, "
                    f"{row['t_plasma']/row['t_res_no_escape']:.9e}"
                )

    print("\nCritical transition x where baseline recycling capacity equals supply")
    Mref = 1.0e11
    xlo = critical_x(Mref, SUPPLY[Mref][0])
    xhi = critical_x(Mref, SUPPLY[Mref][1])
    print(f"low supply : xcrit={xlo:.12e}, rcrit(M=1e11)={xlo*r_b(Mref):.12e} m")
    print(f"high supply: xcrit={xhi:.12e}, rcrit(M=1e11)={xhi*r_b(Mref):.12e} m")
    for rt in R_TRANSITION:
        print(
            f"r_t={rt:.3e} m -> Mcrit(low)={critical_mass_for_physical_transition(rt,xlo):.9e} kg, "
            f"Mcrit(high)={critical_mass_for_physical_transition(rt,xhi):.9e} kg"
        )

    print("\nWeak-timescale closure at A8 threshold radii")
    print("M_kg, channel, p, t_res_s, lambda_required_s^-1, P_using_fast_Fe_scale, t_plasma/t_res")
    for M in SUPPLY:
        for name, x in (("Ni58-threshold", X_NI58_EC), ("Fe56-threshold", X_FE56_EC)):
            row = weak_threshold_row(M, x)
            print(
                f"{M:.6e}, {name}, {row['p']:.9e}, {row['t_res_no_escape']:.9e}, "
                f"{row['lambda_required']:.9e}, {row['P_ec_fast_Fe_scale']:.9e}, "
                f"{row['t_plasma']/row['t_res_no_escape']:.9e}"
            )

    print("\nInterpretation")
    print("- In the strong-coupling/geometric branch tau_out is enormous, so ballistic permanent escape is negligible.")
    print("- Then repeated encounters give chi_capture~1; the issue becomes whether the reservoir can process the imposed supply without pile-up.")
    print("- For M>=~1e11 kg, all tested 3e-11...2e-10 m transition scales have xi_required<=1 at the historical Michel range.")
    print("- M=1e10 kg is transition-scale/backpressure sensitive and is not closed by this reduced model.")
    print("- The opposite collisionless bracket gives tiny chi, demonstrating that the coupling/escape physics is the decisive discriminator.")
    print("- Plasma response is much faster than residence, supporting quasineutral bulk flow as a reduced closure, not fixing the discrete BH charge exactly.")
    print("- At the A8 EC threshold radii, weak rates would need to be ~1/t_res; the aggressive published Fe rate scale is many orders too slow.")
    print("- Therefore prompt one-pass weak equilibration is not supported in the supply-processing strong-coupling branch.")
    print("- Final Stage 3.69 still requires first-principles WDM EOS/transport or a coupled time-dependent hydro/kinetic calculation to replace the geometric collision proxy.")


if __name__ == "__main__":
    main()
