# Stage 3.69I / A13b — Grant-2021 experimentell gefitteter Liquid-Fe-Outer-EOS-Anker

## Status

**PARTIAL EMPIRICAL-FIT OUTER CLOSURE CALCULATED / RAW ZENODO + SESAME TABLE INGESTION STILL OPEN**

Dieser Block ersetzt **nicht** die noch offene direkte Einlesung der Zenodo-Rohdaten oder der SESAME-92141-Tabelle. Er nutzt stattdessen die in Grant et al. (2021) publizierte analytische Liquid-Fe-EOS-Fitform als experimentell verankerten Outer-EOS-Abschnitt.

Primärquelle:

- S. C. Grant et al. (2021), *Equation of State Measurements on Iron Near the Melting Curve at Planetary Core Conditions by Shock and Ramp Compressions*, JGR Solid Earth 126, e2020JB020008.
- DOI: `10.1029/2020JB020008`
- Daten-DOI laut Publikation: `10.5281/zenodo.4464112`

Die Publikation berichtet eine elevated-temperature Liquid-Fe-Isentrope ungefähr über `275...400 GPa` und sehr gute Übereinstimmung mit SESAME 92141. Im aktuellen Zugriff konnte der Zenodo-Rohdatensatz nicht zuverlässig maschinenlesbar abgerufen werden. **Es wurden keine Punkte aus Figuren erfunden oder digitalisiert.**

## Publizierte analytische EOS

Grant et al. refitten die Ichikawa-Form. Isothermaler Vinet-Rydberg-Anteil:

```text
P_iso(rho) = 3 K0 (rho/rho0)^(2/3)
             [1-(rho0/rho)^(1/3)]
             exp{(3/2)(K0'-1)[1-(rho0/rho)^(1/3)]}.
```

Thermische Energie:

```text
E_th(rho,T) = 3 n R [ T + e0 (rho0/rho)^g T^2 ].
```

Thermischer Druck:

```text
P_th(rho,T) = gamma(rho) rho_mol [E_th(rho,T)-E_th(rho,T0)].
```

Grüneisen-Form:

```text
gamma(rho) = gamma0 [1 + a((rho0/rho)^b - 1)].
```

Publizierte Fitparameter, Referenz `7000 K`, `0 GPa`:

```text
K0      = 25.3 +/- 4.0 GPa
K0'     = 6.60 +/- 0.33
rho0    = 5.187 g/cm3
gamma0  = 2.42 +/- 0.12
a       = 1
b       = 0.35
e0      = 0.314e-4 1/K
g       = -0.4.
```

## PREM-Ankopplung

A13 verwendet als äußeren Rand:

```text
rho_inf = 13.08848 g/cm3
P_inf   = 363.8521 GPa
K_S     = 1.4253 TPa
T_ref   = 6000 K.
```

Der Grant-Fit wird druckseitig additiv an `P_inf` geankert. Die Ableitung `dP/drho` bleibt dadurch unverändert. Entlang einer Adiabate wird

```text
d ln T / d ln rho = gamma(rho)
```

verwendet.

Für den Nominalfit ergibt sich am PREM-Rand:

```text
B_Grant(rho_inf) ~1.4192 TPa
B_Grant / K_PREM ~0.9957.
```

Damit reproduziert der unabhängig gefittete Liquid-Fe-Pfad den PREM-Zentrums-Bulkmodul am gewählten Rand auf etwa `0.4 %` — ein nützlicher Konsistenzcheck, aber kein unabhängiger Nachweis des BH-Modells.

Der Grant-Abschnitt wird **nur bis 400 GPa** verwendet. Nominal:

```text
P = 400 GPa -> rho_t ~13.4129 g/cm3
B_t ~1.5348 TPa.
```

Oberhalb dieses experimentell gestützten Bereichs bleibt eine transparente Zwischen-Dichte-Sensitivität nötig:

```text
beta_mid = 1.4 ... 1.8
rho_rel  = 1e5 ... 1e7 g/cm3
beta_inner = 4/3.
```

