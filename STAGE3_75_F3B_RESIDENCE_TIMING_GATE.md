# Stage 3.75 / F3b – Multi-Pass / Co-orbital Residence Timing Gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** MULTI-PASS RESIDENCE AMPLIFICATION PASS / GENERIC RANDOM-IMPACT TIMING RESCUE FAIL / ABSOLUTE DELIVERY PROBABILITY OPEN

## Ziel

Stage 3.74 / F3 zeigte für die erste zusammenhängende Hill-Passage bei 1 AU nur etwa

```text
mean first residence ~35.3 d.
```

Der damit verbundene zufällige Timingfaktor gegenüber einer `10...100 Myr` langen terrestrischen Akkretionsphase ist extrem klein.

F3b prüft, ob bekannte wiederholte Begegnungen, temporäre Erd-Satellitenbahnen und co-orbitale Zustände diese Timing-Suppression um genügend Größenordnungen vergrößern können.

Die zentrale Größe ist dabei nicht die Anzahl der Umläufe, sondern

```text
cumulative capture-eligible Hill residence time.
```

Für einen zufällig verteilten impulsiven Massensprung kann ein Seed nur dann profitieren, wenn der Massensprung zeitlich mit einem capture-fähigen Hill-Zustand überlappt.

## Literaturanker

### Earth temporary captured orbiters

Granvik, Vaubaillon & Jedicke, Icarus 218, 262–277 (2012), DOI `10.1016/j.icarus.2011.12.003`:

```text
mean Earth TCO capture duration = 286 +/-18 d
mean revolutions during capture = 2.88 +/-0.82.
```

Damit ist ein realistisch modellierter Earth-TCO im Mittel deutlich langlebiger als F3s erste Hill-Passage.

### 2020 CD3

De la Fuente Marcos & de la Fuente Marcos, MNRAS 494, 1089–1097 (2020), DOI `10.1093/mnras/staa659`:

```text
median capture duration ~4 yr
some clone trajectories remained geocentric for nearly a century.
```

Damit existiert ein echter long-lived Tail.

### Co-orbitale / Horseshoe-Zustände

Kaplan & Cengiz, MNRAS 496, 4420–4429 (2020), DOI `10.1093/mnras/staa1803`, finden für konkrete Earth-Horseshoe-Kandidaten co-orbitale Zustände von grob

```text
~900 yr
~2700 yr
~3300 yr.
```

Wichtig:

```text
co-orbital lifetime != Hill-sphere residence time.
```

Ein Horseshoe-Objekt verbringt den Großteil einer solchen Resonanzphase **nicht** innerhalb der Hill-Sphäre. F3b benutzt `3300 yr` deshalb nur in einem absichtlich unrealistischen Stress-Gate, in dem 100% dieser Zeit als Hill-residence behandelt werden. Das liefert eine obere Grenze, keinen realistischen Wert.

### Temporary-capture efficiency

Higuchi & Ida (2017) erhalten im zirkularen Grenzfall eine temporäre Capture-Wahrscheinlichkeit von ungefähr

```text
~0.1% der Hill-sphere encounters.
```

Dieser Faktor wird **nicht** in die F3b-Hauptzahlen multipliziert, weil die Projekt-Anfangsbedingung bereits einen speziell kalten, solar gebundenen Seed voraussetzt und dessen reale Orbitalverteilung unbekannt ist. Er zeigt jedoch, dass temporäre Capture selbst nicht automatisch bei jedem Hill-Eintritt auftritt.

## Residence-Amplifikation gegenüber F3

F3 first passage:

```text
35.3 d = 0.0966 yr.
```

Daraus folgen die reinen Verweilzeit-Verstärkungen:

| Zustand | angenommene cumulative residence | Verstärkung gegen F3 |
|---|---:|---:|
| F3 first passage | `35.3 d` | `1x` |
| publizierter mittlerer Earth TCO | `286 d` | `~8.1x` |
| 2020 CD3 median | `4 yr` | `~41.5x` |
| extremer ~100-yr Clone-Tail | `100 yr` | `~1.04e3x` |
| 3300-yr co-orbital **100%-Hill upper bound** | `3300 yr` | `~3.42e4x` |

Damit ist die erste Teilfrage klar:

```text
multi-pass / long-lived residence enhancement exists:
PASS.
```

Aber F3 hatte eine Timing-Lücke von ungefähr `1e8...1e9` gegenüber Myr-Zeitskalen. Selbst ein 100-jähriger Extremtail gewinnt nur rund drei Größenordnungen zurück.

