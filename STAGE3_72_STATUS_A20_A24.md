# Stage 3.72 – Status A20–A24

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** NEW CLOSURE GATES CALCULATED / FULL-PHYSICS DOWNSTREAM TESTS UPSTREAM-BLOCKED

## Ausgangspunkt

Der Reduced-/Pre-Falsification-Stack A1–A19 bleibt als abgeschlossener Projektmeilenstein eingefroren. Stage 3.72 greift die danach verbliebenen Full-Physics-Schlussprobleme an.

## A20 – Tabulated Fe EOS ingestion gate

```text
Tabulated P(rho) ingestion + h(rho) reconstruction + Michel critical finder:
COMPLETE / PASS regression.

Grant raw Zenodo data:
OPEN / blocked by current data access.

Direct SESAME 92141:
OPEN.

Uncontrolled extrapolation beyond measured table:
REJECTED.
```

Wichtige Erkenntnis: Grant-Rohdaten koennen den Outer-Fe-EOS-Abschnitt haerten, decken aber nicht automatisch den deutlich tieferen Michel-Kritikpunkt ab.

## A21 – Screened-electron matcher conditioning

Bei `M=1e11 kg`, Earth-speed:

```text
alpha_e ~1.923e-4
pM ~6.69e-9
lambda_db ~1.11e-8 m
lambda_TF ~2.95e-11 ... 4.29e-11 m
neutral leading P_abs ~O(4e-11)
required far-field scale x >> O(1e9)
```

Damit ist die direkte Wiederverwendung des A4-Proton-Matchers numerisch nicht kontrolliert.

```text
A4 matcher reuse for electrons:
REJECTED AS UNCONTROLLED.

Full screened-electron S-matrix:
OPEN.
```

## A22 – Fe-Ni-light-element mixture data gate

Eine oeffentliche, CC0-lizenzierte Datenbasis wurde verifiziert:

```text
Liu & Asimow CaltechDATA
DOI 10.22002/dxgqf-tw269
```

Verifizierte Komponenten umfassen Fe, Fe-Ni, Fe-O, Fe-Si, Fe-S, Fe-C, Fe-H und ausgewaehlte ternaere Mischungen.

```text
public mixture dataset existence/coverage:
VERIFIED.

workbook/schema ingestion machinery:
COMPLETE / PASS synthetic regression.

binary workbook numerical ingestion in current run:
BLOCKED BY TOOL DOWNLOAD.

full mixture EOS:
OPEN.
```

## A23 – Two-temperature + weak-reaction gate

Publizierter warm-dense Fe-Anker:

```text
tau_ei ~2.6 +/-0.1 ps
```

Outer `r_B/c_eff` Vergleich:

```text
1e10 kg: tau_ei/t_cross ~4.43
1e11 kg: ~0.443
2e11 kg: ~0.221
5e11 kg: ~0.0885
```

Daraus folgt:

```text
Te=Ti everywhere:
REJECTED as universal Full-WDM assumption.
```

Der bestehende aggressive `56Fe` Electron-Capture-Benchmark bleibt am schnellen Fe-Threshold etwa `4e12` mal langsamer als die Reduced Residence-Zeit.

```text
prompt weak equilibrium in fast branch:
NOT SUPPORTED.

weak processing in stalled/backpressure reservoir:
OPEN.
```

## A24 – Final net-Mdot identifiability

A13b conservative supply vs A10 capacity:

| M_BH | Xi_min | Xi_max |
|---:|---:|---:|
| `1e10` | `0.832` | `61.64` |
| `1e11` | `1.59e-3` | `0.118` |
| `2e11` | `2.42e-4` | `1.80e-2` |
| `5e11` | `2.00e-5` | `1.49e-3` |

```text
>=1e11 kg:
reduced processing-capable classification retained.

1e10 kg:
EOS/supply/backpressure conditional classification retained.
```

