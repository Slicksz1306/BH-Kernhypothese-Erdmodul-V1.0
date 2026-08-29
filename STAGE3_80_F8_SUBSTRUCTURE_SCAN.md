# Stage 3.80 / F8a – Co-moving cold substructure phase-space scan

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** SEMI-ANALYTIC SOLVER PASS / MINI-HALO CANDIDATES FOUND / STREAM COLLAPSE-OVERLAP CANDIDATES FOUND / LONG-TERM RETENTION OPEN / FINAL F8 OPEN

## Ziel

F7 hat normale Galactic-halo-Ursprünge für die von F6 geforderte terrestrische kalte Seed-Population verworfen. F8 testet den letzten Origin-Spezialbranch:

```text
pre-existing co-moving cold dark substructure
-> proto-solar collapse / phase-space mapping
-> solar-bound cold seeds near ~1 AU
-> F5 embryo-exchange capture
-> F4 growth-assisted engulfment.
```

F6-Referenz:

```text
M1 = 0.03 M_E
mu_H,50 = 8.318 eligible seeds / Proto-Earth Hill volume.
```

## Kritische Physik-Korrektur

Für einen selbstgebundenen virialisierten Mini-Halo dürfen `M_sub`, `r_core` und `sigma_sub` nicht unabhängig gescannt werden. F8 trennt daher zwei Klassen.

### A. `mini`

Isotroper Plummer-Halo:

```text
rho(r) = 3 M/(4 pi a^3) [1+r^2/a^2]^(-5/2)

sigma_1D^2(r)
= G M/(6 a) [1+r^2/a^2]^(-1/2).
```

Damit wird `sigma` aus `M_sub` und `a` abgeleitet.

Bei festem `a` gilt zentral:

```text
rho ~ M
sigma ~ M^(1/2)
Q=rho/sigma^3 ~ M^(-1/2).
```

Die ursprünglich vorgeschlagene Regression `mu_H must increase monotonically with M_sub` ist daher für den virialisierten cold-phase-space Gate nicht korrekt.

### B. `stream`

Ungebundener Gaussian cold-clump / finite stream segment. Hier dürfen `M_sub`, `r_core`, `sigma_sub` und `v_rel` unabhängig sein; dafür werden ballistische Expansion und Bulk-Drift während des protosolaren Kollapses explizit gerechnet.

Ein Stream-Stage-1-PASS bedeutet nur ausreichende Phase-Space-Dichte während des Kollapses; 10-Myr-Retention nach Sonnenbindung bleibt OPEN.

## F7/F8 Phase-Space Gate

Die low-velocity phase-space density im Proto-Sun-Frame wird als

```text
Q_eff = rho/sigma^3 * exp[-v_rel^2/(2 sigma^2)]
```

modelliert.

Der exponentielle Faktor macht co-motion zu einer echten dynamischen Bedingung: ein dichter Halo ist für F6 nutzlos, wenn seine Bulk-Geschwindigkeit gegenüber der Proto-Sonne viel größer als seine interne Dispersion ist.

Als capture-freundlicher Upper-Bound wird der F7-Mapping-Proxy verwendet:

```text
rho_bound(r)
= [4/(3 sqrt(pi))] Q_eff (G M_sun/r)^(3/2).
```

Bei `r=1 AU`:

```text
mu_H = rho_bound(1 AU) V_H / M_seed.
```

PASS-Schwelle:

```text
mu_H >= 8.318.
```

Erforderliche initiale Q-Werte:

| Seedmasse | Q_req [M_sun pc^-3 (km/s)^-3] |
|---:|---:|
| `1e10 kg` | `0.146794` |
| `1e11 kg` | `1.46794` |
| `2e11 kg` | `2.93589` |
| `5e11 kg` | `7.33972` |

## Collapse-overlap / co-motion

Referenz:

```text
t_collapse = 0.06 Myr.
```

Im reduzierten Overlap-Stressproxy:

```text
d = v_rel t_collapse.
```

Damit ergibt bereits

```text
v_rel = 1 km/s
-> d ~12,650 AU
```

während des Kollapses. Kompakte Substrukturen benötigen daher echte co-motion; `v_rel <=1 km/s` allein ist noch keine ausreichende Aussage.

## Mini-Halo Cluster-Survival Stressproxy

F8a kombiniert zwei transparente reduzierte Gates:

```text
mean rho(<r_half) > 3 rho_cluster
```

und einen impulsiven stellar-encounter Proxy mit

```text
Delta E_impulse(b_disrupt) ~ |E_bind|
P_survive = exp[-Gamma t].
```

Cluster-Stressmodelle:

| model | n_star [pc^-3] | v_star [km/s] |
|---|---:|---:|
| low | `1e2` | `1.4` |
| med | `1e3` | `2.0` |
| high | `1e4` | `2.9` |

Literatur zu Mini-Halo-Disruption zeigt, dass einfache Impulsenergie-Kriterien reale Massverluste nur näherungsweise erfassen; dichte Kerne können widerstandsfähiger sein, und successive Encounters verändern das Profil. Der F8a-Survivalwert ist deshalb nur ein Screening-Proxy.

## Canonical Example Grid

```text
branch = both
M_sub = 1e-15 ... 1e-4 M_sun, 10 Punkte
r_core = 1e-3 ... 1e3 AU, 12 Punkte
stream sigma = 0.01 ... 1 km/s, 8 Punkte
hybrid v_rel grid, 6 Punkte
4 seed masses
cluster = med
```

Gesamt:

```text
25,920 rows.
```

### Mini-Halo

```text
phase-space pass rows = 702
Stage-1 candidate rows = 390
Stage-1 + unchanged-present-day-density rows = 0.
```

Diese Zähler sind Grid-Zellen, keine Wahrscheinlichkeiten.

