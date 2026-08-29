# Stage 3.78 / F6 – Population-weighted formation gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** F5 LOCAL KERNEL SURVIVES / REQUIRED SOLAR-BOUND SEED OVERDENSITY QUANTIFIED / NORMAL HALO POPULATION FAIL / ABSOLUTE PRIMORDIAL SEED ABUNDANCE OPEN

## Ziel

F5 hat einen lokalen, konditionalen dynamischen Kern geliefert:

```text
already solar-bound Hill-region seed
+ strong hyperbolic embryo encounter
=> persistent Proto-Earth capture possible.
```

Im STRONG-Ensemble blieben

```text
5/300 = 1.67%
```

bis `20 Omega^-1 ~3.18 yr` stabil.

F6 faltet diesen Kernel erstmals mit einer expliziten Seed-Population. Da der physische Ursprung und die helioszentrische `a,e,i`-Verteilung des Seeds nicht bekannt sind, wäre ein einzelner absoluter `P_delivery`-Wert erfunden. F6 invertiert deshalb das Problem:

```text
Welche lokale Seed-Belegung bzw. wie viele primordial solar-bound Seeds
werden benötigt, um eine vorgegebene Earth-delivery probability zu erreichen?
```

## Literaturanker für die Embryophase

Terrestrische Planetenbildung liefert nach Runaway/Oligarchic Growth typischerweise mehrere zehn bis ungefähr hundert lunar- bis marsgroße Embryonen. Charakteristische Anfangsabstände liegen grob bei `5...10` mutual Hill radii; die anschließende chaotische Giant-Impact-Phase dauert ungefähr `10...100 Myr`.

Relevante Standardanker:

- Chambers et al., *Icarus* 119, 261 (1996), DOI `10.1006/icar.1996.0019`: multi-planet systems mit Abständen kleiner als ungefähr zehn mutual Hill radii werden instabil und entwickeln enge Begegnungen.
- Raymond et al., *Annual Review of Earth and Planetary Sciences* / terrestrial-formation reviews: mehrere zehn bis ungefähr hundert Embryonen nach oligarchischem Wachstum; Giant-Impact-Phase über ungefähr `10...100 Myr`.
- Fang & Deng, *MNRAS* 496, 3781 (2020), DOI `10.1093/mnras/staa1724`: terrestrische N-body-Simulationen zeigen wiederholte extreme Proto-Planet-Begegnungen; der genaue Encounter-Count ist stark formationshistorienabhängig.

F6 setzt deshalb **keinen** literaturseitig angeblich exakt bekannten Encounter-Count ein. `N_enc` bleibt ein expliziter Stressparameter.

## 1. Population-weighted Poisson gate

Sei

```text
n_seed = lokale Number density der eligible solar-bound cold seeds
V_H    = Hill-sphere volume des Proto-Earth-Embryos
mu_H   = n_seed V_H
K_F5   = conditional F5 persistent-capture kernel
S_post = post-capture survival/engulfment factor
N_enc  = Anzahl relevanter F5-kompatibler Embryo-Begegnungen.
```

Dann ist die erwartete Zahl erfolgreicher Delivery-Ereignisse im einfachen independent-event Nullmodell

```text
lambda = N_enc K_F5 S_post mu_H
       = N_enc K_F5 S_post n_seed V_H.
```

und

```text
P_delivery = 1 - exp(-lambda).
```

Für ein Ziel `P_*` folgt direkt

```text
mu_H,req = -ln(1-P_*)/(N_enc K_F5 S_post).
```

Der große Vorteil: Diese Gleichung ist unabhängig von einer frei erfundenen globalen Seed-Verteilung.

## 2. Referenzwahl

F6-Referenz:

```text
M1       = 0.03 M_E
K_F5     = 5/300 = 0.016667
N_enc    = 10
S_post   = 0.5
P_*      = 0.5.
```

`S_post=0.5` ist **kein gemessener Wert**, sondern ein transparenter Nuisance-Referenzpunkt zwischen vollständigem Verlust und perfektem Überleben.

Die Wahl `M1=0.03 M_E` ist formationsphysikalisch relevant: F4 zeigte für einen typischen Capture-Orbit bei `a_seed~0.3 r_H`, dass adiabatisches Growth-assisted Engulfment nur funktioniert, wenn der Capture ungefähr vor

```text
M1 ~0.041 M_E
```

stattfindet. Ein viel größerer Embryo würde zwar ein größeres Hill-Volumen besitzen, aber den Growth-engulfment Vorteil verlieren.

Für `M1=0.03 M_E`:

```text
r_H = 4.650e8 m = 465,012 km
V_H = 4.212e26 m^3.
```

## 3. Hauptergebnis – benötigte Hill-Belegung

Mit der Referenzwahl:

```text
mu_H,50 = ln(2)/(10 * 0.016667 * 0.5)
        = 8.318.
```

Das heißt:

```text
Für 50% Delivery braucht der Referenzbranch im Mittel
~8.3 eligible Seeds pro Proto-Earth-Hill-Volumen
an den relevanten Encounter-Epochen.
```

