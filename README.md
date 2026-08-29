# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Reduced Stack A1–A19 abgeschlossen; A20–A31 / Stage 3.72 weitergeführt; Formation bis Stage 3.80 / F8a  
**Stand:** 29.08.2026  
**Erstveröffentlichung Erdmodul V1.0:** 23.08.2026

> `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs-/Prioritätsarchiv. Neue Rechnungen werden versioniert in Markdown und reproduzierbaren Python-Skripten fortgeschrieben.

## Wissenschaftliche Aussagegrenze

Die **SL/BH-Kernhypothese Erdmodul** ist ein quantitativer, reproduzierbarer und falsifizierbarer **theoretischer Forschungsentwurf**. Sie ist **kein experimenteller Nachweis** und derzeit **keine etablierte physikalische Theorie**.

Aktuell gilt:

```text
keine direkte Detektion eines Erdzentrum-BH
keine eindeutige positive H0-Signatur
H+ negativ im stärksten projektintern verwendeten SK-IV-Hochenergievergleich
H0 OPEN / nicht nachgewiesen
mehrere interne Solver-/Regressionstests bestanden
mehrere frühere Annahmen korrigiert oder verworfen
Formation/Delivery weiterhin OPEN und stark origin-fine-tuned
F8a findet nur konditionale cold-substructure Kandidaten, keinen Formation-Nachweis.
```

## Branches

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

### H+

Projekt-Hawking/Greybody-Proxy im Band `25.29...31.29 MeV`:

```text
~0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Gegen den stärksten publizierten SK-IV-Binconstraint bleibt H+ in der **projektinternen Reinterpretation FAIL**. Dies ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

### H0

```text
P_Hawking = 0
H0 = OPEN / nicht nachgewiesen.
```

H0 muss Full-WDM-Akkretion, Formation/Delivery und eine eindeutige Real-Data-Signatur bestehen.

# Aktiver Erdbranch

Die starke Zentralmassen-/Hard-Cavity-Variante ist verworfen. Aktiv ist nur der kleine **smooth-compensated Branch**.

PREM-Zentrumsreferenz:

```text
rho_c      ~13.08848 g/cm3
c_eff      ~10.4355 km/s
Kappa_S    ~1.4253 TPa
Pressure   ~363.852 GPa
dK/dP      ~2.356.
```

Bei `M=1e11 kg`:

```text
r_B ~6.13e-8 m
r_s ~1.49e-16 m.
```

Die reduzierten Makrotests liefern für diesen kleinen Branch keinen eigenen robusten Struktur-Ausschluss. Das ist Modellkompatibilität innerhalb der getesteten Proxies, keine Evidenz für einen BH.

# Reduced Stack A1–A19

```text
Schwarzschild-Dirac Regressionen: PASS
Proton @1e11 kg: ~0.9503 classical
Fe-56 @1e11 kg: ~0.99754 classical
Ni-58 @1e11 kg: ~0.99646 classical
large coherent Fe/Ni wave suppression: NOT FOUND
repeated-encounter recycling included
naive local Kn~1 = permanent escape: REJECTED
A13/A13b relativistic outer supply: PARTIAL CALCULATED
A14 dense-core screening: PARTIAL
A15 reduced throughput >=1e11 kg: processing-capable in tested stack
A16 hard 47-TW total-budget pretest: NO EXCLUSION
A17 microscopic near-zone seismics: not a useful direct channel
A18 H+ strongest-SK-IV project comparison: FAIL
A19 normal halo -> Earth capture: VERY STRONG FAIL.
```

# Stage 3.72 – A20–A31 Charge / WDM-Transport

```text
electron Dirac sink flux-direct: stabilized
nonlinear Thomas-Fermi screening: calculated and recoupled
collective charge response: much faster than hydrodynamic evolution
independent naive ion/electron n*v*sigma current model: REJECTED
ambipolar/electronic transport hierarchy: strongly constrained
exact Q_eq: OPEN
```

Verbleibender Charge-Engpass:

```text
multicomponent Onsager / Maxwell-Stefan mobility matrix
+ thermodynamic chemical-potential derivatives
+ sink-boundary coupling.
```

Zentrale Dateien:

- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `stage3_72_a31_ambipolar_mobility_gate.py`

# Formation / Delivery

