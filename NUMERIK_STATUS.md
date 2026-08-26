# Numerischer und physikalischer Status – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Aktuelle Stufe:** Stage 3.69 bis A13 partiell numerisch bearbeitet; Full-Multiphysics und Stage 3.70 offen

## Aussagegrenze

`PASS` bezeichnet nur einen definierten Solver-/Regressionstest innerhalb seiner Annahmen. Kein numerischer PASS ist eine experimentelle Bestaetigung eines Erdzentrum-BH.

```text
H+ = mit Standard-Hawking
H0 = ohne Hawking
```

H+ Standard-Hawking bleibt im getesteten Projekt-SK-IV-Reinterpretationsmodell FAIL. H0 bleibt OPEN.

# Kernresultate A1-A12

```text
Dirac proton @1e11 kg: ~0.9503 classical
Fe-56 scalar/composite @1e11 kg: ~0.99754 classical
Ni-58 scalar/composite @1e11 kg: ~0.99646 classical
large wave suppression: NOT FOUND
charged-electron far-field matcher: OPEN
```

Repeated encounter:

```text
chi_capture=p/(p+e_perm)
```

A10:

```text
local Kn~1 != permanent escape through outer dense Fe/WDM reservoir.
```

A11/A12:

```text
absorbing Bondi regression: PASS
reflecting/capacity-limited boundary: outward backpressure shock
1e10 historical-supply shock position converges to ~1.23 r_B at t=0.8
stationary finite shock Mdot: NOT ESTABLISHED.
```

A12b:

```text
Zbar_Fe(rho=13.0885 g/cm3,T=6000K)~2.76
eta=8.5...26 mPa s
k=67...87 W/m/K
```

Dissipative sensitivity does not qualitatively remove the historical high-supply 1e10 backpressure branch.

# A12c – outer supply reopened

Historical `1e11 kg` supply

```text
1.47e-8 ... 1.46e-7 kg/s
```

is now **LEGACY / EOS-SENSITIVE**.

Relativistic constant-Gamma sensitivity:

```text
Gamma=1.75  -> 1.19e-7 kg/s
Gamma=1.80  -> 2.89e-8
Gamma=1.85  -> 8.02e-9
Gamma=2.00  -> 3.35e-10
Gamma=2.356 -> 2.40e-12 [stress limit only]
```

A constant PREM-local stiffness to the horizon is rejected as a preferred physical closure.

# A13 – general-EOS Michel solver

Implemented equations:

```text
4 pi r^2 rho0 u = Mdot
h sqrt(1-2M/r+u^2)=h_inf
```

Critical point:

```text
u_s^2=a_s^2/(1+3a_s^2)
r_s/M=(1+3a_s^2)/(2a_s^2)
h_s/sqrt(1+3a_s^2)=h_inf.
```

## Regression

General-EOS constant-stiffness solver reproduces A12c at `M=1e11 kg`:

```text
beta=1.50  rel drift ~8.7e-5
beta=1.80  ~3.1e-5
beta=2.00  ~2.5e-5
beta=2.356 ~1.8e-5
```

```text
A13 solver regression: PASS
```

## Variable-EOS surrogate

PREM outer `P`, `K_S`, `dK/dP` are matched simultaneously. Controlled EOS transitions:

```text
outer beta=2.356 only to rho=30...47.2 g/cm3
beta_mid=1.4...1.8
inner transition rho=1e5...1e7 g/cm3
beta_inner=4/3.
```

This is a sensitivity family, not a confidence interval.

At `M=1e11 kg`:

```text
Mdot_supply,surrogate ~4.64e-8 ... 1.37e-6 kg/s.
```

## Reclassification against A10 processing capacity

| M_BH | Xi_min | Xi_max |
|---:|---:|---:|
| `1e10` | `0.467` | `13.76` |
| `1e11` | `8.94e-4` | `2.64e-2` |
| `2e11` | `1.36e-4` | `4.01e-3` |
| `5e11` | `1.12e-5` | `3.32e-4` |

```text
M>=1e11 kg: robustly processing-capable across tested A13 surrogate
M=1e10 kg: Xi crosses 1 -> supply/EOS conditional.
```

# Real-data A13b gap

Grant et al. 2021 provide liquid-Fe elevated-isentrope measurements and public supporting data. Their paper reports:

```text
K0=25.3 +/-4.0 GPa
K0'=6.60 +/-0.33
gamma0=2.42 +/-0.12
rho0=5.187 g/cm3 reference.
```

The linked Zenodo dataset could not be reliably machine-read in the current run, so no figure-derived points were invented.

```text
real tabulated Fe/Ni isentrope: OPEN
final physical supply band: OPEN
final species-resolved net Mdot: OPEN
```

# Wichtige Korrekturen

```text
Hard cavity -> rejected
Michel = automatic horizon Mdot -> rejected
single-pass loss cone = net suppression -> rejected
Fe/Ni spin-1/2 -> corrected to 0+ composite proxy
sonic point blocks all feedback -> corrected
EC threshold = instant neutronization -> corrected
Kn=1 = permanent escape -> rejected
1e10 always backpressure -> corrected: EOS/supply conditional
historical Michel range = universal supply -> rejected
constant PREM stiffness to horizon = preferred supply -> rejected / stress limit.
```

# Aktuelle Endmatrix

| Frage | Status |
|---|---|
| Dirac/scalar capture solvers | **PASS/CALCULATED under defined tests** |
| charged-electron Coulomb far field | **OPEN** |
| A9-A12 inner processing/transport | **PARTIAL, strongly hardened** |
| A13 general-EOS critical solver | **PASS regression** |
| A13 variable-EOS surrogate supply | **CALCULATED** |
| `>=1e11 kg` inner processing | **ROBUST in tested A13 surrogate** |
| `1e10 kg` capacity/backpressure | **EOS/SUPPLY CONDITIONAL** |
| real tabulated Fe/Ni supply | **OPEN** |
| final net Mdot | **OPEN** |
| Stage 3.69 Full-Multiphysics | **OPEN** |
| Stage 3.70 Real-Data falsification | **OPEN** |
| direct BH detection | **NONE** |

# Naechster Block

```text
A13b:
real liquid-Fe isentrope / SESAME-consistent data ingestion
-> reconstruct h(rho)
-> direct general-EOS Michel critical solve
-> final defensible outer-supply bracket
-> recouple A9-A12
-> rerun heat/age constraints.
```
