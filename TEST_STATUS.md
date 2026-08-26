# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 26.08.2026  
**Forschungsstand:** Stage 3.69 bis A12c partiell numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen

## Statusbegriffe

- **PASS** = definierter Solver-/Regression-/Konvergenztest bestanden; kein empirischer Nachweis.
- **CALCULATED** = definierter Benchmark numerisch berechnet.
- **PARTIAL** = ein kontrollierter Unterblock ist gerechnet, aber die volle Closure fehlt.
- **FAIL** = konkret getesteter Branch/Mechanismus scheitert am verwendeten Test.
- **OPEN** = mit vorhandener Closure nicht abschliessend entschieden.
- **CORRECTED** = fruehere Zwischenannahme durch haerteren Test ersetzt.

## Branches

```text
H+ = Standard-Hawking
H0 = ohne Hawking
```

Beide bleiben getrennt und parallel.

# Struktur / Makromodell

| Test | Status |
|---|---|
| starke Zentralmassenvariante | **FAIL** |
| Hard-Cavity/Hard-Replacement | **FAIL / verworfen** |
| kleiner smooth-compensated Branch | kein eigener Makro-Ausschluss in reduzierten Modellen |
| vereinfachte Seismik/Normalmoden | kein robuster Ausschluss, kein positiver Nachweis |
| direkte experimentelle Detektion | **keine** |
| eindeutige positive Signatur | **keine** |

# H+

```text
H+ Standard-Hawking:
FAIL im getesteten Greybody/SK-IV-Projekt-Reinterpretationsmodell.
```

Keine offizielle Super-K-Erdzentrum-BH-Exklusion wird behauptet.

# Stage 3.69 Capture-/Transportstack

| Teiltest | Status |
|---|---|
| Schwarzschild-Dirac radial solver | **PASS als Solver-/Regressionstest** |
| Horizon/current conservation | **PASS** |
| In/Out matching | **PASS an getesteten Benchmarks** |
| Earth-speed Protonenscan `1e10...5e11 kg` | **CALCULATED** |
| `M=1e11 kg` neutraler Protonenwert | **~0.9503 classical** |
| charged Proton Dirac `Q=0...24e` | **PARTIAL / CALCULATED** |
| charged Electron Coulomb-Fernfeld | **OPEN** |
| Fe-56/Ni-58 `0+` scalar/KG solver | **PASS low-alpha regression** |
| Fe-56 coherent capture @`1e11 kg` | **~0.99754 classical** |
| Ni-58 coherent capture @`1e11 kg` | **~0.99646 classical** |
| grosse Wave-Suppression bei `1e11 kg` | **NOT FOUND** |
| dense charge-screening scale | **CALCULATED als atomic/sub-nm proxy** |
| ungescreenter `r_B`-weiter Coulombblocker | **NOT SUPPORTED** |
| Single-pass `p` als automatische Netto-Mdot-Fraktion | **CORRECTED / REJECTED** |
| repeated-encounter `chi=p/(p+e_perm)` | **DONE** |
| early weak-Spitzer switch ohne weak coupling | **NOT JUSTIFIED** |
| prompt one-pass weak equilibrium/neutronization | **NOT SUPPORTED** |

# A9 – Residence/Recycling

A9 koppelt Capture pro Encounter, permanenten Escape, Reservoir-Masse und Processing-Zeit.

Unter dem **historischen** Michel-Supply-Benchmark ergab sich:

```text
M=1e10 kg: transition-/backpressure-sensitive
M=1e11 kg: processing-capable im getesteten strong-coupling bracket
M=2e11 kg: klare Processing-Reserve
M=5e11 kg: grosse Processing-Reserve.
```

Diese Aussage wird ab A12c als **conditional on outer supply EOS** verstanden.

# A10 – First-Principles-Informed WDM Transport Envelope

Direkte Fe-QMD-/EOS-Daten wurden fuer den aeusseren Near-Zone-Shell verwendet; tiefere Bereiche bleiben extrapoliert.

Schnellstes/escape-freundlichstes Envelope unter dem historischen Supply:

```text
M=1e10 kg: tau_total~1.92e2, Xi_high~1.468
M=1e11 kg: tau_total~1.93e3, Xi_high~2.81e-3
M=2e11 kg: tau_total~3.86e3, Xi_high~4.28e-4
M=5e11 kg: tau_total~9.66e3, Xi_high~3.54e-5.
```

