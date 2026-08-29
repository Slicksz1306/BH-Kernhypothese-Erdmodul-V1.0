# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 29.08.2026  
**Forschungsstand:** Reduced Stack A1–A19 abgeschlossen; A20–A31 / Stage 3.72 weitergeführt; Formation/Delivery bis Stage 3.80 / F8a; Multi-Gate Closure bis Stage 3.94; Toy-A35-Diagnostik bis Stage 3.95A

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
Formation/Delivery OPEN / stark origin-fine-tuned
F8a candidate regions != formation proof.
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

# 5. Stage 3.94 – Multi-Gate Closure F12 / A34 / H0

Stage 3.94 bündelt drei reduzierte, klar begrenzte Solverblöcke:

| Gate | Numerischer Status | Physische Aussagegrenze |
|---|---|---|
| F12 | Proxy-Arithmetik + Sweep **PASS** | physikalisches `P_zeta(k)` und echtes `f_NL` **OPEN** |
| A34 | stationäre Ein-Spezies-ODE **PASS** | finales multikomponentiges `Q_eq` **OPEN** |
| H0 | Massenkompensation + Sensitivitätsproxy **PASS** | eindeutige seismische H0-Vorhersage **OPEN** |

Die A34-Konzentrationslösung wurde gegen die Differentialgleichung selbst geprüft. Die Regressionen umfassen:

```text
Randbedingungen c(r_sink)=0 und c(R)=c_inf
normiertes ODE-Residuum auf 400 logarithmischen Radialpunkten
radiale Flusserhaltung dotN(r)=const.
Innenprofil-Regressionsschutz gegen die frühere exponentielle Überhöhung
```

Defaultlauf:

```text
maximales normiertes ODE-Residuum = 1.30e-9  (<1e-6)
relative Streuung von dotN(r)     = 2.61e-9  (<1e-6)
```

Aktueller reproduzierter Teststand:

```text
Stage 3.94 regression suite: 14/14 PASS
F8a regression suite:        12/12 PASS
Stage 3.95A diagnostic suite: 16/16 PASS
unittest discovery gesamt:   42/42 PASS
```

Dieser PASS bestätigt die mathematische Konsistenz der reduzierten stationären A34-Lösung innerhalb ihrer Eingaben und Randbedingungen. Er bestätigt weder eine vollständige multikomponentige Ladungs-Closure noch die SL/BH-Kernhypothese experimentell.

# 5a. Stage 3.95A – A35 Diagnostic Charge Theorem

Stage 3.95A untersucht zunaechst nur das ungeschirmte diagonale Zwei-Spezies-Toy-Modell

```text
h(x) = x/[1-exp(-x)]
f(N) = Z dotN_i(N) - dotN_e(N)
N    = Q/e.
```

Analytisch und numerisch regressionsgesichert gilt innerhalb dieses Modells:

```text
h'(x) > 0
f'(N) < 0
genau ein kontinuierlicher stabiler Toy-Nullpunkt.
```

Der Root ist keine physikalische Ladungsvorhersage. Bereits der freie Scan ueber `D_e/D_i`, `Z` und `T_e/T_i` zeigt seine starke Transportabhaengigkeit. Elektrische Leitfaehigkeit wird dabei nicht als vollstaendige Elektronen-Diffusionsclosure interpretiert.

Bei aeusserer Quasineutralitaet und gleichen Transportfaktoren wird der kritische neutrale Root unabhaengig vom Rootfinder durch

```text
(D_e/D_i)_crit = h(x_i)/h(x_e) = 132.876774528
```

reproduziert.

Die diskrete Ergaenzung verwendet

```text
N -> N-1 durch Elektronencapture
N -> N+Z durch Ionencapture
G^T P = 0 im stationaeren endlichen Zustandsraum.
```

Der Test prueft Normierung, Nichtnegativitaet, Generatorvorzeichen, Mastergleichungsresiduum und kleine Randwahrscheinlichkeit. Zusaetzlich schliessen die ersten beiden stationaeren Sprungmomente relativ mit etwa `1.58e-15` und `2.22e-14`. Mittelwert, Varianz und Modus sind fuer `N_max=100,150,200` konvergent. Die Kramers-Moyal/OU-Varianz `77.2372` liegt im Referenzfall etwa `0.286%` von der diskreten Varianz `77.4585` entfernt. Nichtganzzahlige mittlere Ionisation wird nicht als diskrete Sprungweite zugelassen.

