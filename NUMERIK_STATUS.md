# Numerischer Status – SL-TOV / Earth Matching

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 25.08.2026  
**Aktuelle Stufe:** Stage 1.7

## 1. Bedeutung von „validiert“

In diesem Dokument bedeutet **numerisch validiert** ausschließlich:

- der definierte Solver erfüllt die festgelegten Randbedingungen,
- die Lösung erfüllt die jeweiligen Residual-/Regularitätskriterien,
- die für die jeweilige Stage vorgesehenen Konvergenz- oder Cross-Solver-Checks sind bestanden.

Es bedeutet **nicht**:

- experimentell bestätigt,
- geophysikalisch direkt beobachtet,
- oder als Fundamentaltheorie bewiesen.

Die Validierung ist immer relativ zur konkret implementierten Gleichung, Closure, Diskretisierung, Parameterwahl und Teststufe zu lesen.

## 2. Modellkern

Der sphärische Minimalstack verwendet im Jordan Frame

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

Die Außenintegration beginnt bei

```text
r_a > r_h
r_h = 2 G M_SL / c^2.
```

Die unmittelbare BH-Nahzone wird nicht als gewöhnliche TOV-Flüssigkeit durch den Horizont extrapoliert.

## 3. Referenzzweig

Der am weitesten untersuchte aktuelle Zweig verwendet

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14.
```

Dieser Parametersatz wird für die Stage-1.5D-, Stage-1.6- und Stage-1.7-Vergleiche beibehalten, damit die Teststufen nicht durch jeweils neue Fitparameter vermischt werden.

## 4. Stufen dürfen nicht vermischt werden

Die einzelnen Stages testen unterschiedliche Ebenen:

- **Stage 1.2:** nichttrivialer Skalar-BVP / Continuation,
- **Stage 1.3B/C:** frühe voll gekoppelte Earth-Matching-Läufe,
- **Stage 1.5D:** verbesserte BH-konsistente Randwertfortsetzung,
- **Stage 1.6:** Layered-PREM-EOS und Cross-Solver-Validierung,
- **Stage 1.7:** Ableitung beobachtungsnaher Erdobservablen.

Ein Punkt kann daher in einer niedrigeren Stufe numerisch existieren, ohne bereits als vollständige Earth-Matching-Lösung einer höheren Stufe validiert zu sein.

## 5. Historischer Stand Stage 1.3B

Für `r_c = 1000 km` wurden voll gekoppelte differentielle Läufe für

```text
M_SL = 1e12, 1e16, 1e18 kg
q0   = 1e-14, 1e-13, 3e-13
```

unter den damaligen Kriterien validiert.

Beispiel des später fortgesetzten Referenzzweigs:

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

## 6. Historischer Stand Stage 1.3C

Die damalige Precision-Single-Shooting-Fortsetzung ergab:

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

Ein 70-Punkt-Collocation-Lauf bei 100 km erreichte zwar

```text
max_abs_residual ~ 1.20e-06
deltaR/R_E       ~ -1.85e-04
deltaM/M_E       ~  6.61e-05
```

aber keine ausreichende Mesh-Konvergenz. Deshalb blieb 100 km Kandidat und wurde nicht promoted.

Dieser alte Stand setzte die voll gekoppelte Frontier bei 500 km. Die späteren Stages verschieben diese **numerische** Frontier.

## 7. Stage 1.5D – BH-konsistente Fortsetzung

Mit verbesserter BH-konsistenter Randwertbehandlung wurde der Referenzzweig weitergeführt.

| `r_c` | Status Stage 1.5D |
|---:|---|
| 500 km | validiert |
| 300 km | validiert |
| 275 km | Kandidat |
| 250–100 km | offen |

Für `r_c = 300 km` gilt ungefähr

```text
xi / xi_crit,BH ≈ 1.000142
q_max            ≈ 1e-14.
```

Die differentielle Massenabweichung des SL-Zweigs gegenüber dem jeweiligen GR-Lauf beträgt ungefähr

```text
Delta M_SL / M_GR ≈ -(8–9)e-6.
```

Die ältere GR/PREM-Barotrop-Closure hatte dagegen eine systematische Baselineabweichung von ungefähr

```text
~ 6.94e-5.
```

Damit war die Closure-Ungenauigkeit größer als das zu untersuchende differentielle SL-Signal. Das motivierte Stage 1.6.

## 8. Stage 1.6 – Layered-PREM-EOS

Stage 1.6 verwendet eine deutlich präzisere geschichtete PREM-nahe Earth-Closure.

### 8.1 GR-Baseline

Die reproduzierte GR-Baseline liegt ungefähr bei

```text
Delta R/R ≈ 4.17e-9
Delta M/M ≈ 4.44e-8.
```

Konservativ liegt die numerische Baseline damit auf dem Niveau `~1e-7` oder besser.

### 8.2 Voll gekoppelte SL-Läufe

| `r_c` | `Delta M/M` gegenüber GR | Status Stage 1.6 |
|---:|---:|---|
| 500 km | `≈ -9.2e-6` | validiert |
| 300 km | `≈ -8.65e-6` | validiert |
| 250 km | — | Kandidat |
| 200 km | — | offen |

Der **kleinste derzeit cross-solver-validierte voll gekoppelte Punkt ist `r_c = 300 km`**.

Die 300-km-Grenze ist eine Solver-/Validierungsfrontier des aktuellen Referenzzweigs, keine physikalische Ausschlussgrenze für kleinere Reichweiten.

## 9. Stage 1.7 – abgeleitete Erdobservablen

Auf den cross-solver-validierten 500- und 300-km-Punkten wurden beobachtungsnähere Größen berechnet.

### 9.1 Relative Gravitation

| `r_c` | `max |Delta g/g|`, `r >= 100 km` | zentrale Größenordnung ab `r >= 10 km` |
|---:|---:|---:|
| 500 km | `≈ 1.8e-4` | `≈ 1.5e-3` |
| 300 km | `≈ 2.1e-4` | `≈ 1.6e-3` |

### 9.2 P-Wellen-Geschwindigkeit

Für beide Referenzpunkte liegt

```text
|Delta V_P/V_P| ~ 3e-6.
```

### 9.3 ICB-/CMB-Lage

| `r_c` | `Delta r_ICB` | `Delta r_CMB` |
|---:|---:|---:|
| 500 km | `-43.8 m` | `-35.0 m` |
| 300 km | `-61.1 m` | `-33.9 m` |

### 9.4 P-Wellen-Laufzeit

| `r_c` | `Delta T_P` |
|---:|---:|
| 500 km | `+0.0119 s` |
| 300 km | `+0.0088 s` |

### 9.5 Materie-Trägheitsmoment

Die differentielle Änderung liegt in der Größenordnung

```text
Delta I/I ~ -(7–8)e-6.
```

Die Stage-1.7-Werte sind Modellvorhersagen der angegebenen numerischen Lösungen und keine bereits beobachteten terrestrischen Anomalien.

## 10. Amplitudenscan bei `r_c = 300 km`

Die Sensitivität auf größere Randamplituden wurde zusätzlich untersucht:

| `q(r_a)` | `Delta r_ICB` | `Delta r_CMB` | `Delta T_P` |
|---:|---:|---:|---:|
| `1e-14` | `≈ -61 m` | `≈ -34 m` | `+0.0088 s` |
| `1e-13` | `≈ -604 m` | `≈ -339 m` | `≈ +0.095 s` |
| `3e-13` | `≈ -1.77 km` | `≈ -1.02 km` | nicht als konservativer Referenzwert promoted |

Diese Punkte bilden einen Sensitivitätsscan. Größere `q`-Werte werden nicht allein aufgrund dieses Scans als physikalisch zulässige Erdparameter promoted.

## 11. Aktuelle Statusmatrix

Für den Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

ergibt sich derzeit:

| Bereich | aktueller konservativer Status |
|---|---|
| `r_c = 500 km` | voll gekoppelt validiert |
| `r_c = 300 km` | voll gekoppelt + cross-solver-validiert; Stage-1.7-Observablen berechnet |
| `r_c = 250–275 km` | Kandidatenbereich; Status hängt von Stage/Solver ab |
| `r_c <= 200–250 km` | numerisch offen |

Die verschiedenen Stage-Grenzen werden bewusst getrennt dokumentiert. Es wird keine künstlich schärfere physikalische Grenze aus unterschiedlichen Solverstufen zusammengesetzt.

## 12. Promotionsregeln für Short-Range-Lösungen

Eine Short-Range-Lösung wird erst als validiert markiert, wenn mindestens erfüllt sind:

1. reguläre Solver-/Optimizer-Konvergenz,
2. Rand- und Gleichungsresiduen unter den festgelegten Toleranzen,
3. Mesh-Konvergenz,
4. Stabilität gegenüber Continuation-Richtung,
5. Übereinstimmung unabhängiger Solver im Überlappungsbereich,
6. endliche und reproduzierbare Radius-/ADM-Masse,
7. Erhalt des vorgesehenen nichttrivialen fundamentalen Zweigs,
8. konsistente Earth-Closure-Baseline.

## 13. Offene numerische Arbeit

Für kürzere Reichweiten bleiben insbesondere:

- steifer Boundary-Value-Solver,
- analytische/sparse Jacobians,
- Multiple Shooting,
- adaptive Mesh-Verfeinerung,
- Pseudo-Arclength-Continuation,
- Vorwärts-/Rückwärts-Continuation,
- unabhängige Solver-Crosschecks,
- fundamentale Fe/Ni-Hochdruck-EOS,
- vollständiger Seismologie-/Normalmoden-Likelihood-Fit.

## 14. Reproduzierbarkeitsprinzip

Jedes veröffentlichte numerische Resultat soll mindestens mit folgenden Angaben archiviert werden:

```text
Git-Commit
Solverversion / Stage
M_SL
m_chi bzw. r_c
xi
lambda
q(r_a) / Seed
Matching-Radius r_a
Earth-Closure / EOS-Version
Toleranzen
Mesh / Schrittweite
Randresiduen
R
M_ADM
abgeleitete Observablen
Konvergenzstatus
Cross-Solver-Status
```

## 15. Aktuelle Aussagegrenze

Der aktuelle numerische Stand zeigt, dass der dokumentierte kleine redistributive Referenzzweig bis `r_c = 300 km` voll gekoppelt und cross-solver-validiert verfolgt werden konnte und dass für diesen Zweig inzwischen Gravitation, P-Wellen-Geschwindigkeit, ICB/CMB-Lage, P-Wellen-Laufzeit und Trägheitsmoment als differentielle Modellvorhersagen berechnet wurden.

Das ist ein deutlich weitergehender numerischer Stand als Stage 1.3C, aber weiterhin **kein experimenteller Nachweis** eines Schwarzen Lochs im Erdzentrum.
