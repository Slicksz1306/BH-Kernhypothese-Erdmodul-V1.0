#!/usr/bin/env python3
"""Stage 3.69A-1 low-alpha Schwarzschild-Dirac regression test.

Purpose
-------
Validate the horizon-to-infinity coefficient extraction against the published
Unruh/Doran low-energy limit before applying the solver to the Earth branch.

Natural units G=hbar=c=M_BH=1 are used, so m=alpha_g.
This is a single-particle wave benchmark, NOT the dense-core net accretion rate.
"""

from math import exp, pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp


def radial_A(x, kappa, E, m):
    s = sqrt(2.0 / x)
    B = np.array([[1.0, s], [s, 1.0]], dtype=complex)
    C = np.array([
        [kappa / x, 1j * (E + m) - s / (4.0 * x)],
        [1j * (E - m) - s / (4.0 * x), -kappa / x],
    ], dtype=complex)
    return B @ C


def horizon_u0(kappa, E, m):
    return np.array([
        kappa - 2j * (E + m) + 0.25,
        kappa + 2j * (E - m) - 0.25,
    ], dtype=complex)


def horizon_u1(kappa, E, m):
    x0 = 2.0
    A0 = radial_A(x0, kappa, E, m)
    h = 1.0e-5
    A1 = (radial_A(x0 + h, kappa, E, m) - radial_A(x0 - h, kappa, E, m)) / (2.0 * h)
    return np.linalg.solve(0.5 * np.eye(2, dtype=complex) - A0, A1 @ horizon_u0(kappa, E, m))


def wronskian(U, x):
    s = sqrt(2.0 / x)
    J = np.array([[-s, 1.0], [1.0, -s]], dtype=complex)
    return float(np.real(np.vdot(U, J @ U)))


def integrate_samples(alpha, speed_u, kappa, xs):
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    m = alpha
    E = alpha * gamma
    eps = 1.0e-6
    x0 = 2.0 + eps
    U0 = horizon_u0(kappa, E, m) + eps * horizon_u1(kappa, E, m)
    U0 /= sqrt(-wronskian(U0, x0))

    sol = solve_ivp(
        lambda x, y: radial_A(x, kappa, E, m) @ y / (1.0 - 2.0 / x),
        (x0, float(xs[-1])), U0, t_eval=xs,
        method="DOP853", rtol=1.0e-12, atol=1.0e-14,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol, E, m


def local_incoming_amplitude(U, x, kappa, E, m):
    """Finite-radius WKB/local-eigenmode extraction of |alpha_kappa|."""
    D = radial_A(x, kappa, E, m) / (1.0 - 2.0 / x)
    vals, vecs = np.linalg.eig(D)
    p = sqrt(E**2 - m**2)
    beta = (m**2 + 2.0 * p**2) / p
    target_in = -p + E * sqrt(2.0 / x) - beta / x
    target_out = +p + E * sqrt(2.0 / x) + beta / x
    i_in = int(np.argmin(np.abs(vals.imag - target_in)))
    i_out = int(np.argmin(np.abs(vals.imag - target_out)))

    vin = vecs[:, i_in]
    vout = vecs[:, i_out]
    q = p / (E + m)
    Win = wronskian(vin, x)
    Wout = wronskian(vout, x)
    if not (Win < 0.0 and Wout > 0.0):
        raise RuntimeError("Could not identify in/out flux modes")
    vin *= sqrt((-2.0 * q) / Win)
    vout *= sqrt((+2.0 * q) / Wout)
    ain, _ = np.linalg.solve(np.column_stack([vin, vout]), U)
    return float(abs(ain))


def extrapolated_alpha(alpha, speed_u, kappa, x_max, n=30):
    xs = np.geomspace(0.25 * x_max, x_max, n)
    sol, E, m = integrate_samples(alpha, speed_u, kappa, xs)
    amps = np.array([
        local_incoming_amplitude(U, x, kappa, E, m)
        for U, x in zip(sol.y.T, xs)
    ])
    fit = np.polyfit(1.0 / np.sqrt(xs), amps, 2)
    a_inf = float(np.polyval(fit, 0.0))
    return a_inf, wronskian(sol.y[:, -1], x_max)


def sigma_lowest_partialwaves(alpha, E_over_m, x_max):
    u = sqrt(1.0 - 1.0 / E_over_m**2)
    E = alpha * E_over_m
    m = alpha
    p = sqrt(E**2 - m**2)
    total = 0.0
    details = []
    for kappa in (-1, +1):
        a_inf, W_end = extrapolated_alpha(alpha, u, kappa, x_max)
        total += 1.0 / a_inf**2
        details.append((kappa, a_inf, W_end))
    sigma = pi * total / (2.0 * p * (E - m))  # Doran et al. Eq. (30)
    return sigma, details


def unruh(alpha, speed_u):
    root = sqrt(1.0 - speed_u**2)
    X = 2.0 * pi * alpha * (1.0 + speed_u**2) / (speed_u * root)
    denom = 1.0 if X > 700.0 else 1.0 - exp(-X)
    return 4.0 * pi**2 * (1.0 + speed_u**2) * alpha / (speed_u**2 * root * denom)


def main():
    alpha = 0.0025
    E_over_m = 2.0
    u = sqrt(1.0 - 1.0 / E_over_m**2)
    analytic = unruh(alpha, u)
    print(f"alpha={alpha}, E/m={E_over_m}, u={u:.12f}")
    print(f"Unruh/Doran sigma/M^2 = {analytic:.12f}")

    for x_max in (20_000.0, 40_000.0):
        sigma, details = sigma_lowest_partialwaves(alpha, E_over_m, x_max)
        print(f"x_max={x_max:.0f} sigma/M^2={sigma:.12f} rel_to_Unruh={(sigma/analytic-1)*100:+.6f}%")
        for kappa, a_inf, W_end in details:
            print(f"  kappa={kappa:+d} |alpha_kappa|={a_inf:.12f} W_end={W_end:.12f}")


if __name__ == "__main__":
    main()