Das ist der zentrale F6-Befund.

Ein einzelner zufällig solar gebundener Seed reicht damit nicht annähernd aus, solange die Hill-Duty-Cycle klein ist.

### Sensitivität gegen Encounter Count

Bei `S_post=0.5` und demselben F5-Kernel:

| N_enc | benötigte mittlere Hill-Belegung für 50% |
|---:|---:|
| `1` | `83.18` Seeds |
| `3` | `27.73` |
| `10` | `8.318` |
| `30` | `2.773` |
| `100` | `0.832` |

Selbst **100** vollständig F5-kompatible Strong-Encounters würden also für 50% Delivery noch ungefähr einen eligible Seed pro Hill-Volumen verlangen.

## 4. Lokale Number- und Mass-density

Für die Referenz gilt

```text
n_seed,50 = 1.975e-26 m^-3.
```

Die entsprechende mittlere Seed-Separation ist ungefähr

```text
n^(-1/3) ~3.70e8 m
          ~0.00247 AU
          ~370,000 km.
```

Die erforderliche Massendichte skaliert linear mit der Seed-/BH-Masse:

| M_BH | rho_seed,50 [kg/m^3] | Overdensity vs 0.3 GeV/cm^3 Galactic DM |
|---:|---:|---:|
| `1e10 kg` | `1.975e-16` | `3.69e5 x` |
| `1e11 kg` | `1.975e-15` | `3.69e6 x` |
| `2e11 kg` | `3.950e-15` | `7.39e6 x` |
| `5e11 kg` | `9.874e-15` | `1.85e7 x` |

Damit ist F6 eindeutig:

```text
normal Galactic-halo density cannot supply the F5 branch.
```

Das ist konsistent mit A19/F1. Der überlebende Formation-Branch benötigt eine **stark solar gebundene primordial overdense Population**, nicht normale Halo-Dark-Matter-Flux.

## 5. Vergleich mit heutigen Solar-System-DM-Limits

Tsai et al., JCAP 02 (2024) 029, DOI `10.1088/1475-7516/2024/02/029`, benutzen OSIRIS-REx/Bennu-Trajektoriendaten und finden in der Nähe von `~1.1 AU` ungefähr

```text
rho_DM <~3.3e-15 kg/m^3
       ~6e6 times the canonical Galactic DM density.
```

Dieser Vergleich ist interessant:

```text
M_BH=1e10 kg  -> F6 reference density well below that benchmark
M_BH=1e11 kg  -> ~0.60 of that benchmark
M_BH=2e11 kg  -> ~1.20 times that benchmark
M_BH=5e11 kg  -> ~2.99 times that benchmark.
```

Aber:

```text
THIS IS NOT A DIRECT EXCLUSION OF THE PRIMORDIAL F6 POPULATION.
```

Gründe:

1. F6 benötigt die Population während der frühen terrestrial-formation epoch, nicht zwingend heute.
2. Seeds können später eingefangen, ausgestoßen oder anderweitig aus dem 1-AU-Phasenraum entfernt worden sein.
3. Ephemeriden-Density-Limits modellieren eine verteilte DM-Komponente; eine anisotrope/co-orbitale kompakte Population mappt nicht exakt auf denselben Parameter.

Der heutige Bennu-Wert ist daher ein **retention benchmark**, kein F6-Formation-Ausschluss.

Ein Review der planetary-ephemeris Tests gibt außerdem eine Gesamt-DM-Masse innerhalb Saturn von Größenordnung `<~7e-11 M_sun` an. Die F6-Referenz-Populationen unten liegen mit ihrer Gesamtmasse deutlich darunter, sodass der rohe Gesamtmassen-Budgettest den Branch nicht allein ausschließt.

## 6. Geometrische globale Seed-Abundance

Zur Illustration wird ein phase-mixed Geometrieproxy benutzt.

Für eine Population um 1 AU mit radialer Breite `Delta a` und vertikaler Halb-Höhe `H=a sin i`:

Thin disk (`H <= r_H`):

```text
f_H ~ r_H^2/(2 a Delta a).
```

3-D torus (`H > r_H`):

```text
f_H ~ r_H^3/(3 a Delta a H).
```

Dann

```text
N_seed,50 = ln(2)/(N_enc K_F5 S_post f_H).
```

Für `M1=0.03 M_E`, `N_enc=10`, `S_post=0.5`:

| Seed population proxy | Delta a | i | f_H | N_seed für 50% |
|---|---:|---:|---:|---:|
| razor-cold co-orbital band | `~0.00622 AU` | `0.01 deg` | `7.77e-4` | `1.07e4` |
| ultra-cold annulus | `0.02 AU` | `0.05 deg` | `2.42e-4` | `3.44e4` |
| cold inner disk | `0.10 AU` | `0.5 deg` | `1.15e-5` | `7.25e5` |
| warm broad disk | `0.50 AU` | `2 deg` | `5.74e-7` | `1.45e7` |

