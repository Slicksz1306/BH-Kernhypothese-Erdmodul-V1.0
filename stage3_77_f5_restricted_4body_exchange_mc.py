#!/usr/bin/env python3
"""Stage 3.77 / F5 — direct restricted four-body exchange-capture Monte Carlo.

Bodies
------
Sun (fixed origin in heliocentric inertial coordinates), Proto-Earth embryo M1,
second embryo M2, and a massless seed. M1/M2 are integrated mutually; the seed
feels Sun+M1+M2. The Sun's reflex motion is neglected because embryo masses are
<< M_sun.

Purpose
-------
Test whether a solar-bound/cold seed that is already in M1's Hill-scale region
at the epoch of an embryo-embryo flyby can be converted into a stable M1-bound
orbit by collisionless exchange/scattering.

This is a CONDITIONAL encounter calculation, not an absolute Solar-System
formation probability. The seed is deliberately conditioned to be present in
M1's Hill region at embryo pericentre.

Critical correction
-------------------
A discarded pilot used V ~ Omega R_H,mut directly at closest approach. For
kappa=b/R_H,mut<1 this can be below mutual escape speed and spuriously creates
embryo-bound encounters. The final implementation instead samples hyperbolic
V_inf and sets the pericentre speed to

    V_p^2 = V_inf^2 + 2 G (M1+M2)/b

or, in mutual-Hill units,

    (V_p / (Omega R_H,mut))^2 = u_inf^2 + 6/kappa.

Each full run is paired with a counterfactual control using exactly the same
M1+seed initial state but M2 mass set to zero. A capture is attributed to the
embryo encounter only if the full run succeeds while the control does not.
"""

from __future__ import annotations

import argparse
from collections import Counter
from dataclasses import dataclass
from math import pi, sqrt
import numpy as np
from scipy.integrate import solve_ivp

M_EARTH_OVER_M_SUN = 5.9722e24 / 1.98847e30
R_EARTH_OVER_AU = 6.371e6 / 1.495978707e11


def rhs_full(_t, y, mu1, mu2):
    r1, v1 = y[0:2], y[2:4]
    r2, v2 = y[4:6], y[6:8]
    rs, vs = y[8:10], y[10:12]

    r1s = np.hypot(*r1)
    r2s = np.hypot(*r2)
    rss = np.hypot(*rs)

    d12 = r2 - r1
    r12 = np.hypot(*d12)
    d1 = rs - r1
    rd1 = np.hypot(*d1)
    d2 = rs - r2
    rd2 = np.hypot(*d2)

    a1 = -r1 / r1s**3 + mu2 * d12 / r12**3
    a2 = -r2 / r2s**3 - mu1 * d12 / r12**3
    aseed = -rs / rss**3 - mu1 * d1 / rd1**3 - mu2 * d2 / rd2**3

    out = np.empty(12)
    out[0:2] = v1
    out[2:4] = a1
    out[4:6] = v2
    out[6:8] = a2
    out[8:10] = vs
    out[10:12] = aseed
    return out


def rhs_control(_t, y, mu1):
    r1, v1 = y[0:2], y[2:4]
    rs, vs = y[4:6], y[6:8]
    r1s = np.hypot(*r1)
    rss = np.hypot(*rs)
    d = rs - r1
    rd = np.hypot(*d)
    a1 = -r1 / r1s**3
    aseed = -rs / rss**3 - mu1 * d / rd**3

    out = np.empty(8)
    out[0:2] = v1
    out[2:4] = a1
    out[4:6] = vs
    out[6:8] = aseed
    return out


def classify(r1, v1, rs, vs, mu1, mfrac):
    dr = rs - r1
    dv = vs - v1
    r = np.hypot(*dr)
    eps = 0.5 * np.dot(dv, dv) - mu1 / r
    h = dr[0] * dv[1] - dr[1] * dv[0]
    r_h = (mu1 / 3.0) ** (1.0 / 3.0)
    radius = R_EARTH_OVER_AU * mfrac ** (1.0 / 3.0)

    if r <= radius:
        return "body", eps, np.nan, r / r_h

    if eps < 0.0:
        a_seed = -mu1 / (2.0 * eps)
        alpha_stable = 0.4895 if h >= 0.0 else 0.9309
        if a_seed < alpha_stable * r_h:
            return "stable", eps, a_seed / r_h, r / r_h
        return "bound_unstable", eps, a_seed / r_h, r / r_h

    return "unbound", eps, np.nan, r / r_h


@dataclass(frozen=True)
class Params:
    mfrac: float
    q: float
    kappa: float
    u_inf: float
    f_seed: float
    beta: float
    phi: float
    theta: float
    sign: int


def sample_params(rng, mode):
    mfrac = 10.0 ** rng.uniform(-3.0, -1.0)

    if mode == "strong":
        q = 10.0 ** rng.uniform(np.log10(0.3), 0.0)
        kappa = rng.uniform(0.3, 0.8)
        u_inf = rng.uniform(0.5, 1.5)
    elif mode == "weak":
        q = 10.0 ** rng.uniform(np.log10(0.03), np.log10(0.1))
        kappa = rng.uniform(0.9, 1.5)
        u_inf = rng.uniform(1.5, 3.0)
    else:
        q = 10.0 ** rng.uniform(np.log10(0.03), 0.0)
        kappa = rng.uniform(0.3, 1.5)
        u_inf = 10.0 ** rng.uniform(np.log10(0.5), np.log10(3.0))

    return Params(
        mfrac=mfrac,
        q=q,
        kappa=kappa,
        u_inf=u_inf,
        f_seed=rng.uniform(0.1, 1.0),
        beta=rng.uniform(1.0, 1.15),
        phi=rng.uniform(0.0, 2.0 * pi),
        theta=rng.uniform(0.0, 2.0 * pi),
        sign=int(rng.choice((-1, 1))),
    )


