# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.3  
**Aktueller Forschungsstand:** Stage 3.14  
**Stand:** 25.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Archivhinweis:** `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs- und Prioritätsnachweis erhalten. Die aktuelle Weiterentwicklung wird in den Markdown-Dateien dokumentiert.

## Wissenschaftlicher Status

Die **SL/BH-Kernhypothese Erdmodul** ist ein theoretisches Forschungsmodell. `SL` bezeichnet ein **Schwarzes Loch**.

Die definierende Annahme lautet: Im Erdzentrum wird ein kleines zentrales Schwarzes Loch als redistributive Zentralmasse modelliert. Seine Masse wird im Basismodell nicht zusätzlich zur Erdmasse addiert, sondern ersetzt dieselbe PREM-Masse im Zentralbereich.

Es wird **keine direkte Detektion eines Schwarzen Lochs im Erdzentrum behauptet**. Numerisch bestandene Solver-, Matching- oder Cross-Solver-Tests sind keine empirischen Nachweise.

## Aktueller Kernstatus in einem Satz

Die starke Variante, in der ein zentrales Schwarzes Loch einen wesentlichen Anteil der Erdmasse oder Erdgravitation trägt, ist mit der beobachteten Erdstruktur nicht vereinbar. Ein wesentlich kleineres zentrales Schwarzes Loch wird dadurch nicht grundsätzlich ausgeschlossen. Der derzeit härteste offene beziehungsweise belastende Block ist die **Langzeitakkretion**.

## Redistributive Massenbuchhaltung

Für eine gewählte SL-Masse `M_SL` wird der strukturelle Ersatzradius `r_rep` definiert durch

```text
M_PREM(<r_rep) = M_SL.
```

Im ideal kugelsymmetrischen Grenzfall bleibt außerhalb der Ersatzregion die eingeschlossene Masse erhalten:

```text
M_model(<r) = M_PREM(<r),   r >= r_rep.
```

Damit werden SL-Masse und gewöhnliche Materie nicht doppelt gezählt.

## Drei getrennte Radien

```text
Schwarzschildradius:        r_s   = 2 G M_SL / c^2
Akkretions-/Bondiskala:     r_B   = G M_SL / c_eff^2
Struktureller Ersatzradius: M_PREM(<r_rep) = M_SL
```

`r_s`, `r_B` und `r_rep` sind physikalisch unterschiedliche Größen.

## Feldtheoretischer Minimalrahmen

Der aktuelle sphärische Jordan-Frame-Minimalstack verwendet

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4
```

mit gekoppelten Metrik-, Druck-, Massen- und Skalarfeldgleichungen. Der Grenzfall

```text
xi -> 0, chi -> 0, dchi/dr -> 0
```

muss auf die gewöhnliche GR-TOV-Struktur zurückfallen.

Der zentrale SL wird über eine **Horizon-/Matching-Randbedingung** behandelt; ein reales Schwarzes Loch ist kein reguläres TOV-Zentrum.

## Earth-Matching und geophysikalischer Stand

Für den am weitesten untersuchten Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

wurden mit der Layered-PREM-Closure voll gekoppelte Earth-Matching-Lösungen bei `r_c=500 km` und `r_c=300 km` cross-solver-validiert. `250–275 km` bleibt Kandidatenbereich; kleinere Reichweiten sind numerisch nicht als voll gekoppelte Lösungen promoted.

Die GR-Baseline der gehärteten Closure reproduziert ungefähr

```text
Delta R/R ~ 4.17e-9
Delta M/M ~ 4.44e-8.
```

Abgeleitete Sensitivitäten des Referenzzweigs umfassen unter anderem:

- relative Gravitation außerhalb der zentralen Zone,
- PREM-nahe Dichte-/Geschwindigkeitsproxies,
- ICB-/CMB-Verschiebungen,
- P-/PKP-/PKIKP-Laufzeitänderungen,
- Materie-Trägheitsmoment,
- prototypische Normalmoden.

Diese Größen sind **Modellvorhersagen und Sensitivitäten**, keine gemessenen SL-Signaturen.

## Akkretions- und Langzeitblock — Stage 2 bis 3.14

Der Akkretionsblock wurde wesentlich über die frühere einfache Bondi-Abschätzung hinaus erweitert.

### Was bestehen blieb

Die klassische Bondi-Formel ist mathematisch korrekt innerhalb ihrer Fluid-/EOS-Annahmen. Eine direkte Anwendung auf festen Erdkernstoff ist jedoch eine physikalische Modellannahme und keine algebraische Notwendigkeit.

### Was korrigiert wurde

Mehrere frühere Zwischenresultate wurden nach härteren Tests ausdrücklich zurückgezogen oder eingeengt:

- Die alte Aussage, lokale Wärme müsse automatisch alles bis zur Bondiskala schmelzen, war zu stark.
- Die frühere Stage-3.10-Grenze von ungefähr `54 r_s` war ein Artefakt einer konstanten `Gamma~4`-Extrapolation und ist **keine robuste physikalische Grenze**.
- Die Stage-3.13-`8 GPa`-Mikrorettung kann nicht in das tiefe Coulomb-Regime übertragen werden und ist als physischer Rettungsmechanismus **zurückgezogen**.