Diese Intermediate-/Inner-Segmente sind weiterhin Modellbrackets und **keine** direkte Grant-/SESAME-Messung.

## General-EOS-Michel-Ergebnis

Nominaler Grant-Fit mit dem bestehenden `beta_mid/rho_rel`-Sensitivitätsraster:

```text
M_BH = 1e11 kg:
Mdot_supply ~1.29e-7 ... 3.80e-6 kg/s.
```

Konservativer Corner-Scan mit

```text
K0      = 25.3 +/-4.0 GPa
K0'     = 6.60 +/-0.33
gamma0  = 2.42 +/-0.12
T_anchor= 5500, 6000, 6500 K
beta_mid= 1.4, 1.8
rho_rel = 1e5, 1e7 g/cm3
```

ergibt:

```text
M_BH = 1e11 kg:
Mdot_supply,Grant-fit-anchor ~8.27e-8 ... 6.13e-6 kg/s.
```

**Das ist kein statistisches Konfidenzintervall.** Es ist eine kombinierte publizierte Fitparameter-/Temperatur-/Intermediate-EOS-Sensitivität.

## Recoupling an A10-Fast-Processing-Capacity

Mit dem konservativen Corner-Band:

| M_BH | Mdot_min [kg/s] | Mdot_max [kg/s] | Xi_min | Xi_max |
|---:|---:|---:|---:|---:|
| `1e10` | `8.27e-10` | `6.13e-8` | `0.832` | `61.60` |
| `1e11` | `8.27e-8` | `6.13e-6` | `1.59e-3` | `1.18e-1` |
| `2e11` | `3.31e-7` | `2.45e-5` | `2.42e-4` | `1.80e-2` |
| `5e11` | `2.07e-6` | `1.53e-4` | `2.00e-5` | `1.48e-3` |

Daraus folgt innerhalb dieses A13b-Fit-Anker-Stacks:

```text
M>=1e11 kg:
Xi_max < 1 -> inner processing-capable conclusion survives.

M=1e10 kg:
Xi crosses / exceeds 1 strongly -> supply/EOS conditional remains.
```

Der Robustheitsabstand für `1e11 kg` ist kleiner als im ursprünglichen A13-Surrogat (`Xi_max~0.026` dort, hier bis ~0.118), bleibt aber im getesteten Fit-Anker-Raster unter 1.

## Interpretation

A13b zeigt zwei Dinge:

1. Der experimentell gefittete Grant-Liquid-Fe-Outer-Pfad ist am PREM-Rand überraschend konsistent mit `K_S`.
2. Wenn das Intermediate-EOS bereits oberhalb des experimentell gestützten `400 GPa`-Bereichs weich werden darf, kann der Michel-Supply höher liegen als im ursprünglichen A13-Surrogat.

Damit ist der A13-Satz

```text
constant PREM stiffness to horizon -> stress limit only
```

weiter gestützt.

Nicht zulässig ist dagegen:

```text
Grant-fit-anchor band = final physical Earth-BH accretion rate.
```

Es fehlen weiterhin direkte Rohdaten-/SESAME-Einlesung, reale Intermediate-/Deep-WDM-EOS, Zusammensetzung und finale species-resolved Nettoakkretion.

## Reproduzierbarkeit

Solver:

- `stage3_69i_a13b_grant_fit_anchor.py`

Der Solver implementiert den publizierten Grant-Fit bis 400 GPa, die PREM-Ankopplung, thermodynamische Enthalpieintegration, die exakte A13-Michel-Kritikalität und den Capacity-Recoupling-Scan.

## A13b Restpunkt

```text
raw Zenodo pressure-density traces / direct SESAME 92141 isentrope
-> machine-readable ingestion
-> direct interpolation + thermodynamic reconstruction
-> Michel solve without intermediate fitted surrogate where data exist.
```

Bis dahin:

**A13b = PARTIAL, nicht FINAL.**