`r_match=6.13e-8 m` ist in diesem Block der bisherige Bondi-/Materialradius als effektive A34-Matchingflaeche. Er ist bei `M=1e11 kg` etwa `4.13e8` Schwarzschildradien gross und wird nicht als Ereignishorizont oder mikroskopisch hergeleitete Capture-Flaeche bezeichnet.

Status:

```text
stabiler Driftfaktor und Monotonietheorem: PASS
kontinuierliche Toy-Root-Stabilitaet:       PASS
diskrete Markov-Diagnostik:                PASS
Generator-/Momenten-/Trunkierungschecks:    PASS
Stage-3.95A Tests:                          16/16 PASS
reales WDM-/Screening-/Sink-Q_eq:           OPEN
experimenteller BH-Nachweis:                NONE
```

# 6. Formation / Delivery

## F1 – Protosolar / co-moving Seed

```text
normal halo -> protostellar cloud: strongly negative as generic terrestrial delivery
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

Für `a_seed~0.3 r_H` muss Capture im adiabatischen Proxy ungefähr vor `M1~0.041 M_E` erfolgen, damit spätere Growth-assisted Engulfment bis `1 M_E` möglich bleibt.

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

```text
local collisionless embryo-exchange mechanism: PASS conditionally
generic formation probability: NOT ESTABLISHED.
```

## F6 – Population-weighted Formation Gate

```text
lambda = N_enc K_F5 S_post n_seed V_H
P_delivery = 1-exp(-lambda).
```

Referenz:

```text
M1=0.03 M_E
K_F5=5/300
N_enc=10
S_post=0.5
P_target=0.5
r_H=465,012 km
V_H=4.212e26 m^3
mu_H,50=8.318 seeds per Hill volume.
```

Required local density:

| M_BH | rho_seed,50 [kg/m^3] | overdensity vs canonical Galactic DM |
|---:|---:|---:|
| `1e10 kg` | `1.975e-16` | `3.69e5 x` |
| `1e11 kg` | `1.975e-15` | `3.69e6 x` |
| `2e11 kg` | `3.950e-15` | `7.39e6 x` |
| `5e11 kg` | `9.874e-15` | `1.85e7 x` |

Reference geometric abundance:

```text
N_seed,50 ~1.07e4 ... 1.45e7.
```

```text
raw total seed mass budget: NOT the main bottleneck
normal Galactic halo abundance: FAIL
one isolated solar-bound seed: FAIL as generic solution
primordial solar-bound overdense seed population: OPEN but demanding.
```

## F7 – Seed-Origin / Solar-Bound Phase-Space Gate

Canonical-halo adiabatic inheritance using maximally generous `f_PBH=f_s=1`, `rho_h=0.3 GeV/cm^3`, `sigma_h=200 km/s` gives at 1 AU:

```text
rho_bd(1 AU)=1.329e-24 kg/m^3.
```

| M_PBH | mu_H | shortfall vs 8.318 |
|---:|---:|---:|
| `1e10 kg` | `5.60e-8` | `1.49e8 x` |
| `1e11 kg` | `5.60e-9` | `1.49e9 x` |
| `2e11 kg` | `2.80e-9` | `2.97e9 x` |
| `5e11 kg` | `1.12e-9` | `7.43e9 x` |

```text
canonical Galactic-halo adiabatic inheritance @1 AU: FAIL.
```

A deliberately generous protostellar-cloud upper bound can produce wide captured low-mass PBHs, but after an already-overoptimistic point-Sun `q<1 AU` filter only about

```text
157, 15.7, 7.87, 3.15
```

inner candidates remain for `1e10,1e11,2e11,5e11 kg`, versus F6's best global requirement `~1.07e4`.

```text
wide protostellar PBH capture: PASS existence
terrestrial cold-seed supply: FAIL generous upper bound.
```

Standard giant-planet capture from a 200-km/s halo likewise misses the required instantaneous cold 1-AU density by roughly `1e9...1e10`.

Remaining F7 rescue:

```text
pre-existing co-moving cold PBH mini-halo/stream: OPEN exotic initial condition.
```

## F8a – Co-moving cold substructure semi-analytic scan

### Critical model correction

For a self-bound virialized mini-halo, `M_sub`, `r_core`, and `sigma_sub` are not independent. F8 therefore separates:

```text
mini:
Plummer self-bound halo; sigma derived from M and r_core

