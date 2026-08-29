# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Reduced Stack A1–A19 abgeschlossen; A20–A31 / Stage 3.72 weitergeführt; Formation bis Stage 3.78 / F6  
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
Formation/Delivery weiterhin OPEN.
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

## A19 – normaler Halo → fertige Erde

```text
DeltaE/E_inf ~1e-18 ... 5e-17
normal halo -> direct Earth capture: VERY STRONG FAIL.
```

## Stage 3.73 / F1 – Protosolar / co-moving Seed

```text
protoplanetary gas drag: insufficient
normal halo -> protostellar cloud: strongly negative
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

Für einen Seed bei `f=0.3 r_H`:

```text
prograde stable-capture kick   ~0.748 v_H
retrograde stable-capture kick ~0.376 v_H.
```

Ein enger Embryo–Embryo-Stressproxy erreicht diese Größenordnung.

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

Jeder Lauf besitzt einen gepaarten `M2=0`-Kontrolllauf.

### Kritische Korrektur

Ein capture-freundlicher Pilot mit `V~Omega R_H,mut` direkt am Perizentrum wurde **verworfen**. Final werden echte hyperbolische Flybys benutzt:

```text
V_p^2 = V_inf^2 + 2 G (M1+M2)/b.
```

### Persistenz bis 20 Omega^-1

`20 Omega^-1 ~3.18 yr` bei 1 AU.

| Ensemble | persistent stable | Status |
|---|---:|---|
| STRONG | `5/300 = 1.67%` | **PASS conditional** |
| BROAD | `3/300 = 1.00%` | **PASS conditional** |
| WEAK | `0/300` | **not found persistent** |

Persistente Captures besitzen etwa

```text
a_seed/r_H ~0.21 ... 0.58
```

während M2 nach dem Lauf typischerweise bereits `~55...150` mutual Hill radii entfernt ist.

Exchange-induced FULL-only body crossings:

```text
STRONG 4/300
BROAD  3/300
WEAK   0/300.
```

Bereits negative planetozentrische Energie beim Body-Eintritt:

```text
STRONG 2/4
BROAD  3/3.
```

Positive-E one-pass crossings bleiben trotz capture-freundlichem A19-Drag klar ungebunden.

```text
F5 local collisionless exchange mechanism: PASS conditionally
absolute formation probability: OPEN.
```

Zentrale Dateien:

- `STAGE3_77_F5_RESTRICTED_4BODY_EXCHANGE_MC.md`
- `stage3_77_f5_restricted_4body_exchange_mc.py`

## Stage 3.78 / F6 – Population-weighted Formation Gate

F6 faltet den F5-Kernel mit einer expliziten lokalen Seed-Population.

Da die primordial solar-bound Seed-Verteilung unbekannt ist, wird kein erfundener absoluter Wert benutzt. Stattdessen:

```text
lambda = N_enc K_F5 S_post n_seed V_H
P_delivery = 1 - exp(-lambda).
```

Für ein Ziel `P_*`:

```text
mu_H,req = n_seed V_H
         = -ln(1-P_*)/(N_enc K_F5 S_post).