Beispiel nahe dem F6-Gate:

```text
M_sub ~5.99e-6 M_sun
r_core ~0.00351 AU
v_rel = 0.01 km/s
M_seed = 1e10 kg
sigma_phase ~2.65 m/s
mu_H,mapped ~11.56
P_cluster_proxy ~0.9995.
```

Der gleiche Punkt bei `v_rel=1 km/s` fällt durch Drift + low-velocity suppression praktisch auf `mu_H -> 0`.

### Stream / finite clump

Canonical Example:

```text
Stage-1 collapse-overlap candidates = 692.
```

Sie treten im Beispiel nur im sehr kalten/co-moving Teil auf. Beispiel nahe dem `1e11 kg` Gate:

```text
M_sub ~4.64e-12 M_sun
r_core = 1000 AU
sigma = 0.01 km/s
v_rel = 0.01 km/s
collapse overlap fraction ~0.969
mu_H,mapped ~8.61.
```

Das ist kein finaler Stream-PASS; die solar-bound Retention über `1e6...1e7 yr` muss F8b/F8c erst zeigen.

## Seed-fraction correction

Das erste Draft-Modell setzte implizit `all substructure mass = compact seeds`. F8a gibt daher explizit

```text
f_seed_required = mu_H,50 / mu_H(f_seed=1)
```

aus. Ein Stage-1-Kandidat muss `f_seed_required <=1` erfüllen.

## Present-day retention benchmark

F6/F7 verwenden aus OSIRIS-REx/Bennu einen distributed-DM Benchmark nahe 1.1 AU von ungefähr

```text
rho_DM ~3.3e-15 kg/m^3.
```

Für Mini-Halos wird konservativ die größere von raw Plummer-1-AU-Dichte und gemappter Seed-Dichte gegen diesen Wert gehalten. Im Canonical Example erfüllt keine Mini-Halo-Stage-1-Zelle gleichzeitig einen unveränderten heutigen Retention-Benchmark.

Das ist kein primordialer Ausschluss. Es bedeutet, dass erfolgreiche frühe Kandidaten typischerweise spätere stripping/ejection/profile evolution benötigen oder heute in einem anderen Zustand vorliegen müssen.

## Regressionstests

`test_stage3_80_f8_substructure_scan.py`:

```text
7/7 PASS
```

Geprüft werden:

1. Plummer `rho proportional M`.
2. Virial `sigma^2 proportional M`.
3. `Q proportional M^-1/2` bei festem scale radius.
4. F6/F7-Q regression für `1e11 kg`: `1.46794 M_sun pc^-3 (km/s)^-3`.
5. Bulk-velocity suppression.
6. Stream-Expansion senkt lokale Dichte.
7. `rho_required -> mu_H` roundtrip reproduziert `8.318`.

## Statusmatrix

| Teiltest | Status |
|---|---|
| Initialdraft Syntax/Variablen | **CORRECTED** |
| unabhängiger `M,r,sigma`-Scan für bound mini-halo | **REJECTED** |
| Plummer/Virial regressions | **PASS** |
| F6 Q requirement | **PASS** |
| bulk co-motion gate | **PASS / explicit** |
| self-bound mini-halo phase-space candidates | **FOUND / conditional** |
| mini-halo 10-Myr survival | **PARTIAL proxy** |
| finite stream collapse-overlap candidates | **FOUND / conditional** |
| stream post-capture 10-Myr retention | **OPEN** |
| unchanged present-day retention | **tension / model dependent** |
| final F8 | **OPEN** |
| direct BH evidence | **NONE** |

## Konsequenz

F7s letzter Origin-Rescue wird durch F8a nicht sofort widerlegt:

```text
A sufficiently cold, dense, co-moving substructure can exceed the F6
phase-space requirement in a self-consistent virialized mini-halo screen.
```

Aber der Preis ist klar:

```text
strong co-motion is essential
+ cluster survival must survive harder modelling
+ solar-potential growth must be simulated self-consistently
+ later evolution must satisfy present-day bounds
+ compact-seed fraction and cosmological origin remain unexplained.
```

F8a ist daher **PASS als parameter-space existence screen**, nicht als Formation proof.

## Nächster Schritt – F8b

```text
Monte-Carlo cluster disruption of only the F8a candidate region
-> successive stellar encounters
-> evolving binding/profile
-> low/med/high cluster histories
-> P_survive(t=1e6...1e7 yr).
```

Danach F8c: Proto-Sun + time-dependent gas/Solar potential + candidate substructure N-body validation.

## Reproduzierbare Dateien

- `stage3_80_f8_substructure_scan.py`
- `test_stage3_80_f8_substructure_scan.py`
- `results/f8_example_candidates.csv`
- `results/f8_example_summary.json`
- GitHub Issue `#35`.

## Literaturanker

- Green & Goodwin (2007), MNRAS 375, 1111, DOI `10.1111/j.1365-2966.2007.11397.x`.
- Goerdt et al. (2007), MNRAS 375, 191, DOI `10.1111/j.1365-2966.2006.11281.x`.
- Shen et al. (2022), arXiv:2207.11276.
- Brown et al. (2016), MNRAS 457, 1062, Solar birth-cluster models.
- Batygin et al. (2020), arXiv:2002.05656, cluster dynamics / Solar-System exposure.

## Schlussstatus

```text
F8a SEMI-ANALYTIC PHASE-SPACE EXISTENCE: PASS / candidates found
F8 CLUSTER + SOLAR-FORMATION SURVIVAL: OPEN
PRESENT-DAY COMPATIBILITY: OPEN / later evolution generally required
ABSOLUTE EARTH DELIVERY: OPEN
DIRECT BH EVIDENCE: NONE
```
