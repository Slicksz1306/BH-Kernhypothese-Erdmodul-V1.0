# Stage 3.79 / F7 – Seed-Origin / Solar-Bound Phase-Space Gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** STANDARD GALACTIC-HALO ORIGIN FAIL FOR TERRESTRIAL PHASE SPACE / PROTOSTELLAR WIDE CAPTURE EXISTS BUT INNER-1-AU SUPPLY FAIL / GIANT-PLANET CAPTURE LOCAL DENSITY FAIL / NONSTANDARD CO-MOVING COLD DARK OVERDENSITY OPEN

## Ziel

F6 hat den lokalen Formation-Engpass erstmals als Populationsanforderung formuliert. Für den Referenzbranch

```text
M1 = 0.03 M_E
K_F5 = 5/300
N_enc = 10
S_post = 0.5
P_delivery = 0.5
```

wird benötigt:

```text
mu_H,50 = 8.318 eligible Seeds pro Proto-Earth-Hill-Volumen.
```

Die zentrale F7-Frage ist deshalb nicht mehr nur

```text
Kann irgendein PBH solar gebunden werden?
```

sondern

```text
Kann ein Standard-Ursprung genügend LOW-VELOCITY PHASE-SPACE DENSITY
im terrestrischen ~1-AU-Bereich erzeugen, um F6 zu speisen?
```

Das ist wesentlich strenger als eine reine Gesamtzahl solar gebundener PBHs auf weiten Orbits.

## Literaturanker

### Eroshenko 2023 – kollabierende protostellare Wolke

Y. N. Eroshenko, *New Astronomy* 103, 102057 (2023), DOI `10.1016/j.newast.2023.102057`, untersucht freie Objekte und PBHs in einer kollabierenden protostellaren Wolke.

Verwendete Referenzgrößen:

```text
R_i ~7500 AU
t_d ~6e4 yr
sigma_halo ~200 km/s
v_cap ~0.5 km/s.
```

Die Arbeit findet für Galactic-halo-PBHs wegen der hohen Geschwindigkeitsdispersion eine extrem kleine Capture-Wahrscheinlichkeit pro Halo-Objekt. Wichtig für unser sehr kleines PBH-Massenfenster ist aber: Die NUMBER density skaliert wie `1/M_PBH`, daher kann die Gesamtzahl weit gebundener low-mass PBHs trotzdem groß sein.

F7 darf deshalb **nicht** einfach aus "kleine Einzelwahrscheinlichkeit" auf "keine PBHs" schließen. Entscheidend ist die spätere terrestrische Phasenraumdichte.

### Oncins et al. 2022 – adiabatisch gebundene DM bei Sternbildung

M. Oncins et al., *MNRAS* 517, 28–37 (2022), DOI `10.1093/mnras/stac2647`, formulieren für die bei Sternbildung gebundene collisionless-DM-Komponente im low-velocity phase-space limit

```text
rho_bd(r)
= 4 f_s/(3 sqrt(pi))
  * rho_h/sigma_h^3
  * (G M_*/r)^(3/2).
```

Damit wird direkt sichtbar:

```text
relevante Ressource = rho_h / sigma_h^3,
```

nicht nur `rho_h`.

### Dehnen, Hands & Schoenrich 2022 – planetare Capture und Liouville-Mischung

W. Dehnen, T. O. Hands & R. Schoenrich, *MNRAS* 512, 4078–4085 (2022), DOI `10.1093/mnras/stab3666`, zeigen für Solar-System-Capture:

```text
99% der Captures kommen aus v_inf <~3.7 km/s,
```

und Jupiter-/Saturn-crossing bound phase space wird über Capture + Ejection mit der ungebundenen lokalen phase-space density gemischt.

Die Arbeit findet außerdem, dass Captives in sehr weiten Orbits meist rasch wieder ausgestoßen werden und dass selbst im inneren Solar System kein dauerhafter collisionless orbital trap für die captured population existiert.

Diese Resultate sind auf PBHs als masselose Testobjekte anwendbar, solange `M_PBH << M_planet`, was für `1e10...5e11 kg` extrem gut erfüllt ist.

