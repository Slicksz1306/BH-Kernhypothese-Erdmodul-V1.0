#!/usr/bin/env python3
"""Stage 3.69H / A12: shock convergence + literature-constrained transport audit.

This is a PARTIAL A12 closure. It deliberately does not pretend that a full
P(rho,T), E(rho,T), Zbar(rho,T) table has been reconstructed from papers.

It performs:
1) high-resolution convergence of the A11 1e10-kg partial-sink shock branch;
2) longer-domain shock-propagation audit;
3) literature-constrained Reynolds/Peclet estimates from liquid Fe/FeNi
   viscosity, heat capacity and thermal conductivity;
4) explicit literature-correction flag for Wang 2014 vs Sjostrom & Crockett 2018.

The full dissipative WDM PDE remains open because adding physical viscosity
and conduction consistently requires a thermodynamically consistent EOS/temperature
mapping rather than the A11 constant-gamma surrogate.
"""
from __future__ import annotations
import argparse
from math import exp, sqrt
import numpy as np
from scipy.optimize import brentq

G=6.67430e-11
CINF=10.4355e3
RHO0=13088.5
CP_FE=850.0
ETA_RANGE=(8.5e-3,26e-3)
K_RANGE=(67.0,87.0)
XI_1E10=1.468052
A_CAP=1.0/XI_1E10

def rb(M): return G*M/CINF**2
def t_bondi(M): return rb(M)/CINF

def transport_numbers(M):
    Lc=rb(M)*CINF
    re=[Lc/(eta/RHO0) for eta in ETA_RANGE]
    pe=[Lc/(k/(RHO0*CP_FE)) for k in K_RANGE]
    return {"M":M,"rB":rb(M),"tB":t_bondi(M),
            "Re_min":min(re),"Re_max":max(re),
            "Pe_min":min(pe),"Pe_max":max(pe)}

def bondi_lambda(g):
    rc=(5-3*g)/4; yc=2/(5-3*g)
    return rc**2*yc**(1/(g-1))*sqrt(yc),rc,yc

def bondi_state(r,g):
    lam,rc,yc=bondi_lambda(g)
    if abs(r-rc)/max(rc,1e-30)<1e-6:
        y=yc
    else:
        def f(z):
            y=exp(z)
            return 0.5*lam**2/(r**4*y**(2/(g-1)))+y/(g-1)-1/r-1/(g-1)
        zs=np.linspace(-12,16,400); fs=[f(float(z)) for z in zs]; roots=[]
        for i in range(len(zs)-1):
            if fs[i]*fs[i+1]<0:
                roots.append(exp(brentq(f,float(zs[i]),float(zs[i+1]))))
        y=yc if not roots else (max(roots) if r>rc else min(roots))
    rho=y**(1/(g-1)); v=-lam/(r*r*rho); p=rho*y/g
    return rho,v,p,p/(g-1)+0.5*rho*v*v

def p2c(rho,v,p,g): return np.array([rho,rho*v,p/(g-1)+0.5*rho*v*v],float)
def prim(U,g):
    rho=U[:,0]; v=U[:,1]/rho; p=(g-1)*(U[:,2]-0.5*rho*v*v); return rho,v,p
def flux(U,g):
    rho,v,p=prim(U,g); return np.column_stack((rho*v,rho*v*v+p,v*(U[:,2]+p)))
def hll(UL,UR,g):
    rhoL,vL,pL=prim(UL,g); rhoR,vR,pR=prim(UR,g)
    aL=np.sqrt(g*pL/rhoL); aR=np.sqrt(g*pR/rhoR)
    sL=np.minimum(vL-aL,vR-aR); sR=np.maximum(vL+aL,vR+aR)
    FL=flux(UL,g); FR=flux(UR,g)
    F=(sR[:,None]*FL-sL[:,None]*FR+(sL*sR)[:,None]*(UR-UL))/(sR-sL)[:,None]
    F[sL>=0]=FL[sL>=0]; F[sR<=0]=FR[sR<=0]; return F
def sprim(U,g):
    rho=U[0]; v=U[1]/rho; p=(g-1)*(U[2]-0.5*rho*v*v); return rho,v,p
def sflux(U,g):
    rho,v,p=sprim(U,g); return np.array([rho*v,rho*v*v+p,v*(U[2]+p)])
