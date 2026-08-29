# Stage 3.72 / A30 – Ionentransport über den Screening-Layer

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** PUBLISHED Fe/Ni DIFFUSION TIMESCALE RECOUPLED / FIXED-ION TF LIMITED TO EARLY RESPONSE / FULL AMBIPOLAR MOBILITY OPEN

## Ziel

A27 zeigte eine ultrakurze Elektronen-/Feldantwort von `O(1e-17 s)`. A28 löste daraufhin statisches nichtlineares TF-Screening mit zunächst fixiertem positiven Ionenhintergrund.

A30 prüft, ob dieser fixe Ionenhintergrund auch über die deutlich längere A26-Mehrfachladungs-Aufbauzeit haltbar wäre.

## Literaturanker Fe/Ni-Transport

Li et al., *Ab initio determination on diffusion coefficient and viscosity of FeNi fluid under Earth's core condition*, Scientific Reports 12, 21255 (2022), DOI `10.1038/s41598-022-24594-8`, berichten entlang der Kernadiabate:

```text
D_Fe ~2.58 ... 3.35e-9 m^2/s
D_Ni ~2.47 ... 3.37e-9 m^2/s.
```

Die Arbeit findet Fe und Ni in derselben Größenordnung und nahezu konstante Selbst-Diffusionskoeffizienten entlang der Kernadiabate.

A30 verwendet konservativ den gemeinsamen Bereich

```text
D_ion ~2.47 ... 3.37e-9 m^2/s.
```

Wichtig: Selbst-Diffusion ist **nicht identisch** mit einer elektrisch getriebenen Mehrkomponenten-Mobilität. Sie dient hier nur als publizierter struktureller Transport-Zeitskalenanker.

## Screening-Längen

A28:

```text
lambda_TF ~2.952e-11 ... 4.292e-11 m.
```

Eine einfache Diffusionszeit über eine Screeninglänge ist

```text
t_ion,lambda ~ lambda_TF^2 / D_ion.
```

Daraus folgt über alle Endpunktkombinationen:

```text
t_ion,lambda ~2.59e-13 ... 7.46e-13 s
             ~0.26 ... 0.75 ps.
```

## Vergleich zur Elektronenantwort

A27:

```text
electronic / electrostatic response ~1e-17 ... few 1e-17 s.
```

Der Ionenstrukturtransport ist damit grob

```text
~1e4 ... 1e5
```

langsamer als die erste elektronische Screeningantwort.

Damit ist die A28-Annahme eines zunächst fixierten Ionenbackgrounds für die **früheste Elektronenrelaxation** sinnvoll.

## Vergleich zu A26s naivem `+5e`-Aufbau

A26:

```text
fully-ionized endpoint: ~5.7e-13 s
low-Zbar endpoint:      ~5.4e-12 s.
```

A30:

```text
ion diffusion over lambda_TF ~2.6e-13 ... 7.5e-13 s.
```

Damit ist die Ionenumordnung

- am fully-ionized schnellen A26-Endpunkt **vergleichbar** mit der naiven `+5e`-Aufbauzeit;
- am low-Zbar langsameren A26-Endpunkt bereits **deutlich schneller** als der naive Mehrfachladungsaufbau.

Daraus folgt:

```text
fixed-ion background throughout multi-e charge buildup:
NOT SELF-CONSISTENT as a general closure.
```

## Vergleich zur äußeren Hydrodynamik

Bei `M=1e11 kg`:

```text
r_B/c_eff ~5.87e-12 s ~5.9 ps.
```

A30 ergibt

```text
t_ion,lambda / (r_B/c_eff) ~0.044 ... 0.127.
```

Ionen können sich über eine atomare/TF-Screeninglänge daher im Reduced-Outer-Core-Vergleich noch **vor** einer ganzen Bondi-Crossing-Zeit strukturell umordnen.

## Hierarchie nach A30

Es entsteht nun eine klarere Mehrskalenstruktur:

```text
~1e-17 s:
electron plasma / Maxwell / TF electronic response

~3e-13 ... 7e-13 s:
Fe/Ni structural diffusion across lambda_TF

~2.6e-12 s:
published warm-dense Fe electron-ion energy relaxation anchor

~5.9e-12 s @1e11 kg:
outer r_B/c_eff hydrodynamic crossing.
```

Die Reihenfolge stützt ein Bild, in dem zuerst Elektronenfelder reagieren, danach bereits die Ionenstruktur im Screening-Layer nachziehen kann, bevor die äußere Hydrodynamik eine ganze `r_B`-Skala durchläuft.

## Konsequenz für `Q_eq`

A27 bleibt bestätigt:

```text
Q cannot be obtained by integrating fixed independent n*v*sigma currents.
```

A30 verschärft dies:

```text
not only electron screening, but also ionic rearrangement becomes relevant
before or during the naive A26 multi-e buildup.
```

Damit braucht eine echte floating/current-balance Closure mindestens

```text
electron conductivity / degeneracy
ion + electron multicomponent mobility
ambipolar electrochemical field
nonlinear screening
species sink kernels
composition / ionization
Q-dependent current balance.
```

## Was A30 nicht behauptet

Aus `D_self` wird **keine exakte Ionendrift-Mobilität** abgeleitet. Insbesondere werden Nernst-Einstein/Einstein-Relationen nicht ungeprüft als exakte WDM-Mischungsclosure verwendet, weil starke Kopplung und Kreuzkorrelationen relevant sein können.

Daher:

```text
exact ion electrical mobility:
OPEN.

exact ambipolar current-balance Q_eq:
OPEN.
```

## Beziehung zu A28/A29

A28/A29 bleiben gültige **elektronische Early-Time / static-screening Sinktests**.

A30 begrenzt ihre Interpretation:

```text
fixed ions:
reasonable for earliest ~1e-17 electron response,
not adequate for the full ~ps current-balance evolution.
```

## Reproduzierbare Datei

- `stage3_72_a30_ion_screening_transport.py`

## Schlussstatus

```text
published Fe/Ni diffusion recoupling:
CALCULATED.

ion response across lambda_TF:
~0.26...0.75 ps.

fixed-ion approximation over full charge buildup:
REJECTED AS GENERAL CLOSURE.

multicomponent ambipolar mobility/current closure:
OPEN.

experimental BH detection:
NONE.
```
