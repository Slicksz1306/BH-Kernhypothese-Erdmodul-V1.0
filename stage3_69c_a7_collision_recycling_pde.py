#!/usr/bin/env python3
"""Stage 3.69C / A-7: corrected collision-regime map + recycling/backpressure test.

This reduced solver does four things:
1. Corrects the A-6 collision-length shortcut by enforcing radial density/temperature scalings.
2. Brackets strong-coupling (roughly geometric) versus weak-coupling Coulomb behavior.
3. Solves the exact repeated-encounter/escape probability model.
4. Optionally runs a 1-D spherical Euler Bondi benchmark with absorbing or reflecting inner boundary.

It is a regime/closure test, NOT a final dense-Fe EOS or transport solution.
"""
from __future__ import annotations
from math import pi, sqrt, exp
import argparse

G = 6.67430e-11
C = 299_792_458.0
KB = 1.380649e-23
EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19

M_BH = 1.0e11
RHO_INF = 13_088.5
C_INF = 10.4355e3
T_INF = 6000.0

A_I0 = 1.1925764049670166e-10
LAMBDA_GEOM0 = 1.1243718173803313e-10
R_B = G*M_BH/C_INF**2
R_S = 2*G*M_BH/C**2
ELL_CRIT = 4*G*M_BH/C
GAMMA_FLOW = 5.0/3.0
MICHEL_LOW = 1.47e-8
MICHEL_HIGH = 1.46e-7


def gamma_coupling0(z_eff: float) -> float:
    coul = z_eff*z_eff*E_CHARGE**2/(4*pi*EPS0*A_I0)
    return coul/(KB*T_INF)


def gamma_coupling(x: float, z_eff: float) -> float:
    # rho~r^-3/2 -> a_i~r^1/2; T~r^-1 -> Gamma~r^1/2.
    return gamma_coupling0(z_eff)*sqrt(x)


def kn_geometric(x: float) -> float:
    # Constant geometric collision cross section: lambda~rho^-1~r^3/2, Kn~r^1/2.
    kn_b=LAMBDA_GEOM0/R_B
    return kn_b*sqrt(x)


def kn_coulomb(x: float, kn_b: float) -> float:
    # Weak-coupling Coulomb: lambda_C~T^2/n~r^-1/2 -> Kn~r^-3/2.
    return kn_b*x**(-1.5)


def x_coulomb_transition(kn_b: float) -> float:
    return kn_b**(2.0/3.0)


def loss_cone_at_x(x: float, gamma: float=GAMMA_FLOW) -> dict:
    r=R_B*x
    cs=C_INF/sqrt(x)
    sigma_perp=cs/sqrt(gamma)
    ell_typ=r*sigma_perp
    p=min(1.0,0.5*(ELL_CRIT/ell_typ)**2)
    vff=sqrt(2*G*M_BH/r)
    tcycle=r/vff
    return dict(r=r, cs=cs, ell_typ=ell_typ, p=p, tcycle=tcycle)


def reservoir_mass(x_inner: float) -> float:
    # Integral of rho_inf*(r_B/r)^3/2 from x_inner*r_B to r_B.
    return (8*pi/3)*RHO_INF*R_B**3*(1-x_inner**1.5)


def eventual_capture(p: float, e: float) -> float:
    """Capture p, permanent escape e, otherwise recycle."""
    if p<0 or e<0 or p+e>1+1e-15:
        raise ValueError("Need p>=0, e>=0, p+e<=1")
    if p+e==0:
        return 0.0
    return p/(p+e)


def escape_for_chi(p: float, chi: float) -> float:
    if not 0<chi<=1:
        raise ValueError
    return p*(1/chi-1)


