#!/usr/bin/env python3
"""Stage 3.69I / A13b: Grant-2021 liquid-Fe experimental-fit outer-EOS anchor.

Purpose
-------
Use the published analytic liquid-Fe EOS fit from Grant et al. (2021),
DOI 10.1029/2020JB020008, as an experimentally anchored outer segment of the
A13 general-EOS Michel calculation.

Important limitation
--------------------
This is NOT direct ingestion of the Zenodo raw P-rho traces or the SESAME 92141
table. The Grant experiment constrains an elevated-temperature liquid-Fe
isentrope roughly over 275--400 GPa. We therefore use the published fit only
through 400 GPa, anchor it to the PREM central boundary, and retain an explicit
intermediate-density sensitivity family above that pressure.

No experimental points are fabricated or digitized from figures.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import exp, log, pi, sqrt
import itertools
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq

G = 6.67430e-11
C = 299_792_458.0
R = 8.31446261815324
M_MOLAR_FE = 55.845e-3  # kg/mol

# PREM center / A13 outer boundary.
RHO_INF = 13_088.48          # kg/m3
P_INF = 363.8521e9           # Pa
KAPPA_INF = 1.4253e12        # Pa
T_INF_DEFAULT = 6000.0       # K
CP_INF = 850.0               # J/kg/K
H_INF = 1.0 + (CP_INF*T_INF_DEFAULT + P_INF/RHO_INF)/C**2

# Grant et al. 2021 / Ichikawa-form reference state, 7000 K and 0 GPa.
RHO0 = 5.187e3               # kg/m3
T0 = 7000.0                  # K
K0_NOM = 25.3e9              # Pa
K0_ERR = 4.0e9
K0P_NOM = 6.60
K0P_ERR = 0.33
GAMMA0_NOM = 2.42
GAMMA0_ERR = 0.12
A_GAMMA = 1.0
B_GAMMA = 0.35
E0 = 0.314e-4                # 1/K
G_ELECTRONIC = -0.4

P_GRANT_MAX = 400.0e9        # use published experimental-fit anchor only to 400 GPa
RHO_REL_VALUES_GCC = (1.0e5, 2.10e6, 1.0e7)
BETA_MID_VALUES = (1.4, 1.5, 1.6, 5.0/3.0, 1.75, 1.8)
BETA_INNER = 4.0/3.0
MASSES = (1.0e10, 1.0e11, 2.0e11, 5.0e11)

# A10 fast-envelope inner processing capacities, as used in A13.
HIST_HIGH = {1e10:1.46e-9, 1e11:1.46e-7, 2e11:5.84e-7, 5e11:3.65e-6}
XI_HIGH_FAST = {1e10:1.468052, 1e11:2.811021e-3, 2e11:4.278392e-4, 5e11:3.537298e-5}
CAPACITY = {m:HIST_HIGH[m]/XI_HIGH_FAST[m] for m in MASSES}


@dataclass
class CriticalState:
    rho: float
    P: float
    h: float
    B: float
    a2: float
    r_over_M: float
    mdot: float


class GrantAnchoredEOS:
    def __init__(self, K0=K0_NOM, K0p=K0P_NOM, gamma0=GAMMA0_NOM,
                 T_anchor=T_INF_DEFAULT, beta_mid=1.6,
                 rho_rel_gcc=2.10e6):
        self.K0 = K0
        self.K0p = K0p
        self.gamma0 = gamma0
        self.T_anchor = T_anchor
        self.beta_mid = beta_mid
        self.rho_rel = rho_rel_gcc*1000.0

        self._Praw_inf = self.P_raw(RHO_INF)
        self.rho_t = brentq(lambda r: self.P_grant(r)-P_GRANT_MAX,
                            RHO_INF*(1+1e-10), RHO_INF*3.0)
        self.P_t = P_GRANT_MAX
        self.B_t = self.B_grant(self.rho_t)
        self.h_t = H_INF + quad(
            lambda rr: self.dPdr_grant(rr)/(rr*C**2),
            RHO_INF, self.rho_t, epsrel=1e-9, limit=100,
        )[0]

        y = self.rho_rel/self.rho_t
        b = self.beta_mid
        self.P_rel = self.P_t + self.B_t/b*(y**b-1.0)
        self.B_rel = self.B_t*y**b
        self.h_rel = self.h_t + self.B_t/(self.rho_t*C**2) * \
            (y**(b-1.0)-1.0)/(b-1.0)

    def gamma(self, rho):
        # a=1 -> gamma = gamma0*(rho0/rho)^b
        return self.gamma0*(RHO0/rho)**B_GAMMA

    def T_adiabat(self, rho):
        # d ln T / d ln rho = gamma(rho), anchored at PREM rho,T.
        expo = self.gamma0/B_GAMMA * (
            (RHO0/RHO_INF)**B_GAMMA - (RHO0/rho)**B_GAMMA
        )
        return self.T_anchor*exp(expo)

    def P_iso(self, rho):
        x = (RHO0/rho)**(1.0/3.0)
        return 3.0*self.K0*(rho/RHO0)**(2.0/3.0)*(1.0-x) * \
            exp(1.5*(self.K0p-1.0)*(1.0-x))

    def E_th(self, rho, T):
        return 3.0*R*(T + E0*(RHO0/rho)**G_ELECTRONIC*T*T)  # J/mol

    def P_raw(self, rho):
        T = self.T_adiabat(rho)
        molar_density = rho/M_MOLAR_FE
        Pth = self.gamma(rho)*molar_density * \
            (self.E_th(rho,T)-self.E_th(rho,T0))
        return self.P_iso(rho)+Pth

    def P_grant(self, rho):
        # Preserve Grant derivative but shift P so the path passes PREM exactly.
        return self.P_raw(rho)-self._Praw_inf+P_INF

    def dPdr_grant(self, rho):
        eps = 2e-6
        return (self.P_grant(rho*(1+eps))-self.P_grant(rho*(1-eps))) / \
            (2*eps*rho)

    def B_grant(self, rho):
        return rho*self.dPdr_grant(rho)

    def state(self, rho):
        if rho <= self.rho_t:
            P = self.P_grant(rho)
            h = H_INF + quad(
                lambda rr:self.dPdr_grant(rr)/(rr*C**2),
                RHO_INF, rho, epsrel=1e-8, limit=80,
            )[0]
            B = self.B_grant(rho)
        elif rho <= self.rho_rel:
            y = rho/self.rho_t
            b = self.beta_mid
            P = self.P_t+self.B_t/b*(y**b-1.0)
            B = self.B_t*y**b
            h = self.h_t+self.B_t/(self.rho_t*C**2)*(y**(b-1)-1)/(b-1)
        else:
            y = rho/self.rho_rel
            b = BETA_INNER
            P = self.P_rel+self.B_rel/b*(y**b-1.0)
            B = self.B_rel*y**b
            h = self.h_rel+self.B_rel/(self.rho_rel*C**2)*(y**(b-1)-1)/(b-1)
        a2 = B/(rho*h*C**2)
        return P,h,B,a2

    def critical_state(self, M):
        def residual(lrho):
            rho = exp(lrho)
            _,h,_,a2 = self.state(rho)
            if not (0.0 < a2 < 1.0):
                return np.nan
            return h/sqrt(1.0+3.0*a2)-H_INF

        grid = np.linspace(log(RHO_INF*(1+1e-10)), log(RHO_INF*1e16), 12000)
        roots=[]
        x0=grid[0]; f0=residual(x0)
        for x1 in grid[1:]:
            f1=residual(x1)
            if np.isfinite(f0) and np.isfinite(f1) and f0*f1 < 0:
                roots.append(brentq(residual,x0,x1,xtol=1e-12,rtol=1e-11))
            x0,f0=x1,f1
        if len(roots) != 1:
            raise RuntimeError(f"expected one causal critical root, got {len(roots)}")
        rho=exp(roots[0])
        P,h,B,a2=self.state(rho)
        u=sqrt(a2/(1.0+3.0*a2))
        r_over_M=(1.0+3.0*a2)/(2.0*a2)
        r=(G*M/C**2)*r_over_M
        mdot=4*pi*r*r*rho*C*u
        return CriticalState(rho,P,h,B,a2,r_over_M,mdot)


def nominal_scan():
    rows=[]
    for beta_mid,rho_rel in itertools.product(BETA_MID_VALUES,RHO_REL_VALUES_GCC):
        eos=GrantAnchoredEOS(beta_mid=beta_mid,rho_rel_gcc=rho_rel)
        st=eos.critical_state(1e11)
        rows.append((st.mdot,beta_mid,rho_rel,eos.rho_t,eos.B_t,st.rho))
    return rows


def uncertainty_corner_scan():
    rows=[]
    for K0,K0p,gamma0,T,beta_mid,rho_rel in itertools.product(
        (K0_NOM-K0_ERR,K0_NOM,K0_NOM+K0_ERR),
        (K0P_NOM-K0P_ERR,K0P_NOM,K0P_NOM+K0P_ERR),
        (GAMMA0_NOM-GAMMA0_ERR,GAMMA0_NOM,GAMMA0_NOM+GAMMA0_ERR),
        (5500.0,6000.0,6500.0),
        (1.4,1.8),
        (1e5,1e7),
    ):
        eos=GrantAnchoredEOS(K0,K0p,gamma0,T,beta_mid,rho_rel)
        st=eos.critical_state(1e11)
        rows.append((st.mdot,K0,K0p,gamma0,T,beta_mid,rho_rel,
                     eos.rho_t,eos.B_t,st.rho))
    return rows


def print_recoupling(lo,hi):
    print("M_kg,Mdot_min,Mdot_max,Xi_min,Xi_max")
    for M in MASSES:
        scale=(M/1e11)**2
        mlo,mhi=lo*scale,hi*scale
        print(f"{M:.6e},{mlo:.12e},{mhi:.12e},"
              f"{mlo/CAPACITY[M]:.12e},{mhi/CAPACITY[M]:.12e}")


def main():
    nominal=nominal_scan()
    nlo=min(nominal,key=lambda r:r[0]); nhi=max(nominal,key=lambda r:r[0])
    corners=uncertainty_corner_scan()
    clo=min(corners,key=lambda r:r[0]); chi=max(corners,key=lambda r:r[0])

    eos0=GrantAnchoredEOS()
    Binf=eos0.B_grant(RHO_INF)
    print("A13b Grant-2021 experimental-fit anchor")
    print(f"PREM K_S={KAPPA_INF:.9e} Pa; Grant-path B_inf={Binf:.9e} Pa; ratio={Binf/KAPPA_INF:.6f}")
    print(f"nominal 400-GPa transition rho={eos0.rho_t/1000:.6f} g/cm3, B={eos0.B_t:.9e} Pa")
    print(f"nominal Mdot_1e11={nlo[0]:.12e}...{nhi[0]:.12e} kg/s")
    print(f"corner  Mdot_1e11={clo[0]:.12e}...{chi[0]:.12e} kg/s")
    print("\nrecoupling using conservative corner envelope")
    print_recoupling(clo[0],chi[0])
    print("\nstatus: PARTIAL EMPIRICAL-FIT OUTER ANCHOR; raw Zenodo/SESAME ingestion still OPEN")

if __name__ == '__main__':
    main()
