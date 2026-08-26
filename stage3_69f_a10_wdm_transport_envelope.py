#!/usr/bin/env python3
"""Stage 3.69F / A10: first-principles-informed WDM transport envelope.

This is a reduced transport audit, not a final first-principles WDM/GR-hydro
solution. It replaces the single geometric mean-free-path proxy of A9 by a
literature-calibrated outer Fe/Fe-Ni transport envelope plus an
escape-favoring OCP/EPT-inspired inner scaling.

Literature anchors used conceptually:
- liquid Fe / Fe-Ni first-principles diffusion near core conditions:
  D ~ 5e-9 m^2/s, viscosity of order 6--26 mPa s;
- Wang et al. PRE 89, 023101 (2014): QMD Fe transport at
  rho=12.5--25 g/cm^3, T=0.5--15 eV and Stokes-Einstein coefficient
  bounded roughly by 1/(6*pi) ... 0.18;
- Blanchet et al. PRE 111, 015206 (2025): first-principles Fe EOS from
  7.874 to 47.2 g/cm^3 and 5500 K to 1e9 K;
- OCP self-diffusion scaling D*=2.95 Gamma^-1.34 is used only as an
  inner scaling law, normalized continuously to the outer QMD envelope.

Important: fixed Z=2 in the inner OCP scaling is deliberately chosen as an
escape-favoring / high-diffusivity comparison branch. It is not claimed to be
the actual mean ionization of deep compressed iron.
"""
from __future__ import annotations
from math import pi, sqrt, exp, erfc
import numpy as np

G=6.67430e-11
C=299_792_458.0
KB=1.380649e-23
EPS0=8.8541878128e-12
QE=1.602176634e-19
AMU=1.66053906660e-27

RHO0=13_088.5
T0=6000.0
CINF=10.4355e3
GAMMA_GAS=5.0/3.0
A_FE=56.0
M_I=A_FE*AMU

SUPPLY={
    1.0e10:(1.47e-10,1.46e-9),
    1.0e11:(1.47e-8,1.46e-7),
    2.0e11:(5.88e-8,5.84e-7),
    5.0e11:(3.68e-7,3.65e-6),
}

X_QMD_MIN=(RHO0/25_000.0)**(2.0/3.0)

LAMBDA_MATCH={
    "slow":2.482330172118451e-12,
    "mid_qmd":9.54256807250963e-12,
    "fast":3.6496840688154346e-11,
}

def rb(M):
    return G*M/CINF**2

def rs(M):
    return 2*G*M/C**2

def state(x):
    return RHO0*x**(-1.5), T0/x

def vth_i(x):
    _,T=state(x)
    return sqrt(3*KB*T/M_I)

def ocp_raw(x,Z=2.0):
    rho,T=state(x)
    ni=rho/M_I
    a=(3.0/(4*pi*ni))**(1.0/3.0)
    Gamma=Z*Z*QE*QE/(4*pi*EPS0*a*KB*T)
    wpi=sqrt(ni*Z*Z*QE*QE/(EPS0*M_I))
    Dstar=2.95*Gamma**(-1.34)
    D=Dstar*a*a*wpi
    lam=3.0*D/vth_i(x)
    return D,lam,Gamma

def lambda_outer_se(x,lam_match):
    return lam_match*X_QMD_MIN/x

def lambda_hybrid(x,lam_match):
    if x>=X_QMD_MIN:
        return lambda_outer_se(x,lam_match)
    lam0=ocp_raw(X_QMD_MIN,2.0)[1]
    return lam_match/lam0*ocp_raw(x,2.0)[1]

def loss_cycle(M,x):
    r=rb(M)*x
    cs=CINF/sqrt(x)
    sigma_perp=cs/sqrt(GAMMA_GAS)
    ell_typ=r*sigma_perp
    ell_crit=4*G*M/C
    p=min(1.0,0.5*(ell_crit/ell_typ)**2)
    vff=sqrt(2*G*M/r)
    t_cycle=r/vff
    return p,t_cycle,t_cycle/p

