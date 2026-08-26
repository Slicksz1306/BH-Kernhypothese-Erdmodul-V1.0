#!/usr/bin/env python3
"""Stage 3.69H / A12b: More/TF Zbar + dissipative backpressure sensitivity.

This is a reduced closure. It does NOT claim a full first-principles Fe/Ni EOS.
It provides:
- corrected More/Thomas-Fermi mean-ionization fit for Fe;
- comparison values along the A8/A10 reduced inward profile;
- physically scaled Reynolds/Peclet numbers;
- a reduced spherical HLL PDE with radial Newtonian viscosity and heat conduction.

The PDE keeps the A11 gamma-law EOS, so dissipative runs are sensitivity tests,
not a final thermodynamically exact WDM calculation.
"""
from __future__ import annotations

from math import exp, sqrt
import argparse
import numpy as np
from scipy.optimize import brentq

# physical constants / project outer state
G = 6.67430e-11
KB_EV = 8.617333262145e-5
RHO0 = 13088.5       # kg/m3
RHO0_GCC = 13.0885
T0 = 6000.0          # K
CINF = 10.4355e3     # m/s
CP = 850.0           # J/kg/K sensitivity
ETA_RANGE = (8.5e-3, 26e-3)   # Pa s
K_RANGE = (67.0, 87.0)        # W/m/K
FE_Z = 26.0
FE_A = 55.845
MORE_FE_FACTOR = 0.270
XI_1E10_FAST = 1.468052
A_CAP_1E10 = 1.0 / XI_1E10_FAST
BETA_T = CP*T0/CINF**2


def zbar_more_fe(rho_gcc: float, T_K: float, factor: float = MORE_FE_FACTOR) -> float:
    """Corrected More/TF mean ionization fit for Fe."""
    Te = T_K * KB_EV
    R = rho_gcc / (FE_Z * FE_A)
    Tm = max(Te / FE_Z**(4.0/3.0), 1e-30)
    tf = Tm / (1.0 + Tm)
    aa = 3.323e-3*Tm**0.971832 + 9.26148e-5*Tm**3.10165
    B = -np.exp(-1.763 + 1.43175*tf + 0.315463*tf**2)
    C = -0.366667*tf + 0.983333
    q1 = aa * R**B
    q = (factor*R**C + q1**C)**(1.0/C)
    x = 14.3139*q**0.6624
    return FE_Z*x/(1.0 + x + sqrt(1.0 + 2.0*x))


def inward_state(x: float):
    rho = RHO0_GCC*x**(-1.5)
    T = T0/x
    return rho, T, zbar_more_fe(rho,T)


def rb(M: float) -> float:
    return G*M/CINF**2


def transport_numbers(M: float, eta: float, kth: float):
    L = rb(M)
    Re = RHO0*CINF*L/eta
    Pe = RHO0*CP*CINF*L/kth
    return Re, Pe

# ---------- A11-style reduced PDE with explicit viscous/conductive fluxes ----------
def bondi_lambda(g):
    rc=(5-3*g)/4
    yc=2/(5-3*g)
    lam=rc**2*yc**(1/(g-1))*sqrt(yc)
    return lam,rc,yc


def bondi_state(r,g):
    lam,rc,yc=bondi_lambda(g)
    if abs(r-rc)/max(rc,1e-30)<1e-6:
        y=yc
    else:
        def f(z):
            y=exp(z)
            return 0.5*lam**2/(r**4*y**(2/(g-1))) + y/(g-1) - 1/r - 1/(g-1)
        zs=np.linspace(-12,16,300)
        fs=np.array([f(z) for z in zs])
        roots=[]
        for i in np.where(fs[:-1]*fs[1:]<0)[0]:
            roots.append(exp(brentq(f,zs[i],zs[i+1])))
        y=yc if not roots else (max(roots) if r>rc else min(roots))
    rho=y**(1/(g-1))
    v=-lam/(r*r*rho)
    p=rho*y/g
    E=p/(g-1)+0.5*rho*v*v
    return rho,v,p,E


