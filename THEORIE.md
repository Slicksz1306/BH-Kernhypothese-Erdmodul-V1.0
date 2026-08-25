# SL/BH-Kernhypothese Erdmodul V1.2

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** V1.2  
**Numerischer Entwicklungsstand:** Stage 1.7  
**Stand:** 25.08.2026  
**Erstveröffentlichung V1.0:** 23.08.2026

## 1. Gegenstand und Status

`SL` bezeichnet in diesem Projekt ein **Schwarzes Loch**.

Die definierende Modellannahme des Erdmoduls lautet:

> Im Zentrum der Erde wird ein kleines Schwarzes Loch als kompakte Zentralmasse modelliert, dessen Masse im redistributiven Basismodell nicht zusätzlich zur Erdmasse addiert wird, sondern eine gleich große Menge der sonst angenommenen zentralen PREM-Masse ersetzt.

Diese Aussage ist eine **Hypothese**, keine Beobachtung. Es liegt kein direkter experimenteller Nachweis eines Schwarzen Lochs im Erdzentrum vor.

Der aktuelle Stand trennt vier Ebenen:

1. redistributive Massenbuchhaltung,
2. geophysikalische Konsistenztests,
3. voll gekoppelte numerische Earth-Matching-Lösung,
4. daraus abgeleitete beobachtungsnahe Signaturen.

## 2. Abgrenzung von der früheren starken Grenzvariante

Die frühere Grenzidee

```text
M_SL ~ M_Earth
```

als nahezu alleiniger Träger der Erdmasse ist nicht das aktuelle Modell. Unter PREM und Standard-GR würde eine derart starke Zentralisierung die radiale Massenverteilung, das Trägheitsmoment und die Seismologie massiv verändern.

Das aktuelle Modell untersucht einen **kleinen redistributiven SL/BH-Zweig**.

## 3. Nullmodell und Massenbuchhaltung

Als geophysikalische Referenz dient PREM.

Für eine gewählte Zentralmasse `M_SL` wird der strukturelle Ersatzradius `r_rep` definiert durch

```text
M_PREM(<r_rep) = M_SL.
```

Im Basismodell wird genau diese PREM-Masse aus dem Zentralbereich entfernt und durch die kompakte Zentralmasse ersetzt.

Für `r >= r_rep` gilt in der ideal kugelsymmetrischen Massenbuchhaltung

```text
M_model(<r) = M_PREM(<r).
```

Damit bleibt dort im monopolen Newton-Grenzfall

```text
g_model(r) = g_PREM(r).
```

Das ist eine Buchhaltungsidentität. Druckprofil, Materialphysik, Seismologie und relativistische Feldgleichungen müssen zusätzlich separat konsistent gelöst werden.

## 4. Drei physikalisch verschiedene Radien

### Schwarzschildradius

```text
r_s = 2 G M_SL / c^2
```

### Bondi-/Referenzskala

```text
r_B = G M_SL / c_eff^2
```

`c_eff` ist im Erdinneren eine modellabhängige Referenzgröße. Die seismische P-Wellen-Geschwindigkeit ist nicht automatisch identisch mit dem thermodynamischen Schallparameter eines idealen Bondi-Fluids.

### Struktureller Ersatzradius

```text
M_PREM(<r_rep) = M_SL
```

nahe dem Zentrum näherungsweise

```text
r_rep ~= [3 M_SL / (4 pi rho_c)]^(1/3).
```

Bei `rho_c ~ 1.31e4 kg/m^3` ergeben sich ungefähr:

| `M_SL` | `r_rep` |
|---:|---:|
| `1e10 kg` | `57 m` |
| `1e12 kg` | `0.26 km` |
| `1e14 kg` | `1.2 km` |
| `1e16 kg` | `5.7 km` |
| `1e18 kg` | `26 km` |
| `1e20 kg` | `122 km` |
| `1e22 kg` | `568 km` |

