# Stage 3.69F / A-10 – First-Principles-Informed WDM Transport + Time-Dependent Sink Coupling

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** PARTIAL FIRST-PRINCIPLES-INFORMED TRANSPORT ENVELOPE CALCULATED / FULL WDM-HYDRO NOT YET CLOSED

## Ausgangsfrage

A9 verwendete fuer den strong-coupling Branch eine geometrische Mean-Free-Path-Skalierung. A10 prueft, ob der zentrale A9-Befund bestehen bleibt, wenn der aeussere Fe/Fe-Ni-Transport an publizierte QMD/ab-initio-Daten gekoppelt und die innere Zone mit einer konservativen WDM/OCP-Skalierung fortgesetzt wird.

## Durchgefuehrter A10-Teil

```text
PREM/core reference state
 -> published Fe/Fe-Ni diffusion + viscosity
 -> QMD-domain map on rho(x),T(x)
 -> transport mean-free-path envelope
 -> QMD-normalized escape-favoring inner OCP scaling
 -> local Kn=1 radius
 -> integrated escape optical depth
 -> A9 repeated-encounter processing capacity
 -> M=1e10...5e11 kg scan.
```

Reproduzierbar in:

- `STAGE3_69F_A10_WDM_TRANSPORT_ENVELOPE.md`
- `stage3_69f_a10_wdm_transport_envelope.py`

## Literaturabdeckung

Warm-dense Fe-QMD liefert Transport fuer etwa

```text
rho=12.5...25 g/cm^3
T=0.5...15 eV.
```

Auf dem aktuellen Reduced Inward-Pfad wird `rho=25 g/cm^3` bereits bei

```text
x=r/r_B ~0.6496
```

erreicht. Die 2025 first-principles Fe-EOS reicht bis `47.2 g/cm^3`, entsprechend nur bis etwa `x~0.425` auf diesem Proxy.

Damit ist die aeussere Zone first-principles/QMD-kalibrierbar; die tiefste innere Zone liegt ausserhalb direkt publizierter Transporttabellen.

## Zentrales A10-Ergebnis

Selbst der schnellste / escape-freundlichste QMD-kalibrierte Transportfall besitzt allein im aeusseren QMD-Shell eine Kollisionsoptische Tiefe von ungefaehr

```text
M=1e10 kg: tau_outer ~74.7
M=1e11 kg: tau_outer ~747.
```

Mit der QMD-normalisierten inneren `Z=2` OCP-Sensitivitaet wird am lokalen `Kn=1`-Punkt

```text
M=1e10 kg: tau_total ~192
M=1e11 kg: tau_total ~1932
M=2e11 kg: tau_total ~3865
M=5e11 kg: tau_total ~9663.
```

Damit gilt im getesteten Envelope:

```text
local Kn~1 != permanent escape to the outer reservoir.
```

Der Weg nach aussen bleibt kollisionsoptisch dick.

## Processing-Capacity

Im schnellsten Diffusionsfall am oberen historischen Supply:

```text
M=1e10 kg: Xi_high ~1.47 -> backpressure-sensitive
M=1e11 kg: Xi_high ~2.81e-3
M=2e11 kg: Xi_high ~4.28e-4
M=5e11 kg: Xi_high ~3.54e-5.
```

Fuer die mittlere und langsamere QMD-Kalibrierung liegt `Xi` noch weiter unter 1.

Daher wird der A9-Massensplit reproduziert:

```text
M>=~1e11 kg:
    reduced transport branch remains supply-processing capable.

M=1e10 kg:
    remains backpressure/transport sensitive.
```

## Acceptance-Criteria-Status

1. `rho,T`-Pfad reproduzierbar: **DONE**.  
2. Transportquellen/Gueltigkeitsbereiche dokumentiert: **DONE fuer aeusseren QMD-Shell; inner extrapolation explicit sensitivity**.  
3. `e_perm` aus Transportoptical-depth statt freiem Faktor: **DONE als Reduced Envelope**.  
4. voller zeitabhaengiger WDM-1D-Solver mit Massenerhaltung: **OPEN**.  
5. absorbing/reflecting dynamische Regression: **A7 DONE; A10 real partial sink OPEN**.  
6. Massenscan `1e10...5e11 kg`: **DONE fuer Reduced Envelope**.  
7. finales first-principles `Mdot_BH`-Band: **OPEN**.  
8. Extrapolationsunsicherheit sichtbar: **DONE**.  
9. kein empirischer Nachweis behauptet: **DONE**.

## Aussagegrenze

A10 bestaetigt **nicht** die Existenz eines Erdzentrum-BH. Es zeigt lediglich, dass die A9-Recycling/Processing-Schlussfolgerung fuer `M>=~1e11 kg` auch unter einem first-principles-informierten und bewusst escape-freundlichen Transportenvelope bestehen bleibt.

Die tiefste WDM-Zone ist noch nicht first-principles geschlossen.

## Naechster Pflichtblock

```text
Stage 3.69G / A11:
EOS/ionization table + time-dependent partial-sink WDM/Bondi PDE
+ energy equation
+ charge/composition advection
+ A4/A5 absorptive capture boundary
-> dynamically generated backpressure
-> tighter species-resolved net-Mdot_BH band.
```

A10 bleibt gemeinsamer Materietransport fuer H+ und H0. H+ besitzt zusaetzliche Hawking-Terme; der bisherige H+-Neutrinobefund wird durch A10 nicht aufgehoben.
