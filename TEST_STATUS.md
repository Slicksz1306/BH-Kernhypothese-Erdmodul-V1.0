# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 25.08.2026  
**Theorie-Textstand:** Erdmodul V1.3  
**Aktueller Forschungsstand:** Stage 3.14

## 1. Statusbegriffe

- **validiert** = der konkret benannte numerische Solver-/Konvergenztest erfüllt die festgelegten Kriterien.
- **Kandidat** = numerisch plausibel, aber nicht vollständig cross-solver-/mesh-bestätigt.
- **Sensitivität** = Parameter- oder Modellvergleich; keine empirische Grenze.
- **offen** = mit den vorhandenen Gleichungen/Daten noch nicht belastbar entschieden.
- **korrigiert/zurückgezogen** = ein früheres Zwischenresultat wurde durch einen härteren Test ersetzt.
- **empirisch bestätigt** = würde unabhängige Messdaten erfordern und ist derzeit nicht erreicht.

Keiner der hier dokumentierten Tests ist eine direkte Detektion eines Schwarzen Lochs im Erdzentrum.

## 2. Referenzzweig

Der am weitesten ausgearbeitete Testzweig verwendet

```text
M_SL = 1e16 kg
q(r_a) = 1e-14
```

mit redistributiver Zentralmasse:

```text
M_PREM(<r_rep) = M_SL.
```

## 3. Struktur- und Earth-Matching-Block

### Stage 1.5D – BH-konsistente Fortsetzung

| `r_c` | Status |
|---:|---|
| 500 km | validiert |
| 300 km | validiert |
| 275 km | Kandidat |
| 250–100 km | offen |

### Stage 1.6 – Layered-PREM-Closure

GR-Baseline:

```text
Delta R/R ~ 4.17e-9
Delta M/M ~ 4.44e-8
```

Voll gekoppelte Referenzpunkte:

| `r_c` | `Delta M/M` gegen GR | Status |
|---:|---:|---|
| 500 km | `~ -9.2e-6` | validiert |
| 300 km | `~ -8.65e-6` | cross-solver-validiert |
| 250 km | — | Kandidat |
| 200 km | — | offen |

Die 300-km-Grenze ist eine Solverfrontier, keine physikalische Mindestreichweite.

### Stage 1.7 – Erdobservablen

Für den Referenzzweig wurden als differentielle Modellgrößen unter anderem berechnet:

```text
max |Delta g/g| (r >=100 km): ~1.8e-4 ... 2.1e-4
|Delta Vp/Vp|:                 ~3e-6
Delta r_ICB:                   ~ -44 ... -61 m
Delta r_CMB:                   ~ -35 ... -34 m
Delta T_P:                     ~ +0.009 ... +0.012 s
Delta I/I:                     ~ -(7...8)e-6
```

Diese Werte sind Sensitivitäten des angegebenen Modells, keine beobachteten Anomalien.

### Stage 1.8/1.9 – Seismologie-/Normalmoden-Proxies

- 1D P-/PKP-/PKIKP-Raytracing implementiert.
- Für `q=1e-14` liegen typische gleiche-Distanz-Laufzeitverschiebungen im Millisekundenbereich.
- Toroidale Normalmoden wurden mit einem vereinfachten SNREI-artigen FEM-Prototyp untersucht.
- Absolute Moden besitzen in der vereinfachten Closure ungefähr Prozent-Bias; kleine SL-GR-Frequenzverschiebungen sind nicht als Präzisionsnachweis promoted.

## 4. Stabilität, Langzeit und Formation

### Stage 2.0 – algebraische Stabilitätsfilter

Für die getesteten kleinen `q`-Zweige bleiben

```text
F > 0
D = F + 3/2 F_chi^2 > 0.
```

Damit wurde kein elementarer negativer effektiver Planck-Massen-/Ghost-Filter verletzt. Eine vollständige dynamische Stabilitätsanalyse ist nicht abgeschlossen.

### Stage 2.1–2.5 – Bondi/Hawking Benchmarks

Für `M_SL=1e16 kg` liefert die unmodifizierte kanonische Bondi-Referenz grob

```text
Mdot_Bondi ~ 1.28e4 kg/s
```

und wäre geologisch viel zu schnell.

Ein einfacher Standard-Hawking-Lebensdauerbenchmark ergibt eine Erdalter-Untergrenze in der Größenordnung

