#!/usr/bin/env python3
"""Stage 3.72 / A24: final net-Mdot identifiability audit.

This block asks a narrow question:
Can a unique species-resolved Mdot_BH be inferred from the currently closed
A13b/A15 reduced stack?

Answer: not yet. The code quantifies the supply/capacity margins and separates
what is numerically constrained from what still depends on open functions:
mixture EOS, permanent escape, Te/Ti transport/reactions, electron capture and
charge kinetics.

The diagnostic min(supply, capacity) is an UPPER/processing diagnostic only;
it is NOT relabeled as a demonstrated steady BH accretion rate when the system
is overloaded or when species closures are unresolved.
"""

from __future__ import annotations

MASSES = (1e10, 1e11, 2e11, 5e11)

# A13b conservative Grant-fit/T/intermediate-EOS scan at 1e11 kg.
SUPPLY_1E11 = (8.27e-8, 6.13e-6)  # kg/s

# A10 fast-envelope processing capacities reconstructed and already used by A13/A15.
CAPACITY = {
    1e10: 9.94515e-10,
    1e11: 5.19402e-5,
    2e11: 1.3650e-3,
    5e11: 1.03186e-1,
}

OPEN_FUNCTIONS = (
    "mixture EOS P(rho,Te,Ti,X), e(rho,Te,Ti,X)",
    "species-dependent permanent escape e_perm(r,E,species)",
    "electron-ion coupling G(rho,Te,Ti,X)",
    "reaction network rates and composition evolution",
    "screened-electron S-matrix / capture current",
    "stochastic charge kinetics Q(t)",
    "time-dependent hydro/backpressure state",
)


def supply_band(M: float) -> tuple[float, float]:
    scale = (M / 1e11) ** 2
    return SUPPLY_1E11[0] * scale, SUPPLY_1E11[1] * scale


def main() -> None:
    print("Stage 3.72 / A24 net-Mdot identifiability audit")
    print("M_kg,supply_min,supply_max,capacity,Xi_min,Xi_max,diagnostic_upper_min,diagnostic_upper_max")
    for M in MASSES:
        lo, hi = supply_band(M)
        cap = CAPACITY[M]
        print(
            f"{M:.6e},{lo:.12e},{hi:.12e},{cap:.12e},"
            f"{lo/cap:.12e},{hi/cap:.12e},"
            f"{min(lo,cap):.12e},{min(hi,cap):.12e}"
        )

    print("\nWhat is constrained")
    print("- A13b gives a controlled pure-Fe fit-anchored outer supply sensitivity")
    print("- A10/A15 give a reduced inner processing-capacity diagnostic")
    print("- >=1e11 kg: tested supply remains below reduced capacity")
    print("- 1e10 kg: tested supply crosses the reduced capacity")

    print("\nWhat prevents unique final Mdot_BH")
    for item in OPEN_FUNCTIONS:
        print(f"- {item}")

    print("\nIdentifiability result")
    print("UNIQUE species-resolved Mdot_BH(t): NOT IDENTIFIABLE FROM CURRENT CLOSED INPUTS")
    print("Reduced >=1e11 processing-capable conclusion: RETAINED")
    print("Reduced 1e10 EOS/supply/backpressure conditional conclusion: RETAINED")
    print("Any single final Mdot number before A20/A21/A22/A23 upstream closures: REJECTED AS FALSE PRECISION")


if __name__ == "__main__":
    main()
