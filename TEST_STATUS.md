# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 29.08.2026  
**Forschungsstand:** Reduced/partial numerischer Stack bis A19; Stage 3.69 Full-Multiphysics nicht final geschlossen; Stage 3.70 Real-Data-Audit partiell durchgeführt

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

H+ bleibt **FAIL in der projektinternen Reinterpretation des staerksten publizierten SK-IV-Hochenergie-Binlimits**. Die standalone SK-Gd-2026-Limits in demselben Bin sind schwaecher und wuerden den Projektproxy allein nicht ausschliessen. Es wird keine offizielle Super-K-Erdzentrum-BH-Exklusion behauptet.

H0 bleibt **OPEN / nicht nachgewiesen**.

# 1. Struktur / Makromodell

| Test | Status |
|---|---|
| starke Zentralmassenvariante | **FAIL** |
| Hard-Cavity/Hard-Replacement | **FAIL / verworfen** |
| kleiner smooth-compensated Branch | kein eigener Makro-Ausschluss in reduzierten Modellen |
| direkte r_B-Skalen-Seismik | **kein sinnvoller Beobachtungskanal** |
| makroskopische Seismik/Normalmoden | **OPEN – finaler delta-rho/delta-Vp/delta-Vs-Output fehlt** |
| direkte experimentelle Detektion | **keine** |
| eindeutige positive Signatur | **keine** |

# 2. Capture-/Transportstack A1-A12

| Teiltest | Status |
|---|---|
| Schwarzschild-Dirac solver / current / matching | **PASS an definierten Regressionen** |
| Earth-speed Protonenscan `1e10...5e11 kg` | **CALCULATED** |
| Proton @`1e11 kg` | `~0.9503 classical` |
| charged Proton `Q=0...24e` | **PARTIAL / CALCULATED** |
| Fe-56/Ni-58 `0+` scalar/KG | **PASS Regression / CALCULATED** |
| Fe-56 @`1e11 kg` | `~0.99754 classical` |
| Ni-58 @`1e11 kg` | `~0.99646 classical` |
| grosse Wave-Suppression @`1e11 kg` | **NOT FOUND** |
| repeated encounter `chi=p/(p+e_perm)` | **DONE** |
| local `Kn~1` = permanent escape | **REJECTED by A10** |
| prompt one-pass neutronization | **NOT SUPPORTED** |
| A11/A12 dynamic backpressure PDE | **PARTIAL CALCULATED** |
| A12 shock-position convergence to N=1024 | **CALCULATED** |
| stationary finite `1e10 kg` shock-Mdot | **NOT ESTABLISHED** |
| A12b More/TF Fe `Zbar` | **PARTIAL CALCULATED** |
| A12b physical eta/k sensitivity | **PARTIAL CALCULATED** |

# 3. A12c / A13 – relativistischer Outer Supply

Der historische Projekt-Supply

```text
M=1e11 kg:
1.47e-8 ... 1.46e-7 kg/s
```

ist **LEGACY / EOS-SENSITIVE**, keine universelle Rate.

A13 implementiert die stationaere allgemeine EOS-Michel-Kritikalitaet:

```text
4 pi r^2 rho0 u = Mdot
h sqrt(1 - 2M/r + u^2) = h_inf

u_s^2 = a_s^2/(1+3 a_s^2)
r_s/M = (1+3 a_s^2)/(2 a_s^2)
h_s/sqrt(1+3 a_s^2) = h_inf.
```

Constant-stiffness Regression gegen A12c: **PASS**, relativer Drift `~1e-4` oder besser.

A13 variable-EOS Surrogat bei `M=1e11 kg`:

```text
Mdot_supply ~4.64e-8 ... 1.37e-6 kg/s.
```

Dies war ein kontrollierter Sensitivitaetsscan, kein finales Fe/Ni-Konfidenzintervall.

# 4. A13b – Grant-2021 experimentell gefitteter Fe-Outer-Anker

A13b implementiert die publizierte analytische Liquid-Fe-EOS-Fitform von Grant et al. (2021) als experimentell verankerten Outer-Abschnitt bis `400 GPa`.

Publizierte Fitparameter:

```text
K0      = 25.3 +/-4.0 GPa
K0'     = 6.60 +/-0.33
rho0    = 5.187 g/cm3
gamma0  = 2.42 +/-0.12.
```

Am PREM-Zentrumsrand reproduziert der nominale Grant-Pfad den Bulkmodul auf etwa `0.4 %`:

```text
B_Grant ~1.419 TPa
K_PREM  ~1.425 TPa.
```

Nominaler Grant-fit-anchored Sensitivitaetsbereich bei `1e11 kg`:

```text
Mdot_supply ~1.29e-7 ... 3.80e-6 kg/s.
```

