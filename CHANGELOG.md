# Changelog

Dieses Changelog dokumentiert die öffentlich sichtbaren Entwicklungsstände des Erdmoduls.

## V1.2 — 25.08.2026

Aktueller Theorie-Textstand des Repositories.

- Wechsel auf den kleinen redistributiven Erd-BH-Zweig als aktuelles Basismodell.
- Präzisierung der Massenbuchhaltung mit `M_PREM(<r_rep) = M_SL`.
- Klare Trennung von Schwarzschildradius `r_s`, Bondi-/Referenzskala `r_B` und strukturellem Ersatzradius `r_rep`.
- Explizite Trennung zwischen interner Modellkompatibilität, numerischer Validierung und experimentellem Nachweis.
- Integration des SL-TOV / Earth-Matching-Stacks mit Jordan-Frame-Minimalfassung.
- Numerischer Entwicklungsstand 1.3C dokumentiert.
- Für den fortgesetzten Zweig `M_SL = 1e16 kg`, `q0 = 1e-14` sind `r_c = 1000 km`, `750 km` und `500 km` innerhalb der festgelegten numerischen Kriterien validiert.
- `r_c = 300 km` ist mit dem aktuellen Single-Shooting schlecht konditioniert; der 100-km-Collocation-Lauf bleibt Kandidat ohne bestätigte Mesh-Konvergenz.
- Offene Physik und Falsifikationsprinzip explizit ausgewiesen.

## V1.0 — 23.08.2026

Erstveröffentlichung des Erdmoduls.

- Archivierte Veröffentlichungsfassung: `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf`.
- Integritätsnachweis über `SHA256SUMS.txt`.
- Diese PDF bleibt unverändert als Archiv- und Prioritätsnachweis erhalten.

## Versionsprinzip

Der Repository-Name enthält aus historischen Gründen weiterhin `V1.0`. Der aktuelle Textstand wird in `README.md`, `THEORIE.md`, `NUMERIK_STATUS.md` und `CITATION.cff` geführt. Archivierte Publikationsdateien werden nicht nachträglich überschrieben.
