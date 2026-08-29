# Stage 3.73 / F2 – Terrestrischer Pull-down-Capture-Audit

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** TEMPORARY HILL CAPTURE PHYSICALLY ALLOWED / SMOOTH TERRESTRIAL PULL-DOWN WEAK / IMPULSIVE MASS-JUMP CAPTURE KINEMATICALLY OPEN

## Ausgangspunkt

F1 hat gezeigt:

```text
normaler Halo -> fertige Erde: FAIL
MMSN gas drag: FAIL
normaler Halo -> kollabierende protosolare Wolke: strongly negative
pre-bound cold/co-moving solar seed: OPEN initial condition.
```

F2 fragt nun:

```text
Wenn der Seed bereits auf einer solar gebundenen,
relativ kalten heliocentrischen Bahn existiert,
kann planetarer Massenaufbau ihn in einen terrestrischen Embryo einfangen?
```

## Testteilchen-Limit

Im Sun+planet restricted-three-body Problem ist ein `1e10...5e11 kg` PBH gegenueber einem Planeten/Embryo dynamisch praktisch masselos.

Damit gelten fuer seine Hill-Sphaeren-Bahndynamik dieselben test-particle Gleichungen wie fuer ein hinreichend kleines Planetesimal. Die PBH-Masse beeinflusst in diesem F2-Orbitaltest nicht die spezifische Bahnenergie.

Literatur zu planetesimalen Testteilchen zeigt:

- temporaere Capture-Orbits innerhalb/nahe der Hill-Sphaere existieren auch fuer kleine Planetenmassen;
- solche Captures koennen viele bis `O(100)` lokale Umlaufzeiten andauern;
- wachsende Planetenmasse kann in geeigneten Faellen einen temporaer gebundenen Koerper durch **pull-down capture** dauerhaft binden.

Diese Literatur etabliert den Mechanismus allgemein, nicht seine Effizienz fuer einen PBH im terrestrischen Erd-Formation-Branch.

## Hill-Sphaeren-Skalen bei 1 AU

```text
R_H = a (M_p/3M_sun)^(1/3).
```

| M_p | R_H | sqrt(2GM_p/R_H) |
|---:|---:|---:|
| `0.001 M_E` | `0.00100 AU` | `~73 m/s` |
| `0.01 M_E` | `0.00216 AU` | `~157 m/s` |
| `0.1 M_E` | `0.00464 AU` | `~339 m/s` |
| `1 M_E` | `0.0100 AU` | `~730 m/s` |

Ein bereits solar gebundener Seed mit sehr kleiner Relativgeschwindigkeit zur terrestrischen Feeding-Zone kann daher temporaer in die Hill-Dynamik eines Embryos eintreten, ohne dass Gasreibung vorausgesetzt werden muss.

## F2a – glattes planetarer Wachstum

Fuer einen einfachen exponentiellen Wachstumsbenchmark

```text
DeltaM/M = exp(T_cap/t_grow)-1
DeltaR_H/R_H = (1+DeltaM/M)^(1/3)-1.
```

Selbst mit einer absichtlich schnellen terrestrischen Wachstumszeit

```text
t_grow=1e5 yr
```

liefert eine temporaere Capture von

```text
10 yr  -> DeltaR_H/R_H ~3.3e-5
50 yr  -> ~1.67e-4
100 yr -> ~3.33e-4.
```

Fuer `1e6...1e7 yr` Wachstum ist die Hill-Sphaeren-Aenderung waehrend derselben Capture nochmals 10...100 mal kleiner.

Da reale terrestrische Akkretion insgesamt ueber viele Myr bis zig Myr verlaeuft und die Erde erst nach einer langen Giant-Impact-Phase fast ihre Endmasse erreicht, ist ein **glatter** Pull-down waehrend einer typischen kurzen temporaeren Capture im terrestrischen Fall stark ineffizient.

```text
smooth terrestrial-mass growth as generic pull-down capture:
WEAK / NOT A ROBUST FORMATION SOLUTION.
```

## F2b – diskreter Massezuwachs / Giant-Impact Sensitivitaet

Ein impulsiver oder sehr schneller Massezuwachs ist dynamisch anders.