Eine eindeutige finale species-resolved Rate ist jedoch noch nicht mathematisch identifizierbar, weil mehrere offene Funktionen dieselbe Reduced-Rate beeinflussen:

```text
mixture EOS
screened-electron capture current
Te/Ti coupling
reaction network
permanent escape/recycling
Q(t)
time-dependent hydro/backpressure
```

Daher:

```text
single final Mdot_BH number now:
REJECTED AS FALSE PRECISION.

final species-resolved Mdot_BH(t):
OPEN / NOT YET IDENTIFIABLE.
```

## Konsequenz fuer nachfolgende Tests

Die folgenden Full-Physics-Tests sind **nicht sinnvoll unabhaengig ausfuehrbar**, solange A20/A21/A22/A23 nicht physikalisch geschlossen sind:

### Full heat/age rerun

Braucht eine finale zeitabhaengige `Mdot_BH(t)` und Energieablagerung.

```text
Status: UPSTREAM-BLOCKED.
```

A16 bleibt der gueltige Reduced/Pretest und liefert keinen harten 47-TW-/4.54-Gyr-Ausschluss.

### Macroscopic seismic prediction

Braucht aus Full-WDM mindestens

```text
delta rho(r,t)
delta Vp(r,t)
delta Vs(r,t)
```

auf km-relevanten Skalen.

```text
Status: UPSTREAM-BLOCKED.
```

A17 bleibt der Observability-Gate: die mikroskopische Near-Zone selbst ist kein sinnvoller direkter Seismikkanal.

### Full Stage 3.70 H0 likelihood

Braucht eine eindeutige vorhergesagte Observable-Amplitude aus dem Full-Physics-Modell.

```text
Status: UPSTREAM-BLOCKED / NOT IDENTIFIABLE YET.
```

A18 bleibt der aktuelle Real-Data-Audit. H+ bleibt im staerksten verwendeten SK-IV-Projektvergleich negativ; H0 bleibt offen.

## Formation

Formation/Delivery ist von den oben genannten Full-WDM-Datenproblemen weitgehend unabhaengig und wurde in A19 bereits erneut angegriffen.

```text
standard Earth capture / standard tested delivery:
strongly negative.

cold/co-moving primordial seed:
OPEN initial condition; no derived probability/origin.
```

## Aktueller Gesamtstatus nach A24

```text
Reduced stack A1-A19:
COMPLETE IN DEFINED SCOPE.

A20 table-EOS machinery:
COMPLETE; raw data closure OPEN.

A21 electron conditioning:
COMPLETE; full electron S-matrix OPEN.

A22 public mixture data source/gate:
COMPLETE; numerical workbook ingestion OPEN/BLOCKED.

A23 Te/Ti + weak timescale gate:
COMPLETE; full path-dependent closure OPEN.

A24 final-Mdot identifiability:
COMPLETE; unique Mdot_BH NOT IDENTIFIABLE YET.

Full Stage 3.69 multiphysics:
OPEN.

Full H0 Stage 3.70 likelihood:
UPSTREAM-BLOCKED / OPEN.

Formation solution:
OPEN / strongly constrained.

Experimental BH detection:
NONE.
```

## Was den naechsten echten Fortschritt ausloest

Ein echter weiterer Full-Physics-Sprung erfordert mindestens einen der folgenden Inputs:

1. maschinenlesbare Liu/Asimow-Workbooks oder andere verifizierte Fe-Ni-light-element EOS tables;
2. maschinenlesbare Grant/SESAME-Daten fuer den Outer-EOS-Abgleich;
3. einen kontrollierten flux-direct screened-electron Dirac/Jost/Riccati-Solver;
4. publizierte/path-validierte `G(rho,Te,Ti,X)` und Reaktionsraten fuer die relevante Mischung.

Bis dahin werden keine fehlenden Tabellenwerte, Mischgesetze oder finalen Netto-Raten erfunden.
