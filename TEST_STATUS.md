# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 29.08.2026  
**Forschungsstand:** Reduced Stack A1–A19 abgeschlossen; A20–A31 / Stage 3.72 weitergeführt; Formation/Delivery bis Stage 3.78 / F6

## Statusbegriffe

- **PASS** = definierter Solver-/Regression-/Konvergenztest bestanden; kein empirischer Nachweis.
- **CALCULATED** = definierter Benchmark numerisch berechnet.
- **PARTIAL** = kontrollierter Unterblock gerechnet, volle physische Closure fehlt.
- **FAIL** = konkret getesteter Branch scheitert am verwendeten Test.
- **OPEN** = mit vorhandener Closure nicht abschließend entschieden.
- **CORRECTED / REJECTED** = frühere Zwischenannahme durch härteren Test ersetzt.

## Wissenschaftliche Aussagegrenze

```text
keine direkte Detektion eines Erdzentrum-BH
keine eindeutige positive H0-Signatur
H+ FAIL in projektinterner strongest-SK-IV reinterpretation
H0 OPEN / nicht nachgewiesen
Formation/Delivery OPEN
```

Die Projektresultate sind Modell-/Solverresultate und **keine experimentelle BH-Evidenz**.

# 1. Branches

```text
H+ = Standard-Hawking
H0 = ohne Hawking
```

H+ bleibt **FAIL** in der projektinternen Reinterpretation des stärksten publizierten SK-IV-Hochenergie-Binlimits. Dies ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

H0 bleibt **OPEN / nicht nachgewiesen**.

# 2. Struktur / Makromodell

| Test | Status |
|---|---|
| starke Zentralmassenvariante | **FAIL** |
| Hard-Cavity/Hard-Replacement | **FAIL / verworfen** |
| kleiner smooth-compensated Branch | kein eigener Makro-Ausschluss in reduzierten Modellen |
| direkte r_B-Skalen-Seismik | **kein sinnvoller Beobachtungskanal** |
| makroskopische Seismik/Normalmoden | **OPEN** |
| direkte experimentelle Detektion | **keine** |
| eindeutige positive Signatur | **keine** |

# 3. Reduced Capture-/Transportstack A1–A19

| Teiltest | Status |
|---|---|
| Schwarzschild-Dirac solver / current / matching | **PASS an definierten Regressionen** |
| Earth-speed Protonenscan `1e10...5e11 kg` | **CALCULATED** |
| Proton @`1e11 kg` | `~0.9503 classical` |
| Fe-56 @`1e11 kg` | `~0.99754 classical` |
| Ni-58 @`1e11 kg` | `~0.99646 classical` |
| große Wave-Suppression @`1e11 kg` | **NOT FOUND** |
| repeated encounter recycling | **DONE** |
| local `Kn~1` = permanent escape | **REJECTED** |
| A11/A12 dynamic backpressure PDE | **PARTIAL CALCULATED** |
| A13/A13b relativistic/empirical outer supply | **PARTIAL CALCULATED** |
| A14 dense-core screening | **PARTIAL CALCULATED** |
| A15 reduced net throughput `>=1e11 kg` | **PROCESSING-CAPABLE in tested stack** |
| A16 hard total heat-budget pretest | **NO EXCLUSION** |
| A17 microscopic near-zone seismics | **not useful** |
| A18 H+ strongest SK-IV project comparison | **FAIL** |
| A19 normal halo -> Earth capture | **VERY STRONG FAIL** |

A19 capture-freundlicher direct-Earth Proxy bei `v_inf=220 km/s`:

```text
DeltaE/E_inf ~1e-18 ... 5e-17
```

# 4. Stage 3.72 – A20–A31 Charge / WDM Transport

Aktueller konsolidierter Stand:

```text
electron Dirac sink flux-direct: stabilized
nonlinear Thomas-Fermi screening: calculated and recoupled
collective charge response: much faster than hydro
naive independent ion/electron current: REJECTED
exact Q_eq: OPEN
```

Der verbleibende Charge-Engpass ist:

