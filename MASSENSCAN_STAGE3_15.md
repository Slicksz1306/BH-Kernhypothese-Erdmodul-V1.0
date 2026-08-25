# Stage 3.15 – Massenscan: Hawking + Michel gemeinsam

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.3  
**Stand:** 25.08.2026

## Zweck

Stage 3.12 hatte Standard-Hawking und Michel-Akkretion als getrennte Langzeitgrenzen verglichen. Stage 3.15 löst beide Terme erstmals gleichzeitig als reduzierte Massenentwicklung:

```text
dM/dt = k_Michel M^2 - A_H/M^2.
```

Dabei wird die Stage-3.12-Michel-Skalierung `Mdot_Michel proportional M^2` verwendet und der bereits im Projekt benutzte einfache Standard-Hawking-Benchmark `tau(1e11 kg)=2.665e9 yr` beibehalten.

## Zentrale Korrektur

Die frühere starke Aussage

```text
Standard-Hawking + ununterdrückte Michel-Akkretion -> kein gemeinsames Langzeitfenster
```

war zu stark, weil beide Prozesse als getrennte Ausschlussbedingungen statt als gleichzeitig wirkende Terme behandelt wurden.

Im gekoppelten ODE existiert ein Gleichgewicht

```text
M_eq = (A_H/k_Michel)^(1/4),
```

bei dem Michel-Zuwachs und Hawking-Verlust betragsgleich sind.

Für die fünf Stage-3.12-`Y_e`-Sensitivitätszweige ergibt sich

```text
M_eq ~ 1.28e11 ... 2.28e11 kg.
```

Der zugehörige PREM-Ersatzradius beträgt nur ungefähr

```text
r_rep ~ 133 ... 161 m.
```

## Stabilität

Das Gleichgewicht ist kein Attraktor, sondern instabil. Die lineare e-Faltungszeit liegt jedoch bei ungefähr

```text
4.23e9 ... 2.37e10 Jahre.
```

Die nichtlineare Integration über `4.54 Gyr` ergibt für weniger als `1%` Netto-Massenänderung ein Anfangsmassenband von ungefähr

```text
low-Ye:  -0.51% / +0.53% um M_eq
high-Ye: -4.40% / +5.12% um M_eq,
```

mit den übrigen `Y_e`-Zweigen dazwischen.

Das ist ein **Kompensationsband**, kein stabiler Selbstregler.

## Hawking-Leistungs-Sensitivität

Ein Multiplikatorscan `f_H = 0.1, 1, 10, 100` zeigt die erwartete Skalierung

```text
M_eq proportional f_H^(1/4).
```

Die qualitative Existenz eines Balancepunkts bleibt in diesem reduzierten Modell erhalten; Masse und Bandbreite verschieben sich.

Die Multiplikatoren sind Sensitivitätsparameter und keine Behauptung über eine exakte Teilchenspezies-Korrektur.

## Wichtiger Materialphysik-Befund

Die Stage-3.14-Coulomb-Plastizitätsdaten können nicht direkt auf dieses neue Massenband übertragen werden.

Am Michel-Kritikpunkt skaliert die dimensionslose Deformationsrate ungefähr wie `1/M`. Die 2026-MD-Kalibrierung bis `2e-5 omega_p` ist je nach Proxy erst oberhalb ungefähr

```text
u^r/r-Proxy:      5.4e14 ... 6.0e15 kg
Kontinuitätsproxy: 1.1e15 ... 1.2e16 kg
```

direkt anwendbar.

Das neue Hawking/Michel-Gleichgewichtsband liegt rund `4e3 ... 5e4` unter diesen Massengrenzen. Am Gleichgewicht erhält man dimensionslose kritische Raten von ungefähr

```text
0.085 ... 0.52 omega_p  (u^r/r)
0.17  ... 1.05 omega_p  (Kontinuitätsproxy),
```

also weit außerhalb der Stage-3.14-MD-Kalibrierung.

Damit kann Stage 3.14 dieses niedrige Massenband derzeit weder bestätigen noch ausschließen.

## Earth-Matching

Das neue Kandidatenband besitzt nur einen strukturellen PREM-Ersatzradius von etwa `100–200 m`. Die bisher voll gekoppelten und cross-solver-validierten Earth-Matching-Läufe wurden nicht in diesem niedrigen `M_SL`-/sub-km-Bereich validiert.

Daher ist die geophysikalische Verträglichkeit dieses Massenbands ebenfalls noch offen.

## Aktueller Status

- `M_SL=1e16 kg` bleibt durch die relativistische Akkretionsrechnung stark belastet.
- Die gesamte Erd-SL-Hypothese ist dadurch nicht ausgeschieden.
- Im reduzierten simultanen Hawking+Michel-Modell erscheint ein neues Kandidatenband bei ungefähr `1e11 kg`.
- Dieses Band ist instabil, kann aber im einfachen ODE über ein Erdalter nur geringe Nettoänderung zeigen.
- Materialtransport und voll gekoppeltes Earth Matching sind für dieses Band noch nicht validiert.

Es liegt weiterhin **kein empirischer Nachweis eines Schwarzen Lochs im Erdzentrum** vor.
