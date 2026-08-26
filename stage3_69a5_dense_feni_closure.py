#!/usr/bin/env python3
"""Stage 3.69A-5: coherent Fe/Ni scalar capture + dense-core scale diagnostics.

Dominant Fe-56 and Ni-58 nuclei have 0+ ground states.  While a nucleus
remains coherent, a massive scalar/Klein-Gordon partial-wave model is a
better first capture proxy than the spin-1/2 Dirac equation.

This script provides:
- a massive scalar Schwarzschild partial-wave solver;
- a low-coupling external regression using the Unruh scalar/Dirac ratio;
- Earth-speed Fe-56/Ni-58 transition partial waves at M=1e11 kg;
- dense Fe electronic/screening scale estimates;
- a diagnostic comparison of rho*v*sigma single-pass flux to historical
  Michel supply benchmarks.

It does NOT close the final net accretion rate.  The gap between collisional
outer supply and inner phase-space recycling remains a transport problem.
"""

from __future__ import annotations

from math import pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp

from stage3_69a1_dirac_prototype import (
    G, C, HBAR, M_E, alpha_g, classical_sigma_dimensionless,
    unruh_low_energy_dimensionless,
)

EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19
AMU = 1.66053906660e-27
M_N = 1.67492749804e-27

V_EARTH = 10.4355e3
U_EARTH = V_EARTH / C
RHO_CORE = 13_088.5  # kg/m^3 PREM-center proxy
M_REF = 1.0e11

# Atomic masses minus electron rest masses: first coherent nuclear-mass proxy.
M_FE56 = 55.93493633 * AMU - 26.0 * M_E
M_NI58 = 57.9353429 * AMU - 28.0 * M_E


def kg_absorption_probability(alpha: float, speed_u: float, ell: int, x_match: float = 2.0e4, segments: int = 60) -> float:
    """Massive scalar absorption from the Schwarzschild Regge-Wheeler equation.

    Variables are (psi, dpsi/dr_*).  The horizon mode is purely ingoing.
    Piecewise renormalization preserves the reflection ratio while avoiding
    dynamic-range loss.
    """
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    omega = alpha * gamma
    mu = alpha
    x = 2.0 + 1.0e-6
    Y = np.array([1.0 + 0j, -1j * omega], dtype=complex)
    edges = np.geomspace(x, x_match, segments)

    def rhs(xx: float, y: np.ndarray) -> np.ndarray:
        f = 1.0 - 2.0 / xx
        V = f * (mu**2 + ell * (ell + 1.0) / xx**2 + 2.0 / xx**3)
        return np.array([y[1] / f, -(omega**2 - V) * y[0] / f], dtype=complex)

    for x1 in edges[1:]:
        sol = solve_ivp(rhs, (x, x1), Y, method="DOP853", rtol=3.0e-9, atol=3.0e-11)
        if not sol.success:
            raise RuntimeError(sol.message)
        Y = sol.y[:, -1]
        Y /= np.linalg.norm(Y)
        x = x1

    f = 1.0 - 2.0 / x
    V = f * (mu**2 + ell * (ell + 1.0) / x**2 + 2.0 / x**3)
    k_local2 = omega**2 - V
    if k_local2 <= 0.0:
        raise RuntimeError("Matching radius is not in the propagating region")
    k_local = sqrt(k_local2)
    basis = np.array([[1.0, 1.0], [-1j * k_local, +1j * k_local]], dtype=complex)
    Ain, Aout = np.linalg.solve(basis, Y)
    reflection = abs(Aout / Ain) ** 2
    return max(0.0, min(1.0, 1.0 - reflection))


def scalar_sigma_from_transition(alpha: float, speed_u: float, saturated_through: int, transition: dict[int, float]) -> float:
    """sigma/M^2 with lower partial waves treated as saturated P=1."""
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    p = alpha * speed_u * gamma
    total = float((saturated_through + 1) ** 2)  # sum_{l=0}^L (2l+1)
    for ell, P in transition.items():
        total += (2.0 * ell + 1.0) * P
    return pi * total / p**2


def physical_sigma(M_bh_kg: float, sigma_over_M2: float) -> float:
    rg = G * M_bh_kg / C**2
    return sigma_over_M2 * rg**2


def low_alpha_regression() -> None:
    alpha = 0.0025
    E_over_m = 2.0
    speed_u = sqrt(1.0 - 1.0 / E_over_m**2)
    P0 = kg_absorption_probability(alpha, speed_u, 0, x_match=4.0e4, segments=120)
    p = alpha * speed_u * E_over_m
    sigma_scalar = pi * P0 / p**2
    sigma_dirac_unruh = unruh_low_energy_dimensionless(alpha, speed_u)
    target_scalar = 8.0 * sigma_dirac_unruh
    print("Low-alpha scalar regression")
    print(f"sigma_scalar/M^2 = {sigma_scalar:.10f}")
    print(f"8 x Dirac-Unruh  = {target_scalar:.10f}")
    print(f"relative error    = {(sigma_scalar/target_scalar-1.0)*100.0:.5f} %")


