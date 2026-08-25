# Akkretions- und Langzeitstatus – Stage 2 bis 3.15

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.3  
**Stand:** 25.08.2026

## 1. Grundprinzip

Die Bondi- und Michel-Gleichungen werden in diesem Projekt als physikalische Modelle innerhalb klar benannter Annahmen verwendet. Numerische Reproduktion einer Formel ist kein Nachweis eines Erd-SL.

## 2. Referenzzweig 1e16 kg

Für `M_SL=1e16 kg` wurden folgende Größen als Benchmarks gehärtet:

```text
r_s ~ 1.49e-11 m
r_B ~ 5.26e-3 m
Mdot_Bondi ~ 1.28e4 kg/s
```

Ein einfacher Standard-Hawking-Benchmark liefert eine Erdalter-Survival-Skala um `1.19e11 kg`.

## 3. Stage 3.2–3.6 – Mikroakkretion, Creep und Wärme

Ballistische Capture-Proxies, Festkörperdiffusion, Creep, Knudsen-/Kontinuumsübergänge und Wärmeleitung zeigen, dass ein fester Erdkern nicht automatisch wie ein ideales Bondi-Gas behandelt werden darf.

Die frühe Aussage, lokale Wärme müsse zwangsläufig bis zur Bondiskala schmelzen und damit Bondi starten, wurde durch ein Zwei-Phasen-/Thermalisierungsmodell abgeschwächt. Ein Schmelzübergang benötigt gleichzeitig ausreichende lokale Energiedeposition und eine ausreichend große Schmelzzone.

## 4. Stage 3.7–3.11 – Bondi-Audit und Hochdruck-EOS

Die klassische Bondi-Algebra wurde reproduziert; kein mathematischer Fehler in der Formel gefunden.

PREM-nahe Stiffness und Hochdruck-Fe-EOS zeigen jedoch, dass eine konstante Gas-EOS nicht bis in die SL-Nahzone extrapoliert werden darf. Die frühere `~54 r_s`-Grenze eines konstanten `Gamma~4`-Toymodells ist daher als physische Langzeitgrenze zurückgezogen.

## 5. Stage 3.12 – relativistische Michel-Akkretion

Ein allgemeiner barotroper Schwarzschild-Michel-Solver wurde gegen einen analytischen `Gamma=2`-Fall geprüft; die relative `Mdot`-Abweichung lag bei etwa `2e-14`.

Für eine phenomenologische condensed-to-degenerate-EOS und fünf `Y_e`-Sensitivitätszweige ergibt sich bei `M_SL=1e16 kg`:

```text
Mdot_Michel ~ 147 ... 1460 kg/s.
```

Ohne Gegenprozess wäre `+1%` Masse bereits nach ungefähr `2.1e3 ... 2.1e4 Jahren` erreicht. Für reine Akkretionsstabilität wären daher Unterdrückungen um `2e5 ... 2e6` gegenüber dieser Michel-Kapazität nötig.

## 6. Stage 3.13 – Solid/Michel-Kopplung

Eine reduzierte hcp-Fe-Solid/Michel-Kopplung bei Millimeterradien ergibt nahezu die volle Michel-Kapazität. Gewöhnlicher hcp-Fe-Creep liefert dort keine ausreichende `1e5 ... 1e6`-Unterdrückung.

Die alte mikroskopische Sensitivität mit einem `8 GPa`-Stresscap wurde nicht als physische Lösung akzeptiert, weil die tiefe Materie dort kein gewöhnliches hcp-Fe mehr ist.

## 7. Stage 3.14 – Coulomb-Plastizität

In der degenerierten Tiefe wurden Coulombkristall-Skalierungen, Bruchkinetik und aktuelle Perfect-Plasticity-Sensitivitäten verwendet.

Für den `1e16 kg`-Referenzzweig liegen die Michel-Kritikpunkte im oder nahe am untersuchten dimensionslosen Materialratenbereich. Die Michel-Druckabweichung übersteigt die verwendete Coulomb-Yield-Skala deutlich; ein rein elastischer Coulombkristall ist daher keine selbstverständliche permanente Akkretionsbarriere.

Die Stage-3.13-`8 GPa`-Mikrorettung bleibt als Coulomb-Langzeitgrenze zurückgezogen.

