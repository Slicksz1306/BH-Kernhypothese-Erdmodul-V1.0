# Stage 3.73 / F2 – Hill-Sphäre, temporärer Capture und Pull-down durch Embryowachstum

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** STATIC PERMANENT CAPTURE FAIL / SMOOTH PULL-DOWN GENERIC FAIL / GIANT-IMPACT KINEMATIC GATE PASS / TOTAL DELIVERY PROBABILITY OPEN

## Ziel

F1 ließ nach negativem Halo→Erde-, Halo→protostellare-Wolke- und Gasdrag-Test nur noch einen bereits solar gebundenen, kalten Seed als offene Anfangsbedingung übrig.

F2 fragt enger:

```text
Kann ein bereits helioszentrisch/solar gebundener Seed,
der temporär in die Hill-Sphäre eines wachsenden terrestrischen Embryos gerät,
durch zeitabhängiges Embryowachstum permanent gebunden werden?
```

Getestet werden zwei Grenzfälle:

1. langsames/smoothes Pull-down während einer temporären Hill-Capture-Episode;
2. impulsiver Massenzuwachs durch einen Giant Impact, während der Seed innerhalb der Hill-Sphäre ist.

Dies ist ein reduzierter analytischer Energie-/Zeitskalen-Gate-Test. Es ist **noch kein vollständiger N-body-Capture-Wahrscheinlichkeitssolver**.

## Hill-Skalen bei 1 AU

Für einen Embryo der Masse `M_p`:

```text
r_H = a (M_p / (3 M_sun))^(1/3)
Omega = sqrt(G M_sun / a^3)
v_H = Omega r_H
```

Bei `a=1 AU`:

| M_p | r_H [m] | v_H [m/s] | 1/Omega |
|---:|---:|---:|---:|
| `0.01 M_E` | `3.224e8` | `64.19` | `58.13 d` |
| `0.10 M_E` | `6.946e8` | `138.30` | `58.13 d` |
| `0.50 M_E` | `1.188e9` | `236.49` | `58.13 d` |
| `1.00 M_E` | `1.497e9` | `297.96` | `58.13 d` |

Die Hill-Dynamik ist damit für einen kalten, bereits solar gebundenen Seed im Bereich `O(10^2 m/s)` relevant – fundamental anders als der A19-Halo-Test mit `v_inf~220 km/s`.

## Statischer Hill-Capture

Ein statischer zirkularer Drei-Körper-Hill-Eintritt kann **temporäre** Capture-Orbits erzeugen. Ohne dissipativen Prozess oder zeitabhängige Potentialänderung wird daraus jedoch nicht generisch permanente Bindung.

F2 übernimmt daher:

```text
temporary Hill capture: dynamically allowed
static permanent capture without dissipation/mass evolution: FAIL as generic mechanism
```

## Impulsiver Pull-down durch Massenzuwachs

Befindet sich der Seed beim Massensprung `Delta M` im Abstand

```text
r = f r_H
```

vom Embryo, ändert sich seine spezifische planetozentrische Energie näherungsweise um

```text
Delta epsilon = -G DeltaM / r.
```

Ein zuvor schwach ungebundener Zustand mit planetozentrischem hyperbolischem Überschuss `v_inf` kann nach dem Sprung gebunden sein, wenn

```text
0.5 v_inf^2 < G DeltaM / r.
```

Mit

```text
delta = DeltaM/M_p
```

folgt

```text
v_inf,max = sqrt(2 G delta M_p / (f r_H))
          = sqrt(6 delta/f) v_H.
```

Wichtig: Die Seed-/PBH-Masse kürzt sich aus dieser spezifischen Energiebedingung heraus. Der F2-Gate gilt daher gleichermaßen für den Projektbereich `1e10...5e11 kg`, solange der Seed als Testmasse gegenüber dem Embryo behandelt werden kann.

Dies ist bewusst ein lokaler, capture-freundlicher Instantaneous-Potential-Proxy. Ein realer Giant Impact verändert zusätzlich Schwerpunkt, Impuls, Geometrie und zeitabhängiges Mehrkörperpotential; diese Effekte müssen in F3 explizit integriert werden.