def print_regime_map():
    print("Stage 3.69C / A-7 corrected collision/recycling map")
    print(f"r_B={R_B:.9e} m, r_s={R_S:.9e} m, lambda_geom0/r_B={LAMBDA_GEOM0/R_B:.6e}")
    print()
    print("Strong-coupling/geometric proxy:")
    for x in (1.0,1e-1,1e-2,1e-3,1e-4,1e-6):
        print(f"x=r/rB={x:.1e}: Kn_geom={kn_geometric(x):.6e}")
    print("=> under this proxy Kn decreases inward; no inner collisionless transition.")
    print()
    print("Ion coupling proxy (T_inf=6000 K sensitivity):")
    for z in (1,2,4,8,26):
        g0=gamma_coupling0(z)
        x1=1/g0**2
        print(f"Zeff={z:2d}: Gamma_B={g0:.6e}, Gamma=1 at x~{x1:.6e} ({x1*R_B/R_S:.3e} r_s)")
    print()
    print("Weak-coupling Coulomb branch, parameterized by Kn_C(r_B):")
    for kb in (1e-4,3e-4,1e-3,3e-3,1e-2):
        x=x_coulomb_transition(kb)
        lc=loss_cone_at_x(x)
        p=lc["p"]
        tabs=lc["tcycle"]/p
        mres=reservoir_mass(x)
        cap=mres/tabs
        print(f"KnB={kb:.1e}: x_coll={x:.6e}, r={x*R_B:.3e} m, "
              f"p_single={p:.3e}, tcap={tabs:.3e} s, "
              f"Mres/tcap={cap:.3e} kg/s = {cap/MICHEL_HIGH:.3f} x Michel_high")
    print()
    p_ref=8.80629243141394e-6
    print(f"Repeated-encounter escape map using p_ref={p_ref:.6e}:")
    for chi in (1.0,0.7,0.3,0.1,0.01,1e-3,1e-4,1e-5):
        e=escape_for_chi(p_ref,chi)
        feasible=e<=1-p_ref
        print(f"chi={chi:.5g}: required permanent escape e={e:.6e} per encounter, feasible={feasible}")
    print()
    print("Interpretation:")
    print("- single-pass p is NOT the stationary Mdot factor unless almost all misses are permanently removed;")
    print("- a truly reflecting/back-pressure boundary can suppress supply, but is a different closure from recycling;")
    print("- strong-coupling and weak-Coulomb radial collisionality predict opposite Kn trends;")
    print("- dense-Fe ionization/coupling/EOS determines which branch is realized.")


# ---------- optional controlled 1-D Bondi Euler benchmark ----------
def bondi_lambda(g):
    rc=(5-3*g)/4
    yc=2/(5-3*g)
    lam=rc**2*yc**(1/(g-1))*sqrt(yc)
    return lam,rc,yc


def _bondi_state(r,g):
    import numpy as np
    from scipy.optimize import brentq
    lam,rc,yc=bondi_lambda(g)
    if abs(r-rc)/rc<1e-6:
        y=yc
    else:
        def f(z):
            y=exp(z)
            return 0.5*lam**2/(r**4*y**(2/(g-1))) + y/(g-1)-1/r-1/(g-1)
        zs=np.linspace(-12,16,500)
        fs=[f(z) for z in zs]
        roots=[]
        for i in range(len(zs)-1):
            if fs[i]*fs[i+1]<0:
                roots.append(exp(brentq(f,zs[i],zs[i+1])))
        y=yc if not roots else (max(roots) if r>rc else min(roots))
    rho=y**(1/(g-1))
    v=-lam/(r*r*rho)
    p=rho*y/g
    E=p/(g-1)+0.5*rho*v*v
    return rho,v,p,E


def _p2c(rho,v,p,g):
    import numpy as np
    return np.array([rho,rho*v,p/(g-1)+0.5*rho*v*v],float)


def _prim(U,g):
    rho=U[:,0]; v=U[:,1]/rho; p=(g-1)*(U[:,2]-0.5*rho*v*v)
    return rho,v,p


def _flux(U,g):
    import numpy as np
    rho,v,p=_prim(U,g); E=U[:,2]
    return np.column_stack((rho*v,rho*v*v+p,v*(E+p)))


def _hll(UL,UR,g):
    import numpy as np
    rhoL,vL,pL=_prim(UL,g); rhoR,vR,pR=_prim(UR,g)
    aL=np.sqrt(g*pL/rhoL); aR=np.sqrt(g*pR/rhoR)
    sL=np.minimum(vL-aL,vR-aR); sR=np.maximum(vL+aL,vR+aR)
    FL=_flux(UL,g); FR=_flux(UR,g)
    F=(sR[:,None]*FL-sL[:,None]*FR+(sL*sR)[:,None]*(UR-UL))/(sR-sL)[:,None]
    F[sL>=0]=FL[sL>=0]; F[sR<=0]=FR[sR<=0]
    return F