Diese Zahlen sind **keine astrophysikalisch vorhergesagten Seed-Zahlen**. Sie zeigen, welche Population ein zukünftiges F1-Origin-Modell liefern müsste.

Bei `M_BH=1e11 kg` entsprechen sie Gesamtmassen von ungefähr

```text
1.07e15 kg
3.44e15 kg
7.25e16 kg
1.45e18 kg.
```

Selbst die warme Referenz liegt nur bei ungefähr `2.4e-7 M_E`. Die reine Gesamtmasse ist daher überraschenderweise **nicht** der Hauptengpass.

Der Engpass ist die Erzeugung und Aufrechterhaltung von `10^4...10^7` extrem kompakten, bereits solar gebundenen Seeds im richtigen 1-AU-Phasenraum.

## 7. F4/F5 survival cross-check

Die fünf dokumentierten persistenten STRONG-F5-Captures besitzen ungefähr

```text
(M1/M_E, a_seed/r_H):
(0.0532, 0.380)
(0.0159, 0.281)
(0.00339,0.414)
(0.00330,0.214)
(0.0193, 0.302).
```

Wendet man F4s adiabatischen Growth-engulfment Gate auf diese Beispiele an, liegen `4/5` innerhalb des einfachen Engulfment-Bereichs; der Fall `(0.0532,0.380)` liegt außerhalb.

Das zeigt:

```text
growth-assisted engulfment is not obviously a measure-zero subset of the F5 survivors.
```

Es rechtfertigt aber **keinen** exakten `S_post`. Spätere Embryo-Störungen, Giant Impacts und die endgültige zentrale Settling-Closure bleiben offen.

## 8. F6 Statusmatrix

| Teiltest | Status | Ergebnis |
|---|---|---|
| F5 exchange kernel usable in population folding | **PASS** | `K~1.67%` Strong persistent |
| population formula / Poisson gate | **CALCULATED** | explicit `P=1-exp(-lambda)` |
| normal Galactic halo abundance | **FAIL** | required overdensity `~1e5...1e7+` |
| one isolated solar-bound seed | **FAIL as generic population solution** | Hill duty cycle too small |
| required local seed density | **CALCULATED** | mass-dependent table above |
| required global seed number | **PARAMETRIC / CALCULATED** | `~1e4...1e7` in reference geometries |
| raw total seed mass budget | **NO EXCLUSION in reference proxies** | far below Earth mass / broad Saturn-DM mass budget |
| present-day Bennu density comparison | **TENSION for higher masses if population survives unchanged** | not primordial exclusion |
| physical seed production mechanism | **OPEN / dominant bottleneck** | no mechanism yet supplies abundance |
| absolute Earth-delivery probability | **OPEN** | cannot close without seed origin + encounter history |

## 9. Consequence for the formation branch

F5 solved the local mechanics only conditionally. F6 shows what that conditionality costs.

The surviving chain is now

```text
normal halo capture                     VERY STRONG FAIL
normal protostellar halo capture        strongly negative
naked-seed disk gas drag                FAIL
random GI pull-down                     strongly timing-suppressed
multi-pass timing rescue                FAIL as generic mechanism
early embryo exchange mechanics         PASS conditionally
population-weighted F6 normal halo      FAIL
primordial solar-bound overdense seeds  OPEN but quantitatively demanding.
```

The branch is therefore **not dead**, but its bottleneck has moved almost completely to primordial seed origin/abundance.

For the reference `1e11 kg` seed, a 50% Earth-delivery target requires roughly

```text
rho_seed ~2e-15 kg/m^3 near the relevant 1-AU early phase space
~3.7 million times canonical Galactic DM density
```

if only ten relevant Strong encounters and `S_post=0.5` are available.

## Nächster harter Test – F7

F7 must attack the only major formation freedom left:

```text
Can any physically motivated primordial / protosolar mechanism
produce ~1e4...1e7 already solar-bound 1e10...5e11 kg seeds
in the terrestrial feeding region without violating mass/dynamical constraints?
```

Required F7 blocks:

```text
PBH/seed phase-space distribution before Solar birth
stellar-cluster / molecular-cloud gravitational capture
adiabatic Solar potential growth
binary / multi-star exchange capture
retention through gas-disk and embryo phase
present-day survivor fraction
comparison with ephemerides / asteroid tracking.
```

If F7 cannot generate the F6 required abundance, the entire formation/delivery branch becomes strongly negative even though F5 local exchange remains dynamically possible.

## Reproduzierbare Datei

- `stage3_78_f6_population_weighted_formation_gate.py`

## Schlussstatus

```text
F6 POPULATION FOLDING:
PASS / CALCULATED.

NORMAL HALO POPULATION:
FAIL by abundance.

PRIMORDIAL SOLAR-BOUND OVERDENSE POPULATION:
OPEN, quantitatively demanding.

ABSOLUTE EARTH DELIVERY:
OPEN.

EXPERIMENTAL BH DETECTION:
NONE.
```