```

### Referenz

```text
M1       = 0.03 M_E
K_F5     = 5/300 = 1.6667%
N_enc    = 10 relevant strong encounters
S_post   = 0.5 nuisance reference
P_*      = 0.5
r_H      = 465,012 km
V_H      = 4.212e26 m^3.
```

Damit:

```text
mu_H,50 = 8.318 eligible seeds per Hill volume.
```

Sensitivität:

| N_enc | mu_H,50 |
|---:|---:|
| `1` | `83.18` |
| `3` | `27.73` |
| `10` | `8.318` |
| `30` | `2.773` |
| `100` | `0.832` |

### Benötigte lokale Dichte

Bei `M1=0.03 M_E`:

| M_BH | rho_seed,50 [kg/m^3] | vs canonical Galactic DM |
|---:|---:|---:|
| `1e10 kg` | `1.975e-16` | `3.69e5 x` |
| `1e11 kg` | `1.975e-15` | `3.69e6 x` |
| `2e11 kg` | `3.950e-15` | `7.39e6 x` |
| `5e11 kg` | `9.874e-15` | `1.85e7 x` |

Damit:

```text
normal Galactic-halo abundance: FAIL for F5/F6 delivery.
```

Der überlebende Branch verlangt eine stark solar gebundene primordial overdense Seed-Population.

### Geometrische globale Seed-Abundance

Phase-mixed Referenzproxies bei `M1=0.03 M_E`, `N_enc=10`, `S_post=0.5`:

| Seed population | Hill duty proxy | N_seed,50 |
|---|---:|---:|
| razor-cold co-orbital band | `7.77e-4` | `1.07e4` |
| ultra-cold annulus | `2.42e-4` | `3.44e4` |
| cold inner disk | `1.15e-5` | `7.25e5` |
| warm broad disk | `5.74e-7` | `1.45e7` |

Bei `M_BH=1e11 kg` entspricht das Gesamtmassen von ungefähr

```text
1.07e15 ... 1.45e18 kg
```

und damit deutlich weniger als eine Millionstel Erdmasse. **Die rohe Gesamtmasse ist nicht der Hauptengpass.**

Der Engpass ist die Produktion von `~10^4...10^7` bereits solar gebundenen kompakten Seeds im richtigen terrestrischen Phasenraum.

### Present-day density benchmark

OSIRIS-REx/Bennu-Trajektoriendaten liefern für eine verteilte DM-Komponente bei `~1.1 AU` ungefähr

```text
rho_DM <~3.3e-15 kg/m^3.
```

Der F6-Referenzbedarf liegt damit bei `1e11 kg` unter, bei `2e11 kg` ungefähr auf und bei `5e11 kg` darüber.

Das ist **kein direkter primordialer Ausschluss**, weil F6 die frühe Solar-System-Population benötigt und heutige ephemeridenbasierte Dichtelimits nicht exakt auf eine frühe anisotrope kompakte Population abbilden.

F6 Schluss:

```text
population folding: CALCULATED
normal halo abundance: FAIL
one isolated seed as generic solution: FAIL
primordial solar-bound overdense population: OPEN but quantitatively demanding
absolute delivery probability: OPEN.
```

Zentrale F6-Dateien:

- `STAGE3_78_F6_POPULATION_WEIGHTED_FORMATION_GATE.md`
- `stage3_78_f6_population_weighted_formation_gate.py`

Nächster Formationstest:

```text
F7 = physical origin / retention of the required solar-bound seed population
-> pre-solar PBH/seed phase space
-> molecular-cloud / stellar-cluster capture
-> binary/multi-star exchange
-> adiabatic Solar-potential growth
-> retention through disk/embryo epoch
-> present-day survivor fraction
-> ephemeris / asteroid-tracking consistency.
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
| normal halo -> protostellar cloud | **strongly negative** |
| naked-seed disk gas drag | **FAIL / insufficient** |
| random/smooth GI pull-down | **strongly negative / inefficient** |
| F3b generic multi-pass timing rescue | **FAIL** |
| F4 correlated embryo exchange | **PASS kinematic** |
| F4 growth-assisted engulfment | **PASS conditional** |
| F5 direct restricted 4-body exchange | **PASS conditional** |
| F5 Strong persistent stable | **1.67% in defined encounter-conditioned ensemble** |
| F6 normal Galactic seed density | **FAIL by abundance** |
| F6 required solar-bound population | **~1e4...1e7 seeds in reference geometries** |
| F6 primordial overdense solar-bound population | **OPEN / origin unexplained** |
| full formation/delivery probability | **OPEN** |
| direkte experimentelle BH-Detektion | **NONE** |
| eindeutige positive Signatur | **NONE** |

# Was noch wirklich fehlt

```text
1. exact multicomponent Onsager/Maxwell-Stefan charge closure -> Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F7 physical origin/retention of the F6-required solar-bound seed population
6. realistic long-term post-capture survival / engulfment / settling
7. absolute formation/delivery probability.
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
- `STAGE3_71_A19_FORMATION_RECHECK.md`
- `STAGE3_70B_A18_REALDATA_AUDIT.md`

# Open Science / Projekt-Governance

Originale Texte/Dokumentation/Grafiken stehen – soweit nicht anders gekennzeichnet – unter **CC BY 4.0**; originaler Quellcode unter **MIT**.

Wissenschaftliche Prüfung, Reproduktion, Kritik und eigene abgeleitete Arbeiten sind ausdrücklich erlaubt. Der **offizielle Projektstand** (`main`, Stages, Releases) wird nur über dieses Repository und die Freigabe des Projektinhabers definiert.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Reduced Stack A1–A19 plus Stage 3.72 A20–A31 und Formation bis Stage 3.78/F6, Rheinland-Pfalz, Deutschland.