## A19 / F1 – Standard-Halo-Vorstufen

```text
normal halo -> direct Earth: VERY STRONG FAIL
protoplanetary gas drag: insufficient
normal halo -> protostellar cloud: strongly negative as generic terrestrial delivery
already solar-bound, dynamically cold seed: OPEN initial condition.
```

## Stage 3.73 / F2 – Hill / Pull-down Energy Gate

```text
v_inf,max = sqrt(2 G DeltaM/r)
          = sqrt(6 delta/f) v_H.
```

```text
temporary Hill capture: dynamically allowed
static permanent capture without potential evolution: FAIL
smooth terrestrial pull-down: FAIL as generic channel
giant-impact impulsive jump: PASS as local kinematic existence test
absolute probability: OPEN.
```

## Stage 3.74 / F3 – Adaptive Hill-Monte-Carlo + Jacobi Closure

Konservativer zeitgewichteter Pull-down-Anteil bei `r>=0.1 r_H`:

| DeltaM/M | sigma=0.0 | sigma=0.1 | sigma=0.3 | Status |
|---:|---:|---:|---:|---|
| `0.01` | `0` | `0` | `0` | **FAIL in sampled gate** |
| `0.03` | `0` | `0` | `0` | **FAIL in sampled gate** |
| `0.10` | `0.0352%` | `0.0725%` | `0.0722%` | **PASS existence / inefficient** |
| `0.30` | `6.806%` | `6.302%` | `5.653%` | **PASS conditional channel** |

Ein früher fixed-step-RK4-Resultat bei tiefen Encounters wurde wegen Jacobi-Drift verworfen. Finaler DOP853-Solver: PASS an den definierten Regressionen.

## Stage 3.75 / F3b – Multi-Pass / Residence Timing

```text
F3 first passage ~35.3 d
mean Earth TCO ~286 d
2020 CD3 median ~4 yr
extreme clone tail ~100 yr.
```

```text
multi-pass residence enhancement: PASS
multi-pass as generic random-impact timing rescue: FAIL
absolute delivery: OPEN.
```

## Stage 3.76 / F4 – Early permanent embryo-bound Seed

Bei `f=0.3 r_H`:

```text
prograde stable-capture kick    ~0.748 v_H
retrograde stable-capture kick  ~0.376 v_H.
```

Enge Embryo–Embryo-Begegnungen besitzen ausreichend differential impulse als kinematischen Capture-Gate.

Im adiabatischen Wachstumsgrenzfall:

```text
a_seed ∝ 1/M_p
R_p    ∝ M_p^(1/3)
=> a_seed/R_p ∝ M_p^(-4/3).
```

Damit kann ein früh gebundener Seed durch Wachstum später body-crossing werden.

```text
collisionless early permanent binding: PASS kinematic existence
stable embryo-bound phase space: PASS
growth-assisted engulfment: PASS conditional
post-engulfment damping: feasibility only
absolute probability: OPEN.
```

## Stage 3.77 / F5 – Direct restricted 4-body Exchange Monte-Carlo

Direkte Newtonsche Integration:

```text
Sun + Proto-Earth M1 + second embryo M2 + massless seed.
```

Jeder Lauf besitzt einen gepaarten `M2=0`-Kontrolllauf. Ein capture-freundlicher Pilot mit zu kleiner Perizentrumgeschwindigkeit wurde verworfen; final:

```text
V_p^2 = V_inf^2 + 2 G (M1+M2)/b.
```

Persistenz bis `20 Omega^-1 ~3.18 yr`:

| Ensemble | persistent stable | Status |
|---|---:|---|
| STRONG | `5/300 = 1.67%` | **PASS conditional** |
| BROAD | `3/300 = 1.00%` | **PASS conditional** |
| WEAK | `0/300` | **not found persistent** |

Persistente Captures besitzen etwa

```text
a_seed/r_H ~0.21 ... 0.58.
```

Exchange-induced FULL-only body crossings:

```text
STRONG 4/300
BROAD  3/300
WEAK   0/300.
```

Davon sind `2/4` STRONG und `3/3` BROAD beim Body-Eintritt bereits planetozentrisch gebunden. Positive-E one-pass crossings bleiben trotz capture-freundlichem A19-Drag ungebunden.