## Numerischer Giant-Impact-Gate am Hill-Rand

Für `f=1`:

| M_p | delta=0.01 | delta=0.10 | delta=0.30 |
|---:|---:|---:|---:|
| `0.01 M_E` | `15.72 m/s` | `49.72 m/s` | `86.13 m/s` |
| `0.10 M_E` | `33.88 m/s` | `107.13 m/s` | `185.55 m/s` |
| `0.50 M_E` | `57.93 m/s` | `183.19 m/s` | `317.29 m/s` |
| `1.00 M_E` | `72.99 m/s` | `230.80 m/s` | `399.76 m/s` |

Damit existiert ein nichtverschwindender kinematischer Capture-Bereich für bereits kalte, solar gebundene Seeds.

Beispiel `1 M_E`, `delta=0.10`:

```text
r = 1.0 r_H -> v_inf,max ~230.8 m/s
r = 0.5 r_H -> v_inf,max ~326.4 m/s
r = 0.1 r_H -> v_inf,max ~729.9 m/s
r = 0.01 r_H -> v_inf,max ~2308 m/s.
```

Das ist ein **PASS des kinematischen Existenztests**, nicht der Aussage, dass der reale Seed mit ausreichender Wahrscheinlichkeit genau dann dort ist.

## Langsames Pull-down

Für glattes Wachstum mit Wachstumsskala

```text
tau_grow = M_p / Mdot_p
```

und temporärer Aufenthaltszeit `t_res` ist die während des Aufenthalts akkumulierte relative Massenänderung höchstens näherungsweise

```text
delta_eff ~ t_res/tau_grow.
```

Um den Test absichtlich capture-freundlich zu machen, behandeln wir diese gesamte Änderung als wäre sie impulsiv. Das ist eine **obere Grenze**; reale adiabatische Entwicklung kann weniger effizient sein.

Für `1 M_E`, `r=r_H`:

| tau_grow | t_res | delta_eff | optimistisches v_inf,max |
|---:|---:|---:|---:|
| `1 Myr` | `1 yr` | `1e-6` | `0.730 m/s` |
| `1 Myr` | `10 yr` | `1e-5` | `2.308 m/s` |
| `1 Myr` | `100 yr` | `1e-4` | `7.299 m/s` |
| `10 Myr` | `1 yr` | `1e-7` | `0.231 m/s` |
| `10 Myr` | `10 yr` | `1e-6` | `0.730 m/s` |
| `10 Myr` | `100 yr` | `1e-5` | `2.308 m/s` |
| `100 Myr` | `1 yr` | `1e-8` | `0.073 m/s` |
| `100 Myr` | `10 yr` | `1e-7` | `0.231 m/s` |
| `100 Myr` | `100 yr` | `1e-6` | `0.730 m/s` |

Terrestrische Akkretion läuft über Myr- bis 10–100-Myr-Skalen. Gegen typische Hill-Aufenthaltszeiten ist normales glattes Wachstum deshalb zu langsam, um einen breiten permanenten Capture-Kanal zu erzeugen.

Status:

```text
smooth terrestrial pull-down as generic mechanism: FAIL
very long-lived near-separatrix temporary captures: OPEN tail, not established as efficient
```

## Timing-Penalty eines Giant Impact

Der impulsive Mechanismus verlangt zusätzlich, dass der Seed **während** des Massensprungs in der relevanten Hill-Phase liegt.

Eine einfache Hill-Durchgangszeit ist

```text
2/Omega ~0.318 yr
```

bei 1 AU.

Wenn man rein illustrativ einen einzelnen unabhängigen Hill-Durchgang zufällig in ein Akkretionsfenster legt, ergibt sich

```text
0.318 yr / 10 Myr  ~3.18e-8
0.318 yr / 100 Myr ~3.18e-9.
```

Dies ist ausdrücklich **keine Capture-Wahrscheinlichkeit**: wiederholte Hill-Begegnungen, resonante/co-orbitale Zustände und langdauernde temporary captures können die effektive Aufenthaltszeit stark verändern. Der Proxy zeigt nur, dass der Timing-Faktor nicht ignoriert werden darf.

