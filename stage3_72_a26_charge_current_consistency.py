#!/usr/bin/env python3
"""Stage 3.72 / A26: charge-current consistency audit.

This deliberately constructs the naive independent-particle current balance from
existing A5 Fe capture and A25 isolated-electron <sigma v> proxies. Its purpose
is to test whether such a closure is self-consistent in dense screened matter.

It is NOT the project's preferred Q(t) model. A strong mismatch is interpreted
as evidence that collective quasineutral transport/nonlinear screening must be
included before cross sections can be converted to a charge evolution law.
"""

NI = 1.4075e29            # Fe-ion number density proxy [m^-3]
V_I = 10.4355e3           # Earth/core speed proxy [m/s]
SIGMA_FE = 2.28214e-22     # A5 Fe-56 isolated wave-capture cross section [m^2]

# A14 outer-core electron-density endpoints and A25 midpoint-screening
# zero-T Fermi-sphere <sigma v> at Q=+5e.
CASES = {
    "Zbar=2.76": {
        "Z": 2.76,
        "n_e": 3.880584362704415e29,
        "sigma_v_e_Q5": 5.332089012618544e-22,
    },
    "Z=26 upper proxy": {
        "Z": 26.0,
        "n_e": 3.6599183337772704e30,
        "sigma_v_e_Q5": 2.1457192944634492e-22,
    },
}


def main() -> None:
    ion_number_rate = NI*V_I*SIGMA_FE
    print("Stage 3.72 / A26 independent-current consistency audit")
    print(f"naive Fe ion capture number rate={ion_number_rate:.12e} s^-1")

    for label, d in CASES.items():
        positive_charge_rate = d["Z"]*ion_number_rate
        electron_rate = d["n_e"]*d["sigma_v_e_Q5"]
        ratio = positive_charge_rate/electron_rate
        t_to_5e = 5.0/positive_charge_rate
        print(f"\n{label}")
        print(f"positive ion charge current={positive_charge_rate:.12e} e/s")
        print(f"A25 isolated electron capture current @Q=5={electron_rate:.12e} e/s")
        print(f"positive/electron current ratio={ratio:.12e}")
        print(f"naive time to accumulate +5e if unopposed={t_to_5e:.12e} s")

    print("\nInterpretation")
    print("- independent gas-current closure predicts charge growth far beyond the A14 linear-screening bracket")
    print("- therefore independent A5-ion + A25-electron cross sections are NOT a self-consistent Q(t) closure")
    print("- dense plasma quasineutrality, collective electric fields, nonlinear/radial screening, recycling and bulk advection must be coupled")
    print("- the mismatch is a closure failure of the independent-particle model, not evidence that the actual BH reaches huge Q")


if __name__ == "__main__":
    main()
