# Stage 3.76 / F4 – Early permanent embryo-bound seed

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** COLLISIONLESS EXCHANGE KINEMATIC PASS / STABLE EMBRYO-BOUND ORBITS PASS / GROWTH-ASSISTED ENGULFMENT CONDITIONAL PASS / ABSOLUTE DELIVERY PROBABILITY OPEN

## Ziel

F3/F3b haben gezeigt:

```text
single Hill passage + zufälliger Giant Impact:
strong timing suppression

multi-pass / temporary capture:
real, but generically insufficient to remove Myr timing penalty.
```

F4 testet deshalb einen qualitativ anderen Formation-Branch:

```text
already solar-bound cold seed
-> correlated embryo-embryo / exchange encounter
-> permanent early satellite-like binding to Proto-Earth
-> subsequent growth drives the orbit deeper
-> eventual embryo crossing / engulfment
-> repeated interior passages damp toward the centre.
```

Dieser Mechanismus benötigt **keinen zufälligen späteren Impact während einer kurzen Hill-Passage**. Der Energieaustausch und die Capture-Geometrie entstehen im selben Mehrkörperereignis.

F4 ist ein reduzierter analytischer Gate-Test, kein vollständiger terrestrial-formation N-body-Solver.

## Literaturanker

### Collisionless capture bei terrestrischen Planeten

Williams & Zugger, *The Planetary Science Journal* 5, 208 (2024), DOI `10.3847/PSJ/ad5a9a`, zeigen in direkten numerischen Experimenten, dass collisionless binary-exchange capture selbst für Earth-sized terrestrische Planeten bei 1 AU möglich ist. In ihrem konkreten Modell wird nach einer Begegnung eine Komponente eines großen terrestrischen Binaries ausgeworfen und die andere permanent an den Planeten gebunden.

Das ist **kein direkter Wahrscheinlichkeitswert für unseren einzelnen Seed**. Es etabliert aber, dass terrestrische Collisionless-Exchange-Capture kein prinzipiell verbotener Mechanismus ist.

Li et al., *Astronomy & Astrophysics* 638, A139 (2020), DOI `10.1051/0004-6361/201936672`, zeigen außerdem mit N-body-Simulationen, dass Satelliten während enger Planetenbegegnungen von einem Planeten auf einen anderen übertragen werden können; in ihrem Neptune-Regime erreicht die Capture-Wahrscheinlichkeit bei Penetration des Donor-Satellitensystems Größenordnung `~10%`. Dieser Wert wird hier **nicht** auf terrestrische Embryos übertragen; relevant ist nur die demonstrierte Mehrkörper-Energieaustauschphysik.

### Hill-Stabilitätszone

Domingos, Winter & Yokoyama, MNRAS 373, 1227 (2006), DOI `10.1111/j.1365-2966.2006.11104.x`, finden für kleine Exzentrizitäten im zirkularen Grenzfall ungefähr:

```text
prograde stable to  a ~0.4895 r_H
retrograde stable to a ~0.9309 r_H.
```

Die exakten Grenzen hängen von Planeten- und Satellitenexzentrizität ab. F4 benutzt die zirkularen Werte als transparenten Referenz-Gate.

Neuere Arbeiten zu räumlicher temporary capture im Sun-planet CR3BP bestätigen weiterhin große Familien räumlicher temporärer Capture-Bahnen (MNRAS 543, 625, 2025, DOI `10.1093/mnras/staf1430`).

## 1. Frühe Hill-Skalen

Bei 1 AU:

```text
r_H = a (M_p/(3 M_sun))^(1/3)
v_H = Omega r_H.
```

| M_p/M_E | r_H [km] | v_H [m/s] | prograde stable < [km] | retrograde stable < [km] |
|---:|---:|---:|---:|---:|
| `0.001` | `149655` | `29.80` | `73256` | `139313` |
| `0.010` | `322421` | `64.19` | `157825` | `300142` |
| `0.030` | `465012` | `92.58` | `227623` | `432879` |
| `0.100` | `694635` | `138.30` | `340024` | `646636` |

Damit existiert selbst für sehr kleine Proto-Earth-Embryos eine große dynamisch stabile satellite-like Region.

Status:

```text
stable permanent embryo-bound phase space after successful exchange:
PASS / known celestial mechanics.
```

## 2. Wie groß muss der Mehrkörper-Kick sein?

Wir betrachten einen capture-freundlichen Seed, der bei

```text
r = f r_H
```

