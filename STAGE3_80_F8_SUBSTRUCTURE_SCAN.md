# Stage 3.80 / F8a – Co-moving cold substructure phase-space scan

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** SEMI-ANALYTIC SOLVER PASS / PRE-SOLAR MINI+STREAM ORIGIN CANDIDATES FOUND / POST-COLLAPSE TORUS TARGET-STATE GATE PASS CONDITIONAL / LONG-TERM RETENTION OPEN / FINAL F8 OPEN

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

F8a ist jetzt in drei physikalisch getrennte Screenings aufgeteilt:

```text
mini   = präsolarer virialisierter Plummer-Minihalo
stream = präsolarer ungebundener Gaussian-Clump / Streamsegment
torus  = post-collapse / embryo-epoch co-orbital target state at 1 AU.
```

Die drei Branches dürfen nicht miteinander verwechselt werden.

# 1. Kritische Korrekturen am ursprünglichen Grid

## 1.1 F6-Hill-Normierung

Der User-Prototyp verwendete für `mu_H` die Hill-Sphäre einer fertigen Erde.
F6 ist aber auf

```text
M_embryo = 0.03 M_E
```

normiert.

Da

```text
V_H proportional M_embryo,
```

würde `1 M_E` das relevante Hill-Volumen und damit `mu_H` um

```text
1/0.03 = 33.333...
```

überschätzen.

Die korrigierte Regression reproduziert wieder exakt:

```text
seed mass = 1e11 kg
rho_F6    ~1.975e-15 kg/m^3
M1        =0.03 M_E
=> mu_H   =8.318.
```

Status: **CORRECTED / PASS regression.**

## 1.2 `sigma_sub` darf für einen bound Minihalo nicht frei sein

Für einen isotropen Plummer-Halo gilt:

```text
rho(r) = 3 M/(4 pi a^3) [1+r^2/a^2]^(-5/2)

sigma_1D^2(r)
= G M/(6 a) [1+r^2/a^2]^(-1/2).
```

Damit sind `M_sub`, `r_core` und `sigma_sub` gekoppelt.

Bei festem `a` gilt zentral:

```text
rho ~ M
sigma ~ M^(1/2)
Q=rho/sigma^3 ~ M^(-1/2).
```

Ein unabhängiger `M,r,sigma`-Grid ist deshalb für einen selbstgebundenen virialisierten Halo nicht physikalisch.

Status: **independent sigma scan for mini-halo REJECTED.**

Der Plummer-Dispersionsterm entspricht dem Standard-isotropen Plummer-Modell; z.B. wird zentral `sigma_0^2=GM/(6a)` verwendet.

## 1.3 Dünner Stream: `rho_local * V_H` ist nicht allgemein gültig

Wenn eine co-orbitale Population schmaler als die Proto-Earth-Hill-Sphäre ist, darf nicht die lokale Peak-Dichte mit dem gesamten Hill-Volumen multipliziert werden.

Für den neuen `torus`-Branch wird deshalb die tatsächlich innerhalb der Hill-Sphäre liegende Torusmasse integriert.

Lokal ist der Ring entlang einer Achse nahezu gerade; für Gaussian cross-section

```text
rho(s)=rho_0 exp[-s^2/(2w^2)]
```

wird

```text
M_H
=4 pi rho_0 integral_0^RH
  s sqrt(R_H^2-s^2) exp[-s^2/(2w^2)] ds.
```

Im `w << R_H`-Grenzfall folgt

```text
f_H,spatial -> R_H/(pi AU)
            ~9.89e-4.
```

Damit kann ein immer dünnerer Stream `mu_H` nicht künstlich divergieren lassen.

Status: **exact Hill-overlap integration PASS.**

## 1.4 Epizykel-Konsistenz

Für einen unconfined collisionless Torus im Kepler-Potential gilt größenordnungsmäßig

```text
w_epi ~ sigma/Omega.
```

Ein beliebig dünner und gleichzeitig heißer Ring ist daher nicht selbstkonsistent.

Der neue `torus`-Hauptgate verlangt

```text
w >= sigma/Omega.
```

Status: **epicycle gate implemented / PASS regression.**

# 2. F7/F8 Phase-Space Gate für präsolare Strukturen

Für `mini` und `stream` bleibt F7s low-velocity phase-space mapping erhalten:

```text
Q_eff = rho/sigma^3 * exp[-v_rel^2/(2 sigma^2)]
```

