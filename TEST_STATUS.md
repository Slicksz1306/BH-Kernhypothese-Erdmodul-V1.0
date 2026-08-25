# SL/BH-Kernhypothese Erdmodul – aktueller Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 25.08.2026  
**Theorie-Textstand:** Erdmodul V1.2  
**Numerischer Entwicklungsstand:** Stage 1.7  

## 1. Statusbegriffe

Die in diesem Repository verwendeten Begriffe werden strikt getrennt:

- **validiert** = der konkret angegebene numerische Test bzw. Solver-Check erfüllt die festgelegten Kriterien,
- **Kandidat** = numerisch plausibel, aber mindestens ein erforderlicher Crosscheck fehlt,
- **offen** = mit dem aktuellen Verfahren noch nicht belastbar entschieden,
- **empirisch bestätigt** = würde eine unabhängige Beobachtung oder Messung erfordern und ist derzeit **nicht** erreicht.

Kein numerischer Status in diesem Dokument ist ein direkter Nachweis eines Schwarzen Lochs im Erdzentrum.

## 2. Referenzzweig

Der derzeit am weitesten ausgearbeitete Referenzzweig verwendet

```text
M_SL = 1e16 kg
q(r_a) = 1e-14
```

mit einer kleinen redistributiven Zentralmasse. Das zentrale Objekt wird im Basismodell nicht zusätzlich zur Erdmasse addiert, sondern ersetzt dieselbe PREM-Masse im Zentralbereich.

## 3. Stage 1.3C – frühere Short-Range-Frontier

Der ältere voll gekoppelte Single-Shooting-Stand validierte den Referenzzweig bei

```text
r_c = 1000 km
r_c =  750 km
r_c =  500 km
```

und verlor unterhalb von 500 km zunehmend die numerische Konditionierung. Der damalige 100-km-Collocation-Lauf blieb wegen fehlender Mesh-Konvergenz Kandidat.

Dieser Stand ist historisch wichtig, wurde aber durch die späteren Solver- und EOS-Stufen erweitert.

## 4. Stage 1.5D – BH-konsistente Fortsetzung

Mit der verbesserten BH-konsistenten Randwertbehandlung wurde die frühere Frontier verschoben.

Für den Referenzzweig gilt:

| `r_c` | Status |
|---:|---|
| 500 km | validiert |
| 300 km | validiert |
| 275 km | Kandidat |
| 250–100 km | offen |

Für `r_c = 300 km` wurde im validierten Zweig ungefähr

```text
xi / xi_crit,BH ≈ 1.000142
q_max            ≈ 1e-14
```

erreicht.

Die differentielle Massenabweichung des SL-Zweigs gegenüber dem zugehörigen GR-Lauf liegt in dieser Stufe ungefähr bei

```text
Delta M_SL / M_GR ≈ -(8–9)e-6.
```

Zum Vergleich lag die ältere systematische Abweichung der reinen GR/PREM-Barotrop-Closure in der Größenordnung

```text
~ 6.94e-5,
```

also deutlich über dem differentiellen Signal des späteren SL-Zweigs. Genau deshalb wurde die Earth-Closure anschließend weiter verbessert.

## 5. Stage 1.6 – Layered-PREM-EOS und Cross-Solver-Validierung

Stage 1.6 ersetzt die grobere Barotrop-Proxy-Baseline durch eine stärker geschichtete PREM-nahe Earth-Closure.

### GR-Baseline

Die neue GR-Baseline reproduziert die Zielwerte mit ungefähr

```text
Delta R / R ≈ 4.17e-9
Delta M / M ≈ 4.44e-8
```

und liegt damit konservativ auf dem Niveau `~1e-7` oder besser.

### Voll gekoppelte SL-Läufe

Für den Referenzzweig wurden cross-solver-validiert:

| `r_c` | `Delta M/M` gegenüber GR | Status |
|---:|---:|---|
| 500 km | `≈ -9.2e-6` | validiert |
| 300 km | `≈ -8.65e-6` | validiert |
| 250 km | — | Kandidat |
| 200 km | — | offen |

Der **kleinste derzeit cross-solver-validierte voll gekoppelte Punkt ist damit `r_c = 300 km`**.

Diese 300-km-Grenze ist eine aktuelle numerische Validierungsgrenze des implementierten Zweigs, keine fundamentale physikalische Mindestreichweite.

## 6. Stage 1.7 – abgeleitete Erdobservablen

Auf den validierten Referenzlösungen wurden anschließend messnähere Größen ausgewertet.

### 6.1 Relative Gravitation

Für `M_SL = 1e16 kg`, `q(r_a)=1e-14`:

| `r_c` | `max |Delta g/g|` für `r >= 100 km` | zentrale Größenordnung ab `r >= 10 km` |
|---:|---:|---:|
| 500 km | `≈ 1.8e-4` | `≈ 1.5e-3` |
| 300 km | `≈ 2.1e-4` | `≈ 1.6e-3` |

Diese Werte sind Modellvorhersagen des konkret angegebenen numerischen Zweigs, keine bereits gemessenen Anomalien.

### 6.2 P-Wellen-Geschwindigkeit