```text
F5 local collisionless exchange mechanism: PASS conditionally
absolute formation probability: OPEN.
```

Zentrale Dateien:

- `STAGE3_77_F5_RESTRICTED_4BODY_EXCHANGE_MC.md`
- `stage3_77_f5_restricted_4body_exchange_mc.py`

## Stage 3.78 / F6 – Population-weighted Formation Gate

F6 faltet den F5-Kernel mit einer lokalen Seed-Population:

```text
lambda = N_enc K_F5 S_post n_seed V_H
P_delivery = 1 - exp(-lambda).
```

Referenz:

```text
M1       = 0.03 M_E
K_F5     = 5/300
N_enc    = 10
S_post   = 0.5
P_*      = 0.5
r_H      = 465,012 km
V_H      = 4.212e26 m^3
mu_H,50  = 8.318 eligible seeds per Hill volume.
```

Benötigte lokale Dichte:

| M_BH | rho_seed,50 [kg/m^3] | vs canonical Galactic DM |
|---:|---:|---:|
| `1e10 kg` | `1.975e-16` | `3.69e5 x` |
| `1e11 kg` | `1.975e-15` | `3.69e6 x` |
| `2e11 kg` | `3.950e-15` | `7.39e6 x` |
| `5e11 kg` | `9.874e-15` | `1.85e7 x` |

Phase-mixed Referenzgeometrien erfordern global ungefähr

```text
~1.07e4 ... 1.45e7 solar-bound eligible seeds.
```

Die Gesamtmasse davon ist klein; der Engpass ist die lokale Phasenraumdichte und Stückzahl.

```text
population folding: CALCULATED
normal halo abundance: FAIL
one isolated seed as generic solution: FAIL
primordial solar-bound overdense population: OPEN but quantitatively demanding.
```

Zentrale Dateien:

- `STAGE3_78_F6_POPULATION_WEIGHTED_FORMATION_GATE.md`
- `stage3_78_f6_population_weighted_formation_gate.py`

## Stage 3.79 / F7 – Seed-Origin / Solar-Bound Phase-Space Gate

F7 testet, ob Standard-Galactic channels die F6-Anfangsbedingung tatsächlich erzeugen können.

### Canonical-halo adiabatic inheritance

Mit capture-freundlich `f_PBH=f_s=1`, `rho_h=0.3 GeV/cm^3`, `sigma_h=200 km/s` folgt bei 1 AU:

```text
rho_bd(1 AU) = 1.329e-24 kg/m^3.
```

| M_PBH | mu_H,adiabatic | shortfall vs 8.318 |
|---:|---:|---:|
| `1e10 kg` | `5.60e-8` | `1.49e8 x` |
| `1e11 kg` | `5.60e-9` | `1.49e9 x` |
| `2e11 kg` | `2.80e-9` | `2.97e9 x` |
| `5e11 kg` | `1.12e-9` | `7.43e9 x` |

```text
standard Galactic-halo adiabatic inheritance @1 AU: FAIL.
```

### Protostellar-cloud generous upper bound

Selbst wenn jeder langsame Cloud-Entrant eingefangen wird und zusätzlich jeder durch eine fertige Punkt-Sonne auf `q<1 AU` fokussierte Fall als perfekter terrestrial candidate zählt:

| M_PBH | maximaler inner-1-AU candidate upper bound |
|---:|---:|
| `1e10 kg` | `157` |
| `1e11 kg` | `15.7` |
| `2e11 kg` | `7.87` |
| `5e11 kg` | `3.15` |

gegen F6s günstigstes globales Minimum `N_seed,min ~1.07e4`.

```text
wide cloud capture: possible
terrestrial cold-seed supply: FAIL even in generous upper bound.
```

### Giant-planet capture from standard halo

Für den phase-space-mixed Jupiter/Saturn-Pfad bei `sigma=200 km/s`:

```text
n_bound(1 AU)/n_halo ~4.50e-4.
```

F6 Hill occupancy bleibt um ungefähr `1e9...1e10` zu klein.

```text
standard-halo giant-planet capture as F6 source: FAIL.
```

### F7-Schluss

```text
standard Galactic origin channels: FAIL for terrestrial F6 phase space
wide solar capture of very low-mass PBHs: possible but insufficient
pre-existing primordial co-moving cold dark mini-halo/stream: OPEN exotic initial condition
absolute Earth delivery: OPEN / strongly origin-fine-tuned.
```

