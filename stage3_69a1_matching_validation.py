#!/usr/bin/env python3
"""Stage 3.69A-1: asymptotic matching validation for Schwarzschild-Dirac capture.

This script extends the radial current-conserving prototype with an
asymptotic in/out coefficient extractor.  It is deliberately validated first
in the weak-coupling, low-energy regime where Doran et al. (2005) report
agreement with the analytic Unruh approximation.

The code does NOT yet compute the Earth-branch net accretion rate.  In
particular, dense-matter transport, species coupling and charge feedback are
outside this benchmark.

Natural units G = hbar = c = M_BH = 1 are used in the radial solver.
Then particle mass m equals alpha_g = G M_BH m_particle/(hbar c).
"""

from __future__ import annotations

from math import exp, pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp


def radial_A(x: float, kappa: int, energy: float, mass: float) -> np.ndarray:
    """Doran et al. radial matrix in Painleve-Gullstrand coordinates."""
    s = sqrt(2.0 / x)
    B = np.array([[1.0, s], [s, 1.0]], dtype=complex)
    C = np.array(
        [
            [kappa / x, 1j * (energy + mass) - s / (4.0 * x)],
            [1j * (energy - mass) - s / (4.0 * x), -kappa / x],
        ],
        dtype=complex,
    )
    return B @ C


def horizon_u0(kappa: int, energy: float, mass: float) -> np.ndarray:
    """Regular s=0 horizon branch."""
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
    h = 1.0e-6
    A1 = (
        radial_A(x0 + h, kappa, energy, mass)
        - radial_A(x0 - h, kappa, energy, mass)
    ) / (2.0 * h)
    return np.linalg.solve(
        0.5 * np.eye(2, dtype=complex) - A0,
        A1 @ horizon_u0(kappa, energy, mass),
    )


def wronskian(U: np.ndarray, x: float) -> float:
    """Conserved radial current, Doran et al. Eq. (23)."""
    s = sqrt(2.0 / x)
    value = (
        U[0] * np.conj(U[1])
        + np.conj(U[0]) * U[1]
        - s * (abs(U[0]) ** 2 + abs(U[1]) ** 2)
    )
    return float(value.real)


def integrate_mode(
    alpha: float,
    speed_u: float,
    kappa: int,
    x_max: float,
    sample_x: np.ndarray,
):
    """Integrate one regular partial wave and sample it at large radius."""
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    mass = alpha
    energy = alpha * gamma

    eps = 1.0e-6
    x0 = 2.0 + eps
    U = horizon_u0(kappa, energy, mass) + eps * horizon_u1(
        kappa, energy, mass
    )

    # Doran's cross-section formula assumes the regular horizon solution is
    # normalized to W_kappa = -1.
    W0 = wronskian(U, x0)
    if W0 >= 0.0:
        raise RuntimeError(f"Unexpected horizon-current sign: W={W0}")
    U = U / sqrt(-W0)

    def rhs(x, y):
        return radial_A(x, kappa, energy, mass) @ y / (1.0 - 2.0 / x)

    sol = solve_ivp(
        rhs,
        (x0, x_max),
        U,
        t_eval=sample_x,
        method="DOP853",
        rtol=2.0e-10,
        atol=2.0e-12,
    )
    if not sol.success:
        raise RuntimeError(sol.message)

    return sol, energy, mass


def local_incoming_amplitude(
    U: np.ndarray,
    x: float,
    kappa: int,
    energy: float,
    mass: float,
) -> float:
    """Extract |alpha_kappa| from the local asymptotic eigenbasis.

    At large x the two eigenvalues of the exact first-order radial evolution
    matrix approach -i p and +i p.  The negative-imaginary branch is labelled
    incoming and the positive-imaginary branch outgoing.  The eigenvectors
    are normalized to first component 1 before solving for local coefficients.

    Finite-radius 1/sqrt(x) corrections are removed in
    extrapolated_alpha_infinity().
    """
    D = radial_A(x, kappa, energy, mass) / (1.0 - 2.0 / x)
    eigenvalues, eigenvectors = np.linalg.eig(D)

    i_in = int(np.argmin(eigenvalues.imag))
    i_out = int(np.argmax(eigenvalues.imag))

    v_in = eigenvectors[:, i_in] / eigenvectors[0, i_in]
    v_out = eigenvectors[:, i_out] / eigenvectors[0, i_out]
    coeff = np.linalg.solve(np.column_stack([v_in, v_out]), U)
    return float(abs(coeff[0]))