Die relative Änderung der modellierten P-Wellen-Geschwindigkeit liegt für die validierten Referenzzweige in der Größenordnung

```text
|Delta V_P / V_P| ~ 3e-6.
```

### 6.3 ICB-/CMB-Verschiebungen

`ICB` = Inner Core Boundary, `CMB` = Core-Mantle Boundary.

| `r_c` | `Delta r_ICB` | `Delta r_CMB` |
|---:|---:|---:|
| 500 km | `-43.8 m` | `-35.0 m` |
| 300 km | `-61.1 m` | `-33.9 m` |

### 6.4 P-Wellen-Laufzeit

Die berechnete differentielle P-Wellen-Laufzeitänderung beträgt:

| `r_c` | `Delta T_P` |
|---:|---:|
| 500 km | `+0.0119 s` |
| 300 km | `+0.0088 s` |

### 6.5 Trägheitsmoment

Für die Materiekomponente liegt die differentielle Änderung des normierten Trägheitsmoments in der Größenordnung

```text
Delta I / I ~ -(7–8)e-6.
```

Auch dieser Wert gehört zum angegebenen Referenzzweig und ist nicht als unabhängige Messung zu lesen.

## 7. Stage-1.7-Amplitudenscan bei `r_c = 300 km`

Zusätzlich wurde die Reaktion auf größere Feldamplituden untersucht. Dieser Scan dient der Sensitivitätsanalyse und darf nicht mit dem validierten Referenzpunkt `q=1e-14` gleichgesetzt werden.

| `q(r_a)` | `Delta r_ICB` | `Delta r_CMB` | `Delta T_P` |
|---:|---:|---:|---:|
| `1e-14` | `≈ -61 m` | `≈ -34 m` | `+0.0088 s` |
| `1e-13` | `≈ -604 m` | `≈ -339 m` | `≈ +0.095 s` |
| `3e-13` | `≈ -1.77 km` | `≈ -1.02 km` | nicht als konservativer Referenzwert promoted |

Der Scan zeigt, dass die beobachtungsnahen Signaturen mit wachsender Amplitude schnell größer werden. Er dient damit auch dazu, zukünftige Ausschluss- und Sensitivitätsgrenzen zu formulieren.

## 8. Was gegenüber dem alten Repository-Stand erreicht wurde

Der frühere öffentliche Stand endete im Wesentlichen bei der Stage-1.3C-Frontier von 500 km. Seitdem wurden folgende Fortschritte erzielt:

1. BH-konsistentere Randwertbehandlung,
2. Fortsetzung des voll gekoppelten Zweigs bis 300 km,
3. Layered-PREM-EOS / deutlich präzisere GR-Baseline,
4. Cross-Solver-Validierung der 500- und 300-km-Punkte,
5. explizite Gravitätsprofile,
6. P-Wellen-Geschwindigkeitsänderungen,
7. ICB-/CMB-Verschiebungen,
8. P-Wellen-Laufzeitänderungen,
9. Trägheitsmoment-Abweichungen,
10. Amplituden-Sensitivität bei `r_c=300 km`.

Damit ist der aktuelle Entwicklungsstand deutlich weiter als der alte 1.3C-Repository-Text.

## 9. Konservativer aktueller Status

Für den konkret dokumentierten Referenzzweig

```text
M_SL = 1e16 kg
q(r_a) = 1e-14
```

lautet der derzeit belastbare numerische Status:

```text
r_c = 500 km  -> validiert
r_c = 300 km  -> validiert und cross-solver-bestätigt
r_c = 250–275 km -> Kandidatenbereich
r_c <= 200–250 km -> numerisch offen, abhängig von Stufe und Solver
```

Die exakte Grenze hängt vom jeweiligen Testlevel ab. Deshalb werden Stage-1.5D-, Stage-1.6- und Stage-1.7-Aussagen getrennt dokumentiert und nicht zu einer künstlich schärferen physikalischen Grenze vermischt.

## 10. Noch offene harte Prüfsteine

Trotz des Fortschritts bleiben insbesondere offen:

- robuste Fortsetzung unterhalb von 300 km,
- vollständige Mesh-/Jacobian-/Continuation-Konvergenz im Short-Range-Bereich,
- fundamentale Hochdruck-Fe/Ni-EOS statt PREM-kalibrierter Näherung,
- Near-Zone-Capture- und Akkretionsphysik,
- thermischer Langzeitabschluss,
- konsistente Formation Rule,
- vollständiger Seismologie-/Normalmoden-Likelihood-Fit,
- unabhängige, vorab definierte Detektionssignaturen und reale Datenanalyse.

## 11. Wissenschaftliche Aussagegrenze

Der aktuelle Stand erlaubt die Aussage, dass innerhalb der implementierten Gleichungen, Randbedingungen und numerischen Tests ein kleiner redistributiver SL/BH-Zweig bis `r_c = 300 km` reproduzierbar numerisch verfolgt und mit mehreren abgeleiteten Erdobservablen charakterisiert wurde.

Er erlaubt **nicht** die Aussage, dass ein Schwarzes Loch im Erdzentrum experimentell nachgewiesen wurde.