Konservativer Fitparameter/T/Intermediate-EOS-Corner-Scan:

```text
Mdot_supply ~8.27e-8 ... 6.13e-6 kg/s.
```

Status:

```text
A13b empirical-fit outer closure: PARTIAL CALCULATED
raw Zenodo pressure-density traces: OPEN
direct SESAME-92141 table ingestion: OPEN
final physical Mdot_supply uncertainty band: OPEN.
```

# 5. A14 – Dense-core charged-electron screening

Diffuse equal-T Plasmaformel bei `1e11 kg`:

```text
Q_eq,diffuse ~+24.18 e.
```

Im dichten/entarteten Fe-Elektronengas ergibt der Thomas-Fermi-Screening-Proxy ueber `Zbar~2.76...26`:

```text
E_F       ~19.4 ... 86.6 eV
lambda_TF ~4.29e-11 ... 2.95e-11 m.
```

Ein screened Potential-Energie-Bracket liefert eine bevorzugte Dense-Core-Chargeskala von grob

```text
Q ~ O(1...5 e).
```

Recoupling an A4 Proton-Dirac:

```text
Q~+1.6e -> ~0.925 classical
Q~+4.9e -> ~0.867 classical.
```

```text
large electrostatic proton blocker: NOT FOUND
full screened Coulomb-Dirac electron S-matrix: OPEN refinement.
```

# 6. A15 – Integrated Reduced Net-Throughput Audit

A13b Grant-fit Supply recoupled an A10 fast-envelope Processing-Capacity:

| M_BH | Xi_min | Xi_max | Status |
|---:|---:|---:|---|
| `1e10` | `0.832` | `61.60` | **SUPPLY/EOS + BACKPRESSURE CONDITIONAL** |
| `1e11` | `1.59e-3` | `1.18e-1` | **PROCESSING-CAPABLE in tested stack** |
| `2e11` | `2.42e-4` | `1.80e-2` | **PROCESSING-CAPABLE** |
| `5e11` | `2.00e-5` | `1.48e-3` | **PROCESSING-CAPABLE** |

Wichtig:

```text
single-pass capture != stationary throughput.
```

A6/A9 repeated encounters:

```text
chi_capture = p/(p+e_perm).
```

Bei optisch dickem Reservoir und kleinem permanenten Escape darf Fe/Ni single-pass capture nicht einfach einmal auf den Supply multipliziert werden.

```text
M>=1e11 kg:
inner reduced processing is not the bottleneck in tested A13b stack.

M=1e10 kg:
time-dependent backpressure remains decisive.

final Full-WDM species-resolved Mdot_BH:
OPEN.
```

# 7. A16 – aktualisierter Waerme-/Alterstest

Globale Oberflaechen-Waermefluss-Vergleichsskala:

```text
47 +/-2 TW.
```

A13b `eta=1` momentane Restmassenleistung:

| M_BH | P_min [TW] | P_max [TW] |
|---:|---:|---:|
| `1e10` | `7.43e-5` | `5.51e-3` |
| `1e11` | `7.43e-3` | `0.551` |
| `2e11` | `2.97e-2` | `2.20` |
| `5e11` | `0.186` | `13.76` |

```text
hard total heat-budget pre-test: NO EXCLUSION.
```

Ein kompletter geothermischer Quellenfit bleibt offen.

Beim analytischen `dM/dt=kM^2`-4.54-Gyr-Rueckwaertstest bleiben alle Anfangsmassen positiv. Kein algebraischer Alterswiderspruch entsteht. Hohe Supply-Aeste besitzen jedoch kurze heutige `M/Mdot`-Zeiten (`~0.10...0.52 Gyr` fuer hohe `5e11...1e11`-Aeste) und erzeugen damit starken Evolutions-/Fine-Tuning-Druck.

# 8. Stage 3.70A / A17 – Observational Pre-Falsification Gate

Direkte r_B-Near-Zone-Seismik ist extrem sub-wavelength. Bei `lambda=1 km` liegt

```text
ka ~3.9e-11 ... 1.9e-9
```

und ein einfacher `(ka)^4`-Rayleigh-Groessenproxy bei etwa

```text
2e-42 ... 1e-35.
```

Daher ist die mikroskopische Near-Zone selbst kein sinnvoller Seismikkanal.

Makroskopische Seismik bleibt nur dann testbar, wenn Full-Multiphysics ein Profil wie

```text
delta rho(r), delta Vp(r), delta Vs(r)
```

ueber seismologisch relevante Skalen erzeugt.

# 9. Stage 3.70B / A18 – aktueller Real-Data Audit

2026 SK-Gd Publikation, Band `25.29...31.29 MeV`:

```text
SK-IV observed 90% CL        0.04 cm^-2 s^-1 MeV^-1
SK-VI+VII NN observed        0.13
SK-VI+VII BDT observed       0.16.
```

Projekt-H+ Proxy:

```text
0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Damit:

```text
vs strongest SK-IV limit:
project/limit ~2.45 ... 3.05 -> FAIL in project reinterpretation.

vs standalone SK-Gd-2026 limits:
project proxy below those weaker limits.
```

Die 2026 berichtete DSNB-Indikation ist kein Earth-BH-Signal und wird nicht als Unterstuetzung von H+ gewertet.

H0:

```text
REAL-DATA LIKELIHOOD NOT YET IDENTIFIABLE
```

weil eine eindeutige makroskopische Observable-Amplitude noch fehlt.

# 10. A19 – Formation / Delivery Recheck

Optimistische direct-Earth dynamical-friction Rechnung mit `v_inf=220 km/s`, uniformer mittlerer Erddichte und grosszuegigem Reibungsfaktor:

| M_BH | DeltaE/E_inf |
|---:|---:|
| `1e10` | `1.0e-18` |
| `1e11` | `1.0e-17` |
| `2e11` | `2.0e-17` |
| `5e11` | `5.0e-17` |

Standard-Halo-Einfang verfehlt die benoetigte Bindungsenergie damit um etwa `16...18` Groessenordnungen.

Capture-freundliche asymptotische Geschwindigkeitsschwelle im selben Proxy:

```text
1e10 kg -> ~0.0043 m/s
1e11 kg -> ~0.0137 m/s
2e11 kg -> ~0.0194 m/s
5e11 kg -> ~0.0307 m/s.
```

Neuere Drei-Koerper-Sterncapture-Literatur liefert reale Capture-Mechanismen fuer deutlich schwerere PBHs, rettet aber den Projektbereich `1e13...5e14 g` nicht als Earth-delivery Mechanismus.

Formation matrix:

| Mechanismus | Status |
|---|---|
| In-situ-Kollaps normaler Erdmaterie | **FAIL** |
| spaeter direkter Earth-Capture bei normalen Halo-Geschwindigkeiten | **VERY STRONG FAIL** |
| Proto-Earth-/Planetesimal-Standardcapture | **FAIL unter getesteten Standardbedingungen** |
| normaler Halo -> cold disk delivery | **stark negativ** |
| three-body stellar/planetary capture | realer Mechanismus allgemein, aber **kein Rescue fuer Projektmasse/Earth delivery** |
| cold/co-moving primordialer Seed | **OPEN initial condition; Ursprung/Wahrscheinlichkeit nicht hergeleitet** |

# 11. Aktuelle Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| kleiner smooth Erdbranch | kein eigener Struktur-Ausschluss | kein eigener Struktur-Ausschluss |
| strongest SK-IV Hawking anti-nu_e project test | **FAIL** | n/a |
| standalone SK-Gd 2026 high-energy limit | unter Limit im Projektproxy | n/a |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Dense-core Charge/Screening | **PARTIAL, stark eingeengt** | **PARTIAL, stark eingeengt** |
| A13b empirical-fit outer supply | **PARTIAL CALCULATED** | **PARTIAL CALCULATED** |
| `1e10 kg` capacity/backpressure | conditional | conditional |
| `>=1e11 kg` reduced inner processing | processing-capable in tested A13b stack | processing-capable in tested A13b stack |
| final raw-data Fe/Ni EOS supply | **OPEN** | **OPEN** |
| final Full-WDM species net Mdot | **OPEN** | **OPEN** |
| 47-TW hard heat budget | no exclusion | no exclusion |
| real-data unique macro likelihood | branch already negative in tested neutrino proxy | **NOT IDENTIFIABLE YET** |
| Formation | **strongly negative** | **strongly negative** |
| direkte Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

# 12. Was jetzt wirklich noch offen ist

Die Reihenfolge wurde bis A19 abgearbeitet. Die verbleibenden Punkte sind keine weiteren frei waehlbaren Reduced-Tests, sondern fehlende physische Daten/Closures:

```text
1. raw Zenodo / direct SESAME-92141 Fe-isentrope ingestion
2. full screened Coulomb-Dirac electron S-matrix refinement
3. real Fe/Ni/light-element mixture EOS + two-temperature WDM transport
4. species/reaction-resolved final Mdot_BH(t), Q(t)
5. unique macroscopic H0 observable profile/amplitude
6. real PREM/seismic/heat/neutrino likelihood once item 5 exists
7. physically motivated cold/co-moving formation mechanism, if one can be derived.
```

Bis diese Punkte geschlossen sind, ist der korrekte Gesamtstatus:

```text
quantitative, reproducible, falsifiable research hypothesis;
not experimentally detected;
not an established physical theory.
```
