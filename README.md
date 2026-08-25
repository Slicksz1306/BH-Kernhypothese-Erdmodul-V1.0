# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.3  
**Aktueller Forschungsstand:** Stage 3.15  
**Stand:** 25.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Archivhinweis:** `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs- und Prioritätsnachweis erhalten. Die aktuelle Weiterentwicklung wird in den Markdown-Dateien dokumentiert.

## Wissenschaftlicher Status

Die **SL/BH-Kernhypothese Erdmodul** ist ein theoretisches Forschungsmodell. `SL` bezeichnet ein **Schwarzes Loch**.

Die definierende Annahme lautet: Im Erdzentrum wird ein kleines zentrales Schwarzes Loch als redistributive Zentralmasse modelliert. Seine Masse wird im Basismodell nicht zusätzlich zur Erdmasse addiert, sondern ersetzt dieselbe PREM-Masse im Zentralbereich.

Es wird **keine direkte Detektion eines Schwarzen Lochs im Erdzentrum behauptet**. Numerisch bestandene Solver-, Matching- oder Cross-Solver-Tests sind keine empirischen Nachweise.

## Aktueller Kernstatus

Die starke Variante, in der ein zentrales Schwarzes Loch einen wesentlichen Anteil der Erdmasse oder Erdgravitation trägt, ist mit der beobachteten Erdstruktur nicht vereinbar. Ein wesentlich kleineres zentrales Schwarzes Loch wird dadurch nicht grundsätzlich ausgeschlossen.

Für das lange verwendete Referenzmodell `M_SL=1e16 kg` ist die relativistische Langzeitakkretion derzeit der stärkste negative Test. Stage 3.15 zeigt jedoch, dass die gesamte Erd-SL-Massenachse nicht durch diesen einen Referenzpunkt entschieden ist.

## Redistributive Massenbuchhaltung

```text
M_PREM(<r_rep) = M_SL
```

Im ideal kugelsymmetrischen Grenzfall gilt außerhalb der Ersatzregion

```text
M_model(<r) = M_PREM(<r),   r >= r_rep.
```

Damit werden SL-Masse und gewöhnliche Materie nicht doppelt gezählt.

## Feldtheoretischer Minimalrahmen

Der sphärische Jordan-Frame-Minimalstack verwendet

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4.
```

Der GR-Grenzfall muss für `xi -> 0`, `chi -> 0`, `dchi/dr -> 0` auf die gewöhnliche TOV-Struktur zurückfallen. Ein reales zentrales Schwarzes Loch wird über eine Horizon-/Matching-Randbedingung und nicht als reguläres TOV-Zentrum behandelt.

## Earth-Matching

Für den Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

sind `r_c=500 km` und `r_c=300 km` mit der gehärteten Layered-PREM-Closure voll gekoppelt numerisch validiert; der 300-km-Punkt ist cross-solver-validiert. Die GR-Baseline reproduziert ungefähr

```text
Delta R/R ~ 4.17e-9
Delta M/M ~ 4.44e-8.
```

Seismologische Laufzeiten, ICB/CMB-Verschiebungen, Gravitation, Trägheitsmoment und prototypische Normalmoden wurden als Modellsensitivitäten untersucht. Sie sind keine gemessenen SL-Signaturen.

## Akkretionsblock bis Stage 3.14

Die klassische Bondi-Algebra wurde reproduziert; kein mathematischer Fehler in der Formel wurde gefunden. Die entscheidende Frage ist ihre physikalische Anwendbarkeit auf kondensierte, plastische und degenerierte Erdmaterie.

Härtere Tests führten zu mehreren Korrekturen:

- „lokale Wärme schmilzt zwangsläufig alles bis zur Bondiskala“ ist zu stark,
- die frühere `~54 r_s`-Grenze aus einem konstanten `Gamma~4`-Toymodell ist nicht EOS-robust,
- die Stage-3.13-`8 GPa`-Mikrorettung ist nicht auf tiefe Coulombmaterie übertragbar.

Der relativistische Michel-Test mit einer phenomenologischen condensed-to-degenerate EOS ergibt für `M_SL=1e16 kg` ungefähr

```text
Mdot_Michel ~ 147 ... 1460 kg/s,
```

