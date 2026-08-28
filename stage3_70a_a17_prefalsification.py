#!/usr/bin/env python3
"""Stage 3.70A / A17: observational pre-falsification gate.

This does not fit real seismic data. It determines which proposed observables
are even meaningful with the current A13b/A16 physical outputs.
"""
from math import pi

G = 6.67430e-11
C_EFF = 10_435.5
MASSES=(1e10,1e11,2e11,5e11)
WAVELENGTHS=(1e3,1e4,1e5)  # m: explicit scale scan, not an instrument limit

# A16 eta=1 present rest-mass power bounds [TW].
HEAT = {
    1e10:(7.4333e-5,5.5058e-3),
    1e11:(7.4333e-3,5.5058e-1),
    2e11:(2.9733e-2,2.2023),
    5e11:(1.8583e-1,13.7644),
}


def bondi_radius(M):
    return G*M/C_EFF**2


def main():
    print("Stage 3.70A / A17 observational pre-falsification gate")
    print("\nDirect near-zone seismic size parameter")
    print("M_kg,rB_m,lambda_m,ka,(ka)^4_proxy")
    for M in MASSES:
        a=bondi_radius(M)
        for lam in WAVELENGTHS:
            ka=2*pi*a/lam
            print(f"{M:.6e},{a:.12e},{lam:.6e},{ka:.12e},{ka**4:.12e}")

    print("\nHeat hard-budget channel")
    print("M_kg,Pmin_eta1_TW,Pmax_eta1_TW")
    for M in MASSES:
        print(f"{M:.6e},{HEAT[M][0]:.9e},{HEAT[M][1]:.9e}")

    print("\nGate logic")
    print("- H+ standard-Hawking neutrino channel: already FAIL in the tested project reinterpretation")
    print("- H0 direct near-zone seismology: ka << 1 by enormous margins; direct nano/micro-zone scattering is not a useful channel")
    print("- H0 macroscopic seismology: requires predicted delta-rho/delta-Vp/delta-Vs over km-scale or larger structure")
    print("- heat: current hard-budget pre-test gives no exclusion; a full geophysical source-budget fit is still needed")
    print("- matter-process neutrinos: require species/reaction-resolved luminosity and spectrum")
    print("- gravity outside an exactly spherical mass-compensated region has no new monopole; useful tests require moment/inertia or non-spherical/macroscopic effects")
    print("- therefore full Stage 3.70 likelihood is gated by missing unique macroscopic observable amplitudes, not by lack of public PREM/data")

if __name__=='__main__':
    main()