Wenn waehrend eines Massezuwachses `DeltaM` ein Testteilchen bei Abstand `r` nahe dem Embryo bleibt, verschiebt sich seine spezifische planetozentrische Energie in einem Reduced-Limit um

```text
Delta epsilon ~= -G DeltaM/r.
```

Ein vorher knapp ungebundenes Teilchen kann dadurch gebunden werden, falls grob

```text
v_rel < sqrt(2 G DeltaM/r).
```

Am heutigen Earth-Hill-Radius als reine Skalierung:

### `DeltaM=0.01 M_E`

```text
r=1.0 R_H -> v_threshold ~73 m/s
r=0.3 R_H -> ~133 m/s
r=0.1 R_H -> ~231 m/s.
```

### `DeltaM=0.1 M_E`

```text
r=1.0 R_H -> ~231 m/s
r=0.3 R_H -> ~421 m/s
r=0.1 R_H -> ~730 m/s.
```

Groessere/deepere Massenspruenge koennen die kinematische Capture-Schwelle in den `few 1e2...1e3 m/s` Bereich verschieben.

Giant impacts sind ein normaler Bestandteil der Endphase terrestrischer Planetenbildung; moderne Reviews betonen, dass Planeten ihr Wachstum typischerweise durch eine Serie grosser Kollisionen abschliessen. Fuer die Erde verlief der gesamte Massenaufbau ueber zig bis etwa hundert Myr.

Daher gilt:

```text
impulsive / giant-impact pull-down capture of an already nearby low-v seed:
KINEMATICALLY POSSIBLE IN REDUCED MODEL.
```

## Was dies NICHT beweist

F2 berechnet keine Wahrscheinlichkeit.

Ein dauerhafter Seed-Einfang verlangt gleichzeitig:

```text
1. Seed already solar-bound / low relative velocity
2. trajectory enters a temporary Earth-embryo Hill capture
3. capture lasts until a sufficiently large rapid mass-change event
4. post-event Jacobi/orbital energy lies in a permanently bound region
5. later scattering/giant impacts do not eject the seed
6. subsequent dynamics bring/retain it in the growing Earth.
```

Der kritische Faktor ist deshalb **phase-space coincidence**, nicht mehr ein fehlender grundlegender Energieverlustmechanismus.

## Aktualisierte Formationmatrix

| Mechanismus | Status |
|---|---|
| late halo -> finished Earth | VERY STRONG FAIL |
| MMSN gas-drag capture | FAIL |
| normal halo -> protostellar cloud | STRONGLY NEGATIVE |
| pre-bound cold/co-moving solar seed | OPEN INITIAL CONDITION |
| temporary Hill capture by terrestrial embryo | PHYSICALLY ALLOWED |
| smooth terrestrial pull-down during typical short capture | WEAK |
| rapid/impulsive mass-growth pull-down | KINEMATICALLY OPEN |
| realistic probability for Earth incorporation | OPEN / NEEDS N-BODY MONTE CARLO |

## Naechster Formation-Pflichtblock

Der naechste wirklich entscheidende Formationstest ist keine weitere Handformel, sondern ein reproduzierbarer Restricted/N-body Monte-Carlo:

```text
Sun
+ growing terrestrial embryo at ~1 AU
+ realistic embryo mass-history / discrete impacts
+ ensemble of already solar-bound low-e, low-i test-particle seeds
-> temporary capture fraction
-> pull-down fraction
-> retention after later impacts
-> final Earth-bound fraction.
```

Damit kann erstmals eine bedingte Wahrscheinlichkeit

```text
P(Earth-bound | pre-bound cold solar seed)
```

bestimmt werden.

Die vorgelagerte Wahrscheinlichkeit dafuer, dass ein solcher cold solar seed ueberhaupt existiert, bleibt separat offen.

## Schlussstatus

```text
F2 result:
A mathematically viable planet-formation capture path exists in principle:
temporary Hill capture + sufficiently rapid planetary mass growth.

For smooth terrestrial growth it is weak.
For discrete rapid mass-growth events it is kinematically open.

Probability / abundance:
NOT YET ESTABLISHED.
```

## Reproduzierbare Datei

- `stage3_73_f2_terrestrial_pull_down_capture.py`