## 1. F6-Referenzbedarf

F6:

```text
M_embryo = 0.03 M_E
r_H      = 4.650e8 m
V_H      = 4.212e26 m^3
mu_H,50  = 8.318.
```

Daraus folgt die benötigte lokale Seed-Massendichte:

| M_PBH | rho_seed,required @1 AU |
|---:|---:|
| `1e10 kg` | `1.975e-16 kg/m^3` |
| `1e11 kg` | `1.975e-15 kg/m^3` |
| `2e11 kg` | `3.950e-15 kg/m^3` |
| `5e11 kg` | `9.874e-15 kg/m^3` |

## 2. Adiabatic-contraction Gate

Wir setzen absichtlich capture-freundlich

```text
f_PBH = 1
f_s   = 1
rho_h = 0.3 GeV/cm^3
      = 5.348e-22 kg/m^3
sigma_h = 200 km/s.
```

Aus der Oncins-Formel folgt bei `r=1 AU`:

```text
rho_bd(1 AU) = 1.329e-24 kg/m^3.
```

Das ist die gesamte gebundene DM-Massendichte; die Zahl der PBHs hängt dann nur über `1/M_PBH` ab.

### Hill occupancy

| M_PBH | mu_H from canonical adiabatic bound DM | shortfall vs 8.318 |
|---:|---:|---:|
| `1e10 kg` | `5.60e-8` | `1.49e8 x` |
| `1e11 kg` | `5.60e-9` | `1.49e9 x` |
| `2e11 kg` | `2.80e-9` | `2.97e9 x` |
| `5e11 kg` | `1.12e-9` | `7.43e9 x` |

Damit:

```text
canonical Galactic-halo adiabatic inheritance at 1 AU:
FAIL by ~8...10 orders in the F6 occupancy gate.
```

Selbst eine capture-freundlichere Halo-Dispersion von `135 km/s` würde nur um den Faktor `(200/135)^3 ~3.25` helfen und ändert das Urteil nicht.

## 3. Welche Phase-Space-Umgebung wäre nötig?

Weil

```text
rho_bd ∝ rho_h/sigma_h^3,
```

können wir die notwendige primordial co-moving dark environment direkt invertieren.

### Falls rho_h nur kanonisch 0.3 GeV/cm^3 wäre

Dann müsste die DM-Dispersion betragen:

| M_PBH | required sigma_DM |
|---:|---:|
| `1e10 kg` | `378 m/s` |
| `1e11 kg` | `175 m/s` |
| `2e11 kg` | `139 m/s` |
| `5e11 kg` | `102 m/s` |

Das ist keine normale Galactic-halo Population.

### Falls stattdessen sigma_DM = 1 km/s wäre

Dann müsste die lokale **dark** density betragen:

| M_PBH | rho_DM required |
|---:|---:|
| `1e10 kg` | `0.147 M_sun/pc^3` |
| `1e11 kg` | `1.47 M_sun/pc^3` |
| `2e11 kg` | `2.94 M_sun/pc^3` |
| `5e11 kg` | `7.34 M_sun/pc^3` |

Das ist nicht mathematisch unmöglich, würde aber eine bereits **co-moving, cold, dark overdensity / mini-halo / stream** am Solar-Birth-Ort verlangen.

Wichtig:

```text
die ~1...3 km/s interne Stern-Geschwindigkeitsdispersion eines Solar-Birth-Clusters
kühlt normale 100...200 km/s Halo-PBHs NICHT automatisch auf diese Dispersion herunter.
```

Ein ordinary stellar cluster ist deshalb nicht selbst die fehlende Dark-Matter-Phase-Space-Komponente.

Status:

```text
standard halo -> cold solar-bound F6 population: FAIL
pre-existing co-moving cold dark substructure: OPEN exotic initial condition.
```

## 4. Protostellar-cloud Collapse – extreme Upper Bound

Eroshenko verwendet ungefähr

```text
R_i = 7500 AU
t_d = 6e4 yr
v_cap ~0.5 km/s
sigma_halo ~200 km/s.
```

F7 baut nun eine absichtlich extrem capture-freundliche Obergrenze:

1. **Jeder** Halo-PBH mit `v < v_cap`, der die geometrische Cloud-Cross-Section trifft, wird als solar gebunden gezählt.
2. Für den terrestrischen Untertest wird sogar eine fertig konzentrierte Punkt-Sonne zur gravitational focusing Cross-Section benutzt; das ist stärker als das reale frühe distributed-cloud Potential.
3. **Jeder** so fokussierte `q<1 AU`-Trajektorienfall wird als perfekt nutzbarer innerer Seed gezählt.

Maxwellian mit `sigma=200 km/s`:

### alle langsamen Cloud-Entrants – Upper Bound

| M_PBH | N(v<0.5 km/s, crosses cloud) |
|---:|---:|
| `1e10 kg` | `6.24e5` |
| `1e11 kg` | `6.24e4` |
| `2e11 kg` | `3.12e4` |
| `5e11 kg` | `1.25e4` |

Das zeigt eine wichtige Nuance:

```text
TOTAL wide solar-bound PBH count is not necessarily tiny for such low masses.
```

Aber nach der zusätzlichen, bereits überoptimistischen `q<1 AU`-Fokussierung bleibt maximal:

| M_PBH | perfect inner-1-AU candidate upper bound |
|---:|---:|
| `1e10 kg` | `157` |
| `1e11 kg` | `15.7` |
| `2e11 kg` | `7.87` |
| `5e11 kg` | `3.15` |

F6s **globales Minimum** selbst für die günstigste dort getestete co-orbitale Geometrie war bereits

```text
N_seed,min ~1.07e4.
```

Damit fehlt selbst dieser unrealistisch starke Cloud-Upper-Bound um mindestens

```text
~68 x   at 1e10 kg
~679 x  at 1e11 kg
~1.36e3 at 2e11 kg
~3.40e3 at 5e11 kg.
```

Und diese Obergrenze setzt noch nicht einmal voraus, dass die inneren Passagen tatsächlich auf kalten, langlebigen ~1-AU-Orbits enden.

Status:

```text
protostellar cloud can populate WIDE bound PBH orbits: YES in principle
protostellar cloud as supplier of F6 terrestrial cold phase space: FAIL in generous upper bound.
```

## 5. Planetary Capture after Solar-System Formation

Ein naiver total-capture count kann für sehr kleine PBH-Massen groß werden, weil die gravitational capture cross-section mass-independent ist, während `n_PBH ∝1/M_PBH`.

Das reicht aber nicht. Der relevante F6-Wert ist die **instantaneous bound density near 1 AU**.

Mit dem Dehnen/Hands/Schoenrich phase-space-mixed Jupiter/Saturn model und einem Maxwellian `sigma=200 km/s` ergibt deren equation (27) bei `r=1 AU`:

```text
n_bound(1 AU) / n_halo ~4.50e-4.
```

Das liefert für den F6 Proto-Earth-Hill-Raum:

| M_PBH | mu_H from giant-planet captive population | shortfall vs F6 |
|---:|---:|---:|
| `1e10 kg` | `1.01e-8` | `8.20e8 x` |
| `1e11 kg` | `1.01e-9` | `8.20e9 x` |
| `2e11 kg` | `5.07e-10` | `1.64e10 x` |
| `5e11 kg` | `2.03e-10` | `4.10e10 x` |

Das erklärt, warum ein großer **integrated capture count** über Gyr nicht automatisch eine große lokale kalte Population erzeugt:

```text
capture <-> ejection phase-space exchange
+ high-e planet-crossing orbits
+ tiny low-v halo phase-space density.
```

Dehnen et al. zeigen außerdem, dass die captive und unbound Phase-Space-Komponenten in den porösen Jupiter/Saturn-crossing Regionen langfristig gemischt werden und dass keine effizienten collisionless long-term traps bei `a<~2000 AU` entstehen.

Status:

```text
standard-halo giant-planet capture as F6 terrestrial population source:
FAIL in local phase-space density.
```

## 6. Solar Birth Cluster / Multi-Star Exchange

Die Sonne entstand sehr wahrscheinlich in einem jungen Sternaggregat. Typische Solar-birth-cluster Modelle besitzen interne **stellar** velocity dispersions von Größenordnung `~1.4...2.9 km/s`.

