#!/usr/bin/env python3
"""Stage 3.70B / A18: current real-data identifiability audit.

Updates the H+ high-energy antineutrino comparison using the 2026 SK-Gd
publication while retaining the stronger valid SK-IV constraint. For H0 it
records whether a unique observable prediction exists for a real-data likelihood.
"""

PROJECT_HPLUS = (0.098, 0.122)  # cm^-2 s^-1 MeV^-1, project reinterpretation
SKIV_2021_OBS = 0.04            # 25.29--31.29 MeV, repeated in 2026 SK-Gd paper
SKGD_2026_NN_OBS = 0.13
SKGD_2026_BDT_OBS = 0.16


def ratio_band(limit):
    return PROJECT_HPLUS[0]/limit, PROJECT_HPLUS[1]/limit


def main():
    print("Stage 3.70B / A18 current real-data audit")
    for name,lim in (
        ("SK-IV observed 90% CL",SKIV_2021_OBS),
        ("SK-VI+VII NN observed 90% CL",SKGD_2026_NN_OBS),
        ("SK-VI+VII BDT observed 90% CL",SKGD_2026_BDT_OBS),
    ):
        lo,hi=ratio_band(lim)
        print(f"{name}: limit={lim:.6f}, project/limit={lo:.6f}...{hi:.6f}")

    print("\nInterpretation")
    print("- the 2026 SK-Gd-only high-energy limits are weaker than the old SK-IV bin limit")
    print("- the project H+ flux is below the standalone 2026 SK-Gd limits but remains above the strongest published SK-IV bin limit")
    print("- therefore H+ remains FAIL in the project's bin-by-bin reinterpretation against the strongest published constraint")
    print("- the 2026 broad-band DSNB indication is not evidence for an Earth-centered BH source")
    print("- H0 still lacks a unique macroscopic seismic/thermal/neutrino amplitude needed for a full data likelihood")

if __name__=='__main__':
    main()
