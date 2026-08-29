import unittest

import numpy as np

from stage3_95a_a35_diagnostic_charge_theorem import (
    audit_stationary_moments,
    build_default_model,
    build_discrete_generator,
    capture_factor,
    capture_factor_derivative,
    find_continuous_equilibrium,
    kramers_moyal_ou_approximation,
    neutral_root_diffusion_ratio,
    quasineutral_critical_diffusion_ratio,
    scan_continuous_equilibria,
    stationary_charge_distribution,
)


def _balanced_integer_model():
    seed = build_default_model(ion_charge_number=3.0)
    ratio = neutral_root_diffusion_ratio(seed)
    return build_default_model(
        electron_to_ion_diffusion=ratio,
        ion_charge_number=3.0,
    )


class TestStage395ADiagnosticChargeTheorem(unittest.TestCase):
    def test_01_capture_factor_zero_limit_and_extremes(self):
        points = np.array([-1.0e-12, 0.0, 1.0e-12])
        expected = 1.0 + points / 2.0 + points**2 / 12.0
        np.testing.assert_allclose(capture_factor(points), expected, rtol=0.0, atol=1.0e-15)
        self.assertEqual(capture_factor(0.0), 1.0)

        self.assertEqual(capture_factor(-1000.0), 0.0)
        self.assertAlmostEqual(capture_factor(1000.0), 1000.0, places=12)

    def test_02_analytic_capture_factor_derivative_is_positive(self):
        points = np.concatenate(
            (
                np.linspace(-100.0, -1.0e-3, 800),
                np.array([-1.0e-12, 0.0, 1.0e-12]),
                np.linspace(1.0e-3, 100.0, 800),
            )
        )
        derivative = capture_factor_derivative(points)
        self.assertTrue(np.all(np.isfinite(derivative)))
        self.assertTrue(np.all(derivative > 0.0))
        self.assertEqual(capture_factor_derivative(0.0), 0.5)

    def test_03_analytic_derivative_matches_independent_finite_difference(self):
        points = np.array([-20.0, -3.0, -0.5, 0.0, 0.5, 3.0, 20.0])
        step = 1.0e-6
        numerical = (capture_factor(points + step) - capture_factor(points - step)) / (2.0 * step)
        np.testing.assert_allclose(
            capture_factor_derivative(points),
            numerical,
            rtol=2.0e-7,
            atol=2.0e-10,
        )

    def test_04_default_dimensionless_depths_and_charge_response(self):
        model = build_default_model()
        self.assertAlmostEqual(
            model.dimensionless_depth(model.electron, 0.0),
            1.3061356193850623e-3,
            delta=1.0e-10,
        )
        self.assertAlmostEqual(
            model.dimensionless_depth(model.ion, 0.0),
            132.96357096242093,
            delta=1.0e-5,
        )
        self.assertAlmostEqual(
            model.depth_change_per_elementary_charge(model.electron),
            4.956279008896626e-2,
            delta=1.0e-9,
        )
        self.assertAlmostEqual(
            model.depth_change_per_elementary_charge(model.ion),
            -1.3679330064554682e-1,
            delta=1.0e-8,
        )

    def test_05_gravity_cancellation_and_matching_radius_are_diagnostics(self):
        model = build_default_model()
        ion_cancellation_N = -model.dimensionless_depth(
            model.ion, 0.0
        ) / model.depth_change_per_elementary_charge(model.ion)
        electron_cancellation_N = -model.dimensionless_depth(
            model.electron, 0.0
        ) / model.depth_change_per_elementary_charge(model.electron)

        self.assertAlmostEqual(ion_cancellation_N, 972.003528937069, delta=1.0e-4)
        self.assertAlmostEqual(electron_cancellation_N, -0.026353149551115285, delta=1.0e-8)
        self.assertAlmostEqual(model.schwarzschild_radius_m, 1.4852320538237332e-16, delta=1.0e-20)
        self.assertAlmostEqual(model.matching_to_horizon_ratio, 4.1273011743978333e8, delta=1.0e4)

    def test_06_charge_drift_is_strictly_decreasing_in_toy_model(self):
        for diffusion_ratio in (1.0, 100.0, 1000.0):
            for charge_number in (1.0, 2.76, 26.0):
                for temperature_ratio in (0.5, 1.0, 2.0):
                    model = build_default_model(
                        electron_to_ion_diffusion=diffusion_ratio,
                        ion_charge_number=charge_number,
                        electron_to_ion_temperature=temperature_ratio,
                    )
                    for charge_state in (-1000.0, -10.0, 0.0, 10.0, 1000.0):
                        self.assertLess(
                            model.charge_drift_derivative_s(charge_state),
                            0.0,
                        )

    def test_07_continuous_root_regression_exposes_transport_sensitivity(self):
        expected = {
            1.0: 713.4849432757337,
            10.0: 210.21971115036726,
            100.0: 11.539434741082902,
            1000.0: -63.46095178623406,
            2335.3: -85.58752540895279,
        }
        for diffusion_ratio, expected_root in expected.items():
            model = build_default_model(electron_to_ion_diffusion=diffusion_ratio)
            equilibrium = find_continuous_equilibrium(model)
            self.assertAlmostEqual(equilibrium.charge_state_N, expected_root, delta=1.0e-6)
            self.assertLess(equilibrium.drift_slope_s, 0.0)
            self.assertGreater(equilibrium.relaxation_time_s, 0.0)

    def test_08_neutral_root_requires_a_specific_toy_diffusion_ratio(self):
        seed = build_default_model()
        ratio = neutral_root_diffusion_ratio(seed)
        self.assertAlmostEqual(ratio, 132.87677452778138, delta=1.0e-6)

        balanced = build_default_model(electron_to_ion_diffusion=ratio)
        equilibrium = find_continuous_equilibrium(balanced)
        self.assertAlmostEqual(equilibrium.charge_state_N, 0.0, delta=1.0e-11)

    def test_09_three_axis_scan_finds_only_stable_toy_roots(self):
        scan = scan_continuous_equilibria(
            electron_to_ion_diffusions=(1.0, 100.0, 1000.0),
            ion_charge_numbers=(1.0, 2.76, 26.0),
            electron_to_ion_temperatures=(0.5, 1.0, 2.0),
        )
        self.assertEqual(len(scan), 27)
        self.assertTrue(all(np.isfinite(point.equilibrium_N) for point in scan))
        self.assertTrue(all(point.drift_slope_s < 0.0 for point in scan))

    def test_10_discrete_generator_has_expected_jumps_and_conserves_probability(self):
        model = build_default_model(ion_charge_number=2.0)
        states, generator = build_discrete_generator(
            model,
            minimum_N=-3,
            maximum_N=4,
            ion_charge_state=2,
        )
        state_to_index = {int(state): index for index, state in enumerate(states)}
        row = state_to_index[0]

        self.assertGreater(generator[row, state_to_index[-1]], 0.0)
        self.assertGreater(generator[row, state_to_index[2]], 0.0)
        nonzero_destinations = set(np.flatnonzero(generator[row] > 0.0))
        self.assertEqual(
            nonzero_destinations,
            {state_to_index[-1], state_to_index[2]},
        )
        off_diagonal = generator.copy()
        np.fill_diagonal(off_diagonal, 0.0)
        self.assertTrue(np.all(off_diagonal >= 0.0))
        self.assertTrue(np.all(np.diag(generator) <= 0.0))

        ion_destination = state_to_index[2]
        self.assertGreater(generator[row, ion_destination], 0.0)
        self.assertEqual(generator[ion_destination, row], 0.0)

        scale = np.max(np.abs(generator))
        np.testing.assert_allclose(
            np.sum(generator, axis=1) / scale,
            0.0,
            rtol=0.0,
            atol=2.0e-16,
        )

    def test_11_stationary_discrete_charge_distribution_closes_master_equation(self):
        model = _balanced_integer_model()
        result = stationary_charge_distribution(
            model,
            minimum_N=-100,
            maximum_N=100,
            ion_charge_state=3,
        )
        states, generator = build_discrete_generator(
            model,
            minimum_N=-100,
            maximum_N=100,
            ion_charge_state=3,
        )
        independent_residual = np.max(np.abs(generator.T @ result.probabilities)) / np.max(
            -np.diag(generator)
        )

        self.assertAlmostEqual(float(np.sum(result.probabilities)), 1.0, places=14)
        np.testing.assert_array_equal(result.states_N, states)
        self.assertTrue(np.all(result.probabilities >= 0.0))
        self.assertLess(result.stationarity_residual_relative, 1.0e-13)
        self.assertLess(float(independent_residual), 1.0e-13)
        self.assertLess(result.lower_edge_probability + result.upper_edge_probability, 1.0e-12)
        self.assertAlmostEqual(result.mean_N, -0.609144506, delta=1.0e-8)
        self.assertEqual(result.mode_N, -1)
        self.assertGreater(result.variance_N, 0.0)

    def test_12_discrete_charge_requires_integer_consistent_ion_state(self):
        model = build_default_model(ion_charge_number=2.76)
        with self.assertRaises(ValueError):
            build_discrete_generator(
                model,
                minimum_N=-10,
                maximum_N=10,
                ion_charge_state=3,
            )

        with self.assertRaises(ValueError):
            scan_continuous_equilibria(
                electron_to_ion_diffusions=(),
                ion_charge_numbers=(2.76,),
                electron_to_ion_temperatures=(1.0,),
            )

    def test_13_analytic_critical_diffusion_ratio_matches_rate_balance(self):
        model = build_default_model()
        ion_depth = model.dimensionless_depth(model.ion, 0.0)
        electron_depth = model.dimensionless_depth(model.electron, 0.0)
        direct_factor_ratio = capture_factor(ion_depth) / capture_factor(electron_depth)
        analytic_ratio = quasineutral_critical_diffusion_ratio(model)
        rate_balance_ratio = neutral_root_diffusion_ratio(model)

        self.assertAlmostEqual(analytic_ratio, direct_factor_ratio, delta=1.0e-12)
        self.assertAlmostEqual(analytic_ratio, rate_balance_ratio, delta=1.0e-12)
        self.assertAlmostEqual(analytic_ratio, 132.87677452778138, delta=1.0e-6)

        balanced = build_default_model(electron_to_ion_diffusion=analytic_ratio)
        self.assertAlmostEqual(
            find_continuous_equilibrium(balanced).charge_state_N,
            0.0,
            delta=1.0e-11,
        )

    def test_14_stationary_first_and_second_jump_moments_close(self):
        model = _balanced_integer_model()
        result = stationary_charge_distribution(
            model,
            minimum_N=-100,
            maximum_N=100,
            ion_charge_state=3,
        )
        audit = audit_stationary_moments(
            model,
            result,
            ion_charge_state=3,
        )

        self.assertLess(audit.first_moment_residual_relative, 1.0e-12)
        self.assertLess(audit.second_moment_residual_relative, 1.0e-12)
        self.assertGreater(np.sqrt(result.variance_N), 8.0)

    def test_15_discrete_distribution_converges_with_state_truncation(self):
        model = _balanced_integer_model()
        results = [
            stationary_charge_distribution(
                model,
                minimum_N=-bound,
                maximum_N=bound,
                ion_charge_state=3,
            )
            for bound in (100, 150, 200)
        ]

        reference = results[-1]
        for result in results:
            self.assertAlmostEqual(result.mean_N, reference.mean_N, delta=1.0e-7)
            self.assertAlmostEqual(result.variance_N, reference.variance_N, delta=1.0e-6)
            self.assertEqual(result.mode_N, reference.mode_N)
            self.assertLess(
                result.lower_edge_probability + result.upper_edge_probability,
                1.0e-12,
            )

    def test_16_kramers_moyal_variance_crosschecks_discrete_solution(self):
        model = _balanced_integer_model()
        discrete = stationary_charge_distribution(
            model,
            minimum_N=-100,
            maximum_N=100,
            ion_charge_state=3,
        )
        approximation = kramers_moyal_ou_approximation(
            model,
            ion_charge_state=3,
        )
        relative_difference = abs(approximation.variance_N / discrete.variance_N - 1.0)

        self.assertAlmostEqual(approximation.equilibrium_N, 0.0, delta=1.0e-11)
        self.assertGreater(approximation.restoring_rate_s, 0.0)
        self.assertGreater(approximation.jump_variance_rate_s, 0.0)
        self.assertLess(relative_difference, 1.0e-2)


if __name__ == "__main__":
    unittest.main()