### Relativistische Michel-Akkretion — Stage 3.12

Der volle GR-Test zeigt, dass für steife kausale EOS relativistische Michel-Kritikpunkte existieren können, auch wenn die Newtonsche Bondi-Topologie für `Gamma>5/3` versagt.

Mit einer phenomenologischen condensed-matter -> degenerierte-Elektronen-EOS ergaben sich für `M_SL=1e16 kg` je nach effektiver Elektronenfraktion ungefähr

```text
Mdot_Michel ~ 1.5e2 ... 1.5e3 kg/s.
```

Die mittlere Rate für nur `+1%` Masse über 4.54 Gyr liegt dagegen bei ungefähr

```text
Mdot_1% ~ 6.98e-4 kg/s.
```

Damit benötigt der `1e16 kg`-Referenzzweig in diesem Modell eine Unterdrückung von ungefähr

```text
~2e5 ... 2e6
```

gegenüber der ununterdrückten Michel-Rate.

### Solid/Michel-Kopplung — Stage 3.13

Eine selbstkonsistente reduzierte hcp-Fe-Solid/Michel-Kopplung bei Millimeterradien ergab nahezu die volle Michel-Rate. Ein gewöhnlicher fester hcp-Fe-Bereich liefert in diesem Modell daher **nicht automatisch** die benötigte Unterdrückung.

### Coulomb-Plastizität — Stage 3.14

Für die tiefe, degenerierte Materie ist gewöhnliche hcp-Fe-Rheologie nicht mehr die passende Beschreibung. Der Test wurde daher auf Coulombkristall-Skalierungen und aktuelle Plastizitätsresultate umgestellt.

Der reduzierte Vergleich zeigt:

- die Michel-Kritikpunkte liegen im oder nahe am untersuchten dimensionslosen Coulomb-Plastizitätsbereich,
- die Michel-Druckabweichung übersteigt die verwendete Coulomb-Yield-Skala deutlich,
- ein rein elastischer Coulombkristall würde daher vor Erreichen des Michel-Zustands yielden,
- aktuelle Plastizitätsmodelle sprechen eher für plastisches Weiterfließen nach dem Yield als für einen dauerhaft blockierenden Hochviskositätszustand.

Damit ist die einfache Rettung

```text
"Festkörper -> kein Nachschub"
```

für `M_SL=1e16 kg` derzeit **nicht nachgewiesen**.

## Hawking + Michel

Im Stage-3.12-Sensitivitätsmodell liegen die geologischen Michel-Massenobergrenzen grob bei

```text
~4.8e9 ... 4.8e10 kg,
```

während der einfache Standard-Hawking-Erdalter-Benchmark eine Überlebensuntergrenze von ungefähr

```text
~1.19e11 kg
```

ergibt.

Damit existiert in **diesem konkreten Modell** kein überlappendes Langzeitfenster für Standard-Hawking plus ununterdrückte Michel-Akkretion. Das ist ein starker negativer Befund, aber noch kein empirischer Ausschluss der gesamten SL-Kernhypothese, weil die reale nichtstationäre Fest-/Plasma-/Kompositionskopplung noch nicht vollständig gelöst ist.

## Was als Nächstes entschieden werden muss

Die derzeit wichtigsten offenen Tests sind:

1. vollständiger Massenscan über mehrere Größenordnungen von `M_SL`,
2. gekoppelte relativistische Festkörper-/Plasma-/Thermaltransportgleichungen,
3. realistische Elektroneneinfang-/Kompositionsentwicklung in der tiefen Near Zone,
4. robuste Formation Rule,
5. reale Seismologie-/Normalmoden-Likelihood statt Sensitivitätsproxies,
6. unabhängige vorab definierte Detektionssignaturen.

## Falsifikationsprinzip

Eine konkrete Parameterwahl muss mit **demselben Parametersatz** gleichzeitig gegen Erdmasse, Radius, Trägheitsmoment, Seismologie, Normalmoden, Wärmehaushalt, Langzeitstabilität, Formation, Akkretion und numerische Konvergenz bestehen.

Wenn ein harter Test einen Zweig ausschließt, wird dieser Zweig nicht durch nachträgliches Umdeuten als bestanden markiert.

## Dateien

- [`THEORIE.md`](THEORIE.md) – aktueller Erdmodul-Theoriestand V1.3.
- [`TEST_STATUS.md`](TEST_STATUS.md) – aktuelle Test- und Validierungsmatrix bis Stage 3.14.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) – numerischer und physikalischer Entwicklungsstand.
- [`AKKRETION_STATUS.md`](AKKRETION_STATUS.md) – detaillierter Akkretions-/Langzeitstatus Stage 2 bis 3.14.
- [`CHANGELOG.md`](CHANGELOG.md) – Versions- und Korrekturhistorie.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) – Anforderungen für Review und Reproduktion.
- [`CITATION.cff`](CITATION.cff) – Zitiermetadaten.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` – unveränderte Erstveröffentlichung.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.3*, theoretischer Forschungsentwurf, aktueller Entwicklungsstand Stage 3.14, Rheinland-Pfalz, Deutschland.
