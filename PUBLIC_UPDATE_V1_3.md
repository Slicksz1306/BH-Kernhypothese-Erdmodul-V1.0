# Öffentliche Forschungsnotiz – SL/BH-Kernhypothese Erdmodul V1.3

**Stand:** 25.08.2026  
**Autor:** Daniel Marcel Schlicksupp

Das Erdmodul wurde nach einer erweiterten Serie von Struktur-, Seismologie-, Akkretions-, Hochdruck-EOS- und Rheologietests auf **V1.3 / Stage 3.14** aktualisiert.

## Wichtigste Fortschritte

- Layered-PREM-Earth-Matching mit cross-solver-validierten Referenzpunkten bei `r_c=500 km` und `r_c=300 km`.
- Horizon-/BH-konsistente Randwertbehandlung.
- Seismologie-/Laufzeit-/Trägheitsmoment-Sensitivitäten.
- Mikroakkretions-, Wärme- und Melt-Feedback-Tests.
- nichtlineare hcp-Fe-Rheologie und Hochdruck-EOS-Härtung.
- relativistischer Michel-Akkretionssolver mit analytischem Selfcheck.
- Coulombkristall-/Plastizitäts-Audit der tiefen degenerierten Near Zone.

## Wichtigste Korrekturen

Frühere zu starke Zwischenaussagen wurden nicht beibehalten:

- „lokale Wärme startet zwangsläufig sofort Bondi“: zu stark.
- alte `~54 r_s`-Capture-Grenze: nicht EOS-robust, zurückgezogen.
- `8 GPa`-Mikro-Suppressionsgrenze aus hcp-Fe: nicht auf das tiefe Coulomb-Regime übertragbar, als physischer Rettungsmechanismus zurückgezogen.

## Aktuell stärkster Gegentest

Für den häufig getesteten Referenzpunkt

```text
M_SL = 1e16 kg
```

ergibt eine phenomenologische Dense-Matter-EOS im relativistischen Michel-Test ungefähr

```text
Mdot_Michel ~ 147 ... 1460 kg/s.
```

Für weniger als `+1%` Masse über das Erdalter wäre im Mittel nur ungefähr

```text
Mdot_1% ~ 6.98e-4 kg/s
```

zulässig.

Damit benötigt dieser konkrete Zweig eine quantitativ nachgewiesene Unterdrückung von ungefähr

```text
2e5 ... 2e6
```

gegenüber der ununterdrückten Michel-Kapazität.

Eine solche Unterdrückung wurde bisher weder durch gewöhnliches hcp-Fe-Creep noch durch einen generischen Coulomb-Festkörpermechanismus belastbar gezeigt.

## Wissenschaftliche Aussage

Der aktuelle Stand ist eine **ausgearbeitete, falsifizierbare SL-Kernhypothese mit relativistischem und numerischem Forschungsrahmen**.

Es wird **kein experimenteller Nachweis eines Schwarzen Lochs im Erdzentrum** behauptet.

Der nächste prioritäre Test ist ein vollständiger Massenscan über mehrere Größenordnungen, um zu bestimmen, ob innerhalb desselben Hawking-/Michel-/Transportstacks überhaupt ein langfristig konsistentes Erd-SL-Massenfenster verbleibt.

Repository: `Slicksz1306/SL-BH-Kernhypothese-Erdmodul`
