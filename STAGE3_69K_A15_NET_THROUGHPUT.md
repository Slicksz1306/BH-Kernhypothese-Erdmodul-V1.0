# Stage 3.69K / A15 — Integrierter Reduced Net-Throughput Audit

## Status

**PARTIAL INTEGRATED THROUGHPUT CLOSURE CALCULATED / FINAL SPECIES-RESOLVED FULL-WDM NET MDOT STILL OPEN**

A15 verbindet erstmals den A13b-Outer-Supply-Anker mit der A10-Innenkapazität, der A6/A9-Recycling-Logik, den A5-Fe/Ni-Wave-Capture-Ergebnissen und der A14-Dense-Core-Charge-Closure.

Der Block ist absichtlich konservativ: `Mdot_supply` wird nicht einfach in `Mdot_BH` umbenannt.

## Physischer Stack

```text
Grant-2021/PREM outer supply (A13b)
 -> WDM optical-depth / transport envelope (A10)
 -> repeated encounters / recycling (A6/A9)
 -> Fe/Ni wave capture (A5)
 -> screened stochastic charge feedback (A14)
 -> inner processing capacity (A9/A10)
 -> time-dependent backpressure if overloaded (A11/A12).
```

First-principles Fe-EOS-Arbeiten decken relevante Teilbereiche ab, aber noch nicht den gesamten für dieses Problem benötigten Pfad:

- Sjostrom & Crockett, PRE 97, 053209 (2018): QMD-Fe `7...30 g/cm3`, `1...100 eV`.
- Blanchet et al., PRE 111, 015206 (2025): first-principles Fe-EOS von `7.874 g/cm3`, `5500 K` bis `47.2 g/cm3`, `1e9 K`, inklusive Helmholtz-Freienergie/Entropie via thermodynamischer Integration.

Damit ist eine reale WDM-Verankerung vorhanden, aber keine vollständige tabellierte Fe/Ni/light-element/two-temperature Kinetik über alle im Projekt auftretenden Dichten.

## A13b Supply

Konservativer Grant-Fit-/Temperatur-/Intermediate-EOS-Sensitivitätsbereich bei `1e11 kg`:

```text
Mdot_supply = 8.27e-8 ... 6.13e-6 kg/s.
```

Mit Michel-`M^2`-Skalierung im getesteten stationären Outer-Modell:

| M_BH | Supply min [kg/s] | Supply max [kg/s] |
|---:|---:|---:|
| `1e10` | `8.27e-10` | `6.13e-8` |
| `1e11` | `8.27e-8` | `6.13e-6` |
| `2e11` | `3.31e-7` | `2.45e-5` |
| `5e11` | `2.07e-6` | `1.53e-4` |

## A10 fast-envelope processing capacity

| M_BH | Mdot_capacity [kg/s] |
|---:|---:|
| `1e10` | `9.95e-10` |
| `1e11` | `5.19e-5` |
| `2e11` | `1.36e-3` |
| `5e11` | `1.03e-1` |

Daraus:

| M_BH | Xi_min | Xi_max | Reduced classification |
|---:|---:|---:|---|
| `1e10` | `0.832` | `61.60` | **SUPPLY/EOS + BACKPRESSURE CONDITIONAL** |
| `1e11` | `1.59e-3` | `1.18e-1` | **PROCESSING-CAPABLE in tested stack** |
| `2e11` | `2.42e-4` | `1.80e-2` | **PROCESSING-CAPABLE** |
| `5e11` | `2.00e-5` | `1.48e-3` | **PROCESSING-CAPABLE** |

## Warum Fe/Ni single-pass capture nicht direkt mit Supply multipliziert wird

A5 ergab bei `1e11 kg`:

```text
Fe-56 sigma/sigma_classical ~0.99754
Ni-58 sigma/sigma_classical ~0.99646.
```

A14 liefert für geladene Protonen im bevorzugten screened few-e charge bracket grob

```text
~0.87 ... 0.93 classical.
```

Diese Zahlen sind **single-particle/single-encounter capture diagnostics**. A6/A9 zeigte für repeated encounters exakt

```text
chi_capture = p/(p+e_perm).
```

Wenn Misses im optisch dicken Reservoir verbleiben und `e_perm << p`, nähert sich die eventual-capture-Fraktion 1. Deshalb wäre es falsch, z.B. `Mdot_supply * 0.99754` als die stationäre Fe-Nettoakkretion zu deklarieren.

A10 fand bereits in der direkt first-principles/QMD-gedeckten Außenschale große optische Tiefen; `local Kn~1` ist daher nicht gleich permanenter Escape.

## Was A15 belastbar sagt

### `M>=1e11 kg`

Über **alle** getesteten A13b-Grant-Fit-Anker-Branches gilt

```text
Xi < 1.
```

Damit ist die bisher modellierte innere Processing-Kapazität nicht der Engpass. Innerhalb der reduzierten A6/A9/A10/A14-Closures kann der Supply verarbeitet werden.

Das bedeutet **nicht**, dass die endgültige reale Rate bereits bestimmt ist. Der dominante offene Unsicherheitsblock ist nun die reale Outer-/Intermediate-EOS-, Mischung-, Reaktions- und two-temperature Closure.

### `M=1e10 kg`

Der A13b-Supply schneidet die Kapazitätsgrenze:

```text
Xi ~0.83 ... 61.6.
```

Der einfache diagnostische Ceiling

```text
min(Mdot_supply, Mdot_capacity)
```

liegt damit ungefähr bei

```text
8.27e-10 ... 9.95e-10 kg/s,
```

aber dieser Wert ist **keine nachgewiesene stationäre Mdot**. A11/A12 zeigte bei Kapazitätsüberlastung einen nach außen laufenden Backpressure-Shock und etablierte gerade keine stationäre endliche Innenrate. Für `1e10 kg` bleibt deshalb die zeitabhängige Lösung entscheidend.

## Was für eine finale Full-WDM/species-resolved Mdot noch fehlt

Eine echte Endclosure muss mindestens gleichzeitig liefern:

```text
P(rho,T,composition)
e(rho,T,composition)
Zbar(rho,T)
T_e(r,t), T_i(r,t)
electron-ion relaxation
ion/electron diffusion + viscosity + conductivity
Fe/Ni/light-element mixture fractions
weak/nuclear reaction network where residence times allow it
stochastic Q(t) charge-state kinetics
species-resolved capture sinks
Mdot_BH(t) after hydrodynamic feedback.
```

Keine dieser Größen darf durch eine freie globale `chi_transport` ersetzt werden.

## A15 conclusion

```text
M>=1e11 kg:
  reduced integrated stack remains processing-capable;
  outer/intermediate physical supply closure is now the larger uncertainty.

M=1e10 kg:
  capacity crossing remains real in tested envelope;
  time-dependent backpressure prevents a claimed steady net Mdot.

final full-WDM species-resolved Mdot_BH:
  OPEN.
```

## Reproducibility

- `stage3_69k_a15_net_throughput.py`

This code reports supply, capacity, Xi and the diagnostic `min(supply,capacity)` ceiling without presenting it as a demonstrated stationary BH accretion rate.