## 8. Stage 3.15 – simultane Hawking/Michel-Entwicklung

Die frühere Stage-3.12-Aussage

```text
Standard-Hawking + ununterdrücktes Michel -> kein Langzeit-Overlap
```

war als getrennte Schnittmengenbetrachtung zu stark.

Stage 3.15 löst stattdessen beide Prozesse gemeinsam:

```text
dM/dt = k_Michel M^2 - A_H/M^2.
```

Damit besitzt jeder feste `Y_e`-Michel-Zweig ein Gleichgewicht

```text
M_eq = (A_H/k_Michel)^(1/4),
```

bei dem Akkretion und Verdampfung betragsgleich sind.

Für den fünfgliedrigen `Y_e`-Sweep ergibt der einfache Standard-Hawking-Benchmark:

```text
M_eq ~ 1.28e11 ... 2.28e11 kg.
```

### Stabilität

Das Gleichgewicht ist instabil, aber die e-Faltungszeit ist lang:

```text
~4.23e9 ... 2.37e10 Jahre.
```

Die exakte reduzierte ODE-Integration über `4.54 Gyr` ergibt ein Anfangsmassenband mit weniger als `1%` Nettoänderung von ungefähr

```text
-0.51/+0.53% bis -4.40/+5.12% um M_eq.
```

Das ist ein **Kompensationsband**, kein Attraktor.

### Wichtige physikalische Grenze

Für dieses niedrige Massenband ist die Stage-3.14-Coulomb-Plastizitätskalibrierung nicht direkt anwendbar. Die dimensionslose Michel-Deformationsrate skaliert ungefähr wie `1/M`.

Die 2026-MD-Ratengrenze `2e-5 omega_p` wird je nach Proxy erst oberhalb von ungefähr

```text
5.4e14 ... 1.2e16 kg
```

erreicht. Das neue Gleichgewichtsband liegt etwa `4e3 ... 5e4` darunter.

Am Gleichgewicht ergeben sich als reine Skalierung ungefähr

```text
0.085 ... 0.52 omega_p  (u^r/r)
0.17  ... 1.05 omega_p  (Kontinuitätsproxy),
```

also weit außerhalb der Stage-3.14-MD-Kalibrierung.

Damit kann der Coulomb-Plastizitätstest aus Stage 3.14 dieses neue niedrige Massenband derzeit **nicht direkt ausschließen**.

## 9. Earth-Matching-Folge

Für `M_eq~1e11 kg` liegt der PREM-Ersatzradius nur bei ungefähr

```text
133 ... 161 m.
```

Dieser Bereich liegt unterhalb der bisher voll gekoppelten, cross-solver-validierten niedrigen-Massenauflösung. Die geophysikalische Verträglichkeit des Stage-3.15-Kandidatenbands ist daher noch offen.

## 10. Hawking-Leistungs-Sensitivität

Ein Multiplikatorscan `f_H=0.1,1,10,100` bewahrt im reduzierten Modell qualitativ einen Balancepunkt und verschiebt ihn gemäß

```text
M_eq proportional f_H^(1/4).
```

Die Faktoren sind Sensitivitätsparameter und keine präzise Greybody-/Teilchenspezies-Modellierung.

## 11. Aktueller konservativer Status

```text
M_SL ~ 1e16 kg:
    relativistische Langzeitakkretion bleibt ein starker negativer Test.

M_SL ~ 1e11 kg:
    neues Hawking/Michel-Kompensationsband im reduzierten ODE,
    aber Materialtransport und Earth Matching noch nicht validiert.
```

Die gesamte kleine Erd-SL-Hypothese ist damit weder bestätigt noch durch die bisherigen Akkretionstests vollständig ausgeschlossen.

## 12. Nächste Arbeit

1. voll gekoppeltes Earth Matching im `~1e11 kg`-Band,
2. Transportmodell für extrem hohe dimensionslose Deformationsraten,
3. Hawking-Greybody-/Teilchenspezies-, Spin- und Ladungssensitivität,
4. nichtstationäre thermische Rückkopplung,
5. Formation Rule.

Details zum Massenscan: [`MASSENSCAN_STAGE3_15.md`](MASSENSCAN_STAGE3_15.md).
