# Stage 3.69F / A10 – First-Principles-Informed WDM Transport Envelope

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** PARTIAL FIRST-PRINCIPLES-INFORMED TRANSPORT CLOSURE CALCULATED / A9 MASS-REGIME SPLIT CONFIRMED / FULL WDM-HYDRO STILL OPEN

## Ziel

A10 ersetzt den einzelnen geometrischen Mean-Free-Path-Proxy aus A9 durch ein publiziertes Fe/Fe-Ni-Transportfenster und eine konservative innere Plasma-Extrapolation.

Die Frage lautet:

```text
published Fe transport
 -> collision / diffusion envelope
 -> permanent escape optical depth
 -> local Kn=1 transition
 -> repeated capture / residence
 -> processing capacity
 -> backpressure sensitivity
 -> net-Mdot reduced band.
```

Kein Ergebnis dieses Blocks ist ein experimenteller Nachweis eines Erdzentrum-BH.

## 1. Literaturanker

### Liquid Fe / Fe-Ni nahe Erdkernbedingungen

Ab-initio/QMD-Arbeiten liefern fuer fluessiges Fe bzw. Fe-Ni Selbst-Diffusionskoeffizienten in der Groessenordnung

```text
D_i ~5e-9 m^2/s
```

und dynamische Viskositaeten im Bereich weniger bis einiger zehn mPa s. Als konkrete publizierte Referenzen werden u.a. verwendet:

- Alfè, Kresse & Gillan, Phys. Rev. B 61 (2000): first-principles liquid Fe transport;
- Fe-Ni QMD, Scientific Reports 12 (2022): `D_Fe~5.2e-9 m^2/s`, `eta~8.5 mPa s` bei `T=4300 K`, `rho=10.7 g/cm^3`;
- breite liquid-Fe Literaturwerte um `eta~6...26 mPa s`.

### Warm-dense Fe QMD

Wang et al., Phys. Rev. E 89, 023101 (2014), berechnen EOS, Selbst-Diffusion und Viskositaet fuer

```text
rho = 12.5 ... 25 g/cm^3
T   = 0.5 ... 15 eV.
```

Die QMD-Ergebnisse stuetzen eine Stokes-Einstein-artige Relation. Der dimensionslose Faktor liegt im betrachteten Bereich zwischen klassischen Grenzen und etwa `0.18`.

### Erweiterte Fe-EOS

Blanchet et al., Phys. Rev. E 111, 015206 (2025), erweitern first-principles Fe-EOS/ionization calculations auf

```text
rho = 7.874 ... 47.2 g/cm^3
T   = 5500 K ... 1e9 K.
```

Diese Arbeit erweitert die EOS-Abdeckung deutlich, liefert aber keine komplette Transporttabelle fuer den gesamten A10-Inward-Pfad.

### Strong-coupling / WDM transport

Effective-Potential-Theory und moderne WDM-Stopping-Modelle zeigen, dass klassische schwach gekoppelte Spitzer-Transporttheorie in WDM nicht blind verwendet werden darf. Screening, Korrelationen und Elektronendegeneration muessen in den Transport eingehen.

## 2. Direkte Datenabdeckung des reduzierten Erdpads

A8/A9 benutzen als Sensitivitaet

```text
rho(x)=rho0*x^-3/2
T(x)=T0/x
x=r/r_B
rho0=13.0885 g/cm^3
T0=6000 K.
```

Die Wang-QMD-Transportdichte `25 g/cm^3` wird bereits erreicht bei

```text
x_QMD_min = 0.64958.
```

Dort gilt

```text
T ~9237 K ~0.796 eV.
```

Die 2025 first-principles EOS-Dichtegrenze `47.2 g/cm^3` wird bei

```text
x ~0.425.
```

ueberschritten.

**Konsequenz:** Die publizierten first-principles Daten kalibrieren den aeusseren Near-Zone-Shell gut, decken aber die extrem komprimierte innere Zone des reduzierten Profiles nicht direkt ab. Eine Behauptung `A10 full first-principles solved` waere daher nicht gerechtfertigt.

## 3. Outer-shell Transportenvelope

Aus QMD/Stokes-Einstein und der publizierten Fe-Viskositaet wird am Rand `x=0.64958` ein bewusst breites effektives Momentum-Randomization-Length-Band verwendet:

```text
slow:    lambda_match = 2.48e-12 m
mid-QMD: lambda_match = 9.54e-12 m
fast:    lambda_match = 3.65e-11 m.
```

Der `fast`-Fall ist absichtlich escape-freundlich.

Schon **nur** fuer den direkt QMD-abgedeckten Shell `x=0.64958...1` folgt:

```text
M=1e10 kg:
    tau_outer_QMD = 74.7 ... 1099

M=1e11 kg:
    tau_outer_QMD = 747 ... 10985.
```

Damit ist permanenter ballistischer Escape bereits im publiziert kalibrierten aeusseren Shell exponentiell unterdrueckt.

Im schnellsten Fall bei `1e10 kg`:

```text
exp(-tau_outer) ~ exp(-74.7) << 1.
```

Es ist daher nicht notwendig, die unbekannte tiefste WDM-Zone als perfekt kollisional anzunehmen, um zu zeigen, dass ein Teilchen vom inneren Bereich nicht einfach frei durch den gesamten aeusseren dichten Fe-Shell entkommt.

## 4. Konservative innere Scaling-Closure

Fuer `x<0.64958` wird kein frei erfundener konstanter Mean-Free-Path eingesetzt.

Als Sensitivitaet wird die OCP-Selbst-Diffusionsskalierung

```text
D* = 2.95 Gamma^-1.34
```

verwendet und **kontinuierlich an den QMD-Shell normiert**.

Fuer diese innere Skalierung wird bewusst `Z=2` genommen. Wang et al. verwendeten denselben niedrigen Ionladungswert als OCP-Vergleich; oberhalb einiger eV uebersteigt das OCP-Modell ihre QMD-Diffusion. Damit ist dieser Branch als escape-freundlicher / diffusiver Vergleich gedacht, nicht als Behauptung ueber die reale tiefe Fe-Ionisation.

Hoehere reale Ionisation und staerkere Korrelation koennen die Kollisionalitaet erhoehen.

## 5. Kn=1 und Escape-Optical-Depth

Der Solver bestimmt fuer jede Transportkalibrierung den lokalen Radius

```text
Kn=lambda/r=1
```

und integriert danach die gesamte optische Tiefe bis `r_B`.

### Schnellstes / escape-freundlichstes Envelope

| `M_BH` | `x_Kn1` | `r_Kn1` [m] | `tau_total` | `Xi_high` |
|---:|---:|---:|---:|---:|
| `1e10 kg` | `3.96e-3` | `2.43e-11` | `1.92e2` | `1.47` |
| `1e11 kg` | `3.24e-4` | `1.99e-11` | `1.93e3` | `2.81e-3` |
| `2e11 kg` | `1.53e-4` | `1.87e-11` | `3.86e3` | `4.28e-4` |
| `5e11 kg` | `5.63e-5` | `1.73e-11` | `9.66e3` | `3.54e-5` |

Der lokale `Kn=1`-Radius liegt damit fuer den relevanten `1e11...5e11 kg`-Bereich um `~2e-11 m`, also nahe bzw. unterhalb des unteren A9-Transition-Sensitivity-Bereichs.

Trotz lokalem `Kn~1` bleibt

```text
tau_out >> 1
```

weil die Materie auf dem Weg nach aussen wieder durch einen sehr optisch dicken WDM/liquid-Fe-Shell muss.

Damit ist

```text
local kinetic transition != permanent escape to outer reservoir.
```

## 6. Processing Capacity / Backpressure

A9 definierte

```text
Xi = Mdot_supply / Mdot_capacity.
```

- `Xi<=1`: der Reduced Reservoir-/Recycling-Sink kann den auferlegten Supply verarbeiten;
- `Xi>1`: Pile-up/Backpressure wird relevant.

A10 ergibt:

### `M>=1e11 kg`

Fuer **alle drei** QMD/WDM-Transportkalibrierungen gilt sogar am oberen historischen Supply:

```text
Xi_high << 1.
```

Im schnellsten Diffusionsfall:

```text
1e11 kg: Xi_high ~2.81e-3
2e11 kg: Xi_high ~4.28e-4
5e11 kg: Xi_high ~3.54e-5.
```

Damit bleibt der A9-Befund fuer diesen Reduced Branch stabil:

```text
M>=~1e11 kg:
    supply-processing capable.
```

