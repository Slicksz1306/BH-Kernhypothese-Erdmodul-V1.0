# Stage 3.74 / F3 – Adaptive Hill-Monte-Carlo / Jacobi Pull-down Gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** NUMERICAL HILL SOLVER PASS / F2 TWO-BODY GATE HARDENED / GIANT-IMPACT PULL-DOWN NONZERO BUT NARROW / ABSOLUTE DELIVERY PROBABILITY OPEN

## Ziel

F2 zeigte nur einen lokalen Zwei-Körper-Energiegate:

```text
already solar-bound cold seed
+ temporary Hill residence
+ rapid embryo mass increase
=> capture kinematically possible.
```

F3 ersetzt diesen optimistischen Gate durch eine explizite planare Hill-Dynamik mit Solartiden und Jacobi-Closure.

Die Frage lautet jetzt:

```text
Wenn ein kalter, bereits solar gebundener Test-Seed tatsächlich in die Hill-Sphäre
eines terrestrischen Embryos eintritt, welcher Anteil der zeitgewichteten Zustände
wird durch einen instantanen Massensprung DeltaM/M dauerhaft hinter geschlossenen
L1/L2-Hälsen eingeschlossen?
```

Wichtig: F3 liefert **noch keine absolute Solar-System-Capture-Wahrscheinlichkeit**. Es liefert eine konditionale Pull-down-Fraktion innerhalb eines definierten Encounter-Ensembles.

## Literaturanker

Die lokale Hill-Näherung und temporäre Capture-Orbits aus helioszentrischen Bahnen sind Standard in der Planetesimal-Capture-Literatur:

- Ohtsuki et al. / Higuchi & Ida: low-random-velocity temporary capture under Hill equations.
- Suetsugu, Ohtsuki & Tanigawa / Suetsugu & Ohtsuki: temporary captures, including long-lived pseudo-periodic families; MNRAS 377, 1763 (2007) und MNRAS 431, 1709 (2013), DOI `10.1093/mnras/stt290`.
- Hansen, Science Advances 5, eaaw8665 (2019), DOI `10.1126/sciadv.aaw8665`: pull-down capture becomes inefficient when planetary growth is slow compared with the relevant orbital dynamics.

Terrestrische Planeten schließen ihre Akkretion über eine Giant-Impact-Phase ab; Earth erreichte nach aktuellen Reviews etwa `99%` seiner finalen Masse innerhalb ungefähr `60...100 Myr` nach den ersten kondensierten Festkörpern. Giant impacts haben sehr unterschiedliche Akkretionswirkungsgrade und können merge/hit-and-run outcomes liefern.

## Hill-Gleichungen

Verwendet werden dimensionslose Hill-Einheiten:

```text
length   = r_H
time     = Omega^-1
velocity = Omega r_H = v_H.
```

Planar:

```text
x'' - 2 y' - 3 x = -3 x/r^3
y'' + 2 x'       = -3 y/r^3.
```

Der Jacobi-Integralwert lautet für einen dimensionslosen planetaren Massenfaktor `m`:

```text
C = 3 x^2 + 6 m/r - (vx^2 + vy^2).
```

Die L1/L2-Punkte liegen bei

```text
x_L = m^(1/3)
```

und ihr Jacobi-Wert ist

```text
C_L = 9 m^(2/3).
```

Nach einem instantanen relativen Massensprung

```text
delta = DeltaM/M
m_new = 1 + delta
```

wird ein momentaner Zustand als **topologisch permanent eingefangen** klassifiziert, wenn

```text
C_new > C_L,new
```

während er innerhalb der planetaren Hill-Lobe liegt. Dann sind die L1/L2-Zero-Velocity-Necks im idealisierten zeitunabhängigen post-impact Hill-System geschlossen.

Das ist ein wesentlich härterer Capture-Gate als F2s lokales

```text
0.5 v_inf^2 < G DeltaM/r.
```

## Numerik

Der erste Versuch mit fixed-step RK4 zeigte bei tiefen Vorbeiflügen unakzeptablen Jacobi-Drift und überschätzte Capture. Diese Resultate wurden verworfen.

Finaler F3-Solver:

```text
scipy solve_ivp
method = DOP853
rtol   = 3e-10
atol   = 1e-12
```

Referenzläufe zeigen für die Hill-Segmente:

```text
median peak-to-peak Jacobi drift ~1.0e-8 ... 1.2e-8
maximum                        ~1.4e-7 ... 2.5e-7.
```

Status:

```text
adaptive Hill integration / Jacobi conservation: PASS
fixed-step RK4 deep-encounter result: REJECTED.
```

## Referenz-Ensemble

Pro velocity ensemble:

```text
N = 1000
|b| uniform in [0.5, 3.0] r_H
random sign(b)
y_start = +/-8 r_H
vy_start = -1.5 b + Gaussian noise
vx_start = Gaussian noise
sigma_v/v_H = 0.0, 0.1, 0.3
```