def shll(UL,UR,g):
    rL,vL,pL=sprim(UL,g); rR,vR,pR=sprim(UR,g)
    aL=sqrt(g*pL/rL); aR=sqrt(g*pR/rR); sL=min(vL-aL,vR-aR); sR=max(vL+aL,vR+aR)
    FL=sflux(UL,g); FR=sflux(UR,g)
    if sL>=0:return FL
    if sR<=0:return FR
    return (sR*FL-sL*FR+sL*sR*(UR-UL))/(sR-sL)

def run(A=A_CAP,g=1.5,t_end=0.8,N=256,rmin=0.03,rmax=10.0,cfl=0.28):
    faces=np.geomspace(rmin,rmax,N+1); centers=(0.5*(faces[:-1]**3+faces[1:]**3))**(1/3)
    vol=(faces[1:]**3-faces[:-1]**3)/3; U=np.empty((N,3))
    for i,r in enumerate(centers):
        rho,v,p,E=bondi_state(float(r),g); U[i]=[rho,rho*v,E]
    q=faces[-1]/faces[-2]; rg=centers[-1]*q; rho,v,p,E=bondi_state(float(rg),g); Uouter=np.array([rho,rho*v,E])
    M0=float(np.sum(U[:,0]*vol)); E0=float(np.sum(U[:,2]*vol)); bmass=benergy=srcenergy=0.0; t=0.0
    while t<t_end:
        rho,v,p=prim(U,g)
        if rho.min()<=0 or p.min()<=0 or not np.isfinite(U).all(): raise RuntimeError("nonphysical PDE state")
        a=np.sqrt(g*p/rho); dt=cfl*np.min((faces[1:]-faces[:-1])/(np.abs(v)+a)); dt=min(dt,t_end-t)
        F=np.empty((N+1,3)); rho0,v0,p0=sprim(U[0],g); out=sflux(U[0],g)
        ghost=p2c(rho0,-v0,p0,g); wall=shll(ghost,U[0],g); F[0]=A*out+(1-A)*wall
        F[1:N]=hll(U[:-1],U[1:],g); F[N]=shll(U[-1],Uouter,g)
        src=np.column_stack((np.zeros(N),2*p/centers-rho/centers**2,-rho*v/centers**2))
        bmass += dt*(faces[-1]**2*F[-1,0]-faces[0]**2*F[0,0]); benergy += dt*(faces[-1]**2*F[-1,2]-faces[0]**2*F[0,2]); srcenergy += dt*np.sum(src[:,2]*vol)
        U += -dt/vol[:,None]*(faces[1:,None]**2*F[1:]-faces[:-1,None]**2*F[:-1])+dt*src; t += dt
    rho,v,p=prim(U,g); mdot=-centers**2*rho*v; grad=np.abs(np.gradient(np.log(rho),np.log(centers)))
    mask=(centers>0.2)&(centers<0.8*rmax); jj=np.where(mask)[0]; j=jj[np.argmax(grad[mask])]; i04=int(np.argmin(np.abs(centers-0.04)))
    M=float(np.sum(U[:,0]*vol)); Et=float(np.sum(U[:,2]*vol))
    return {"N":N,"t":t,"rmax":rmax,"shock_r":float(centers[j]),"mdot_r004":float(mdot[i04]),"rho_max":float(rho.max()),
            "mass_res":float(((M-M0)+bmass)/M0),"energy_res":float(((Et-E0)+benergy-srcenergy)/E0)}

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--full",action="store_true"); args=ap.parse_args()
    print("A12 literature-constrained transport numbers")
    for M in (1e10,1e11,2e11,5e11): print(transport_numbers(M))
    Ns=[128,256,512]+([1024] if args.full else [])
    print("\n1e10-kg A_cap shock convergence at t=0.8")
    for N in Ns: print(run(N=N,t_end=0.8,rmax=10.0))
    print("\nLong-domain shock propagation, N=256")
    for te in (0.8,1.2,1.6,2.0): print(run(N=256,t_end=te,rmax=30.0))
    print("\nInterpretation")
    print("- shock position converges much faster than inner Mdot")
    print("- the current A=1/Xi partial-sink branch is not stationary: the shock propagates outward")
    print("- inner flux decreases with resolution/time; no finite stationary shock-regulated Mdot is claimed")
    print("- Re/Pe show physical viscosity/conduction are most relevant at 1e10 kg")
    print("- consistent dissipative PDE requires a thermodynamically consistent Fe/Ni EOS/T mapping")
    print("- Wang 2014 is legacy/sensitivity only after Sjostrom-Crockett 2018 high-pressure pseudopotential revision")
    print("- full tabulated Zbar(rho,T) remains OPEN")
if __name__=="__main__": main()
