#!/usr/bin/env python3
"""Stage 3.73 / F2: terrestrial-embryo pull-down capture audit.

A project-mass PBH is treated as a test particle in the Sun+embryo potential.
The calculation separates:
1) smooth embryo growth during typical temporary Hill-sphere capture;
2) an impulsive planetary mass jump (giant-impact sensitivity limit).

This is a reduced kinematic gate, not a capture probability calculation.
"""

from math import exp, sqrt

G = 6.67430e-11
M_SUN = 1.98847e30
M_EARTH = 5.9722e24
AU = 1.495978707e11


def hill_radius(mp: float, a: float = AU) -> float:
    return a*(mp/(3*M_SUN))**(1/3)


def v_escape_at_hill(mp: float) -> float:
    rh = hill_radius(mp)
    return sqrt(2*G*mp/rh)


def smooth_growth_fraction(tcap_yr: float, tgrow_yr: float):
    dm = exp(tcap_yr/tgrow_yr)-1.0
    drh = (1.0+dm)**(1/3)-1.0
    return dm, drh


def impulsive_capture_speed(delta_m: float, r: float) -> float:
    """Reduced instantaneous mass-jump threshold from DeltaE=-G DeltaM/r."""
    return sqrt(2*G*delta_m/r)


def main() -> None:
    print("Stage 3.73 / F2 terrestrial pull-down capture audit")
    print("\nHill benchmarks at 1 AU")
    print("Mplanet_Mearth,RH_AU,v_esc_at_RH_mps")
    for f in (1e-3, 1e-2, 0.1, 1.0):
        mp=f*M_EARTH
        rh=hill_radius(mp)
        print(f"{f:.6e},{rh/AU:.9e},{v_escape_at_hill(mp):.9e}")

    print("\nSmooth growth during temporary capture")
    print("tgrow_yr,tcap_yr,DeltaM_over_M,DeltaRH_over_RH")
    for tgrow in (1e5, 1e6, 1e7):
        for tcap in (10.0, 50.0, 100.0):
            dm,drh=smooth_growth_fraction(tcap,tgrow)
            print(f"{tgrow:.6e},{tcap:.6e},{dm:.9e},{drh:.9e}")

    print("\nImpulsive mass-jump reduced capture threshold")
    rh_e=hill_radius(M_EARTH)
    print("DeltaM_Mearth,r_over_RHearth,v_threshold_mps")
    for dmf in (0.01,0.1,0.5,1.0):
        for rf in (1.0,0.3,0.1):
            v=impulsive_capture_speed(dmf*M_EARTH,rf*rh_e)
            print(f"{dmf:.6e},{rf:.6e},{v:.9e}")

    print("\nInterpretation")
    print("- temporary Hill-sphere capture is dynamically allowed for low-random-velocity heliocentric test particles.")
    print("- smooth terrestrial growth over >=1e5 yr changes RH by only ~1e-6...3e-4 during 10...100 yr captures: weak pull-down in this reduced gate.")
    print("- an impulsive 1...10% Earth-mass jump while a seed is already inside the Hill sphere can change specific energy enough to bind relative speeds of order tens...hundreds m/s, depending on radius.")
    print("- larger mass jumps/deeper temporary orbits raise that threshold into the few 1e2...1e3 m/s range.")
    print("- this demonstrates kinematic possibility, not probability; phase coincidence and realistic N-body accretion history remain open.")


if __name__ == "__main__":
    main()