Massensprünge:

```text
delta = 0.01, 0.03, 0.10, 0.30.
```

Die `entry fraction` dieses Gitters ist **kein astrophysikalischer Encounter-Rate-Schätzer**. Das `b`-Intervall ist absichtlich auf Hill-relevante Encounters gelegt.

### Singularitäts-/Deep-Encounter-Schutz

Der Punktmassen-Hill-Solver wird bei

```text
r < 0.02 r_H
```

abgebrochen.

Für den konservativen Capture-Hauptwert werden ausschließlich Zustände

```text
r >= 0.1 r_H
```

gezählt. Damit hängt die Hauptaussage nicht von tiefen, numerisch und physikalisch komplizierten Embryo-Durchgängen ab.

## Encounter-Diagnostik

| sigma_v/v_H | Hill-entry im gewählten Grid | deep r<0.02 unter Entrants | >=1 planetozentrischer Umlauf | mean first residence |
|---:|---:|---:|---:|---:|
| `0.0` | `33.3%` | `27.0%` | `29.7%` | `0.603 Omega^-1` |
| `0.1` | `32.1%` | `26.2%` | `27.4%` | `0.607 Omega^-1` |
| `0.3` | `27.5%` | `22.2%` | `21.1%` | `0.608 Omega^-1` |

Bei 1 AU:

```text
Omega^-1 ~58.13 d
mean first Hill residence ~35.1...35.4 d.
```

Die Simulation verfolgt hier nur das **erste zusammenhängende Hill-Segment**. Die in der Literatur bekannten long-lived multi-pass/pseudo-periodic temporary-capture tails werden damit noch nicht vollständig erfasst.

## Hauptresultat – zeitgewichtete Jacobi-Closure

### Gesamte aufgelöste Hill-Sphäre `r>=0.02 r_H`

| delta | sigma=0.0 | sigma=0.1 | sigma=0.3 |
|---:|---:|---:|---:|
| `0.01` | `0` | `0` | `0` |
| `0.03` | `0.0938%` | `0.0865%` | `0.1008%` |
| `0.10` | `1.905%` | `1.643%` | `1.304%` |
| `0.30` | `8.613%` | `7.946%` | `7.029%` |

### Konservativer Hauptwert `r>=0.1 r_H`

| delta | sigma=0.0 | sigma=0.1 | sigma=0.3 |
|---:|---:|---:|---:|
| `0.01` | `0` | `0` | `0` |
| `0.03` | `0` | `0` | `0` |
| `0.10` | `0.0352%` | `0.0725%` | `0.0722%` |
| `0.30` | `6.806%` | `6.302%` | `5.653%` |

Ein unabhängiger zweiter `sigma=0.1`, `N=1000` Seed-Lauf ergab:

```text
delta=0.10 -> 0.0624%  at r>=0.1 r_H
delta=0.30 -> 6.580%   at r>=0.1 r_H.
```

Damit ist die Größenordnung des Referenzresultats gegen einen einfachen RNG-Seed-Wechsel stabil.

## Interpretation

### 1% Massensprung

```text
outer-Hill Jacobi closure: NOT FOUND in reference sample.
```

Das bedeutet **nicht mathematisch exakt Null**, sondern: kein aufgelöster Capture-State im getesteten konservativen Ensemble.

Status: **FAIL as an efficient outer-Hill pull-down channel / tiny unresolved tail remains possible.**

### 3% Massensprung

Capture taucht nur in tiefen `r<0.1 r_H` Zuständen auf. Im konservativen Outer-Hill-Tally:

```text
0 captures.
```

Status: **FAIL in conservative outer-Hill first-passage ensemble.**

### 10% Massensprung

F2s Zwei-Körper-Gate sah einen breiten kinematischen Bereich. Mit Solartiden/Jacobi-Closure schrumpft dieser massiv:

```text
r>=0.1 r_H:
P_close | instantaneous Hill occupancy
~3.5e-4 ... 7.2e-4
= 0.035...0.072%.
```

Capture existiert also, aber nur in einem sehr schmalen Teil der first-passage phase space.

Status: **PASS existence / FAIL as broad efficient channel in this reduced ensemble.**

### 30% Massensprung

Jetzt öffnet sich ein klarer endlicher Pull-down-Bereich:

```text
r>=0.1 r_H:
P_close | instantaneous Hill occupancy
~0.0565 ... 0.0681
= 5.65...6.81%.
```

Status: **PASS as a non-negligible conditional Hill pull-down channel.**

Aber auch das ist noch *bedingt darauf*, dass der Seed genau zum Impact-Zeitpunkt in der Hill-Sphäre sitzt.

## Timing-Faktor

Die mittlere first-passage Hill-residence liegt bei etwa

```text
35.3 d ~0.0966 yr.
```

Für **einen** zufällig platzierten Giant Impact in einem Akkretionsfenster von

```text
10 Myr  -> residence/window ~9.7e-9
100 Myr -> residence/window ~9.7e-10.
```

