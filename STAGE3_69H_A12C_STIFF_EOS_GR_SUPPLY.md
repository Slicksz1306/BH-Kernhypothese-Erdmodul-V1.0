# Stage 3.69H / A12c – Stiff-EOS GR/Michel Supply Recalibration

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** SUPPLY BENCHMARK REOPENED / RELATIVISTIC STIFF-EOS SENSITIVITY CALCULATED / FULL PIECEWISE Fe-EOS MICHEL SOLVER OPEN

## Motivation

A9-A12 behandelten den historischen Michel-Supply

```text
M=1e11 kg:
Mdot_supply ~1.47e-8 ... 1.46e-7 kg/s
```

als aeusseren Benchmark. Dieser Bereich stammte aus einem frueheren phenomenologischen Dense-Matter-Michel-Solver bei `1e16 kg` plus `Mdot~M^2`-Skalierung.

A12c prueft erstmals explizit, wie empfindlich dieser Supply gegen eine **steife EOS** ist.

## 1. PREM zeigt einen steifen lokalen Erdkernzustand

PREM am Erdzentrum liefert ungefaehr

```text
rho       = 13.08848 g/cm3
Phi       = 108.90 km2/s2
Kappa_S   = 14253 kbar = 1.4253 TPa
Pressure  = 3638.521 kbar = 363.8521 GPa
dK/dP     = 2.3560.
```

Dabei

```text
c_eff^2 = Kappa_S/rho = 108.90 km2/s2
c_eff   = 10.4355 km/s.
```

Fuer einen reinen lokalen Polytropen `P=K rho^Gamma` gilt formal

```text
dK/dP = Gamma.
```

Damit ist `Gamma~2.356` ein sinnvoller **lokaler stiffness proxy**, aber kein globales Fe-EOS bis zum Horizont.

## 2. Warum Newton-Bondi fuer stiff EOS nicht reicht

Baumgarte & Shapiro (MNRAS 502, 3003, 2021) zeigen:

```text
Gamma <=5/3:
    Newtonian Bondi rate is reliable for a_inf<<1.

Gamma >5/3:
    Newtonian Bondi critical solution becomes unphysical;
    a full relativistic Michel/Bondi treatment is required.
```

Der relativistische kritische Sound-Speed `a_s` folgt aus

```text
(1+3 a_s^2) [1-a_s^2/(Gamma-1)]^2
 = [1-a_inf^2/(Gamma-1)]^2.
```

Die Accretion-Eigenzahl ist

```text
lambda_GR =
(a_s/a_inf)^((5-3Gamma)/(Gamma-1))
*[(Gamma-1-a_inf^2)/(Gamma-1-a_s^2)]^(1/(Gamma-1))
*(1+3a_s^2)^(3/2)/4.
```

In SI bleibt die Rate

```text
Mdot = 4 pi lambda_GR G^2 M^2 rho_inf / c_s,inf^3.
```

## 3. Earth-center stiff-polytrope sensitivity

Verwendet:

```text
rho_inf = 13088.48 kg/m3
c_s,inf = 10.435516 km/s
a_inf = c_s/c ~3.481e-5.
```

Bei `M=1e11 kg`:

| Gamma | lambda_GR | a_s^2 | Mdot [kg/s] |
|---:|---:|---:|---:|
| 1.50 | 5.00e-1 | 4.85e-9 | 3.22e-6 |
| 5/3 | 2.50e-1 | 2.32e-5 | 1.61e-6 |
| 1.70 | 8.74e-2 | 2.23e-2 | 5.63e-7 |
| 1.75 | 1.85e-2 | 5.63e-2 | 1.19e-7 |
| 1.80 | 4.48e-3 | 9.07e-2 | 2.89e-8 |
| 1.85 | 1.24e-3 | 1.26e-1 | 8.02e-9 |
| 2.00 | 5.20e-5 | 2.32e-1 | 3.35e-10 |
| 2.20 | 2.33e-6 | 3.79e-1 | 1.50e-11 |
| 2.356 PREM-local proxy | 3.72e-7 | 4.97e-1 | 2.40e-12 |
| 2.50 | 9.41e-8 | 6.07e-1 | 6.07e-13 |

