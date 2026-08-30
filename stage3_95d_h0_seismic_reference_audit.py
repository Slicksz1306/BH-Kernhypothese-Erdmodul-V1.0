"""Stage 3.95D - H0 seismic reference-model audit.

This module does NOT predict a black-hole signal. It isolates one specific
systematic: how the absolute radial P-wave baseline changes when the PREM outer
core is replaced by the EPOC-Vinet outer-core model of Irving, Cottaar & Lekic
(2018), while the rest of Earth remains PREM.

Scientific scope
----------------
* PREM is used as a 1-D reference Earth model.
* EPOC-Vinet applies only to the liquid outer core (ICB..CMB).
* The EPOC paper itself notes that its planet is not globally self-consistent
  because P(CMB) and g(ICB) are fixed while regions outside the outer core are
  held to PREM.
* Therefore the PREM+EPOC construction below is a path-background sensitivity
  experiment, not a replacement whole-Earth model.
* A Stage-3.94 H0 perturbation confined to r <= 2 km is disjoint from EPOC's
  outer-core domain; its local differential travel-time proxy is unchanged by
  this outer-core-only swap. Absolute center-to-surface / center-scatter
  baselines do shift.

Sources
-------
PREM: Dziewonski & Anderson (1981); IRIS EMC DOI 10.17611/DP/10131390.
EPOC: Irving, Cottaar & Lekic (2018), DOI 10.1126/sciadv.aar2538.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
import math

from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

G = 6.67430e-11
R_EARTH_M = 6_371_000.0
R_ICB_M = 1_221_500.0
R_CMB_M = 3_480_000.0

# EPOC-Vinet median parameters, Irving et al. (2018), Table 1.
EPOC_K0S_PA = 67.5e9
EPOC_K0S_PRIME = 6.12
EPOC_RHO0_KG_M3 = 6110.0
EPOC_P_CMB_PA = 135.75e9
EPOC_G_ICB_M_S2 = 4.4002


@dataclass(frozen=True)
class EPOCProfile:
    p_icb_pa: float
    p_cmb_pa: float
    g_cmb_m_s2: float
    rho_cmb_kg_m3: float
    vp_cmb_m_s: float
    outer_core_time_s: float
    solution: object


def prem_vp_m_s(radius_m: float) -> float:
    """Radial PREM P velocity (1-s polynomial representation), in m/s."""
    r_km = float(radius_m) / 1000.0
    if not 0.0 <= r_km <= 6371.0:
        raise ValueError("radius must lie within Earth")
    x = r_km / 6371.0

    if r_km < 1221.5:
        vp = 11.2622 - 6.3640 * x**2
    elif r_km < 3480.0:
        vp = 11.0487 - 4.0362*x + 4.8023*x**2 - 13.5732*x**3
    elif r_km < 3630.0:
        vp = 15.3891 - 5.3181*x + 5.5242*x**2 - 2.5514*x**3
    elif r_km < 5600.0:
        vp = 24.9520 - 40.4673*x + 51.4832*x**2 - 26.6419*x**3
    elif r_km < 5701.0:
        vp = 29.2766 - 23.6027*x + 5.5242*x**2 - 2.5514*x**3
    elif r_km < 5771.0:
        vp = 19.0957 - 9.8672*x
    elif r_km < 5971.0:
        vp = 39.7027 - 32.6166*x
    elif r_km < 6151.0:
        vp = 20.3926 - 12.2569*x
    elif r_km < 6346.6:
        vp = 4.1875 + 3.9382*x
    elif r_km < 6356.0:
        vp = 6.8
    elif r_km < 6368.0:
        vp = 5.8
    else:
        vp = 1.45
    return vp * 1000.0


PREM_LAYER_BOUNDS_M = (
    0.0, 1_221_500.0, 3_480_000.0, 3_630_000.0, 5_600_000.0,
    5_701_000.0, 5_771_000.0, 5_971_000.0, 6_151_000.0,
    6_346_600.0, 6_356_000.0, 6_368_000.0, 6_371_000.0,
)


def _travel_time(vp, a_m: float, b_m: float) -> float:
    return float(quad(lambda r: 1.0 / vp(r), a_m, b_m,
                      epsabs=1e-11, epsrel=1e-11, limit=200)[0])


def prem_radial_time_s(a_m: float = 0.0, b_m: float = R_EARTH_M) -> float:
    """One-way radial PREM P-wave time between two radii."""
    if not 0.0 <= a_m <= b_m <= R_EARTH_M:
        raise ValueError("require 0 <= a <= b <= R_Earth")
    bounds = [a_m]
    bounds.extend(x for x in PREM_LAYER_BOUNDS_M if a_m < x < b_m)
    bounds.append(b_m)
    return sum(_travel_time(prem_vp_m_s, x0, x1)
               for x0, x1 in zip(bounds[:-1], bounds[1:]))


def _epoc_eta() -> float:
    return 1.5 * (EPOC_K0S_PRIME - 1.0)


def epoc_pressure_from_x_pa(x: float) -> float:
    """Vinet pressure, x=(V/V0)^(1/3)."""
    eta = _epoc_eta()
    return (3.0 * EPOC_K0S_PA * (1.0 - x) / x**2
            * math.exp(eta * (1.0 - x)))


def epoc_x_from_pressure(p_pa: float) -> float:
    if p_pa < 0:
        raise ValueError("pressure must be non-negative")
    return float(brentq(lambda x: epoc_pressure_from_x_pa(x) - p_pa,
                        0.2, 1.0, xtol=1e-14, rtol=1e-14))


def epoc_properties(p_pa: float) -> tuple[float, float, float]:
    """Return (rho, K_S, Vp) for the EPOC-Vinet median parameter set."""
    x = epoc_x_from_pressure(float(p_pa))
    eta = _epoc_eta()
    rho = EPOC_RHO0_KG_M3 / x**3
    k_s = (EPOC_K0S_PA / x**2
           * (2.0 + (eta - 1.0)*x - eta*x**2)
           * math.exp(eta * (1.0 - x)))
    vp = math.sqrt(k_s / rho)
    return rho, k_s, vp


def _integrate_epoc(p_icb_pa: float, dense_output: bool):
    def rhs(r, y):
        p, g = y
        rho, _, _ = epoc_properties(p)
        return (-rho * g, 4.0 * math.pi * G * rho - 2.0 * g / r)

    return solve_ivp(
        rhs,
        (R_ICB_M, R_CMB_M),
        (p_icb_pa, EPOC_G_ICB_M_S2),
        rtol=1e-10,
        atol=(1e-2, 1e-10),
        max_step=2000.0,
        dense_output=dense_output,
    )


@lru_cache(maxsize=1)
def solve_epoc_profile() -> EPOCProfile:
    """Reconstruct EPOC-Vinet by shooting on P(ICB) to fixed P(CMB)."""
    def residual(p_icb):
        sol = _integrate_epoc(p_icb, False)
        if not sol.success:
            raise RuntimeError(sol.message)
        return float(sol.y[0, -1] - EPOC_P_CMB_PA)

    p_icb = float(brentq(residual, 300e9, 370e9, xtol=1e-3, rtol=1e-12))
    sol = _integrate_epoc(p_icb, True)
    if not sol.success:
        raise RuntimeError(sol.message)
    p_cmb = float(sol.y[0, -1])
    g_cmb = float(sol.y[1, -1])
    rho_cmb, _, vp_cmb = epoc_properties(p_cmb)

    def vp_epoc(r):
        p = float(sol.sol(r)[0])
        return epoc_properties(p)[2]

    t_outer = _travel_time(vp_epoc, R_ICB_M, R_CMB_M)
    return EPOCProfile(
        p_icb_pa=p_icb,
        p_cmb_pa=p_cmb,
        g_cmb_m_s2=g_cmb,
        rho_cmb_kg_m3=rho_cmb,
        vp_cmb_m_s=vp_cmb,
        outer_core_time_s=t_outer,
        solution=sol,
    )


def hybrid_prem_epoc_center_surface_time_s() -> float:
    """PREM whole path with only the outer-core segment replaced by EPOC."""
    prem_total = prem_radial_time_s()
    prem_outer = prem_radial_time_s(R_ICB_M, R_CMB_M)
    return prem_total - prem_outer + solve_epoc_profile().outer_core_time_s


def absolute_center_scatter_baseline_shift_s() -> float:
    """Two-leg radial path shift caused by the outer-core reference swap."""
    return 2.0 * (hybrid_prem_epoc_center_surface_time_s()
                  - prem_radial_time_s())


def outer_core_swap_overlaps_local_h0(perturbation_outer_radius_m: float) -> bool:
    """Whether a central H0 perturbation extends into EPOC's outer-core domain."""
    if perturbation_outer_radius_m < 0:
        raise ValueError("radius must be non-negative")
    return perturbation_outer_radius_m > R_ICB_M


def audit_summary() -> dict[str, float | str | bool]:
    epoc = solve_epoc_profile()
    prem_total = prem_radial_time_s()
    prem_outer = prem_radial_time_s(R_ICB_M, R_CMB_M)
    hybrid = hybrid_prem_epoc_center_surface_time_s()
    return {
        "prem_center_surface_s": prem_total,
        "prem_outer_core_s": prem_outer,
        "epoc_outer_core_s": epoc.outer_core_time_s,
        "hybrid_center_surface_s": hybrid,
        "one_way_shift_s": hybrid - prem_total,
        "two_way_center_scatter_shift_s": 2.0*(hybrid-prem_total),
        "epoc_p_icb_gpa": epoc.p_icb_pa/1e9,
        "epoc_vp_cmb_km_s": epoc.vp_cmb_m_s/1000.0,
        "epoc_rho_cmb_kg_m3": epoc.rho_cmb_kg_m3,
        "stage394_2km_overlap": outer_core_swap_overlaps_local_h0(2000.0),
        "interpretation": "PATH_BACKGROUND_SENSITIVITY_ONLY",
        "experimental_bh_evidence": "NONE",
    }


if __name__ == "__main__":
    for key, value in audit_summary().items():
        print(f"{key}: {value}")