Daraus folgt als reine single-passage/single-impact Skalierung für das konservative Outer-Hill-Tally:

### delta=0.10

```text
10 Myr window:
~3.4e-12 ... 7.0e-12

100 Myr window:
~3.4e-13 ... 7.0e-13.
```

### delta=0.30

```text
10 Myr window:
~5.5e-10 ... 6.6e-10

100 Myr window:
~5.5e-11 ... 6.6e-11.
```

Diese Zahlen sind **keine Gesamt-Capture-Wahrscheinlichkeit**. Bei `N_enc` relevanten Hill-Passagen und `N_GI` relevanten Giant Impacts skaliert der seltene unabhängige Grenzfall zunächst ungefähr wie

```text
P ~ N_enc * N_GI * (t_res/T_epoch) * P_Jacobi_close,
```

bis Korrelationen, Resonanzen und Sättigung wichtig werden.

Damit ist klar, wo der eigentliche offene Hebel liegt:

```text
repeated encounters / co-orbital residence / long-lived temporary capture
versus
number and mass-ratio distribution of giant impacts.
```

## Was F3 gegenüber F2 ändert

F2 bleibt als korrekter **lokaler kinematischer Existenztest** bestehen, war aber capture-freundlich.

F3 zeigt:

```text
Solar tides + L1/L2 Jacobi barrier
reduce the useful pull-down phase space very strongly.
```

Insbesondere:

```text
delta <=0.03:
no conservative outer-Hill capture found.

delta ~0.10:
nonzero but ~1e-4...1e-3 conditional occupancy fraction.

delta ~0.30:
~few-percent conditional occupancy fraction.
```

Der Giant-Impact-Rescue ist damit **nicht tot**, aber deutlich schmaler als F2 allein vermuten ließ.

## F3 Statusmatrix

| Teiltest | Status | Ergebnis |
|---|---|---|
| adaptive Hill/DOP853 solver | **PASS** | Jacobi drift ~1e-8 median ptp |
| fixed-step deep-encounter RK4 | **FAIL / REJECTED** | spurious capture inflation |
| temporary first Hill passage | **PASS** | dynamically present in injection ensemble |
| `delta=0.01` outer pull-down | **FAIL in sampled gate** | none found |
| `delta=0.03` outer pull-down | **FAIL in sampled gate** | none found |
| `delta=0.10` outer pull-down | **PASS existence / inefficient** | `0.035...0.072%` occupancy |
| `delta=0.30` outer pull-down | **PASS conditional** | `5.65...6.81%` occupancy |
| single-passage random timing | **strongly suppressive** | `~1e-9...1e-10` residence/window before closure factor |
| long-lived multi-pass temporary-capture tail | **OPEN** | first-segment solver does not close it |
| realistic giant-impact mass/time distribution | **OPEN** | must be sampled from N-body formation histories |
| initial solar-bound Seed phase-space density | **OPEN** | F1 origin problem remains |
| absolute Earth-delivery probability | **OPEN** | not identifiable yet |

## Konsequenz

Der Formation/Delivery-Branch kann jetzt enger formuliert werden:

```text
normal halo -> Earth: VERY STRONG FAIL
halo -> protostellar capture: strongly negative
disk gas drag: insufficient
already solar-bound cold seed: OPEN initial condition
smooth terrestrial pull-down: FAIL as generic channel
small giant-impact jumps <=3%: negative in conservative F3 gate
~10% giant impact: narrow surviving channel
~30% giant impact: finite conditional pull-down channel
absolute delivery probability: OPEN.
```

Das ist **keine Evidenz für einen Erdzentrum-BH**. Es ist lediglich der aktuelle quantitative Status des noch offenen Formation-Spezialkanals.

## Nächster harter Test – F3b

F3b muss die größte verbleibende F3-Lücke schließen:

```text
full multi-passage/global CR3BP or direct N-body
-> heliocentric orbital elements a,e,i
-> repeated synodic encounters
-> co-orbital / horseshoe / quasi-satellite regions
-> long-lived temporary-capture residence distribution
-> stochastic impact epochs
-> realistic DeltaM/M distribution
-> permanent-capture probability per solar-bound seed.
```

Erst danach kann entschieden werden, ob repeated residence die starke Timing-Suppression relevant kompensiert oder ob der Formation-Branch praktisch endgültig kollabiert.

## Reproduzierbare Datei

- `stage3_74_f3_hill_monte_carlo.py`

## Schlussstatus

```text
F3 NUMERICAL GATE:
PASS.

F2 GIANT-IMPACT EXISTENCE:
CONFIRMED but strongly narrowed by Hill/Jacobi dynamics.

GENERIC EFFICIENT GIANT-IMPACT DELIVERY:
NOT ESTABLISHED; small/medium jumps strongly suppressed.

ABSOLUTE FORMATION/DELIVERY:
OPEN.

NEXT:
F3b multi-passage / global N-body timing calculation.
```