und als absichtlich capture-freundlicher Upper-Bound

```text
rho_bound(r)
= [4/(3 sqrt(pi))] Q_eff (G M_sun/r)^(3/2).
```

Bei 1 AU:

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

# 3. Collapse-overlap / co-motion

Referenz:

```text
t_collapse = 0.06 Myr.
```

Im reduzierten Overlap-Stressproxy:

```text
d = v_rel t_collapse.
```

Schon

```text
v_rel =1 km/s
```

ergibt während `0.06 Myr` einen Drift von ungefähr

```text
~12,650 AU.
```

Das macht echte co-motion unverzichtbar.

# 4. Mini-Halo Cluster-Survival Stressproxy

Der vorhandene F8a-Minihalo-Branch bleibt erhalten.

Er kombiniert:

```text
mean rho(<r_half) > 3 rho_cluster
```

mit einem einfachen impulsiven Stellar-Encounter-Screen.

Cluster-Referenzen:

| model | n_star [pc^-3] | v_star [km/s] |
|---|---:|---:|
| low | `1e2` | `1.4` |
| med | `1e3` | `2.0` |
| high | `1e4` | `2.9` |

Wichtig:

```text
cluster_survival_prob is a screening proxy, not a calibrated N-body probability.
```

Langsame weite Begegnungen können adiabatisch abgeschirmt sein; successive encounters können Kerne strippen statt sie instantan vollständig zu zerstören.

Die Literatur zu jungen Sternhaufen zeigt, dass enge Begegnungen real auftreten: für solarmassige Clustersterne werden in typischen offenen Clustern Größenordnung `10...20%` Begegnungen innerhalb `100 AU` berichtet. Das rechtfertigt einen Survival-Test, aber nicht die Gleichsetzung mit sicherer Zerstörung der 1-AU-Population.

# 5. Reproduktion des bisherigen Origin-Grids

Der ursprüngliche `mini+stream` Canonical-Run bleibt nach dem Merge exakt reproduziert:

```text
25,920 rows total.
```

## Mini

```text
rows                    = 2,880
phase-space pass         = 702
Stage-1 candidates       = 390
Stage-1 + unchanged today= 0.
```

Candidate `v_rel` range im diskreten Grid:

```text
0 ... 0.01 km/s.
```

## Stream

```text
rows                    = 23,040
phase-space pass         = 5,391
Stage-1 candidates       = 692
Stage-1 + unchanged today= 0.
```

Candidate `v_rel` range:

```text
0 ... 0.1 km/s.
```

Die alten F8a-Origin-Zähler wurden damit nicht durch den neuen Torus-Block verändert.

# 6. Neuer post-collapse `torus`-Branch

Dieser Branch testet nicht erneut den F7-Collapse-Mapper, sondern die Frage:

```text
Wenn die frühe Struktur bereits als solar-orbitierende kalte co-orbitale
Population bei ~1 AU angekommen ist, welche Breite, Dispersion und Stückzahl
braucht sie tatsächlich für F6?
```

Full torus grid:

```text
M_sub = 1e-18 ... 1e-6 M_sun, 40 log points
width = 1e-4 ... 0.3 AU, 24 log points
sigma = 0.01 ... 2 km/s, 30 points
v_rel = 0 ... 1 km/s, 5 points
4 seed masses
```

Gesamt:

```text
576,000 rows.
```

Reiner F6 `mu_H`-Gate:

```text
341,112 rows pass.
```

Nach

```text
exact Hill overlap
+ epicycle consistency
+ thin-torus validity
```

bleiben

```text
85,721 Stage-1 target-state rows.
```

Das entspricht `14.9%` des absichtlich log/linear konstruierten Grids.

**Diese Grid-Fraktion ist keine astrophysikalische Wahrscheinlichkeit.**

## Thin-ring Stückzahlgrenze

Für perfekte velocity eligibility:

```text
N_seed,min
~ mu_H,50 / [R_H/(pi AU)]
~8.41e3 Seeds.
```

Der diskrete Vollscan findet wegen seiner logarithmischen Massenabtastung ein Minimum von ungefähr

```text
9.64e3 Seeds.
```

Damit reproduziert F8a unabhängig die F6-razor-cold Größenordnung `~1e4`.

# 7. Epicycle-matched Hauptresultat

Setze ohne zusätzliche Confinement-Physik

```text
w = sigma/Omega
```