```text
local Kn~1 != permanent escape through the outer Fe/WDM reservoir.
```

Status: **PARTIAL FIRST-PRINCIPLES-INFORMED**.

# A11 – Dynamic Partial-Sink PDE

Finite-volume/HLL sphärischer Euler-Solver:

```text
absorbing Bondi regression: PASS auf Prozentniveau
reflecting boundary: outward backpressure/shock reproduced
mass residual: ~1e-16...few 1e-15
energy residual: ~1e-16...few 1e-15.
```

Fe-like `A=0.99754` Sensitivitaet bleibt praktisch absorbierend.

Mit dem aus dem historischen hohen Supply abgeleiteten `1e10 kg` Capacity-Limiter `A_cap~0.681` entsteht dynamischer Backpressure.

Status: **PARTIAL CALCULATED**.

# A12 – High-resolution Shock + Transportaudit

`1e10 kg`, historische Capacity-Randbedingung, `t=0.8 r_B/c_inf`:

```text
N=128  shock~1.269 r_B, inner flux~2.10e-2
N=256  shock~1.254 r_B, inner flux~1.63e-2
N=512  shock~1.233 r_B, inner flux~1.12e-2
N=1024 shock~1.229 r_B, inner flux~6.94e-3.
```

Shock-Lage konvergiert, eine stationaere endliche innere `Mdot` nicht.

Long-domain:

```text
t=0.8 -> shock~1.26 r_B
t=1.2 -> ~1.74 r_B
t=1.6 -> ~2.22 r_B
t=2.0 -> ~2.68 r_B.
```

Damit ist der getestete `1e10 kg`-Zweig ein **outward-propagating backpressure state**, keine nachgewiesene stationaere Shock-Endrate.

Transportaudit:

```text
1e10 kg: Re~32...98, Pe~8...11
1e11 kg: Re~322...985, Pe~82...106
2e11 kg: Re~644...1970, Pe~164...212
5e11 kg: Re~1610...4924, Pe~409...531.
```

# A12b – Zbar + Dissipation

More/Thomas-Fermi Fe-Closure mit Low-T-Korrekturfaktor `0.270`:

```text
rho=13.0885 g/cm3, T=6000 K -> Zbar~2.76.
```

Gegen eine publizierte solid-density Average-Atom-Definition liegt der Fit bei `0.1...10 eV` etwa `12...16 %` niedriger; `Zbar` wird daher als Modellband behandelt.

Literaturgebundene

```text
eta=8.5...26 mPa s
k=67...87 W/m/K
Cp~850 J/kg/K
```

wurden in einen Reduced dissipativen PDE-Sensitivitaetstest eingebaut. Unter der historischen `1e10 kg` Capacity-Randbedingung entfernen eta/k den Backpressure-Ast nicht.

Status: **PARTIAL CALCULATED**; thermodynamisch exakte Fe-EOS-PDE bleibt OPEN.

# A12c – Stiff-EOS relativistische Supply-Korrektur

Dies ist die wichtigste aktuelle Korrektur.

PREM Zentrum:

```text
rho~13.08848 g/cm3
Kappa_S~1.4253 TPa
P~363.852 GPa
dK/dP~2.356
c_s~10.4355 km/s.
```

Fuer `Gamma>5/3` wird der relativistische Michel-Kritikalitaetstest statt Newton-Bondi benutzt.

Bei `M=1e11 kg` im **konstanten-Gamma Sensitivitaetsscan**:

| Gamma | Mdot [kg/s] |
|---:|---:|
| `1.75` | `1.19e-7` |
| `1.80` | `2.89e-8` |
| `1.85` | `8.02e-9` |
| `2.00` | `3.35e-10` |
| `2.20` | `1.50e-11` |
| `2.356` local PREM proxy | `2.40e-12` |

Der historische Projekt-Supply

```text
1.47e-8...1.46e-7 kg/s @1e11 kg
```

entspricht im einfachen konstanten-Gamma GR-Surrogat etwa

```text
Gamma~1.743...1.826.
```

Daher:

```text
historical Michel supply:
CORRECTED -> LEGACY / EOS-SENSITIVE BENCHMARK.
```

Der lokale PREM-Wert `dK/dP~2.356` darf **nicht** als konstantes globales Gamma bis zum Horizon verwendet werden. Die `2.40e-12 kg/s` ist keine finale Endrate.

