#!/usr/bin/env python3
"""Stage 3.72 / A25: flux-direct screened-electron Dirac prototype.

This fixes the numerical conditioning problem identified in A21 by evaluating
absorption from the conserved incoming flux directly instead of subtracting
P_abs = 1-|S|^2 when P_abs is ~1e-11.

Model scope
-----------
- Schwarzschild/Doran massive Dirac equation used in A1/A4.
- BH charge Q=N e enters through a finite-range Yukawa-screened Coulomb proxy
  V ~ exp(-r/lambda_TF)/r for an electron (attractive for positive Q).
- lambda_TF is held constant as a sensitivity parameter at the A14 outer-core
  values. This is NOT a self-consistent nonlinear/radially varying screening
  calculation.
- Q scan is restricted to 0...5 e, the A14 linear-response-scale bracket.
- Neutral cases are regressed against the Unruh low-energy result.
- Electron speeds include the A14 degenerate-Fermi endpoints, not only c_eff.

The output is an isolated-particle/static-screening S-matrix proxy, not Q(t)
or a final dense-plasma electron current closure.
"""

from __future__ import annotations

from math import exp, log, pi, sqrt
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.integrate import solve_ivp

G = 6.67430e-11
C = 299_792_458.0
HBAR = 1.054571817e-34
M_E = 9.1093837015e-31
EPS0 = 8.8541878128e-12
E_CHARGE = 1.602176634e-19
ALPHA_EM = E_CHARGE**2/(4*pi*EPS0*HBAR*C)

M_REF = 1.0e11
V_EARTH = 10.4355e3
R_G = G*M_REF/C**2
ALPHA_E = G*M_REF*M_E/(HBAR*C)

# A14 outer-core Thomas-Fermi bracket.
LAMBDA_TF = (2.95e-11, 4.29e-11)
X_TF = tuple(lam/R_G for lam in LAMBDA_TF)
X_TF_MID = 0.5*(X_TF[0] + X_TF[1])

# A14 Fermi-energy bracket from Zbar~2.76 through fully stripped upper proxy.
E_F_EV = (19.4, 86.6)
V_F = tuple(sqrt(2*E*E_CHARGE/M_E) for E in E_F_EV)


def params(speed: float):
    u = speed/C
    gamma = 1.0/sqrt(1.0-u*u)
    mass = ALPHA_E
    energy = ALPHA_E*gamma
    momentum = ALPHA_E*u*gamma
    return u, mass, energy, momentum


def current_matrix(x: float) -> np.ndarray:
    s = sqrt(2.0/x)
    return np.array([[-s, 1.0], [1.0, -s]], dtype=complex)


def wronskian(U: np.ndarray, x: float) -> float:
    return float(np.real(np.vdot(U, current_matrix(x) @ U)))


def radial_A(x: float, kappa: int, speed: float, charge_e: float,
             x_tf: float) -> np.ndarray:
    _, mass, energy, _ = params(speed)
    s = sqrt(2.0/x)

    # Electron q=-e around positive BH Q=+N e -> attractive potential.
    # A4 convention has e_local = E - zeta/x, hence zeta<0 for electron.
    zeta = -charge_e*ALPHA_EM*exp(-x/x_tf) if charge_e else 0.0
    e_local = energy - zeta/x

    B = np.array([[1.0, s], [s, 1.0]], dtype=complex)
    Cmat = np.array([
        [kappa/x, 1j*(e_local+mass)-s/(4*x)],
        [1j*(e_local-mass)-s/(4*x), -kappa/x],
    ], dtype=complex)
    return B @ Cmat