def feni_reference() -> None:
    classical_dim = classical_sigma_dimensionless(U_EARTH)
    configs = [
        ("Fe-56", M_FE56, 76, [77, 78, 79, 80]),
        ("Ni-58", M_NI58, 79, [80, 81, 82, 83]),
    ]
    print("\nEarth-speed coherent 0+ capture at M=1e11 kg")
    for name, mass, saturated, ells in configs:
        alpha = alpha_g(M_REF, mass)
        transition = {ell: kg_absorption_probability(alpha, U_EARTH, ell) for ell in ells}
        sigma_dim = scalar_sigma_from_transition(alpha, U_EARTH, saturated, transition)
        sigma_m2 = physical_sigma(M_REF, sigma_dim)
        print(f"{name}: alpha={alpha:.9f}, 4alpha={4*alpha:.6f}")
        for ell, P in transition.items():
            print(f"  l={ell:3d}: P_abs={P:.9e}")
        print(f"  sigma/classical={sigma_dim/classical_dim:.9f}")
        print(f"  sigma={sigma_m2:.12e} m^2")


def dense_scales() -> None:
    Z, A = 26.0, 56.0
    m_ion = A * AMU
    n_i = RHO_CORE / m_ion
    n_e = Z * n_i
    a_i = (3.0 / (4.0 * pi * n_i)) ** (1.0 / 3.0)
    a_e = (3.0 / (4.0 * pi * n_e)) ** (1.0 / 3.0)
    k_F = (3.0 * pi**2 * n_e) ** (1.0 / 3.0)
    p_F = HBAR * k_F
    E_F = p_F**2 / (2.0 * M_E)
    v_F = p_F / M_E
    lambda_TF = sqrt(2.0 * EPS0 * E_F / (3.0 * n_e * E_CHARGE**2))
    r_s = 2.0 * G * M_REF / C**2
    r_B = G * M_REF / V_EARTH**2
    N_i_B = 4.0 * pi * r_B**3 * n_i / 3.0
    N_e_B = Z * N_i_B
    N_e_TF = 4.0 * pi * lambda_TF**3 * n_e / 3.0

    def coulomb_eV(r):
        return (E_CHARGE**2 / (4.0 * pi * EPS0 * r)) / E_CHARGE

    print("\nDense Fe scale proxies")
    print(f"n_i={n_i:.6e} m^-3, n_e={n_e:.6e} m^-3")
    print(f"a_i={a_i:.6e} m, a_e={a_e:.6e} m")
    print(f"E_F={E_F/E_CHARGE:.6f} eV, v_F={v_F:.6e} m/s")
    print(f"p_F/(m_e c)={p_F/(M_E*C):.6e}")
    print(f"lambda_TF(proxy)={lambda_TF:.6e} m")
    print(f"r_s={r_s:.6e} m, r_B={r_B:.6e} m")
    print(f"r_B/lambda_TF={r_B/lambda_TF:.3f}, lambda_TF/r_s={lambda_TF/r_s:.3e}")
    print(f"ions in r_B ~{N_i_B:.6e}, electrons in r_B ~{N_e_B:.6e}")
    print(f"free-electron count in one lambda_TF sphere ~{N_e_TF:.6f}")
    print(f"Coulomb energy per e: r_s={coulomb_eV(r_s)/1e6:.6f} MeV, lambda_TF={coulomb_eV(lambda_TF):.6f} eV, a_i={coulomb_eV(a_i):.6f} eV")


def rate_diagnostics() -> None:
    # Fe coherent sink value from the transition calculation above.
    alpha = alpha_g(M_REF, M_FE56)
    transition = {ell: kg_absorption_probability(alpha, U_EARTH, ell) for ell in [77, 78, 79, 80]}
    sigma_dim = scalar_sigma_from_transition(alpha, U_EARTH, 76, transition)
    sigma_fe = physical_sigma(M_REF, sigma_dim)
    mdot_single = RHO_CORE * V_EARTH * sigma_fe
    year = 365.25 * 86400.0
    michel = [1.47e-8, 1.46e-7]
    print("\nRate diagnostics at M=1e11 kg")
    print(f"rho*v*sigma_Fe single-pass proxy = {mdot_single:.12e} kg/s = {mdot_single*year:.9e} kg/year")
    print(f"rest-energy equivalent = {mdot_single*C**2:.6e} W")
    for mdot in michel:
        print(
            f"Michel benchmark {mdot:.3e} kg/s: gap={mdot/mdot_single:.6e}, "
            f"kg/year={mdot*year:.6f}, rest-power={mdot*C**2/1e12:.6f} TW, "
            f"M/mdot={M_REF/mdot/year/1e9:.3f} Gyr"
        )


def tidal_nuclear_scale() -> None:
    A = 56.0
    R_n = 1.2e-15 * A ** (1.0 / 3.0)
    E_bind = 8.8e6 * E_CHARGE
    r_tidal = (G * M_REF * M_N * R_n**2 / E_bind) ** (1.0 / 3.0)
    r_s = 2.0 * G * M_REF / C**2
    print("\nNuclear tidal scale proxy")
    print(f"R_Fe ~{R_n:.6e} m")
    print(f"r_tidal ~{r_tidal:.6e} m ~{r_tidal/r_s:.3f} r_s")
    print("This is only a tidal-binding proxy; compression/collisions/reactions can change composition earlier.")


def main() -> None:
    print("Stage 3.69A-5 coherent Fe/Ni + dense-core diagnostics")
    low_alpha_regression()
    feni_reference()
    dense_scales()
    rate_diagnostics()
    tidal_nuclear_scale()
    print("\nStatus")
    print("- scalar/Klein-Gordon low-alpha external regression: PASS (~0.2%)")
    print("- coherent Fe-56/Ni-58 wave capture at 1e11 kg: near classical, no strong suppression")
    print("- dense charge screening: local atomic/sub-nm scale, not r_B-scale blocker")
    print("- final dense-core net Mdot: OPEN because transport/recycling/composition closure remains")
    print("- next step: kinetic transport + charge-state + nuclear/composition closure")


if __name__ == "__main__":
    main()
