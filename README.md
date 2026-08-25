# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Geburtsdatum:** 13.06.1988  
**Region:** Rheinland-Pfalz  
**Land:** Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.2  
**Numerischer Entwicklungsstand:** Stage 1.7  
**Stand:** 25.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Versionshinweis:** Der Repository-Name enthält aus historischen Gründen weiterhin `V1.0`. Die Datei `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` ist die unveränderte Veröffentlichungsfassung vom 23.08.2026 und bleibt als Archiv-/Prioritätsnachweis erhalten. Der SHA-256-Hash bezieht sich weiterhin auf diese unveränderte V1.0-PDF. Die Markdown-Dateien dokumentieren den fortgeschrittenen aktuellen Forschungsstand.

## Wissenschaftlicher Status

Die **SL/BH-Kernhypothese Erdmodul** ist ein theoretisches Forschungsmodell. `SL` bezeichnet in diesem Projekt ein **Schwarzes Loch**.

Für die Erde wird geprüft, ob ein kleines zentrales Schwarzes Loch in einem redistributiven Modell mit geophysikalischen Randbedingungen und einer voll gekoppelten numerischen Earth-Matching-Lösung vereinbar sein kann.

Es wird **keine direkte Detektion eines Schwarzen Lochs im Erdzentrum behauptet**. Begriffe wie „validiert“, „bestanden“ oder „cross-solver-bestätigt“ beziehen sich ausschließlich auf genau benannte interne numerische Tests.

## Aktuelles Erdmodell

Die frühere starke Grenzvariante

```text
M_SL ~ M_Earth
```

ist nicht Bestandteil des aktuellen Erdmodells. Unter PREM und Standard-GR wäre eine derart starke Zentralisierung mit radialer Massenverteilung, Seismologie und Trägheitsmoment unvereinbar.

Der aktuelle kleine redistributive Zweig verwendet stattdessen

```text
M_PREM(<r_rep) = M_SL.
```

Das zentrale Objekt wird also nicht zusätzlich zur gemessenen Erdmasse addiert, sondern ersetzt im Basismodell dieselbe PREM-Masse im Zentrum. Im ideal kugelsymmetrischen Grenzfall gilt außerhalb der Ersatzregion

```text
M_model(<r) = M_PREM(<r),  r >= r_rep.
```

## Drei getrennte Skalen

```text
Schwarzschildradius:        r_s   = 2 G M_SL / c^2
Bondi-/Referenzskala:       r_B   = G M_SL / c_eff^2
Struktureller Ersatzradius: M_PREM(<r_rep) = M_SL
```

`r_s`, `r_B` und `r_rep` sind physikalisch verschiedene Größen und dürfen nicht gleichgesetzt werden.

## Numerischer Stack

