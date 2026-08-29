#!/usr/bin/env python3
"""Stage 3.72 / A31: ambipolar mobility/current-balance identifiability gate.

The Nernst-Einstein ionic conductivity is used ONLY as a deliberately simple
stress proxy.  In strongly coupled multicomponent WDM, exact charge/mass
transport requires Maxwell-Stefan/Onsager cross coefficients; tracer/self
D alone is not a complete electrical mobility closure.
"""

E = 1.602176634e-19
K_B = 1.380649e-23
N_I = 1.4075e29            # m^-3, project outer Fe ion-density proxy
T = 6000.0                 # K, outer reference
D_RANGE = (2.47e-9, 3.37e-9)  # m^2/s, published Fe/Ni self-D envelope
ZBAR_RANGE = (2.76, 26.0)      # A12b/A14 endpoints
SIGMA_E_MIN = 9.2e5        # S/m, experimental Fe-Ni-Si outer-core lower limit benchmark


def sigma_ion_ne(zbar: float, D: float) -> float:
    return N_I * (zbar*E)**2 * D/(K_B*T)


def main():
    print("Stage 3.72 / A31 ambipolar mobility gate")
    vals=[]
    for z in ZBAR_RANGE:
        for D in D_RANGE:
            s=sigma_ion_ne(z,D)
            vals.append(s)
            print(f"Zbar={z:.3f}, D={D:.6e} m2/s -> sigma_i_NE={s:.6e} S/m, sigma_e_min/sigma_i={SIGMA_E_MIN/s:.6e}")
    print(f"\nnaive ionic NE envelope={min(vals):.6e} ... {max(vals):.6e} S/m")
    print(f"electronic lower-limit benchmark={SIGMA_E_MIN:.6e} S/m")
    print(f"electron/ion conductivity dominance={SIGMA_E_MIN/max(vals):.6e} ... {SIGMA_E_MIN/min(vals):.6e}")

    print("\nInterpretation")
    print("- even an independent-ion Nernst-Einstein stress proxy leaves electronic transport dominant")
    print("- the fully-ionized Z=26 endpoint is deliberately extreme and still gives electron dominance ~O(10)")
    print("- at Zbar~2.76 the dominance is O(1e3)")
    print("- self/tracer D does NOT determine the multicomponent charge-current response")
    print("- Maxwell-Stefan/Onsager cross coefficients and chemical-potential derivatives are required")
    print("- therefore exact ambipolar E(r) and floating/current-balance Q_eq remain non-identifiable from current public inputs")
    print("- do not use this NE proxy as a final ionic conductivity or Q_eq prediction")


if __name__ == "__main__":
    main()
