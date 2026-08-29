# Stage 3.72 / A22 – Fe-Ni-light-element WDM data gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** PUBLIC MIXTURE DATASET VERIFIED / INGESTION GATE COMPLETE / NUMERICAL MIXTURE EOS CLOSURE OPEN

## Warum A22 noetig ist

A13b/A20 nutzen reines bzw. nahezu reines liquid Fe als Outer-EOS-Anker. Die reale Erde besitzt jedoch keinen reinen Fe-Aussenkern. Fuer die Full-WDM-Closure muss mindestens Fe-Ni plus ein Sensitivitaetsraum fuer plausible leichte Elemente betrachtet werden.

## Neue primaere Datenbasis

Liu & Asimow (2025), JGR Solid Earth, DOI `10.1029/2024JB030419`, simulieren Fluessigmetall bei Druck-/Temperaturbedingungen des Erdaussenkerns und behandeln

```text
Fe-Ni
Fe-O
Fe-Si
Fe-S
Fe-C
Fe-H
```

sowie ausgewaehlte ternaere/hoehere Mischungen. Die Arbeit konstruiert daraus ein Multikomponenten-Mischungsmodell und vergleicht selbstkonsistente Profile mit seismischen Modellen wie PREM.

Die zugehoerigen Rohdaten sind in CaltechDATA veroeffentlicht:

```text
Liu & Asimow (2024)
DOI: 10.22002/dxgqf-tw269
License: CC0 1.0
```

Der Record ist als `Dataset Open` ausgewiesen.

## Verifizierte Dateien

Der CaltechDATA-Record listet unter anderem:

```text
Fe11.xls
Ni_Fe11.xls
O_Fe11.xls
Si_Fe11.xls
S_Fe11.xls
C_Fe11.xls
H_Fe11.xls
O12_Si6_Fe11.xls
O6_Si12_Fe11.xls
O9_Si9_Fe11.xls
O32_Fe11.xls
Si9_Fe11.xls
Table.S.1.xlsx
Table.S.2.xlsx
Table.S.3.xlsx
tableS4.xlsx
shock_wave_data.xlsx
```

Damit existiert eine konkrete oeffentliche Datenbasis fuer die Fe/Ni/light-element-EOS-Closure; die Zusammensetzung muss nicht mehr durch frei gewaehlte ad-hoc Mischungsparameter ersetzt werden.

## Aktueller Downloadstatus

Die HTML-Metadaten, Dateinamen, Groessen, MD5-Hashes und CC0-Lizenz sind verifiziert. Der aktuelle Toolpfad kann die binaeren `.xls/.xlsx` Downloads jedoch nicht stabil abrufen (`cache miss`).

Es werden deshalb **keine Workbook-Werte erfunden oder aus Suchsnippets rekonstruiert**.

```text
public dataset existence/coverage: VERIFIED
binary workbook content ingestion in current run: BLOCKED BY TOOL DOWNLOAD
```

Das ist ein Zugriffsblock, kein physikalischer Test-Fail.

## Implementierter Ingestion Gate

`stage3_72_a22_mixture_wdm_data_gate.py` kann nach lokalem Vorliegen der Workbooks:

1. alle erwarteten Dateien inventarisieren;
2. Workbook-Sheets und Spalten erfassen;
3. numerische Wertebereiche melden;
4. Kandidatenspalten fuer `P`, `T`, `rho/V`, Energie markieren;
5. ein Mindest-Thermodynamik-Schema pruefen;
6. fehlende Dateien oder Excel-Engine-Probleme explizit melden;
7. einen JSON-Audit-Report erzeugen.

Der Gate besitzt einen synthetischen Schema-Selftest.

## Harte wissenschaftliche Guardrails

Der Code behandelt Spaltennamen nur als Kandidaten. Er darf **nicht** automatisch annehmen, dass beispielsweise eine Spalte `P` in GPa oder `V` in A^3/Atom steht.

Vor einer EOS-Rechnung muessen Einheiten und thermodynamische Definitionen aus Workbook-/Paper-Metadaten explizit feststehen.

Ebenso wird kein automatisches lineares Mischgesetz angenommen. Liu & Asimow untersuchen Nichtidealitaeten und konstruieren ein thermodynamisches Multikomponentenmodell; ein simples

```text
P_mix = sum X_i P_i
```

waere ohne Herleitung keine zulaessige Ersatzclosure.

## Bedeutung fuer die bisherige Hypothese

A22 korrigiert keine A13b-Zahl direkt, weil die Binärdaten im aktuellen Lauf nicht eingelesen werden konnten. Es verbessert aber die Datenlage wesentlich:

```text
A13b pure-Fe experimental-fit sensitivity
    -> bleibt gueltiger Partial-Outer-Anker

A22 public Fe-Ni-light-element first-principles dataset
    -> verified preferred input for Full-WDM mixture closure
```

Die zentrale A15-Aussage bleibt daher unveraendert:

```text
>=1e11 kg processing-capable in tested reduced stack
1e10 kg supply/EOS/backpressure conditional
```

Sie wird durch A22 weder zum Full-Physics-PASS noch falsifiziert.

## Was A22 noch nicht liefert

```text
real mixture P(rho,T,X)
real mixture e(rho,T,X)
consistent entropy/isentrope
Te/Ti two-temperature transport
reaction network
stochastic Q(t)
final species-resolved Mdot_BH(t)
```

Diese Punkte bleiben Full-WDM-Aufgaben.

## Reproduzierbare Datei

- `stage3_72_a22_mixture_wdm_data_gate.py`

## A22 Schlussstatus

```text
Public Fe-Ni-light-element raw-data source:
VERIFIED.

License/access metadata:
OPEN / CC0 VERIFIED.

Workbook ingestion/schema machinery:
COMPLETE / PASS synthetic regression.

Actual binary workbook numerical ingestion:
BLOCKED BY CURRENT TOOL DOWNLOAD.

Full multicomponent EOS closure:
OPEN.
```
