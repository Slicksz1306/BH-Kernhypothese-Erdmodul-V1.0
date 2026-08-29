# Stage 3.77 / F5 – Restricted 4-body Exchange-Capture Monte-Carlo

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** DIRECT NEWTONIAN ENCOUNTER SOLVER PASS / PERMANENT EXCHANGE-CAPTURE FOUND CONDITIONALLY / GENERIC FORMATION PROBABILITY OPEN

## Ziel

F4 zeigte analytisch, dass ein früher Mehrkörper-Kick ausreichend groß sein kann, um einen bereits solar gebundenen Seed dauerhaft an einen Proto-Earth-Embryo zu binden.

F5 ersetzt den reinen Kick-Gate durch eine direkte Newtonsche Encounter-Integration:

```text
Sun + Proto-Earth M1 + second embryo M2 + massless seed.
```

Die Frage lautet:

```text
Wenn ein solar gebundener/cold Seed bereits in M1s Hill-Region vorhanden ist,
und M2 einen echten hyperbolischen Embryo-Flyby ausführt,
kann die Mehrkörperstreuung einen permanenten M1-Capture erzeugen?
```

Wichtig:

```text
F5 ist auf die enge Embryo-Begegnung UND Seed-Anwesenheit konditioniert.
```

Die Resultate sind daher **keine absolute Solar-System-Delivery-Wahrscheinlichkeit**.

## Literaturkontext

Williams & Zugger, *The Planetary Science Journal* 5, 208 (2024), DOI `10.3847/PSJ/ad5a9a`, demonstrieren collisionless binary-exchange capture durch Earth-sized terrestrische Planeten bei 1 AU. Ihre Capture-Objekte sind massive Binärkomponenten und damit nicht unser einzelner Seed; der relevante Punkt ist, dass terrestrischer collisionless exchange dynamisch möglich ist.

Terrestrische Giant-Impact/N-body-Literatur verwendet die Hill-Geschwindigkeit als natürliche niedrige Embryo-Geschwindigkeitsskala. Ein typischer Skalierungsanker ist

```text
v_H ~0.4 km/s (M_emb/M_E)^(1/3)
```

bei 1 AU für Earth-mass scale embryos; frühe kleinere Embryos liegen entsprechend darunter.

## Direkter Solver

Verwendet werden heliocentrische inertiale Koordinaten mit

```text
G M_sun = 1
a = 1 AU
Omega = 1
```

und DOP853:

```text
rtol = 3e-8
atol = 3e-10
max_step = 0.2 Omega^-1.
```

M1 und M2 fühlen Sonne + gegenseitige Gravitation.

Der Seed ist masselos und fühlt

```text
Sun + M1 + M2.
```

Die Sonnen-Reflexbewegung durch die sehr kleinen Embryomassen wird vernachlässigt.

## Kritische Pilot-Korrektur

Ein erster F5-Pilot setzte

```text
V ~ Omega R_H,mut
```

direkt am nominellen Perizentrum `b=kappa R_H,mut`.

Das ist für `kappa<1` unphysikalisch capture-freundlich, weil die gegenseitige Escape-Speed dort größer sein kann. Dadurch können künstlich embryo-bound Begegnungen entstehen.

**Diese Pilotresultate wurden vollständig verworfen.**

Final wird eine echte hyperbolische asymptotische Geschwindigkeit `V_inf` gesampelt und am Perizentrum gesetzt:

```text
V_p^2 = V_inf^2 + 2 G (M1+M2)/b.
```

In mutual-Hill-Einheiten:

```text
(V_p / (Omega R_H,mut))^2 = u_inf^2 + 6/kappa.
```

Damit ist der M1-M2-Zweig zum Start des Encounter-Fensters hyperbolisch statt künstlich gebunden.

## Gepaarter Kontrolllauf

Jede Initialbedingung wird zweimal integriert:

```text
FULL:
Sun + M1 + M2 + seed

CONTROL:
Sun + M1 + same seed state
M2 mass = 0.
```

Ein F5-Capture wird dem Embryo-Encounter nur zugeschrieben, wenn

```text
FULL -> stable/body success
CONTROL -> not stable and not body.
```

Damit werden Seed-Bahnen ausgeschlossen, die auch ohne M2 zufällig gebunden oder körperkreuzend geworden wären.

## Sampled Parameter

Proto-Earth:

```text
M1 = 1e-3 ... 1e-1 M_E
```

Seed-State am Encounter:

```text
r_seed = 0.1 ... 1.0 r_H,1
v_seed = beta v_esc(local)
beta = 1.00 ... 1.15
random phase and velocity direction.
```

Der Seed ist damit absichtlich ein Hill-region/cold encounter ensemble; dies ist keine Verteilung normaler Halo-PBHs.

### BROAD

