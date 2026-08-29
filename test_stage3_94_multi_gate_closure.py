import math
import unittest

import numpy as np

from stage3_94_multi_gate_closure import (
    a34_concentration_profile,
    run_sweep,
    solve_a34_drift_diffusion,
    solve_f12_primordial,
    solve_h0_seismic_anomaly,
)


def _a34_profile_and_numerical_derivative(result, radii):
    """Evaluate the A34 profile and an independent central derivative."""
    step = radii * 1.0e-6

    def profile(points):
        return a34_concentration_profile(
            points,
            alpha_m=result.alpha_m,
            r_sink_m=result.r_sink_m,
            R_outer_m=result.R_outer_m,
            c_inf_m3=result.c_inf_m3,
        )

    concentration = profile(radii)
    derivative = (profile(radii + step) - profile(radii - step)) / (2.0 * step)
    return concentration, derivative


class TestStage394(unittest.TestCase):
    def test_01_f12_poisson(self):
        r = solve_f12_primordial()
        self.assertAlmostEqual(r.delta_P, 1.414213562373095e-5, places=16)

    def test_02_f12_amp_proxy(self):
        r = solve_f12_primordial()
        self.assertAlmostEqual(r.A_amp_proxy, 7.071067811865476e4, places=8)

    def test_03_f12_power_proxy(self):
        r = solve_f12_primordial()
        self.assertAlmostEqual(r.A_power_proxy, 5.0e9, delta=1e-3)

    def test_04_f12_ng_proxy(self):
        r = solve_f12_primordial()
        self.assertAlmostEqual(r.Q_NG_proxy, 4.999929289321882e9, delta=1e-3)

    def test_05_a34_alpha(self):
        r = solve_a34_drift_diffusion()
        self.assertAlmostEqual(r.alpha_m, 8.1507e-6, delta=1e-10)

    def test_06_a34_dimensionless_depth(self):
        r = solve_a34_drift_diffusion()
        self.assertAlmostEqual(r.alpha_over_r_sink, 132.96, delta=0.02)

    def test_07_a34_boundaries(self):
        r = solve_a34_drift_diffusion()
        c = a34_concentration_profile(
            np.array([r.r_sink_m, r.R_outer_m]),
            alpha_m=r.alpha_m,
            r_sink_m=r.r_sink_m,
            R_outer_m=r.R_outer_m,
            c_inf_m3=r.c_inf_m3,
        )
        self.assertAlmostEqual(c[0], 0.0, places=12)
        self.assertAlmostEqual(c[1], r.c_inf_m3, places=12)

    def test_08_a34_rate_scaling(self):
        a = solve_a34_drift_diffusion(c_inf_m3=1.0)
        b = solve_a34_drift_diffusion(c_inf_m3=10.0)
        self.assertAlmostEqual(b.particle_rate_s / a.particle_rate_s, 10.0, places=12)

    def test_09_a34_ode_residual(self):
        result = solve_a34_drift_diffusion()
        radii = np.geomspace(result.r_sink_m * 1.001, result.R_outer_m / 1.001, 400)
        concentration, derivative = _a34_profile_and_numerical_derivative(result, radii)

        drift = result.alpha_m * concentration / radii**2
        source = result.particle_rate_s / (
            4.0 * math.pi * result.D_eff * result.thermo_factor * radii**2
        )
        residual = derivative + drift - source
        scale = np.abs(derivative) + np.abs(drift) + np.abs(source) + np.finfo(float).tiny
        relative_residual = np.abs(residual) / scale

        self.assertLess(float(np.max(relative_residual)), 1.0e-6)

    def test_10_a34_flux_is_conserved(self):
        result = solve_a34_drift_diffusion()
        radii = np.geomspace(result.r_sink_m * 1.001, result.R_outer_m / 1.001, 400)
        concentration, derivative = _a34_profile_and_numerical_derivative(result, radii)

        flux_density = -result.D_eff * result.thermo_factor * (
            derivative + result.alpha_m * concentration / radii**2
        )
        particle_rate = -4.0 * math.pi * radii**2 * flux_density
        relative_spread = (np.max(particle_rate) - np.min(particle_rate)) / abs(
            np.mean(particle_rate)
        )

        self.assertLess(float(relative_spread), 1.0e-6)
        np.testing.assert_allclose(
            particle_rate,
            result.particle_rate_s,
            rtol=1.0e-6,
            atol=0.0,
        )

    def test_11_a34_inner_profile_has_no_exponential_overshoot(self):
        result = solve_a34_drift_diffusion()
        radius = 2.0 * result.r_sink_m
        concentration = float(
            a34_concentration_profile(
                radius,
                alpha_m=result.alpha_m,
                r_sink_m=result.r_sink_m,
                R_outer_m=result.R_outer_m,
                c_inf_m3=result.c_inf_m3,
            )
        )
        expected = result.c_inf_m3 * (
            -np.expm1(-result.alpha_m * (1.0 / result.r_sink_m - 1.0 / radius))
        ) / (-np.expm1(-result.exponent_span))

        self.assertAlmostEqual(concentration, float(expected), places=12)
        self.assertLessEqual(concentration, result.c_inf_m3)

    def test_12_h0_shell_density(self):
        r = solve_h0_seismic_anomaly()
        self.assertAlmostEqual(r.delta_rho_shell_kg_m3, -5.714285714285714, places=12)

    def test_13_h0_mass_compensation(self):
        r = solve_h0_seismic_anomaly()
        positive_mass_scale = 4.0 * math.pi * 100.0 * 1000.0**3
        self.assertLess(abs(r.compensated_mass_kg), positive_mass_scale * 1e-11)

    def test_14_full_50_point_sweep(self):
        s = run_sweep(50)
        self.assertEqual({k: len(v) for k, v in s.items()}, {"F12": 50, "A34": 50, "H0": 50})


if __name__ == "__main__":
    unittest.main()
