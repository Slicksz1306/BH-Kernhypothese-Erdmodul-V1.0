#!/usr/bin/env python3
"""Stage 3.71 / A19: formation/delivery recheck.

Uses an intentionally optimistic one-crossing dynamical-friction estimate for
an Earth transit. The purpose is to test whether standard halo-speed direct
capture is even energetically plausible.

F_df ~ 4 pi G^2 M^2 rho I / v^2,
with I=30 chosen as a generous Coulomb/friction factor proxy. A realistic
collisional-fluid I near Mach~1 can be much smaller, so this is capture-friendly.
"""
from math import pi, sqrt

G=6.67430e-11
R_E=6.371e6
RHO_E=5514.0
V_ESC=11.2e3
V_HALO=220e3
I_OPT=30.0
MASSES=(1e10,1e11,2e11,5e11)


def energy_loss_one_crossing(M,vinf):
    v=sqrt(vinf*vinf+V_ESC*V_ESC)
    force=4*pi*G*G*M*M*RHO_E*I_OPT/(v*v)
    return force*(2*R_E)


def capture_energy(M,vinf):
    return 0.5*M*vinf*vinf


def threshold_vinf(M):
    # Solve 8 pi G^2 M^2 rho I R/(vinf^2+vesc^2)=0.5 M vinf^2.
    A=16*pi*G*G*M*RHO_E*I_OPT*R_E
    y=(-V_ESC**2+sqrt(V_ESC**4+4*A))/2
    return sqrt(max(y,0.0))


def main():
    print("Stage 3.71 / A19 optimistic direct-Earth-capture recheck")
    print(f"uniform rho={RHO_E} kg/m3, diameter path, I={I_OPT}, v_halo={V_HALO/1e3} km/s")
    print("M_kg,DeltaE_halo_J,Einf_halo_J,DeltaE_over_Einf,v_inf_capture_threshold_m_s")
    for M in MASSES:
        de=energy_loss_one_crossing(M,V_HALO)
        ei=capture_energy(M,V_HALO)
        print(f"{M:.6e},{de:.12e},{ei:.12e},{de/ei:.12e},{threshold_vinf(M):.12e}")

    print("\nInterpretation")
    print("- standard halo-speed one-pass capture fails by ~16-18 orders in energy")
    print("- even with a generous friction factor, capture requires an already extremely co-moving vinf of only millimeters-to-centimeters per second")
    print("- such a cold/co-moving condition is an initial-condition/origin hypothesis, not a standard halo capture mechanism")
    print("- recent three-body star-capture work does not rescue this mass range: published/preprint inspiral thresholds for Jupiter-like companions are enormously heavier")

if __name__=='__main__':
    main()
