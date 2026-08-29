# Stage 3.72 / A24 – Final net-`Mdot_BH` identifiability audit

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** REDUCED SUPPLY/CAPACITY MARGINS CALCULATED / UNIQUE FULL-PHYSICS `Mdot_BH(t)` NOT IDENTIFIABLE YET

## Frage

Nach A20-A23 ist zu pruefen, ob die vorhandenen Rechnungen bereits eine eindeutige finale species-resolved Netto-Akkretionsrate liefern.

Die Antwort ist:

```text
Nein.
```

Das ist kein numerischer Fehlschlag, sondern ein **Identifizierbarkeitsbefund**: mehrere noch offene physikalische Funktionen beeinflussen dieselbe Netto-Rate.

## Aktuell quantifizierbare Supply-/Capacity-Margen

A13b konservativer Grant-fit/T/Intermediate-EOS-Sensitivitaetsbereich bei `1e11 kg`:

```text
Mdot_supply ~8.27e-8 ... 6.13e-6 kg/s.
```

Mit der bereits in A13/A15 verwendeten `M^2`-Skalierung und den A10-fast Processing-Capacities:

| M_BH | Supply min [kg/s] | Supply max [kg/s] | Capacity [kg/s] | Xi_min | Xi_max |
|---:|---:|---:|---:|---:|---:|
| `1e10` | `8.27e-10` | `6.13e-8` | `9.95e-10` | `0.832` | `61.64` |
| `1e11` | `8.27e-8` | `6.13e-6` | `5.19e-5` | `1.59e-3` | `0.118` |
| `2e11` | `3.31e-7` | `2.45e-5` | `1.37e-3` | `2.42e-4` | `1.80e-2` |
| `5e11` | `2.07e-6` | `1.53e-4` | `1.03e-1` | `2.00e-5` | `1.49e-3` |

Damit bleibt der bereits gehaertete Reduced-Befund bestehen:

```text
M>=1e11 kg:
outer tested supply < reduced inner processing capacity.

M=1e10 kg:
supply crosses capacity -> time-dependent backpressure remains decisive.
```

## Warum `min(Supply, Capacity)` keine finale Rate ist

Formal kann man als reine Durchsatzdiagnostik schreiben

```text
Mdot_diag = min(Mdot_supply, Mdot_capacity).
```

A11/A12 zeigen aber bereits, dass ein ueberlastetes System nicht automatisch in einen stationaeren Zustand mit `Mdot=Mdot_capacity` geht; es kann einen nach aussen laufenden Backpressure-Shock erzeugen.

Auch im nicht ueberlasteten Bereich ist `Mdot_supply` erst dann die BH-Netto-Rate, wenn unter anderem permanenter Escape, Elektronen-/Ionenstrom, Charge und Reaktionen konsistent geschlossen sind.

Daher wird `Mdot_diag` **nicht** als `Mdot_BH` ausgegeben.

## Noch offene Funktionen, die dieselbe Netto-Rate beeinflussen

Nach A20-A23 fehlen mindestens:

```text
1. mixture EOS P(rho,Te,Ti,X), e(rho,Te,Ti,X)
2. species-dependent permanent escape e_perm(r,E,species)
3. G(rho,Te,Ti,X), Ce, Ci, Ke/Ki
4. reaction network + composition/Ye evolution
5. full screened-electron capture S-matrix/current
6. stochastic charge kinetics Q(t)
7. time-dependent hydro/backpressure solution
```

Mehrere unterschiedliche Kombinationen dieser Funktionen koennen denselben reduzierten Supply-/Capacity-Wert erzeugen, aber unterschiedliche reale `Mdot_BH(t)` liefern.

Damit ist das inverse Problem aktuell nicht eindeutig.

## A24 Kernaussage

```text
unique full-physics species-resolved Mdot_BH(t):
NOT IDENTIFIABLE FROM CURRENT CLOSED INPUTS.
```

Eine einzelne Zahl jetzt festzulegen waere Scheingenauigkeit und wird als Projektmethode verworfen.

## Was trotzdem robust bleibt

A24 hebt die bisherigen Reduced-Ergebnisse **nicht** auf:

- Proton-/Fe-/Ni-Wavecapture zeigt keinen grossen Wellenstopper im getesteten Bereich.
- A14 findet keinen grossen elektrostatischen Protonenblocker im screened Dense-Core-Bracket.
- A10/A15 zeigen fuer `>=1e11 kg` grosse Processing-Capacity-Reserve im getesteten Stack.
- `1e10 kg` bleibt der EOS-/Supply-/Backpressure-Uebergangsbereich.

Diese Aussagen sind weiterhin Reduced/Partial und keine Messung.

## Abhaengigkeitskette fuer den echten Abschluss

```text
A20 raw/table EOS
 + A22 mixture EOS
 + A21 full screened electron current
 + A23 Te/Ti + reaction closure
        ↓
time-dependent species hydro/transport
        ↓
Q(t), Ye(t), escape/recycling
        ↓
final Mdot_BH(t)
        ↓
heat/age + macro seismic/neutrino observables
        ↓
full Stage 3.70 H0 likelihood
```

## Reproduzierbare Datei

- `stage3_72_a24_net_mdot_identifiability.py`

## Schlussstatus

```text
Reduced supply/capacity margin audit:
COMPLETE / CALCULATED.

>=1e11 reduced processing-capable classification:
RETAINED.

1e10 conditional classification:
RETAINED.

Single final Mdot before upstream Full-WDM closures:
REJECTED AS FALSE PRECISION.

Final species-resolved Mdot_BH(t):
OPEN / NOT YET IDENTIFIABLE.
```
