# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 26.08.2026  
**Forschungsstand:** Stage 3.69 bis A13 partiell numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen

## Statusbegriffe

- **PASS** = definierter Solver-/Regression-/Konvergenztest bestanden; kein empirischer Nachweis.
- **CALCULATED** = definierter Benchmark numerisch berechnet.
- **PARTIAL** = kontrollierter Unterblock gerechnet, volle physische Closure fehlt.
- **FAIL** = konkret getesteter Branch scheitert am verwendeten Test.
- **OPEN** = mit vorhandener Closure nicht abschliessend entschieden.
- **CORRECTED** = fruehere Zwischenannahme durch haerteren Test ersetzt.

## Branches

```text
H+ = Standard-Hawking
H0 = ohne Hawking
```

H+ Standard-Hawking bleibt **FAIL im getesteten Projekt-SK-IV-Reinterpretationsmodell**. H0 bleibt OPEN. Keine offizielle Super-K-Erdzentrum-BH-Exklusion wird behauptet.

# Struktur / Makromodell

| Test | Status |
|---|---|
| starke Zentralmassenvariante | **FAIL** |
| Hard-Cavity/Hard-Replacement | **FAIL / verworfen** |
| kleiner smooth-compensated Branch | kein eigener Makro-Ausschluss in reduzierten Modellen |
| vereinfachte Seismik/Normalmoden | kein robuster Ausschluss, kein positiver Nachweis |
| direkte experimentelle Detektion | **keine** |
| eindeutige positive Signatur | **keine** |

# Capture-/Transportstack A1-A12

| Teiltest | Status |
|---|---|
| Schwarzschild-Dirac solver / current / matching | **PASS an definierten Regressionen** |
| Earth-speed Protonenscan `1e10...5e11 kg` | **CALCULATED** |
| Proton @`1e11 kg` | `~0.9503 classical` |
| charged Proton `Q=0...24e` | **PARTIAL / CALCULATED** |
| charged Electron Coulomb-Fernfeld | **OPEN** |
| Fe-56/Ni-58 `0+` scalar/KG | **PASS Regression / CALCULATED** |
| Fe-56 @`1e11 kg` | `~0.99754 classical` |
| Ni-58 @`1e11 kg` | `~0.99646 classical` |
| grosse Wave-Suppression @`1e11 kg` | **NOT FOUND** |
| repeated encounter `chi=p/(p+e_perm)` | **DONE** |
| local `Kn~1` = permanent escape | **REJECTED by A10** |
| prompt one-pass neutronization | **NOT SUPPORTED** |
| A11/A12 dynamic backpressure PDE | **PARTIAL CALCULATED** |
| A12 shock-position convergence to N=1024 | **CALCULATED** |
| stationary finite 1e10 shock-Mdot | **NOT ESTABLISHED** |
| A12b More/TF Fe `Zbar` | **PARTIAL CALCULATED** |
| A12b physical eta/k sensitivity | **PARTIAL CALCULATED** |

# A12c – Supply-Korrektur

Der historische Projekt-Supply

```text
M=1e11 kg:
1.47e-8 ... 1.46e-7 kg/s
```

ist ab A12c **LEGACY / EOS-SENSITIVE**, keine universelle Rate.

Constant-Gamma relativistische Sensitivitaet:

```text
Gamma=1.75  -> 1.19e-7 kg/s
Gamma=1.80  -> 2.89e-8
Gamma=1.85  -> 8.02e-9
Gamma=2.00  -> 3.35e-10
Gamma=2.20  -> 1.50e-11
Gamma=2.356 -> 2.40e-12  [local PREM stiffness stress limit only]
```

```text
1e10 always backpressure -> CORRECTED:
backpressure is conditional on outer supply EOS.
```

# A13 – General-EOS relativistischer Michel-Supply

A13 implementiert die stationaeren Schwarzschild/Michel-Gleichungen fuer eine allgemeine thermodynamisch konsistente barotrope/isentrope EOS.

```text
4 pi r^2 rho0 u = Mdot
h sqrt(1 - 2M/r + u^2) = h_inf
```

Kritischer Punkt:

```text
u_s^2 = a_s^2/(1+3 a_s^2)
r_s/M = (1+3 a_s^2)/(2 a_s^2)
h_s/sqrt(1+3 a_s^2) = h_inf.
```

## A13 Regression

Constant-stiffness Regression gegen A12c bei `M=1e11 kg`:

```text
beta=1.50  relative drift ~8.7e-5
beta=1.80  ~3.1e-5
beta=2.00  ~2.5e-5
beta=2.356 ~1.8e-5.
```

```text
A13 general-EOS solver regression: PASS
```

## A13 variable-EOS surrogate

PREM `P`, `K_S`, `dK/dP` werden am Aussenrand gematched. Local PREM stiffness wird nur bis `30...47.2 g/cm3` gehalten. Danach:

```text
beta_mid=1.4...1.8
rho_rel transition sensitivity=1e5...1e7 g/cm3
inner beta=4/3.
```

Das ist ein kontrollierter Surrogat-Sensitivitaetsscan, **kein finales Fe/Ni-Konfidenzintervall**.

Bei `M=1e11 kg`:

```text
Mdot_supply,surrogate ~4.64e-8 ... 1.37e-6 kg/s.
```

Damit wird A12c praezisiert:

```text
constant PREM stiffness to horizon -> STRESS LIMIT ONLY
variable EOS softening -> supply can return to historical range or above.
```

## A13 recoupling to A10 capacity

| M_BH | Xi_min | Xi_max | Status im getesteten Surrogat |
|---:|---:|---:|---|
| `1e10` | `0.467` | `13.76` | **EOS/SUPPLY CONDITIONAL** |
| `1e11` | `8.94e-4` | `2.64e-2` | **PROCESSING-CAPABLE** |
| `2e11` | `1.36e-4` | `4.01e-3` | **PROCESSING-CAPABLE** |
| `5e11` | `1.12e-5` | `3.32e-4` | **PROCESSING-CAPABLE** |

```text
M>=1e11 kg:
processing-capable result survives robustly across the controlled A13 surrogate.

M=1e10 kg:
Xi crosses 1; backpressure remains EOS/supply conditional.
```

# A13b real-data status

Grant et al. 2021 report liquid-Fe elevated isentrope measurements `~275...400 GPa`, excellent agreement with SESAME 92141 and public supporting data at Zenodo DOI `10.5281/zenodo.4464112`.

The paper reports fit parameters:

```text
K0=25.3 +/-4.0 GPa
K0'=6.60 +/-0.33
gamma0=2.42 +/-0.12
rho0=5.187 g/cm3 reference.
```

The Zenodo dataset was not reliably machine-retrievable in the current run. No data were fabricated/digitized from figures.

```text
real tabulated liquid-Fe isentrope ingestion: OPEN
final physical Mdot_supply uncertainty band: OPEN
```

# Wichtige Korrekturen

```text
Bondi/Michel = automatically horizon Mdot -> CORRECTED
one-pass loss cone = stationary suppression -> REJECTED
Fe/Ni spin-1/2 -> CORRECTED to 0+ scalar/composite proxy
sonic point blocks long-term feedback -> CORRECTED
EC threshold = instant neutronization -> CORRECTED
local Kn=1 = permanent escape -> REJECTED
1e10 always backpressure -> CORRECTED: conditional on EOS/supply
historical Michel range = universal supply -> REJECTED / LEGACY
constant PREM stiffness to horizon = preferred supply -> REJECTED / stress limit only.
```

# Formation

| Mechanismus | Status |
|---|---|
| In-situ-Kollaps normaler Erdmaterie | **FAIL** |
| spaeter direkter Earth-Capture | **FAIL** |
| Proto-Earth-/Planetesimal-Standardcapture | **FAIL** |
| normaler Halo -> cold disk delivery | **stark negativ / FAIL unter getesteten Bedingungen** |
| cold/co-moving Anfangsbedingung | mathematisch moeglich, Herkunft **OPEN** |

# Aktuelle Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| kleiner smooth Erdbranch | kein eigener Struktur-Ausschluss | kein eigener Struktur-Ausschluss |
| Hawking-Neutrinotest | **FAIL im Projektmodell** | nicht anwendbar |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Charge-/Screening | teilweise berechnet | teilweise berechnet |
| A9-A12 inner processing | **stark gehaertet / PARTIAL** | **stark gehaertet / PARTIAL** |
| A13 general-EOS machinery | **PASS regression / PARTIAL physical** | **PASS regression / PARTIAL physical** |
| A13 variable-EOS surrogate | **CALCULATED** | **CALCULATED** |
| `1e10 kg` capacity/backpressure | EOS/supply conditional | EOS/supply conditional |
| `>=1e11 kg` inner processing | robust in tested A13 surrogate | robust in tested A13 surrogate |
| real tabulated Fe/Ni supply | **OPEN** | **OPEN** |
| charged-electron closure | **OPEN** | **OPEN** |
| final species-resolved net Mdot | **OPEN** | **OPEN** |
| Formation | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

# Naechster Pflichtblock

```text
A13b:
public liquid-Fe isentrope / SESAME-consistent data ingestion
-> thermodynamic h(rho) reconstruction
-> general-EOS Michel directly on data
-> final outer-supply bracket
-> recouple A9-A12
-> rerun heat/age constraints.
```

Danach bleiben charged-electron closure, finale Full-WDM/net-Mdot Closure und Stage 3.70 Real-Data-Falsifikation.
