# Numerischer und physikalischer Status – SL-TOV / Earth Matching / Akkretion

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 25.08.2026  
**Theorie-Textstand:** V1.3  
**Aktuelle Stufe:** Stage 3.14

## 1. Bedeutung von „validiert“

**Numerisch validiert** bedeutet ausschließlich, dass der konkret angegebene Solver- oder Konvergenztest innerhalb der implementierten Gleichungen, Randbedingungen, EOS/Closure und Toleranzen bestanden wurde.

Es bedeutet nicht „experimentell bestätigt“ und nicht „Schwarzes Loch im Erdzentrum nachgewiesen“.

## 2. Feldgleichungs-/Earth-Matching-Kern

Der sphärische Minimalstack verwendet im Jordan Frame

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4
```

mit gekoppelten Gleichungen für Metrik, Masse, Druck und Skalarfeld.

Der GR-Grenzfall

```text
xi -> 0
chi -> 0
dchi/dr -> 0
```

muss die gewöhnliche GR-TOV-Struktur reproduzieren.

Das zentrale SL wird nicht als reguläres Zentrum behandelt. Die numerische Außenlösung beginnt an einem Matching-Radius `r_a > r_h`.

## 3. Earth-Matching Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

### Stage 1.5D

```text
500 km -> validiert
300 km -> validiert
275 km -> Kandidat
250 km und kleiner -> offen
```

### Stage 1.6 Layered-PREM-EOS

GR-Baseline:

```text
Delta R/R ~ 4.17e-9
Delta M/M ~ 4.44e-8
```

Cross-Solver:

```text
r_c=500 km -> Delta M/M ~ -9.2e-6, validiert
r_c=300 km -> Delta M/M ~ -8.65e-6, validiert
r_c=250 km -> Kandidat
r_c=200 km -> offen
```

## 4. Struktur-/Observablenblock

Auf den validierten 500-/300-km-Zweigen wurden Stage-1.7-Observablen berechnet. Größenordnungen:

```text
max |Delta g/g|, r>=100 km ~ 1.8e-4 ... 2.1e-4
|Delta Vp/Vp|              ~ 3e-6
Delta r_ICB                ~ -44 ... -61 m
Delta r_CMB                ~ -35 ... -34 m
Delta T_P                  ~ +0.009 ... +0.012 s
Delta I/I                  ~ -(7...8)e-6
```

Stage 1.8/1.9 ergänzen 1D P-/PKP-/PKIKP-Raytracing und toroidale Normalmodenproxies. Diese Blöcke sind Sensitivitätsrechnungen und noch kein Real-Data-Likelihood-Fit.

## 5. Horizon- und Nahzonen-Härtung

Ab Stage 1.5 wurde die Randbehandlung explizit BH-konsistent gehärtet. Ein reales SL besitzt einen Horizont; die unmittelbare Nahzone darf nicht durch eine reguläre Zentrumslösung ersetzt werden.

Für kleine `M_SL` sind die linearen Eigenwertverschiebungen zwischen regulärem Zentrum und BH-Robin-Randbedingung zwar klein, die physikalisch korrekte Randbedingung bleibt dennoch der BH-Horizont-/Near-Zone-Zweig.

## 6. Langzeit-/Akkretionsstack

### Kanonische Bondi-Referenz

Für den Erdkern-Referenzzustand und `M_SL=1e16 kg`:

```text
Mdot_Bondi ~ 1.28e4 kg/s
```

Die Formel ist algebraisch reproduziert. Ihre direkte Anwendung auf festen Erdkernstoff ist jedoch eine physikalische Modellannahme.

### Ballistik / Diffusion / Creep / Wärme

Stages 3.2–3.6 testeten Grenzregime für

- direkte Teilchencapture,
- Festkörperdiffusion,
- nichtlinearen Creep,
- Wärmeleitung,
- lokale Thermalisierung,
- Melt-Front-Feedback.

Diese Rechnungen zeigten, dass „Wärme -> sofort vollständige Schmelze -> automatisch Bondi“ keine zwingende Ein-Schritt-Folge ist.

## 7. Rheologie-Härtung

Stage 3.8 ersetzt konstante Viskosität durch eine stressabhängige hcp-Fe-Potenzrheologie. Die entscheidende Erkenntnis ist, dass geophysikalische Niedrig-Strain-Viskositäten nicht unverändert in die SL-Nahzone extrapoliert werden dürfen.

Stage 3.9 ergänzt ideal-plastische Cavity-Grenztests.

## 8. Hochdruck-EOS

Stage 3.10/3.11 ersetzten einfache PREM-/konstante-`Gamma`-Extrapolationen schrittweise durch Hochdruck-Fe-EOS-Sensitivitäten.

Wichtige Korrektur:

```text
alte ~54 r_s Capture-Grenze -> nicht EOS-robust, zurückgezogen
```

Die tatsächliche Nahzonen-EOS ändert sich über kondensierte, ionisierte und degenerierte Materieregime und kann nicht durch ein einziges konstantes `Gamma` beschrieben werden.

## 9. Relativistischer Michel-Solver – Stage 3.12

Für stationäre kugelsymmetrische GR-Akkretion wurde die Michel-Kritikpunktstruktur implementiert.

Der allgemeine barotrope Solver wurde gegen eine analytische `Gamma=2`-Lösung getestet:

```text
relative Mdot-Abweichung ~ 2e-14
```

Mit einer phenomenologischen condensed -> degenerierte-Elektronen-EOS und `Y_e`-Sensitivität ergibt sich für `M_SL=1e16 kg`:

```text
Mdot_Michel ~ 147 ... 1460 kg/s
```

Daraus folgen bei `Mdot ~ M^2` ungefähr:

```text
t(+1%) ~ 2.1e3 ... 2.1e4 yr
```

gegenüber 4.54 Gyr Erdalter.

Erforderliche mittlere Langzeitunterdrückung:

```text
~2e5 ... 2e6
```

## 10. Solid -> Michel Interface – Stage 3.13

Eine reduzierte serielle Kopplung wurde konstruiert:

```text
Mdot_solid(Delta P) = Mdot_Michel(P_inner)
```

Bei der durch die 5-TPa-Fe-Schmelz-/EOS-Sensitivität markierten Millimeterzone konvergieren die Gleichgewichte nahezu auf die ununterdrückte Michel-Kapazität.

Damit ist hcp-Fe-Creep auf dieser Skala kein ausreichender `10^5–10^6`-Limiter im reduzierten Modell.

## 11. Coulomb-Plastizität – Stage 3.14

Die tiefe degenerierte Zone wird nicht mehr mit einem hcp-Fe-`8 GPa`-Cap behandelt.

Getestet wurden Coulombkristall-Skalierungen, Bruchkinetik und aktuelle Perfect-Plasticity-Sensitivitäten.

Zentrale numerische Befunde:

- Michel-Kritikpunkte liegen im oder nahe am untersuchten dimensionslosen Coulomb-Plastizitätsratenbereich.
- Die reduzierte hydrostatisch-vs-Michel Druckabweichung am Kritikpunkt übersteigt die verwendete Polycristall-Yield-Skala grob um `~1.6e2 ... 1.1e3`.
- Ein rein elastischer Coulombkristall kann den Michel-Zustand in diesem Vergleich nicht halten; Yield tritt vorher auf.
- Nach Yield ist ein plastisches Weiterfließen ein relevanter Kandidat und keine automatische Blockade.

Korrektur:

```text
Stage-3.13 8-GPa-Mikrorettung -> als physische Coulomb-Grenze zurückgezogen
```

## 12. Aktuelle numerische Entscheidungslage

### Bestandene/hart dokumentierte Punkte

- GR-Grenztests des SL-TOV-Minimalstacks.
- Layered-PREM-Baseline auf `~1e-7` oder besser.
- voll gekoppelte 500-/300-km-Referenzpunkte.
- Horizon-/BH-konsistente Randwertbehandlung.
- Michel-Solver analytischer Selfcheck.
- zahlreiche Grenz-/Sensitivitätsrechnungen für Akkretion, Wärme, EOS und Rheologie.

### Nicht abgeschlossen

- vollständige nichtstationäre relativistische Elastoplastik + Plasma + Wärme,
- realistische Elektroneneinfang-/Kompositionsentwicklung,
- vollständiger Massenscan,
- Formation Rule,
- Real-Data-Seismologie-Likelihood,
- unabhängige experimentelle Signatur.

## 13. Aktueller stärkster negativer Befund

Für den `1e16 kg`-Referenzzweig liefert Standard-Hawking + ununterdrückte relativistische Michel-Akkretion im Stage-3.12-Modell **kein langfristig überlappendes Massenfenster**.

Dieser Befund ist modellabhängig, aber er ist derzeit der stärkste physikalische Gegentest des Erdmoduls und wird nicht als bestanden umetikettiert.

## 14. Nächste numerische Priorität

Massenscan über mehrere Größenordnungen:

```text
M_SL ~ 1e8 ... 1e16 kg
```

mit identischem Stack für

```text
Hawking + Michel + Solid/Plasma-Transport + Earth-age + Earth-Matching.
```

Ziel ist die Bestimmung eines tatsächlich verbleibenden Parameterfensters oder dessen Ausschluss innerhalb des gewählten Modells.
