"""
Stage 3.94 Multi-Gate Closure Solver

Three analytical/reduced gates:
1. F12: primordial-origin Poisson amplification proxies.
2. A34: stationary spherical Nernst-Planck/Bondi drift-diffusion sink.
3. H0: compensated PREM-scale density perturbation and seismic travel-time proxy.

Important scientific scope:
- F12 outputs are explicitly proxies, not a physical P_zeta peak or measured f_NL.
- A34 returns a transport rate for a chosen reference concentration; it is not the
  final multicomponent electrical equilibrium charge Q_eq.
- H0 is a compensated structural proxy; a unique PREM prediction remains OPEN.
"""

from __future__ import annotations

from dataclasses import dataclass, asdict
from typing import Dict, List

import numpy as np
from scipy import constants as const
from scipy.integrate import quad


@dataclass(frozen=True)
class F12Result:
    N_seed: float
    z_vir: float
    delta_target: float
    delta_P: float
    A_amp_proxy: float
    A_power_proxy: float
    Q_NG_proxy: float


@dataclass(frozen=True)
class A34Result:
    D_eff: float
    T_core: float
    M_seed_kg: float
    r_sink_m: float
    R_outer_m: float
    c_inf_m3: float
    particle_mass_u: float
    thermo_factor: float
    alpha_m: float
    alpha_over_r_sink: float
    exponent_span: float
    particle_rate_s: float


@dataclass(frozen=True)
class H0Result:
    r_core_m: float
    r_outer_m: float
    delta_rho_0_kg_m3: float
    delta_rho_shell_kg_m3: float
    compensated_mass_kg: float
    V_P0_m_s: float
    rho_0_kg_m3: float
    delta_t_center_ray_s: float


def solve_f12_primordial(
    N_seed: float = 5.0e9,
    z_vir: float = 3500.0,
    delta_target: float = 1.0,
) -> F12Result:
    """Return the corrected Stage-3.94 F12 proxy quantities.

    For a Poisson seed count N, delta_P = N^(-1/2). The amplification quantities
    are bookkeeping proxies only; no mapping to P_zeta(k) or f_NL is claimed.
    """
    if N_seed <= 0:
        raise ValueError("N_seed must be > 0")
    if delta_target <= 0:
        raise ValueError("delta_target must be > 0")

    delta_P = N_seed ** -0.5
    A_amp_proxy = delta_target / delta_P
    A_power_proxy = A_amp_proxy**2
    Q_NG_proxy = A_power_proxy - A_amp_proxy

    return F12Result(
        N_seed=N_seed,
        z_vir=z_vir,
        delta_target=delta_target,
        delta_P=delta_P,
        A_amp_proxy=A_amp_proxy,
        A_power_proxy=A_power_proxy,
        Q_NG_proxy=Q_NG_proxy,
    )


def a34_concentration_profile(
    r_m: np.ndarray | float,
    *,
    alpha_m: float,
    r_sink_m: float,
    R_outer_m: float,
    c_inf_m3: float,
) -> np.ndarray:
    """Exact stationary concentration profile for the reduced spherical sink.

    Boundary conditions: c(r_sink)=0, c(R_outer)=c_inf.
    """
    r = np.asarray(r_m, dtype=float)
    if np.any(r < r_sink_m) or np.any(r > R_outer_m):
        raise ValueError("r must satisfy r_sink <= r <= R_outer")

    span = alpha_m * (1.0 / r_sink_m - 1.0 / R_outer_m)
    denom = -np.expm1(-span)
    local = alpha_m * (1.0 / r_sink_m - 1.0 / r)

    return (
        c_inf_m3
        * np.exp(alpha_m * (1.0 / r - 1.0 / R_outer_m))
        * (-np.expm1(-local))
        / denom
    )


def solve_a34_drift_diffusion(
    D_eff: float = 3.0e-9,
    T_core: float = 5500.0,
    M_seed_kg: float = 1.0e11,
    r_sink_m: float = 6.13e-8,
    R_outer_m: float = 1.0e5,
    c_inf_m3: float = 1.0,
    particle_mass_u: float = 55.845,
    thermo_factor: float = 1.0,
) -> A34Result:
    """Solve the corrected stationary spherical drift-diffusion gate.

    Flux density:
        J_r = -D * Phi * [dc/dr + alpha/r^2 * c]

    with
        alpha = G M m / (k_B T).

    The inward particle rate is
        dotN = 4*pi*D*Phi*alpha*c_inf /
               (1 - exp[-alpha(1/r_sink - 1/R_outer)]).

    c_inf=1 m^-3 therefore means the returned rate is per chosen reference
    particle density, not a final physical accretion rate.
    """
    if min(D_eff, T_core, M_seed_kg, r_sink_m, R_outer_m, c_inf_m3, thermo_factor) <= 0:
        raise ValueError("all physical inputs must be > 0")
    if R_outer_m <= r_sink_m:
        raise ValueError("R_outer_m must exceed r_sink_m")

    m_particle = particle_mass_u * const.atomic_mass
    alpha = const.G * M_seed_kg * m_particle / (const.k * T_core)
    span = alpha * (1.0 / r_sink_m - 1.0 / R_outer_m)
    denom = -np.expm1(-span)
    particle_rate = 4.0 * np.pi * D_eff * thermo_factor * alpha * c_inf_m3 / denom

    return A34Result(
        D_eff=D_eff,
        T_core=T_core,
        M_seed_kg=M_seed_kg,
        r_sink_m=r_sink_m,
        R_outer_m=R_outer_m,
        c_inf_m3=c_inf_m3,
        particle_mass_u=particle_mass_u,
        thermo_factor=thermo_factor,
        alpha_m=alpha,
        alpha_over_r_sink=alpha / r_sink_m,
        exponent_span=span,
        particle_rate_s=particle_rate,
    )


