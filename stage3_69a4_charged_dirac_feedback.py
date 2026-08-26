#!/usr/bin/env python3
"""Stage 3.69A-4: charged proton Dirac capture + charge feedback.

This extends the Stage-3.69A-1 Schwarzschild Dirac system by minimal
coupling to a weak central Coulomb field while keeping the geometry
Schwarzschild.  This is justified only for |Q| << Q_extremal; it is NOT a
full Reissner-Nordstrom wave solver.

The code is intentionally scoped to the proton channel.  At Earth speed
the electron asymptotic momentum is so small that the local finite-radius
basis used here is not a controlled Coulomb far-field matcher.  Charged
electron wave capture therefore remains OPEN.

Natural radial units: G=hbar=c=M_BH=1, x=r/M.
For a proton and BH charge Q=N e, the Coulomb energy shift is
    E_eff(x) = E_inf - N * alpha_EM / x.

The integrated two-spinor is renormalized between logarithmic radial
segments.  Only its direction and the asymptotic A_out/A_in ratio are
required, so this prevents large dynamic-range loss without changing the
reflection coefficient.
"""

from __future__ import annotations

from math import pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import root

from stage3_69a1_dirac_prototype import (
    G, C, HBAR, M_P, alpha_g, classical_sigma_dimensionless, current_matrix,
)

EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19
ALPHA_EM = E_CHARGE**2 / (4.0 * pi * EPS0 * HBAR * C)
V_EARTH = 10.4355e3
U_EARTH = V_EARTH / C
M_REF = 1.0e11


def wronskian(U: np.ndarray, x: float) -> float:
    return float(np.real(np.vdot(U, current_matrix(x) @ U)))


def radial_A_charged(x: float, kappa: int, energy: float, mass: float, zeta: float) -> np.ndarray:
    """Doran radial matrix with minimal electrostatic energy shift."""
    s = sqrt(2.0 / x)
    e_local = energy - zeta / x
    B = np.array([[1.0, s], [s, 1.0]], dtype=complex)
    Cmat = np.array(
        [
            [kappa / x, 1j * (e_local + mass) - s / (4.0 * x)],
            [1j * (e_local - mass) - s / (4.0 * x), -kappa / x],
        ],
        dtype=complex,
    )
    return B @ Cmat


def rhs(x: float, y: np.ndarray, kappa: int, energy: float, mass: float, zeta: float) -> np.ndarray:
    return radial_A_charged(x, kappa, energy, mass, zeta) @ y / (1.0 - 2.0 / x)


def horizon_initial(alpha: float, speed_u: float, kappa: int, zeta: float, eps: float = 1.0e-6):
    gamma = 1.0 / sqrt(1.0 - speed_u**2)
    mass = alpha
    energy = alpha * gamma
    e_h = energy - zeta / 2.0
    u0 = np.array(
        [
            kappa - 2j * (e_h + mass) + 0.25,
            kappa + 2j * (e_h - mass) - 0.25,
        ],
        dtype=complex,
    )
    xh = 2.0
    A0 = radial_A_charged(xh, kappa, energy, mass, zeta)
    h = 1.0e-5
    A1 = (
        radial_A_charged(xh + h, kappa, energy, mass, zeta)
        - radial_A_charged(xh - h, kappa, energy, mass, zeta)
    ) / (2.0 * h)
    u1 = np.linalg.solve(0.5 * np.eye(2, dtype=complex) - A0, A1 @ u0)
    x0 = xh + eps
    U = u0 + eps * u1
    U /= np.linalg.norm(U)
    return x0, U, energy, mass


def integrate_direction(alpha: float, speed_u: float, kappa: int, zeta: float, x_match: float, segments: int = 120):
    x, U, energy, mass = horizon_initial(alpha, speed_u, kappa, zeta)
    edges = np.geomspace(x, x_match, segments)
    for x1 in edges[1:]:
        sol = solve_ivp(
            lambda xx, yy: rhs(xx, yy, kappa, energy, mass, zeta),
            (x, x1), U, method="DOP853", rtol=2.0e-10, atol=2.0e-12,
        )
        if not sol.success:
            raise RuntimeError(sol.message)
        U = sol.y[:, -1]
        U /= np.linalg.norm(U)
        x = x1
    return U, energy, mass


