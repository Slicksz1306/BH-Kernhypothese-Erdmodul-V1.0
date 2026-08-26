#!/usr/bin/env python3
"""Stage 3.69A-1 Schwarzschild-Dirac prototype.

Purpose
-------
This prototype implements the radial massive Dirac system used by
Doran, Lasenby, Dolan & Hinder (2005) in Painleve-Gullstrand
coordinates, starts on the regular horizon branch, integrates outward,
and checks conservation of the radial probability-current Wronskian.

IMPORTANT:
- This is a solver/self-consistency milestone, not yet a validated
  absorption-cross-section calculator.
- Asymptotic in/out amplitude extraction and partial-wave summation are
  deliberately NOT reported as physical results until benchmarked against
  the published curves/low-energy limits.
- Natural units G = hbar = c = 1 are used inside the radial solver.
  The geometric black-hole mass is scaled to M=1, so x=r/M and the
  particle rest mass becomes alpha = G M_BH m/(hbar c).
"""

from __future__ import annotations

from math import pi, sqrt, exp
import numpy as np
from scipy.integrate import solve_ivp

# SI constants for regime conversion
G = 6.67430e-11
C = 299_792_458.0
HBAR = 1.054571817e-34
M_E = 9.1093837139e-31
M_P = 1.67262192595e-27
U = 1.66053906660e-27
M_FE56 = 55.93493633 * U


def alpha_g(M_bh_kg: float, m_kg: float) -> float:
    return G * M_bh_kg * m_kg / (HBAR * C)


def radial_A(x: float, kappa: int, energy: float, mass: float) -> np.ndarray:
    """Right-hand matrix A in (1-2/x) dU/dx = A U.

    This is Eq. (16) of Doran et al. in the M=1 scaling. The first matrix
    contains sqrt(2/x), as required by the Painleve-Gullstrand form and by
    exact current conservation.
    """
    s = sqrt(2.0 / x)
    B = np.array([[1.0, s], [s, 1.0]], dtype=complex)
    Cmat = np.array(
        [
            [kappa / x, 1j * (energy + mass) - s / (4.0 * x)],
            [1j * (energy - mass) - s / (4.0 * x), -kappa / x],
        ],
        dtype=complex,
    )
    return B @ Cmat


def horizon_u0(kappa: int, energy: float, mass: float) -> np.ndarray:
    """Regular s=0 horizon eigenvector (Doran et al., Eq. 19), M=1."""
    return np.array(
        [
            kappa - 2j * (energy + mass) + 0.25,
            kappa + 2j * (energy - mass) - 0.25,
        ],
        dtype=complex,
    )


def horizon_u1(kappa: int, energy: float, mass: float) -> np.ndarray:
    """First regular Taylor coefficient about x=2.

    With U=U0 + delta U1 + ... and 1-2/x = delta/2 + ...,
    (1/2 I - A0) U1 = A1 U0.
    """
    x0 = 2.0
    A0 = radial_A(x0, kappa, energy, mass)
    h = 1.0e-6
    A1 = (radial_A(x0 + h, kappa, energy, mass) - radial_A(x0 - h, kappa, energy, mass)) / (2.0 * h)
    return np.linalg.solve(0.5 * np.eye(2, dtype=complex) - A0, A1 @ horizon_u0(kappa, energy, mass))


def wronskian(U: np.ndarray, x: float) -> float:
    """Conserved radial current W_kappa (Doran et al., Eq. 23), M=1."""
    s = sqrt(2.0 / x)
    value = (
        U[0] * np.conj(U[1])
        + np.conj(U[0]) * U[1]
        - s * (abs(U[0]) ** 2 + abs(U[1]) ** 2)
    )
    return float(value.real)


def integrate_mode(alpha: float, speed_u: float, kappa: int, x_max: float = 1000.0):
    """Integrate one regular partial wave and return current-conservation diagnostics."""
    if not (0.0 < speed_u < 1.0):
        raise ValueError("speed_u must satisfy 0<u<1")
    if kappa == 0:
        raise ValueError("kappa cannot be zero")

    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    mass = alpha
    energy = alpha * gamma

    eps = 1.0e-6
    U0 = horizon_u0(kappa, energy, mass)
    U1 = horizon_u1(kappa, energy, mass)
    y0 = U0 + eps * U1
    x_start = 2.0 + eps

    def rhs(x, y):
        return radial_A(x, kappa, energy, mass) @ y / (1.0 - 2.0 / x)

    sol = solve_ivp(
        rhs,
        (x_start, x_max),
        y0,
        method="DOP853",
        rtol=1.0e-10,
        atol=1.0e-12,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    w_start = wronskian(y0, x_start)
    w_end = wronskian(sol.y[:, -1], x_max)
    rel_drift = abs((w_end - w_start) / w_start)
    return {
        "alpha": alpha,
        "u": speed_u,
        "kappa": kappa,
        "x_max": x_max,
        "W_start": w_start,
        "W_end": w_end,
        "relative_W_drift": rel_drift,
        "nfev": sol.nfev,
    }


def unruh_low_energy_dimensionless(alpha: float, speed_u: float) -> float:
    """Doran et al. Eq. (31): sigma_abs/(GM/c^2)^2.

    Use only as a published low-energy benchmark, not as a universal formula
    across alpha. In particular it must not be blindly extrapolated to the
    strong-coupling Fe-56 regime.
    """
    u = speed_u
    root = sqrt(1.0 - u * u)
    X = 2.0 * pi * alpha * (1.0 + u * u) / (u * root)
    denom = 1.0 if X > 700.0 else 1.0 - exp(-X)
    return 4.0 * pi**2 * (1.0 + u * u) * alpha / (u * u * root * denom)


def main():
    print("Stage 3.69A-1 Dirac integration self-check")
    print("Benchmark: alpha=0.2, u=0.5, x=r/M: 2 -> 1000")
    for kappa in (-1, 1):
        out = integrate_mode(alpha=0.2, speed_u=0.5, kappa=kappa)
        print(out)

    M_bh = 1.0e11
    u_earth = 10.4355e3 / C
    print("\nEarth-branch coupling diagnostic at M_BH=1e11 kg")
    for name, mass in (("electron", M_E), ("proton", M_P), ("Fe-56", M_FE56)):
        a = alpha_g(M_bh, mass)
        print(f"{name:8s} alpha_g={a:.9e}")

    # Electron is safely in the low-alpha regime. The proton value is printed
    # only as an analytic comparison and is not accepted as a final result.
    a_e = alpha_g(M_bh, M_E)
    a_p = alpha_g(M_bh, M_P)
    print("\nPublished low-energy analytic benchmark at Earth supply speed")
    print(f"electron sigma/(GM/c^2)^2 ~= {unruh_low_energy_dimensionless(a_e, u_earth):.9e}")
    print(f"proton   sigma/(GM/c^2)^2 ~= {unruh_low_energy_dimensionless(a_p, u_earth):.9e}  [extrapolation; not final]")
    print("\nNo physical sigma_abs is accepted from the ODE solver until asymptotic")
    print("in/out matching reproduces the published Doran/Unruh benchmark curves.")


if __name__ == "__main__":
    main()