```text
multicomponent Onsager / Maxwell-Stefan mobility matrix
+ chemical-potential derivatives
+ sink-boundary coupling.
```

A31 hält ausdrücklich fest:

```text
self diffusion != mutual diffusion != charge mobility.
```

# 5. Formation / Delivery

## F1 – Protosolar / co-moving Seed

```text
normal halo -> protostellar cloud: strongly negative
protoplanetary gas drag for naked seed: insufficient / FAIL
already solar-bound dynamically cold seed: OPEN initial condition.
```

## F2 – Hill / Pull-down Energy Gate

```text
temporary Hill capture: PASS / dynamically allowed
static permanent capture without potential evolution: FAIL
smooth terrestrial pull-down: FAIL as generic channel
giant-impact impulsive mass jump: PASS kinematic existence
absolute delivery probability: OPEN.
```

## F3 – Adaptive Hill-Monte-Carlo / Jacobi Closure

Konservativer `r>=0.1 r_H` Pull-down-Anteil:

| DeltaM/M | Ergebnis |
|---:|---:|
| `0.01` | `0` in sampled outer gate |
| `0.03` | `0` in sampled outer gate |
| `0.10` | `0.035...0.072%` |
| `0.30` | `5.65...6.81%` |

```text
adaptive DOP853/Jacobi solver: PASS
fixed-step deep-encounter RK4 result: REJECTED
small GI <=3%: FAIL in sampled outer gate
10% GI: PASS existence / inefficient
30% GI: PASS conditional few-percent channel.
```

## F3b – Multi-Pass / Residence Timing

Literatur-/Stressanker:

```text
F3 first passage ~35.3 d
mean Earth TCO ~286 d
2020 CD3 median ~4 yr
extreme clone tail ~100 yr.
```

```text
multi-pass residence amplification: PASS
multi-pass as generic Myr random-impact timing rescue: FAIL.
```

## F4 – Early permanent embryo-bound Seed

```text
collisionless terrestrial exchange capture: physically allowed
stable embryo-bound phase space: PASS
embryo-scattering kick scale: PASS kinematic
growth-assisted engulfment: PASS conditional in adiabatic limit
post-engulfment damping: Myr-scale feasibility in optimistic proxy
absolute probability: OPEN.
```

Für `a_seed~0.3 r_H` muss Capture im adiabatischen Proxy ungefähr vor

```text
M1 ~0.041 M_E
```

erfolgen, damit spätere Growth-assisted Engulfment bis `1 M_E` möglich bleibt.

## F5 – Restricted 4-body Exchange Monte-Carlo

Direkt integriert:

```text
Sun + Proto-Earth M1 + second embryo M2 + massless seed.
```

Kritische Korrektur:

```text
unphysical low-pericentre-speed pilot: REJECTED
final hyperbolic flyby:
V_p^2 = V_inf^2 + 2G(M1+M2)/b.
```

Gepaarter `M2=0` Counterfactual: **PASS**.

Persistenz bis `20 Omega^-1 ~3.18 yr`:

| Ensemble | persistent stable |
|---|---:|
| STRONG | `5/300 = 1.67%` |
| BROAD | `3/300 = 1.00%` |
| WEAK | `0/300` |

Exchange-induced FULL-only body crossings:

```text
STRONG 4/300
BROAD  3/300
WEAK   0/300
```

Bereits gebunden beim Body-Eintritt:

```text
STRONG 2/4
BROAD  3/3.
```

Positive-energy one-pass crossings bleiben trotz großzügigem A19-Drag ungebunden.

Status:

```text
local collisionless embryo-exchange mechanism: PASS conditionally
generic formation probability: NOT ESTABLISHED.
```

## F6 – Population-weighted Formation Gate

Core model:

```text
lambda = N_enc K_F5 S_post n_seed V_H
P_delivery = 1-exp(-lambda).
```

Reference:

```text
M1=0.03 M_E
K_F5=5/300
N_enc=10
S_post=0.5
P_target=0.5
r_H=465,012 km
V_H=4.212e26 m^3.
```