und `v_eligible=1 km/s`.

| sigma | w_epi [AU] | N_seed required, v_rel=0 | N_seed required, v_rel=1 km/s |
|---:|---:|---:|---:|
| `0.01 km/s` | `3.36e-4` | `8.51e3` | `1.72e4` |
| `0.05 km/s` | `1.68e-3` | `1.33e4` | `2.77e4` |
| `0.10 km/s` | `3.36e-3` | `3.47e4` | `7.54e4` |
| `0.20 km/s` | `6.71e-3` | `1.23e5` | `2.92e5` |
| `0.50 km/s` | `1.68e-2` | `1.00e6` | `2.46e6` |
| `1.00 km/s` | `3.36e-2` | `1.48e7` | `2.23e7` |
| `2.00 km/s` | `6.71e-2` | `3.82e8` | `4.30e8` |

Damit wird F7s qualitative Aussage quantitativ verschärft:

```text
sigma <=~0.1...0.2 km/s:
F6 needs ~1e4...1e5 seeds.

sigma ~0.5 km/s:
~1e6 seeds.

sigma ~1 km/s:
~1e7 seeds.

sigma ~2 km/s:
~few 1e8 seeds.
```

Für `1e11 kg` pro Seed entsprechen die `v_rel=0` Reihen ungefähr:

```text
sigma=0.01 km/s -> 8.5e14 kg
sigma=0.10 km/s -> 3.5e15 kg
sigma=0.50 km/s -> 1.0e17 kg
sigma=1.00 km/s -> 1.5e18 kg
sigma=2.00 km/s -> 3.8e19 kg.
```

Die rohe Gesamtmasse ist weiter nicht der dominante Engpass.

Der Engpass ist:

```text
extreme coldness
+ co-orbitality
+ survival of the required number phase-space density.
```

# 8. Selbstgebundener Plummer-Branch nach Sonnenbildung

Ein solarzentrierter self-gravitating Plummer-Halo darf nicht als unverändertes post-Sun Gleichgewicht interpretiert werden.

Für F6-erfüllende low-mass Plummer-Beispiele ist am 1-AU-Ort die selbstgravitative Random-Velocity-Skala nur Größenordnung `sub-m/s`, während der solare Kepler-Speed ungefähr `30 km/s` beträgt.

Damit dominiert das Sonnenpotential die reine Halo-Selbstgravitation um viele Größenordnungen.

Konsequenz:

```text
self_bound_plummer is only a pre-solar initial-condition screen.
```

Nach Bildung der Sonne muss dieser Zustand über das zeitabhängige Gas-/Sonnenpotential remapped werden.

Das ist F8c/N-body-Arbeit und wird nicht durch F8a behauptet.

# 9. Present-day retention benchmark

Der Bennu/OSIRIS-REx distributed-DM Benchmark nahe 1.1 AU bleibt ungefähr

```text
rho_DM <~3.3e-15 kg/m^3.
```

Im vorhandenen `mini` Canonical Grid erfüllt keine Stage-1-Zelle gleichzeitig einen unveränderten heutigen Retention-Benchmark.

Das ist **kein primordialer Ausschluss**. Erfolgreiche frühe Kandidaten müssen aber typischerweise später

```text
strip / eject / phase-mix / accrete / otherwise deplete
```

oder heute eine deutlich andere Verteilung besitzen.

# 10. Regressionstests

`test_stage3_80_f8_substructure_scan.py`:

```text
12/12 PASS
```

Geprüft werden jetzt:

1. Plummer `rho proportional M`.
2. Virial `sigma^2 proportional M`.
3. `Q proportional M^-1/2` bei festem scale radius.
4. F6/F7 Q regression für `1e11 kg`.
5. Bulk-velocity suppression.
6. Stream expansion/dilution.
7. F6 density-to-`mu_H` roundtrip.
8. Expliziter Faktor `33.333` zwischen `1 M_E`- und F6-`0.03 M_E`-Hillvolumen.
9. Thin-torus Hill-intersection limit.
10. Torus velocity-eligibility suppression.
11. Epicycle-matched `sigma=0.1 km/s` requirement (`~3.5e4` Seeds).
12. Compatibility grid row/column reproducibility.

# 11. Statusmatrix