Zentrale F7-Dateien:

- `STAGE3_79_F7_SEED_ORIGIN_PHASE_SPACE_GATE.md`
- `stage3_79_f7_seed_origin_phase_space_gate.py`

## Stage 3.80 / F8a – Co-moving cold substructure scan

F8 testet den letzten F7-Origin-Rescue. Eine zentrale Korrektur ist eingebaut:

```text
self-bound virialized mini-halo:
M_sub and r_core free; sigma derived from the profile

unbound cold stream/clump:
M_sub, r_core, sigma_sub and v_rel may be independent,
but ballistic expansion and bulk drift are explicit.
```

Für einen Plummer-Mini-Halo:

```text
rho(r) = 3M/(4 pi a^3) [1+r^2/a^2]^(-5/2)
sigma_1D^2(r) = GM/(6a) [1+r^2/a^2]^(-1/2).
```

Damit gilt bei festem `a`:

```text
rho ~ M
sigma ~ M^(1/2)
Q = rho/sigma^3 ~ M^(-1/2).
```

Ein unabhängiger Scan von `M_sub`, `r_core` und `sigma_sub` für einen selbstgebundenen Halo wurde deshalb verworfen.

### Low-velocity phase-space Gate

```text
Q_eff = rho/sigma^3 * exp[-v_rel^2/(2 sigma^2)]

rho_bound(1 AU)
= [4/(3 sqrt(pi))] Q_eff (G M_sun/AU)^(3/2)

mu_H = rho_bound V_H / M_seed.
```

F6-PASS-Schwelle:

```text
mu_H >= 8.318.
```

Erforderliche `Q`-Werte:

| Seedmasse | Q_req [M_sun pc^-3 (km/s)^-3] |
|---:|---:|
| `1e10 kg` | `0.146794` |
| `1e11 kg` | `1.46794` |
| `2e11 kg` | `2.93589` |
| `5e11 kg` | `7.33972` |

Der Bulk-Offset ist explizit: über `0.06 Myr` verschiebt `v_rel=1 km/s` eine Substruktur um ungefähr `12,650 AU`. Hohe Dichte allein genügt daher nicht; echte Co-Motion ist erforderlich.

### Canonical F8a example grid

```text
25,920 rows
M_sub = 1e-15 ... 1e-4 M_sun
r_core = 1e-3 ... 1e3 AU
stream sigma = 0.01 ... 1 km/s
hybrid v_rel grid
4 seed masses
medium cluster stress model.
```

Resultat:

```text
mini-halo phase-space pass rows: 702
mini-halo Stage-1 candidate rows: 390
mini-halo Stage-1 + unchanged present-day density benchmark: 0
stream phase-space pass rows: 5391
stream collapse-overlap Stage-1 candidate rows: 692.
```

Diese Zähler sind **Grid-Zellen, keine astrophysikalischen Wahrscheinlichkeiten**.

`f_seed_required = mu_H,50/mu_H(f_seed=1)` ist explizit ausgegeben. Damit wird nicht mehr stillschweigend angenommen, dass 100% einer generischen Dark-Substructure aus kompakten Seeds bestehen.

### F8a Status

```text
Plummer/Virial regression tests: 7/7 PASS
self-consistent mini-halo phase-space candidates: FOUND
finite stream collapse-overlap candidates: FOUND
mini-halo cluster survival: PARTIAL reduced proxy
stream solar-bound 1e6...1e7 yr retention: OPEN
unchanged present-day retention: tension/model-dependent
final F8: OPEN.
```

Der Parameterraum ist also **nicht schon im semi-analytischen Phase-Space-Screen leer**. Das ist aber noch kein physikalischer Ursprungserfolg. F8b/F8c müssen zeigen, ob die Kandidaten successive Cluster-Encounters, Sonnenbildung und spätere Entwicklung wirklich überleben.

Zentrale F8a-Dateien:

- `STAGE3_80_F8_SUBSTRUCTURE_SCAN.md`
- `stage3_80_f8_substructure_scan.py`
- `test_stage3_80_f8_substructure_scan.py`
- `results/f8_example_candidates.csv`
- `results/f8_example_summary.json`
- GitHub Issue `#35`.

