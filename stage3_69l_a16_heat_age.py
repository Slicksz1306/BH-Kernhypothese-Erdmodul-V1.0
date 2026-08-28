#!/usr/bin/env python3
"""Stage 3.69L / A16: heat and 4.54-Gyr growth sensitivity audit.

Uses the A13b Grant-fit anchored supply envelope. For processing-capable
>=1e11 kg branches, Mdot is treated as an upper reduced-throughput proxy.
For 1e10 kg the overloaded/backpressure caveat remains explicit.

The Mdot=k M^2 integration is a stationary-environment sensitivity law, not a
complete terrestrial history.
"""

C = 299_792_458.0
SEC_YR = 365.25*24*3600
AGE_YR = 4.54e9
AGE_S = AGE_YR*SEC_YR
EARTH_HEAT_W = 47.0e12
EARTH_MASS = 5.9722e24

MASSES = (1.0e10, 1.0e11, 2.0e11, 5.0e11)
MDOT_LO_1E11 = 8.27068e-8
MDOT_HI_1E11 = 6.12599e-6


def band(M):
    scale=(M/1e11)**2
    return MDOT_LO_1E11*scale, MDOT_HI_1E11*scale


def backward_initial_mass(M_now, mdot_now):
    # dM/dt=k M^2, with k=mdot_now/M_now^2.
    t_growth=M_now/mdot_now
    return M_now/(1.0+AGE_S/t_growth)


def main():
    print("Stage 3.69L / A16 heat-age audit")
    print("Earth heat reference = 47 TW; Earth age = 4.54 Gyr")
    print("M,edge,mdot,P_eta1_TW,tgrowth_Gyr,M_initial_4p54Ga,DeltaM,DeltaM_over_Earth,Pavg_eta1_TW,eta_for_47TW")
    for M in MASSES:
        for edge,mdot in (("lo",band(M)[0]),("hi",band(M)[1])):
            power=mdot*C*C
            tg=M/mdot
            Mi=backward_initial_mass(M,mdot)
            dM=M-Mi
            pavg=dM*C*C/AGE_S
            print(
                f"{M:.6e},{edge},{mdot:.12e},{power/1e12:.9e},{tg/SEC_YR/1e9:.9e},"
                f"{Mi:.12e},{dM:.12e},{dM/EARTH_MASS:.9e},{pavg/1e12:.9e},{EARTH_HEAT_W/power:.9e}"
            )
    print("\nInterpretation")
    print("- all tested present eta=1 rest-mass powers are below the 47-TW total surface heat-flow reference")
    print("- this is only a hard-budget pre-test; it does not mean all that power could be hidden inside the known terrestrial heat budget")
    print("- backward kM^2 solutions remain positive over 4.54 Gyr, so this sensitivity law has no algebraic age contradiction")
    print("- high-rate present branches have short M/Mdot timescales and therefore strong nonlinear evolutionary sensitivity")
    print("- 1e10 kg is not a demonstrated steady branch because A15/A11/A12 backpressure remains open")

if __name__ == '__main__':
    main()
