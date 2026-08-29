#!/usr/bin/env python3
"""Stage 3.76 / F4 — early permanent embryo-bound seed gate.

Reduced analytic tests:
1) stable satellite zone in Hill units,
2) embryo-embryo encounter tidal-impulse scale versus capture kick,
3) adiabatic growth-assisted orbital engulfment,
4) optimistic repeated interior-crossing dynamical-friction sink timescale.

This is NOT an absolute formation probability and NOT a full N-body integration.
"""

from math import sqrt, pi

G = 6.67430e-11
M_SUN = 1.98847e30
M_E = 5.9722e24
R_E = 6.371e6
AU = 1.495978707e11
RHO_E = 5514.0
I_OPT = 30.0
YEAR = 365.25 * 86400.0

OMEGA = sqrt(G * M_SUN / AU**3)
R_H_E = AU * (M_E / (3.0 * M_SUN)) ** (1.0 / 3.0)
V_H_E = OMEGA * R_H_E

A_PRO = 0.4895   # Domingos et al. circular low-e prograde limit in r_H
A_RET = 0.9309   # circular low-e retrograde limit in r_H


def hill_scales(mu: float):
    return R_H_E * mu ** (1.0 / 3.0), V_H_E * mu ** (1.0 / 3.0)


def required_kick_over_vh(f: float, alpha: float) -> float:
    """Best-case antiparallel kick from a locally parabolic state at r=f r_H
    to a bound orbit of semimajor axis alpha r_H.

    Uses GM_p/r_H = 3 v_H^2.
    """
    vesc = sqrt(6.0 / f)
    return vesc - sqrt(vesc * vesc - 3.0 / alpha)


def tidal_impulse_over_vh(q: float, f: float, kappa: float) -> float:
    """Straight-line differential/tidal impulse scale.

    M2=q M1, seed-primary separation r=f r_H1,
    perturber impact parameter b=kappa R_H,mut,
    encounter speed V~Omega R_H,mut.

    Delta v_rel / v_H1 ~ 6 q f / [kappa^2 (1+q)].

    This is only an order-of-magnitude gate and becomes marginal when b~r.
    """
    return 6.0 * q * f / (kappa * kappa * (1.0 + q))


def isotropic_energy_orientation_fraction(f: float, alpha: float, d: float) -> float:
    """Energy-only orientation proxy for a kick of fixed magnitude d*v_H.
    Not a capture probability: angular momentum, encounter correlations and
    full 4-body dynamics are omitted.
    """
    v = sqrt(6.0 / f)
    target_binding = 3.0 / (2.0 * alpha)
    c = (-target_binding - 0.5 * d * d) / (v * d)
    if c <= -1.0:
        return 0.0
    if c >= 1.0:
        return 1.0
    return 0.5 * (1.0 + c)


def adiabatic_engulf_mass(mu_i: float, f: float) -> float:
    """Constant-density host + isotropic adiabatic growth.

    a~1/M and R~M^(1/3). For initial a_i=f r_H(mu_i), solve a(M)=R(M).
    Returns M_engulf/M_E.
    """
    return mu_i * (f * R_H_E / R_E) ** (3.0 / 4.0)


def latest_initial_mass_for_engulfment(f: float) -> float:
    """Largest initial M/M_E that reaches a=R by M=1 M_E in adiabatic limit."""
    return (1.0 / (f * R_H_E / R_E)) ** (3.0 / 4.0)


def surface_orbital_period_constant_density() -> float:
    return 2.0 * pi * sqrt(R_E**3 / (G * M_E))


def df_efold_years(mu: float, m_bh: float) -> float:
    """Optimistic A19-rescaled diameter-crossing dynamical-friction proxy.

    At v~v_esc, uniform density and I=30:
      DeltaE/E_orb ~ 6 I M_BH/M_p
    per diameter crossing, taking one crossing per surface-orbit period.
    """
    frac = 6.0 * I_OPT * m_bh / (mu * M_E)
    return surface_orbital_period_constant_density() / frac / YEAR


