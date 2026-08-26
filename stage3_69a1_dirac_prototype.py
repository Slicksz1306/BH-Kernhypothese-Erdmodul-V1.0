#!/usr/bin/env python3
"""Stage 3.69A-1 Schwarzschild-Dirac prototype.

Implements the massive Dirac radial system of Doran, Lasenby, Dolan &
Hinder (2005) in Painleve-Gullstrand coordinates, the regular horizon
branch, conserved-current diagnostics, and a flux-normalized local
in/out matching diagnostic.

Scientific scope
----------------
- This is a single-particle Schwarzschild-Dirac solver benchmark.
- It is NOT yet the dense-matter H0 net accretion rate.
- The final Earth closure still needs composition, collisions, nuclear
  coherence/dissociation, electrostatic charge feedback and transport.
- Natural units G=hbar=c=1 are used in the radial solver and M=1, so
  x=r/M, m=alpha=G M_BH m_particle/(hbar c), E=m/sqrt(1-u^2).
"""

from __future__ import annotations

from math import pi, sqrt, exp
import numpy as np
from scipy.integrate import solve_ivp

G = 6.67430e-11
C = 299_792_458.0
HBAR = 1.054571817e-34
M_E = 9.1093837139e-31
M_P = 1.67262192595e-27


def alpha_g(M_bh_kg: float, m_kg: float) -> float:
    return G * M_bh_kg * m_kg / (HBAR * C)


def radial_A(x: float, kappa: int, energy: float, mass: float) -> np.ndarray:
    """Matrix in (1-2/x)dU/dx=A U, Doran et al. Eq. (16), M=1."""
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


def rhs(x: float, y: np.ndarray, kappa: int, energy: float, mass: float) -> np.ndarray:
    return radial_A(x, kappa, energy, mass) @ y / (1.0 - 2.0 / x)


def horizon_u0(kappa: int, energy: float, mass: float) -> np.ndarray:
    """Regular s=0 horizon eigenvector, Doran et al. Eq. (19), M=1."""
    return np.array(
        [
            kappa - 2j * (energy + mass) + 0.25,
            kappa + 2j * (energy - mass) - 0.25,
        ],
        dtype=complex,
    )


def horizon_u1(kappa: int, energy: float, mass: float) -> np.ndarray:
    """First regular Taylor coefficient around x=2."""
    x0 = 2.0
    A0 = radial_A(x0, kappa, energy, mass)
    h = 1.0e-5
    A1 = (radial_A(x0 + h, kappa, energy, mass) - radial_A(x0 - h, kappa, energy, mass)) / (2.0 * h)
    return np.linalg.solve(
        0.5 * np.eye(2, dtype=complex) - A0,
        A1 @ horizon_u0(kappa, energy, mass),
    )


def current_matrix(x: float) -> np.ndarray:
    s = sqrt(2.0 / x)
    return np.array([[-s, 1.0], [1.0, -s]], dtype=complex)


def wronskian(U: np.ndarray, x: float) -> float:
    return float(np.real(np.vdot(U, current_matrix(x) @ U)))


def normalized_horizon_initial(alpha: float, speed_u: float, kappa: int, eps: float = 1.0e-6):
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    mass = alpha
    energy = alpha * gamma
    x0 = 2.0 + eps
    U = horizon_u0(kappa, energy, mass) + eps * horizon_u1(kappa, energy, mass)
    W = wronskian(U, x0)
    if W >= 0.0:
        raise RuntimeError("Regular horizon branch did not have inward current")
    U = U / sqrt(-W)  # choose W=-1 for the numerical mode
    return x0, U, energy, mass


