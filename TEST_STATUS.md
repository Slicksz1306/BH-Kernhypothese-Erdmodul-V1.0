# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 26.08.2026  
**Forschungsstand:** bis Stage 3.69G/A-11 numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen

## Statusbegriffe

- **PASS** = definierter Solver-/Regression-/Konvergenztest bestanden; kein empirischer Nachweis.
- **CALCULATED** = definierter Benchmark numerisch berechnet.
- **FAIL** = konkret getesteter Branch/Mechanismus scheitert am verwendeten Test.
- **OPEN** = mit vorhandener Closure nicht abschliessend entschieden.
- **CORRECTED** = fruehere Zwischenannahme durch haerteren Test ersetzt.

## Branches

```text
H+ = Standard-Hawking
H0 = ohne Hawking
```

Beide bleiben parallel.

## Struktur / Makromodell

| Test | Status |
|---|---|
| starke Zentralmassenvariante | **FAIL** |
| Hard-Cavity/Hard-Replacement | **FAIL / verworfen** |
| kleiner smooth-compensated Branch | weiter getestet; kein eigener Makro-Ausschluss in reduzierten Modellen |
| vereinfachte Seismik/Normalmoden | kein robuster Ausschluss, kein positiver Nachweis |
| globale Waermeproxies | kein Ausschluss des getesteten kleinen Supply-Benchmarks |

## H+

```text
H+ Standard-Hawking:
FAIL im getesteten Greybody/SK-IV-Projekt-Reinterpretationsmodell.
```

Keine offizielle Super-K-Erdzentrum-BH-Exklusion wird behauptet.

## Stage 3.69 Materie-/Capture-/Transportstack

| Teiltest | Status |
|---|---|
| Schwarzschild-Dirac radial solver | **PASS als Solver-/Regressionstest** |
| Horizon/current conservation | **PASS** |
| In/Out matching | **PASS an getesteten Benchmarks** |
| Low-alpha externe Dirac-Regression | **PASS** |
| Earth-speed Protonenscan `1e10...5e11 kg` | **CALCULATED** |
| `M=1e11 kg` neutraler Protonenwert | **CALCULATED: ~0.9503 classical** |
| charged Proton Dirac `Q=0...24e` | **PARTIAL PASS / CALCULATED** |
| charged Electron Coulomb-Fernfeld | **OPEN** |
| Fe-56/Ni-58 `0+` scalar/KG solver | **PASS low-alpha regression** |
| Fe-56 coherent capture @`1e11 kg` | **CALCULATED: ~0.99754 classical** |
| Ni-58 coherent capture @`1e11 kg` | **CALCULATED: ~0.99646 classical** |
| grosse Wave-Suppression bei `1e11 kg` | **NOT FOUND** |
| dense charge-screening scale | **CALCULATED als atomic/sub-nm proxy** |
| ungescreenter `r_B`-weiter Coulombblocker | **NOT SUPPORTED** |
| Single-pass `p` als automatische Netto-Mdot-Fraktion | **CORRECTED / REJECTED** |
| repeated-encounter formula `chi=p/(p+e)` | **DONE** |
| strong-coupling radial Knudsen scaling | **CALCULATED** |
| early weak-Spitzer switch ohne `Gamma<<1` | **NOT JUSTIFIED** |
| 1-D absorbing Bondi PDE | **PASS benchmark auf Prozentniveau** |
| reflecting/backpressure PDE | **CALCULATED; outward shock demonstrated** |
| prompt one-pass weak equilibrium/neutronization | **NOT SUPPORTED** |

## A9 – Residence/Recycling Reduced Closure

A9 koppelt repeated encounters, permanenten Escape, Reservoir-Processing, Plasmaresponse und Weak-Reaction-Gates.

```text
chi_capture = p/(p+e_perm)
```

Massensplit:

```text
M=1e10 kg: transition-/backpressure-sensitive
M=1e11 kg: supply-processing capable im getesteten strong-coupling bracket
M=2e11 kg: klare Processing-Reserve
M=5e11 kg: sehr grosse Processing-Reserve.
```

Bei `M=1e11 kg` und `r_t=3e-11...2e-10 m`:

```text
Xi_high ~0.0079 ... 0.905.
```

Promptes Weak-Equilibrium bleibt im schnellen Branch nicht gestuetzt.

## A10 – First-Principles-Informed WDM Transport Envelope

Publizierte Fe-QMD-/EOS-Daten wurden auf den Reduced Earth path abgebildet.

Direkte Datenbereiche:

```text
WDM Fe QMD transport: rho~12.5...25 g/cm3, T~0.5...15 eV
2025 Fe first-principles EOS: rho~7.874...47.2 g/cm3, T~5500 K...1e9 K.
```

Der direkt QMD-kalibrierte aeussere Shell ist bereits stark optisch dick.

Schnellstes / escape-freundlichstes A10-Envelope:

```text
M=1e10 kg: tau_total~1.92e2, Xi_high~1.47
M=1e11 kg: tau_total~1.93e3, Xi_high~2.81e-3
M=2e11 kg: tau_total~3.86e3, Xi_high~4.28e-4
M=5e11 kg: tau_total~9.66e3, Xi_high~3.54e-5.
```

Damit gilt:

```text
local Kn~1 != permanent escape through the outer Fe/WDM reservoir.
```

