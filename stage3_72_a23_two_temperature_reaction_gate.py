#!/usr/bin/env python3
"""Stage 3.72 / A23: two-temperature + weak-reaction timescale gate.

This audit does not extrapolate a laboratory WDM Fe relaxation time through the
entire BH inflow. It uses the published 2.6 ps warm-dense-Fe relaxation time as
an OUTER/near-solid-density scale comparison only and carries forward the A8/A9
weak-reaction transit-time gates.

Purpose:
- decide where a one-temperature closure is at least timescale-plausible;
- identify where Te/Ti must remain independent state variables;
- prevent energetic reaction thresholds from being mislabeled as equilibrium.
"""

from __future__ import annotations

from math import sqrt

G = 6.67430e-11
C_EFF = 10.4355e3

MASSES = (1e10, 1e11, 2e11, 5e11)

# Fernandez-Panella et al., PRB 101, 184309 (2020): characteristic warm-dense
# Fe electron-phonon/electron-ion relaxation time in their experimental/TTM
# state near Te~19000 -> ~10000 K, Ti~10000 K, near-solid density.
TAU_EI_WDM_FE = 2.6e-12
TAU_EI_WDM_FE_ERR = 0.1e-12

# A9 residence-time gates at the A8 electron-capture energetic thresholds,
# M=1e11 kg reduced fast branch.
T_RES_NI_THRESHOLD = 9.13e-14
T_RES_FE_THRESHOLD = 1.50e-17

# Aggressive published 56Fe EC benchmark used in A8:
LAMBDA_EC_FE_BENCH = 1.5916e4  # s^-1
TAU_EC_FE_BENCH = 1.0 / LAMBDA_EC_FE_BENCH


def bondi_radius(M: float) -> float:
    return G * M / C_EFF**2


def crossing_time(M: float) -> float:
    return bondi_radius(M) / C_EFF


def main() -> None:
    print("Stage 3.72 / A23 two-temperature + reaction gate")
    print(f"published outer WDM-Fe tau_ei={TAU_EI_WDM_FE:.3e} +/- {TAU_EI_WDM_FE_ERR:.1e} s")
    print("\nOuter r_B/c_eff comparison")
    print("M_kg,r_B_m,t_cross_s,tau_ei/t_cross")
    for M in MASSES:
        rb = bondi_radius(M)
        tc = crossing_time(M)
        print(f"{M:.6e},{rb:.12e},{tc:.12e},{TAU_EI_WDM_FE/tc:.12e}")

    print("\nInterpretation of outer comparison")
    print("- tau_ei/t_cross <<1: one-temperature response can be timescale-plausible")
    print("- tau_ei/t_cross ~1: explicit Te/Ti closure is important")
    print("- tau_ei/t_cross >1: advection can outrun the laboratory relaxation benchmark")
    print("- laboratory tau_ei is NOT extrapolated to deep density/temperature")

    print("\nA8/A9 weak-reaction gates @1e11 kg")
    print(f"Ni threshold t_res={T_RES_NI_THRESHOLD:.12e} s -> required rate={1/T_RES_NI_THRESHOLD:.12e} s^-1")
    print(f"Fe threshold t_res={T_RES_FE_THRESHOLD:.12e} s -> required rate={1/T_RES_FE_THRESHOLD:.12e} s^-1")
    print(f"published aggressive Fe EC benchmark lambda={LAMBDA_EC_FE_BENCH:.12e} s^-1")
    print(f"published aggressive Fe EC benchmark tau={TAU_EC_FE_BENCH:.12e} s")
    print(f"Fe benchmark / required-rate ratio={LAMBDA_EC_FE_BENCH/(1/T_RES_FE_THRESHOLD):.12e}")
    print(f"Fe reaction-time / residence-time={TAU_EC_FE_BENCH/T_RES_FE_THRESHOLD:.12e}")

    print("\nGate status")
    print("OUTER Te=Ti everywhere assumption: NOT JUSTIFIED AS A UNIVERSAL CLOSURE")
    print("OUTER two-temperature dynamics: REQUIRED SENSITIVITY, especially low-mass branch")
    print("DEEP prompt weak equilibrium in fast branch: NOT SUPPORTED by current benchmark")
    print("STALLED/backpressure weak processing: remains OPEN because residence time can grow")
    print("FULL closure requires G(rho,Te,Ti,X), Ce, Ci, Ke/Ki and reaction rates on the actual path")


if __name__ == "__main__":
    main()