| Teiltest | Status |
|---|---|
| Originaldraft F6 Hill mass | **CORRECTED** |
| unabhängiger `M,r,sigma` Minihalo-Scan | **REJECTED** |
| Plummer/Virial regressions | **PASS** |
| F7 `Q_eff` co-motion gate | **PASS / explicit** |
| pre-solar Minihalo phase-space candidates | **FOUND / conditional** |
| Minihalo cluster survival | **PARTIAL proxy** |
| finite pre-solar Stream collapse-overlap | **FOUND / conditional** |
| exact post-collapse torus/Hill overlap | **PASS** |
| epicycle-width consistency | **PASS gate** |
| cold `sigma<=0.1...0.2 km/s` torus F6 target | **PASS conditional** |
| warm `~1 km/s` torus | **requires ~1e7 seeds** |
| normal halo origin | **FAIL from F7** |
| post-collapse stream/torus survival to embryo epoch | **OPEN** |
| time-dependent Sun+gas remapping | **OPEN** |
| unchanged present-day retention | **tension / model dependent** |
| final F8 | **OPEN** |
| direct Earth-BH evidence | **NONE** |

# 12. Konsequenz

F8a widerlegt F7s letzten Origin-Rescue **nicht sofort**.

Es zeigt aber jetzt genauer, was der Branch wirklich verlangt:

```text
pre-solar cold/co-moving structure
+ successful collapse mapping
+ post-collapse torus-like phase space
+ sigma preferably <=0.1...0.2 km/s
+ ~1e4...1e5 compact seeds for the coldest useful branch
+ survival through cluster and embryo heating
+ strong later depletion or present-day consistency.
```

Damit ist F8a weiterhin

```text
PASS as parameter-space existence screen
```

aber **kein Formation proof**.

# 13. Nächste harte Schritte

## F8b – Cluster survival

Nicht mehr nur ein single-impulse proxy:

```text
Monte-Carlo sequence of stellar encounters
+ evolving mass/profile after stripping
+ low/med/high birth-cluster histories
+ P_survive(t=1e6...1e7 yr)
+ explicit adiabatic shielding for slow wide encounters.
```

Literatur zu jungen Clustern zeigt, dass `10...20%` solarmassiger Sterne in typischen offenen Clustern Begegnungen innerhalb `100 AU` erleben können; daher ist dieser Test relevant.

## F8c – Sun/gas remapping

```text
Proto-Sun + time-dependent gas potential
+ candidate mini/stream initial conditions
-> final a,e,i / torus width / velocity dispersion near 1 AU.
```

Erst F8b+c können entscheiden, ob die F8a-Zielzustände physisch erzeugbar sind.

# Reproduzierbare Dateien

- `stage3_80_f8_substructure_scan.py`
- `stage380f8substructurescan.py` – compatibility shim für den ursprünglichen User-Dateinamen
- `test_stage3_80_f8_substructure_scan.py`
- `STAGE3_80_F8_SUBSTRUCTURE_SCAN.md`
- bestehende `results/f8_example_candidates.csv`
- bestehende `results/f8_example_summary.json`

CLI:

```bash
python stage3_80_f8_substructure_scan.py --branch both
python stage3_80_f8_substructure_scan.py --branch torus
python stage3_80_f8_substructure_scan.py --branch all
pytest -q test_stage3_80_f8_substructure_scan.py
```

# Literaturanker

- Standard isotropic Plummer velocity-dispersion relation; z.B. Plummer-model treatments with `sigma_0^2=GM/(6a)`.
- Brown et al. (2016), MNRAS 457, 1062: Solar birth-cluster models with velocity dispersions roughly `1.4...2.9 km/s` for their adopted cluster set.
- Hao et al. / cluster fly-by literature: order `10...20%` of Solar-mass members in typical open clusters can experience encounters inside `100 AU`.
- Green & Goodwin (2007), MNRAS 375, 1111, DOI `10.1111/j.1365-2966.2007.11397.x`.
- Goerdt et al. (2007), MNRAS 375, 191, DOI `10.1111/j.1365-2966.2006.11281.x`.

# Schlussstatus

```text
F8a PRE-SOLAR ORIGIN PHASE-SPACE: candidates remain
F8a POST-COLLAPSE TORUS TARGET STATE: PASS conditionally
F8 CLUSTER + SOLAR-FORMATION SURVIVAL: OPEN
PRESENT-DAY COMPATIBILITY: OPEN / later evolution generally required
ABSOLUTE EARTH DELIVERY: OPEN
DIRECT BH EVIDENCE: NONE
```