def integrate_horizon_mode(alpha: float, speed_u: float, kappa: int, x_max: float = 1000.0):
    x0, U0, energy, mass = normalized_horizon_initial(alpha, speed_u, kappa)
    sol = solve_ivp(
        lambda x, y: rhs(x, y, kappa, energy, mass),
        (x0, x_max),
        U0,
        method="DOP853",
        rtol=1.0e-10,
        atol=1.0e-12,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol.y[:, -1], wronskian(U0, x0), wronskian(sol.y[:, -1], x_max)


def local_flux_modes(alpha: float, speed_u: float, kappa: int, x: float):
    """Local large-r in/out eigenmodes, normalized to Doran asymptotic flux.

    Doran's leading asymptotic modes have W_in=-2p/(E+m) and
    W_out=+2p/(E+m).  At finite but large x we diagonalize the exact
    local first-order radial matrix, identify modes by the sign of their
    radial phase velocity, and normalize them to those same fluxes.

    This accelerates convergence relative to a pointwise leading-order
    asymptotic basis.  Matching-radius stability is therefore an explicit
    acceptance check.
    """
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    mass = alpha
    energy = alpha * gamma
    p = alpha * speed_u * gamma
    D = radial_A(x, kappa, energy, mass) / (1.0 - 2.0 / x)
    vals, vecs = np.linalg.eig(D)

    beta = (mass**2 + 2.0 * p**2) / p
    target_in = -p + energy * sqrt(2.0 / x) - beta / x
    target_out = +p + energy * sqrt(2.0 / x) + beta / x
    i_in = int(np.argmin(np.abs(np.imag(vals) - target_in)))
    i_out = int(np.argmin(np.abs(np.imag(vals) - target_out)))

    Uin = vecs[:, i_in]
    Uout = vecs[:, i_out]
    q = p / (energy + mass)

    Win = wronskian(Uin, x)
    Wout = wronskian(Uout, x)
    if not (Win < 0.0 and Wout > 0.0):
        raise RuntimeError("Could not identify inward/outward local flux modes")

    Uin *= sqrt((-2.0 * q) / Win)
    Uout *= sqrt((+2.0 * q) / Wout)
    return Uin, Uout


def scattering_ratio(alpha: float, speed_u: float, kappa: int, x_match: float = 1000.0):
    """Return S_kappa=A_out/A_in and diagnostics at one matching radius."""
    Uh, W0, W1 = integrate_horizon_mode(alpha, speed_u, kappa, x_match)
    Uin, Uout = local_flux_modes(alpha, speed_u, kappa, x_match)
    Ain, Aout = np.linalg.solve(np.column_stack([Uin, Uout]), Uh)
    S = Aout / Ain
    return S, {
        "W_start": W0,
        "W_end": W1,
        "relative_W_drift": abs((W1 - W0) / W0),
        "Ain_abs2": abs(Ain) ** 2,
        "Aout_abs2": abs(Aout) ** 2,
        "absorption_probability": 1.0 - abs(S) ** 2,
    }


def sigma_abs_dimensionless(alpha: float, E_over_m: float, kmax: int, x_match: float = 1000.0):
    """Partial-wave absorption sigma/M^2 using Dolan-Doran-Lasenby Eq. (73)."""
    if E_over_m <= 1.0:
        raise ValueError("E/m must exceed 1 for an unbound state")
    u = sqrt(1.0 - 1.0 / E_over_m**2)
    p = alpha * u * E_over_m
    total = 0.0
    rows = []
    for k in range(1, kmax + 1):
        for kappa in (-k, +k):
            S, diag = scattering_ratio(alpha, u, kappa, x_match=x_match)
            Pabs = max(0.0, 1.0 - abs(S) ** 2)
            total += abs(kappa) * Pabs
            rows.append((kappa, Pabs, diag["relative_W_drift"]))
    return pi * total / p**2, rows


def classical_sigma_dimensionless(speed_u: float) -> float:
    """Doran et al. Eq. (3), sigma/M^2."""
    u = speed_u
    return pi / (2.0 * u**4) * (
        8.0 * u**4 + 20.0 * u**2 - 1.0 + (1.0 + 8.0 * u**2) ** 1.5
    )


def unruh_low_energy_dimensionless(alpha: float, speed_u: float) -> float:
    """Doran et al. Eq. (31), low-energy analytic benchmark sigma/M^2."""
    u = speed_u
    root = sqrt(1.0 - u * u)
    X = 2.0 * pi * alpha * (1.0 + u * u) / (u * root)
    denom = 1.0 if X > 700.0 else 1.0 - exp(-X)
    return 4.0 * pi**2 * (1.0 + u * u) * alpha / (u * u * root * denom)


def main():
    print("Stage 3.69A-1 Schwarzschild-Dirac matching prototype")

    # Current-conservation self-check
    print("\nCurrent-conservation benchmark: alpha=0.2, u=0.5")
    for kappa in (-1, 1):
        _, diag = scattering_ratio(0.2, 0.5, kappa, x_match=1000.0)
        print(kappa, diag)

    # Matching-radius convergence at two Doran-like benchmark energies.
    print("\nPartial-wave cross-section convergence, alpha=0.2")
    for Eom in (1.5, 2.0):
        for xm in (500.0, 1000.0, 2000.0):
            sigma, _ = sigma_abs_dimensionless(0.2, Eom, kmax=4, x_match=xm)
            u = sqrt(1.0 - 1.0 / Eom**2)
            print(
                f"E/m={Eom:.1f} x_match={xm:6.0f} "
                f"sigma/M^2={sigma:.9f} classical={classical_sigma_dimensionless(u):.9f}"
            )

    # Higher-energy trend. kmax=9 is converged for this point in the project test.
    sigma5, _ = sigma_abs_dimensionless(0.2, 5.0, kmax=9, x_match=600.0)
    u5 = sqrt(1.0 - 1.0 / 25.0)
    print(
        f"\nE/m=5.0: sigma/M^2={sigma5:.9f}, "
        f"classical={classical_sigma_dimensionless(u5):.9f}, "
        f"geometric_optics=27*pi={27*pi:.9f}"
    )

    # Earth-branch analytic low-energy single-particle benchmarks.
    M_bh = 1.0e11
    u_earth = 10.4355e3 / C
    rg = G * M_bh / C**2
    print("\nEarth reference point M_BH=1e11 kg, v=10.4355 km/s")
    for name, mass in (("electron", M_E), ("proton", M_P)):
        a = alpha_g(M_bh, mass)
        dim = unruh_low_energy_dimensionless(a, u_earth)
        print(
            f"{name:8s} alpha={a:.9e} "
            f"Unruh-lowE sigma={dim*rg**2:.9e} m^2"
        )

    print("\nImportant: these Earth values are isolated-particle Schwarzschild benchmarks,")
    print("not the final dense-core net capture rate.")


if __name__ == "__main__":
    main()