def _scalar_flux(U,g):
    import numpy as np
    rho=U[0]; v=U[1]/rho; p=(g-1)*(U[2]-0.5*rho*v*v)
    return np.array([rho*v,rho*v*v+p,v*(U[2]+p)])


def _scalar_hll(UL,UR,g):
    def pp(U):
        rho=U[0];v=U[1]/rho;p=(g-1)*(U[2]-0.5*rho*v*v)
        return rho,v,p
    rL,vL,pL=pp(UL);rR,vR,pR=pp(UR)
    aL=sqrt(g*pL/rL);aR=sqrt(g*pR/rR)
    sL=min(vL-aL,vR-aR);sR=max(vL+aL,vR+aR)
    FL=_scalar_flux(UL,g);FR=_scalar_flux(UR,g)
    if sL>=0:return FL
    if sR<=0:return FR
    return (sR*FL-sL*FR+sL*sR*(UR-UL))/(sR-sL)


def run_pde(inner="absorb", absorb_fraction=1.0, t_end=0.4, N=240):
    import numpy as np
    g=1.5; rmin=0.03; rmax=10.0; cfl=0.30
    faces=np.geomspace(rmin,rmax,N+1)
    centers=(0.5*(faces[:-1]**3+faces[1:]**3))**(1/3)
    vol=(faces[1:]**3-faces[:-1]**3)/3
    U=np.empty((N,3))
    for i,r in enumerate(centers):
        ro,v,p,E=_bondi_state(r,g);U[i]=[ro,ro*v,E]
    q=faces[-1]/faces[-2]; rg=centers[-1]*q
    ro,v,p,E=_bondi_state(rg,g); Uouter=np.array([ro,ro*v,E])
    t=0; step=0
    while t<t_end:
        rho,v,p=_prim(U,g)
        if rho.min()<=0 or p.min()<=0:
            raise RuntimeError("nonphysical PDE state")
        a=np.sqrt(g*p/rho)
        dt=cfl*np.min((faces[1:]-faces[:-1])/(np.abs(v)+a))
        dt=min(dt,t_end-t)
        F=np.empty((N+1,3))
        if inner=="absorb":
            F[0]=_scalar_flux(U[0],g)
        else:
            rho0=U[0,0];v0=U[0,1]/rho0;p0=(g-1)*(U[0,2]-0.5*rho0*v0*v0)
            ghost=_p2c(rho0,-v0,p0,g)
            wall=_scalar_hll(ghost,U[0],g)
            out=_scalar_flux(U[0],g)
            F[0]=absorb_fraction*out+(1-absorb_fraction)*wall
        F[1:N]=_hll(U[:-1],U[1:],g)
        F[N]=_scalar_hll(U[-1],Uouter,g)
        src=np.column_stack((np.zeros(N),2*p/centers-rho/centers**2,-rho*v/centers**2))
        U += -dt/vol[:,None]*(faces[1:,None]**2*F[1:]-faces[:-1,None]**2*F[:-1])+dt*src
        t+=dt;step+=1
    rho,v,p=_prim(U,g)
    mdot=-centers**2*rho*v
    lam,_,_=bondi_lambda(g)
    print(f"PDE: inner={inner}, A={absorb_fraction}, t={t:.3f} rB/cinf, steps={step}, analytic lambda={lam:.6f}")
    for rr in (0.04,0.08,0.12,0.2,0.5,1.0,2.0,5.0):
        i=int(np.argmin(np.abs(centers-rr)))
        mach=abs(v[i])/sqrt(g*p[i]/rho[i])
        print(f"r={centers[i]:.4f}: mdot/(4pi rhoinf c rB^2)={mdot[i]: .6f}, Mach={mach:.4f}")
    print("A reflecting result is a back-pressure extreme, NOT a kinetic-recycling model.")


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--pde",choices=["none","absorb","reflect"],default="none")
    ap.add_argument("--absorb-fraction",type=float,default=0.0)
    ap.add_argument("--t-end",type=float,default=0.4)
    args=ap.parse_args()
    print_regime_map()
    if args.pde!="none":
        run_pde(args.pde,args.absorb_fraction,args.t_end)


if __name__=="__main__":
    main()
