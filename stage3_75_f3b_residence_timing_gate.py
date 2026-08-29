#!/usr/bin/env python3
"""Stage 3.75 / F3b — multi-pass / temporary-capture residence timing gate.

This script does NOT claim an absolute Earth-delivery probability. It combines
published Earth temporary-capture residence-time anchors with the F3 Jacobi
closure fractions to quantify how much multi-pass residence can relieve the
random Giant-Impact timing penalty.

Key point: for random impact epochs, the relevant quantity is cumulative time
spent in capture-eligible Hill states, not the raw number of loops.
"""

from __future__ import annotations

from math import exp

DAYS_PER_YEAR = 365.25

# Stage 3.74 / F3 first-passage anchor.
F3_FIRST_PASS_DAYS = 35.3

# Published Earth temporary-capture anchors.
# Granvik et al. (Icarus 218, 262-277, 2012): mean TCO duration 286 +/- 18 d,
# mean 2.88 +/- 0.82 revolutions.
EARTH_TCO_MEAN_DAYS = 286.0

# de la Fuente Marcos & de la Fuente Marcos (MNRAS 494, 1089-1097, 2020):
# 2020 CD3 median capture duration ~4 yr; some clones nearly a century.
CD3_MEDIAN_YEARS = 4.0
EXTREME_CLONE_YEARS = 100.0

# Kaplan & Cengiz (MNRAS 496, 4420-4429, 2020): examples of Earth horseshoe
# states lasting up to ~3300 yr. Treating an entire such interval as if it were
# inside the Hill sphere is intentionally impossible/capture-friendly and is
# used only as an upper-bound stress test.
COORBITAL_STRESS_YEARS = 3300.0

# Conservative F3 r>=0.1 r_H Jacobi-closure fractions. We use the average of
# the three documented velocity brackets plus the independent sigma=0.1 rerun.
P_JACOBI_10 = (0.000352 + 0.000725 + 0.000722 + 0.000624) / 4.0
P_JACOBI_30 = (0.06806 + 0.06302 + 0.05653 + 0.06580) / 4.0


def overlap_probability(cumulative_residence_years: float,
                        epoch_myr: float,
                        n_impacts: int) -> float:
    """Poisson/random-timing overlap probability.

    n_impacts is the expected number of relevant impulsive mass-growth events
    in the epoch. This is a stress-scan parameter, not an inferred terrestrial
    Giant-Impact count.
    """
    epoch_years = epoch_myr * 1.0e6
    lam = n_impacts * cumulative_residence_years / epoch_years
    return 1.0 - exp(-lam)


def print_case(name: str, residence_years: float, epoch_myr: float = 10.0) -> None:
    amp = residence_years / (F3_FIRST_PASS_DAYS / DAYS_PER_YEAR)
    print(f"\n{name}")
    print(f"  residence = {residence_years:.6g} yr")
    print(f"  amplification vs F3 first passage = {amp:.3g}x")
    print("  N_GI      P(overlap)       P10=overlap*F3Jacobi10    P30=overlap*F3Jacobi30")
    for n_gi in (1, 10, 100):
        p = overlap_probability(residence_years, epoch_myr, n_gi)
        print(f"  {n_gi:4d}   {p:12.6e}      {p*P_JACOBI_10:18.6e}      {p*P_JACOBI_30:18.6e}")


def main() -> None:
    print("Stage 3.75 / F3b — residence / timing gate")
    print(f"F3 conservative mean P_Jacobi(delta=0.10) = {P_JACOBI_10:.6e}")
    print(f"F3 conservative mean P_Jacobi(delta=0.30) = {P_JACOBI_30:.6e}")
    print("Impact counts 1/10/100 are stress tests, not a claimed formation history.")

    cases = (
        ("F3 first Hill passage", F3_FIRST_PASS_DAYS / DAYS_PER_YEAR),
        ("Published mean Earth TCO", EARTH_TCO_MEAN_DAYS / DAYS_PER_YEAR),
        ("2020 CD3 median capture", CD3_MEDIAN_YEARS),
        ("Extreme ~100 yr clone tail", EXTREME_CLONE_YEARS),
        ("3300 yr co-orbital 100%-Hill-occupancy UPPER BOUND", COORBITAL_STRESS_YEARS),
    )

    for epoch in (10.0, 100.0):
        print(f"\n=== formation epoch = {epoch:.0f} Myr ===")
        for name, residence in cases:
            print_case(name, residence, epoch)

    print("\nInterpretation")
    print("multi-pass/TCO residence amplification: PASS (real, measured/numerically established)")
    print("mean Earth TCO amplification vs F3 first pass: ~8.1x")
    print("2020 CD3 median amplification: ~41.5x")
    print("100 yr extreme-tail amplification: ~1.0e3x")
    print("generic removal of Myr random-impact timing penalty: FAIL")
    print("co-orbital lifetime != Hill-sphere occupancy; 3300 yr row is an extreme upper bound")
    print("absolute delivery probability: OPEN")


if __name__ == "__main__":
    main()