def horizon_initial(kappa: int, speed: float, charge_e: float, x_tf: float,
                    eps: float = 1e-6):
    _, mass, energy, _ = params(speed)
    xh = 2.0
    A0 = radial_A(xh, kappa, speed, charge_e, x_tf)
    dh = 1e-5
    A1 = (
        radial_A(xh+dh, kappa, speed, charge_e, x_tf)
        - radial_A(xh-dh, kappa, speed, charge_e, x_tf)
    )/(2*dh)

    zeta_h = -charge_e*ALPHA_EM*exp(-xh/x_tf) if charge_e else 0.0
    e_h = energy - zeta_h/xh
    u0 = np.array([
        kappa - 2j*(e_h+mass) + 0.25,
        kappa + 2j*(e_h-mass) - 0.25,
    ], dtype=complex)
    u1 = np.linalg.solve(0.5*np.eye(2, dtype=complex)-A0, A1 @ u0)
    x0 = xh + eps
    U = u0 + eps*u1
    W = wronskian(U, x0)
    if W >= 0:
        raise RuntimeError("regular horizon branch does not carry inward flux")
    U /= sqrt(-W)  # physical normalization W_H=-1
    return x0, U


def choose_xmatch(speed: float, x_tf: float) -> float:
    u = speed/C
    # Require both screened potential and Schwarzschild phase drift to be small.
    return max(2.0e7, 20.0*x_tf, 20.0/u**2)


def integrate_log_normalized(kappa: int, speed: float, charge_e: float,
                             x_tf: float, xmatch: float,
                             segments: int = 320,
                             rtol: float = 2e-10):
    x, U = horizon_initial(kappa, speed, charge_e, x_tf)
    log_scale = 0.0
    for x1 in np.geomspace(x, xmatch, segments+1)[1:]:
        sol = solve_ivp(
            lambda xx, yy: radial_A(xx, kappa, speed, charge_e, x_tf) @ yy
                           /(1.0-2.0/xx),
            (x, x1), U, method="DOP853", rtol=rtol, atol=rtol*1e-2,
        )
        if not sol.success:
            raise RuntimeError(sol.message)
        Uraw = sol.y[:, -1]
        norm = np.linalg.norm(Uraw)
        log_scale += log(norm)
        U = Uraw/norm
        x = x1
    return U, log_scale


def absorption_probability(kappa: int, speed: float, charge_e: float,
                           x_tf: float, xmatch: float | None = None) -> float:
    if xmatch is None:
        xmatch = choose_xmatch(speed, x_tf)

    U, log_scale = integrate_log_normalized(
        kappa, speed, charge_e, x_tf, xmatch
    )

    # At the matching radius the Yukawa term is negligible. Build the neutral
    # local exact in/out basis and identify modes by current sign.
    D = radial_A(xmatch, kappa, speed, 0.0, x_tf)/(1.0-2.0/xmatch)
    _, vecs = np.linalg.eig(D)
    currents = [wronskian(vecs[:, j], xmatch) for j in range(2)]
    i_in = int(np.argmin(currents))
    i_out = int(np.argmax(currents))
    W_in = currents[i_in]
    W_out = currents[i_out]
    if not (W_in < 0.0 < W_out):
        raise RuntimeError("could not identify inward/outward flux modes")

    A_in = np.linalg.solve(
        np.column_stack([vecs[:, i_in], vecs[:, i_out]]), U
    )[0]

    # Actual horizon solution has W_H=-1. Segment renormalization is restored
    # through log_scale. This evaluates absorbed/incoming flux DIRECTLY and
    # never forms 1-|S|^2.
    log_pabs = -log(-W_in) - 2.0*log(abs(A_in)) - 2.0*log_scale
    return exp(log_pabs)


def sigma_abs(speed: float, charge_e: float, x_tf: float,
              kmax: int = 2, xmatch: float | None = None):
    _, _, _, p = params(speed)
    total = 0.0
    rows = []
    for k in range(1, kmax+1):
        for kappa in (-k, +k):
            P = absorption_probability(kappa, speed, charge_e, x_tf, xmatch)
            total += abs(kappa)*P
            rows.append((kappa, P))
    dimless = pi*total/p**2
    return dimless, dimless*R_G**2, rows