```text
M_Hawking,min ~ 1.19e11 kg.
```

### Stage 2.6/2.7 – vorgeschlagene Quantenunterdrückung

Eine vorgeschlagene quantenmechanische Capture-Unterdrückung wurde als Sensitivität geprüft, ist in der Literatur jedoch umstritten. Sie wird **nicht** als gelöster Langzeitmechanismus verwendet.

### Stage 2.9 – Formation/Capture

Einfache heutige galaktische PBH-Einfangraten sind für den Referenzfall extrem klein. Ein gewöhnlicher heutiger Capture-Ursprung ist daher stark unplausibel; frühe primordial gebundene Entstehung bleibt als offene Formation Rule getrennt.

## 5. Mikroakkretion und Wärme

### Stage 3.2–3.5

Getestet wurden als Grenzregime:

- direkte ballistische Capture-Proxies,
- Knudsen-/Kontinuumschecks,
- Festkörperdiffusion,
- Creep-Supply,
- Wärmeleitung,
- Melt-Front-/Stefan-Proxies.

Ergebnis: **„lokale Wärme schmilzt zwangsläufig alles und startet automatisch Bondi“ ist zu stark.** Ob eine Fluidzone entsteht, hängt von Transport, lokaler Thermalisierung, Rheologie und Phasenfeedback ab.

### Stage 3.6 – korrigierter Zwei-Phasen-Proxy

Stage 3.5 hatte implizit volle lokale Energiedeponierung in der Melt-Radius-Abschätzung verwendet. Stage 3.6 führte explizit

```text
P_local = f_th * Mdot * c_s^2
```

ein.

Für einen repräsentativen Fall `eta=1e14 Pa s`, `k=100 W/m/K`, `DeltaT=500 K` liegt die Melt-to-rB-Schwelle eher bei mehreren Prozent lokaler Kopplung als bei ~1%.

## 6. Literatur-/Rheologie-Audit

### Stage 3.7

- Die klassische Bondi-Algebra und der 4D-Koeffizient wurden reproduziert.
- Kein mathematischer Fehler in der Bondi-Formel gefunden.
- Hauptproblem ist die **Anwendbarkeit** auf kondensierte Erdmaterie.

### Stage 3.8/3.9

- konstante Viskosität durch stressabhängige hcp-Fe-Potenzrheologie ersetzt,
- starke Deformationsraten nahe der SL-Nahzone zeigen, dass langsame geophysikalische Viskositäten nicht direkt extrapoliert werden dürfen,
- ideal-plastische Cavity-Grenztests zeigen Übergänge im GPa-Festigkeitsbereich.

## 7. Hochdruck-EOS und relativistische Akkretion

### Stage 3.10

Ein PREM-basierter lokaler Stiffness-Check ergab `Gamma_eff` im Kern grob deutlich über `5/3`. Eine konstante `Gamma~4`-Extrapolation wurde als Toy-Modell geprüft.

**Korrektur:** Die daraus abgeleitete alte Capture-Grenze um `~54 r_s` ist nicht robust und wurde später zurückgezogen.

### Stage 3.11

Smith-/Hakim-basierte Hochdruck-Fe-EOS wurden bis in den TPa-Bereich als gehärtete äußere Near-Zone verwendet. Ergebnis:

- gemessene/DFT-gestützte Fe-EOS reicht wesentlich weiter als PREM,
- der eigentliche mikroskopische Capture-/Sonic-Bereich liegt aber noch tiefer,
- konstantes `Gamma~4` darf nicht bis zum Horizont extrapoliert werden.

### Stage 3.12 – relativistische Michel-Akkretion

Wichtige Korrektur: Für steife kausale EOS kann die volle GR-Michel-Lösung einen regulären kritischen Akkretionszweig besitzen, auch wenn die Newtonsche Bondi-Topologie für `Gamma>5/3` versagt.

Der allgemeine barotrope Michel-Solver reproduziert den analytischen `Gamma=2`-Test mit relativer Mdot-Abweichung von ungefähr `2e-14`.

Mit einer phenomenologischen condensed-matter -> degenerierte-Elektronen-EOS wurden für `M_SL=1e16 kg` über einen `Y_e`-Sensitivitätsbereich ungefähr

```text
Mdot_Michel ~ 147 ... 1460 kg/s
```