nahe einer lokal parabolischen planetozentrischen Bahn liegt.

Mit

```text
G M_p / r_H = 3 v_H^2
```

ist die lokale Escape-Geschwindigkeit

```text
v_esc/v_H = sqrt(6/f).
```

Soll ein optimal antiparalleler Impuls den Seed auf eine Bahn mit

```text
a_s = alpha r_H
```

bringen, ist der minimale Energie-Kick

```text
Delta v_req/v_H
= sqrt(6/f) - sqrt(6/f - 3/alpha).
```

Bei `f=0.3`:

```text
prograde target alpha=0.4895:
Delta v_req ~0.748 v_H

retrograde target alpha=0.9309:
Delta v_req ~0.376 v_H.
```

Physikalisch:

| M_p | prograde kick @0.3 r_H | retrograde kick @0.3 r_H |
|---:|---:|---:|
| `0.01 M_E` | `48.0 m/s` | `24.1 m/s` |
| `0.03 M_E` | `69.2 m/s` | `34.8 m/s` |
| `0.10 M_E` | `103.4 m/s` | `52.0 m/s` |

Diese Skala ist deutlich kleiner als km/s und liegt direkt in der Hill-/Embryo-Encounter-Dynamik.

## 3. Embryo–Embryo differential impulse

Für einen zweiten Embryo

```text
M_2 = q M_1
```

verwenden wir einen einfachen tidal-impulse Stressproxy.

Bei Seed-Abstand `r=f r_H,1`, Perturber-Impactparameter

```text
b = kappa R_H,mut
```

und Encounter-Speed

```text
V ~ Omega R_H,mut
```

ergibt die straight-line Tidal-Näherung

```text
Delta v_rel/v_H,1
~ 6 q f / [kappa^2 (1+q)].
```

Diese Formel ist nur ein Größenordnungs-Gate; bei `b~r` ist die Tidal-/Straight-line-Näherung bereits marginal und ein echter 4-body/N-body-Solver nötig.

Für `f=0.3`:

| q=M2/M1 | kappa | Delta v_rel/v_H |
|---:|---:|---:|
| `0.10` | `1.0` | `0.164` |
| `0.10` | `0.5` | `0.655` |
| `0.30` | `1.0` | `0.415` |
| `0.30` | `0.7` | `0.848` |
| `1.00` | `1.0` | `0.900` |

Damit liegt der differentielle Mehrkörper-Kick bei engen Begegnungen mit `q~0.3...1` **genau in der Größenordnung**, die der stabile Capture-Gate verlangt.

Beispiel:

```text
q=0.3
kappa=0.7
f=0.3

Delta v_tide ~0.848 v_H

required:
prograde ~0.748 v_H
retrograde ~0.376 v_H.
```

Status:

```text
embryo-embryo scattering has sufficient energy scale for permanent capture:
PASS as kinematic existence test.
```

## 4. Orientation-only Stressproxy

Wenn die Kickrichtung absichtlich als isotrop behandelt wird, kann man als reinen Energieproxy die Fraktion der Richtungen bestimmen, die genügend Energie entfernen.

Für festen Kick `d=Delta v/v_H` und einen lokal parabolischen Zustand ist

```text
v d cos(theta) + d^2/2 < -3/(2 alpha)
```

nötig.

Dieser Proxy ignoriert Angular-Momentum-Constraints, Encounter-Korrelationen, Solar-Tide-Geometrie und das reale Mehrkörperproblem. Er ist **keine Capture-Wahrscheinlichkeit**.

Bei `f=0.3`:

| q | kappa | d/v_H | energy-only prograde fraction | energy-only retrograde fraction |
|---:|---:|---:|---:|---:|
| `0.10` | `0.50` | `0.655` | `0` | `18.8%` |
| `0.30` | `0.70` | `0.848` | `4.85%` | `24.0%` |
| `1.00` | `1.00` | `0.900` | `6.90%` | `25.0%` |

Das Ergebnis dient nur als Sanity Check:

```text
capture-compatible kick orientations are not measure-zero
once a sufficiently strong correlated embryo encounter occurs.
```

Die echte conditional probability bleibt **OPEN**.

## 5. Growth-assisted orbital engulfment

Ein früh permanent gebundener Seed löst das F3b-Timingproblem nur dann endgültig, wenn er später in den wachsenden Embryo gelangt.

Im idealisierten adiabatischen Grenzfall langsamer isotroper Massenzunahme gilt für eine Testteilchenbahn:

```text
a_s ∝ 1/M_p
```