def initial_conditions(p: Params):
    mu1 = p.mfrac * M_EARTH_OVER_M_SUN
    mu2 = p.q * mu1
    r_h_mut = ((mu1 + mu2) / 3.0) ** (1.0 / 3.0)
    r_h_1 = (mu1 / 3.0) ** (1.0 / 3.0)

    r1 = np.array([1.0, 0.0])
    v1 = np.array([0.0, 1.0])

    b = p.kappa * r_h_mut
    v_peri_hill = sqrt(p.u_inf * p.u_inf + 6.0 / p.kappa)

    r2 = r1 + np.array([b, 0.0])
    v2 = v1 + np.array([0.0, p.sign * v_peri_hill * r_h_mut])

    dr_seed = p.f_seed * r_h_1 * np.array([np.cos(p.phi), np.sin(p.phi)])
    rs = r1 + dr_seed
    v_escape = sqrt(2.0 * mu1 / (p.f_seed * r_h_1))
    dv_seed = p.beta * v_escape * np.array([np.cos(p.theta), np.sin(p.theta)])
    vs = v1 + dv_seed

    full = np.r_[r1, v1, r2, v2, rs, vs]
    control = np.r_[r1, v1, rs, vs]
    return mu1, mu2, full, control


def integrate_pair(p: Params, t_end=3.0):
    mu1, mu2, y_full0, y_ctrl0 = initial_conditions(p)
    radius = R_EARTH_OVER_AU * p.mfrac ** (1.0 / 3.0)

    def body_full(_t, y, _mu1, _mu2):
        return np.hypot(*(y[8:10] - y[0:2])) - radius

    body_full.terminal = True
    body_full.direction = -1

    full = solve_ivp(
        rhs_full,
        (0.0, t_end),
        y_full0,
        args=(mu1, mu2),
        method="DOP853",
        rtol=3e-8,
        atol=3e-10,
        max_step=0.2,
        events=body_full,
    )

    yf = full.y[:, -1]
    cf = classify(yf[0:2], yf[2:4], yf[8:10], yf[10:12], mu1, p.mfrac)
    if full.t_events[0].size:
        cf = ("body",) + cf[1:]

    def body_control(_t, y, _mu1):
        return np.hypot(*(y[4:6] - y[0:2])) - radius

    body_control.terminal = True
    body_control.direction = -1

    ctrl = solve_ivp(
        rhs_control,
        (0.0, t_end),
        y_ctrl0,
        args=(mu1,),
        method="DOP853",
        rtol=3e-8,
        atol=3e-10,
        max_step=0.2,
        events=body_control,
    )

    yc = ctrl.y[:, -1]
    cc = classify(yc[0:2], yc[2:4], yc[4:6], yc[6:8], mu1, p.mfrac)
    if ctrl.t_events[0].size:
        cc = ("body",) + cc[1:]

    return cf, cc


def integrate_full_long(p: Params, t_end=20.0):
    mu1, mu2, y0, _ = initial_conditions(p)
    radius = R_EARTH_OVER_AU * p.mfrac ** (1.0 / 3.0)

    def body_full(_t, y, _mu1, _mu2):
        return np.hypot(*(y[8:10] - y[0:2])) - radius

    body_full.terminal = True
    body_full.direction = -1

    sol = solve_ivp(
        rhs_full,
        (0.0, t_end),
        y0,
        args=(mu1, mu2),
        method="DOP853",
        rtol=3e-8,
        atol=3e-10,
        max_step=0.2,
        events=body_full,
    )

    y = sol.y[:, -1]
    out = classify(y[0:2], y[2:4], y[8:10], y[10:12], mu1, p.mfrac)
    if sol.t_events[0].size:
        out = ("body",) + out[1:]
    return out


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--n", type=int, default=300, help="samples per ensemble")
    args = parser.parse_args()

    seeds = {"strong": 2001, "broad": 2002, "weak": 2003}

    for mode in ("strong", "broad", "weak"):
        rng = np.random.default_rng(seeds[mode])
        rows = []
        candidates = []

        for _ in range(args.n):
            p = sample_params(rng, mode)
            full, ctrl = integrate_pair(p)
            rows.append((full[0], ctrl[0]))

            if full[0] in ("stable", "bound_unstable") and ctrl[0] not in ("stable", "body"):
                candidates.append((p, full, ctrl))

        print("\n", mode.upper())
        print("3 Omega^-1 paired states:", Counter(rows))

        persistent = Counter()
        for p, full, ctrl in candidates:
            outcome = integrate_full_long(p, 20.0)
            persistent[outcome[0]] += 1

        print("candidate outcomes at 20 Omega^-1:", persistent)
        print("NOTE: 20 Omega^-1 = ~3.18 yr at 1 AU.")


if __name__ == "__main__":
    main()