Es gilt ausdrücklich

```text
r_s != r_B != r_rep.
```

## 5. Trägheitsmoment und Seismologie

Eine zentrale Redistribution verändert den Beitrag der ersetzten Materie zum axialen Trägheitsmoment. Im einfachen kugelsymmetrischen Ersatzmodell ist die führende Änderung

```text
Delta C = -(8 pi / 3) Integral[0,r_rep] rho(r) r^4 dr.
```

PREM kodiert gleichzeitig die radiale Erdstruktur über seismische Laufzeiten, Normalmoden und globale Parameter. Eine vollständige Version des Modells muss deshalb Massenprofil, Trägheitsmoment und Seismologie mit demselben Parametersatz bestehen.

## 6. Akkretion, Wärme und Langzeitentwicklung

Die klassische Bondi-Formel

```text
dM/dt = 4 pi lambda G^2 rho M^2 / c_eff^3
```

wird nur als Referenzbenchmark verwendet. Der reale Erdkern ist kein unendliches homogenes ideales Gas.

Relevante offene Punkte sind unter anderem:

- Festkörper-/Flüssigkeitsstruktur,
- Hochdruck-EOS,
- diskrete beziehungsweise ballistische Capture-Prozesse,
- relativistische Nahzone,
- Wärmeleitung und Konvektion,
- Langzeitentwicklung von `M_SL(t)` und Erdstruktur.

Für eine lokale thermische Deponierung gilt formal

```text
L_SL = eta (dM/dt) c^2.
```

Die tatsächliche Stärke dieses Constraints hängt von Capture-Rate, Effizienz und Energietransport ab.

## 7. Formation Rule

Normale Erdkernmaterie kollabiert unter Standard-GR nicht spontan zu einem kleinen Schwarzen Loch der hier betrachteten Art.

Das Modell benötigt daher eine explizite Entstehungs- oder Einfanggeschichte. Solange diese nicht quantitativ geschlossen ist, bleibt die Formation Rule eine offene Physikfrage.

## 8. Dynamische Erweiterung: SL-TOV-Minimalmodell

