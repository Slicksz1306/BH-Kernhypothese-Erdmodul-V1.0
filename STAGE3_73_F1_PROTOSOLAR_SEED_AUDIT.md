# Stage 3.73 / F1 – Protosolarer co-moving Seed: Formation-/Delivery-Audit

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** DISK-GAS-CAPTURE FAIL / NORMAL-HALO→PROTOSTELLAR-CLOUD STRONGLY NEGATIVE / PRE-BOUND COLD-CO-MOVING SEED OPEN

## Fragestellung

A19 hatte spaeten Einfang eines project-mass BH durch die bereits existierende Erde stark negativ getestet. F1 prueft einen physikalisch anderen Ursprung:

```text
Seed existiert schon vor der Erde
-> Molekuelwolke / protosolare Umgebung
-> protoplanetare Scheibe
-> Planetesimal / Embryo
-> spaetere Erde.
```

Es werden drei unterschiedliche Mechanismen getrennt:

1. dissipativer Einfang durch Gasreibung in der protoplanetaren Scheibe;
2. wiederholte supersonische Scheibendurchgaenge;
3. zeitabhaengige Gravitationsbindung waehrend des Kollapses einer protostellaren Wolke.

Ein bereits gravitativ gebundener, kalter/co-moving Seed ist eine vierte, separate Anfangsbedingung.

## Literaturanker

### Gaseous dynamical friction

Ostriker (1999), *Dynamical Friction in a Gaseous Medium*, ApJ 513, 252–258:

```text
F_df = -4 pi (G M)^2 rho I(Mach) / V^2.
```

Im stark subsonischen Grenzfall gilt

```text
F_df ~= -4 pi (G M)^2 rho V /(3 c_s^3).
```

Damit wird die Geschwindigkeitsdaempfung bei kleinen Machzahlen linear in `V`; sie divergiert nicht fuer `V -> 0`.

### MMSN / protosolare Scheibe

Hayashi-MMSN Referenz bei 1 AU:

```text
Sigma_g ~=1700 g/cm2 =1.70e4 kg/m2
T~=280 K
c_s~=1 km/s.
```

Palaeomagnetische Solar-Nebula-Rekonstruktionen sind mit einer weitgehenden Gaszerstreuung des inneren/aeusseren Nebels bis grob `~4...5 Myr` kompatibel. F1 benutzt bewusst `4.9 Myr` als grosszuegige obere Daempfungszeit.

### Capture during star formation

Oncins et al. (2022) zeigen, dass PBHs in einer ausreichend kalten, dichten Sternentstehungsumgebung waehrend der baryonischen Kontraktion an einen entstehenden Stern gebunden werden koennen, besonders bei hoher DM-Dichte und kleiner Geschwindigkeitsdispersion.

Eroshenko (2023), *Capture of the free-floating planets and primordial black holes into protostellar clouds*, untersucht explizit den Kollaps einer protostellaren Wolke und findet dagegen fuer PBHs aus einem normalen galaktischen Halo mit Geschwindigkeitsdispersion um `~200 km/s` eine **extrem kleine Capture-Wahrscheinlichkeit**.

Diese Resultate sind nicht widerspruechlich: entscheidend ist die Phase-Space-Verteilung des Seed-Populationsanteils.

## F1a – subsonische Gasreibung in der MMSN

Am MMSN-Midplane bei 1 AU ergibt

```text
H = c_s/Omega ~=4.99e9 m
rho_mid ~=1.36e-6 kg/m3.
```

Aus dem Ostriker-Subsonic-Limit folgt die e-folding Daempfungszeit

```text
tau_df = 3 c_s^3 /(4 pi G^2 M rho).
```

| M_BH | tau_df |
|---:|---:|
| `1e10 kg` | `~1.23e17 yr` |
| `1e11 kg` | `~1.23e16 yr` |
| `2e11 kg` | `~6.14e15 yr` |
| `5e11 kg` | `~2.46e15 yr` |

Gegen `4.9 Myr` Disklebensdauer liegen diese Zeiten um ungefaehr `5e8...2.5e10` zu hoch.

```text
subsonic co-moving gas-drag capture:
FAIL.
```

Wichtig: Sehr kleine Relativgeschwindigkeit macht gasfoermige dynamische Reibung hier **nicht** beliebig stark; im subsonischen Grenzfall wird die Kraft proportional zu `V` klein.

## F1b – wiederholte supersonische Scheibendurchgaenge

Fuer einen bewusst grosszuegigen supersonischen Dragfaktor

```text
I=10
```

und einen vertikalen Durchgang durch die MMSN-Saeulendichte folgt ungefaehr

```text
DeltaE/E ~= 8 pi G^2 M Sigma_g I / v^4.
```

Als extrem grosszuegige Obergrenze werden zwei Durchgaenge pro 1-Jahr-Orbit ueber `4.9 Myr` angesetzt:

```text
N_cross ~=9.8e6.
```

Selbst beim guenstigsten getesteten hohen Massenrand `5e11 kg`:

```text
v_rel=3 km/s:  cumulative DeltaE/E ~1.15e-9
v_rel=10 km/s: ~9.3e-12
v_rel=30 km/s: ~1.15e-13.
```

Die niedrigeren BH-Massen verlieren entsprechend noch weniger Energie.

```text
supersonic repeated MMSN-crossing capture:
FAIL by many orders of magnitude.
```

## F1c – zeitabhaengiger protostellarer Wolkenkollaps

Dieser Mechanismus ist anders als Drag: die Gravitationspotentialtiefe aendert sich waehrend der Passage eines Objektes durch die kontrahierende Wolke.

Fuer einen einfachen `1 M_sun`-Potentialbenchmark:

| Wolkenradius | v_escape |
|---:|---:|
| `0.10 pc` | `~0.293 km/s` |
| `0.05 pc` | `~0.415 km/s` |
| `0.01 pc` | `~0.927 km/s` |

Verglichen mit einer normalen Halo-Geschwindigkeitsdispersion

```text
sigma_v ~=200 km/s
```

liegt nur ein extrem kleiner Anteil der unverschobenen Maxwell-Speed-Verteilung unter diesen Geschwindigkeiten:

```text
R=0.10 pc: ~8.4e-10
R=0.05 pc: ~2.4e-9
R=0.01 pc: ~2.6e-8.
```

Diese Zahlen sind nur ein Phase-Space-Illustrator und keine vollstaendige Capture-Wahrscheinlichkeit. Sie zeigen aber denselben Kernpunkt wie Eroshenko (2023): ein normaler Halo ist viel zu schnell fuer effiziente protostellare Capture.

```text
normal Galactic-halo PBH -> contracting protosolar cloud:
STRONGLY NEGATIVE / literature-consistent.
```

## F1d – bereits kalter/co-moving Seed

Die obigen negativen Tests schliessen **nicht** folgende Anfangsbedingung aus:

```text
Seed ist bereits vor dem Kollaps Teil einer niedrigen Relativgeschwindigkeits-Population
oder bereits gravitativ an die lokale Sternentstehungsregion gebunden.
```

Oncins et al. zeigen allgemein, dass bei ausreichend kleiner Geschwindigkeitsdispersion und dichter Sternentstehungsumgebung PBHs waehrend Sternbildung gebunden werden koennen.

Fuer die protosolare Umgebung ist jedoch weder

```text
existence of such a cold PBH subpopulation
noch deren abundance / phase-space density
```

hergeleitet.

Daher:

```text
pre-bound / cold / co-moving protosolar Seed:
OPEN INITIAL CONDITION.
```

Dies ist wesentlich praeziser als `formation impossible`, aber auch wesentlich schwaecher als ein geloester Formationmechanismus.

## Noch fehlender planetarer Schritt

Selbst wenn ein Seed bereits an das junge Sonnensystem gebunden ist, folgt daraus nicht automatisch:

```text
Seed -> terrestrial feeding zone -> Planetesimal -> Proto-Earth -> Erdzentrum.
```

Ein collisionless BH `klebt` nicht an Staub/Gas. Der naechste Formationstest muss deshalb die zeitabhaengige N-body-/Potentialfrage loesen:

```text
Sun + disk + growing planetesimals/embryos + test-particle PBH
```

und pruefen, ob planetarer Massenaufbau, Drei-Koerper-Effekte oder temporaere Co-Orbital-Bindung einen bereits solar gebundenen Seed dauerhaft in einen terrestrischen Embryo ueberfuehren koennen.

## Aktualisierte Formationmatrix

| Mechanismus | Status |
|---|---|
| In-situ-Kollaps normaler Erdmaterie | FAIL |
| spaeter direkter Earth-Capture aus normalem Halo | VERY STRONG FAIL |
| protoplanetare MMSN-Gasreibung, subsonisch | FAIL |
| wiederholte supersonische MMSN-Durchgaenge | FAIL |
| normaler Halo -> kollabierende protosolare Wolke | STRONGLY NEGATIVE |
| bereits solar/protostellar gebundener cold/co-moving Seed | OPEN INITIAL CONDITION |
| solar gebundener Seed -> terrestrischer Embryo | OPEN / NEXT FORMATION BLOCK |

## Schlussstatus

```text
F1 result:
planet formation diversity does open a genuinely distinct formation branch,
but ordinary disk gas drag does not rescue it.

The only surviving branch tested here is not a late-capture mechanism:
it requires a seed already in a cold/low-relative-velocity protosolar phase-space component.

This branch is OPEN, not established.
```

## Reproduzierbare Datei

- `stage3_73_f1_protosolar_seed_audit.py`
