#!/usr/bin/env python3
"""Stage 3.72 / A30: ion transport across the Thomas-Fermi screening layer.

Uses published Fe/Ni self-diffusion coefficients along Earth's core adiabat as
an order-of-magnitude transport anchor. This is a reduced timescale audit, not
a charged-ion mobility or full ambipolar transport solution.
"""

LAMBDA_TF = (2.952e-11, 4.292e-11)      # m, A28 endpoints
D_ION = (2.47e-9, 3.37e-9)              # m^2/s, broad Fe/Ni published envelope
T_ELECTRON_RESPONSE = (8.85e-18, 2.85e-17)  # s, A27 benchmarks
T_BUILD_A26 = (5.7e-13, 5.4e-12)        # s, fully-ionized -> low-Zbar naive +5e
T_HYDRO_1E11 = 5.87e-12                 # s, r_B/c_eff


def main():
    print("Stage 3.72 / A30 ion screening-layer transport audit")
    vals=[]
    for lam in LAMBDA_TF:
        for D in D_ION:
            t=lam*lam/D
            vals.append(t)
            print(f"lambda={lam:.6e} m D={D:.6e} m2/s -> lambda^2/D={t:.6e} s")
    lo,hi=min(vals),max(vals)
    print(f"ion diffusion envelope across lambda_TF: {lo:.6e} ... {hi:.6e} s")
    print(f"vs electron response: {lo/max(T_ELECTRON_RESPONSE):.3e} ... {hi/min(T_ELECTRON_RESPONSE):.3e} times slower")
    print(f"vs A26 fast naive +5e buildup: {lo/T_BUILD_A26[0]:.3e} ... {hi/T_BUILD_A26[0]:.3e}")
    print(f"vs A26 slow naive +5e buildup: {lo/T_BUILD_A26[1]:.3e} ... {hi/T_BUILD_A26[1]:.3e}")
    print(f"vs hydro rB/c_eff @1e11: {lo/T_HYDRO_1E11:.3e} ... {hi/T_HYDRO_1E11:.3e}")
    print("\nInterpretation")
    print("- electrons rearrange first on ~1e-17 s scales")
    print("- Fe/Ni ionic structure can diffuse across one screening length on ~0.26...0.75 ps")
    print("- this is still faster than the ~5.9 ps outer hydro crossing at 1e11 kg")
    print("- fixed ions are acceptable only for the earliest electronic response, not for a full multi-e charge buildup/current-balance closure")
    print("- self-diffusion is not identical to charged mobility; full ambipolar transport remains OPEN")


if __name__ == "__main__":
    main()
