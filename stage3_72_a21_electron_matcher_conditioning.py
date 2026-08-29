#!/usr/bin/env python3
"""Stage 3.72 / A21: screened-electron Dirac matcher conditioning audit.

This is NOT the final screened-electron S-matrix. It quantifies why the
existing A4 finite-radius charged-proton matcher cannot simply be reused for
Earth-speed electrons in double precision.

The audit computes:
- electron gravitational coupling alpha_e,
- dimensionless asymptotic momentum pM,
- reduced de Broglie wavelength,
- Thomas-Fermi screening range in physical and r_g units,
- the radius scale at which the Schwarzschild sqrt(2/x) asymptotic drift is
  smaller than the tiny Earth-speed momentum,
- the neutral Unruh low-energy absorption scale that the numerical matcher
  would have to resolve.

Acceptance requirement for a future full electron solver:
- use a Jost/Riccati/log-derivative or equivalent flux-direct formulation,
  not subtraction of 1-|S|^2 at ~1e-11 level;
- include finite-range screened Coulomb potential;
- reproduce the neutral low-energy benchmark before turning on charge;
- demonstrate matching-radius and precision convergence.
"""

from __future__ import annotations

from math import exp, pi, sqrt

G = 6.67430e-11
C = 299_792_458.0
HBAR = 1.054571817e-34
M_E = 9.1093837015e-31

M_REF = 1.0e11
V_EARTH = 10.4355e3
LAMBDA_TF_RANGE = (2.95e-11, 4.29e-11)  # A14 dense-core bracket [m]


def alpha_g(M: float, m: float) -> float:
    return G * M * m / (HBAR * C)


def unruh_low_energy_sigma_dimless(alpha: float, u: float) -> float:
    root = sqrt(1.0 - u * u)
    X = 2.0 * pi * alpha * (1.0 + u * u) / (u * root)
    denom = 1.0 if X > 700.0 else 1.0 - exp(-X)
    return 4.0 * pi**2 * (1.0 + u * u) * alpha / (u * u * root * denom)


def main() -> None:
    u = V_EARTH / C
    gamma = 1.0 / sqrt(1.0 - u * u)
    alpha = alpha_g(M_REF, M_E)
    p = alpha * u * gamma
    r_g = G * M_REF / C**2
    lambda_db_reduced = HBAR / (M_E * V_EARTH)

    # In the A1 asymptotic phase, the Schwarzschild drift contains E*sqrt(2/x).
    # Requiring that term to be smaller than p gives roughly x > 2/u^2.
    x_grav_min = 2.0 / u**2

    sigma_dim = unruh_low_energy_sigma_dimless(alpha, u)
    pabs_sum_k1 = sigma_dim * p**2 / pi
    pabs_per_leading_kappa = 0.5 * pabs_sum_k1

    print("Stage 3.72 / A21 screened-electron matcher conditioning")
    print(f"M={M_REF:.6e} kg")
    print(f"v={V_EARTH:.6e} m/s, u={u:.12e}")
    print(f"alpha_e={alpha:.12e}")
    print(f"p_dimensionless={p:.12e}")
    print(f"r_g={r_g:.12e} m")
    print(f"lambda_db_reduced={lambda_db_reduced:.12e} m")
    print(f"x_gravity_asymptotic_scale~2/u^2={x_grav_min:.12e}")

    print("\nThomas-Fermi screening bracket")
    for lam in LAMBDA_TF_RANGE:
        print(
            f"lambda_TF={lam:.6e} m, "
            f"x_TF=lambda/r_g={lam/r_g:.12e}, "
            f"lambda_TF/lambda_db={lam/lambda_db_reduced:.12e}"
        )

    print("\nNeutral low-energy calibration target")
    print(f"Unruh sigma/M^2={sigma_dim:.12e}")
    print(f"leading |kappa|=1 Pabs sum~{pabs_sum_k1:.12e}")
    print(f"per leading kappa Pabs~{pabs_per_leading_kappa:.12e}")

    print("\nNumerical implication")
    print("- direct 1-|S|^2 subtraction must resolve O(1e-11) absorption")
    print("- the A4 proton matcher was designed for O(1) proton absorption changes")
    print("- Earth-speed electron in/out modes become nearly degenerate at finite radius")
    print("- screened Coulomb range is finite, but Schwarzschild asymptotics still require x >> 1e9")
    print("- therefore naive reuse of the A4 double-precision matcher is NOT CONTROLLED")

    print("\nRequired next solver architecture")
    print("1. flux-direct Jost/Riccati/log-derivative formulation")
    print("2. finite-range screened Coulomb potential")
    print("3. neutral Unruh benchmark regression at Earth-speed")
    print("4. precision and matching-radius convergence")
    print("5. only then scan Q~O(1...5 e)")


if __name__ == "__main__":
    main()
