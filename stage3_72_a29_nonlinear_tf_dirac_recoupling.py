#!/usr/bin/env python3
"""Stage 3.72 / A29: recouple A28 nonlinear TF screening to A25 Dirac sink.

Scope: endpoint Fermi speeds, Q=1,3,5 e, static spherical screening only.
This is NOT a collective floating-charge calculation.
"""
from math import exp, log, pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp

from stage3_72_a25_flux_direct_screened_electron import (
    C, ALPHA_E, ALPHA_EM, R_G, params, current_matrix, wronskian,
    sigma_abs as sigma_yukawa, V_F,
)
from stage3_72_a28_nonlinear_tf_screening import (
    ENDPOINTS, M_E_C2_EV, endpoint_params, solve_profile,
)


class NonlinearTFPotential:
    def __init__(self, ne: float, EF_eV: float, charge_e: float):
        self.ne = ne
        self.EF_eV = EF_eV
        self.charge_e = charge_e
        self.sol, self.lam, self.q1, _ = solve_profile(ne, EF_eV, charge_e, xmax=40.0)
        self.eps = EF_eV/M_E_C2_EV
        self.x_tf = self.lam/R_G

    def delta_energy(self, x: float) -> float:
        z = x/self.x_tf
        if z >= 40.0:
            return 0.0
        z = max(z, 1.0e-6)
        psi = float(self.sol.sol(z)[0])
        # Natural Dirac energy shift: alpha_e * e phi/(m_e c^2).
        return ALPHA_E*self.eps*psi


def radial_A_nltf(x: float, kappa: int, speed: float,
                  profile: NonlinearTFPotential | None) -> np.ndarray:
    _, mass, energy, _ = params(speed)
    s = sqrt(2.0/x)
    e_local = energy + (profile.delta_energy(x) if profile is not None else 0.0)
    B = np.array([[1.0, s], [s, 1.0]], dtype=complex)
    Cmat = np.array([
        [kappa/x, 1j*(e_local+mass)-s/(4.0*x)],
        [1j*(e_local-mass)-s/(4.0*x), -kappa/x],
    ], dtype=complex)
    return B @ Cmat


def horizon_initial(kappa: int, speed: float, profile: NonlinearTFPotential | None,
                    eps_h: float = 1.0e-6):
    _, mass, energy, _ = params(speed)
    xh = 2.0
    A0 = radial_A_nltf(xh, kappa, speed, profile)
    dh = 1.0e-5
    A1 = (
        radial_A_nltf(xh+dh, kappa, speed, profile)
        - radial_A_nltf(xh-dh, kappa, speed, profile)
    )/(2.0*dh)
    e_h = energy + (profile.delta_energy(xh) if profile is not None else 0.0)
    u0 = np.array([
        kappa - 2j*(e_h+mass) + 0.25,
        kappa + 2j*(e_h-mass) - 0.25,
    ], dtype=complex)
    u1 = np.linalg.solve(0.5*np.eye(2, dtype=complex)-A0, A1 @ u0)
    x0 = xh + eps_h
    U = u0 + eps_h*u1
    W = wronskian(U, x0)
    if W >= 0.0:
        raise RuntimeError("regular horizon branch is not inward")
    U /= sqrt(-W)
    return x0, U


def choose_xmatch(speed: float, profile: NonlinearTFPotential | None) -> float:
    u = speed/C
    xtf = profile.x_tf if profile is not None else 5.0e5
    return max(2.0e7, 40.0*xtf, 20.0/u**2)


def integrate_log_normalized(kappa: int, speed: float,
                             profile: NonlinearTFPotential | None,
                             xmatch: float, segments: int = 320):
    x, U = horizon_initial(kappa, speed, profile)
    log_scale = 0.0
    for x1 in np.geomspace(x, xmatch, segments+1)[1:]:
        sol = solve_ivp(
            lambda xx, yy: radial_A_nltf(xx, kappa, speed, profile) @ yy
                           /(1.0-2.0/xx),
            (x, x1), U, method="DOP853", rtol=2.0e-10, atol=2.0e-12,
        )
        if not sol.success:
            raise RuntimeError(sol.message)
        raw = sol.y[:, -1]
        norm = np.linalg.norm(raw)
        log_scale += log(norm)
        U = raw/norm
        x = x1
    return U, log_scale


def pabs(kappa: int, speed: float, profile: NonlinearTFPotential | None) -> float:
    xmatch = choose_xmatch(speed, profile)
    U, log_scale = integrate_log_normalized(kappa, speed, profile, xmatch)
    D = radial_A_nltf(xmatch, kappa, speed, None)/(1.0-2.0/xmatch)
    _, vecs = np.linalg.eig(D)
    currents = [wronskian(vecs[:, j], xmatch) for j in range(2)]
    i_in = int(np.argmin(currents))
    i_out = int(np.argmax(currents))
    W_in = currents[i_in]
    if not (W_in < 0.0 < currents[i_out]):
        raise RuntimeError("could not identify asymptotic modes")
    A_in = np.linalg.solve(
        np.column_stack([vecs[:, i_in], vecs[:, i_out]]), U
    )[0]
    return exp(-log(-W_in)-2.0*log(abs(A_in))-2.0*log_scale)


def sigma_nltf(speed: float, profile: NonlinearTFPotential | None, kmax: int = 1):
    _, _, _, p = params(speed)
    total = 0.0
    for k in range(1, kmax+1):
        for kappa in (-k, +k):
            total += abs(kappa)*pabs(kappa, speed, profile)
    return pi*total/p**2


def main() -> None:
    print("Stage 3.72 / A29 nonlinear-TF -> flux-direct Dirac recoupling")
    for idx, (label, ep) in enumerate(ENDPOINTS.items()):
        speed = V_F[idx]
        ne, EF = ep["ne"], ep["EF_eV"]
        _, _, _, lam, _ = endpoint_params(ne, EF)
        x_tf = lam/R_G
        neutral = sigma_nltf(speed, None)
        print(f"\n[{label}] vF={speed:.9e} m/s EF={EF:.6f} eV lambda={lam:.9e} m")
        print("Qe,linearYukawa/neutral,nonlinearTF/neutral,nonlinear/linear")
        for Q in (1.0, 3.0, 5.0):
            prof = NonlinearTFPotential(ne, EF, Q)
            nl = sigma_nltf(speed, prof)
            lin = sigma_yukawa(speed, Q, x_tf, kmax=1)[0]
            print(f"{Q:.0f},{lin/neutral:.9e},{nl/neutral:.9e},{nl/lin:.9e}")

    print("\nInterpretation")
    print("- A28 nonlinear static screening changes endpoint-vF A25 capture only at the few-percent level for Q<=5e")
    print("- the sign and order-of-magnitude of positive-Q electron focusing survive")
    print("- this does not determine Q_eq or replace collective WDM transport")


if __name__ == "__main__":
    main()
