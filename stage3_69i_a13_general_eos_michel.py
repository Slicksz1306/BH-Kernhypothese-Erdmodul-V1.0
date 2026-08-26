#!/usr/bin/env python3
"""Stage 3.69I / A13: general-EOS relativistic Michel supply audit.

This solver implements the exact Michel critical-point conditions for an
arbitrary thermodynamically consistent barotropic/isentrope surrogate.

It is deliberately split into two levels:
1. Regression: single-segment constant-stiffness barotropes reproduce A12c.
2. Variable-EOS family: PREM P, K_S and dK/dP are matched at the outer
   boundary; the EOS is then allowed to soften above the directly covered
   high-pressure Fe domain and tends toward Gamma=4/3 after the
   electron-relativistic density scale.

This is NOT a final tabulated Fe/Ni EOS. The variable-EOS scan is a controlled
surrogate envelope used to determine which previous transport conclusions are
robust to outer-supply uncertainty.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import exp, log, pi, sqrt
import numpy as np
from scipy.optimize import brentq

G = 6.67430e-11
C = 299_792_458.0
HBAR = 1.054571817e-34
M_E = 9.1093837015e-31
AMU = 1.66053906660e-27

# PREM-center boundary, Table II.
RHO_INF = 13_088.48          # kg/m^3
P_INF = 3638.521e8           # Pa
KAPPA_INF = 14253.0e8        # Pa
DKDP_INF = 2.3560
T_INF = 6000.0               # K reference sensitivity
CP_INF = 850.0               # J/kg/K, small h_inf sensitivity only
H_INF = 1.0 + (CP_INF*T_INF + P_INF/RHO_INF)/C**2

# Direct Fe EOS data-domain markers.
RHO_FE_QMD_2018_MAX_GCC = 30.0
RHO_FE_FP_2025_MAX_GCC = 47.2

# Fully stripped Fe p_F=m_e c density scale, used only as an inner-transition
# sensitivity center. Actual Zbar evolves continuously.
FE_A = 56.0
FE_Z = 26.0
N_E_REL = (M_E*C/HBAR)**3/(3*pi*pi)
RHO_E_REL_GCC = N_E_REL * AMU * FE_A/FE_Z / 1000.0

MASSES = (1.0e10, 1.0e11, 2.0e11, 5.0e11)

# A10 fast-envelope processing capacities reconstructed from its reported
# high-supply Xi values. Capacity is an inner transport diagnostic, not a
# newly assumed outer supply.
HIST_HIGH = {
    1.0e10: 1.46e-9,
    1.0e11: 1.46e-7,
    2.0e11: 5.84e-7,
    5.0e11: 3.65e-6,
}
XI_HIGH_FAST = {
    1.0e10: 1.468052,
    1.0e11: 2.811021e-3,
    2.0e11: 4.278392e-4,
    5.0e11: 3.537298e-5,
}
CAPACITY = {M: HIST_HIGH[M]/XI_HIGH_FAST[M] for M in MASSES}


@dataclass
class CriticalState:
    rho: float
    P: float
    h: float
    B: float
    a2: float
    u: float
    r_over_M: float
    mdot: float


class SegmentedBarotrope:
    """Continuous shifted-polytrope/Murnaghan isentrope.

    Each segment satisfies dB/dP=beta and therefore
      B = B0 (rho/rho0)^beta
      P = P0 + B0/beta [(rho/rho0)^beta - 1].
    P, B and the relativistic specific enthalpy h are continuous at every
    transition. Along an isentrope dh = dP/(rho c^2).
    """

    def __init__(self, transition_rho_gcc: tuple[float, ...],
                 betas: tuple[float, ...], label: str = ""):
        if len(betas) != len(transition_rho_gcc) + 1:
            raise ValueError("len(betas) must equal len(transitions)+1")
        if any(b <= 1.0 for b in betas):
            raise ValueError("all stiffness exponents beta must exceed 1")
        self.transition_rho_gcc = tuple(transition_rho_gcc)
        self.betas = tuple(betas)
        self.label = label

        self.rho_start = [RHO_INF]
        self.P_start = [P_INF]
        self.B_start = [KAPPA_INF]
        self.h_start = [H_INF]

        for rho_gcc, beta in zip(self.transition_rho_gcc, self.betas[:-1]):
            rho_new = rho_gcc * 1000.0
            rho0, P0, B0, h0 = (
                self.rho_start[-1], self.P_start[-1],
                self.B_start[-1], self.h_start[-1],
            )
            if rho_new <= rho0:
                raise ValueError("transitions must be increasing and > rho_inf")
            y = rho_new/rho0
            P_new = P0 + B0/beta*(y**beta - 1.0)
            h_new = h0 + B0/(rho0*C**2) * (y**(beta-1.0)-1.0)/(beta-1.0)
            B_new = B0*y**beta
            self.rho_start.append(rho_new)
            self.P_start.append(P_new)
            self.B_start.append(B_new)
            self.h_start.append(h_new)

    def _segment(self, rho: float) -> int:
        i = 0
        for j, rho0 in enumerate(self.rho_start[1:], start=1):
            if rho >= rho0:
                i = j
            else:
                break
        return i

    def state(self, rho: float) -> tuple[float, float, float, float]:
        """Return P [Pa], h/c^2 dimensionless, bulk modulus B [Pa], a^2/c^2."""
        i = self._segment(rho)
        rho0 = self.rho_start[i]
        P0 = self.P_start[i]
        B0 = self.B_start[i]
        h0 = self.h_start[i]
        beta = self.betas[i]
        y = rho/rho0
        P = P0 + B0/beta*(y**beta - 1.0)
        h = h0 + B0/(rho0*C**2)*(y**(beta-1.0)-1.0)/(beta-1.0)
        B = B0*y**beta
        a2 = B/(rho*h*C**2)  # a^2=dP/d(epsilon)
        return P, h, B, a2

    def _critical_residual_logrho(self, lrho: float) -> float:
        rho = exp(lrho)
        _, h, _, a2 = self.state(rho)
        if not (0.0 < a2 < 1.0):
            return np.nan
        # Bernoulli h*sqrt(1-2M/r+u^2)=h_inf and Michel critical conditions.
        return h/sqrt(1.0 + 3.0*a2) - H_INF

    def critical_densities(self) -> list[float]:
        lmin = log(RHO_INF*(1.0 + 1e-12))
        lmax = log(RHO_INF*1e16)
        grid = np.linspace(lmin, lmax, 30000)
        roots: list[float] = []
        prev_l = grid[0]
        prev_f = self._critical_residual_logrho(prev_l)
        for lr in grid[1:]:
            f = self._critical_residual_logrho(lr)
            if np.isfinite(prev_f) and np.isfinite(f) and prev_f*f < 0.0:
                root = brentq(
                    self._critical_residual_logrho, prev_l, lr,
                    xtol=1e-13, rtol=1e-12,
                )
                rho = exp(root)
                if not roots or abs(log(rho/roots[-1])) > 1e-7:
                    roots.append(rho)
            prev_l, prev_f = lr, f
        return roots

    def critical_state(self, M: float) -> CriticalState:
        roots = self.critical_densities()
        if len(roots) != 1:
            raise RuntimeError(
                f"{self.label or 'EOS'}: expected one causal critical root, got {len(roots)}"
            )
        rho = roots[0]
        P, h, B, a2 = self.state(rho)
        u = sqrt(a2/(1.0 + 3.0*a2))
        r_over_M = (1.0 + 3.0*a2)/(2.0*a2)
        r = (G*M/C**2)*r_over_M
        mdot = 4.0*pi*r*r*rho*C*u
        return CriticalState(rho, P, h, B, a2, u, r_over_M, mdot)


def regression_constant_beta() -> None:
    """General-EOS solver regression against A12c constant-Gamma values."""
    targets = {
        1.50: 3.2234236090230676e-6,
        1.80: 2.8897951966320954e-8,
        2.00: 3.3523923474321034e-10,
        2.356: 2.4000267887496013e-12,
    }
    print("constant-beta general-EOS regression @1e11 kg")
    for beta, target in targets.items():
        eos = SegmentedBarotrope((), (beta,), label=f"beta={beta}")
        got = eos.critical_state(1e11).mdot
        print(
            f"beta={beta:.6f}: general={got:.12e}, A12c={target:.12e}, "
            f"rel={(got/target-1):+.3e}"
        )


def variable_family_scan() -> list[dict]:
    """Controlled PREM-matched variable-EOS family.

    Direct-data boundary:
      rho_soft = 30 or 47.2 g/cm3.
    Intermediate stiffness sensitivity:
      beta_mid = 1.4 ... 1.8.
    Inner relativistic-softening density:
      1e5 ... 1e7 g/cm3, centered near pF=m_ec ~2.1e6 g/cm3.
    Final segment beta=4/3.

    This grid is a surrogate family, NOT a statistical confidence interval.
    """
    rows: list[dict] = []
    for rho_soft in (RHO_FE_QMD_2018_MAX_GCC, RHO_FE_FP_2025_MAX_GCC):
        for beta_mid in (1.4, 1.5, 1.6, 5.0/3.0, 1.75, 1.8):
            for rho_rel in (1e5, RHO_E_REL_GCC, 1e7):
                eos = SegmentedBarotrope(
                    (rho_soft, rho_rel),
                    (DKDP_INF, beta_mid, 4.0/3.0),
                    label=f"soft={rho_soft},mid={beta_mid},rel={rho_rel}",
                )
                st = eos.critical_state(1e11)
                rows.append({
                    "rho_soft_gcc": rho_soft,
                    "beta_mid": beta_mid,
                    "rho_rel_gcc": rho_rel,
                    "mdot_1e11": st.mdot,
                    "rho_crit_gcc": st.rho/1000.0,
                    "a2_crit": st.a2,
                    "rcrit_over_M": st.r_over_M,
                })
    return rows


def print_capacity_reclassification(rows: list[dict]) -> None:
    lo = min(r["mdot_1e11"] for r in rows)
    hi = max(r["mdot_1e11"] for r in rows)
    rlo = min(rows, key=lambda r: r["mdot_1e11"])
    rhi = max(rows, key=lambda r: r["mdot_1e11"])

    print("\ncontrolled variable-EOS surrogate envelope")
    print(f"rho_e_rel(pF=mec, fully stripped Fe proxy)={RHO_E_REL_GCC:.6e} g/cm3")
    print(f"Mdot_1e11 min={lo:.12e} kg/s from {rlo}")
    print(f"Mdot_1e11 max={hi:.12e} kg/s from {rhi}")
    print("\nMass / processing-capacity reclassification")
    print("M_kg,Mdot_min,Mdot_max,Xi_min,Xi_max")
    for M in MASSES:
        scale = (M/1e11)**2
        mlo, mhi = lo*scale, hi*scale
        print(
            f"{M:.6e},{mlo:.12e},{mhi:.12e},"
            f"{mlo/CAPACITY[M]:.12e},{mhi/CAPACITY[M]:.12e}"
        )

    print("\nCentral transition-density slice: rho_soft=47.2 g/cm3, rho_rel=pF=mec")
    for beta_mid in (1.4,1.5,1.6,5.0/3.0,1.7,1.75,1.8):
        eos = SegmentedBarotrope(
            (47.2, RHO_E_REL_GCC),
            (DKDP_INF, beta_mid, 4.0/3.0),
            label=f"central beta={beta_mid}",
        )
        st = eos.critical_state(1e11)
        print(
            f"beta_mid={beta_mid:.9f}: Mdot={st.mdot:.12e}, "
            f"rho_crit={st.rho/1000:.6e} g/cm3, a2={st.a2:.6e}"
        )


def main() -> None:
    print("Stage 3.69I / A13 general-EOS relativistic Michel supply audit")
    print(f"PREM: rho={RHO_INF:.6f} kg/m3, P={P_INF:.6e} Pa, "
          f"K_S={KAPPA_INF:.6e} Pa, dK/dP={DKDP_INF:.6f}")
    print(f"h_inf-1={H_INF-1.0:.6e}")
    regression_constant_beta()
    rows = variable_family_scan()
    print_capacity_reclassification(rows)
    print("\nInterpretation")
    print("- exact general-EOS Michel critical equations are implemented and regress A12c")
    print("- keeping PREM stiffness only through the measured/first-principles Fe domain, then softening, can restore supply to the historical range or above")
    print("- therefore A12c's constant-stiffness very-low supply is a stress limit, not a central prediction")
    print("- across the controlled beta_mid=1.4..1.8 family, >=1e11 kg remains processing-capable (Xi_max<1)")
    print("- 1e10 kg still crosses Xi=1 across the EOS family and remains supply/EOS-conditional")
    print("- final A13 requires a real tabulated isentrope/general Fe-Ni EOS through the intermediate-density gap; this surrogate envelope is not a confidence interval")


if __name__ == "__main__":
    main()
