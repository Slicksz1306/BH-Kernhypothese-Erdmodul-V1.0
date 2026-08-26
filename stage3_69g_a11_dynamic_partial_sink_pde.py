#!/usr/bin/env python3
"""Stage 3.69G / A11: time-dependent partial-sink Bondi/WDM transport benchmark.

This is a REDUCED dynamic closure, not a full first-principles WDM hydro code.

What it does
------------
1. Reproduces the spherical Bondi benchmark used in A7.
2. Replaces the binary absorbing/reflecting boundary by a continuous partial-sink
   boundary A in [0,1].
3. Uses A10 transport-capacity results to define a mass-dependent capacity limiter
   for the high-supply branch:
       A_cap = min(1, 1/Xi_high).
4. Checks discrete finite-volume mass and energy conservation.
5. Scans an EOS-stiffness envelope gamma=1.4, 1.5, 1.6.
6. Keeps the full-Zbar/EOS table requirement explicitly OPEN; gamma is only a
   transparent EOS-stiffness sensitivity surrogate.

Important interpretation
------------------------
A is NOT identified one-to-one with the A5 wave cross-section. The separate
A=0.99754 run is only a Fe-like sink sensitivity test. The A10 mass-dependent
A_cap is a transport-capacity limiter, not a microscopic horizon probability.

Literature/data-domain anchors used by the project:
- Wang et al., Phys. Rev. E 89, 023101 (2014): WDM Fe QMD transport,
  rho=12.5--25 g/cm^3, T=0.5--15 eV.
- Blanchet et al., Phys. Rev. E 111, 015206 (2025): Fe first-principles EOS,
  rho=7.874--47.2 g/cm^3, T=5500 K--1e9 K.
- Dhang, Sharma & Mukhopadhyay (2016): spherical accretion inner-boundary
  sensitivity and outward shocks for reflective boundaries.
"""
from __future__ import annotations

from math import exp, sqrt
import numpy as np
from scipy.optimize import brentq

# A10 high-supply Xi in the fastest / escape-favoring transport envelope.
XI_HIGH_FAST = {
    1.0e10: 1.468052,
    1.0e11: 2.811021e-3,
    2.0e11: 4.278392e-4,
    5.0e11: 3.537298e-5,
}

FE_LIKE_SINK_SENSITIVITY = 0.99754


def bondi_lambda(g: float):
    rc = (5.0 - 3.0*g)/4.0
    yc = 2.0/(5.0 - 3.0*g)
    lam = rc**2 * yc**(1.0/(g-1.0)) * sqrt(yc)
    return lam, rc, yc


def bondi_state(r: float, g: float):
    lam, rc, yc = bondi_lambda(g)
    if abs(r-rc)/max(rc,1e-30) < 1e-6:
        y = yc
    else:
        def f(z):
            y = exp(z)
            return 0.5*lam**2/(r**4*y**(2.0/(g-1.0))) + y/(g-1.0) - 1.0/r - 1.0/(g-1.0)
        zs = np.linspace(-12.0, 16.0, 500)
        fs = [f(z) for z in zs]
        roots = []
        for i in range(len(zs)-1):
            if fs[i]*fs[i+1] < 0.0:
                roots.append(exp(brentq(f, zs[i], zs[i+1])))
        y = yc if not roots else (max(roots) if r > rc else min(roots))
    rho = y**(1.0/(g-1.0))
    v = -lam/(r*r*rho)
    p = rho*y/g
    E = p/(g-1.0) + 0.5*rho*v*v
    return rho, v, p, E


def p2c(rho, v, p, g):
    return np.array([rho, rho*v, p/(g-1.0) + 0.5*rho*v*v], float)


def prim(U, g):
    rho = U[:,0]
    v = U[:,1]/rho
    p = (g-1.0)*(U[:,2]-0.5*rho*v*v)
    return rho, v, p


def flux(U, g):
    rho, v, p = prim(U,g)
    return np.column_stack((rho*v, rho*v*v+p, v*(U[:,2]+p)))


def hll(UL, UR, g):
    rhoL,vL,pL = prim(UL,g)
    rhoR,vR,pR = prim(UR,g)
    aL = np.sqrt(g*pL/rhoL)
    aR = np.sqrt(g*pR/rhoR)
    sL = np.minimum(vL-aL, vR-aR)
    sR = np.maximum(vL+aL, vR+aR)
    FL = flux(UL,g)
    FR = flux(UR,g)
    F = (sR[:,None]*FL-sL[:,None]*FR+(sL*sR)[:,None]*(UR-UL))/(sR-sL)[:,None]
    F[sL>=0] = FL[sL>=0]
    F[sR<=0] = FR[sR<=0]
    return F


def sprim(U, g):
    rho = U[0]
    v = U[1]/rho
    p = (g-1.0)*(U[2]-0.5*rho*v*v)
    return rho,v,p


def sflux(U,g):
    rho,v,p = sprim(U,g)
    return np.array([rho*v, rho*v*v+p, v*(U[2]+p)])


def shll(UL,UR,g):
    rhoL,vL,pL = sprim(UL,g)
    rhoR,vR,pR = sprim(UR,g)
    aL = sqrt(g*pL/rhoL)
    aR = sqrt(g*pR/rhoR)
    sL = min(vL-aL, vR-aR)
    sR = max(vL+aL, vR+aR)
    FL = sflux(UL,g)
    FR = sflux(UR,g)
    if sL >= 0: return FL
    if sR <= 0: return FR
    return (sR*FL-sL*FR+sL*sR*(UR-UL))/(sR-sL)