## 4. Relation zum historischen Projekt-Supply

Der historische Bereich

```text
1.47e-8 ... 1.46e-7 kg/s
```

entspricht in diesem **einfachen konstanten-polytropen GR-Surrogat** etwa

```text
Gamma ~1.743 ... 1.826.
```

Damit ist klar:

```text
historical Michel benchmark = an EOS-dependent range,
not a universal outer-supply rate.
```

## 5. Massenscan

Da bei festem asymptotischem Zustand der Michel-Polytropenscan weiterhin `Mdot~M^2` skaliert:

### Gamma=1.80

```text
1e10 kg -> 2.89e-10 kg/s
1e11 kg -> 2.89e-8
2e11 kg -> 1.16e-7
5e11 kg -> 7.22e-7.
```

### Gamma=2.00

```text
1e10 kg -> 3.35e-12 kg/s
1e11 kg -> 3.35e-10
2e11 kg -> 1.34e-9
5e11 kg -> 8.38e-9.
```

### Gamma=2.356 local-PREM proxy

```text
1e10 kg -> 2.40e-14 kg/s
1e11 kg -> 2.40e-12
2e11 kg -> 9.60e-12
5e11 kg -> 6.00e-11.
```

## 6. Wichtige Aussagegrenze

`Gamma=2.356` darf **nicht** als globaler Fe-Polytrop bis zum Horizon interpretiert werden.

Der kritische Punkt dieses konstanten stiff-polytrope Surrogats erreicht relativistische Sound-Speed-Werte. Reales Fe/Ni wird vorher

```text
compression
-> pressure ionization
-> thermal ionization
-> degenerate plasma
-> relativistic electronic/nuclear regimes
```

durchlaufen. `Gamma_eff` ist daher radial und thermodynamisch variabel.

A12c liefert deshalb **kein neues finales Mdot**, sondern eine harte Supply-Sensitivitaet.

## 7. Konsequenz fuer A9-A12

Der innere Processing-Befund bleibt logisch gueltig:

```text
if supply is lower, processing-capable branches remain processing-capable or become even easier.
```

Aber der `1e10 kg` capacity-driven Backpressure-Zweig war an den historischen hohen Supply gekoppelt.

Im A10-fast Modell war

```text
Xi_high(1e10)~1.468.
```

Unter der stiff-polytrope GR supply sensitivity faellt `Xi` stark:

```text
Gamma=1.80 -> Xi~0.29
Gamma=1.85 -> Xi~0.081
Gamma=2.00 -> Xi~0.0034
Gamma=2.356 -> Xi~2.4e-5.
```

Der Uebergang `Xi=1` liegt in diesem einfachen GR-polytrope Vergleich bei etwa

```text
Gamma ~1.756.
```

Damit muss die bisherige Aussage

```text
1e10 kg -> dynamic backpressure
```

praezisiert werden zu

```text
1e10 kg -> backpressure only for sufficiently high/soft-EOS supply;
           stiff-EOS supply can remove the capacity overload entirely.
```

## 8. Neue Statuskorrektur

```text
historical Michel supply: LEGACY / EOS-SENSITIVE BENCHMARK
A9-A12 inner processing capacity: still useful
1e10 capacity-backpressure: CONDITIONAL ON SUPPLY EOS
>=1e11 processing capability: survives; lower stiff-EOS supply strengthens it
final net Mdot: OPEN
```

## 9. Naechster Pflichtschritt

Ein belastbarer Supply braucht einen **piecewise/general-EOS relativistischen Michel-Solver**:

```text
PREM outer state
-> realistic Fe/Ni P(rho,T), E(rho,T)
-> pressure/thermal ionization via bounded Zbar
-> EOS softening/stiffening along compression
-> relativistic critical point
-> Mdot_supply(EOS)
-> then A9-A12 transport/capture closure.
```

Dies wird als A13/Stage-3.69I vorbereitet.