Der aktuelle Simulationsstack verwendet eine sphärische Jordan-Frame-Minimalfassung mit

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4
```

und

```text
y = [m, nu, p, chi, psi]
psi = dchi/dr.
```

Die hydrostatische Integration beginnt außerhalb der unmittelbaren BH-Nahzone bei einem Matching-Radius `r_a > r_h`. Der GR-Grenzfall `xi -> 0`, `chi -> 0`, `psi -> 0` bleibt ein harter Solvercheck.

## Fortschritt von Stage 1.3C bis Stage 1.7

Der ältere öffentliche Stand endete bei einer voll gekoppelten Single-Shooting-Frontier von `r_c = 500 km`. In den nachfolgenden Tests wurde dieser Stand deutlich erweitert.

### Stage 1.5D – BH-konsistente Fortsetzung

Für den Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

wurden

```text
r_c = 500 km  -> validiert
r_c = 300 km  -> validiert
r_c = 275 km  -> Kandidat
r_c <= 250 km -> numerisch offen
```

erreicht.

Für den 300-km-Punkt gilt ungefähr

```text
xi / xi_crit,BH ≈ 1.000142
q_max            ≈ 1e-14
Delta M_SL/M_GR  ≈ -(8–9)e-6.
```

### Stage 1.6 – Layered-PREM-EOS und Cross-Solver

Die verbesserte geschichtete PREM-nahe Earth-Closure reproduziert die GR-Baseline mit ungefähr

```text
Delta R/R ≈ 4.17e-9
Delta M/M ≈ 4.44e-8.
```

Damit wurde der systematische Baselinefehler gegenüber der älteren Barotrop-Closure stark reduziert.

Voll gekoppelt und cross-solver-validiert sind aktuell:

| `r_c` | `Delta M/M` gegenüber GR | Status |
|---:|---:|---|
| 500 km | `≈ -9.2e-6` | validiert |
| 300 km | `≈ -8.65e-6` | validiert |
| 250 km | — | Kandidat |
| 200 km | — | offen |

Der **kleinste derzeit cross-solver-validierte voll gekoppelte Punkt ist `r_c = 300 km`**.

## Stage 1.7 – Erdobservablen

Auf den validierten 500- und 300-km-Lösungen wurden anschließend messnähere Größen ausgewertet.

### Gravitation

| `r_c` | `max |Delta g/g|` für `r >= 100 km` | zentrale Größenordnung ab `r >= 10 km` |
|---:|---:|---:|
| 500 km | `≈ 1.8e-4` | `≈ 1.5e-3` |
| 300 km | `≈ 2.1e-4` | `≈ 1.6e-3` |

### P-Wellen-Geschwindigkeit

Für beide validierten Referenzzweige liegt die relative Änderung in der Größenordnung

```text
|Delta V_P/V_P| ~ 3e-6.
```

### ICB-/CMB-Verschiebung

| `r_c` | `Delta r_ICB` | `Delta r_CMB` |
|---:|---:|---:|
| 500 km | `-43.8 m` | `-35.0 m` |
| 300 km | `-61.1 m` | `-33.9 m` |

### P-Wellen-Laufzeit

| `r_c` | `Delta T_P` |
|---:|---:|
| 500 km | `+0.0119 s` |
| 300 km | `+0.0088 s` |

### Trägheitsmoment

Für die Materiekomponente ergibt sich im Referenzzweig ungefähr

```text
Delta I/I ~ -(7–8)e-6.
```

Diese Größen sind **Vorhersagen des angegebenen numerischen Modells**, keine bereits gemessenen Anomalien.

## Amplituden-Sensitivität bei `r_c = 300 km`

Zusätzlich wurde die Reaktion auf größere Feldamplituden untersucht:

| `q(r_a)` | `Delta r_ICB` | `Delta r_CMB` | `Delta T_P` |
|---:|---:|---:|---:|
| `1e-14` | `≈ -61 m` | `≈ -34 m` | `+0.0088 s` |
| `1e-13` | `≈ -604 m` | `≈ -339 m` | `≈ +0.095 s` |
| `3e-13` | `≈ -1.77 km` | `≈ -1.02 km` | nicht als konservativer Referenzwert promoted |

Der Amplitudenscan ist eine Sensitivitätsstudie und nicht automatisch eine Validierung dieser größeren Amplituden als physikalische Erdparameter.

## Aktueller belastbarer Kernstatus

Für den konkret dokumentierten Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

ist der aktuelle konservative Status:

```text
500 km -> voll gekoppelt validiert
300 km -> voll gekoppelt und cross-solver-validiert
250–275 km -> Kandidatenbereich, abhängig von Teststufe
<= 200–250 km -> numerisch offen
```

Die 300-km-Frontier ist eine aktuelle numerische Validierungsgrenze der Implementierung und **keine fundamentale physikalische Mindestreichweite**.

Die vollständige Trennung der Stages und Kennzahlen steht in [`TEST_STATUS.md`](TEST_STATUS.md) und [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md).

## Offene Physik

Noch nicht geschlossen sind insbesondere:

1. Formation Rule / Entstehungsmechanismus des zentralen SL,
2. Near-Zone-Capture- und Akkretionsphysik,
3. thermischer Energie- und Transportabschluss,
4. fundamentale Hochdruck-Fe/Ni-EOS statt PREM-kalibrierter Näherung,
5. vollständiger PREM-/Normalmoden-/Laufzeit-Likelihood-Fit,
6. robuste Short-Range-BVP-Lösung unterhalb von 300 km,
7. unabhängige, vorab festgelegte Detektionssignaturen und reale Datenanalyse.

## Falsifikationsprinzip

Eine konkrete Parameterwahl muss mit **demselben Parametersatz** gleichzeitig gegen alle relevanten Beobachtungsklassen bestehen. Parameter dürfen nicht für jeden Test separat nachjustiert werden.

Zu prüfen sind insbesondere Erdmasse und Radius, Trägheitsmoment, Seismologie, Normalmoden, Wärmehaushalt, Langzeitstabilität, Formation, Akkretion sowie numerische Konvergenz.

## Wissenschaftlicher Review

Technische Kritik, Reproduktionsversuche und Falsifikationsanalysen sind ausdrücklich erwünscht. Für belastbare Reviews siehe [`CONTRIBUTING.md`](CONTRIBUTING.md). Ein strukturiertes GitHub-Issue-Template ist ebenfalls vorhanden.

## Dateien

- [`THEORIE.md`](THEORIE.md) – aktueller Erdmodul-Theoriestand.
- [`TEST_STATUS.md`](TEST_STATUS.md) – aktueller Stage-1.7-Test- und Validierungsstand mit Kennzahlen.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) – numerische Entwicklung und Solvergrenzen.
- [`CHANGELOG.md`](CHANGELOG.md) – nachvollziehbare Entwicklung der öffentlichen Theorie- und Numerikstände.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) – Anforderungen für Reproduktion, Review und technische Einwände.
- [`LICENSE`](LICENSE) – Rechte- und Nutzungshinweis.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` – archivierte Erstveröffentlichung V1.0 vom 23.08.2026.
- `SHA256SUMS.txt` – Prüfsumme der archivierten V1.0-PDF.
- `CITATION.cff` – Zitiermetadaten des aktuellen Repository-Textstands.

## Primärreferenz

A. M. Dziewonski & D. L. Anderson (1981), *Preliminary Reference Earth Model*, Physics of the Earth and Planetary Interiors 25, 297–356. DOI: 10.1016/0031-9201(81)90046-7.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.2*, Theorie- und Forschungsentwurf, numerischer Entwicklungsstand Stage 1.7, Rheinland-Pfalz, Deutschland.
