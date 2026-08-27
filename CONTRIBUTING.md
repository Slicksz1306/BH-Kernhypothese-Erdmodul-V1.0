# Wissenschaftliche Beiträge und Review

Dieses Repository dokumentiert ein theoretisches Forschungsmodell. Beiträge sollen deshalb möglichst prüfbar, reproduzierbar und klar zwischen Modellannahme, Mathematik, Numerik und Beobachtung unterscheiden.

## Offizieller Projektstand

Die **SL/BH-Kernhypothese Erdmodul** ist das offizielle Forschungsprojekt von
**Daniel Marcel Schlicksupp**.

Externe Beiträge, Issues, Kommentare, Rechnungen und Pull Requests sind als
wissenschaftliche Vorschläge willkommen. Sie verändern den offiziellen
Projektstand jedoch **nicht automatisch**.

Eine externe Änderung wird erst dann Bestandteil des offiziellen Projekts,
wenn Daniel Marcel Schlicksupp sie ausdrücklich geprüft und in den offiziellen
Projektstand übernommen bzw. gemerged hat.

Es besteht kein Anspruch auf Aufnahme eines Pull Requests oder einer externen
Weiterentwicklung in das offizielle Projekt.

Eigene Forks, unabhängige Solver, alternative Modelle und abgeleitete
Forschungsprojekte sind unter den jeweils geltenden CC-BY-4.0-/MIT-Bedingungen
erlaubt. Solche Arbeiten müssen als eigenständig oder verändert gekennzeichnet
werden und dürfen nicht als offizieller neuer Stage-, Versions- oder
Release-Stand dieses Projekts dargestellt werden.

Siehe auch `OFFICIAL_PROJECT_POLICY.md`.

## Sinnvolle Beiträge

Geeignet sind insbesondere:

- Reproduktion oder Widerlegung numerischer Resultate,
- alternative Randwert- oder Collocation-Verfahren,
- Konsistenzprüfungen gegen PREM, Seismologie, Normalmoden oder Trägheitsmoment,
- Analyse von Akkretions-, Capture-, Wärme- oder Langzeitstabilitätsbedingungen,
- Prüfung des GR-Grenzfalls und anderer harter Solverchecks,
- Vorschläge für vorab definierte, falsifizierbare Beobachtungssignaturen,
- Hinweise auf Dimensions-, Einheiten-, Vorzeichen- oder Implementierungsfehler.

## Mindestangaben für einen belastbaren Review

Bitte möglichst angeben:

1. exakte betroffene Gleichung, Datei oder Abschnitt,
2. verwendeten Parametersatz,
3. Einheiten und Konventionen,
4. numerisches Verfahren und Toleranzen,
5. erwartetes gegenüber beobachtetem Ergebnis,
6. Code, Rechenschritte oder Referenzen, soweit verfügbar.

Ein Einwand sollte erkennen lassen, ob er **konzeptionell**, **mathematisch**, **numerisch** oder **empirisch** ist. Diese Ebenen werden im Projekt bewusst getrennt.

## Reproduzierbarkeit

Numerische Aussagen gelten nur für den jeweils angegebenen Parametersatz und die dokumentierten Konvergenz-/Solverkriterien. Eine intern validierte numerische Lösung ist kein experimenteller Nachweis eines Schwarzen Lochs im Erdzentrum.

Der aktuelle numerische Stand und seine Grenzen sind in `NUMERIK_STATUS.md` dokumentiert.

## Lizenzierung externer Beiträge

Bitte keine Inhalte einreichen, für deren Weitergabe keine Rechte bestehen.

Sofern nicht ausdrücklich anders vereinbart, sollen Beiträge, die tatsächlich
in das offizielle Repository übernommen werden, mit dessen Lizenzschema
vereinbar sein:

- Nicht-Software-Inhalte: **CC BY 4.0**
- Quellcode: **MIT License**

## Archivschutz

Die Datei `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` ist die archivierte Erstveröffentlichung vom 23.08.2026 und soll nicht überschrieben oder nachträglich verändert werden. `SHA256SUMS.txt` dokumentiert ihre Prüfsumme.

Änderungen am aktuellen Modelltext sollen stattdessen versioniert in den Markdown-Dateien erfolgen und im `CHANGELOG.md` nachvollziehbar bleiben.