### `M=1e10 kg`

Hier ist der Ausgang transportabhaengig:

```text
slow envelope:    Xi_high ~9.9e-4
mid-QMD envelope: Xi_high ~3.8e-2
fast envelope:    Xi_high ~1.47.
```

Nur der schnellste / am wenigsten kollisional gedachte Rand ueberschreitet `Xi=1` leicht.

Damit bleibt

```text
M=1e10 kg:
    backpressure-sensitive / OPEN.
```

Diese qualitative Massentrennung reproduziert A9 mit einer deutlich staerker an publizierte Transportphysik gekoppelten Closure.

## 7. Was A10 widerlegt bzw. nicht stuetzt

Nicht gestuetzt wird die einfache Kette

```text
local Kn~1
 -> particle escapes permanently
 -> one-pass loss cone becomes net-Mdot factor.
```

Der aeussere QMD-kalibrierte Shell allein besitzt dafuer eine viel zu grosse Kollisionsoptische Tiefe.

Ebenso wird fuer `M>=1e11 kg` im getesteten Transportenvelope keine 5-6-Orders-of-Magnitude-Netto-Unterdrueckung erzeugt.

## 8. Was A10 NICHT beweist

A10 ist **kein** vollstaendiger first-principles WDM-Solver.

Offen bleiben insbesondere:

```text
Zbar(rho,T) ueber den gesamten tiefen Pfad
vollstaendige Fe/Ni EOS ausserhalb publizierter Dichtefenster
electron-ion energy exchange
time-dependent radiation / thermal transport
charged-electron Coulomb capture
real partial-reflection boundary condition
multicomponent Fe/Ni/light-element chemistry
fully coupled hydro/kinetic backpressure solution.
```

Die 2025 Fe-EOS und vorhandene QMD-Transportliteratur reichen nicht bis zu den extremen Dichten des einfachen `rho~x^-3/2`-Profiles. Das ist jetzt die klar definierte verbleibende Daten-/Solverluecke.

## 9. A10-Status

```text
outer Fe/Fe-Ni transport calibration: PASS / literature grounded
QMD-domain mapping onto Earth reduced path: CALCULATED
QMD-shell optical-depth bound: CALCULATED
inner QMD-normalized OCP/EPT-like envelope: CALCULATED SENSITIVITY
permanent ballistic escape in tested envelope: NOT SUPPORTED
M>=1e11 reduced supply-processing capacity: CONFIRMED
M=1e10 backpressure sensitivity: CONFIRMED
full first-principles WDM transport closure: OPEN
final species-resolved Mdot_BH: OPEN
```

## 10. Naechster Block

Der naechste sinnvolle Schritt ist nicht mehr ein weiterer freier Transportfaktor, sondern

```text
Stage 3.69G / A11:
EOS/ionization table construction
+ time-dependent partial-sink Bondi/WDM PDE
+ energy equation
+ charge/composition advection
+ A4/A5 capture boundary
-> dynamically generated backpressure
-> tighter Mdot_BH band.
```

A11 muss insbesondere testen, ob der `1e10 kg`-Rand einen stabilen backpressure-regulierten Zustand bildet und ob der `>=1e11 kg`-Supply-processing-Branch im zeitabhaengigen Modell bestehen bleibt.

## Referenzen

- C. Wang et al., *Quantum molecular dynamics study of warm dense iron*, Phys. Rev. E 89, 023101 (2014), DOI: 10.1103/PhysRevE.89.023101.
- A. Blanchet et al., *First-principles molecular-dynamics equation of state of liquid to dense plasma iron*, Phys. Rev. E 111, 015206 (2025), DOI: 10.1103/PhysRevE.111.015206.
- D. Alfe, G. Kresse, M. J. Gillan, *Structure and dynamics of liquid iron under Earth's core conditions*, Phys. Rev. B 61 (2000).
- *Ab initio determination on diffusion coefficient and viscosity of FeNi fluid under Earth's core condition*, Scientific Reports 12 (2022).
- S. D. Baalrud & J. Daligault, *Effective Potential Theory for Transport Coefficients across Coupling Regimes*, Phys. Rev. Lett. 110, 235001 (2013).
- L. J. Babati et al., *Collisional stopping power of ions in warm dense matter*, Phys. Rev. E 113, 015201 (2026).