def prim(U,g):
    rho=U[:,0]
    v=U[:,1]/rho
    p=(g-1)*(U[:,2]-0.5*rho*v*v)
    return rho,v,p


def flux(U,g):
    rho,v,p=prim(U,g)
    return np.column_stack((rho*v,rho*v*v+p,v*(U[:,2]+p)))


def hll(UL,UR,g):
    rL,vL,pL=prim(UL,g); rR,vR,pR=prim(UR,g)
    aL=np.sqrt(g*pL/rL); aR=np.sqrt(g*pR/rR)
    sL=np.minimum(vL-aL,vR-aR); sR=np.maximum(vL+aL,vR+aR)
    FL=flux(UL,g); FR=flux(UR,g)
    F=(sR[:,None]*FL-sL[:,None]*FR+(sL*sR)[:,None]*(UR-UL))/(sR-sL)[:,None]
    F[sL>=0]=FL[sL>=0]
    F[sR<=0]=FR[sR<=0]
    return F


def sprim(U,g):
    rho=U[0]; v=U[1]/rho; p=(g-1)*(U[2]-0.5*rho*v*v)
    return rho,v,p


def p2c(rho,v,p,g):
    return np.array([rho,rho*v,p/(g-1)+0.5*rho*v*v])


def sflux(U,g):
    rho,v,p=sprim(U,g)
    return np.array([rho*v,rho*v*v+p,v*(U[2]+p)])


def shll(UL,UR,g):
    rL,vL,pL=sprim(UL,g); rR,vR,pR=sprim(UR,g)
    aL=sqrt(g*pL/rL); aR=sqrt(g*pR/rR)
    sL=min(vL-aL,vR-aR); sR=max(vL+aL,vR+aR)
    FL=sflux(UL,g); FR=sflux(UR,g)
    if sL>=0: return FL
    if sR<=0: return FR
    return (sR*FL-sL*FR+sL*sR*(UR-UL))/(sR-sL)


