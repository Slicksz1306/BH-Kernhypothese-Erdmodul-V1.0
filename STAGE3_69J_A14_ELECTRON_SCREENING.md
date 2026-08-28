# Stage 3.69J / A14 — Dense-core charged-electron screening closure

## Status

**PARTIAL DENSE-CORE CHARGE CLOSURE CALCULATED / FULL SCREENED COULOMB-DIRAC ELECTRON S-MATRIX STILL OPEN**

## Motivation

A4 showed that positive BH charge suppresses proton capture only by an order-unity factor over the tested `Q=0...24e` range, but the charged-electron far-field problem was left open because a naive finite-radius Coulomb basis is not controlled for the very small electron gravitational coupling.

The dense Earth-core environment changes the appropriate outer boundary: electrons are degenerate / warm-dense and electrostatic fields are screened on a Thomas-Fermi scale much smaller than `r_B`.

## Literature anchors

- Zajaček et al. (2018), *On the charge of the Galactic centre black hole*, MNRAS 480, 4408: diffuse stationary proton/electron plasma gives a small equilibrium BH charge; for equal temperatures the formula reduces to the mass-difference equilibrium scale. The same paper explicitly discusses exponential plasma shielding beyond the Debye scale.
- Nakao et al. (2025), *Electrification of a nonrotating black hole*, Phys. Rev. D 112, 064033: relativistic treatment confirms that plasma accretion can charge a nonrotating BH and that the equilibrium charge depends on proton/electron temperatures.
- For a degenerate electron gas the Thomas-Fermi screening length is

```text
lambda_TF = sqrt(2 eps0 E_F / (3 n_e e^2)).
```

The screened point-charge potential is Yukawa-like,

```text
phi(r) ~ Q exp(-r/lambda_TF)/(4 pi eps0 r).
```

## Diffuse benchmark

For `M_BH=1e11 kg`, equal electron/proton temperatures give

```text
Q_eq,diffuse ~ +24.181 e.
```

The proton force-balance scale is

```text
Q_p,force ~ +48.388 e,
```

while the electron force-balance magnitude is only

```text
|Q_e,force| ~ 0.02635 e.
```

These continuous diffuse-plasma scales are not automatically valid in dense Fe/WDM matter.

## Dense Fe/WDM electron state

Using the A5 outer ion-density proxy

```text
n_i ~1.4075e29 m^-3
```

and the A12b outer mean-ionization value `Zbar~2.76`, with full ionization `Z=26` retained only as an upper electron-density proxy:

| Zbar | n_e [m^-3] | E_F [eV] | v_F [m/s] | lambda_TF [m] |
|---:|---:|---:|---:|---:|
| `2.76` | `3.88e29` | `19.4` | `2.61e6` | `4.29e-11` |
| `5` | `7.04e29` | `28.9` | `3.19e6` | `3.89e-11` |
| `10` | `1.41e30` | `45.8` | `4.01e6` | `3.46e-11` |
| `26` | `3.66e30` | `86.6` | `5.52e6` | `2.95e-11` |

Thus the preferred outer-core screening length is a few `1e-11 m`, consistent with the earlier A5 scale.

## Screened charge-energy bracket

At one Thomas-Fermi length the Yukawa factor contributes `exp(-1)`. For one positive elementary BH charge, the attractive electron potential-energy magnitude at `r=lambda_TF` is therefore about

```text
12.3 ... 17.9 eV
```

across `Zbar=2.76...26`.

Equating this screened potential scale to the electron Fermi energy gives a reduced charge-response scale

```text
N_screen ~ E_F / |e phi_1(lambda_TF)|
         ~ 1.57 ... 4.83 elementary charges.
```

Adding the small `6000 K` thermal term changes this only weakly:

```text
N_screen,thermal ~1.64 ... 4.87 e.
```

This is **not an exact equilibrium-charge derivation**. It is a physically transparent dense-core screening bracket showing that the diffuse `+24.18e` scale cannot simply be imported into the degenerate Earth-core environment.

## Response timescale

The local screening-response scale

```text
t_screen ~ lambda_TF / v_F
```

is

```text
~5e-18 ... 2e-17 s.
```

Thus electron charge rearrangement is effectively instantaneous compared with any macroscopic supply or thermal evolution in the project.

## Recoupling to A4 proton Dirac capture

Running the existing charged-proton Dirac solver at the dense screened charge scale gives, for `M=1e11 kg` and Earth-speed protons:

```text
Q~+1.6e -> sigma_p/sigma_neutral_classical ~0.925
Q~+3.67e -> ~0.889
Q~+4.9e -> ~0.867.
```

Therefore the dense screened charge bracket does **not** create an orders-of-magnitude proton-capture suppression.

Positive charge also attracts electrons, providing a fast self-neutralizing feedback. Negative charge reverses the feedback and strongly favors proton capture / electron repulsion. Because charge is quantized in units of `e`, the actual microscopic state should be treated as a stochastic few-charge process rather than a smooth large continuous `Q`.

## Conclusion

Within the reduced dense-core charge closure:

```text
diffuse +24e equilibrium scale -> NOT preferred for Earth core
screened dense-core charge scale -> O(1...5 e)
proton capture suppression at that scale -> order-unity only
large electrostatic proton blocker -> NOT FOUND
```

The remaining refinement is a full **screened Coulomb-Dirac electron scattering/capture calculation** using a finite-range/Yukawa outer potential and dense-matter electron distribution. That refinement can change detailed charge statistics but is not currently indicated to generate the many-orders suppression required to overturn the A10/A13 processing result.

## Reproducibility

- `stage3_69j_a14_electron_screening.py`

## Claims boundary

This is a reduced dense-matter closure, not a direct measurement and not a complete kinetic charge-state simulation.
