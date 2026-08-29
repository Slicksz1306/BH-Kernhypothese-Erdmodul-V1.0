# Stage 3.72 / A20 – Tabulated Fe EOS ingestion gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** INGESTION MACHINERY COMPLETE / RAW GRANT-ZENODO + DIRECT SESAME DATA CLOSURE OPEN

## Ziel

A20 ersetzt **keine** fehlenden Messdaten durch Figure-Digitalisierung oder erfundene Punkte. Der Block baut stattdessen die direkte tabellarische Schnittstelle fuer einen echten Druck-Dichte-Isentropen-Datensatz und prueft, ob ein gelieferter Datensatz den relativistischen Michel-Kritikpunkt tatsaechlich abdeckt.

Eingabeschema:

```text
rho_gcc,P_GPa
```

Optionale Zusatzspalten wie `T_K` oder Unsicherheiten duerfen vorhanden sein.

Solver:

```text
P(rho) -> shape-preserving PCHIP

dh = dP/(rho c^2)

a^2/c^2 = (dP/drho)/(h c^2)

h_s/sqrt(1+3 a_s^2) = h_inf
```

Wenn innerhalb der gelieferten Dichtetabelle kein regulaerer Michel-Kritikpunkt liegt, **verweigert der Code die Extrapolation** und meldet `DATA RANGE INSUFFICIENT`.

## Regression

Die komplette Tabellen-Pipeline wurde gegen den bekannten A13-`beta=1.5`-Fall regressiert.

Bei `M_BH=1e11 kg`:

```text
A13 target ~3.22370e-6 kg/s
A20 tabulated reconstruction ~3.22370e-6 kg/s
relative drift << 2e-4
```

Damit sind CSV-Ingestion, monotone Interpolation, Enthalpie-Rekonstruktion und der Michel-Kritikpunkt-Finder im definierten Regressionstest konsistent.

## Was die Grant-Daten wirklich abdecken

Primaerquelle:

- S. C. Grant et al., *Equation of State Measurements on Iron Near the Melting Curve at Planetary Core Conditions by Shock and Ramp Compressions*, JGR Solid Earth 126 (2021), DOI `10.1029/2020JB020008`.
- Data Availability DOI: `10.5281/zenodo.4464112`.

Die Publikation dokumentiert zwei Z-Machine-Experimente:

```text
Z3155:
  initial shock ~270 GPa
  usable final pressure-density analysis to ~398 GPa
  robust high-pressure path

Z3339:
  initial shock ~265 GPa
  release/ramp path to ~375 GPa
  analysis ceases to converge beyond ~12.6 g/cm3
```

Die Autoren berichten gute Uebereinstimmung mit SESAME 92141 in diesem experimentell abgedeckten Bereich.

## Zentrale neue Aussage

Der Grant-Rohdatensatz ist ein **Outer-core EOS anchor**, aber selbst ein perfekter Rohdatenimport kann die gesamte Michel-Supply-Frage nicht automatisch schliessen.

Grund:

```text
measured Grant domain ~few 100 GPa, rho ~Earth-core scale

Michel critical density in A13/A13b:
can lie far above the directly measured density domain,
depending on the intermediate/deep EOS.
```

Daher gilt:

```text
raw Grant data -> can replace/validate outer fitted segment
raw Grant data alone -> cannot justify uncontrolled extrapolation to rho_crit
```

Die fehlende Intermediate-/Deep-EOS-Closure bleibt physikalisch relevant, selbst nachdem die Zenodo-Daten verfuegbar sind.

## Aktueller Datenzugriffsstatus

Der DOI und die Datenverfuegbarkeit sind in der Primaerpublikation verifiziert. In der aktuellen Tool-Session konnte der konkrete Zenodo-Dateiinhalt jedoch nicht stabil als maschinenlesbare Tabelle abgerufen werden.

Es wurden deshalb ausdruecklich **keine** Punkte aus Figure 7/8 digitalisiert und keine Messpunkte erfunden.

```text
Grant raw CSV/table ingestion: BLOCKED BY DATA ACCESS IN CURRENT RUN
SESAME 92141 direct table ingestion: NOT AVAILABLE IN CURRENT RUN
```

Das ist kein physikalischer FAIL der Hypothese, sondern ein offener externer Daten-/Lizenz-/Zugriffsblock.

## Physikalische Zusatzwarnung

Grant misst **reines bzw. nahezu reines Eisen**. Die reale Erde besitzt im aeusseren Kern einen Fe/Ni/light-element Mix. Deshalb ist auch eine vollstaendige reine-Fe-Tabelle nicht automatisch identisch mit der PREM-Mischungs-EOS.

Der korrekte naechste Full-Physics-Pfad bleibt:

```text
raw liquid-Fe data
+ Fe/Ni/light-element mixture EOS
+ thermal / two-temperature closure
-> continuous outer-to-critical EOS
-> general-EOS Michel
-> transport/capture recoupling
-> final species-resolved Mdot_BH(t)
```

## Reproduzierbare Datei

- `stage3_72_a20_tabulated_eos_gate.py`

## A20 Schlussstatus

```text
Tabulated EOS ingestion machinery:
PASS / COMPLETE in regression scope.

Grant raw-data physics closure:
OPEN / BLOCKED BY DATA ACCESS.

Direct SESAME-92141 closure:
OPEN.

Uncontrolled extrapolation from measured Grant range to Michel critical point:
REJECTED.

Final physical Mdot_supply:
OPEN.
```