bei ungefähr erhaltener Exzentrizität.

Für einen constant-density Embryo gilt gleichzeitig

```text
R_p ∝ M_p^(1/3).
```

Damit fällt

```text
a_s/R_p ∝ M_p^(-4/3).
```

Ein bereits gebundener Orbit wird also relativ zur wachsenden Oberfläche **sehr schnell tiefer**.

Startet die Bahn bei

```text
a_i = f r_H(M_i),
```

dann wird im adiabatischen Proxy die Oberfläche erreicht bei

```text
M_engulf/M_E
= (M_i/M_E) [f (r_H,E/R_E)]^(3/4).
```

Mit

```text
r_H,E/R_E ~234.90
```

folgt die späteste Capture-Masse, die bis `1 M_E` noch engulfed wird:

| initial f=a/r_H | max M_i/M_E für Engulfment bis 1 M_E |
|---:|---:|
| `0.05` | `0.158` |
| `0.10` | `0.0937` |
| `0.30` | `0.0411` |
| prograde edge `0.4895` | `0.0285` |
| retrograde edge `0.9309` | `0.0176` |

Beispiele für `M_i=0.01 M_E`:

```text
f=0.10 -> engulf at ~0.107 M_E
f=0.30 -> engulf at ~0.243 M_E
f=0.4895 -> engulf at ~0.351 M_E
f=0.9309 -> engulf at ~0.569 M_E.
```

Das ist ein überraschend starker Early-Capture-Hebel:

```text
capture before a few percent Earth mass
+ stable orbit
+ sufficiently smooth subsequent growth
=> physical engulfment before final Earth mass is natural in the adiabatic limit.
```

### Wichtiger Gegenstress: impulsives Wachstum

Der `a∝1/M`-Shrink gilt nicht für einen einzigen späten Massensprung. Wenn die gesamte Restmasse impulsiv addiert würde, schrumpft eine anfangs kreisförmige Bahn wesentlich weniger.

Daher:

```text
adiabatic/sufficiently granular growth engulfment:
PASS in idealized limit

single-late-jump growth:
DOES NOT reproduce the same inward contraction

realistic stochastic accretion history:
OPEN.
```

## 6. Direkter Nebel-Gasdrag

F1 bleibt unverändert:

```text
naked compact seed + protoplanetary disk gas drag:
insufficient / FAIL as generic capture mechanism.
```

F4 benötigt diesen Kanal nicht für die initiale permanent binding.

## 7. Nach dem Engulfment: repeated interior crossings

Sobald die Bahn die feste/flüssige Proto-Earth schneidet, tritt der Seed wiederholt durch dichte Materie.

Als absichtlich optimistischen Anschluss an A19 verwenden wir denselben Dynamical-Friction-Proxy:

```text
F_df ~ 4 pi G^2 M_BH^2 rho I / v^2
I = 30.
```

Bei

```text
v ~ v_esc
```

und einem diameter crossing durch einen uniform-density Embryo vereinfacht sich die fraktionale Energieänderung pro Passage ungefähr zu

```text
DeltaE/|E_orb| ~ 6 I M_BH/M_p.
```

Für constant density ist die Surface-Orbitalperiode etwa

```text
T_surface ~1.406 h.
```

Daraus ergibt sich ein optimistischer Energie-e-folding-Zeitscale:

| M_p | 1e10 kg | 1e11 kg | 2e11 kg | 5e11 kg |
|---:|---:|---:|---:|---:|
| `0.01 M_E` | `5.32 Myr` | `0.532 Myr` | `0.266 Myr` | `0.106 Myr` |
| `0.03 M_E` | `15.96 Myr` | `1.60 Myr` | `0.798 Myr` | `0.319 Myr` |
| `0.10 M_E` | `53.2 Myr` | `5.32 Myr` | `2.66 Myr` | `1.06 Myr` |

Für eine grobe Energieänderung um Faktor `100` wären im konstanten e-fold-Proxy etwa `ln(100)=4.6` solcher Zeiten nötig.

Beispiel `M_p=0.03 M_E`:

```text
M_BH=1e10 kg -> ~73.5 Myr for 4.6 e-folds
M_BH=1e11 kg -> ~7.35 Myr
M_BH=2e11 kg -> ~3.68 Myr
M_BH=5e11 kg -> ~1.47 Myr.
```

Das ist erstmals im Formation-Stack eine Damping-Skala, die für einen **bereits planet-bound und body-crossing Seed** mit terrestrischen Wachstumszeiten konkurrieren kann.

