#!/usr/bin/env python3
"""Stage 3.69D / A-8: dense Fe/Ni coupling + weak-reaction timescale map.

Reduced, reproducible regime diagnostics for M_BH=1e11 kg.

This script:
- uses the same PREM-center reference state as A5/A7;
- propagates a deliberately simple adiabatic sensitivity scaling
  rho~x^-3/2, T~x^-1 with x=r/r_B;
- tracks ion coupling Gamma_i, geometric Knudsen number, electron Fermi momentum;
- locates continuum electron-capture energy thresholds for 58Ni->58Co and
  56Fe->56Mn using atomic mass differences;
- compares local dynamical times with a published high-density 56Fe stellar
  electron-capture rate benchmark.

It is NOT an NSE/network calculation and does not assume weak equilibrium.
"""
from __future__ import annotations
from math import pi, sqrt

G=6.67430e-11
C=299_792_458.0
HBAR=1.054571817e-34
KB=1.380649e-23
EPS0=8.8541878128e-12
E_CHARGE=1.602176634e-19
M_E=9.1093837139e-31
AMU=1.66053906660e-27

M_BH=1.0e11
RHO0=13_088.5
T0=6000.0
V0=10.4355e3
Z=26.0
A=56.0
A_I0=1.1925764049670166e-10
LAMBDA_GEOM0=1.1243718173803313e-10
R_B=G*M_BH/V0**2
R_S=2*G*M_BH/C**2
N_I0=RHO0/(A*AMU)
N_E0=Z*N_I0
PF0=HBAR*(3*pi*pi*N_E0)**(1/3)
Y0=PF0/(M_E*C)
GAMMA0_Z26=Z*Z*E_CHARGE**2/(4*pi*EPS0*A_I0*KB*T0)
KN0=LAMBDA_GEOM0/R_B
ME_C2_MEV=0.51099895
U_MEV=931.49410242

# Atomic masses, u. Threshold kinetic energy for continuum electron capture
# equals daughter-parent atomic-mass excess in this reduced treatment.
M56FE=55.934939347
M56MN=55.938906784
M58NI=57.935346224
M58CO=57.935755037
Q_FE_MEV=(M56MN-M56FE)*U_MEV
Q_NI_MEV=(M58CO-M58NI)*U_MEV

# Published screened 56Fe EC benchmark at rho*Ye=1e11 g/cm3, T9=3.
# Liu & Luo 2013 (MNRAS 433, 1108): lambda_ec^s = 1.5916e4 s^-1.
LAMBDA_EC_FE_HIGH=1.5916e4


def state(x: float, z_eff: float=26.0) -> dict:
    rho=RHO0*x**(-1.5)
    T=T0/x
    # n~x^-3/2 => a~x^1/2; Gamma~Zeff^2/(aT)~sqrt(x)
    Gamma=GAMMA0_Z26*(z_eff/Z)**2*sqrt(x)
    Kn_geom=KN0*sqrt(x)
    y=Y0/sqrt(x)
    ef_kin=(sqrt(1+y*y)-1)*ME_C2_MEV
    r=x*R_B
    t_dyn=sqrt(r**3/(2*G*M_BH))
    return dict(x=x,r=r,r_rs=r/R_S,rho=rho,T=T,Gamma=Gamma,Kn=Kn_geom,y=y,EF_MeV=ef_kin,t_dyn=t_dyn)


def x_for_fermi_kinetic(q_mev: float) -> float:
    gamma=1.0+q_mev/ME_C2_MEV
    y=sqrt(gamma*gamma-1.0)
    return (Y0/y)**2


def print_state(label: str, x: float, z_eff: float=26.0):
    s=state(x,z_eff)
    print(f"{label}: x={x:.9e}, r={s['r']:.6e} m = {s['r_rs']:.3e} r_s")
    print(f"  rho={s['rho']:.6e} kg/m3 = {s['rho']/1000:.6e} g/cm3")
    print(f"  T={s['T']:.6e} K, Gamma_i(Zeff={z_eff:g})={s['Gamma']:.6e}")
    print(f"  Kn_geom={s['Kn']:.6e}, pF/(mec)={s['y']:.6e}, E_F,kin={s['EF_MeV']:.6e} MeV")
    print(f"  t_dyn={s['t_dyn']:.6e} s")


def main():
    print("Stage 3.69D / A-8 dense Fe/Ni coupling + weak-timescale map")
    print(f"r_B={R_B:.9e} m, r_s={R_S:.9e} m")
    print(f"Gamma_i(r_B,Z=26)={GAMMA0_Z26:.6e}, Kn_geom(r_B)={KN0:.6e}")
    print(f"pF0/(mec)={Y0:.6e}")
    print()

    for x in (1.0,1e-2,1e-4,1e-6):
        print_state("grid",x)
    print()

    x_rel=Y0**2
    print_state("electron-relativistic pF=mec",x_rel)
    print()

    print(f"58Ni->58Co continuum EC kinetic threshold ~{Q_NI_MEV:.6f} MeV")
    x_ni=x_for_fermi_kinetic(Q_NI_MEV)
    print_state("Ni58 EC threshold",x_ni)
    print("  ion-coupling sensitivity:")
    for ze in (10.0,20.0,26.0):
        print(f"    Zeff={ze:4.1f}: Gamma={state(x_ni,ze)['Gamma']:.3f}")
    print()

    print(f"56Fe->56Mn continuum EC kinetic threshold ~{Q_FE_MEV:.6f} MeV")
    x_fe=x_for_fermi_kinetic(Q_FE_MEV)
    print_state("Fe56 EC threshold",x_fe)
    print("  ion-coupling sensitivity:")
    for ze in (10.0,20.0,26.0):
        print(f"    Zeff={ze:4.1f}: Gamma={state(x_fe,ze)['Gamma']:.3f}")
    print()

    x_gamma1=(1.0/GAMMA0_Z26)**2
    print_state("Gamma_i(Z=26)=1 sensitivity",x_gamma1)
    print("  Note: this adiabatic proxy reaches Gamma=1 only extremely near the horizon;")
    print("  it therefore does not support inserting a weak-coupling Spitzer mean-free path earlier by assumption.")
    print()

    tau_ec=1.0/LAMBDA_EC_FE_HIGH
    s_fe=state(x_fe)
    print("Weak-reaction timescale benchmark")
    print(f"published screened 56Fe lambda_ec at rho*Ye=1e11 g/cm3,T9=3: {LAMBDA_EC_FE_HIGH:.6e} s^-1")
    print(f"tau_ec={tau_ec:.6e} s")
    print(f"Fe-threshold local t_dyn={s_fe['t_dyn']:.6e} s")
    print(f"tau_ec/t_dyn={tau_ec/s_fe['t_dyn']:.6e}")
    print("This benchmark is at much higher rho*Ye than the threshold point; it is used only as a deliberately aggressive rate scale.")
    print("Energetically open EC therefore does not imply local weak equilibrium during one inward transit.")
    print()
    print("Status")
    print("- strong-coupling/geometric branch remains collisional through Ni/Fe EC threshold radii in this reduced map")
    print("- weak-coupling Coulomb/Spitzer branch is not self-consistent there without an explicit EOS/ionization transition")
    print("- EC thresholds can open, but published weak rates are vastly slower than local dynamical times")
    print("- prompt neutronization/NSE in one pass: NOT ESTABLISHED")
    print("- long residence/recycling could change the conclusion and remains a transport-network coupling problem")


if __name__ == '__main__':
    main()