## Literaturkontext

- Temporäre Hill-Capture-Orbits helioszentrischer Kleinkörper in Drei-Körper-Dynamik sind etabliert; niedrige Relativenergien nahe den Lagrangepunkten sind dabei zentral (Suetsugu et al., MNRAS 431, 1709, 2013).
- Pull-down capture durch schnelles Planetenwachstum ist als realer Mechanismus numerisch demonstriert worden; Hansen (Science Advances 5, eaaw8665, 2019) findet stark sinkende Effizienz, wenn das Wachstum gegenüber der relevanten orbitalen Dynamik zu langsam wird, in seinem Modell insbesondere für Wachstumszeiten >~30 Orbitalzeiten.
- Terrestrische Planeten wachsen über eine Giant-Impact-Phase von grob `10...100 Myr`; moderne Reviews setzen die Mond-formende Endphase der Erdentstehung in den Bereich vieler zehn Myr (Morbidelli et al. 2012; Halliday & Canup 2023; Marchi & Korenaga 2025).

## F2 Statusmatrix

| Teilfrage | Status | Aussage |
|---|---|---|
| temporärer Hill-Capture eines solar gebundenen kalten Seeds | **PASS / known dynamics** | temporäre Bindung ist dynamisch möglich |
| statischer Übergang zu permanenter Bindung | **FAIL** | ohne Dissipation oder Potentialänderung kein generischer Rescue |
| normales smoothes terrestrisches Wachstum | **FAIL als generischer Kanal** | Massenänderung pro Hill-Aufenthalt zu klein |
| extrem lang lebender separatrix-naher Temporary-Capture | **OPEN** | benötigt N-body-Verweilzeitverteilung |
| impulsiver Giant-Impact-Massensprung | **PASS kinematic existence** | für `delta~0.01...0.30` entstehen Capture-Schwellen von `O(10...400 m/s)` am Hill-Rand |
| reale Seed-Phasenraumdichte | **OPEN** | F1-Ursprungsproblem bleibt |
| Seed innerhalb Hill-Sphäre beim Impact | **OPEN / probability bottleneck** | Timing und Wiederholungsbegegnungen fehlen |
| Gesamtmechanismus F2 | **OPEN** | nicht ausgeschlossen, aber keine belastbare Delivery-Wahrscheinlichkeit |

## Konsequenz für A19/F1

F2 ändert **nicht** die früheren negativen Resultate:

```text
normal halo -> direct Earth: VERY STRONG FAIL
normal halo -> protostellar cloud: strongly negative
protoplanetary gas drag capture: insufficient
```

Neu ist nur:

```text
already solar-bound + dynamically cold seed
+ temporary Hill residence
+ sufficiently rapid embryo mass jump
=> permanent capture is kinematically possible.
```

Der Formation/Delivery-Block ist damit nicht mehr ausschließlich ein Energieproblem. Der verbleibende Engpass ist jetzt eine **Phasenraum-/Timing-Wahrscheinlichkeit**.

## Nächster harter Test

```text
F3 = restricted/N-body Monte-Carlo:
solar-bound seed orbital distribution
-> repeated Hill encounters
-> temporary-capture residence-time distribution
-> stochastic embryo growth / giant-impact epochs
-> permanent-capture fraction.
```

F3 muss mindestens über `a,e,i`, Encounter-Phase, Embryomasse und `DeltaM/M` scannen. Erst daraus kann eine belastbare Delivery-Wahrscheinlichkeit statt nur einer Existenzbedingung entstehen.

## Reproduzierbare Datei

- `stage3_73_f2_hill_pulldown_capture.py`

## Schlussstatus

```text
F2 ENERGY GATE:
NOT EXCLUDED.

SMOOTH PULL-DOWN:
FAIL as generic terrestrial mechanism.

GIANT-IMPACT PULL-DOWN:
PASS as kinematic existence test.

TOTAL FORMATION/DELIVERY:
OPEN; probability not established.

experimental BH detection:
NONE.
```