def reservoir_mass(M,x):
    return (8*pi/3)*RHO0*rb(M)**3*(1-x**1.5)

def find_kn1(M,lam_match):
    xs=np.logspace(-10,0,30000)
    vals=np.array([lambda_hybrid(x,lam_match)/(rb(M)*x) for x in xs])
    i=int(np.argmin(np.abs(np.log(vals))))
    return float(xs[i]),float(vals[i])

def integrate_tau(M,x0,lam_match,n=100000):
    xs=np.geomspace(x0,1.0,n)
    f=np.array([rb(M)/lambda_hybrid(float(x),lam_match) for x in xs])
    return float(np.trapezoid(f,xs))

def outer_shell_tau(M,lam_match):
    return rb(M)/(lam_match*X_QMD_MIN)*(1-X_QMD_MIN**2)/2

def maxwell_tail():
    a=sqrt(2*GAMMA_GAS)
    return erfc(a/sqrt(2))+sqrt(2/pi)*a*exp(-0.5*a*a)

F_TAIL=maxwell_tail()

def processing(M,x,mdot):
    p,tcyc,tres=loss_cycle(M,x)
    mres=reservoir_mass(M,x)
    cap=mres/tres
    return p,tres,cap,mdot/cap

def main():
    print("Stage 3.69F / A10 first-principles-informed WDM transport envelope")
    print(f"x_QMD_min={X_QMD_MIN:.9e}")
    rho,T=state(X_QMD_MIN)
    print(f"QMD-shell boundary: rho={rho/1000:.6f} g/cm3, T={T:.3f} K = {KB*T/QE:.6f} eV")
    print(f"instantaneous Maxwell v>vesc tail={F_TAIL:.9f}")
    print()
    print("Mass scan at local Kn=1")
    print("cal,M_kg,x_Kn1,r_Kn1_m,r_Kn1_over_rs,tau_outer_QMD,tau_total,p,tres_s,Mdot_cap,Xi_low,Xi_high,e_perm_upper")
    for name,lm in LAMBDA_MATCH.items():
        for M,(mlo,mhi) in SUPPLY.items():
            xkn,_=find_kn1(M,lm)
            tau_shell=outer_shell_tau(M,lm)
            tau=integrate_tau(M,xkn,lm)
            p,tres,cap,xilo=processing(M,xkn,mlo)
            _,_,_,xihi=processing(M,xkn,mhi)
            eupper=F_TAIL*exp(-tau) if tau<745 else 0.0
            print(f"{name},{M:.6e},{xkn:.9e},{xkn*rb(M):.9e},{xkn*rb(M)/rs(M):.9e},"
                  f"{tau_shell:.9e},{tau:.9e},{p:.9e},{tres:.9e},{cap:.9e},"
                  f"{xilo:.9e},{xihi:.9e},{eupper:.9e}")
    print()
    print("Interpretation")
    print("- Published QMD Fe transport directly constrains only the outer shell of the reduced profile; deeper densities exceed its tabulated domain.")
    print("- Even the fastest-diffusion outer calibration gives tau_QMD_shell~75 at 1e10 kg and ~746 at 1e11 kg.")
    print("- Therefore ballistic permanent escape through the calibrated outer shell is already exponentially suppressed.")
    print("- A QMD-normalized, deliberately escape-favoring Z=2 OCP inner scaling keeps total tau_out >> 1 for all tested masses.")
    print("- For M>=1e11 kg, Xi_high << 1 across the full calibration envelope: the reduced sink can process the historical supply.")
    print("- For M=1e10 kg, the fastest-diffusion envelope has Xi_high~1.47 and remains backpressure-sensitive.")
    print("- This supports the A9 mass-regime split, but does NOT complete first-principles A10 because Zbar/EOS/transport are not tabulated over the full inner density path.")
    print("- Full Stage 3.69 still requires a time-dependent WDM hydro/kinetic solution and a charged-electron capture closure.")

if __name__=="__main__":
    main()
