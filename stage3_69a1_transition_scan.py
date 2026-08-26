#!/usr/bin/env python3
"""Stage 3.69A-1 intermediate-alpha Schwarzschild-Dirac transition scan.

Fixed u=0.5 solver benchmark. This is NOT an Earth-core velocity calculation.
It tests the published qualitative requirement that the fermion absorption
cross section oscillates around the classical point-particle result and tends
toward it as alpha increases.

Only partial waves whose conserved-current drift remains below 1e-4 are used.
Numerically unstable high-|kappa| tail modes are discarded; their physical
absorption contribution is already tiny at the chosen kmax.
"""

from math import pi, sqrt
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


def wronskian(U, x):
    s = sqrt(2.0 / x)
    J = np.array([[-s, 1.0], [1.0, -s]], dtype=complex)
    return float(np.real(np.vdot(U, J @ U)))


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


def one_mode(alpha, u, kappa, x_match):
    gamma = 1.0 / sqrt(1.0 - u**2)
    m = alpha
    E = alpha * gamma
    p = alpha * u * gamma
    eps = 1.0e-6
    x0 = 2.0 + eps
    U0 = horizon_u0(kappa, E, m) + eps * horizon_u1(kappa, E, m)
    U0 /= sqrt(-wronskian(U0, x0))

    sol = solve_ivp(
        lambda x, y: radial_A(x, kappa, E, m) @ y / (1.0 - 2.0 / x),
        (x0, x_match), U0,
        method="DOP853", rtol=2.0e-10, atol=2.0e-12,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    U = sol.y[:, -1]

    D = radial_A(x_match, kappa, E, m) / (1.0 - 2.0 / x_match)
    vals, vecs = np.linalg.eig(D)
    beta = (m**2 + 2.0 * p**2) / p
    target_in = -p + E * sqrt(2.0 / x_match) - beta / x_match
    target_out = +p + E * sqrt(2.0 / x_match) + beta / x_match
    i_in = int(np.argmin(np.abs(vals.imag - target_in)))
    i_out = int(np.argmin(np.abs(vals.imag - target_out)))

    vin = vecs[:, i_in]
    vout = vecs[:, i_out]
    q = p / (E + m)
    Win = wronskian(vin, x_match)
    Wout = wronskian(vout, x_match)
    if not (Win < 0.0 and Wout > 0.0):
        raise RuntimeError("Could not identify in/out modes")
    vin *= sqrt((-2.0 * q) / Win)
    vout *= sqrt((+2.0 * q) / Wout)

    Ain, Aout = np.linalg.solve(np.column_stack([vin, vout]), U)
    Pabs = 1.0 - abs(Aout / Ain)**2
    return Pabs, wronskian(U, x_match)


def sigma_filtered(alpha, u, kmax, x_match, W_tol=1.0e-4):
    p = alpha * u / sqrt(1.0 - u**2)
    total = 0.0
    rows = []
    for k in range(1, kmax + 1):
        for kappa in (-k, +k):
            Pabs, Wend = one_mode(alpha, u, kappa, x_match)
            drift = abs(Wend + 1.0)
            accepted = drift < W_tol and -1.0e-6 <= Pabs <= 1.0 + 1.0e-6
            if accepted:
                P = min(1.0, max(0.0, Pabs))
                total += abs(kappa) * P
            rows.append((kappa, Pabs, drift, accepted))
    return pi * total / p**2, rows


def classical_sigma(u):
    return pi / (2.0 * u**4) * (
        8.0 * u**4 + 20.0 * u**2 - 1.0 + (1.0 + 8.0 * u**2)**1.5
    )


def main():
    u = 0.5
    classical = classical_sigma(u)
    cases = [(0.2, 4), (0.35, 5), (0.7, 7)]
    print(f"u={u}, classical sigma/M^2={classical:.12f}")
    for alpha, kmax in cases:
        print(f"\nalpha={alpha}, kmax={kmax}")
        for x_match in (500.0, 1000.0):
            sigma, rows = sigma_filtered(alpha, u, kmax, x_match)
            used = [k for k, _, _, ok in rows if ok]
            print(
                f"x_match={x_match:.0f} sigma/M^2={sigma:.12f} "
                f"ratio_to_classical={sigma/classical:.12f} used={used}"
            )


if __name__ == "__main__":
    main()
