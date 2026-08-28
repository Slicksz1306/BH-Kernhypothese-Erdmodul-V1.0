#!/usr/bin/env python3
"""Stage 3.69K / A15: integrated reduced net-throughput audit.

Combines the A13b Grant-fit outer-supply envelope with the A10 fast-envelope
inner processing capacities and the A6/A9 repeated-encounter logic.

This script deliberately does NOT rename supply as a final species-resolved
black-hole accretion rate.  It reports what can be inferred before the missing
full WDM/mixture/two-temperature kinetic closure is available.
"""

MASSES = (1.0e10, 1.0e11, 2.0e11, 5.0e11)

# A13b conservative Grant-fit/T/intermediate-EOS envelope at 1e11 kg.
SUPPLY_LO_1E11 = 8.27068e-8
SUPPLY_HI_1E11 = 6.12599e-6

# A10 fast-envelope capacities reconstructed in A13 from the published project
# high-supply/Xi values. They are inner processing diagnostics, not outer rates.
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

# A5 coherent whole-nucleus single-pass wave-capture ratios at 1e11 kg.
# They are shown for context only: repeated encounters mean they must NOT be
# multiplied once into the stationary supply when permanent escape is tiny.
FE56_SINGLE_PASS_RATIO = 0.99754
NI58_SINGLE_PASS_RATIO = 0.99646

# A14 screened-charge proton examples. Again these are local/single-particle
# diagnostics and not direct stationary throughput factors.
PROTON_CHARGED_RATIO_LOW = 0.925   # ~+1.6e
PROTON_CHARGED_RATIO_HIGH = 0.867  # ~+4.9e


def supply_band(M):
    scale = (M/1.0e11)**2
    return SUPPLY_LO_1E11*scale, SUPPLY_HI_1E11*scale


def main():
    print("Stage 3.69K / A15 integrated reduced net-throughput audit")
    print("M_kg,supply_min,supply_max,capacity,Xi_min,Xi_max,throughput_ceiling_min,throughput_ceiling_max")
    for M in MASSES:
        lo, hi = supply_band(M)
        cap = CAPACITY[M]
        print(
            f"{M:.6e},{lo:.12e},{hi:.12e},{cap:.12e},"
            f"{lo/cap:.12e},{hi/cap:.12e},{min(lo,cap):.12e},{min(hi,cap):.12e}"
        )

    print("\nInterpretation")
    print("- A6/A9: chi_capture=p/(p+e_perm); single-pass wave ratios are not stationary throughput factors")
    print("- A10: outer WDM shell has very large optical depth in tested envelopes, so permanent ballistic escape is strongly suppressed")
    print("- >=1e11 kg: all A13b Grant-fit branches have Xi<1; reduced inner processing is not capacity-limiting")
    print("- 1e10 kg: Xi crosses far above 1; A11/A12 time-dependent backpressure remains decisive")
    print("- min(supply,capacity) is only a throughput ceiling/diagnostic, NOT a demonstrated steady Mdot_BH for overloaded branches")
    print("- final species-resolved net Mdot still needs real mixture EOS/transport, two-temperature closure, reactions and stochastic charge kinetics")

if __name__ == '__main__':
    main()
