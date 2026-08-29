#!/usr/bin/env python3
"""Stage 3.73 / F1: protosolar co-moving seed formation audit.

Tests three distinct formation ideas for M_BH=1e10...5e11 kg:
1) capture/damping by MMSN gas drag at 1 AU;
2) repeated supersonic disk crossings over the gas-disk lifetime;
3) low-velocity access to a contracting ~1 Msun protostellar cloud.

This is a formation/delivery audit only. It does not assume that a seed already
bound to the protosolar system is automatically incorporated into Earth.
"""

from __future__ import annotations

from math import erf, exp, pi, sqrt

G = 6.67430e-11
K_B = 1.380649e-23
M_H = 1.6735575e-27
M_SUN = 1.98847e30
AU = 1.495978707e11
PC = 3.085677581e16
YEAR = 365.25 * 86400.0

MASSES = (1e10, 1e11, 2e11, 5e11)

# Hayashi MMSN at 1 AU.
SIGMA_G = 1700.0 * 10.0  # g/cm2 -> kg/m2
T = 280.0
MU = 2.34
CS = sqrt(K_B*T/(MU*M_H))
OMEGA = 2*pi/YEAR
H = CS/OMEGA
RHO_MID = SIGMA_G/(sqrt(2*pi)*H)

# Conservative upper end of paleomagnetic gas-disk dispersal interval.
DISK_LIFETIME = 4.9e6 * YEAR
N_CROSS = 2.0 * DISK_LIFETIME/YEAR

# Deliberately generous supersonic Ostriker/Coulomb-log factor.
I_SUP = 10.0

# Halo velocity scale used in the PBH/protostellar-cloud literature.
SIGMA_HALO = 200e3


def tau_df_subsonic(M: float) -> float:
    """Ostriker M<<1 damping e-fold time: dv/dt=-v/tau."""
    return 3.0*CS**3/(4*pi*G**2*M*RHO_MID)


def fractional_energy_loss_per_disk_crossing(M: float, v: float) -> float:
    """Generous supersonic thin-disk estimate DeltaE/E.

    F_df ~= 4 pi G^2 M^2 rho I / v^2.
    Integrating rho dl -> Sigma gives DeltaE/E = 8 pi G^2 M Sigma I / v^4.
    """
    return 8*pi*G**2*M*SIGMA_G*I_SUP/v**4


def escape_speed(M: float, R: float) -> float:
    return sqrt(2*G*M/R)


def maxwell_speed_cdf(v: float, sigma: float) -> float:
    """3D Maxwell speed CDF for 1D component dispersion sigma."""
    x = v/(sqrt(2)*sigma)
    return erf(x) - sqrt(2/pi)*(v/sigma)*exp(-v*v/(2*sigma*sigma))


def main() -> None:
    print("Stage 3.73 / F1 protosolar co-moving seed audit")
    print("\nMMSN @1 AU")
    print(f"Sigma_g={SIGMA_G:.6e} kg/m2")
    print(f"T={T:.1f} K  c_s={CS:.6e} m/s")
    print(f"H={H:.6e} m  rho_mid={RHO_MID:.6e} kg/m3")
    print(f"disk lifetime={DISK_LIFETIME/YEAR:.3e} yr")
    print(f"max two-crossings/orbit count={N_CROSS:.3e}")

    print("\nSubsonic gaseous-dynamical-friction damping")
    print("M_kg,tau_df_yr,tau/disk_lifetime")
    for M in MASSES:
        tau = tau_df_subsonic(M)
        print(f"{M:.6e},{tau/YEAR:.9e},{tau/DISK_LIFETIME:.9e}")

    print("\nSupersonic repeated disk-crossing stress test (I=10)")
    print("M_kg,v_mps,DeltaE_over_E_per_crossing,max_cumulative_Ncross")
    for M in MASSES:
        for v in (3e3, 1e4, 3e4):
            f = fractional_energy_loss_per_disk_crossing(M, v)
            print(f"{M:.6e},{v:.6e},{f:.9e},{f*N_CROSS:.9e}")

    print("\nContracting protosolar-cloud low-velocity phase-space gate")
    print("R_pc,vesc_km_s,Maxwell_CDF_v_below_vesc_sigma200kms")
    for Rpc in (0.1, 0.05, 0.01):
        vesc = escape_speed(M_SUN, Rpc*PC)
        print(f"{Rpc:.6e},{vesc/1e3:.9e},{maxwell_speed_cdf(vesc,SIGMA_HALO):.9e}")

    print("\nInterpretation")
    print("- MMSN gas drag cannot capture/damp project-mass seeds on disk timescales.")
    print("- repeated supersonic disk crossings are also negligible even with I=10.")
    print("- a normal ~200 km/s halo PBH has an extremely small low-speed phase-space fraction relative to a protostellar cloud.")
    print("- literature likewise finds PBH capture from the Galactic halo into a contracting protostellar cloud extremely small.")
    print("- a seed already in a distinct cold/co-moving low-velocity population remains a separate initial condition, not excluded by these drag calculations.")
    print("- incorporation of such a pre-bound seed into a terrestrial embryo/Earth remains a separate N-body/time-dependent-potential problem.")


if __name__ == "__main__":
    main()
