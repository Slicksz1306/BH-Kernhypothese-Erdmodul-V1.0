# Changelog

Dieses Changelog dokumentiert die öffentlich sichtbaren Entwicklungsstände des Erdmoduls.

## V1.3 / Stage 3.15 — 25.08.2026

Massenscan `M_SL~1e8...1e16 kg` und wichtige Korrektur des kombinierten Hawking/Michel-Langzeitarguments.

### Stage 3.15 – simultane Massenentwicklung

Statt Standard-Hawking und Michel-Akkretion als getrennte Ausschlussgrenzen zu schneiden, wird nun die reduzierte gemeinsame Gleichung verwendet:

```text
dM/dt = k_Michel M^2 - A_H/M^2.
```

Für die fünf Stage-3.12-`Y_e`-Zweige ergibt sich im einfachen Standard-Hawking-Benchmark ein instabiles Gleichgewicht

```text
M_eq ~ 1.28e11 ... 2.28e11 kg.
```

Die lineare e-Faltungszeit liegt ungefähr bei

```text
4.23e9 ... 2.37e10 Jahre.
```

Für weniger als `1%` Netto-Massenänderung über `4.54 Gyr` liegt das Anfangsmassenband je nach `Y_e` ungefähr bei

```text
-0.51/+0.53% bis -4.40/+5.12% um M_eq.
```

### Korrektur zu Stage 3.12

Die frühere starke Aussage

```text
Standard-Hawking + ununterdrücktes Michel -> kein überlappendes Langzeitfenster
```

wird korrigiert. Sie entstand aus getrennten Einzelgrenzen. Bei simultaner Evolution existiert im reduzierten Modell ein Hawking/Michel-Kompensationsband.

Dieses Band ist kein stabiler Attraktor und kein Nachweis eines Erd-SL.

### Materialphysik-Grenze

Das neue Gleichgewichtsband liegt weit unterhalb des direkten Stage-3.14-Coulomb-MD-Ratenbereichs. Die dimensionslose Michel-Deformationsrate skaliert ungefähr wie `1/M`.

Die Stage-3.14-MD-Kalibrierung ist je nach Proxy erst oberhalb von ungefähr

```text
5.4e14 ... 1.2e16 kg
```

direkt anwendbar. Das neue `~1e11 kg`-Band liegt etwa `4e3 ... 5e4` darunter.

### Earth-Matching-Grenze

Für das neue Kandidatenband beträgt der PREM-Ersatzradius nur ungefähr

```text
133 ... 161 m.
```

Der voll gekoppelte Earth-Matching-Stack ist in diesem niedrigen `M_SL`-/sub-km-Bereich noch nicht cross-solver-validiert.

### Neue Datei

- `MASSENSCAN_STAGE3_15.md` – vollständige öffentliche Zusammenfassung des Massenscans.

---

## V1.3 / Stage 3.14 — 25.08.2026

Größere Härtung des Akkretions-, Near-Zone- und Materialphysikblocks.

- Bondi-Algebra reproduziert; kein mathematischer Fehler gefunden.
- Mikroakkretion, Creep, Wärme und Zwei-Phasen-Feedback untersucht.
- alte `~54 r_s`-Grenze als nicht EOS-robust zurückgezogen.
- relativistische Michel-Akkretion implementiert und analytisch gegengeprüft.
- für `M_SL=1e16 kg` ergab die phenomenologische Dense-Matter-EOS `Mdot_Michel~147...1460 kg/s`.
- hcp-Fe-Solid/Michel-Kopplung lieferte bei Millimeterradien keine ausreichende Unterdrückung.
- Coulomb-Plastizität schwächte eine generische Festkörperblockade weiter.
- Stage-3.13-`8 GPa`-Mikrorettung als Coulomb-Langzeitgrenze zurückgezogen.

---

## V1.2 / Stage 1.7 — 25.08.2026

- Titel auf **SL/BH-Kernhypothese Erdmodul** vereinheitlicht.
- kleiner redistributiver SL/BH-Zweig als aktuelles Erd-Basismodell dokumentiert.
- Layered-PREM-Earth-Closure eingeführt.
- GR-Baseline auf ungefähr `Delta R/R~4.17e-9`, `Delta M/M~4.44e-8` verbessert.
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