def unruh_low_energy(speed: float) -> float:
    u = speed/C
    root = sqrt(1.0-u*u)
    X = 2*pi*ALPHA_E*(1.0+u*u)/(u*root)
    denom = 1.0 if X > 700.0 else 1.0-exp(-X)
    return 4*pi*pi*(1.0+u*u)*ALPHA_E/(u*u*root*denom)


def fermi_average_sigma_v(vf: float, charge_e: float, x_tf: float,
                          quadrature: int = 6) -> float:
    """T=0 nonrelativistic Fermi-sphere average <sigma v>.

    Speed density is 3 v^2/v_F^3. This is a controlled degeneracy proxy, not a
    finite-T Fermi-Dirac/collective plasma current calculation.
    """
    nodes, weights = leggauss(quadrature)
    xs = 0.5*(nodes+1.0)
    ws = 0.5*weights
    out = 0.0
    for x, w in zip(xs, ws):
        speed = x*vf
        _, sigma_m2, _ = sigma_abs(speed, charge_e, x_tf, kmax=1)
        out += w*3*x*x*sigma_m2*speed
    return float(out)


def neutral_regression() -> None:
    print("Neutral Unruh regressions")
    for speed in (V_EARTH, *V_F):
        target = unruh_low_energy(speed)
        got, _, rows = sigma_abs(speed, 0.0, X_TF_MID, kmax=2)
        print(
            f"v={speed:.6e} m/s target={target:.12e} got={got:.12e} "
            f"rel={got/target-1:+.3e} rows={rows}"
        )


def matching_regression() -> None:
    print("\nMatching-radius regression, representative Q=5")
    for speed in V_F:
        base = choose_xmatch(speed, X_TF_MID)
        vals = []
        for factor in (0.5, 1.0, 2.0, 5.0):
            dimless, _, _ = sigma_abs(
                speed, 5.0, X_TF_MID, kmax=2, xmatch=base*factor
            )
            vals.append(dimless)
        print(f"v={speed:.6e}: " + ", ".join(f"{x:.9e}" for x in vals))


def scan() -> None:
    print("\nFermi-endpoint screened-Q scan")
    for speed in V_F:
        neutral = sigma_abs(speed, 0.0, X_TF_MID, kmax=2)[0]
        print(f"vF={speed:.6e} m/s")
        print("Qe, ratio_minTF, ratio_maxTF")
        for Q in range(0, 6):
            ratios = []
            for xtf in X_TF:
                dimless, _, _ = sigma_abs(speed, float(Q), xtf, kmax=2)
                ratios.append(dimless/neutral)
            print(f"{Q},{ratios[0]:.9e},{ratios[1]:.9e}")

        print("Qe,<sigma v>_midTF [m3/s]")
        for Q in (0, 1, 3, 5):
            av = fermi_average_sigma_v(speed, float(Q), X_TF_MID)
            print(f"{Q},{av:.12e}")


def main() -> None:
    print("Stage 3.72 / A25 flux-direct screened-electron Dirac prototype")
    print(f"M={M_REF:.6e} kg alpha_e={ALPHA_E:.12e} r_g={R_G:.12e} m")
    print(f"lambda_TF={LAMBDA_TF[0]:.6e}...{LAMBDA_TF[1]:.6e} m")
    print(f"vF={V_F[0]:.6e}...{V_F[1]:.6e} m/s")
    neutral_regression()
    matching_regression()
    scan()
    print("\nScope")
    print("- flux-direct absorption removes catastrophic 1-|S|^2 subtraction")
    print("- neutral low-energy regression is the primary numerical acceptance test")
    print("- positive Q enhances isolated electron capture in the static screened proxy")
    print("- Q<=5 only: beyond this, linear/static TF screening is not a controlled model")
    print("- radial/nonlinear screening, collective quasineutral current and Q(t) remain OPEN")


if __name__ == "__main__":
    main()
