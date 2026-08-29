#!/usr/bin/env python3
"""Stage 3.73 / F2 — Hill-sphere temporary capture and pull-down capture.

This is a reduced analytic gate, not an N-body capture-probability solver.
It evaluates the energy condition for a solar-bound seed that is already
inside a terrestrial embryo's Hill sphere when the embryo mass grows.
"""

from math import sqrt, pi

G = 6.67430e-11
M_SUN = 1.98847e30
M_EARTH = 5.9722e24
AU = 1.495978707e11
YEAR = 365.25 * 86400.0


def hill_quantities(m_planet, a=AU):
    omega = sqrt(G * M_SUN / a**3)
    r_h = a * (m_planet / (3.0 * M_SUN)) ** (1.0 / 3.0)
    v_h = omega * r_h
    t_h = 1.0 / omega
    return omega, r_h, v_h, t_h


def v_capture_impulsive(m_planet, delta, f=1.0, a=AU):
    """Maximum positive planetocentric v_inf removable by an instantaneous
    fractional planet-mass increase delta at radius r=f*r_H.

    Condition: 0.5*v_inf^2 < G*DeltaM/r.
    """
    _, r_h, _, _ = hill_quantities(m_planet, a)
    r = f * r_h
    return sqrt(2.0 * G * delta * m_planet / r)


def v_capture_smooth(m_planet, residence_time, growth_timescale, f=1.0, a=AU):
    # Reduced upper-bound: treat accumulated smooth growth during residence
    # as though it occurred instantaneously. Real adiabatic dynamics can be
    # less efficient, so this is deliberately capture-friendly.
    delta_eff = residence_time / growth_timescale
    return delta_eff, v_capture_impulsive(m_planet, delta_eff, f=f, a=a)


def main():
    print("Stage 3.73 / F2 — Hill / pull-down capture reduced gate")
    print("PBH/seed mass cancels from the specific-energy condition.")
    print()

    print("Embryo Hill scales at 1 AU")
    print("M/Mearth   r_H [m]        v_H [m/s]    1/Omega [days]")
    for mu in (0.01, 0.1, 0.5, 1.0):
        _, r_h, v_h, t_h = hill_quantities(mu * M_EARTH)
        print(f"{mu:7.2f}   {r_h:12.5e}   {v_h:10.3f}   {t_h/86400.0:10.3f}")

    print("\nImpulsive mass-growth gate at r=r_H")
    print("M/Mearth   delta=0.01   delta=0.10   delta=0.30   [m/s]")
    for mu in (0.01, 0.1, 0.5, 1.0):
        vals = [v_capture_impulsive(mu*M_EARTH, d) for d in (0.01, 0.10, 0.30)]
        print(f"{mu:7.2f}   {vals[0]:10.3f}   {vals[1]:10.3f}   {vals[2]:10.3f}")

    print("\nRadial leverage for a 1 Mearth embryo, delta=0.10")
    for f in (1.0, 0.5, 0.1, 0.01):
        print(f"r={f:5.2f} r_H -> v_inf,max={v_capture_impulsive(M_EARTH,0.10,f=f):.3f} m/s")

    print("\nSmooth-growth optimistic upper bounds at r=r_H, 1 Mearth")
    print("tau_growth    residence    delta_eff      v_inf,max")
    for tau_myr in (1.0, 10.0, 100.0):
        for tres_yr in (1.0, 10.0, 100.0):
            d, v = v_capture_smooth(M_EARTH, tres_yr*YEAR, tau_myr*1e6*YEAR)
            print(f"{tau_myr:7.1f} Myr   {tres_yr:7.1f} yr   {d:10.3e}   {v:10.3f} m/s")

    # A deliberately transparent timing-only coincidence scale. This is not
    # a capture probability because it omits repeated encounters and phase space.
    _, _, _, t_h = hill_quantities(M_EARTH)
    hill_crossing = 2.0 * t_h
    print("\nSingle-passage random-timing coincidence proxy")
    print(f"2/Omega = {hill_crossing/YEAR:.3f} yr")
    for epoch_myr in (10.0, 100.0):
        p = hill_crossing / (epoch_myr*1e6*YEAR)
        print(f"window / {epoch_myr:.0f} Myr = {p:.3e}")

    print("\nInterpretation")
    print("STATIC permanent capture without dissipation/mass evolution: FAIL")
    print("SMOOTH terrestrial pull-down as a generic capture channel: FAIL / separatrix-tail OPEN")
    print("IMPULSIVE giant-impact mass jump kinematic existence: PASS")
    print("OVERALL F2 delivery probability: OPEN (requires N-body phase-space + impact timing)")


if __name__ == "__main__":
    main()