def extrapolated_alpha_infinity(
    alpha: float,
    speed_u: float,
    kappa: int,
    x_max: float = 80_000.0,
    n_sample: int = 50,
) -> tuple[float, float]:
    """Return extrapolated |alpha_kappa| and final Wronskian.

    The fit variable t=1/sqrt(x) follows the leading asymptotic structure of
    the Painleve-Gullstrand radial equation.  A quadratic fit is used only in
    the outermost quarter-to-full x_max interval.
    """
    xs = np.geomspace(0.25 * x_max, x_max, n_sample)
    sol, energy, mass = integrate_mode(alpha, speed_u, kappa, x_max, xs)

    amps = np.array(
        [
            local_incoming_amplitude(U, x, kappa, energy, mass)
            for U, x in zip(sol.y.T, xs)
        ]
    )
    t = 1.0 / np.sqrt(xs)
    fit = np.polyfit(t, amps, 2)
    alpha_inf = float(np.polyval(fit, 0.0))
    W_end = wronskian(sol.y[:, -1], x_max)
    return alpha_inf, W_end


def sigma_abs_low_partialwaves(
    alpha: float,
    speed_u: float,
    x_max: float = 80_000.0,
) -> tuple[float, list[tuple[int, float, float]]]:
    """Doran Eq. (30), restricted to kappa=+/-1 for low-alpha validation."""
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    mass = alpha
    energy = alpha * gamma
    momentum = sqrt(energy**2 - mass**2)

    partial_sum = 0.0
    details = []
    for kappa in (-1, +1):
        a_inf, W_end = extrapolated_alpha_infinity(
            alpha, speed_u, kappa, x_max=x_max
        )
        term = abs(kappa) / a_inf**2
        partial_sum += term
        details.append((kappa, a_inf, W_end))

    sigma = pi * partial_sum / (2.0 * momentum * (energy - mass))
    return sigma, details


def unruh_low_energy(alpha: float, speed_u: float) -> float:
    """Doran Eq. (31): low-energy Unruh approximation, sigma/M^2."""
    u = speed_u
    root = sqrt(1.0 - u**2)
    X = 2.0 * pi * alpha * (1.0 + u**2) / (u * root)
    denominator = 1.0 if X > 700.0 else 1.0 - exp(-X)
    return (
        4.0
        * pi**2
        * (1.0 + u**2)
        * alpha
        / (u**2 * root * denominator)
    )


def run_benchmark(alpha: float, e_over_m: float = 2.0):
    speed_u = sqrt(1.0 - 1.0 / e_over_m**2)
    numerical, details = sigma_abs_low_partialwaves(alpha, speed_u)
    analytic = unruh_low_energy(alpha, speed_u)
    rel = (numerical / analytic - 1.0) * 100.0

    print(f"alpha={alpha:.7g}, E/m={e_over_m:g}, u={speed_u:.9f}")
    print(f"  numerical sigma/M^2 = {numerical:.9f}")
    print(f"  Unruh    sigma/M^2 = {analytic:.9f}")
    print(f"  relative difference = {rel:+.6f}%")
    for kappa, a_inf, W_end in details:
        print(
            f"  kappa={kappa:+d}: |alpha_kappa|_inf={a_inf:.9e}, "
            f"W(x_max)={W_end:.12f}"
        )
    print()


if __name__ == "__main__":
    print("Stage 3.69A-1 asymptotic matching validation")
    print("Low-alpha benchmark; only |kappa|=1 retained as in the low-energy limit.\n")
    run_benchmark(0.005)
    run_benchmark(0.0025)
    print(
        "Interpretation: convergence toward the published Unruh/Doran low-energy "
        "limit validates the asymptotic coefficient extraction in this regime. "
        "It does not yet validate the dense Earth-branch transport closure."
    )