## Random-impact Timingmodell

Für eine gesamte capture-fähige Verweilzeit `t_res`, eine Formationsepoche `T` und `N_GI` unabhängige relevante impulsive Massensprünge wird als transparentes Nullmodell verwendet:

```text
P_overlap = 1 - exp[-N_GI t_res/T].
```

Für kleine Werte:

```text
P_overlap ~= N_GI t_res/T.
```

Die Werte

```text
N_GI = 1, 10, 100
```

sind reine Stress-Scan-Parameter. Es wird **nicht behauptet**, dass die Erde 100 geeignete `DeltaM/M=0.1...0.3` Giant Impacts erfahren hätte.

## 10-Myr-Stressscan – Timing allein

### Mittlerer Earth TCO: 286 d

```text
N_GI=1   -> P_overlap ~7.83e-8
N_GI=10  -> P_overlap ~7.83e-7
N_GI=100 -> P_overlap ~7.83e-6.
```

Selbst wenn **jeder** überlappende Impact garantiert permanent capturen würde, bleibt der Zufallsoverlap damit winzig.

### 2020-CD3-artiger 4-yr Capture

```text
N_GI=1   -> ~4.00e-7
N_GI=10  -> ~4.00e-6
N_GI=100 -> ~4.00e-5.
```

### Extremtail 100 yr

```text
N_GI=1   -> ~1.00e-5
N_GI=10  -> ~1.00e-4
N_GI=100 -> ~9.995e-4.
```

Auch ein bereits sehr extremer 100-jähriger temporärer Capture erreicht bei zehn geeigneten Impacts über 10 Myr nur etwa

```text
1e-4 overlap probability
```

vor jedem weiteren dynamischen Capture-Gate.

### 3300-yr co-orbital Stress-UPPER-BOUND

Wenn man physikalisch unrealistisch die **gesamten 3300 yr** als ununterbrochene Hill-residence behandelt:

```text
N_GI=1   -> P_overlap ~3.30e-4
N_GI=10  -> P_overlap ~3.29e-3
N_GI=100 -> P_overlap ~3.25e-2.
```

Dies ist eine echte obere Grenze für diesen Stressfall. Reale Horseshoe-/co-orbitale Objekte verbringen nur einen Teil ihrer Zeit in Hill-Nähe, daher muss der reale Wert darunter liegen.

## Recoupling an F3 Jacobi-Closure

F3s konservativer `r>=0.1 r_H`-Gate lieferte über die dokumentierten Läufe im Mittel ungefähr

```text
DeltaM/M=0.10:
P_Jacobi ~6.06e-4.

DeltaM/M=0.30:
P_Jacobi ~6.34e-2.
```

Diese Faktoren sind **first-passage-Ensemble-Proxies**, keine exakt bekannten Closure-Wahrscheinlichkeiten eines bereits gebundenen TCO. F3b zeigt sie deshalb nur als zusätzliche Skalierung; der stärkere Schluss folgt bereits aus `P_overlap` allein.

Für den publizierten mittleren Earth-TCO (`286 d`) und `T=10 Myr`:

### N_GI=10

```text
P_overlap               ~7.83e-7
P_overlap * P_Jacobi10  ~4.74e-10
P_overlap * P_Jacobi30  ~4.96e-8.
```

Für einen `4 yr` langen CD3-artigen Capture:

```text
N_GI=10:
P_overlap               ~4.00e-6
P_overlap * P_Jacobi10  ~2.42e-9
P_overlap * P_Jacobi30  ~2.53e-7.
```

Für den `100 yr` Extremtail:

```text
N_GI=10:
P_overlap               ~9.9995e-5
P_overlap * P_Jacobi10  ~6.06e-8
P_overlap * P_Jacobi30  ~6.33e-6.
```

## Warum Multi-Pass die Timing-Lücke nicht schließt

Der wichtige Punkt ist dimensionslos:

```text
mean TCO / 10 Myr ~7.8e-8
4 yr / 10 Myr     ~4e-7
100 yr / 10 Myr   ~1e-5.
```

Der TCO-/Multi-Pass-Mechanismus gewinnt also reale Faktoren von `~8` bis `~10^3` gegenüber F3s First-Pass zurück.

Benötigt würden jedoch ohne starke Korrelationen typischerweise viele weitere Größenordnungen, um eine zufällig platzierte Giant-Impact-Sequenz mit einer seltenen capture-fähigen Seed-Phase zuverlässig zusammenzubringen.