## Korrigierter 1e10-Status

Der fruehere Satz

```text
1e10 kg -> dynamic backpressure
```

war zu breit. Im konstanten-Gamma GR-Sensitivitaetsscan:

```text
Gamma=1.80  -> Xi~0.29
Gamma=1.85  -> Xi~0.081
Gamma=2.00  -> Xi~0.0034
Gamma=2.356 -> Xi~2.4e-5
Xi=1 threshold ~Gamma=1.756.
```

Aktueller Status:

```text
1e10 kg:
BACKPRESSURE CONDITIONAL ON SUPPLY EOS.
soft/high supply can overload the inner capacity;
stiff/lower supply can remove the overload.
```

## >=1e11 kg

```text
inner processing-capable result survives.
actual outer supply and final net Mdot are reopened as EOS-dependent.
```

Eine niedrigere stiff-EOS Supply-Rate vergroessert die Processing-Reserve.

# Wichtige Korrekturen

```text
Bondi/Michel = automatisch Horizon-Mdot -> CORRECTED
one-pass loss cone = stationary Mdot factor -> REJECTED
Fe/Ni as spin-1/2 Dirac -> CORRECTED to 0+ scalar/composite
Unruh proton extrapolation @alpha~0.353 -> REPLACED by full Dirac
A6 collisionless shortcut -> CORRECTED in A7
sonic point blocks all long-term feedback -> CORRECTED
EC threshold open = instant neutronization -> CORRECTED
local Kn=1 = permanent escape -> REJECTED by A10
capacity deficit = arbitrary static suppression -> REPLACED by dynamic PDE
1e10 always backpressure -> CORRECTED by A12c: conditional on supply EOS
historical Michel range = universal supply -> REJECTED / LEGACY EOS-SENSITIVE.
```

# Formation

| Mechanismus | Status |
|---|---|
| In-situ-Kollaps normaler Erdmaterie | **FAIL** |
| spaeter direkter Earth-Capture | **FAIL** |
| Proto-Earth-/Planetesimal-Standardcapture | **FAIL** |
| normaler Halo -> cold disk delivery | **stark negativ / FAIL unter getesteten Standardbedingungen** |
| cold/co-moving Anfangsbedingung | mathematisch moeglich, Herkunft **OPEN** |

# Aktuelle Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| kleiner smooth Erdbranch | kein eigener Struktur-Ausschluss | kein eigener Struktur-Ausschluss |
| Hawking-Neutrinotest | **FAIL im Projektmodell** | nicht anwendbar |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Charge-/Screening | teilweise berechnet | teilweise berechnet |
| A9 Processing/Residence | **CALCULATED Reduced** | **CALCULATED Reduced** |
| A10 WDM transport envelope | **PARTIAL** | **PARTIAL** |
| A11/A12 dynamic backpressure | **PARTIAL** | **PARTIAL** |
| A12b Zbar/eta/k sensitivity | **PARTIAL** | **PARTIAL** |
| historical Michel supply | **LEGACY / EOS-SENSITIVE** | **LEGACY / EOS-SENSITIVE** |
| `1e10 kg` capacity backpressure | conditional on EOS/supply | conditional on EOS/supply |
| `>=1e11 kg` inner processing | processing-capable in current models | processing-capable in current models |
| general-EOS outer supply | **OPEN** | **OPEN** |
| final species-resolved net Mdot | **OPEN** | **OPEN** |
| Formation | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

# Naechster Block

```text
Stage 3.69I / A13:
general/piecewise Fe/Ni EOS
+ relativistic variable-EOS Michel critical point
+ Mdot_supply(EOS) uncertainty band
+ recouple A9-A12 inner transport/capture
+ revised net Mdot band
+ rerun long-term/heat constraints.
```

# Schluss

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell.
H0: OPEN / nicht nachgewiesen.
Innerer Capture-/Transportblock: stark gehaertet.
Historischer Michel-Supply: nicht mehr als feste Rate akzeptiert.
1e10 backpressure: supply/EOS-dependent.
>=1e11 inner processing: bleibt robust im aktuellen Reduced Stack.
Finale general-EOS supply/net-Mdot: OPEN.
Formation: stark negativ.
Empirischer Erdzentrum-BH-Nachweis: keiner.
```