Das hilft nur dann für PBHs, wenn eine PBH-Komponente **bereits** dieselbe co-moving low-velocity distribution besitzt.

Normale Halo-PBHs haben dagegen eine viel höhere Galactic dispersion / bulk relative speed. Reine Newtonsche Mehrkörperstreuung kann einzelne Objekte binden, aber sie erzeugt keine dissipative Kühlung einer ganzen hot-halo population auf `~0.1...1 km/s`.

Der F6-Bedarf ist deshalb am besten als required phase-space merit factor geschrieben:

```text
(rho_DM/sigma_DM^3)_required
/
(rho_halo/sigma_halo^3)
~1.5e8 ... 7.4e9
```

für `1e10...5e11 kg`.

Ein ordinary natal cluster ohne eigene kompakte Dark-Matter-Komponente schließt diese Lücke nicht.

## 7. F7 Statusmatrix

| Ursprungskanal | Status | Ergebnis |
|---|---|---|
| canonical halo -> adiabatic solar inheritance @1 AU | **FAIL** | F6 shortfall `~1e8...1e10` |
| protostellar collapse -> any wide bound PBHs | **PASS existence** | total low-mass count can be large |
| protostellar collapse -> terrestrial `q<1 AU` population | **FAIL upper bound** | max `~3...157` vs F6 minimum `~1.07e4` |
| ordinary halo gas/dynamical drag | **FAIL** | previous F1 + Eroshenko consistent |
| standard Sun+giant-planet halo capture @1 AU | **FAIL phase-space density** | shortfall `~8e8...4e10` |
| ordinary stellar birth cluster alone | **FAIL as PBH cooler** | stellar sigma != halo-PBH sigma |
| pre-existing co-moving cold PBH mini-halo/stream | **OPEN** | required `rho/sigma^3` quantified |
| absolute primordial abundance of such substructure | **OPEN** | no standard origin established |
| direct Earth-centre BH evidence | **NONE** | formation dynamics only |

## Konsequenz

F4/F5 bleiben mathematisch wichtig:

```text
IF an eligible solar-bound cold Seed is already in the terrestrial Hill phase space,
correlated embryo exchange can capture it.
```

F7 zeigt aber, dass Standard-Galactic channels diese Anfangsbedingung **nicht liefern**.

Der überlebende Formation-Branch wird jetzt deutlich spezieller:

```text
pre-existing primordial compact-object population
+ already co-moving with the proto-Sun
+ phase-space merit rho/sigma^3 enhanced by ~1e8...1e10 over canonical halo
+ survives solar formation
+ populates terrestrial zone
+ F5 embryo exchange
+ F4 growth engulfment
+ interior damping.
```

Das ist kein formaler mathematischer Ausschluss, aber eine starke Fine-Tuning-/Origin-Verschärfung.

## Nächster harter Test – F8

F8 sollte den **letzten offenen origin-rescue** direkt testen:

```text
primordial co-moving dark mini-halo / cold stream around proto-Sun
-> required mass, size and velocity dispersion from F7
-> tidal survival in Galactic field / natal cluster
-> adiabatic response to Sun formation
-> terrestrial-zone phase-space profile
-> present-day depletion requirement
-> observational consistency.
```

Wenn keine plausible compact dark substructure die F7 phase-space merit factors liefern und zugleich später ausreichend depletiert werden kann, ist der Formation/Delivery-Branch praktisch geschlossen.

## Reproduzierbare Datei

- `stage3_79_f7_seed_origin_phase_space_gate.py`

## Schlussstatus

```text
F7 STANDARD GALACTIC ORIGIN:
FAIL for F6 terrestrial phase-space supply.

F7 WIDE SOLAR CAPTURE OF LOW-MASS PBHs:
possible, but not sufficient.

NONSTANDARD PRIMORDIAL CO-MOVING COLD DARK SUBSTRUCTURE:
OPEN.

ABSOLUTE EARTH DELIVERY:
OPEN / now strongly origin-fine-tuned.

EXPERIMENTAL BH DETECTION:
NONE.
```