def main():
    print("Stage 3.76 / F4 — early embryo-bound seed reduced gate")
    print(f"Earth r_H/R_E = {R_H_E/R_E:.6f}")
    print(f"constant-density surface orbital period = {surface_orbital_period_constant_density()/3600:.4f} h")

    print("\nStable-zone scales at 1 AU")
    print("M/M_E      r_H[km]    v_H[m/s]   prograde<km   retrograde<km")
    for mu in (0.001, 0.01, 0.03, 0.10):
        rh, vh = hill_scales(mu)
        print(f"{mu:7.3f}  {rh/1e3:10.1f}  {vh:10.3f}  {A_PRO*rh/1e3:12.1f}  {A_RET*rh/1e3:13.1f}")

    print("\nRequired best-case kick at r=0.3 r_H")
    print(f"prograde target: {required_kick_over_vh(0.3,A_PRO):.6f} v_H")
    print(f"retrograde target: {required_kick_over_vh(0.3,A_RET):.6f} v_H")
    for mu in (0.01, 0.03, 0.10):
        _, vh = hill_scales(mu)
        print(
            f"M={mu:.2f} M_E -> pro {required_kick_over_vh(0.3,A_PRO)*vh:.2f} m/s, "
            f"retro {required_kick_over_vh(0.3,A_RET)*vh:.2f} m/s"
        )

    print("\nEmbryo-embryo tidal impulse gate at seed radius 0.3 r_H")
    print("q=M2/M1  kappa=b/R_Hmut  dv/v_H  P_energy,pro  P_energy,retro")
    for q in (0.10, 0.30, 1.00):
        for kappa in (1.0, 0.7, 0.5):
            d = tidal_impulse_over_vh(q, 0.3, kappa)
            pp = isotropic_energy_orientation_fraction(0.3, A_PRO, d)
            pr = isotropic_energy_orientation_fraction(0.3, A_RET, d)
            print(f"{q:8.2f}  {kappa:16.2f}  {d:7.3f}  {pp:12.4f}  {pr:14.4f}")

    print("\nAdiabatic growth-assisted engulfment")
    print("f=a_i/r_H   latest initial M/M_E engulfed by final 1 M_E")
    for f in (0.05, 0.10, 0.30, A_PRO, A_RET):
        print(f"{f:10.4f}   {latest_initial_mass_for_engulfment(f):.6f}")

    print("\nExamples: M_engulf/M_E")
    for mu_i in (0.001, 0.003, 0.010, 0.030):
        vals = [adiabatic_engulf_mass(mu_i, f) for f in (0.10, 0.30, A_PRO, A_RET)]
        print(f"M_i={mu_i:.3f}: f=.10 {vals[0]:.4f}, f=.30 {vals[1]:.4f}, pro-edge {vals[2]:.4f}, retro-edge {vals[3]:.4f}")

    print("\nOptimistic repeated interior-crossing DF e-fold time [Myr]")
    print("Mhost/M_E     1e10kg      1e11kg      2e11kg      5e11kg")
    for mu in (0.01, 0.03, 0.10):
        vals = [df_efold_years(mu, m)/1e6 for m in (1e10,1e11,2e11,5e11)]
        print(f"{mu:9.2f}  {vals[0]:10.3f}  {vals[1]:10.3f}  {vals[2]:10.3f}  {vals[3]:10.3f}")

    print("\nInterpretation")
    print("collisionless exchange / embryo-scattering energy scale: PASS as kinematic mechanism")
    print("single naked seed capture probability in realistic terrestrial N-body history: OPEN")
    print("stable embryo-bound orbit after successful exchange: PASS in known Hill stability zones")
    print("adiabatic growth can drive early bound orbit inward and engulf it: PASS in adiabatic limit")
    print("single-late-jump growth does not reproduce the same shrinkage: growth-history closure OPEN")
    print("naked-seed nebular gas drag: remains FAIL / insufficient from F1")
    print("post-engulfment repeated-crossing DF: potentially Myr-scale in optimistic A19 proxy, but physical closure OPEN")
    print("overall F4: OPEN — physically viable correlated route exists, absolute delivery fraction not identified")


if __name__ == "__main__":
    main()
