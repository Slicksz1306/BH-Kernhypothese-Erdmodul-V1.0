"""Stage 3.95A / A35 diagnostic charge theorem.

This module deliberately closes only an ideal, diagonal two-species reference
model.  It proves and tests the monotonic charge feedback of the unscreened
stationary A34 drift-diffusion formula and adds a finite-state stochastic
charge diagnostic.

Scientific scope
----------------
* The continuous and discrete results are Toy-A35 diagnostics.
* ``r_match_m`` is an effective absorbing/matching boundary inherited from
  A34.  It is not identified with the event horizon.
* The bare Coulomb term is used only to define a controlled mathematical
  reference.  It is not a WDM screening or ambipolar-transport closure.
* A physical equilibrium charge still requires separate ionic mass transport,
  electronic charge transport, nonlinear screening and sink-capture kernels.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import numpy as np
from scipy import constants as const
from scipy.optimize import brentq


COULOMB_CONSTANT = 1.0 / (4.0 * np.pi * const.epsilon_0)
ELEMENTARY_CHARGE = const.elementary_charge


def _return_scalar_if_scalar(value: np.ndarray, original: np.ndarray) -> np.ndarray | float:
    if original.ndim == 0:
        return float(value.reshape(()))
    return value


def capture_factor(x: np.ndarray | float) -> np.ndarray | float:
    """Return ``x / (1 - exp(-x))`` without cancellation at ``x=0``.

    ``x`` is the dimensionless drift depth ``alpha * Delta``.  The series is
    used around zero, while a rearranged expression avoids overflow for strong
    repulsion (large negative ``x``).
    """
    original = np.asarray(x, dtype=float)
    if np.any(~np.isfinite(original)):
        raise ValueError("x must be finite")

    flat = original.reshape(-1)
    out = np.empty_like(flat)
    small = np.abs(flat) <= 1.0e-3
    strong_repulsion = (~small) & (flat < -50.0)
    regular = ~(small | strong_repulsion)

    xs = flat[small]
    out[small] = 1.0 + xs / 2.0 + xs**2 / 12.0 - xs**4 / 720.0 + xs**6 / 30240.0

    xr = flat[strong_repulsion]
    exp_x = np.exp(xr)
    out[strong_repulsion] = (-xr) * exp_x / (-np.expm1(xr))

    xg = flat[regular]
    out[regular] = xg / (-np.expm1(-xg))

    reshaped = out.reshape(original.shape)
    return _return_scalar_if_scalar(reshaped, original)


def capture_factor_derivative(x: np.ndarray | float) -> np.ndarray | float:
    """Return the stable analytic derivative of :func:`capture_factor`.

    Analytically this derivative is strictly positive for every finite real
    ``x``.  Extremely negative values can underflow to zero in binary64, which
    represents an exponentially suppressed rate rather than a sign reversal.
    """
    original = np.asarray(x, dtype=float)
    if np.any(~np.isfinite(original)):
        raise ValueError("x must be finite")

    flat = original.reshape(-1)
    out = np.empty_like(flat)
    small = np.abs(flat) <= 1.0e-3
    strong_repulsion = (~small) & (flat < -50.0)
    regular = ~(small | strong_repulsion)

    xs = flat[small]
    out[small] = 0.5 + xs / 6.0 - xs**3 / 180.0 + xs**5 / 5040.0

    xr = flat[strong_repulsion]
    exp_x = np.exp(xr)
    out[strong_repulsion] = (
        exp_x * (exp_x - (1.0 + xr)) / (1.0 - exp_x) ** 2
    )

    xg = flat[regular]
    exp_minus_x = np.exp(-xg)
    denominator = -np.expm1(-xg)
    out[regular] = (
        1.0 - (1.0 + xg) * exp_minus_x
    ) / denominator**2

    reshaped = out.reshape(original.shape)
    return _return_scalar_if_scalar(reshaped, original)


@dataclass(frozen=True)
class ToySpecies:
    """One ideal species in the diagonal Stage-3.95A reference model."""

    name: str
    charge_number: float
    mass_kg: float
    temperature_K: float
    diffusion_m2_s: float
    outer_density_m3: float
    transport_factor: float = 1.0

    def __post_init__(self) -> None:
        numeric = (
            self.charge_number,
            self.mass_kg,
            self.temperature_K,
            self.diffusion_m2_s,
            self.outer_density_m3,
            self.transport_factor,
        )
        if not self.name:
            raise ValueError("species name must not be empty")
        if not all(np.isfinite(value) for value in numeric):
            raise ValueError("species inputs must be finite")
        if self.charge_number == 0.0:
            raise ValueError("charge_number must be non-zero")
        if min(numeric[1:]) <= 0.0:
            raise ValueError("species mass, temperature, transport and density must be > 0")


@dataclass(frozen=True)
class ContinuousEquilibrium:
    charge_state_N: float
    charge_C: float
    drift_slope_s: float
    relaxation_time_s: float
    bracket_N: tuple[float, float]


@dataclass(frozen=True)
class ScanPoint:
    electron_to_ion_diffusion: float
    ion_charge_number: float
    electron_to_ion_temperature: float
    equilibrium_N: float
    drift_slope_s: float


@dataclass(frozen=True)
class DiscreteChargeResult:
    states_N: np.ndarray
    probabilities: np.ndarray
    mean_N: float
    variance_N: float
    mode_N: int
    stationarity_residual_relative: float
    lower_edge_probability: float
    upper_edge_probability: float
    generator_scale_s: float


@dataclass(frozen=True)
class DiscreteMomentAudit:
    first_moment_residual_s: float
    first_moment_residual_relative: float
    second_moment_residual_s: float
    second_moment_residual_relative: float


@dataclass(frozen=True)
class KramersMoyalApproximation:
    equilibrium_N: float
    restoring_rate_s: float
    jump_variance_rate_s: float
    variance_N: float


@dataclass(frozen=True)
class ToyChargeModel:
    """Unscreened diagonal electron/ion charge-feedback diagnostic."""

    central_mass_kg: float
    r_match_m: float
    outer_radius_m: float
    electron: ToySpecies
    ion: ToySpecies

    def __post_init__(self) -> None:
        geometry = (self.central_mass_kg, self.r_match_m, self.outer_radius_m)
        if not all(np.isfinite(value) for value in geometry):
            raise ValueError("geometry inputs must be finite")
        if min(geometry) <= 0.0:
            raise ValueError("mass and radii must be > 0")
        if self.outer_radius_m <= self.r_match_m:
            raise ValueError("outer_radius_m must exceed r_match_m")
        if self.electron.charge_number >= 0.0:
            raise ValueError("electron species must have negative charge")
        if self.ion.charge_number <= 0.0:
            raise ValueError("ion species must have positive charge")

    @property
    def inverse_radius_span_m_inv(self) -> float:
        return 1.0 / self.r_match_m - 1.0 / self.outer_radius_m

    @property
    def schwarzschild_radius_m(self) -> float:
        return 2.0 * const.G * self.central_mass_kg / const.c**2

    @property
    def matching_to_horizon_ratio(self) -> float:
        return self.r_match_m / self.schwarzschild_radius_m

    def alpha_m(self, species: ToySpecies, charge_state_N: float) -> float:
        """Return the gravity-minus-Coulomb drift length ``alpha_s(N)``."""
        if not np.isfinite(charge_state_N):
            raise ValueError("charge_state_N must be finite")
        gravitational = const.G * self.central_mass_kg * species.mass_kg
        electrostatic = (
            COULOMB_CONSTANT
            * species.charge_number
            * ELEMENTARY_CHARGE**2
            * charge_state_N
        )
        return (gravitational - electrostatic) / (const.k * species.temperature_K)

    def dimensionless_depth(self, species: ToySpecies, charge_state_N: float) -> float:
        return self.alpha_m(species, charge_state_N) * self.inverse_radius_span_m_inv

    def depth_change_per_elementary_charge(self, species: ToySpecies) -> float:
        return (
            -COULOMB_CONSTANT
            * species.charge_number
            * ELEMENTARY_CHARGE**2
            * self.inverse_radius_span_m_inv
            / (const.k * species.temperature_K)
        )

    def particle_rate_s(self, species: ToySpecies, charge_state_N: float) -> float:
        base_rate = (
            4.0
            * np.pi
            * species.diffusion_m2_s
            * species.transport_factor
            * species.outer_density_m3
            / self.inverse_radius_span_m_inv
        )
        x = self.dimensionless_depth(species, charge_state_N)
        return base_rate * float(capture_factor(x))

    def particle_rate_derivative_s(self, species: ToySpecies, charge_state_N: float) -> float:
        base_rate = (
            4.0
            * np.pi
            * species.diffusion_m2_s
            * species.transport_factor
            * species.outer_density_m3
            / self.inverse_radius_span_m_inv
        )
        x = self.dimensionless_depth(species, charge_state_N)
        return (
            base_rate
            * float(capture_factor_derivative(x))
            * self.depth_change_per_elementary_charge(species)
        )

    def charge_drift_e_s(self, charge_state_N: float) -> float:
        """Return ``dN/dt`` in elementary charges per second."""
        return sum(
            species.charge_number * self.particle_rate_s(species, charge_state_N)
            for species in (self.ion, self.electron)
        )

    def charge_drift_derivative_s(self, charge_state_N: float) -> float:
        """Return ``d(dN/dt)/dN``, equal to ``d(dQ/dt)/dQ``."""
        return sum(
            species.charge_number
            * self.particle_rate_derivative_s(species, charge_state_N)
            for species in (self.ion, self.electron)
        )


def build_default_model(
    *,
    electron_to_ion_diffusion: float = 1.0,
    ion_charge_number: float = 2.76,
    electron_to_ion_temperature: float = 1.0,
    outer_ion_density_m3: float = 1.4075e29,
    ion_diffusion_m2_s: float = 3.0e-9,
    ion_temperature_K: float = 5500.0,
) -> ToyChargeModel:
    """Build the A34-parameter reference with quasineutral outer densities.

    The free ratios are diagnostic scan axes, not measured WDM closures.
    """
    scan_inputs = (
        electron_to_ion_diffusion,
        ion_charge_number,
        electron_to_ion_temperature,
        outer_ion_density_m3,
        ion_diffusion_m2_s,
        ion_temperature_K,
    )
    if not all(np.isfinite(value) and value > 0.0 for value in scan_inputs):
        raise ValueError("all default-model scan inputs must be finite and > 0")

    ion = ToySpecies(
        name="representative Fe ion",
        charge_number=ion_charge_number,
        mass_kg=55.845 * const.atomic_mass,
        temperature_K=ion_temperature_K,
        diffusion_m2_s=ion_diffusion_m2_s,
        outer_density_m3=outer_ion_density_m3,
    )
    electron = ToySpecies(
        name="electron",
        charge_number=-1.0,
        mass_kg=const.electron_mass,
        temperature_K=electron_to_ion_temperature * ion_temperature_K,
        diffusion_m2_s=electron_to_ion_diffusion * ion_diffusion_m2_s,
        outer_density_m3=ion_charge_number * outer_ion_density_m3,
    )
    return ToyChargeModel(
        central_mass_kg=1.0e11,
        r_match_m=6.13e-8,
        outer_radius_m=1.0e5,
        electron=electron,
        ion=ion,
    )


def neutral_root_diffusion_ratio(model: ToyChargeModel) -> float:
    """Return the electron/ion diffusion ratio that makes ``F(0)=0``.

    All other model inputs, including outer densities and transport factors,
    are held fixed.  This is an algebraic Toy-A35 diagnostic only.
    """
    positive_rate = model.ion.charge_number * model.particle_rate_s(model.ion, 0.0)
    electron_magnitude = (
        -model.electron.charge_number * model.particle_rate_s(model.electron, 0.0)
    )
    current_ratio = model.electron.diffusion_m2_s / model.ion.diffusion_m2_s
    return current_ratio * positive_rate / electron_magnitude


def quasineutral_critical_diffusion_ratio(model: ToyChargeModel) -> float:
    """Return the analytic ``D_e/D_i`` ratio for a neutral Toy-A35 root.

    For electron charge number ``-1`` and outer quasineutrality
    ``n_e = Z*n_i``, current balance at ``N=0`` reduces independently to

        D_e/D_i = (Phi_i/Phi_e) * h(x_i)/h(x_e).

    This expression is intentionally separate from
    :func:`neutral_root_diffusion_ratio`, which obtains the same quantity from
    the two full particle rates.
    """
    if not np.isclose(model.electron.charge_number, -1.0, rtol=0.0, atol=1.0e-14):
        raise ValueError("analytic quasineutral ratio requires electron charge number -1")
    expected_electron_density = model.ion.charge_number * model.ion.outer_density_m3
    if not np.isclose(
        model.electron.outer_density_m3,
        expected_electron_density,
        rtol=1.0e-12,
        atol=0.0,
    ):
        raise ValueError("analytic quasineutral ratio requires n_e = Z*n_i")

    ion_depth = model.dimensionless_depth(model.ion, 0.0)
    electron_depth = model.dimensionless_depth(model.electron, 0.0)
    return (
        model.ion.transport_factor
        / model.electron.transport_factor
        * float(capture_factor(ion_depth))
        / float(capture_factor(electron_depth))
    )


def find_continuous_equilibrium(
    model: ToyChargeModel,
    *,
    initial_half_width_N: float = 1.0,
    max_abs_N: float = 1.0e6,
) -> ContinuousEquilibrium:
    """Find the unique Toy-A35 root after bracketing it symmetrically."""
    if not np.isfinite(initial_half_width_N) or initial_half_width_N <= 0.0:
        raise ValueError("initial_half_width_N must be finite and > 0")
    if not np.isfinite(max_abs_N) or max_abs_N < initial_half_width_N:
        raise ValueError("max_abs_N must be finite and >= initial_half_width_N")

    half_width = initial_half_width_N
    while True:
        left = -half_width
        right = half_width
        f_left = model.charge_drift_e_s(left)
        f_right = model.charge_drift_e_s(right)
        if f_left >= 0.0 and f_right <= 0.0:
            break
        if half_width >= max_abs_N:
            raise RuntimeError("no charge-drift sign change found inside max_abs_N")
        half_width = min(2.0 * half_width, max_abs_N)

    root = float(
        brentq(
            model.charge_drift_e_s,
            left,
            right,
            xtol=1.0e-12,
            rtol=1.0e-12,
        )
    )
    slope = model.charge_drift_derivative_s(root)
    if not np.isfinite(slope) or slope >= 0.0:
        raise RuntimeError("Toy-A35 stability theorem violated numerically")

    return ContinuousEquilibrium(
        charge_state_N=root,
        charge_C=root * ELEMENTARY_CHARGE,
        drift_slope_s=slope,
        relaxation_time_s=-1.0 / slope,
        bracket_N=(left, right),
    )


def scan_continuous_equilibria(
    *,
    electron_to_ion_diffusions: Iterable[float],
    ion_charge_numbers: Iterable[float],
    electron_to_ion_temperatures: Iterable[float],
) -> list[ScanPoint]:
    """Scan the three explicit Toy-A35 sensitivity axes."""
    diffusion_values = tuple(electron_to_ion_diffusions)
    charge_values = tuple(ion_charge_numbers)
    temperature_values = tuple(electron_to_ion_temperatures)
    if not diffusion_values or not charge_values or not temperature_values:
        raise ValueError("all scan axes must contain at least one value")

    results: list[ScanPoint] = []
    for diffusion_ratio in diffusion_values:
        for charge_number in charge_values:
            for temperature_ratio in temperature_values:
                model = build_default_model(
                    electron_to_ion_diffusion=float(diffusion_ratio),
                    ion_charge_number=float(charge_number),
                    electron_to_ion_temperature=float(temperature_ratio),
                )
                equilibrium = find_continuous_equilibrium(model)
                results.append(
                    ScanPoint(
                        electron_to_ion_diffusion=float(diffusion_ratio),
                        ion_charge_number=float(charge_number),
                        electron_to_ion_temperature=float(temperature_ratio),
                        equilibrium_N=equilibrium.charge_state_N,
                        drift_slope_s=equilibrium.drift_slope_s,
                    )
                )
    return results


def _validate_discrete_charge_model(
    model: ToyChargeModel,
    ion_charge_state: int,
) -> None:
    if isinstance(ion_charge_state, bool) or not isinstance(
        ion_charge_state, (int, np.integer)
    ):
        raise ValueError("ion_charge_state must be an integer")
    if ion_charge_state <= 0:
        raise ValueError("ion_charge_state must be > 0")
    if not np.isclose(model.electron.charge_number, -1.0, rtol=0.0, atol=1.0e-14):
        raise ValueError("discrete model requires electron charge number -1")
    if not np.isclose(
        model.ion.charge_number,
        float(ion_charge_state),
        rtol=0.0,
        atol=1.0e-14,
    ):
        raise ValueError("ion_charge_state must match the model ion charge")


def jump_moment_rates_s(
    model: ToyChargeModel,
    charge_state_N: float,
    *,
    ion_charge_state: int,
) -> tuple[float, float]:
    """Return the first two Kramers-Moyal jump moments ``A(N), B(N)``.

    ``A = Z*lambda_i - lambda_e`` is the charge-state drift and
    ``B = Z**2*lambda_i + lambda_e`` is the jump-variance rate.
    """
    _validate_discrete_charge_model(model, ion_charge_state)
    electron_rate = model.particle_rate_s(model.electron, charge_state_N)
    ion_rate = model.particle_rate_s(model.ion, charge_state_N)
    drift = ion_charge_state * ion_rate - electron_rate
    jump_variance = ion_charge_state**2 * ion_rate + electron_rate
    return drift, jump_variance


def build_discrete_generator(
    model: ToyChargeModel,
    *,
    minimum_N: int,
    maximum_N: int,
    ion_charge_state: int,
) -> tuple[np.ndarray, np.ndarray]:
    """Build a censored finite-state generator for quantized sink charge.

    Electron capture produces ``N -> N-1`` and ion capture produces
    ``N -> N+Z``.  Transitions leaving the finite interval are censored; the
    returned stationary solution is trustworthy only when its edge probability
    is negligible.
    """
    if isinstance(minimum_N, bool) or not isinstance(minimum_N, (int, np.integer)):
        raise ValueError("minimum_N must be an integer")
    if isinstance(maximum_N, bool) or not isinstance(maximum_N, (int, np.integer)):
        raise ValueError("maximum_N must be an integer")
    if maximum_N <= minimum_N:
        raise ValueError("maximum_N must exceed minimum_N")
    _validate_discrete_charge_model(model, ion_charge_state)

    states = np.arange(minimum_N, maximum_N + 1, dtype=int)
    index = {int(state): position for position, state in enumerate(states)}
    generator = np.zeros((states.size, states.size), dtype=float)

    for row, state in enumerate(states):
        electron_destination = int(state) - 1
        if electron_destination >= minimum_N:
            rate = model.particle_rate_s(model.electron, float(state))
            generator[row, index[electron_destination]] += rate
            generator[row, row] -= rate

        ion_destination = int(state) + ion_charge_state
        if ion_destination <= maximum_N:
            rate = model.particle_rate_s(model.ion, float(state))
            generator[row, index[ion_destination]] += rate
            generator[row, row] -= rate

    return states, generator


def stationary_charge_distribution(
    model: ToyChargeModel,
    *,
    minimum_N: int,
    maximum_N: int,
    ion_charge_state: int,
) -> DiscreteChargeResult:
    """Solve ``G.T @ P = 0`` for the truncated stochastic charge process."""
    states, generator = build_discrete_generator(
        model,
        minimum_N=minimum_N,
        maximum_N=maximum_N,
        ion_charge_state=ion_charge_state,
    )
    scale = float(np.max(-np.diag(generator)))
    if not np.isfinite(scale) or scale <= 0.0:
        raise RuntimeError("discrete generator has no finite positive transition scale")

    scaled_generator = generator / scale
    system = scaled_generator.T.copy()
    rhs = np.zeros(states.size, dtype=float)
    system[-1, :] = 1.0
    rhs[-1] = 1.0
    probabilities = np.linalg.solve(system, rhs)

    if float(np.min(probabilities)) < -1.0e-10:
        raise RuntimeError("stationary solve produced materially negative probabilities")
    probabilities = np.clip(probabilities, 0.0, None)
    probabilities /= float(np.sum(probabilities))

    residual = float(np.max(np.abs(scaled_generator.T @ probabilities)))
    mean = float(np.dot(states, probabilities))
    variance = float(np.dot((states - mean) ** 2, probabilities))
    lower_edge = float(probabilities[0])
    upper_edge = float(np.sum(probabilities[states > maximum_N - ion_charge_state]))

    return DiscreteChargeResult(
        states_N=states,
        probabilities=probabilities,
        mean_N=mean,
        variance_N=variance,
        mode_N=int(states[int(np.argmax(probabilities))]),
        stationarity_residual_relative=residual,
        lower_edge_probability=lower_edge,
        upper_edge_probability=upper_edge,
        generator_scale_s=scale,
    )


def audit_stationary_moments(
    model: ToyChargeModel,
    distribution: DiscreteChargeResult,
    *,
    ion_charge_state: int,
) -> DiscreteMomentAudit:
    """Audit the stationary first and second raw jump-moment balances.

    The formulas use the uncensored physical Toy-A35 rates.  A finite-state
    solution therefore needs negligible edge probability in addition to small
    relative residuals.
    """
    _validate_discrete_charge_model(model, ion_charge_state)
    states = np.asarray(distribution.states_N, dtype=float)
    probabilities = np.asarray(distribution.probabilities, dtype=float)
    if states.ndim != 1 or probabilities.shape != states.shape:
        raise ValueError("states and probabilities must be matching 1-D arrays")
    if np.any(probabilities < 0.0) or not np.isclose(
        np.sum(probabilities), 1.0, rtol=0.0, atol=1.0e-12
    ):
        raise ValueError("probabilities must be non-negative and normalized")

    electron_rates = np.array(
        [model.particle_rate_s(model.electron, state) for state in states]
    )
    ion_rates = np.array(
        [model.particle_rate_s(model.ion, state) for state in states]
    )

    first_terms = ion_charge_state * ion_rates - electron_rates
    electron_second_terms = electron_rates * (-2.0 * states + 1.0)
    ion_second_terms = ion_rates * (
        2.0 * ion_charge_state * states + ion_charge_state**2
    )
    second_terms = electron_second_terms + ion_second_terms

    first_residual = float(np.dot(probabilities, first_terms))
    second_residual = float(np.dot(probabilities, second_terms))
    first_scale = float(
        np.dot(probabilities, ion_charge_state * ion_rates + electron_rates)
    )
    second_scale = float(
        np.dot(
            probabilities,
            np.abs(electron_second_terms) + np.abs(ion_second_terms),
        )
    )
    if first_scale <= 0.0 or second_scale <= 0.0:
        raise RuntimeError("moment audit encountered a non-positive scale")

    return DiscreteMomentAudit(
        first_moment_residual_s=first_residual,
        first_moment_residual_relative=abs(first_residual) / first_scale,
        second_moment_residual_s=second_residual,
        second_moment_residual_relative=abs(second_residual) / second_scale,
    )


def kramers_moyal_ou_approximation(
    model: ToyChargeModel,
    *,
    ion_charge_state: int,
) -> KramersMoyalApproximation:
    """Linear-noise variance around the stable continuous Toy-A35 root."""
    _validate_discrete_charge_model(model, ion_charge_state)
    equilibrium = find_continuous_equilibrium(model)
    drift, jump_variance = jump_moment_rates_s(
        model,
        equilibrium.charge_state_N,
        ion_charge_state=ion_charge_state,
    )
    restoring_rate = -model.charge_drift_derivative_s(equilibrium.charge_state_N)
    rate_scale = (
        ion_charge_state * model.particle_rate_s(model.ion, equilibrium.charge_state_N)
        + model.particle_rate_s(model.electron, equilibrium.charge_state_N)
    )
    if abs(drift) > 1.0e-10 * rate_scale:
        raise RuntimeError("continuous equilibrium does not close the jump drift")
    if restoring_rate <= 0.0 or jump_variance <= 0.0:
        raise RuntimeError("OU approximation requires stable positive rates")

    return KramersMoyalApproximation(
        equilibrium_N=equilibrium.charge_state_N,
        restoring_rate_s=restoring_rate,
        jump_variance_rate_s=jump_variance,
        variance_N=jump_variance / (2.0 * restoring_rate),
    )


def main() -> None:
    model = build_default_model(electron_to_ion_diffusion=100.0)
    equilibrium = find_continuous_equilibrium(model)
    scan = scan_continuous_equilibria(
        electron_to_ion_diffusions=(1.0, 100.0, 1000.0),
        ion_charge_numbers=(2.76, 5.0, 26.0),
        electron_to_ion_temperatures=(0.5, 1.0, 2.0),
    )

    integer_seed = build_default_model(ion_charge_number=3.0)
    neutral_ratio = neutral_root_diffusion_ratio(integer_seed)
    analytic_ratio = quasineutral_critical_diffusion_ratio(integer_seed)
    integer_model = build_default_model(
        electron_to_ion_diffusion=neutral_ratio,
        ion_charge_number=3.0,
    )
    discrete = stationary_charge_distribution(
        integer_model,
        minimum_N=-100,
        maximum_N=100,
        ion_charge_state=3,
    )
    moment_audit = audit_stationary_moments(
        integer_model,
        discrete,
        ion_charge_state=3,
    )
    ou_approximation = kramers_moyal_ou_approximation(
        integer_model,
        ion_charge_state=3,
    )

    print("=== Stage 3.95A / A35 Diagnostic Charge Theorem ===")
    print("Scientific scope: Toy-A35 only; physical multicomponent Q_eq remains OPEN")
    print(f"r_match/r_Schw = {model.matching_to_horizon_ratio:.6e}")
    print(
        "continuous reference: "
        f"N_eq={equilibrium.charge_state_N:.9f}, "
        f"F'={equilibrium.drift_slope_s:.6e} s^-1"
    )
    print(
        "neutral-root diffusion ratio: "
        f"rate-balance={neutral_ratio:.9f}, analytic={analytic_ratio:.9f}"
    )
    print(f"scan points={len(scan)}, all stable={all(point.drift_slope_s < 0.0 for point in scan)}")
    print(
        "discrete reference: "
        f"mean_N={discrete.mean_N:.9f}, mode_N={discrete.mode_N}, "
        f"variance_N={discrete.variance_N:.9f}, "
        f"edge_P={discrete.lower_edge_probability + discrete.upper_edge_probability:.3e}"
    )
    print(
        "moment residuals: "
        f"first={moment_audit.first_moment_residual_relative:.3e}, "
        f"second={moment_audit.second_moment_residual_relative:.3e}"
    )
    print(
        "OU variance cross-check: "
        f"approx={ou_approximation.variance_N:.9f}, "
        f"discrete={discrete.variance_N:.9f}"
    )


if __name__ == "__main__":
    main()
