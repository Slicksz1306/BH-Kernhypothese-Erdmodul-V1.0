# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 26.08.2026  
**Forschungsstand:** bis Stage 3.69D/A-8 numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen

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
| `r_s`, `r_B`, `r_rep` getrennt | **DONE** |
| vereinfachte Seismik/Normalmoden | kein robuster Ausschluss, kein positiver Nachweis |
| globale Waermeproxies | kein Ausschluss des getesteten kleinen Supply-Benchmarks |

## H+

```text
H+ Standard-Hawking:
FAIL im getesteten Greybody/SK-IV-Projekt-Reinterpretationsmodell.
```

Keine offizielle Super-K-Erdzentrum-BH-Exklusion wird behauptet.

## Stage 3.69 Materie-/Capture-Stack

| Teiltest | Status |
|---|---|
| Schwarzschild-Dirac radial solver | **PASS als Solver-/Regressionstest** |
| Horizon/current conservation | **PASS** |
| In/Out matching | **PASS an getesteten Benchmarks** |
| Low-alpha externe Dirac-Regression | **PASS** |
| Intermediate-alpha Doran-Struktur | **PASS qualitativ/numerisch** |
| Earth-speed Protonenscan `1e10...5e11 kg` | **CALCULATED** |
| `M=1e11 kg` neutraler Protonenwert | **CALCULATED: ~0.9503 classical** |
| charged Proton Dirac `Q=0...24e` | **PARTIAL PASS / CALCULATED** |
| charged Electron Coulomb-Fernfeld | **OPEN** |
| Fe-56/Ni-58 korrekter `0+` scalar/KG solver | **PASS low-alpha regression** |
| Fe-56 coherent capture @`1e11 kg` | **CALCULATED: ~0.99754 classical** |
| Ni-58 coherent capture @`1e11 kg` | **CALCULATED: ~0.99646 classical** |
| grosse Wave-Suppression bei `1e11 kg` | **NOT FOUND** |
| dense charge-screening scale | **CALCULATED als atomic/sub-nm proxy** |
| ungescreenter `r_B`-weiter Coulombblocker | **NOT SUPPORTED** |
| Single-pass `p` als automatische Netto-Mdot-Fraktion | **CORRECTED / REJECTED** |
| repeated-encounter formula `chi=p/(p+e)` | **DONE** |
| strong-coupling radial Knudsen scaling | **CALCULATED: Kn decreases inward** |
| early weak-Spitzer switch ohne `Gamma<<1` | **NOT JUSTIFIED** |
| 1-D absorbing Bondi PDE | **PASS benchmark auf Prozentniveau** |
| reflecting/backpressure PDE | **CALCULATED; outward shock demonstrated** |
| relativistische Elektronendegeneration | **CALCULATED** |
| `58Ni` EC energetic threshold | **CALCULATED** |
| `56Fe` EC energetic threshold | **CALCULATED** |
| prompt one-pass weak equilibrium/neutronization | **NOT SUPPORTED** |
| residence/backpressure + weak-network closure | **OPEN** |
| finale species-resolved `Mdot_BH` | **OPEN** |

## Wichtige Korrekturen

```text
Bondi/Michel = automatisch Horizon-Mdot -> CORRECTED
One-pass loss-cone fraction = permanente Mdot suppression -> CORRECTED
Fe/Ni als Spin-1/2 Dirac -> CORRECTED to scalar/composite 0+
Unruh proton low-E extrapolation at alpha~0.353 -> REPLACED by full Dirac result
A6 r_coll~lambda_geom collisionless shortcut -> CORRECTED in A7
sonic point prevents all long-term feedback -> CORRECTED; shock/backpressure can propagate outward
EC threshold open -> instant NSE/neutronization -> CORRECTED
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
| Recycling/Backpressure-Regime | reduziert eingegrenzt | reduziert eingegrenzt |
| Prompt weak equilibrium | nicht supported | nicht supported |
| finale Residence+Weak-Network `Mdot` | **OPEN** | **OPEN** |
| Formation | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## Naechster Block

```text
Stage 3.69E / A-9:
residence-time/backpressure transport
+ charge-neutrality closure
+ minimal Fe/Ni weak network
-> chi_transport
-> net Mdot_BH
```

## Schluss

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell.
H0: OPEN / nicht nachgewiesen.
Materie-Capture-Wellenblock: stark gehaertet; keine grosse Wave-Suppression bei 1e11 kg gefunden.
Entscheidende Restunsicherheit: Residence/Recycling/Backpressure + weak-network transport closure.
Formation: stark negativ.
Empirischer Erdzentrum-BH-Nachweis: keiner.
```
