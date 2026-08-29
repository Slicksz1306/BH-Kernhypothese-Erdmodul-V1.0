#!/usr/bin/env python3
"""Stage 3.72 / A27: collective quasineutral charge-response audit.

This is a reduced timescale/consistency test.  It does NOT solve the final
nonlinear dense-plasma floating potential or Q(t).  It asks whether the naive
independent ion/electron current mismatch from A26 can persist long enough to
build a multi-e charge before the conducting, degenerate plasma rearranges.
"""
from math import pi, sqrt

EPS0 = 8.8541878128e-12
E = 1.602176634e-19
M_E = 9.1093837015e-31

# A14/A26 endpoints at the PREM central reference state.
NE_LOW = 3.88e29       # m^-3, Zbar~2.76 endpoint
NE_HIGH = 3.66e30      # m^-3, fully-ionized upper proxy
LAMBDA_TF = (2.95e-11, 4.29e-11)  # m
V_F = (2.612e6, 5.519e6)           # m/s

# Outer-core metallic conductivity comparison scale.  Literature values for
# liquid Fe/alloys are O(1e6 S/m); this is a benchmark, not a full radial law.
SIGMA_E = 1.0e6        # S/m

# Previously calculated project timescales.
T_BUILD_A26 = (5.7e-13, 5.4e-12)  # s: naive +5e buildup endpoints
T_EI_A23 = 2.6e-12                 # s: published warm-dense Fe anchor
R_B_1E11 = 6.13e-8                 # m
C_EFF = 10.4355e3                   # m/s


def omega_pe(ne: float) -> float:
    return sqrt(ne * E * E / (EPS0 * M_E))


def main() -> None:
    print("Stage 3.72 / A27 collective charge-response audit")
    print("\nElectron collective response")
    for ne in (NE_LOW, NE_HIGH):
        w = omega_pe(ne)
        print(
            f"ne={ne:.6e} m^-3  omega_pe={w:.6e} s^-1  "
            f"1/omega_pe={1/w:.6e} s  period={2*pi/w:.6e} s"
        )

    tau_M = EPS0 / SIGMA_E
    print(f"\nMaxwell relaxation benchmark @sigma={SIGMA_E:.3e} S/m: tau_M={tau_M:.6e} s")

    print("\nThomas-Fermi layer transit times")
    vals = []
    for lam in LAMBDA_TF:
        for vf in V_F:
            t = lam / vf
            vals.append(t)
            print(f"lambda={lam:.3e} m, vF={vf:.3e} m/s -> t={t:.6e} s")
    print(f"TF transit envelope={min(vals):.6e} ... {max(vals):.6e} s")

    t_cross = R_B_1E11 / C_EFF
    print(f"\nA23/A26 comparison: rB/c_eff @1e11={t_cross:.6e} s")
    print(f"tau_ei anchor={T_EI_A23:.6e} s")
    for t in T_BUILD_A26:
        print(f"A26 naive +5e buildup={t:.6e} s = {t/tau_M:.6e} tau_M")
    print(f"tau_ei/tau_M={T_EI_A23/tau_M:.6e}")
    print(f"(rB/c_eff)/tau_M={t_cross/tau_M:.6e}")

    print("\nInterpretation")
    print("- collective electrostatic rearrangement occurs O(1e5...1e6) faster than the naive A26 charge buildup/hydro scales")
    print("- independent ion/electron gas currents cannot remain unmodified while multi-e charge accumulates")
    print("- on hydro timescales Q should be treated as a quasi-static collective current-balance variable")
    print("- exact Q_eq still requires nonlinear screening, species transport/mobility and sink-boundary closure")
    print("- this is NOT a proof that Q_eq lies at any specific number of elementary charges")


if __name__ == "__main__":
    main()