erhalten.

Die Zeit bis `+1%` Masse liegt dann nur bei ungefähr

```text
~2.1e3 ... 2.1e4 yr.
```

Für weniger als `1%` Wachstum über `4.54 Gyr` ist eine Unterdrückung gegenüber Michel von ungefähr

```text
~2e5 ... 2e6
```

erforderlich.

### Stage 3.12 Hawking/Michel-Massenfenster

Unter Standard-Hawking + **ununterdrückter** Stage-3.12-Michel-Akkretion ergibt sich in diesem Modell kein Langzeit-Überlappungsfenster:

```text
Michel <1%-Massenobergrenze ~4.8e9 ... 4.8e10 kg
Hawking-Erdatler-Untergrenze ~1.19e11 kg
```

Das ist ein **starker negativer Modellbefund**.

## 8. Festkörper-/Plasma-Kopplung

### Stage 3.13

Eine reduzierte selbstkonsistente hcp-Fe-Solid->Michel-Interface-Kopplung bei Millimeterradien ergab nahezu die volle Michel-Kapazität bei subprozentigen Druckabweichungen. Damit liefert gewöhnliche hcp-Fe-Rheologie dort nicht die benötigte `1e5–1e6`-Unterdrückung.

Eine scheinbare Rettung bei einem mikroskopischen Interface mit einem `8 GPa`-Stresscap wurde als Sensitivität gefunden, aber ausdrücklich als materialphysikalisch unsicher markiert.

### Stage 3.14 – Coulomb-Plastizität

Die tiefe Materie wurde auf Coulombkristall-Skalierungen umgestellt. Ergebnis:

- die Stage-3.12-Michel-Kritikpunkte liegen im oder nahe am untersuchten dimensionslosen Coulomb-Plastizitätsratenbereich,
- die reduzierte Michel-Druckabweichung liegt deutlich über der verwendeten Coulomb-Yield-Skala,
- ein rein elastischer Coulombkristall würde yielden,
- aktuelle Plastizitätsresultate sprechen nach Yield eher für fortgesetzten plastischen Fluss als für eine dauerhaft blockierende starre Phase.

**Korrektur:** Die Stage-3.13-`8 GPa`-Mikrorettung wird als physikalische Langzeitgrenze zurückgezogen, weil dieser hcp-Fe-Stresscap im Coulomb-Regime nicht übertragbar ist.

## 9. Aktuelle Statusmatrix

| Bereich | Status |
|---|---|
| starke Erd-SL-Variante | mit Erdstruktur unvereinbar |
| kleiner redistributiver Earth-Matching-Zweig | numerisch bis 300 km gehärtet |
| Seismologie/Normalmoden | Sensitivitäten, kein empirischer Nachweis |
| Standard-Bondi direkt auf festen Kern | nicht automatisch gerechtfertigt |
| relativistische Michel-Akkretion | starker negativer Test für `1e16 kg` |
| hcp-Fe-Solid-Suppression | bei mm-Skalen nicht ausreichend im reduzierten Modell |
| Coulomb-Solid-Suppression | einfache Blockade derzeit nicht nachgewiesen |
| Formation | offen / gewöhnlicher heutiger Capture stark unplausibel |
| empirische Detektion | keine |

## 10. Nächster harter Test

Der nächste prioritäre Schritt ist ein **Massenscan** mit demselben physikalischen Stack:

```text
M_SL ~ 1e8 ... 1e16 kg
```

gegen

- Standard-Hawking,
- relativistische Michel-Akkretion,
- Coulomb-/Plasma-Transport,
- Earth-age-Wachstum,
- strukturelle Earth-Matching-Grenzen.

Ziel ist nicht, einen bevorzugten Massenpunkt zu retten, sondern zu bestimmen, ob überhaupt ein konsistentes Erd-SL-Massenfenster verbleibt.

## 11. Aussagegrenze

Der aktuelle Stand zeigt einen weit ausgearbeiteten, falsifizierbaren theoretischen Erd-SL-Rahmen mit bestandenen numerischen Teiltests und gleichzeitig einem starken offenen/negativen Akkretionsblock.

Er erlaubt **nicht** die Aussage, dass ein Schwarzes Loch im Erdzentrum experimentell nachgewiesen oder die Hypothese als etablierte physikalische Theorie bestätigt wurde.
