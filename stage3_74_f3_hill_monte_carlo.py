#!/usr/bin/env python3
"""Stage 3.74 / F3 — adaptive planar Hill Monte-Carlo pull-down capture gate.

Purpose
-------
Quantify, within a deliberately reduced planar Hill model, the fraction of
solar-bound/cold encounter states that become *topologically confined* after
an instantaneous embryo-mass jump.

This is NOT an absolute Solar-System delivery probability. The injection
ensemble is model-defined, the embryo orbit is circular, the test particle is
massless, only the first Hill-sphere passage is sampled, and impact momentum /
centre-of-mass shifts are omitted.

Numerics
--------
- Hill units: distance r_H, time Omega^-1, velocity Omega*r_H.
- Planar Hill equations:
    x'' - 2 y' - 3 x = -3 x/r^3
    y'' + 2 x'       = -3 y/r^3
- Adaptive scipy.integrate.solve_ivp(DOP853)
- rtol=3e-10, atol=1e-12.
- A deep-approach guard terminates at r < 0.02 r_H.
- The conservative permanent-capture tally uses only states r >= 0.1 r_H.

Permanent-capture proxy
-----------------------
The Hill Jacobi constant for mass factor m is

    C = 3 x^2 + 6 m/r - (vx^2 + vy^2)

and the L1/L2 value is

    C_L = 9 m^(2/3).

After an instantaneous fractional mass jump delta, m=1+delta. A state inside
the new Hill lobe with C_new > C_L has closed L1/L2 zero-velocity necks in the
ideal time-independent planar Hill model. That is the F3 pull-down capture
criterion.

Reference ensemble
------------------
- impact parameter |b| uniform in [0.5, 3.0] pre-impact Hill radii
- random sign of b
- upstream y = +/-8 r_H
- shear velocity vy = -1.5 b + Gaussian(dv_y)
- vx = Gaussian(dv_x)
- sigma_v = 0.0, 0.1, 0.3 in units of v_H
- N=1000 per sigma for the documented reference run
- deltas = 0.01, 0.03, 0.10, 0.30

The reported entry fraction is only an injection-grid diagnostic and must not
be interpreted as an astrophysical encounter probability.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Optional

import numpy as np
from scipy.integrate import solve_ivp

DELTAS = np.array([0.01, 0.03, 0.10, 0.30], dtype=float)
SIGMAS = (0.0, 0.1, 0.3)
SEEDS = (100, 101, 102)


def hill_rhs(_t: float, s: np.ndarray) -> np.ndarray:
    x, y, vx, vy = s
    r2 = x * x + y * y
    r = np.sqrt(r2)
    r3 = r2 * r
    return np.array([
        vx,
        vy,
        2.0 * vy + 3.0 * x - 3.0 * x / r3,
        -2.0 * vx - 3.0 * y / r3,
    ])


def jacobi(s: np.ndarray, mass_factor: float = 1.0) -> np.ndarray:
    x, y, vx, vy = s
    r = np.hypot(x, y)
    return 3.0 * x * x + 6.0 * mass_factor / r - vx * vx - vy * vy


def l1_l2_jacobi(mass_factor: float) -> float:
    return 9.0 * mass_factor ** (2.0 / 3.0)


@dataclass
class Segment:
    duration: float
    state: np.ndarray
    radius: np.ndarray
    status: str


def first_hill_segment(
    b: float,
    dvx: float,
    dvy: float,
    *,
    y_upstream: float = 8.0,
    approach_limit: float = 30.0,
    inside_limit: float = 50.0,
    sample_dt: float = 0.01,
    deep_guard: float = 0.02,
) -> Optional[Segment]:
    y0 = y_upstream if b > 0.0 else -y_upstream
    s0 = np.array([b, y0, dvx, -1.5 * b + dvy], dtype=float)

    def entry_event(_t, s):
        return np.hypot(s[0], s[1]) - 1.0

    entry_event.terminal = True
    entry_event.direction = -1

    def deep_event(_t, s):
        return np.hypot(s[0], s[1]) - deep_guard

    deep_event.terminal = True
    deep_event.direction = -1

    approach = solve_ivp(
        hill_rhs,
        (0.0, approach_limit),
        s0,
        method="DOP853",
        rtol=3e-10,
        atol=1e-12,
        max_step=0.15,
        events=(entry_event, deep_event),
    )

    if len(approach.t_events[0]) == 0:
        return None

    te = approach.t_events[0][0]
    se = approach.y_events[0][0]

    # Tiny inward nudge prevents the exit event from firing at the same root.
    se = se + hill_rhs(te, se) * 1e-8

    def exit_event(_t, s):
        return np.hypot(s[0], s[1]) - 1.0

    exit_event.terminal = True
    exit_event.direction = +1

    inside = solve_ivp(
        hill_rhs,
        (0.0, inside_limit),
        se,
        method="DOP853",
        rtol=3e-10,
        atol=1e-12,
        max_step=0.05,
        events=(exit_event, deep_event),
        dense_output=True,
    )

    tend = inside.t[-1]
    if tend <= 0.0:
        return None

    t = np.arange(0.0, tend, sample_dt)
    if t.size < 2:
        t = np.linspace(0.0, tend, 2)

    state = inside.sol(t)
    radius = np.hypot(state[0], state[1])

    if len(inside.t_events[0]) > 0:
        status = "exit"
    elif len(inside.t_events[1]) > 0:
        status = "deep"
    else:
        status = "long"

    return Segment(tend, state, radius, status)


def run_ensemble(
    n: int,
    sigma_v: float,
    seed: int,
    *,
    bmin: float = 0.5,
    bmax: float = 3.0,
    conservative_rmin: float = 0.1,
) -> dict:
    rng = np.random.default_rng(seed)
    b = rng.uniform(bmin, bmax, n) * rng.choice((-1.0, 1.0), n)
    dvx = rng.normal(0.0, sigma_v, n)
    dvy = rng.normal(0.0, sigma_v, n)

    entered = 0
    deep = 0
    long = 0
    looped = 0
    durations = []
    jacobi_ptp = []

    total_all = 0
    total_outer = 0
    captured_all = np.zeros(DELTAS.size, dtype=np.int64)
    captured_outer = np.zeros(DELTAS.size, dtype=np.int64)
    any_outer = np.zeros(DELTAS.size, dtype=np.int64)

    for bi, ux, uy in zip(b, dvx, dvy):
        segment = first_hill_segment(bi, ux, uy)
        if segment is None:
            continue

        entered += 1
        durations.append(segment.duration)
        if segment.status == "deep":
            deep += 1
        elif segment.status == "long":
            long += 1

        s = segment.state
        r = segment.radius
        theta = np.unwrap(np.arctan2(s[1], s[0]))
        if theta.size > 1 and abs(theta[-1] - theta[0]) >= 2.0 * np.pi:
            looped += 1

        c0 = jacobi(s, 1.0)
        jacobi_ptp.append(float(np.ptp(c0)))

        total_all += r.size
        outer = r >= conservative_rmin
        total_outer += int(np.count_nonzero(outer))

        for k, delta in enumerate(DELTAS):
            mf = 1.0 + delta
            cnew = jacobi(s, mf)
            closed = cnew > l1_l2_jacobi(mf)
            captured_all[k] += int(np.count_nonzero(closed))

            closed_outer = closed & outer
            captured_outer[k] += int(np.count_nonzero(closed_outer))
            if np.any(closed_outer):
                any_outer[k] += 1

    durations = np.asarray(durations, dtype=float)
    jacobi_ptp = np.asarray(jacobi_ptp, dtype=float)

    def safe_ratio(a, b):
        return np.asarray(a, dtype=float) / max(1, int(b))

    return {
        "n": n,
        "sigma_v_over_vH": sigma_v,
        "seed": seed,
        "entered": entered,
        "entry_fraction_injection_grid": entered / n,
        "deep_fraction_of_entered": deep / max(1, entered),
        "long_first_segment_fraction": long / max(1, entered),
        "one_loop_fraction_of_entered": looped / max(1, entered),
        "mean_residence_Omega_inv": float(np.mean(durations)) if durations.size else np.nan,
        "median_residence_Omega_inv": float(np.median(durations)) if durations.size else np.nan,
        "p90_residence_Omega_inv": float(np.quantile(durations, 0.9)) if durations.size else np.nan,
        "max_residence_Omega_inv": float(np.max(durations)) if durations.size else np.nan,
        "outer_sample_fraction": total_outer / max(1, total_all),
        "occupancy_capture_all": safe_ratio(captured_all, total_all),
        "occupancy_capture_r_ge_0p1_rH": safe_ratio(captured_outer, total_outer),
        "trajectory_any_capture_r_ge_0p1_rH": safe_ratio(any_outer, entered),
        "jacobi_ptp_median": float(np.median(jacobi_ptp)) if jacobi_ptp.size else np.nan,
        "jacobi_ptp_max": float(np.max(jacobi_ptp)) if jacobi_ptp.size else np.nan,
    }


def print_result(result: dict) -> None:
    print("\n---")
    print(f"sigma_v/v_H = {result['sigma_v_over_vH']:.3f}")
    print(f"N             = {result['n']}")
    print(f"entered       = {result['entered']} ({result['entry_fraction_injection_grid']:.4f})")
    print(f"deep/entered  = {result['deep_fraction_of_entered']:.4f}")
    print(f"loops/entered = {result['one_loop_fraction_of_entered']:.4f}")
    print(
        "residence [Omega^-1]: "
        f"mean={result['mean_residence_Omega_inv']:.4f}, "
        f"median={result['median_residence_Omega_inv']:.4f}, "
        f"p90={result['p90_residence_Omega_inv']:.4f}, "
        f"max={result['max_residence_Omega_inv']:.4f}"
    )
    print(
        "Jacobi ptp: "
        f"median={result['jacobi_ptp_median']:.3e}, "
        f"max={result['jacobi_ptp_max']:.3e}"
    )
    print("delta     all-Hill occupancy     r>=0.1 r_H occupancy     any outer state / entered")
    for d, a, o, q in zip(
        DELTAS,
        result["occupancy_capture_all"],
        result["occupancy_capture_r_ge_0p1_rH"],
        result["trajectory_any_capture_r_ge_0p1_rH"],
    ):
        print(f"{d:5.2f}     {a:18.8e}     {o:21.8e}     {q:21.8e}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=1000, help="samples per sigma_v ensemble")
    args = parser.parse_args()

    print("Stage 3.74 / F3 — adaptive Hill Monte-Carlo")
    print("Deltas:", DELTAS)
    print("Conservative tally: r >= 0.1 r_H")
    print("WARNING: injection-grid fractions are not astrophysical probabilities.")

    for sigma, seed in zip(SIGMAS, SEEDS):
        result = run_ensemble(args.n, sigma, seed)
        print_result(result)


if __name__ == "__main__":
    main()
