# Changelog

Dieses Changelog dokumentiert die öffentlich sichtbaren Entwicklungsstände des Erdmoduls.

## V1.2 / Stage 1.7 — 25.08.2026

Aktueller Theorie- und Numerikstand des Repositories.

### Modell und Dokumentation

- Titel auf **SL/BH-Kernhypothese Erdmodul** vereinheitlicht.
- Kleiner redistributiver SL/BH-Zweig bleibt das aktuelle Erd-Basismodell.
- Massenbuchhaltung weiterhin `M_PREM(<r_rep) = M_SL`.
- Strikte Trennung von Modellannahme, numerischer Validierung und experimentellem Nachweis.
- `TEST_STATUS.md` als zusammenhängende Test- und Validierungsmatrix ergänzt.

### Stage 1.5D

Für den Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

wurde die BH-konsistente Fortsetzung erweitert:

- `r_c = 500 km`: validiert,
- `r_c = 300 km`: validiert,
- `r_c = 275 km`: Kandidat,
- `r_c <= 250 km`: numerisch offen.

Für 300 km gilt ungefähr `xi/xi_crit,BH ≈ 1.000142`, `q_max ≈ 1e-14`. Die differentielle Massenabweichung gegenüber dem jeweiligen GR-Lauf liegt ungefähr bei `-(8–9)e-6`.

### Stage 1.6

- Layered-PREM-Earth-Closure eingeführt.
- GR-Baseline verbessert auf ungefähr `Delta R/R ≈ 4.17e-9` und `Delta M/M ≈ 4.44e-8`.
- `r_c = 500 km`: voll gekoppelt validiert, `Delta M/M ≈ -9.2e-6`.
- `r_c = 300 km`: voll gekoppelt und cross-solver-validiert, `Delta M/M ≈ -8.65e-6`.
- `r_c = 250 km`: Kandidat.
- `r_c = 200 km`: offen.
- Kleinster derzeit cross-solver-validierter voll gekoppelter Punkt: `300 km`.

### Stage 1.7

Für die validierten 500- und 300-km-Referenzzweige wurden beobachtungsnähere Erdobservablen berechnet.

- `max |Delta g/g|` für `r >= 100 km`: ungefähr `1.8e-4` (500 km) und `2.1e-4` (300 km).
- zentrale Größenordnung ab `r >= 10 km`: ungefähr `1.5e-3` bzw. `1.6e-3`.
- `|Delta V_P/V_P| ~ 3e-6`.
- ICB-Verschiebung: `-43.8 m` (500 km), `-61.1 m` (300 km).
- CMB-Verschiebung: `-35.0 m` (500 km), `-33.9 m` (300 km).
- P-Wellen-Laufzeit: `+0.0119 s` (500 km), `+0.0088 s` (300 km).
- Materie-Trägheitsmoment: `Delta I/I ~ -(7–8)e-6`.

Zusätzlich wurde für `r_c = 300 km` ein Amplitudenscan dokumentiert. Bei `q=1e-13` ergeben sich ungefähr ICB/CMB-Verschiebungen von `-604 m/-339 m` und `Delta T_P ≈ +0.095 s`; bei `q=3e-13` ungefähr `-1.77 km/-1.02 km`. Diese größeren Amplituden sind Sensitivitätspunkte und nicht als konservative Erdparameter promoted.

## Früherer V1.2 / Stage 1.3C-Stand — 25.08.2026

Der erste öffentliche V1.2-Numerikstand dokumentierte eine Precision-Single-Shooting-Frontier bei `r_c = 500 km` für `M_SL=1e16 kg`, `q0=1e-14`. `r_c=300 km` war mit dem damaligen Solver noch nicht validiert; der 100-km-Collocation-Lauf blieb wegen fehlender Mesh-Konvergenz Kandidat.

Dieser Stand bleibt historisch nachvollziehbar, wurde aber durch Stage 1.5D, 1.6 und 1.7 überholt.

## V1.0 — 23.08.2026

Erstveröffentlichung des Erdmoduls.

- Archivierte Veröffentlichungsfassung: `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf`.
- Integritätsnachweis über `SHA256SUMS.txt`.
- Diese PDF bleibt unverändert als Archiv- und Prioritätsnachweis erhalten.

## Versionsprinzip

Der Repository-Name enthält aus historischen Gründen weiterhin `V1.0`. Der aktuelle Textstand wird in `README.md`, `THEORIE.md`, `NUMERIK_STATUS.md`, `TEST_STATUS.md` und `CITATION.cff` geführt. Archivierte Publikationsdateien werden nicht nachträglich überschrieben.