während die mittlere Rate für `+1%` Masse über 4.54 Gyr nur ungefähr `6.98e-4 kg/s` beträgt. Ein gewöhnlicher hcp-Fe-Festkörper bei Millimeterradien liefert im reduzierten Modell keine ausreichende Unterdrückung; auch eine generische Coulomb-Festkörperblockade ist durch die getestete Plastizitätsphysik nicht nachgewiesen.

## Stage 3.15 – vollständiger Massenscan und wichtige Korrektur

Stage 3.12 hatte Hawking und Michel als **getrennte** Langzeitgrenzen verglichen. Stage 3.15 löst beide Beiträge gleichzeitig:

```text
dM/dt = k_Michel M^2 - A_H/M^2.
```

Damit existiert im reduzierten Modell ein instabiles Gleichgewicht

```text
M_eq = (A_H/k_Michel)^(1/4)
```

bei ungefähr

```text
M_eq ~ 1.28e11 ... 2.28e11 kg
```

für den Stage-3.12-`Y_e`-Sensitivitätsbereich.

Die frühere starke Aussage

```text
"Standard-Hawking + ununterdrückte Michel-Akkretion -> kein gemeinsames Langzeitfenster"
```

wird daher **korrigiert**: Bei gleichzeitiger Massenentwicklung existiert ein Hawking/Michel-Kompensationsband.

Das Gleichgewicht ist instabil, aber die lineare e-Faltungszeit liegt ungefähr bei `4.2e9 ... 2.4e10 Jahren`. Für weniger als `1%` Netto-Massenänderung über 4.54 Gyr beträgt das Anfangsmassenband je nach `Y_e` ungefähr `-0.5/+0.5%` bis `-4.4/+5.1%` um `M_eq`.

### Warum das noch keine Lösung ist

Der PREM-Ersatzradius dieses neuen Massenbands beträgt nur ungefähr `133 ... 161 m`. In diesem kleinen `M_SL`-/sub-km-Bereich ist das voll gekoppelte Earth Matching noch nicht cross-solver-validiert.

Außerdem skaliert die dimensionslose Michel-Deformationsrate am Kritikpunkt ungefähr wie `1/M`. Das neue `~1e11 kg`-Band liegt um etwa `4e3 ... 5e4` unter den Massengrenzen, für die die Stage-3.14-Coulomb-Plastizitätsdaten direkt im kalibrierten MD-Ratenbereich liegen. Die Materialtransportphysik ist dort deshalb erneut offen.

Details: [`MASSENSCAN_STAGE3_15.md`](MASSENSCAN_STAGE3_15.md).

## Aktueller konservativer Status

```text
M_SL ~ 1e16 kg:
    stark durch relativistische Langzeitakkretion belastet

M_SL ~ 1e11 kg:
    neues Hawking/Michel-Kandidatenband im reduzierten ODE,
    aber Earth Matching und Materialtransport noch nicht validiert
```

Damit ist weder ein Erd-SL nachgewiesen noch die gesamte kleine Erd-SL-Hypothese ausgeschlossen.

## Nächste harte Tests

1. voll gekoppeltes Earth Matching im neuen `~1e11 kg`-Band,
2. Near-Zone-Transport bei dimensionslosen Raten außerhalb der Stage-3.14-MD-Kalibrierung,
3. Hawking-Greybody-/Teilchenspezies-, Spin- und Ladungssensitivität,
4. Formation Rule für das niedrige Massenband,
5. reale Seismologie-/Normalmoden-Likelihood und vorab definierte Detektionssignaturen.

## Dateien

- [`THEORIE.md`](THEORIE.md) – Theorierahmen.
- [`TEST_STATUS.md`](TEST_STATUS.md) – Test- und Validierungsmatrix.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) – numerischer Entwicklungsstand.
- [`AKKRETION_STATUS.md`](AKKRETION_STATUS.md) – Akkretions-/Langzeitstatus.
- [`MASSENSCAN_STAGE3_15.md`](MASSENSCAN_STAGE3_15.md) – aktueller Hawking/Michel-Massenscan.
- [`CHANGELOG.md`](CHANGELOG.md) – Versions- und Korrekturhistorie.
- [`CITATION.cff`](CITATION.cff) – Zitiermetadaten.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` – unveränderte Erstveröffentlichung.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.3*, theoretischer Forschungsentwurf, aktueller Entwicklungsstand Stage 3.15, Rheinland-Pfalz, Deutschland.