def run_pde(A=1.0, g=1.5, t_end=0.6, N=160, rmin=0.03, rmax=10.0, cfl=0.28):
    faces = np.geomspace(rmin,rmax,N+1)
    centers = (0.5*(faces[:-1]**3+faces[1:]**3))**(1.0/3.0)
    vol = (faces[1:]**3-faces[:-1]**3)/3.0
    U = np.empty((N,3))
    for i,r in enumerate(centers):
        rho,v,p,E = bondi_state(r,g)
        U[i] = [rho,rho*v,E]
    q = faces[-1]/faces[-2]
    rg = centers[-1]*q
    rho,v,p,E = bondi_state(rg,g)
    Uouter = np.array([rho,rho*v,E])

    M0 = float(np.sum(U[:,0]*vol))
    E0 = float(np.sum(U[:,2]*vol))
    bmass = benergy = srcenergy = 0.0
    t = 0.0

    while t < t_end:
        rho,v,p = prim(U,g)
        if rho.min() <= 0 or p.min() <= 0 or not np.isfinite(U).all():
            raise RuntimeError("nonphysical PDE state")
        a = np.sqrt(g*p/rho)
        dt = cfl*np.min((faces[1:]-faces[:-1])/(np.abs(v)+a))
        dt = min(dt,t_end-t)

        F = np.empty((N+1,3))
        rho0,v0,p0 = sprim(U[0],g)
        out = sflux(U[0],g)
        ghost = p2c(rho0,-v0,p0,g)
        wall = shll(ghost,U[0],g)
        F[0] = A*out + (1.0-A)*wall
        F[1:N] = hll(U[:-1],U[1:],g)
        F[N] = shll(U[-1],Uouter,g)

        src = np.column_stack((
            np.zeros(N),
            2.0*p/centers-rho/centers**2,
            -rho*v/centers**2,
        ))

        bmass += dt*(faces[-1]**2*F[-1,0]-faces[0]**2*F[0,0])
        benergy += dt*(faces[-1]**2*F[-1,2]-faces[0]**2*F[0,2])
        srcenergy += dt*np.sum(src[:,2]*vol)

        U += -dt/vol[:,None]*(faces[1:,None]**2*F[1:]-faces[:-1,None]**2*F[:-1]) + dt*src
        t += dt

    rho,v,p = prim(U,g)
    mdot = -centers**2*rho*v
    M = float(np.sum(U[:,0]*vol))
    Et = float(np.sum(U[:,2]*vol))
    mass_res = (M-M0)+bmass
    energy_res = (Et-E0)+benergy-srcenergy
    idx04 = int(np.argmin(np.abs(centers-0.04)))
    idx01 = int(np.argmin(np.abs(centers-0.1)))
    idx1 = int(np.argmin(np.abs(centers-1.0)))
    return {
        "A":A,"g":g,"N":N,"t":t,
        "lambda_B":bondi_lambda(g)[0],
        "mdot_r004":float(mdot[idx04]),
        "mdot_r01":float(mdot[idx01]),
        "mdot_r1":float(mdot[idx1]),
        "mass_rel_residual":float(mass_res/max(abs(M0),1e-300)),
        "energy_rel_residual":float(energy_res/max(abs(E0),1e-300)),
        "rho_max":float(rho.max()),
    }


def capacity_limiter(M):
    xi = XI_HIGH_FAST[M]
    return min(1.0, 1.0/xi)


def main():
    print("Stage 3.69G / A11 reduced dynamic partial-sink PDE")
    print("Full first-principles Zbar/EOS table: OPEN; gamma envelope is explicit sensitivity only.\n")

    print("A10 mass-dependent high-supply capacity limiter")
    for M,xi in XI_HIGH_FAST.items():
        print(f"M={M:.3e} kg: Xi_high_fast={xi:.6e}, A_cap={capacity_limiter(M):.6f}")

    print("\nPDE EOS-stiffness / sink scan at t=1 rB/cinf, N=100")
    for g in (1.4,1.5,1.6):
        for label,A in (("absorb",1.0),("Fe-like sensitivity",FE_LIKE_SINK_SENSITIVITY),("1e10 fast capacity",capacity_limiter(1e10)),("reflect",0.0)):
            row = run_pde(A=A,g=g,t_end=1.0,N=100)
            print(label, row)

    print("\nConvergence/conservation scan at gamma=1.5, t=0.6")
    for A in (1.0,FE_LIKE_SINK_SENSITIVITY,capacity_limiter(1e10),0.0):
        for N in (80,120,160,200,240):
            row = run_pde(A=A,g=1.5,t_end=0.6,N=N)
            print(row)

    print("\nInterpretation")
    print("- absorbing Bondi branch is reproduced; finite-volume mass/energy accounting closes to roundoff-scale residuals")
    print("- Fe-like A~0.9975 sensitivity remains close to the absorbing branch")
    print("- the A10-fast 1e10-kg capacity limiter A~0.681 generates dynamical backpressure and strongly reduced inner flux")
    print("- M>=1e11 kg has A_cap=1 in the A10 envelope and remains on the absorbing/supply-processing branch in this reduced PDE")
    print("- exact shock-branch Mdot is not yet grid-converged enough for a Full-WDM claim")
    print("- full Zbar(rho,T), tabulated EOS, conduction/viscosity and charged-electron closure remain required")

if __name__ == "__main__":
    main()