Required eligible Hill occupancy:

```text
mu_H,50 = 8.318 seeds per Hill volume.
```

Encounter-count sensitivity:

| N_enc | mu_H,50 |
|---:|---:|
| `1` | `83.18` |
| `3` | `27.73` |
| `10` | `8.318` |
| `30` | `2.773` |
| `100` | `0.832` |

Required local density at the reference:

| M_BH | rho_seed,50 [kg/m^3] | overdensity vs canonical Galactic DM |
|---:|---:|---:|
| `1e10 kg` | `1.975e-16` | `3.69e5 x` |
| `1e11 kg` | `1.975e-15` | `3.69e6 x` |
| `2e11 kg` | `3.950e-15` | `7.39e6 x` |
| `5e11 kg` | `9.874e-15` | `1.85e7 x` |

Reference geometric abundance requirements:

| population proxy | N_seed,50 |
|---|---:|
| razor-cold co-orbital band | `1.07e4` |
| ultra-cold annulus | `3.44e4` |
| cold inner disk | `7.25e5` |
| warm broad disk | `1.45e7` |

At `M_BH=1e11 kg`, total mass is only about

```text
1.07e15 ... 1.45e18 kg.
```

Therefore:

```text
raw total seed mass budget: NOT the main bottleneck
normal Galactic halo abundance: FAIL
one isolated solar-bound seed: FAIL as generic solution
primordial solar-bound overdense seed population: OPEN but demanding.
```

A current OSIRIS-REx/Bennu distributed-DM benchmark near `1.1 AU` is approximately

```text
rho_DM <~3.3e-15 kg/m^3.
```

This is **not** a direct primordial exclusion. It is only a present-day retention benchmark and depends on the distribution model.

# 6. Current end matrix

| Bereich | Status |
|---|---|
| H+ strongest SK-IV project comparison | **FAIL** |
| H0 | **OPEN / not detected** |
| smooth-compensated Earth macro branch | no Reduced structure exclusion |
| electron sink | stabilized |
| nonlinear TF screening | calculated / recoupled |
| exact multicomponent Q_eq | **OPEN** |
| final Full-WDM species-resolved Mdot_BH(t) | **OPEN** |
| normal halo -> Earth delivery | **VERY STRONG FAIL** |
| normal halo -> protostellar cloud | **strongly negative** |
| disk gas drag | **FAIL / insufficient** |
| random/smooth GI pull-down | **strongly negative** |
| F3b generic multi-pass timing rescue | **FAIL** |
| F4 early embryo exchange | **PASS kinematic** |
| F5 direct 4-body exchange | **PASS conditional** |
| F6 normal Galactic seed abundance | **FAIL** |
| F6 primordial solar-bound overdense population | **OPEN** |
| full formation/delivery probability | **OPEN** |
| experimental BH detection | **NONE** |
| unique positive signature | **NONE** |

# 7. Open hard problems

```text
1. exact multicomponent Onsager/Maxwell-Stefan charge closure -> Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F7 physical origin/retention of the F6-required solar-bound seed population
6. realistic long-term post-capture survival / engulfment / settling
7. absolute formation/delivery probability.
```

# 8. Central files

- `README.md`
- `TEST_STATUS.md`
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `STAGE3_74_F3_HILL_MONTE_CARLO.md`
- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `STAGE3_76_F4_EARLY_EMBRYO_BOUND_SEED.md`
- `STAGE3_77_F5_RESTRICTED_4BODY_EXCHANGE_MC.md`
- `STAGE3_78_F6_POPULATION_WEIGHTED_FORMATION_GATE.md`

## Schlussstatus

```text
LOCAL FORMATION MECHANICS:
conditional exchange capture survives through F5.

POPULATION FOLDING:
F6 calculated.

NORMAL HALO POPULATION:
FAIL.

PRIMORDIAL SOLAR-BOUND OVERDENSE POPULATION:
OPEN / origin unexplained.

ABSOLUTE EARTH DELIVERY:
OPEN.

DIRECT BH EVIDENCE:
NONE.
```