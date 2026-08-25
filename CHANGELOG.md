# Changelog

Dieses Changelog dokumentiert die öffentlich sichtbaren Entwicklungsstände des Erdmoduls.

## V1.3 / Stage 3.14 — 25.08.2026

Größere Härtung des Akkretions-, Near-Zone- und Materialphysikblocks.

### Dokumentation

- `README.md`, `THEORIE.md`, `TEST_STATUS.md`, `NUMERIK_STATUS.md` und `CITATION.cff` auf V1.3 / Stage 3.14 aktualisiert.
- `AKKRETION_STATUS.md` ergänzt.
- Wissenschaftliche Aussagegrenzen deutlicher getrennt: Modellannahme, numerische Validierung, Sensitivität, Korrektur und empirischer Nachweis.

### Stage 1.8/1.9

- 1D P-/PKP-/PKIKP-Raytracing ergänzt.
- toroidale Normalmoden als vereinfachter FEM-Prototyp untersucht.
- kleine Modellverschiebungen werden nicht als Präzisionsnachweis promoted.

### Stage 2

- algebraische Stabilitätsfilter dokumentiert.
- Bondi-/Hawking-Benchmarks gehärtet.
- heutige galaktische PBH-Capture-Raten als Formationstest aufgenommen.
- vorgeschlagene Quantenunterdrückung nur als umstrittene Sensitivität geführt.

### Stage 3.2–3.6 – Mikroakkretion / Wärme

- direkte ballistische Capture-Proxies,
- Festkörperdiffusion und Creep,
- Knudsen-/Kontinuumschecks,
- Wärmeleitung und Melt-Front-Feedback,
- explizite lokale Thermalisierungsfraktion `f_th`.

Korrektur: Die einfache Aussage „lokale Wärme schmilzt automatisch bis zur Bondiskala und startet zwangsläufig Bondi“ ist zu stark.

### Stage 3.7 – Mathematik-/Literatur-Audit

- Bondi-Algebra und 4D-Koeffizient reproduziert.
- kein mathematischer Fehler in der klassischen Bondi-Formel gefunden.
- Hauptfrage ist die physikalische Anwendbarkeit auf kondensierte Erdmaterie.

### Stage 3.8/3.9 – nichtlineare Rheologie

- konstante Viskosität durch stressabhängige hcp-Fe-Potenzrheologie ersetzt.
- Cavity-/Yield-Grenztests ergänzt.
- Niedrig-Strain-Geoviskositäten werden nicht mehr unverändert in die SL-Nahzone extrapoliert.

### Stage 3.10/3.11 – Hochdruck-EOS

- PREM-/konstante-`Gamma`-Extrapolation durch Hochdruck-Fe-EOS-Sensitivitäten gehärtet.
- alte Stage-3.10-Capture-Grenze von ungefähr `54 r_s` als nicht EOS-robust erkannt und zurückgezogen.

### Stage 3.12 – relativistische Michel-Akkretion

Wichtige Korrektur: Das Fehlen eines Newtonschen Bondi-Kritikpunkts für `Gamma>5/3` bedeutet nicht, dass in voller GR keine kritische BH-Akkretion existiert.

Ein allgemeiner barotroper Michel-Solver wurde implementiert und gegen eine analytische `Gamma=2`-Lösung getestet:

```text
relative Mdot-Abweichung ~ 2e-14
```

Für `M_SL=1e16 kg` und eine phenomenologische condensed -> degenerierte-Elektronen-EOS ergibt der `Y_e`-Sensitivitätsbereich ungefähr

```text
Mdot_Michel ~ 147 ... 1460 kg/s.
```

Die Zeit bis `+1%` Masse liegt nur bei ungefähr

```text
~2.1e3 ... 2.1e4 yr.
```

Erforderliche Langzeitunterdrückung gegenüber Michel:

```text
~2e5 ... 2e6.
```

Unter Standard-Hawking + ununterdrückter Michel-Akkretion wurde in diesem Modell kein überlappendes geologisches Massenfenster gefunden.

### Stage 3.13 – Solid/Michel Interface

Eine reduzierte selbstkonsistente hcp-Fe-Solid->Michel-Kopplung bei Millimeterradien ergibt nahezu die volle Michel-Kapazität. Gewöhnlicher hcp-Fe-Creep liefert dort nicht die benötigte `1e5–1e6`-Unterdrückung.

Eine mikroskopische Sensitivität mit `8 GPa`-Stresscap zeigte zunächst mögliche starke geometrische Unterdrückung, wurde aber als materialphysikalisch nicht abgesichert markiert.

### Stage 3.14 – Coulomb-Plastizität

Die tiefe degenerierte Zone wurde auf Coulombkristall-Skalierungen und aktuelle Plastizitätsmodelle umgestellt.

Befunde:

- Michel-Kritikpunkte liegen im/nahe am untersuchten dimensionslosen Coulomb-Plastizitätsratenbereich.
- die reduzierte Michel-Druckabweichung übersteigt die verwendete Coulomb-Yield-Skala deutlich.
- ein rein elastischer Coulombkristall würde vorher yielden.
- plastisches Weiterfließen nach dem Yield ist ein relevanter Kandidat und keine automatische Akkretionsblockade.

Korrektur:

```text
Stage-3.13 8-GPa-Mikrorettung -> als physikalische Coulomb-Langzeitgrenze zurückgezogen.
```

### Aktuelle Konsequenz

Der `M_SL=1e16 kg`-Referenzzweig steht unter einem deutlich stärkeren Langzeit-Akkretionsdruck als im Stage-1.7-Repository-Stand. Eine belastbare Unterdrückung von `~1e5–1e6` gegenüber Michel ist bisher nicht nachgewiesen.

Der nächste prioritäre Test ist ein vollständiger Massenscan über mehrere Größenordnungen.

---

## V1.2 / Stage 1.7 — 25.08.2026

- Titel auf **SL/BH-Kernhypothese Erdmodul** vereinheitlicht.
- kleiner redistributiver SL/BH-Zweig als aktuelles Erd-Basismodell dokumentiert.
- Layered-PREM-Earth-Closure eingeführt.
- GR-Baseline auf ungefähr `Delta R/R ~4.17e-9`, `Delta M/M ~4.44e-8` verbessert.
- `r_c=500 km` und `r_c=300 km` voll gekoppelt validiert; 300 km cross-solver-validiert.
- Gravitation, P-Wellen-Proxies, ICB/CMB, Laufzeit und Trägheitsmoment als differentielle Modellgrößen dokumentiert.

## Früherer V1.2 / Stage 1.3C-Stand — 25.08.2026

Der erste öffentliche V1.2-Numerikstand dokumentierte eine Precision-Single-Shooting-Frontier bei `r_c=500 km` für `M_SL=1e16 kg`, `q0=1e-14`. Dieser Stand wurde durch spätere Stages überholt.

## V1.0 — 23.08.2026

Erstveröffentlichung des Erdmoduls.

- archivierte Veröffentlichungsfassung: `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf`,
- Integritätsnachweis über `SHA256SUMS.txt`,
- PDF bleibt unverändert als Archiv- und Prioritätsnachweis erhalten.

## Versionsprinzip

Archivierte Publikationsdateien werden nicht nachträglich überschrieben. Der aktuelle Forschungsstand wird in den Markdown-Dateien und `CITATION.cff` geführt.
