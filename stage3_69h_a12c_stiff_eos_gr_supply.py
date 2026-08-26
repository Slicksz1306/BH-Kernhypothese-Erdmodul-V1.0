#!/usr/bin/env python3
"""Stage 3.69H / A12c: relativistic stiff-EOS Michel supply sensitivity.

Purpose
-------
Reopen the historical outer-supply benchmark by solving the exact critical
condition for a relativistic Gamma-law Michel flow. This is an EOS-sensitivity
audit, NOT a final Fe/Ni accretion-rate prediction.

The historical project supply at M=1e11 kg was
    1.47e-8 ... 1.46e-7 kg/s.
A12c asks which constant-Gamma relativistic polytropes reproduce that range
for the PREM-center outer state and how strongly the rate changes for stiffer
EOS choices.

Important limitation
--------------------
PREM dK/dP~2.356 is used only as a LOCAL stiffness proxy. Real compressed Fe/Ni
changes phase, ionizes and becomes degenerate; Gamma_eff cannot be held fixed
from the outer core to the horizon. The result therefore brackets supply
sensitivity and motivates a general-EOS Michel solver.
"""
from __future__ import annotations

from math import pi, sqrt
import numpy as np
from scipy.optimize import brentq

G = 6.67430e-11
C = 299_792_458.0

# PREM-center reference state used throughout the Earth module.
RHO_INF = 13_088.48       # kg/m^3
C_S_INF = 10.435516e3     # m/s; sqrt(K_S/rho) from PREM central values
A_INF = C_S_INF / C

# Historical project supply benchmarks.
HIST_LOW_1E11 = 1.47e-8
HIST_HIGH_1E11 = 1.46e-7
HIST_HIGH_1E10 = 1.46e-9
A10_XI_HIGH_1E10 = 1.468052
A10_CAPACITY_1E10 = HIST_HIGH_1E10 / A10_XI_HIGH_1E10

MASSES = (1.0e10, 1.0e11, 2.0e11, 5.0e11)
GAMMAS = (1.50, 5.0/3.0, 1.70, 1.75, 1.80, 1.85, 2.00, 2.20, 2.356, 2.50)


def critical_sound_speed_sq(gamma: float, a_inf: float = A_INF) -> float:
    """Solve the relativistic Michel critical-point equation for a_s^2.

    (1+3 y) [1-y/(Gamma-1)]^2
      = [1-a_inf^2/(Gamma-1)]^2,
    where y=a_s^2 in c=1 units.
    """
    if gamma <= 1.0:
        raise ValueError("gamma must exceed 1")
    rhs = (1.0 - a_inf*a_inf/(gamma-1.0))**2

    def f(y: float) -> float:
        return (1.0 + 3.0*y)*(1.0 - y/(gamma-1.0))**2 - rhs

    lo = max(a_inf*a_inf*(1.0 + 1e-10), 1e-18)
    hi = (gamma-1.0)*(1.0 - 1e-12)
    # A logarithmic/linear hybrid search robustly finds the nontrivial root.
    xs1 = np.geomspace(lo, min(1e-3, hi), 4000) if lo < min(1e-3, hi) else np.array([lo])
    xs2 = np.linspace(max(lo, min(1e-3, hi)), hi, 12000)
    xs = np.unique(np.concatenate((xs1, xs2)))
    vals = np.array([f(float(x)) for x in xs])
    roots = []
    for i in range(len(xs)-1):
        if vals[i] == 0.0:
            roots.append(float(xs[i]))
        elif vals[i]*vals[i+1] < 0.0:
            roots.append(brentq(f, float(xs[i]), float(xs[i+1]), xtol=1e-15, rtol=1e-13))
    if not roots:
        raise RuntimeError(f"no physical critical root found for gamma={gamma}")
    return max(roots)