Nächster Formationstest:

```text
F8b = Monte-Carlo cluster disruption of the F8a candidate region
-> successive stellar encounters
-> evolving binding/profile
-> low/med/high cluster histories
-> P_survive(t=1e6...1e7 yr)

F8c = Proto-Sun + time-dependent gas/Solar potential + candidate substructure N-body validation.
```

# Aktuelle Endmatrix

| Bereich | Status |
|---|---|
| H+ strongest SK-IV project comparison | **FAIL** |
| H0 | **OPEN / not detected** |
| smooth-compensated Earth macro branch | kein eigener Reduced-Strukturausschluss |
| Wave-Capture Proton/Fe/Ni | weitgehend berechnet |
| electron sink | stabilisiert |
| nonlinear TF screening | berechnet / recoupled |
| exact multicomponent Q_eq | **OPEN** |
| final species-resolved Full-WDM Mdot_BH(t) | **OPEN** |
| normal halo -> Earth delivery | **VERY STRONG FAIL** |
| naked-seed disk gas drag | **FAIL / insufficient** |
| random/smooth GI pull-down | **strongly negative / inefficient** |
| F3b generic multi-pass timing rescue | **FAIL** |
| F4 correlated embryo exchange | **PASS kinematic** |
| F4 growth-assisted engulfment | **PASS conditional** |
| F5 direct restricted 4-body exchange | **PASS conditional** |
| F5 Strong persistent stable | **1.67% in defined encounter-conditioned ensemble** |
| F6 normal Galactic seed density | **FAIL by abundance** |
| F6 required solar-bound population | **~1e4...1e7 seeds in reference geometries** |
| F7 canonical-halo origin @1 AU | **FAIL by ~1e8...1e10 phase-space** |
| F7 protostellar wide PBH capture | **PASS existence / insufficient terrestrially** |
| F7 standard giant-planet halo capture @1 AU | **FAIL** |
| F8a virialized cold-substructure phase-space screen | **PASS existence / candidates found** |
| F8a mini-halo cluster survival | **PARTIAL reduced proxy** |
| F8a stream long-term solar retention | **OPEN** |
| F8 unchanged present-day compatibility | **OPEN / evolution required** |
| final F8 physical origin/retention | **OPEN** |
| full formation/delivery probability | **OPEN / strongly fine-tuned** |
| direkte experimentelle BH-Detektion | **NONE** |
| eindeutige positive Signatur | **NONE** |

# Was noch wirklich fehlt

```text
1. exact multicomponent Onsager/Maxwell-Stefan charge closure -> Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F8b successive cluster-encounter Monte-Carlo for candidate substructures
6. F8c Proto-Sun + time-dependent gas/Solar-potential N-body validation
7. realistic long-term post-capture survival / engulfment / settling
8. absolute formation/delivery probability.
```

# Zentrale Statusdateien

- `TEST_STATUS.md`
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `STAGE3_74_F3_HILL_MONTE_CARLO.md`
- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `STAGE3_76_F4_EARLY_EMBRYO_BOUND_SEED.md`
- `STAGE3_77_F5_RESTRICTED_4BODY_EXCHANGE_MC.md`
- `STAGE3_78_F6_POPULATION_WEIGHTED_FORMATION_GATE.md`
- `STAGE3_79_F7_SEED_ORIGIN_PHASE_SPACE_GATE.md`
- `STAGE3_80_F8_SUBSTRUCTURE_SCAN.md`
- `STAGE3_71_A19_FORMATION_RECHECK.md`
- `STAGE3_70B_A18_REALDATA_AUDIT.md`

# Open Science / Projekt-Governance

Originale Texte/Dokumentation/Grafiken stehen – soweit nicht anders gekennzeichnet – unter **CC BY 4.0**; originaler Quellcode unter **MIT**.

Wissenschaftliche Prüfung, Reproduktion, Kritik und eigene abgeleitete Arbeiten sind ausdrücklich erlaubt. Der **offizielle Projektstand** (`main`, Stages, Releases) wird nur über dieses Repository und die Freigabe des Projektinhabers definiert.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Reduced Stack A1–A19 plus Stage 3.72 A20–A31 und Formation bis Stage 3.80/F8a, Rheinland-Pfalz, Deutschland.
