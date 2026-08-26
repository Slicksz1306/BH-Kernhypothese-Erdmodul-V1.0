# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 26.08.2026  
**Forschungsstand:** bis Stage 3.69E/A-9 numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen

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

## Stage 3.69 Materie-/Capture-/Transportstack

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
| A9 collisional escape optical-depth proxy | **CALCULATED** |
| A9 reservoir processing capacity | **CALCULATED** |
| A9 critical transition radius / critical BH mass | **CALCULATED** |
| A9 plasma-response / bulk quasineutrality proxy | **CALCULATED** |
| A9 weak-reaction residence gate | **CALCULATED** |
| `M>=~1e11 kg` strong-coupling/recycling reduced branch | **SUPPLY-PROCESSING CAPABLE** |
| `M=1e10 kg` transport | **OPEN / BACKPRESSURE-SENSITIVE** |
| finale first-principles species-resolved `Mdot_BH` | **OPEN** |

## A9 – zentrale quantitative Closure

Bei repeated encounters gilt

```text
chi_capture = p/(p+e_perm).
```

Im A7/A9 strong-coupling/geometrischen Proxy wird fuer den permanenten ballistischen Escape

```text
e_perm ~ f(v>v_esc) exp(-tau_coll)
```

verwendet. Fuer die getesteten atomaren Transition-Skalen ist `tau_coll>>1`, so dass `e_perm` praktisch verschwindet und Misses rezykliert werden.

Fuer `M=1e11 kg` und `r_t=3e-11...2e-10 m`:

```text
Xi_high = Mdot_supply,high / Mdot_capacity
        ~0.0079 ... 0.905.
```

Damit benoetigt der aktuelle Reduced Strong-Coupling-Branch bei `1e11 kg` keinen zusaetzlichen Capture-Pile-up, um den historischen Michel-/Supply-Benchmark zu verarbeiten.

Massenscan:

```text
M=1e10 kg: transition-scale/backpressure sensitive
M=1e11 kg: supply-processing capable in tested strong-coupling bracket
M=2e11 kg: clear capacity reserve
M=5e11 kg: very large capacity reserve.
```

Kritischer Reduced-Uebergang:

```text
xcrit low  ~8.507e-3
xcrit high ~3.397e-3.
```

Fuer physikalische atomare Transition-Skalen `3e-11...2e-10 m` entspricht das grob

```text
Mcrit ~5.8e9 ... 9.6e10 kg.
```

## A9 – Weak-/Charge-Timescales

Bei `M=1e11 kg`:

```text
Ni-threshold:
    t_res ~9.13e-14 s
    lambda_required ~1.10e13 s^-1

Fe-threshold:
    t_res ~1.50e-17 s
    lambda_required ~6.69e16 s^-1.
```

Der publizierte schnelle `56Fe`-Vergleichswert bei `rho*Ye=1e11 g/cm^3, T9=3`

```text
lambda_ec ~1.5916e4 s^-1
```

liegt viele Groessenordnungen darunter.

```text
prompt weak equilibrium / one-pass neutronization: NOT SUPPORTED
```

im schnellen supply-processing Branch.

Die Elektronen-Plasmaantwort ist wesentlich schneller als die Reduced Residence-Zeit; bulk-quasineutraler Transport ist deshalb als Reduced Closure motiviert. Der diskrete BH-Charge-State bleibt trotzdem nicht exakt geloest.

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
| A9 Residence/Recycling Reduced Closure | **CALCULATED** | **CALCULATED** |
| `>=~1e11 kg` Strong-Coupling Transport | supply-processing capable | supply-processing capable |
| `1e10 kg` Transport | OPEN / backpressure-sensitive | OPEN / backpressure-sensitive |
| Prompt weak equilibrium | not supported in fast branch | not supported in fast branch |
| finale First-Principles Dense-Matter-`Mdot` | **OPEN** | **OPEN** |
| Formation | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## Naechster Block

```text
Stage 3.69F / A-10:
first-principles-informed WDM transport
+ time-dependent hydro/kinetic sink coupling
+ absorptive A4/A5 inner boundary
-> replace geometric mean-free-path proxy
-> e_perm(r,E,species)
-> final reduced species-resolved Mdot band.
```

## Schluss

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell.
H0: OPEN / nicht nachgewiesen.
Materie-Capture-Wellenblock: stark gehaertet; keine grosse Wave-Suppression bei 1e11 kg gefunden.
A9: fuer >=~1e11 kg ist der aktuelle strong-coupling/recycling Reduced Branch supply-processing capable.
1e10 kg: weiterhin backpressure-/transition-sensitive.
Finale Unsicherheit: first-principles WDM Transport/EOS + gekoppelte Hydro/Kinetik.
Formation: stark negativ.
Empirischer Erdzentrum-BH-Nachweis: keiner.
```