def lambda_gr(gamma: float, a_inf: float = A_INF) -> tuple[float, float]:
    """Return (lambda_GR, a_s^2) for a relativistic Gamma-law Michel flow."""
    y = critical_sound_speed_sq(gamma, a_inf)
    a_s = sqrt(y)
    lam = (
        (a_s/a_inf)**((5.0-3.0*gamma)/(gamma-1.0))
        * ((gamma-1.0-a_inf*a_inf)/(gamma-1.0-y))**(1.0/(gamma-1.0))
        * (1.0+3.0*y)**1.5 / 4.0
    )
    return lam, y


def mdot_si(M_kg: float, gamma: float) -> tuple[float, float, float]:
    """Relativistic Gamma-law Michel mass supply in kg/s."""
    lam, y = lambda_gr(gamma)
    mdot = 4.0*pi*lam*G*G*M_kg*M_kg*RHO_INF/(C_S_INF**3)
    return mdot, lam, y


def gamma_for_mdot(target: float, M_kg: float = 1.0e11,
                    lo: float = 1.67, hi: float = 2.20) -> float:
    """Invert the constant-Gamma sensitivity curve for a target Mdot."""
    def f(gamma: float) -> float:
        return mdot_si(M_kg, gamma)[0] - target
    return brentq(f, lo, hi, xtol=1e-12, rtol=1e-11)


def xi_1e10(gamma: float) -> float:
    """Recompute A10 fast-envelope capacity ratio using the GR supply."""
    return mdot_si(1.0e10, gamma)[0] / A10_CAPACITY_1E10


def main() -> None:
    print("Stage 3.69H / A12c stiff-EOS GR/Michel supply sensitivity")
    print(f"rho_inf={RHO_INF:.6f} kg/m3")
    print(f"c_s_inf={C_S_INF:.6f} m/s, a_inf={A_INF:.12e}")
    print(f"A10 inferred 1e10 fast-envelope capacity={A10_CAPACITY_1E10:.12e} kg/s")
    print()

    print("M=1e11 kg constant-Gamma GR sensitivity")
    print("Gamma, lambda_GR, a_s^2, Mdot_kg_s, Xi_1e10")
    for gamma in GAMMAS:
        mdot, lam, y = mdot_si(1.0e11, gamma)
        print(f"{gamma:.9f}, {lam:.12e}, {y:.12e}, {mdot:.12e}, {xi_1e10(gamma):.12e}")

    g_low = gamma_for_mdot(HIST_LOW_1E11)
    g_high = gamma_for_mdot(HIST_HIGH_1E11)
    # Higher Mdot corresponds to the softer/smaller Gamma.
    print("\nHistorical project range mapped to constant-Gamma sensitivity")
    print(f"Mdot_high={HIST_HIGH_1E11:.6e} -> Gamma={g_high:.9f}")
    print(f"Mdot_low ={HIST_LOW_1E11:.6e} -> Gamma={g_low:.9f}")

    g_xi1 = brentq(lambda g: xi_1e10(g)-1.0, 1.67, 1.95, xtol=1e-12, rtol=1e-11)
    print(f"\n1e10 capacity threshold Xi=1 at Gamma~{g_xi1:.9f}")

    print("\nMass scan")
    for gamma in (1.75,1.80,1.85,2.00,2.356):
        print(f"Gamma={gamma:.6f}")
        for M in MASSES:
            print(f"  M={M:.3e} kg -> Mdot={mdot_si(M,gamma)[0]:.12e} kg/s")

    print("\nInterpretation")
    print("- the historical Michel range is EOS-sensitive, not a universal outer-supply rate")
    print("- a stiffer constant-Gamma GR sensitivity can reduce supply by orders of magnitude")
    print("- PREM dK/dP~2.356 is only a LOCAL stiffness proxy and must not be extended unchanged to the horizon")
    print("- >=1e11 processing-capable conclusions become easier if the true supply is smaller")
    print("- the 1e10 backpressure branch is conditional on sufficiently high/soft-EOS supply")
    print("- final supply requires a piecewise/general-EOS relativistic Michel solver with Fe/Ni ionization/degeneracy")


if __name__ == "__main__":
    main()