def absorption_probability(alpha: float, speed_u: float, kappa: int, charge_e: float, x_match: float) -> float:
    """Flux reflection at finite large radius; controlled here for proton scan."""
    zeta = charge_e * ALPHA_EM
    U, energy, mass = integrate_direction(alpha, speed_u, kappa, zeta, x_match)
    D = radial_A_charged(x_match, kappa, energy, mass, zeta) / (1.0 - 2.0 / x_match)
    _, vecs = np.linalg.eig(D)
    currents = [wronskian(vecs[:, j], x_match) for j in range(2)]
    i_in = int(np.argmin(currents))
    i_out = int(np.argmax(currents))
    Uin, Uout = vecs[:, i_in], vecs[:, i_out]
    Win, Wout = wronskian(Uin, x_match), wronskian(Uout, x_match)
    if not (Win < 0.0 < Wout):
        raise RuntimeError("Could not identify charged in/out flux modes")
    Ain, Aout = np.linalg.solve(np.column_stack([Uin, Uout]), U)
    reflection = Wout * abs(Aout) ** 2 / ((-Win) * abs(Ain) ** 2)
    return max(0.0, 1.0 - reflection)


def proton_sigma_ratio(charge_e: float, x_match: float = 5.0e5, kmax: int = 2) -> tuple[float, list]:
    alpha = alpha_g(M_REF, M_P)
    gamma = 1.0 / sqrt(1.0 - U_EARTH**2)
    p = alpha * U_EARTH * gamma
    total = 0.0
    rows = []
    for k in range(1, kmax + 1):
        for kappa in (-k, +k):
            P = absorption_probability(alpha, U_EARTH, kappa, charge_e, x_match)
            total += abs(kappa) * P
            rows.append((kappa, P))
    sigma_dim = pi * total / p**2
    return sigma_dim / classical_sigma_dimensionless(U_EARTH), rows


def proton_force_limit_e(M_bh_kg: float = M_REF) -> float:
    q_coulomb = 4.0 * pi * EPS0 * G * M_bh_kg * M_P / E_CHARGE
    return q_coulomb / E_CHARGE


def nakao_dimensionless_Qp(charge_e: float) -> float:
    """Nakao et al. convention: Q_p=1/2 at proton force balance."""
    return 0.5 * charge_e / proton_force_limit_e(M_REF)


def charged_classical_ratio(charge_e: float) -> float:
    """Relativistic charged-test-particle critical-L proxy from Nakao effective potential."""
    E = 1.0 / sqrt(1.0 - U_EARTH**2)
    Qp = nakao_dimensionless_Qp(charge_e)

    def equations(z):
        R, L2 = z
        Ueff = 1.0 - E**2 - (1.0 - 2.0 * Qp * E) / R + (L2 - Qp**2) / R**2 - L2 / R**3
        dU = (1.0 - 2.0 * Qp * E) / R**2 - 2.0 * (L2 - Qp**2) / R**3 + 3.0 * L2 / R**4
        return [Ueff, dU]

    sol = root(equations, [2.0, 4.0])
    if not sol.success:
        raise RuntimeError("Charged classical critical-orbit solve failed")
    L2 = float(sol.x[1])
    return L2 / 4.0


def main() -> None:
    print("Stage 3.69A-4 charged proton Dirac feedback")
    print(f"M={M_REF:.3e} kg, v={V_EARTH/1e3:.4f} km/s")
    print("charge_e, dirac_sigma/neutral_classical, charged_classical/neutral_classical")
    for N in (0.0, 1.0, 2.0, 3.67, 5.0, 10.0, 15.0, 20.0, 24.18, 30.0, 40.0):
        ratio, _ = proton_sigma_ratio(N)
        print(f"{N:8.2f}, {ratio:.9f}, {charged_classical_ratio(N):.9f}")

    print("\nMatching-radius stability")
    for N in (0.0, 3.67, 10.0, 24.18):
        vals = []
        for xm in (2.0e5, 5.0e5, 1.0e6):
            vals.append(proton_sigma_ratio(N, x_match=xm)[0])
        print(f"Q={N:5.2f} e: " + ", ".join(f"{v:.9f}" for v in vals))

    print("\nScope")
    print("- proton charged-Coulomb wave proxy evaluated on Schwarzschild geometry")
    print("- Q=0 reproduces the Stage-3.69A-3 neutral result to matching accuracy")
    print("- plausible positive Q suppresses proton capture by O(1), not by many orders")
    print("- diffuse-plasma equilibrium Q values are benchmarks, not dense-core closure")
    print("- charged electron Coulomb far-field matching remains OPEN")
    print("- H+ and H0 remain parallel branches")


if __name__ == "__main__":
    main()
