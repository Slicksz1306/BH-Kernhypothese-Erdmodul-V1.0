#!/usr/bin/env python3
"""Stage 3.69J / A14: dense-core charged-electron screening closure.

This is a reduced dense-matter closure for the charge-feedback problem.  It
replaces the diffuse equal-temperature plasma charge scale as the preferred
Earth-core proxy by a Thomas-Fermi-screened, degenerate-electron bracket.

It is NOT a full screened Coulomb-Dirac S-matrix calculation.
"""
from math import pi, sqrt, exp

EPS0 = 8.8541878128e-12
E = 1.602176634e-19
HBAR = 1.054571817e-34
M_E = 9.1093837139e-31
M_P = 1.67262192595e-27
G = 6.67430e-11
C = 299_792_458.0
KB = 1.380649e-23
M_BH = 1.0e11
T = 6000.0
N_I = 1.4075e29  # m^-3, A5 outer Fe ion-density proxy


def fermi_state(zbar):
    ne = zbar*N_I
    pF = HBAR*(3*pi*pi*ne)**(1/3)
    EF = pF*pF/(2*M_E)
    vF = pF/M_E
    lambda_tf = sqrt(2*EPS0*EF/(3*ne*E*E))
    return ne, EF, vF, lambda_tf


def yukawa_energy_per_elementary_charge(lambda_tf):
    # |e phi| at r=lambda_TF for Q=+e, including exp(-1).
    return (E*E/(4*pi*EPS0*lambda_tf))*exp(-1)


def dense_charge_scale(zbar):
    ne,EF,vF,lam = fermi_state(zbar)
    U1 = yukawa_energy_per_elementary_charge(lam)
    n_ef = EF/U1
    n_ef_thermal = (EF + 1.5*KB*T)/U1
    response_time = lam/vF
    return ne,EF/E,vF,lam,n_ef,n_ef_thermal,response_time


def diffuse_equal_T_Qeq_e():
    Q = 2*pi*EPS0*G*(M_P-M_E)*M_BH/E
    return Q/E


def proton_force_balance_e():
    Q = 4*pi*EPS0*G*M_BH*M_P/E
    return Q/E


def electron_force_balance_e():
    Q = 4*pi*EPS0*G*M_BH*M_E/E
    return Q/E


def main():
    print("Stage 3.69J / A14 dense-core electron screening")
    print(f"diffuse equal-T benchmark Qeq = {diffuse_equal_T_Qeq_e():.6f} e")
    print(f"proton force balance = {proton_force_balance_e():.6f} e")
    print(f"electron force-balance magnitude = {electron_force_balance_e():.6f} e")
    print("\nZbar,ne_m-3,EF_eV,vF_m_s,lambdaTF_m,N_EF,N_EF_plus_thermal,response_s")
    for z in (2.76,5.0,10.0,26.0):
        vals=dense_charge_scale(z)
        print(f"{z:.2f}," + ",".join(f"{x:.9e}" for x in vals))
    print("\nInterpretation")
    print("- outer-core degenerate screening gives an O(1-few e) positive-charge scale")
    print("- diffuse +24.18e is a benchmark, not the preferred dense-core equilibrium")
    print("- screening response is ~1e-17 s, far faster than macroscopic supply evolution")
    print("- exact screened Coulomb-Dirac electron matching remains a refinement")

if __name__ == '__main__':
    main()