Der numerische Stack verwendet im Jordan Frame

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4
```

mit

```text
y = [m, nu, p, chi, psi]
psi = dchi/dr.
```

Implementiert werden gekoppelte Massen-, Metrik-, Druck- und Skalarfeldgleichungen, Materieerhaltung/TOV-Hydrostatik, Matching außerhalb der SL-Nahzone und ein harter GR-Grenztest.

Im Grenzfall

```text
xi -> 0
chi -> 0
psi -> 0
```

muss die gewöhnliche GR-TOV-Struktur zurückgewonnen werden.

## 9. Matching und Earth-Closure

Die Integration startet bei

```text
r_a > r_h
r_h = 2 G M_SL / c^2.
```

Die unmittelbare BH-Nahzone wird nicht künstlich als gewöhnliche TOV-Flüssigkeit fortgesetzt.

Der ältere Stack verwendete eine PREM-kalibrierte Barotrop-Closure. Stage 1.6 führte eine präzisere geschichtete PREM-nahe Earth-Closure ein. Sie ist weiterhin keine fundamentale Fe/Ni-Hochdruck-EOS, reduziert aber den numerischen Baselinefehler erheblich.

## 10. Nichttrivialer Skalarzweig

`chi = 0` ist im Minimalmodell immer eine Lösung. Nichttriviale scalarisierte Lösungen müssen deshalb gezielt über Seed, Eigenwertsuche und Continuation verfolgt werden.

Radius und ADM-Masse werden in den fortgeschrittenen Läufen als Forward-Ausgaben kontrolliert und nicht beliebig auf die gewünschten Erdwerte gefittet.

## 11. Historische Stage 1.3C

Für den Referenzzweig

```text
M_SL = 1e16 kg
q0   = 1e-14
```

war mit Precision Single Shooting zunächst

```text
r_c = 1000, 750, 500 km
```

validiert. `r_c = 300 km` war damals numerisch schlecht konditioniert. Ein 100-km-Collocation-Lauf erreichte kleine Residuen, aber keine ausreichende Mesh-Konvergenz.

Diese 500-km-Frontier war eine Solvergrenze der damaligen Implementierung und wurde später erweitert.

## 12. Stage 1.5D – BH-konsistente Fortsetzung

Mit verbesserter BH-konsistenter Randwertbehandlung gilt für den Referenzzweig:

```text
500 km -> validiert
300 km -> validiert
275 km -> Kandidat
250–100 km -> offen
```

Für `r_c = 300 km` wurde ungefähr

```text
xi / xi_crit,BH ≈ 1.000142
q_max            ≈ 1e-14
```

erreicht.

Die differentielle Massenabweichung gegenüber dem jeweiligen GR-Lauf liegt ungefähr bei

```text
Delta M_SL/M_GR ≈ -(8–9)e-6.
```

Die ältere GR/PREM-Barotrop-Closure hatte eine systematische Abweichung von ungefähr `6.94e-5`, weshalb eine präzisere Earth-Closure notwendig war.

## 13. Stage 1.6 – Layered-PREM-EOS und Cross-Solver

Die neue GR-Baseline reproduziert die Zielwerte mit ungefähr

```text
Delta R/R ≈ 4.17e-9
Delta M/M ≈ 4.44e-8.
```

Damit liegt die Baseline konservativ auf dem Niveau `~1e-7` oder besser.

Für den Referenzzweig wurden voll gekoppelt und cross-solver-validiert:

| `r_c` | `Delta M/M` gegenüber GR | Status |
|---:|---:|---|
| 500 km | `≈ -9.2e-6` | validiert |
| 300 km | `≈ -8.65e-6` | validiert |
| 250 km | — | Kandidat |
| 200 km | — | offen |

Damit ist `r_c = 300 km` der kleinste derzeit cross-solver-validierte voll gekoppelte Punkt.

## 14. Stage 1.7 – beobachtungsnahe Erdobservablen

Für

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

wurden auf den validierten 500- und 300-km-Zweigen folgende differentielle Modellgrößen ausgewertet.

### 14.1 Relative Gravitation

| `r_c` | `max |Delta g/g|`, `r >= 100 km` | zentrale Größenordnung ab `r >= 10 km` |
|---:|---:|---:|
| 500 km | `≈ 1.8e-4` | `≈ 1.5e-3` |
| 300 km | `≈ 2.1e-4` | `≈ 1.6e-3` |

### 14.2 P-Wellen-Geschwindigkeit

```text
|Delta V_P/V_P| ~ 3e-6.
```

### 14.3 ICB-/CMB-Lage

| `r_c` | `Delta r_ICB` | `Delta r_CMB` |
|---:|---:|---:|
| 500 km | `-43.8 m` | `-35.0 m` |
| 300 km | `-61.1 m` | `-33.9 m` |

### 14.4 P-Wellen-Laufzeit

| `r_c` | `Delta T_P` |
|---:|---:|
| 500 km | `+0.0119 s` |
| 300 km | `+0.0088 s` |

### 14.5 Trägheitsmoment

Für die Materiekomponente liegt die differentielle Änderung ungefähr bei

```text
Delta I/I ~ -(7–8)e-6.
```

Diese Werte sind Modellvorhersagen des konkret angegebenen Zweigs und keine bereits gemessenen Anomalien.

## 15. Amplitudenscan bei `r_c = 300 km`

Die Sensitivität gegenüber größeren Randamplituden wurde zusätzlich geprüft:

| `q(r_a)` | `Delta r_ICB` | `Delta r_CMB` | `Delta T_P` |
|---:|---:|---:|---:|
| `1e-14` | `≈ -61 m` | `≈ -34 m` | `+0.0088 s` |
| `1e-13` | `≈ -604 m` | `≈ -339 m` | `≈ +0.095 s` |
| `3e-13` | `≈ -1.77 km` | `≈ -1.02 km` | nicht als konservativer Referenzwert promoted |

Der Scan dient der Sensitivitätsanalyse. Größere `q`-Werte werden dadurch nicht automatisch als physikalisch zulässige Erdparameter validiert.

## 16. Aktueller konservativer numerischer Status

Für den Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

gilt derzeit:

```text
r_c = 500 km -> voll gekoppelt validiert
r_c = 300 km -> voll gekoppelt + cross-solver-validiert
r_c = 250–275 km -> Kandidatenbereich, abhängig von Stage/Solver
r_c <= 200–250 km -> numerisch offen
```

Die 300-km-Grenze ist eine aktuelle numerische Validierungsfrontier der Implementierung und keine fundamentale physikalische Mindestreichweite.

## 17. Falsifikationsbedingungen

Eine konkrete Erd-SL/BH-Version muss mit **einem festen Parametersatz** gleichzeitig bestehen gegen:

1. Erdmasse und Radius,
2. normiertes Trägheitsmoment,
3. PREM-Seismologie und Normalmoden,
4. terrestrischen Wärmehaushalt,
5. geologisches Alter und Langzeitentwicklung,
6. physikalisch konsistente Formation,
7. Capture-/Akkretionsgeschichte,
8. robuste numerische Konvergenz,
9. mindestens eine unabhängige vorab definierte Beobachtungssignatur.

## 18. Offene Arbeit

Die nächsten wissenschaftlich relevanten Schritte sind:

- robuste BVP-/Multiple-Shooting-Fortsetzung unterhalb von 300 km,
- analytische oder sparse Jacobians,
- Mesh- und Richtungs-Konvergenz,
- fundamentale Hochdruck-Fe/Ni-EOS,
- explizite Near-Zone-Capture-/Akkretionsgleichungen,
- thermischer Transportabschluss,
- Formation Rule mit eigener Vorhersage,
- vollständiger Seismologie-/Normalmoden-Likelihood-Fit,
- vorregistrierte Messsignaturen und Vergleich mit realen Daten.

## 19. Aktuelle Schlussfolgerung

Seit dem früheren Stage-1.3C-Stand wurde der numerische Erdteil wesentlich erweitert. Der dokumentierte kleine redistributive Referenzzweig kann inzwischen bis `r_c = 300 km` voll gekoppelt und cross-solver-validiert verfolgt werden. Die GR-Baseline wurde durch die Layered-PREM-Closure auf ungefähr `1e-7` oder besser verbessert. Zusätzlich liegen differentielle Vorhersagen für Gravitation, P-Wellen-Geschwindigkeit, ICB/CMB-Lage, P-Wellen-Laufzeit und Trägheitsmoment vor.

Die wissenschaftlich zulässige Aussage lautet daher:

> Innerhalb der implementierten Gleichungen, Randbedingungen und Solverprüfungen wurde für den Referenzzweig `M_SL=1e16 kg`, `q(r_a)=1e-14` bis `r_c=300 km` kein interner ausschließender numerischer Widerspruch gefunden. Die Lösung ist auf dieser Stufe cross-solver-validiert und besitzt quantifizierte Erdobservablen. Ein direkter empirischer Nachweis eines Schwarzen Lochs im Erdzentrum liegt damit nicht vor.

Weitere Details und die historische Trennung der Teststufen stehen in [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) und [`TEST_STATUS.md`](TEST_STATUS.md).

## Primärreferenz

A. M. Dziewonski & D. L. Anderson (1981), *Preliminary Reference Earth Model*, Physics of the Earth and Planetary Interiors 25, 297–356. DOI: 10.1016/0031-9201(81)90046-7.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.2*, Theorie- und Forschungsentwurf, numerischer Entwicklungsstand Stage 1.7, Rheinland-Pfalz, Deutschland.