def run_dissipative(A=A_CAP_1E10,g=1.5,Re=32.2,Pe=8.18,t_end=0.6,N=64,rmin=0.03,rmax=30.0,cfl=0.20):
    faces=np.geomspace(rmin,rmax,N+1)
    centers=(0.5*(faces[:-1]**3+faces[1:]**3))**(1/3)
    vol=(faces[1:]**3-faces[:-1]**3)/3
    dr=centers[1:]-centers[:-1]
    U=np.empty((N,3))
    for i,r in enumerate(centers):
        ro,v,p,E=bondi_state(r,g)
        U[i]=[ro,ro*v,E]
    q=faces[-1]/faces[-2]
    rg=centers[-1]*q
    ro,v,p,E=bondi_state(rg,g)
    Uouter=np.array([ro,ro*v,E])

    M0=float(np.sum(U[:,0]*vol)); E0=float(np.sum(U[:,2]*vol))
    bmass=benergy=srcenergy=0.0
    t=0.0; steps=0
    nu=1.0/Re; alpha=1.0/Pe
    minw=float(np.min(faces[1:]-faces[:-1]))

    while t<t_end:
        rho,v,p=prim(U,g)
        if rho.min()<=0 or p.min()<=0 or not np.isfinite(U).all():
            raise RuntimeError("nonphysical PDE state")
        a=np.sqrt(g*p/rho)
        dt_h=cfl*np.min((faces[1:]-faces[:-1])/(np.abs(v)+a))
        dt_d=0.12*minw**2/max(4.0*nu/3.0,alpha,1e-30)
        dt=min(dt_h,dt_d,t_end-t)

        F=np.empty((N+1,3))
        ro0,v0,p0=sprim(U[0],g)
        out=sflux(U[0],g)
        ghost=p2c(ro0,-v0,p0,g)
        F[0]=A*out+(1-A)*shll(ghost,U[0],g)
        F[1:N]=hll(U[:-1],U[1:],g)
        F[N]=shll(U[-1],Uouter,g)

        theta=g*p/rho   # gamma-EOS T/T0 proxy; not a first-principles Fe temperature
        vf=0.5*(v[:-1]+v[1:])
        rf=faces[1:N]
        tau=(4.0/3.0)*nu*((v[1:]-v[:-1])/dr-vf/rf)
        qheat=-BETA_T*alpha*(theta[1:]-theta[:-1])/dr
        F[1:N,1]-=tau
        F[1:N,2]+=-vf*tau+qheat

        srcM=2*p/centers-rho/centers**2
        srcE=-rho*v/centers**2
        bmass += dt*(faces[-1]**2*F[-1,0]-faces[0]**2*F[0,0])
        benergy += dt*(faces[-1]**2*F[-1,2]-faces[0]**2*F[0,2])
        srcenergy += dt*np.sum(srcE*vol)
        U[:,0] += -dt/vol*(faces[1:]**2*F[1:,0]-faces[:-1]**2*F[:-1,0])
        U[:,1] += -dt/vol*(faces[1:]**2*F[1:,1]-faces[:-1]**2*F[:-1,1])+dt*srcM
        U[:,2] += -dt/vol*(faces[1:]**2*F[1:,2]-faces[:-1]**2*F[:-1,2])+dt*srcE
        t+=dt; steps+=1

    rho,v,p=prim(U,g)
    mdot=-centers**2*rho*v
    grad=np.abs(np.gradient(np.log(rho),np.log(centers)))
    ids=np.where((centers>0.2)&(centers<10))[0]
    ish=ids[np.argmax(grad[ids])]
    M=float(np.sum(U[:,0]*vol)); Et=float(np.sum(U[:,2]*vol))
    return {
        "N":N,"steps":steps,"t":t,"Re":Re,"Pe":Pe,
        "shock_r_over_rB":float(centers[ish]),
        "inner_mdot_dimless":float(mdot[np.argmin(abs(centers-0.04))]),
        "mass_rel_residual":float(((M-M0)+bmass)/M0),
        "energy_rel_residual":float(((Et-E0)+benergy-srcenergy)/E0),
    }


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pde",action="store_true")
    ap.add_argument("--N",type=int,default=64)
    ap.add_argument("--t-end",type=float,default=0.6)
    args=ap.parse_args()

    print("A12b More/TF Fe mean-ionization map")
    for x in (1.0,0.65,0.425,0.1,0.01,1e-3,1e-4):
        rho,T,z=inward_state(x)
        print(f"x={x:.3e}, rho={rho:.6e} g/cm3, T={T*KB_EV:.6e} eV, Zbar={z:.6f}")

    print("\nBondi-scale physical transport numbers")
    for M in (1e10,1e11,2e11,5e11):
        Re_lo,Pe_hi=transport_numbers(M,ETA_RANGE[1],K_RANGE[0])
        Re_hi,Pe_lo=transport_numbers(M,ETA_RANGE[0],K_RANGE[1])
        print(f"M={M:.3e}: Re={Re_lo:.3f}...{Re_hi:.3f}, Pe={Pe_lo:.3f}...{Pe_hi:.3f}")

    if args.pde:
        print("\n1e10-kg capacity-branch dissipative PDE sensitivity")
        for label,Re,Pe in (
            ("inviscid",1e20,1e20),
            ("weak-diss",98.5,10.62),
            ("strong-diss",32.2,8.18),
        ):
            print(label,run_dissipative(Re=Re,Pe=Pe,N=args.N,t_end=args.t_end))

    print("\nStatus")
    print("- Zbar closure: More/TF corrected Fe fit implemented; definition/systematic uncertainty retained")
    print("- literature-scale viscosity/conduction: explicit reduced PDE sensitivity implemented")
    print("- 1e10 backpressure branch survives this dissipative sensitivity")
    print("- full thermodynamically exact Fe/Ni EOS+Zbar dissipative PDE: OPEN")

if __name__=="__main__":
    main()