```text
q=M2/M1 = 0.03 ... 1
kappa=b/R_H,mut = 0.3 ... 1.5
u_inf=V_inf/(Omega R_H,mut) = 0.5 ... 3
N=300.
```

### STRONG

```text
q = 0.3 ... 1
kappa = 0.3 ... 0.8
u_inf = 0.5 ... 1.5
N=300.
```

### WEAK

```text
q = 0.03 ... 0.1
kappa = 0.9 ... 1.5
u_inf = 1.5 ... 3
N=300.
```

## Kurzlauf bei 3 Omega^-1

### STRONG / N=300

```text
FULL, CONTROL counts

unbound, unbound              269
bound_unstable, unbound         8
stable, unbound                 7
body, body                      6
body, unbound                   4
stable, bound_unstable          3
unbound, stable                 2
unbound, bound_unstable         1
```

Damit existieren im 3-Omega-Gate

```text
10 stable-at-that-time exchange-attributable candidates
4 additional body-crossing candidates.
```

### BROAD / N=300

```text
unbound, unbound              285
body, body                      6
stable, unbound                 3
body, unbound                   3
bound_unstable, unbound         2
unbound, bound_unstable         1
```

### WEAK / N=300

```text
unbound, unbound              277
body, body                     11
unbound, bound_unstable         3
stable, stable                  3
bound_unstable, unbound         3
stable, unbound                 1
stable, bound_unstable          1
bound_unstable, bound_unstable  1
```

Der gepaarte Vergleich zeigt bereits die erwartete Hierarchie:

```text
strong close encounter > broad > weak
```

für neue stable-capture candidates.

## Persistenztest bis 20 Omega^-1

Bei 1 AU gilt

```text
Omega^-1 ~58.13 d
20 Omega^-1 ~3.18 yr.
```

Alle exchange-attributable `stable` und `bound_unstable` Zwischenzustände wurden deshalb erneut bis `20 Omega^-1` integriert.

### STRONG

Von den 10 zunächst stable-attributable Kandidaten:

```text
5 remain stable at 20 Omega^-1
1 intersects the Proto-Earth body
4 become unbound.
```

Alle 8 zusätzlichen `bound_unstable` Kandidaten werden bis 20 Omega^-1 wieder unbound.

Konservativer direkt verifizierter permanent-stable Anteil im konditionierten Strong-Ensemble:

```text
5/300 = 1.67%
95% Wilson ~0.71...3.84%.
```

### BROAD

```text
3/300 remain stable at 20 Omega^-1
2/300 bound_unstable candidates escape.
```

Damit:

```text
persistent stable = 1.00%
95% Wilson ~0.34...2.90%.
```

### WEAK

Die zwei zunächst neuen stable candidates liefern langfristig:

```text
0 remain stable
1 becomes body-crossing
1 escapes.
```

Alle vier zusätzlichen `bound_unstable` Kandidaten entkommen.

Damit:

```text
persistent stable = 0/300
95% upper Wilson ~1.26%.
```

## Eigenschaften der persistenten Captures

Die überlebenden Stable-Captures liegen nach 20 Omega^-1 beispielsweise bei

```text
a_seed/r_H ~0.21 ... 0.58
```

und der zweite Embryo ist dann typischerweise bereits

```text
~55 ... 150 mutual Hill radii
```

entfernt.

Damit sind diese Kandidaten keine künstlichen Zustände, die nur bestehen, solange M2 noch direkt daneben sitzt.

Beispiele persistenter STRONG-Captures:

| M1/M_E | q | kappa | u_inf | final a_seed/r_H |
|---:|---:|---:|---:|---:|
| `0.0532` | `0.330` | `0.472` | `1.252` | `0.380` |
| `0.0159` | `0.817` | `0.466` | `1.373` | `0.281` |
| `0.00339` | `0.341` | `0.314` | `0.714` | `0.414` |
| `0.00330` | `0.606` | `0.395` | `0.602` | `0.214` |
| `0.0193` | `0.962` | `0.503` | `1.435` | `0.302` |

Status:

```text
permanent collisionless embryo-exchange capture:
PASS as conditional numerical existence test.
```

## Body-crossing branch

Zusätzlich treten FULL-only body crossings auf:

```text
STRONG: 4/300
BROAD:  3/300
WEAK:   0/300.
```

Davon besitzen beim Body-Eintritt bereits negative planetozentrische Zwei-Körper-Energie:

```text
STRONG: 2/4
BROAD:  3/3.
```

Diese Zustände sind besonders relevant, weil der Encounter den Seed bereits in einen gebundenen körperkreuzenden Zustand gebracht hat.

Die zwei positiven STRONG-body-crossing Fälle besitzen ungefähr

```text
v_inf ~129 m/s
v_inf ~140 m/s.
```