Daher:

```text
multi-pass residence as a real amplification mechanism:
PASS.

multi-pass residence as a generic cure of the Myr random-impact timing penalty:
FAIL.
```

## Was F3b NICHT ausschließt

F3b ist kein mathematischer Beweis, dass Pull-down niemals stattfinden kann.

Offen bleiben Spezialfälle:

```text
1. ein Seed mit sehr viel größerer cumulative Hill occupancy als bekannte TCO-Anker;
2. eine langlebige, impact-korrelierte quasi-satellite/circumplanetary Phase;
3. viele wiederholte temporäre Captures desselben Seeds;
4. andere dissipative Mechanismen während der Embryophase;
5. eine nicht-zufällige Korrelation zwischen Seed-Dynamik und Impaktor-Dynamik;
6. ein Seed, der bereits vor dem finalen terrestrischen Wachstum permanent an den Embryo gebunden war.
```

Punkt 6 wäre jedoch keine Rettung durch F3b, sondern eine **noch frühere Formation-/Capture-Anfangsbedingung**, deren Ursprung separat hergeleitet werden müsste.

## F3b Statusmatrix

| Teiltest | Status | Ergebnis |
|---|---|---|
| reale Multi-Pass/TCO-Existenz | **PASS** | Earth-TCOs und mehrjährige Captures beobachtet/numerisch rekonstruiert |
| mittlere Earth-TCO residence | **CALCULATED / literature anchored** | `286 +/-18 d`, `2.88 +/-0.82 rev` |
| long-lived Earth capture tail | **PASS existence** | CD3 ~4 yr median; einzelne Clones ~100 yr |
| co-orbital/horseshoe longevity | **PASS existence** | `O(10^3 yr)` möglich |
| co-orbital lifetime = Hill occupancy | **REJECTED** | darf nicht gleichgesetzt werden |
| residence amplification vs F3 | **PASS** | ~8x mean, ~42x CD3, ~1e3x extreme tail |
| random-impact timing rescue | **FAIL as generic mechanism** | selbst extreme tails bleiben kurz gegen Myr epoch |
| F3 Jacobi closure after overlap | **still restrictive** | besonders `DeltaM/M~0.10` |
| absolute capture per cold solar-bound seed | **OPEN** | full orbital history fehlt |
| origin/abundance of cold solar-bound seed | **OPEN** | F1 bottleneck bleibt |

## Formation-Branch nach F3b

```text
normal halo -> Earth:
VERY STRONG FAIL

halo -> protostellar cloud:
strongly negative

disk gas drag:
insufficient

already solar-bound dynamically cold seed:
OPEN initial condition

smooth pull-down:
FAIL

small GI jumps <=3%:
negative in F3 conservative gate

10% GI:
kinematically survives, but Jacobi phase-space + timing extremely restrictive

30% GI:
finite conditional Jacobi channel, but random timing remains strongly suppressive

multi-pass/TCO timing rescue:
FAIL as generic mechanism

absolute delivery:
OPEN, now confined to increasingly special correlated/early-bound scenarios.
```

## Nächster harter Test – F4

F3b zeigt, dass eine weitere reine Residence-Verlängerung keine plausible generische Rettung liefert. Der sinnvollste nächste Formationstest ist deshalb nicht einfach ein noch längerer First-Pass-Solver, sondern:

```text
F4 = early permanent embryo-bound seed test

Question:
Could the cold solar-bound seed become permanently bound to a small embryo
BEFORE the late giant-impact epoch, through three-body exchange / embryo-embryo
encounters / early dissipative disk conditions?
```

Alternativ kann ein vollständiger globaler direct-N-body Formation-run den gesamten F1–F3b-Kanal simultan abbilden. Ohne eine physisch motivierte Anfangsverteilung des Seeds würde aber auch dieser nur eine bedingte Wahrscheinlichkeit liefern.

## Reproduzierbare Datei

- `stage3_75_f3b_residence_timing_gate.py`

## Schlussstatus

```text
MULTI-PASS RESIDENCE:
PASS as a real dynamical amplification.

GENERIC GI TIMING RESCUE:
FAIL.

GIANT-IMPACT PULL-DOWN EXISTENCE:
NOT mathematically eliminated, but increasingly fine-tuned.

ABSOLUTE FORMATION/DELIVERY:
OPEN.

EXPERIMENTAL BH DETECTION:
NONE.
```
