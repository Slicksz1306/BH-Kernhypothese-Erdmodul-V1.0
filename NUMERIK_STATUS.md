# Numerischer Status – SL-TOV / Earth Matching

**Projekt:** BH-/SL-Kernhypothese – Erdmodul  
**Stand:** 25.08.2026  
**Aktuelle Stufe:** Earth Matching 1.3C

## 1. Bedeutung von „validiert“

In diesem Dokument bedeutet **numerisch validiert** ausschließlich:

- der definierte Solver hat die festgelegten Randbedingungen erfüllt,
- die Lösung erfüllt die jeweiligen Residual-/Regularitätskriterien,
- und – wo für die jeweilige Stufe gefordert – die vorgesehenen Konvergenzchecks sind bestanden.

Es bedeutet **nicht**:

- experimentell bestätigt,
- astrophysikalisch/geophysikalisch beobachtet,
- oder als Fundamentaltheorie bewiesen.

Die Validierung ist immer relativ zur konkret implementierten Gleichung, Closure, Diskretisierung und Parameterwahl zu lesen.

## 2. Modellkern

Der aktuelle sphärische Minimalstack verwendet im Jordan Frame

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4
```

mit

```text
y = [m, nu, p, chi, psi]
psi = dchi/dr.
```

Der GR-Grenzfall

```text
xi -> 0
chi -> 0
psi -> 0
```

muss auf die gewöhnliche GR-TOV-Struktur zurückfallen.

Die hydrostatische Außenintegration beginnt bei einem Matching-Radius

```text
r_a > r_h
r_h = 2 G M_SL / c^2.
```

Die unmittelbare BH-Nahzone wird nicht als gewöhnliche TOV-Flüssigkeit extrapoliert.

## 3. Earth-Closure

Die derzeitige Closure ist PREM-kalibriert:

1. `rho_PREM(r)` wird als Referenzprofil verwendet.
2. Daraus wird eine hydrostatische Referenzdruckkurve konstruiert.
3. Die numerischen Paare `(p,rho)` definieren `epsilon(p)`.

Das ist eine **Earth-Matching-Closure**, keine fundamentale Fe/Ni-Hochdruck-EOS.

## 4. Stufen dürfen nicht vermischt werden

### Stage 1.2 – Skalarisierungs-/Continuation-Problem

Stage 1.2 validiert den nichttrivialen **Skalarsektor** und seine Randbedingungen für mehrere Eingabeskalen und Selbstkopplungen. Dort existieren konvergierte fundamentale, knotenfreie Lösungen auch bei kurzen `r_c`-Werten.

Das ist wichtig, ist aber **noch nicht dasselbe** wie eine voll rückgekoppelte Erdvorhersage für Radius und ADM-Masse.

Daher ist die Aussage

```text
Stage 1.2: Skalar-BVP bei 100 km validiert
```

nicht im Widerspruch zu

```text
Stage 1.3C: voll gekoppelte 100-km-Erdlösung noch nicht validiert.
```

Die beiden Aussagen testen verschiedene numerische Ebenen.

## 5. Stage 1.3B – voll gekoppelte 1000-km-Referenz

Für `r_c = 1000 km` wurden voll gekoppelte differentielle Läufe für

```text
M_SL = 1e12, 1e16, 1e18 kg
q0   = 1e-14, 1e-13, 3e-13
```

unter den festgelegten Stage-1.3B-Kriterien als numerisch validiert markiert.

Beispiel für den später in 1.3C fortgesetzten Zweig:

```text
M_SL        = 1e16 kg
r_c         = 1000 km
q0          = 1e-14
Robin_norm  = 1.2014e-08
q_max       = 9.9404e-15
deltaR/R_E  = 4.7166e-05
deltaM/M_E  = 3.9143e-05
validated   = true
```

Radius und ADM-Masse sind in diesem Lauf Forward-Ausgaben; sie werden nicht als freie Zielparameter auf exakte Erdwerte gefittet.

## 6. Stage 1.3C – Fortsetzung zu kürzeren Reichweiten

Der konkrete Zweig

```text
M_SL = 1e16 kg
q0   = 1e-14
```

wurde von `r_c = 1000 km` zu kürzeren Skalen fortgesetzt.

### Precision Single Shooting

| `r_c` | Status | `Robin_norm` | `deltaR/R_E` | `deltaM/M_E` |
|---:|---|---:|---:|---:|
| 1000 km | validiert | `1.20e-08` | `4.72e-05` | `3.91e-05` |
| 750 km | validiert | `6.55e-11` | `4.74e-05` | `3.93e-05` |
| 500 km | validiert | `-8.29e-07` | `4.77e-05` | `3.95e-05` |
| 300 km | nicht validiert | `-1.76e-04` | `4.76e-05` | `3.95e-05` |
| 200 km | nicht validiert | `3.44e-01` | `4.80e-05` | `4.02e-05` |
| 150 km | nicht validiert | `9.06e+02` | `1.88e-04` | `1.02e-01` |
| 120 km | nicht validiert | `-2.84e+03` | `1.66e-04` | `3.60e-01` |
| 100 km | nicht validiert | `4.996e+03` | `2.89e-04` | `5.17e-01` |

Ein endlicher Output allein zählt ausdrücklich nicht als Lösung. Sobald das Randresiduum oder die Feldamplitude die Kriterien verletzt, wird der Punkt nicht promoted.

## 7. 100-km-Collocation-Crosscheck

Für `r_c = 100 km` wurde zusätzlich ein sparse Finite-Difference-Collocation-Ansatz getestet.

Ein 70-Punkt-Lauf erreicht beispielsweise

```text
max_abs_residual ~ 1.20e-06
deltaR/R_E       ~ -1.85e-04
deltaM/M_E       ~  6.61e-05
```

Das Residuum allein reicht jedoch nicht. Die 50/60/70-Punkt-Meshes stimmen in den vorhergesagten Erdobservablen noch nicht ausreichend überein.

Daher gilt:

```text
100 km = candidate only
100 km != validated full-coupled result
```

## 8. Aktuelle konservative Frontier

Für den speziellen Pfad

```text
M_SL = 1e16 kg
q0   = 1e-14
```

lautet der derzeit belastbare numerische Stand:

```text
voll gekoppelt validiert: r_c = 1000, 750, 500 km
numerisch offen:          r_c <= 300 km
```

Die Grenze bei 500 km ist **keine physikalische Mindestreichweite**. Sie ist die aktuelle Konditionierungs-/Solvergrenze dieser Implementierung.

## 9. Promotionsregeln für Short-Range-Lösungen

Eine Short-Range-Lösung wird erst als validiert markiert, wenn alle folgenden Bedingungen erfüllt sind:

1. Solver/Optimizer konvergiert regulär.
2. Das maximale normierte Rand-/Gleichungsresiduum liegt unter der festgelegten Toleranz.
3. Die Lösung ist unter Mesh-Verfeinerung konvergent.
4. Die Lösung bleibt bei Umkehr der Continuation-Richtung stabil.
5. Sie stimmt im Überlappungsbereich mit dem validierten Long-Range-Zweig überein.
6. Radius und ADM-Masse bleiben endlich und reproduzierbar.
7. Die nichttriviale Feldamplitude bleibt auf dem vorgesehenen fundamentalen Zweig.

## 10. Nächste numerische Schritte

Für `r_c < 500 km` sind insbesondere vorgesehen:

- steifer Boundary-Value-Solver,
- sparse/analytische Jacobians,
- Multiple Shooting,
- adaptive Mesh-Verfeinerung,
- Pseudo-Arclength-Continuation,
- Vorwärts-/Rückwärts-Continuation,
- unabhängiger Solver-Crosscheck.

Erst danach dürfen kurze Reichweiten als voll gekoppelte Theorieergebnisse promoted werden.

## 11. Reproduzierbarkeitsprinzip

Jedes veröffentlichte numerische Resultat sollte mindestens gemeinsam mit folgenden Angaben archiviert werden:

```text
Git-Commit
Solverversion
M_SL
m_chi bzw. r_c
xi
lambda
q0 / Seed
Matching-Radius r_a
Toleranzen
Mesh/Schrittweite
Randresiduen
R
M_ADM
Konvergenzstatus
```

Damit bleibt klar, welcher Zahlenwert zu welcher konkreten Gleichungs- und Solverversion gehört.