A10 reproduziert den A9-Massensplit, bleibt aber wegen fehlender voller `Zbar/EOS/transport`-Abdeckung **PARTIAL FIRST-PRINCIPLES-INFORMED**.

## A11 – Time-Dependent Partial-Sink PDE

A11 testet den A9/A10-Split erstmals dynamisch mit einem sphärischen Finite-Volume-HLL-Solver.

### Regression / Conservation

```text
absorbing Bondi: PASS auf Prozentniveau
reflecting boundary: Backpressure/outward shock reproduziert
partial sink: implementiert
mass residual: ~1e-16 ... few 1e-15
energy audit residual: ~1e-16 ... few 1e-15.
```

### Fe-like Sensitivitaet

`A=0.99754` wird nur als Sensitivitaet verwendet, **nicht** mit der A5-Cross-Section gleichgesetzt.

Bei `gamma=1.5` bleibt dieser Lauf praktisch auf dem voll absorbierenden Ast.

### Dynamischer Massensplit

Aus A10 wird als Transport-Capacity-Sensitivitaet

```text
A_cap=min(1,1/Xi_high)
```

verwendet.

Damit:

```text
1e10 kg, fast-envelope high-supply:
    Xi_high~1.468 -> A_cap~0.681
    -> dynamischer Backpressure-Zweig entsteht
    -> innerer Flux stark reduziert

>=1e11 kg:
    Xi_high<<1 -> A_cap=1
    -> PDE bleibt auf absorbierendem/supply-processing Ast.
```

Der A9/A10-Massensplit wird damit **dynamisch reproduziert**.

### Offene A11-Konvergenz

Der `1e10 kg / A~0.681` Shockbranch ist in der Regimeentscheidung stabil, aber die exakte Endrate noch nicht gitterkonvergiert.

Bei `gamma=1.5`, `t=0.6 r_B/c_inf`:

```text
N=80  -> inner flux ~0.027
N=120 -> ~0.025
N=160 -> ~0.023
N=200 -> ~0.021
N=240 -> ~0.019.
```

Daher:

```text
A11 dynamic regime split: CALCULATED
A11 exact 1e10 shock-branch Mdot: OPEN
full tabulated WDM EOS/Zbar PDE: OPEN.
```

## Wichtige Korrekturen

```text
Bondi/Michel = automatisch Horizon-Mdot -> CORRECTED
One-pass loss-cone fraction = permanente Mdot suppression -> CORRECTED
Fe/Ni als Spin-1/2 Dirac -> CORRECTED to scalar/composite 0+
Unruh proton low-E extrapolation at alpha~0.353 -> REPLACED by full Dirac result
A6 r_coll~lambda_geom collisionless shortcut -> CORRECTED in A7
sonic point prevents all long-term feedback -> CORRECTED; shock/backpressure can propagate outward
EC threshold open -> instant NSE/neutronization -> CORRECTED
small one-pass p -> stationary chi=p -> CORRECTED by A9 repeated-encounter closure
local Kn=1 -> permanent outer escape -> REJECTED by A10 optical-depth audit
capacity deficit -> static arbitrary suppression -> REPLACED by A11 dynamic backpressure test.
```

## Formation

| Mechanismus | Status |
|---|---|
| In-situ-Kollaps normaler Erdmaterie | **FAIL** |
| spaeter direkter Earth-Capture | **FAIL** |
| Proto-Earth-/Planetesimal-Standardcapture | **FAIL** |
| normaler Halo -> cold disk delivery | **stark negativ / FAIL unter getesteten Standardbedingungen** |
| cold/co-moving Anfangsbedingung | mathematisch moeglich, Herkunft **OPEN** |

## Aktuelle Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| kleiner smooth Erdbranch | kein eigener Struktur-Ausschluss | kein eigener Struktur-Ausschluss |
| Hawking-Neutrinotest | **FAIL im Projektmodell** | nicht anwendbar |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Charge-/Screening-Subtests | teilweise berechnet | teilweise berechnet |
| A9 Residence/Recycling | **CALCULATED** | **CALCULATED** |
| A10 WDM transport envelope | **PARTIAL CALCULATED** | **PARTIAL CALCULATED** |
| A11 dynamic partial-sink PDE | **PARTIAL CALCULATED** | **PARTIAL CALCULATED** |
| `>=1e11 kg` current Reduced transport branch | supply-processing / absorbing dynamic branch | supply-processing / absorbing dynamic branch |
| `1e10 kg` current Reduced transport branch | dynamic backpressure possible / exact Mdot OPEN | dynamic backpressure possible / exact Mdot OPEN |
| finale Full-WDM species-resolved `Mdot` | **OPEN** | **OPEN** |
| Formation | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## Naechster Block

```text
Stage 3.69H / A12:
tabulated Fe/Ni EOS + Zbar
+ thermal conductivity / viscosity / relaxation
+ species/charge advection
+ high-resolution shock convergence
-> dynamic Mdot band with explicit EOS uncertainty.
```

## Schluss

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell.
H0: OPEN / nicht nachgewiesen.
A9-A11: >=1e11 kg bleibt im aktuellen Reduced Matter-Branch supply-processing/absorbing.
1e10 kg: dynamischer Backpressure-Zweig moeglich; exakte Endrate noch OPEN.
Full-WDM EOS/Zbar/dissipative transport: OPEN.
Formation: stark negativ.
Empirischer Erdzentrum-BH-Nachweis: keiner.
```