Selbst der sehr optimistische A19-Dynamical-Friction-Proxy mit `I=30` liefert dort für `M_BH<=5e11 kg` nur

```text
DeltaE_drag/E_inf ~2e-7 ... 3e-7
```

als Maximum.

Damit gilt:

```text
positive-energy one-pass body crossing + ordinary material drag:
FAIL as immediate capture mechanism.
```

Der relevante Body-Zweig sind also die bereits durch Mehrkörperstreuung gebundenen crossings, nicht Reibung eines noch hyperbolischen Seeds.

## Hotter-seed Stresscheck

Zusätzlich wurden Strong-Encounter-Stressproxies mit größeren lokalen Seed-Geschwindigkeiten gerechnet.

```text
beta=1.15...1.50, N=200:
2 stable-at-3-Omega candidates
both remain stable at 20 Omega^-1.

beta=1.50...2.00, N=200:
1 stable-at-3-Omega candidate
remains stable at 20 Omega^-1.
```

Wegen der kleinen Zähler ist dies **kein belastbares Capture-Fraction-Maß**. Es zeigt aber, dass der numerische Exchange-Mechanismus nicht ausschließlich an `beta=1.000...1.01` hängt.

## Was F5 beweist und was nicht

F5 schließt eine zentrale F4-Frage:

```text
Can an actual Newtonian Sun+embryo+embryo encounter
convert a Hill-region seed into a persistent Proto-Earth satellite orbit?

YES in the tested conditional ensembles.
```

F5 schließt ausdrücklich **nicht**:

```text
1. probability that such a seed exists near 1 AU;
2. probability that it occupies M1's Hill region at the embryo encounter;
3. full 3D inclination distribution;
4. realistic correlated terrestrial-formation encounter histories;
5. Myr-Gyr survival through many later embryos/giant impacts;
6. final central settling after body engulfment.
```

Der neue Engpass ist deshalb nicht mehr die lokale Exchange-Kinematik.

Er ist:

```text
TRIPLE-COINCIDENCE PHASE SPACE:
solar-bound seed density
x Hill-region occupancy
x embryo-encounter history.
```

## F5 Statusmatrix

| Teiltest | Status | Ergebnis |
|---|---|---|
| direct Newtonian restricted 4-body solver | **PASS** | Sun+M1+M2+seed integrated |
| low-pericentre-speed pilot | **FAIL / REJECTED** | could create artificial embryo-bound encounters |
| hyperbolic pericentre correction | **PASS** | `V_p^2=V_inf^2+2G(M1+M2)/b` |
| paired M2=0 counterfactual | **PASS** | separates exchange from spontaneous outcomes |
| Strong persistent stable capture | **PASS conditional** | `5/300 = 1.67%` |
| Broad persistent stable capture | **PASS conditional** | `3/300 = 1.00%` |
| Weak persistent stable capture | **NOT FOUND persistent** | `0/300` |
| exchange-induced bound body crossing | **PASS existence** | present in Strong/Broad samples |
| positive-E body crossing + A19 drag | **FAIL** | drag short by ~6–7 orders |
| absolute formation probability | **OPEN** | seed/encounter joint phase space unknown |
| direct BH evidence | **NONE** | this is formation dynamics only |

## Konsequenz

F4s kinematic existence claim survives a much harder direct calculation:

```text
already solar-bound Hill-region seed
+ sufficiently strong hyperbolic embryo encounter
=> persistent Proto-Earth capture is numerically possible.
```

Das ist der stärkste bisher überlebende Formation-Spezialkanal des Projekts.

Aber die Aussage bleibt konditional. Die absolute Delivery-Wahrscheinlichkeit kann erst bestimmt werden, wenn eine reale Population solar gebundener Seeds und eine terrestrial-formation encounter history miteinander gefaltet werden.

## Nächster harter Test – F6

```text
F6 = population-weighted terrestrial formation gate

seed heliocentric a,e,i distribution
+ embryo N-body encounter-rate distribution
+ Hill-occupancy duty cycle
+ F5 conditional capture kernel
+ later survival / engulfment
-> absolute P_delivery per primordial solar-bound seed.
```

Ohne eine physikalisch motivierte Seed-Phasenraumdichte kann F6 mindestens eine **required seed abundance** bzw. einen oberen/unteren Wahrscheinlichkeitsbedarf bestimmen.

## Reproduzierbare Datei

- `stage3_77_f5_restricted_4body_exchange_mc.py`

## Schlussstatus

```text
F5 LOCAL EXCHANGE MECHANISM:
PASS conditionally.

GENERIC FORMATION:
NOT ESTABLISHED.

ABSOLUTE EARTH DELIVERY:
OPEN.

EXPERIMENTAL BH DETECTION:
NONE.
```
