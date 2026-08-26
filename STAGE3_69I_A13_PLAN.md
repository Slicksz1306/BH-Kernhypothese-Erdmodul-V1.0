# Stage 3.69I / A13 – General-EOS Relativistic Michel Supply + Net-Mdot Closure

**Stand:** 26.08.2026  
**Status:** PARTIAL CALCULATED / GENERAL-EOS SOLVER REGRESSION PASS / VARIABLE-EOS SURROGATE DONE / REAL TABULATED Fe/Ni ISENTROPE OPEN

## Motivation

A12c zeigte, dass der historische Michel-Benchmark bei `M=1e11 kg`

```text
1.47e-8 ... 1.46e-7 kg/s
```

nicht als universelle Supply-Rate verwendet werden darf. Ein konstantes PREM-local stiffness surrogate bis zum Horizon war ebenfalls zu stark: reales Fe/Ni ionisiert, degeneriert und aendert seine effektive EOS.

A13 bestimmt deshalb den Supply erstmals mit einer relativistischen **general-EOS** Kritikalitaet.

## A13 – bereits gerechnet

### General-EOS Michel solver

Stationaere sphärische Schwarzschild-Akkretion:

```text
4 pi r^2 rho0 u = Mdot
h sqrt(1 - 2M/r + u^2) = h_inf
```

mit

```text
a^2 = dP/d epsilon.
```

Am kritischen Punkt:

```text
u_s^2 = a_s^2/(1+3 a_s^2)
r_s/M = (1+3 a_s^2)/(2 a_s^2)
h_s/sqrt(1+3 a_s^2) = h_inf.
```

Status: **IMPLEMENTED**.

### Regression

Der Solver reproduziert A12c fuer konstante Steifigkeit bei `M=1e11 kg`:

```text
beta=1.50  rel drift ~+8.7e-5
beta=1.80  ~+3.1e-5
beta=2.00  ~+2.5e-5
beta=2.356 ~+1.8e-5.
```

```text
constant-Gamma/A12c regression: PASS
```

### PREM outer boundary

A13 nutzt gleichzeitig:

```text
rho_inf ~13.08848 g/cm3
P_inf   ~363.8521 GPa
K_S     ~1.4253 TPa
dK/dP   ~2.356
c_s     ~10.4355 km/s.
```

### Thermodynamisch konsistentes piecewise surrogate

Jedes Segment erfuellt

```text
B = rho dP/drho
dB/dP = beta
P, B, h continuous
dh=dP/(rho c^2).
```

Outer PREM stiffness `beta=2.356` wird nur bis

```text
rho_soft=30 oder 47.2 g/cm3
```

gehalten. Danach wird als transparenter Intermediate-EOS-Sensitivitaetstest

```text
beta_mid=1.4 ... 1.8
```

verwendet. Der innere Uebergang zum `4/3`-Ast wird um den Elektronen-Relativitaetsproxy

```text
rho~2.10e6 g/cm3
```

mit Sensitivitaet `1e5...1e7 g/cm3` variiert.

Dies ist **kein** statistisches Konfidenzintervall und keine finale Fe/Ni-EOS.

## Aktuelles A13-Supply-Surrogat

Bei `M=1e11 kg`:

```text
Mdot_supply ~4.64e-8 ... 1.37e-6 kg/s.
```

Das zeigt:

```text
constant PREM stiffness to horizon -> stress limit only
variable EOS softening -> supply can return to historical range or above.
```

Die A12c-Zahl `~2.40e-12 kg/s` fuer konstant `Gamma=2.356` bleibt daher nur ein Stresslimit, keine bevorzugte Endrate.

## Rueckkopplung an A9-A12

A10-fast Processing-Capacity mit dem neuen A13-Surrogat:

| M_BH | Mdot_min [kg/s] | Mdot_max [kg/s] | Xi_min | Xi_max |
|---:|---:|---:|---:|---:|
| `1e10` | `4.64e-10` | `1.37e-8` | `0.467` | `13.76` |
| `1e11` | `4.64e-8` | `1.37e-6` | `8.94e-4` | `2.64e-2` |
| `2e11` | `1.86e-7` | `5.47e-6` | `1.36e-4` | `4.01e-3` |
| `5e11` | `1.16e-6` | `3.42e-5` | `1.12e-5` | `3.32e-4` |

```text
M>=1e11 kg:
processing-capable survives across the entire controlled A13 surrogate.

M=1e10 kg:
Xi crosses 1 -> supply/EOS conditional.
```

## Acceptance Criteria – Status

1. constant-Gamma GR regression: **PASS**
2. thermodynamically consistent variable-EOS route: **PARTIAL PASS via piecewise barotrope**
3. no constant PREM Gamma to horizon: **PASS / corrected**
4. critical-point solution numerically unique in tested family: **PASS**
5. EOS validity/transition markers explicit: **PASS for surrogate**
6. supply range instead of single pseudo-precise value: **PASS for surrogate**
7. mass scan `1e10...5e11`: **CALCULATED**
8. A9-A12 capacity reclassification: **CALCULATED**
9. experimental evidence claim avoided: **PASS**
10. real tabulated Fe/Ni isentrope: **OPEN**
11. final physical Mdot uncertainty band: **OPEN**

## Real-data EOS anchor found for A13b

Grant et al. (2021) measured liquid-Fe elevated isentropes from roughly `275...400 GPa`, found excellent agreement with SESAME 92141, and provide public supporting data via Zenodo DOI `10.5281/zenodo.4464112`.

The paper also reports fitted liquid-Fe EOS parameters at the 7000-K reference state:

```text
K0     = 25.3 +/- 4.0 GPa
K0'    = 6.60 +/- 0.33
gamma0 = 2.42 +/- 0.12
rho0   = 5.187 g/cm3 (reference value used in model).
```

The public Zenodo record was not reliably retrievable in the present tool session, so no data points are fabricated or digitized from figures.

## Naechster Unterblock – A13b

```text
obtain public Grant liquid-Fe isentrope / SESAME-consistent data
-> ingest real rho-P-(c_s/T where supplied) points
-> reconstruct h(rho) thermodynamically
-> run general-EOS Michel directly on tabulated/interpolated data
-> compare with A13 surrogate envelope
-> establish defensible outer-supply bracket
-> recouple A9-A12
-> rerun heat/age constraints.
```

A13 bleibt bis dahin **PARTIAL**. Stage 3.69 Full-Multiphysics und Stage 3.70 bleiben OPEN.