def h0_shell_density(
    r_core_m: float,
    r_outer_m: float,
    delta_rho_0_kg_m3: float,
) -> float:
    """Constant outer-shell density required for exact mass compensation.

    Inner profile:
        delta_rho = delta_rho_0 * [1 - (r/r_core)^2], 0 <= r <= r_core.
    """
    if not (0 < r_core_m < r_outer_m):
        raise ValueError("require 0 < r_core_m < r_outer_m")

    m_inner = 4.0 * np.pi * delta_rho_0_kg_m3 * r_core_m**3 * (2.0 / 15.0)
    shell_volume = 4.0 * np.pi / 3.0 * (r_outer_m**3 - r_core_m**3)
    return -m_inner / shell_volume


def h0_density_perturbation(
    r_m: np.ndarray | float,
    *,
    r_core_m: float,
    r_outer_m: float,
    delta_rho_0_kg_m3: float,
) -> np.ndarray:
    r = np.asarray(r_m, dtype=float)
    shell = h0_shell_density(r_core_m, r_outer_m, delta_rho_0_kg_m3)

    out = np.zeros_like(r)
    core = r <= r_core_m
    shell_mask = (r > r_core_m) & (r <= r_outer_m)

    out[core] = delta_rho_0_kg_m3 * (1.0 - (r[core] / r_core_m) ** 2)
    out[shell_mask] = shell
    return out


def solve_h0_seismic_anomaly(
    r_core_m: float = 1000.0,
    r_outer_m: float = 2000.0,
    delta_rho_0_kg_m3: float = 100.0,
    V_P0_m_s: float = 11030.0,
    rho_0_kg_m3: float = 13088.48,
) -> H0Result:
    """Compensated H0 density/seismic proxy.

    For the travel-time proxy the bulk modulus is held fixed locally, giving
        Vp(r) = Vp0 * sqrt(rho0 / [rho0 + delta_rho(r)]).

    This is intentionally a reduced sensitivity model, not a unique PREM
    prediction for deltaVp/deltaVs.
    """
    shell = h0_shell_density(r_core_m, r_outer_m, delta_rho_0_kg_m3)

    def drho_scalar(r: float) -> float:
        return float(
            h0_density_perturbation(
                np.array([r]),
                r_core_m=r_core_m,
                r_outer_m=r_outer_m,
                delta_rho_0_kg_m3=delta_rho_0_kg_m3,
            )[0]
        )

    m_inner = 4.0 * np.pi * delta_rho_0_kg_m3 * r_core_m**3 * (2.0 / 15.0)
    shell_volume = 4.0 * np.pi / 3.0 * (r_outer_m**3 - r_core_m**3)
    compensated_mass = m_inner + shell * shell_volume

    def vp(r: float) -> float:
        rho = rho_0_kg_m3 + drho_scalar(r)
        if rho <= 0:
            raise ValueError("perturbed density became non-positive")
        return V_P0_m_s * np.sqrt(rho_0_kg_m3 / rho)

    delta_t = 2.0 * quad(
        lambda rr: 1.0 / vp(rr) - 1.0 / V_P0_m_s,
        0.0,
        r_outer_m,
        points=[r_core_m],
        epsabs=1.0e-14,
    )[0]

    return H0Result(
        r_core_m=r_core_m,
        r_outer_m=r_outer_m,
        delta_rho_0_kg_m3=delta_rho_0_kg_m3,
        delta_rho_shell_kg_m3=shell,
        compensated_mass_kg=compensated_mass,
        V_P0_m_s=V_P0_m_s,
        rho_0_kg_m3=rho_0_kg_m3,
        delta_t_center_ray_s=delta_t,
    )


def run_sweep(n: int = 50) -> Dict[str, List[dict]]:
    """Run the corrected 50-point Stage-3.94 smoke sweep for all three gates."""
    if n < 2:
        raise ValueError("n must be >= 2")

    f12 = [
        asdict(solve_f12_primordial(N_seed=float(x)))
        for x in np.geomspace(1.0e8, 1.0e11, n)
    ]
    a34 = [
        asdict(solve_a34_drift_diffusion(M_seed_kg=float(x)))
        for x in np.geomspace(1.0e10, 5.0e11, n)
    ]
    h0 = [
        asdict(solve_h0_seismic_anomaly(delta_rho_0_kg_m3=float(x)))
        for x in np.linspace(1.0, 500.0, n)
    ]
    return {"F12": f12, "A34": a34, "H0": h0}


def main() -> None:
    f12 = solve_f12_primordial()
    a34 = solve_a34_drift_diffusion()
    h0 = solve_h0_seismic_anomaly()
    sweep = run_sweep(50)

    print("=== Stage 3.94 Multi-Gate Solver ===")
    print("F12:", asdict(f12))
    print("A34:", asdict(a34))
    print("H0 :", asdict(h0))
    print("Sweep lengths:", {k: len(v) for k, v in sweep.items()})


if __name__ == "__main__":
    main()
