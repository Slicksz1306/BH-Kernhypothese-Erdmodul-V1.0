#!/usr/bin/env python3
"""Stage 3.72 / A28: nonlinear relativistic Thomas-Fermi screening.

Static spherical electron-screening proxy around a positive point charge in a
uniform positive ionic background.  The electron gas is treated as T=0
relativistic-degenerate Thomas-Fermi matter.  This replaces A25's linear
Yukawa shape as a screening-structure sensitivity test, but it is NOT a full
finite-T WDM/ion-motion/current-balance closure and does not determine Q_eq.
"""
from math import e as EULER, pi, sqrt
import numpy as np
from scipy.integrate import solve_bvp

EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19
M_E_C2_EV = 510_998.95

ENDPOINTS = {
    "low-Zbar": {"ne": 3.88e29, "EF_eV": 19.4},
    "fully-ionized": {"ne": 3.66e30, "EF_eV": 86.6},
}


def endpoint_params(ne: float, EF_eV: float):
    eps = EF_eV / M_E_C2_EV
    mu0 = 1.0 + eps
    # d(n/n0)/dpsi at psi=0, psi=e phi / EF.
    fp0 = 3.0 * mu0 / (2.0 + eps)
    EF_J = EF_eV * E_CHARGE
    lam = sqrt(EPS0 * EF_J / (E_CHARGE**2 * ne * fp0))
    q1 = E_CHARGE**2 / (4.0*pi*EPS0*lam*EF_J)
    return eps, mu0, fp0, lam, q1


def solve_profile(ne: float, EF_eV: float, Qe: float,
                  xmin: float = 1e-6, xmax: float = 30.0,
                  ngrid: int = 4000):
    eps, mu0, fp0, lam, q1 = endpoint_params(ne, EF_eV)
    qdim = Qe*q1
    A0 = mu0*mu0 - 1.0

    x = np.geomspace(xmin, xmax, ngrid)
    psi0 = qdim*np.exp(-x)/x
    dpsi0 = -qdim*np.exp(-x)*(1.0/x + 1.0/x**2)

    def density_ratio(psi):
        A = (mu0 + eps*psi)**2 - 1.0
        A = np.maximum(A, 0.0)
        return (A/A0)**1.5

    def fun(xx, yy):
        psi, dpsi = yy
        rhs = (density_ratio(psi) - 1.0)/fp0
        return np.vstack([dpsi, rhs - 2.0*dpsi/xx])

    def bc(ya, yb):
        # Point-charge flux at inner edge, vanishing potential far away.
        return np.array([xmin*xmin*ya[1] + qdim, yb[0]])

    sol = solve_bvp(
        fun, bc, x, np.vstack([psi0, dpsi0]),
        tol=1e-5, max_nodes=100000,
    )
    if not sol.success:
        raise RuntimeError(sol.message)
    return sol, lam, q1, density_ratio


def screening_radii(sol, qdim):
    xs = np.geomspace(1e-5, 20.0, 20000)
    _, dpsi = sol.sol(xs)
    enclosed = -xs*xs*dpsi/qdim
    out = {}
    for remaining in (0.5, 0.1, 0.01):
        idx = np.where(enclosed <= remaining)[0]
        out[remaining] = float(xs[idx[0]]) if len(idx) else float("nan")
    return out


def main():
    print("Stage 3.72 / A28 nonlinear relativistic Thomas-Fermi screening")
    for label, p in ENDPOINTS.items():
        ne, EF = p["ne"], p["EF_eV"]
        eps, mu0, fp0, lam, q1 = endpoint_params(ne, EF)
        print(f"\n[{label}] ne={ne:.6e} m^-3 EF={EF:.6f} eV")
        print(f"lambda_lin={lam:.12e} m, qdim_per_e={q1:.9e}, fprime0={fp0:.9e}")
        print("Qe,psi(lambda),ne(lambda)/n0,psi/linearYukawa,r50/lambda,r90/lambda,r99/lambda")
        for Q in range(1, 6):
            sol, _, _, density_ratio = solve_profile(ne, EF, float(Q))
            psi1 = float(sol.sol(1.0)[0])
            den1 = float(density_ratio(psi1))
            linear1 = Q*q1/EULER
            sr = screening_radii(sol, Q*q1)
            print(
                f"{Q},{psi1:.9e},{den1:.9e},{psi1/linear1:.9e},"
                f"{sr[0.5]:.9e},{sr[0.1]:.9e},{sr[0.01]:.9e}"
            )

    print("\nInterpretation")
    print("- Q=1...5e already enters nonlinear TF response, especially at the low-EF endpoint")
    print("- nonlinear electron pile-up strengthens screening relative to linear Yukawa")
    print("- ~90% of the point charge is screened within only a few lambda_TF in this static proxy")
    print("- this does not determine the floating/current-balance Q_eq")
    print("- finite T, exchange-correlation, ion motion, mixture effects and dynamic currents remain OPEN")


if __name__ == "__main__":
    main()
