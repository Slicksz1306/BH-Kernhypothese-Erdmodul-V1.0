# Numerischer und physikalischer Status – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 29.08.2026  
**Aktuelle Stufe:** Reduced/partial numerischer Stack bis A19; Stage 3.70B Real-Data-Audit partiell gerechnet

## Aussagegrenze

`PASS` bezeichnet nur einen definierten Solver-/Regression-/Konvergenztest innerhalb seiner Annahmen. Kein numerischer PASS ist eine experimentelle Bestätigung eines Erdzentrum-BH.

```text
H+ = Standard-Hawking
H0 = ohne Hawking
```

H+ bleibt in der Projekt-Reinterpretation des stärksten publizierten SK-IV-Hochenergie-Binlimits negativ. H0 bleibt OPEN / nicht nachgewiesen.

# A1-A12 – Solver / Capture / Transport

```text
Dirac proton @1e11 kg: ~0.9503 classical
Fe-56 scalar/composite: ~0.99754 classical
Ni-58 scalar/composite: ~0.99646 classical
large wave suppression: NOT FOUND
```

Repeated encounter:

```text
chi_capture = p/(p+e_perm).
```

A10:

```text
local Kn~1 != permanent escape through outer dense Fe/WDM reservoir.
```

A11/A12:

```text
absorbing Bondi regression: PASS
capacity-limited boundary: outward backpressure shock
1e10 stationary finite shock Mdot: NOT ESTABLISHED.
```

# A13 – general-EOS Michel

Implemented:

```text
4 pi r^2 rho0 u = Mdot
h sqrt(1-2M/r+u^2)=h_inf

u_s^2=a_s^2/(1+3a_s^2)
r_s/M=(1+3a_s^2)/(2a_s^2)
h_s/sqrt(1+3a_s^2)=h_inf.
```

Constant-stiffness regression against A12c:

```text
relative drift ~1e-5 ... 1e-4
A13 solver regression: PASS.
```

A13 variable-EOS surrogate at `1e11 kg`:

```text
Mdot_supply ~4.64e-8 ... 1.37e-6 kg/s.
```

# A13b – Grant experimental-fit outer EOS

The published Grant-2021 liquid-Fe analytic fit is implemented through `400 GPa`, then coupled to an explicit intermediate/deep EOS sensitivity family.

PREM-boundary check:

```text
B_Grant ~1.419 TPa
K_PREM  ~1.425 TPa
ratio   ~0.9957.
```

At `1e11 kg`:

```text
nominal fit-anchor scan:
~1.29e-7 ... 3.80e-6 kg/s

conservative fit/T/intermediate-EOS corner scan:
~8.27e-8 ... 6.13e-6 kg/s.
```

```text
raw Zenodo / direct SESAME table ingestion: OPEN
final physical supply interval: OPEN.
```

# A14 – Dense-core electron screening

Thomas-Fermi dense-electron bracket:

```text
E_F       ~19.4 ... 86.6 eV
lambda_TF ~4.29e-11 ... 2.95e-11 m
screened charge-response scale ~O(1...5e).
```

Existing proton Dirac solver within that bracket:

```text
Q~+1.6e -> ~0.925 classical
Q~+4.9e -> ~0.867 classical.
```

```text
large electrostatic proton blocker: NOT FOUND
full screened Coulomb-Dirac electron S-matrix: OPEN refinement.
```

# A15 – Integrated reduced throughput

A13b Supply / A10 capacity:

| M_BH | Xi_min | Xi_max |
|---:|---:|---:|
| `1e10` | `0.832` | `61.60` |
| `1e11` | `1.59e-3` | `1.18e-1` |
| `2e11` | `2.42e-4` | `1.80e-2` |
| `5e11` | `2.00e-5` | `1.48e-3` |

```text
M>=1e11 kg: processing-capable in tested A13b reduced stack
M=1e10 kg: supply/EOS/backpressure conditional
final species-resolved net Mdot: OPEN.
```

# A16 – Heat / age

`eta=1` current rest-mass power upper edges:

```text
1e10 kg: 0.0055 TW
1e11 kg: 0.551 TW
2e11 kg: 2.20 TW
5e11 kg: 13.76 TW.
```

```text
47-TW hard total-budget pre-test: NO EXCLUSION.
```

Fixed-environment `dM/dt=kM^2` backward solutions over 4.54 Gyr remain positive; high-rate branches have short present growth times and strong evolutionary sensitivity.

# A17 – Observability gate

Direct microscopic near-zone seismology is extremely sub-wavelength.

At `lambda=1 km`:

```text
ka ~3.9e-11 ... 1.9e-9
(ka)^4 size proxy ~2e-42 ... 1e-35.
```

Thus Stage 3.70 H0 seismology requires a predicted macroscopic profile/amplitude, not direct r_B-scale resolution.

# A18 – Real-data audit

For `25.29...31.29 MeV`, the 2026 SK-Gd publication lists:

```text
SK-IV observed 90% CL   = 0.04 cm^-2 s^-1 MeV^-1
SK-Gd NN observed       = 0.13
SK-Gd BDT observed      = 0.16.
```

Project H+ proxy:

```text
0.098 ... 0.122.
```

So:

```text
project / strongest SK-IV limit = 2.45 ... 3.05
H+ = FAIL in project reinterpretation against strongest published bin constraint.
```

The standalone 2026 SK-Gd-only limits are weaker in that bin. No official Earth-center-BH exclusion is claimed.

H0:

```text
REAL-DATA LIKELIHOOD NOT YET IDENTIFIABLE
```

because a unique macro observable amplitude/profile is still missing.

# A19 – Formation numerical scale test

Optimistic direct-Earth dynamical-friction energy loss at `v_inf=220 km/s`:

```text
DeltaE/E_inf ~1e-18 ... 5e-17
```

for `1e10...5e11 kg`.

One-crossing capture-friendly asymptotic thresholds in same proxy:

```text
~0.0043 ... 0.0307 m/s.
```

```text
normal halo direct Earth capture: VERY STRONG FAIL
cold/co-moving primordial seed: OPEN initial condition / origin not derived.
```

# Current numerical matrix

| Frage | Status |
|---|---|
| Dirac/scalar capture solvers | **PASS/CALCULATED under defined tests** |
| A13 general-EOS critical solver | **PASS regression** |
| A13b empirical-fit Fe outer supply | **PARTIAL CALCULATED** |
| dense-core charge/screening | **PARTIAL / strongly constrained** |
| `>=1e11 kg` reduced inner processing | **PROCESSING-CAPABLE in tested A13b stack** |
| `1e10 kg` capacity/backpressure | **EOS/SUPPLY CONDITIONAL** |
| heat total-budget pre-test | **NO EXCLUSION** |
| H+ strongest SK-IV project comparison | **FAIL** |
| H0 real-data likelihood | **NOT IDENTIFIABLE YET** |
| formation from ordinary halo encounter | **VERY STRONG FAIL** |
| raw tabulated Fe/Ni supply | **OPEN** |
| full mixture/two-temperature WDM | **OPEN** |
| final species-resolved net Mdot | **OPEN** |
| direct BH detection | **NONE** |
| unique positive H0 signature | **NONE** |

# Remaining numerical/physical blockers

```text
1. direct raw Fe-isentrope / SESAME ingestion
2. full composition-dependent two-temperature WDM closure
3. screened electron S-matrix / stochastic charge kinetics refinement
4. final species/reaction-resolved Mdot_BH(t), Q(t)
5. unique macroscopic H0 observable
6. real-data likelihood on that observable
7. formation/delivery mechanism.
```