stream:
unbound Gaussian clump/finite stream; independent sigma,
with ballistic expansion + bulk drift during collapse.
```

For the Plummer reference:

```text
rho(r)=3M/(4 pi a^3) [1+r^2/a^2]^(-5/2)
sigma_1D^2(r)=GM/(6a) [1+r^2/a^2]^(-1/2)
```

At fixed scale radius:

```text
rho ~ M
sigma ~ M^(1/2)
Q=rho/sigma^3 ~ M^(-1/2).
```

Thus the original independent-`sigma` mini-halo grid and the suggested monotonic-`mu_H(M)` test were **REJECTED/CORRECTED**.

### F8 low-velocity gate

```text
Q_eff = rho/sigma^3 * exp[-v_rel^2/(2 sigma^2)]
rho_bound(1 AU) = [4/(3 sqrt(pi))] Q_eff (G M_sun/AU)^(3/2)
mu_H = rho_bound V_H/M_seed
PASS threshold: mu_H >= 8.318.
```

Required Q:

| Seedmass | Q_req [M_sun pc^-3 (km/s)^-3] |
|---:|---:|
| `1e10 kg` | `0.146794` |
| `1e11 kg` | `1.46794` |
| `2e11 kg` | `2.93589` |
| `5e11 kg` | `7.33972` |

Bulk co-motion is explicit. Over `0.06 Myr`, `1 km/s` corresponds to a displacement of about `12,650 AU`, so density alone cannot rescue a non-co-moving compact structure.

### Regression suite

`test_stage3_80_f8_substructure_scan.py`:

```text
12/12 PASS.
```

Tests:

1. Plummer `rho proportional M`.
2. virial `sigma^2 proportional M`.
3. `Q proportional M^-1/2` at fixed scale radius.
4. F6/F7 Q regression: `1e11 kg -> 1.46794 M_sun pc^-3 (km/s)^-3`.
5. bulk-velocity suppression.
6. stream expansion lowers local density.
7. `rho_required -> mu_H` roundtrip reproduces `8.318`.

### Canonical F8a example grid

```text
25,920 rows
M_sub=1e-15...1e-4 M_sun
r_core=1e-3...1e3 AU
stream sigma=0.01...1 km/s
hybrid v_rel grid
4 seed masses
medium cluster stress model.
```

Results:

```text
mini phase-space pass: 702 grid rows
mini Stage-1 candidates: 390
mini Stage-1 + unchanged present-day density benchmark: 0
stream phase-space pass: 5391
stream collapse-overlap Stage-1 candidates: 692.
```

These counts are grid cells, **not astrophysical probabilities**.

The compact-seed mass fraction is explicit:

```text
f_seed_required = mu_H,50 / mu_H(f_seed=1).
```

Stage-1 requires `f_seed_required<=1`.

### F8a conclusion

```text
semi-analytic phase-space existence screen: PASS / candidates found
self-bound mini-halo candidate region: FOUND conditionally
finite-stream collapse-overlap region: FOUND conditionally
mini-halo cluster survival: PARTIAL stress proxy
stream post-capture 1e6...1e7 yr retention: OPEN
unchanged present-day retention: tension/model-dependent
final F8 physical origin/retention: OPEN
absolute Earth delivery: OPEN
experimental BH evidence: NONE.
```

The F7 origin rescue is therefore **not immediately empty in parameter space**, but F8a does not establish that such a substructure forms, survives the natal cluster/Solar collapse, or remains observationally allowed.

# 7. Current end matrix

| Bereich | Status |
|---|---|
| H+ strongest SK-IV project comparison | **FAIL** |
| H0 | **OPEN / not detected** |
| smooth-compensated Earth macro branch | no Reduced structure exclusion |
| electron sink | stabilized |
| nonlinear TF screening | calculated / recoupled |
| A34 reduced stationary ODE + residual/flux regressions | **14/14 Stage-3.94 suite PASS** |
| A35 diagonal Toy-Monotonietheorem | **PASS in Stage 3.95A reference model** |
| A35 diskrete Ladungsdiagnostik | **16/16 Stage-3.95A suite PASS** |
| exact multicomponent Q_eq | **OPEN** |
| final Full-WDM species-resolved Mdot_BH(t) | **OPEN** |
| normal halo -> Earth delivery | **VERY STRONG FAIL** |
| disk gas drag | **FAIL / insufficient** |
| random/smooth GI pull-down | **strongly negative** |
| F3b generic multi-pass timing rescue | **FAIL** |
| F4 early embryo exchange | **PASS kinematic** |
| F5 direct 4-body exchange | **PASS conditional** |
| F6 normal Galactic seed abundance | **FAIL** |
| F7 canonical-halo origin @1 AU | **FAIL by ~1e8...1e10** |
| F7 protostellar wide PBH capture | **PASS existence / insufficient terrestrially** |
| F7 standard giant-planet halo capture | **FAIL** |
| F8a virialized cold-substructure phase-space | **PASS existence screen / candidates found** |
| F8a regression suite | **12/12 PASS** |
| complete unittest discovery | **42/42 PASS** |
| F8a cluster survival | **PARTIAL reduced proxy** |
| F8 stream long-term solar retention | **OPEN** |
| F8 present-day compatibility | **OPEN / evolution required** |
| final F8 physical viability | **OPEN** |
| full formation/delivery probability | **OPEN / strongly fine-tuned** |
| experimental BH detection | **NONE** |
| unique positive signature | **NONE** |

# 8. Open hard problems

```text
1. Stage 3.95B: ionischer Stofftransport + elektronischer WDM-Transport + Screening + Sink-Capture -> reales Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F8b successive stellar-encounter / cluster-disruption Monte-Carlo
6. F8c Proto-Sun + time-dependent gas/Solar-potential N-body validation
7. realistic long-term post-capture survival / engulfment / settling
8. absolute formation/delivery probability.
```

# 9. Central files

- `README.md`
- `TEST_STATUS.md`
- `STAGE3_94_MULTI_GATE_CLOSURE.md`
- `stage3_94_multi_gate_closure.py`
- `test_stage3_94_multi_gate_closure.py`
- `STAGE3_95A_A35_DIAGNOSTIC_CHARGE_THEOREM.md`
- `stage3_95a_a35_diagnostic_charge_theorem.py`
- `test_stage3_95a_a35_diagnostic_charge_theorem.py`
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `STAGE3_74_F3_HILL_MONTE_CARLO.md`
- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `STAGE3_76_F4_EARLY_EMBRYO_BOUND_SEED.md`
- `STAGE3_77_F5_RESTRICTED_4BODY_EXCHANGE_MC.md`
- `STAGE3_78_F6_POPULATION_WEIGHTED_FORMATION_GATE.md`
- `STAGE3_79_F7_SEED_ORIGIN_PHASE_SPACE_GATE.md`
- `STAGE3_80_F8_SUBSTRUCTURE_SCAN.md`
- `stage3_80_f8_substructure_scan.py`
- `test_stage3_80_f8_substructure_scan.py`
- `results/f8_example_candidates.csv`
- `results/f8_example_summary.json`

## Schlussstatus

```text
LOCAL FORMATION MECHANICS:
conditional exchange capture survives through F5.

POPULATION FOLDING:
F6 calculated.

STANDARD GALACTIC ORIGIN CHANNELS:
FAIL for required terrestrial phase space in F7.

F8a COLD-SUBSTRUCTURE PHASE-SPACE SCREEN:
PASS as existence screen; candidate cells found.

F8 CLUSTER/SOLAR-FORMATION SURVIVAL:
OPEN.

ABSOLUTE EARTH DELIVERY:
OPEN / strongly fine-tuned.

DIRECT BH EVIDENCE:
NONE.
```