Aber:

```text
I=30 is intentionally generous
uniform density is crude
extended-body orbit changes inside R_p
real liquid/solid/WDM response is not closed
```

Daher ist dies **kein finaler Sink-to-center-Beweis**.

Status:

```text
repeated interior-crossing damping can be Myr-scale in optimistic reduced proxy:
PASS feasibility

physical proto-Earth drag / settling closure:
OPEN.
```

## 8. Was F4 gegenüber F3b ändert

F3b scheiterte als generischer Rescue primär an einem **zufälligen Timingproblem**:

```text
short temporary residence
vs
Myr-wide impact epoch.
```

F4 besitzt einen korrelierten Mechanismus:

```text
embryo close encounter itself
-> supplies the energy kick
-> can leave seed permanently embryo-bound.
```

Damit entfällt der mathematische Faktor

```text
t_res/T_GI
```

aus F3b **für diesen speziellen Capture-Kanal**.

Der neue Engpass lautet stattdessen:

```text
How often does the special cold solar-bound seed undergo
an early sufficiently close embryo exchange/scattering encounter
that deposits it inside the stable satellite phase space?
```

## 9. F4 Statusmatrix

| Teiltest | Status | Ergebnis |
|---|---|---|
| collisionless permanent capture around terrestrial planet exists in literature | **PASS existence** | binary-exchange demonstrated numerically |
| stable prograde/retrograde embryo-bound phase space | **PASS** | `~0.49/0.93 r_H` circular reference limits |
| embryo-scattering kick scale | **PASS kinematic** | `O(0.4...1) v_H` accessible in close `q~0.3...1` encounters |
| orientation-only nonzero capture measure | **PASS sanity check** | nonzero for sufficiently strong encounters |
| actual single-seed N-body capture fraction | **OPEN** | requires terrestrial embryo ensemble |
| naked-seed nebular gas drag | **FAIL / insufficient** | F1 unchanged |
| adiabatic growth-assisted engulfment | **PASS conditional** | early captures before few-% M_E naturally cross surface in this limit |
| impulsive-growth counterpart | **negative for same strong shrinkage** | realistic growth granularity matters |
| post-engulfment repeated-crossing DF | **PASS feasibility / OPEN closure** | optimistic e-fold `~0.1...50 Myr` depending mass/host |
| absolute Earth-centre delivery probability | **OPEN** | not yet identified |

## 10. Gesamtinterpretation

F4 ist der erste Formation-Branch seit A19, der nicht auf einen zufälligen kurzen Capture/Impact-Overlap angewiesen ist und gleichzeitig einen plausiblen Weg bis zum Materialkontakt besitzt.

Das Ergebnis ist trotzdem **kein Nachweis und kein Probability-PASS**:

```text
F4 correlated early-capture mechanism:
NOT EXCLUDED / physically viable in reduced gates.

absolute probability:
OPEN.
```

Der Formation-Branch ist daher noch nicht geschlossen, aber der Engpass hat sich erneut verschoben:

```text
from energy impossibility (A19)
to random timing (F3/F3b)
to early correlated N-body capture cross section (F4).
```

## Nächster harter Test – F5

```text
F5 = terrestrial embryo N-body exchange Monte Carlo

primary embryo M1 ~1e-3...1e-1 M_E
perturber q ~0.03...1
seed heliocentric cold a,e,i distribution
mutual encounter impact parameter / velocity distribution
full Sun + two embryos + test seed integration

outputs:
P(permanent stable capture)
post-capture a,e,i distribution
fraction with immediate body-crossing pericentre
fraction later engulfed under sampled growth histories
final centre-delivery proxy.
```

Nur F5 kann aus F4s kinematischem PASS eine belastbare Capture-Fraktion machen.

## Reproduzierbare Datei

- `stage3_76_f4_early_embryo_bound_seed.py`

## Schlussstatus

```text
F4 ENERGY / MULTIBODY EXISTENCE GATE:
PASS.

EARLY STABLE EMBRYO BINDING:
PHYSICALLY ALLOWED.

GROWTH-ASSISTED ENGULFMENT:
PASS IN ADIABATIC LIMIT / REAL HISTORY OPEN.

POST-ENGULFMENT SINKING:
MYR-SCALE FEASIBILITY IN OPTIMISTIC PROXY / FULL CLOSURE OPEN.

ABSOLUTE FORMATION/DELIVERY:
OPEN.

EXPERIMENTAL BH DETECTION:
NONE.
```
