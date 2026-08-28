# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller numerischer Forschungsstand:** Reduced/partial Stack bis A19; Stage 3.70B Real-Data-Audit partiell durchgeführt  
**Stand:** 29.08.2026  
**Erstveröffentlichung Erdmodul V1.0:** 23.08.2026

> `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs-/Prioritätsarchiv. Neue Rechnungen werden versioniert in Markdown und reproduzierbaren Python-Skripten fortgeschrieben.

## Wissenschaftliche Aussagegrenze

Die **SL/BH-Kernhypothese Erdmodul** ist ein quantitativer, reproduzierbarer und falsifizierbarer **theoretischer Forschungsentwurf**. Sie ist **kein experimenteller Nachweis** und derzeit **keine etablierte physikalische Theorie**.

Es gibt aktuell:

```text
keine direkte Detektion eines Erdzentrum-BH
keine eindeutige positive H0-Signatur
mehrere bestandene interne Solver-/Regressionstests
mehrere korrigierte/verwarfene frühere Annahmen
mehrere noch offene physische Closures.
```

## Branches

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Die beiden Branches werden strikt getrennt.

### H+

Der Projekt-Hawking/Greybody-Proxy im Band `25.29...31.29 MeV` liegt bei ungefähr

```text
0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Die 2026 SK-Gd-Publikation listet im selben Band:

```text
SK-IV observed 90% CL        0.04 cm^-2 s^-1 MeV^-1
SK-VI+VII NN observed        0.13
SK-VI+VII BDT observed       0.16.
```

Damit bleibt H+ in der **projektinternen Reinterpretation gegen den stärksten publizierten SK-IV-Binconstraint FAIL**. Die standalone SK-Gd-2026-Daten allein sind in diesem Bin schwächer und würden den Projektproxy nicht ausschließen.

Dies ist **keine offizielle Super-K-Erdzentrum-BH-Exklusion**.

### H0

```text
P_Hawking = 0
H0 = OPEN / nicht nachgewiesen.
```

H0 ist von Hawking-Emissionsgrenzen getrennt, muss aber Full-WDM-Akkretion, Formation und eine eindeutige Real-Data-Signatur bestehen.

# Aktiver Erdbranch

Die starke Zentralmassen-/Hard-Cavity-Variante ist verworfen. Aktiv ist nur der kleine **smooth-compensated Branch**.

PREM-Zentrumsreferenz:

```text
rho_c      ~13.08848 g/cm3
c_eff      ~10.4355 km/s
Kappa_S    ~1.4253 TPa
Pressure   ~363.852 GPa
dK/dP      ~2.356.
```

Bei `M=1e11 kg`:

```text
r_B ~6.13e-8 m
r_s ~1.49e-16 m.
```

Die bisherigen reduzierten Makrotests liefern für diesen kleinen Branch keinen eigenen robusten Struktur-Ausschluss. Das ist **Modellkompatibilität innerhalb der getesteten Proxies, keine Evidenz für einen BH**.

# Numerischer Stack – aktueller Kurzstand

## A1-A5 Wave/Capture

```text
Schwarzschild-Dirac Regressionen: PASS
Proton @1e11 kg: ~0.9503 classical
Fe-56 @1e11 kg: ~0.99754 classical
Ni-58 @1e11 kg: ~0.99646 classical
large coherent Fe/Ni wave suppression: NOT FOUND.
```

## A6-A12 Recycling / WDM / Backpressure

Repeated encounters:

```text
chi_capture = p/(p+e_perm).
```

Ein kleiner single-pass capture factor darf daher nicht direkt als stationäre Nettoakkretions-Unterdrückung interpretiert werden.

A10 zeigte in den getesteten WDM-Transporthüllen große äußere optische Tiefen; `local Kn~1` ist nicht gleich permanenter Escape.

A11/A12 zeigte bei Capacity-Überlastung einen nach außen laufenden Backpressure-Shock. Für `1e10 kg` wurde keine stationäre endliche Innenrate etabliert.

## A13 – General-EOS relativistischer Michel-Solver

A13 löst die stationäre Michel-Kritikalität für eine allgemeine thermodynamisch konsistente EOS:

```text
4 pi r^2 rho0 u = Mdot
h sqrt(1 - 2M/r + u^2) = h_inf

u_s^2 = a_s^2/(1+3 a_s^2)
r_s/M = (1+3 a_s^2)/(2 a_s^2)
h_s/sqrt(1+3 a_s^2) = h_inf.
```

Constant-EOS Regression gegen A12c: **PASS** (`~1e-4` relativ oder besser).

A13-Surrogat bei `1e11 kg`:

```text
Mdot_supply ~4.64e-8 ... 1.37e-6 kg/s.
```

## A13b – Grant-2021 Liquid-Fe Fit-Anker

Die publizierte Grant-2021 Liquid-Fe-EOS-Fitform wird als experimentell verankerter Outer-Abschnitt bis `400 GPa` benutzt.

Nominal:

```text
B_Grant(PREM center) ~1.419 TPa
K_PREM               ~1.425 TPa.
```

Konservativer Fitparameter/T/Intermediate-EOS-Scan bei `1e11 kg`:

```text
Mdot_supply ~8.27e-8 ... 6.13e-6 kg/s.
```

Status:

```text
empirical-fit outer anchor: PARTIAL CALCULATED
raw Zenodo traces: OPEN
direct SESAME-92141 ingestion: OPEN
final physical supply band: OPEN.
```

## A14 – Dense-core Electron Screening

Diffuse equal-T Plasmaformel:

```text
Q_eq,diffuse ~+24.18e @1e11 kg.
```

Dense Thomas-Fermi-Screening ergibt dagegen grob

```text
lambda_TF ~2.95e-11 ... 4.29e-11 m
E_F       ~19.4 ... 86.6 eV
preferred response scale ~O(1...5e).
```

Der vorhandene Proton-Dirac-Solver bleibt in diesem charge bracket nur order-unity unterdrückt:

```text
Q~+1.6e -> ~0.925 classical
Q~+4.9e -> ~0.867 classical.
```

```text
large electrostatic proton blocker: NOT FOUND
exact screened Coulomb-Dirac electron S-matrix: OPEN refinement.
```

## A15 – Integrated Reduced Net-Throughput

A13b Supply gegen A10 Processing-Capacity:

| M_BH | Xi_min | Xi_max | Status |
|---:|---:|---:|---|
| `1e10` | `0.832` | `61.60` | **supply/EOS/backpressure conditional** |
| `1e11` | `1.59e-3` | `1.18e-1` | **processing-capable in tested stack** |
| `2e11` | `2.42e-4` | `1.80e-2` | **processing-capable** |
| `5e11` | `2.00e-5` | `1.48e-3` | **processing-capable** |

```text
M>=1e11 kg:
inner reduced processing is not the current bottleneck.

M=1e10 kg:
time-dependent backpressure remains decisive.

final Full-WDM species-resolved Mdot_BH:
OPEN.
```

## A16 – Wärme / 4.54-Gyr-Sensitivität

`eta=1` Restmassenleistung im A13b-Band:

| M_BH | P_min [TW] | P_max [TW] |
|---:|---:|---:|
| `1e10` | `7.43e-5` | `5.51e-3` |
| `1e11` | `7.43e-3` | `0.551` |
| `2e11` | `2.97e-2` | `2.20` |
| `5e11` | `0.186` | `13.76` |

Verglichen mit `47 +/-2 TW` globalem Erdoberflächen-Wärmefluss:

```text
hard total-budget pre-test: NO EXCLUSION.
```

Dies ist kein kompletter geothermischer Quellenfit.

Beim analytischen `dM/dt=kM^2`-Rückwärtstest über `4.54 Gyr` bleiben die Anfangsmassen positiv; hohe Supply-Aeste besitzen jedoch kurze heutige `M/Mdot`-Zeiten und erzeugen starken Evolutions-/Fine-Tuning-Druck.

# Stage 3.70 – Beobachtung / Falsifikation

## A17 – Observational Pre-Falsification Gate

Direkte Seismik der mikroskopischen `r_B`-Near-Zone ist extrem sub-wavelength. Bei `lambda=1 km`:

```text
ka ~3.9e-11 ... 1.9e-9
(ka)^4 proxy ~2e-42 ... 1e-35.
```

Ein sinnvoller H0-Seismiktest benötigt daher eine **makroskopisch gekoppelte**, vom Full-Multiphysics-Modell vorhergesagte Struktur:

```text
delta rho(r)
delta Vp(r)
delta Vs(r)
mode shifts / waveform amplitudes.
```

## A18 – Current Real-Data Audit

```text
H+:
negative in strongest published SK-IV project comparison.

H0:
REAL-DATA LIKELIHOOD NOT YET IDENTIFIABLE.
```

Der Engpass ist nicht das Fehlen von PREM/Seismik/Heat/Neutrinodaten, sondern die noch fehlende eindeutige H0-Makrovorhersage.

# A19 – Formation / Delivery

Ein capture-freundlicher direct-Earth Dynamical-Friction-Proxy bei `v_inf=220 km/s` liefert:

```text
DeltaE/E_inf ~1e-18 ... 5e-17
```

für `1e10...5e11 kg`.

Die asymptotische Ein-Durchgang-Capture-Schwelle im selben optimistischen Proxy liegt nur bei

```text
~0.004 ... 0.031 m/s.
```

Damit:

```text
normal halo -> direct Earth capture: VERY STRONG FAIL
Proto-Earth/planetesimal standard capture: FAIL under tested conditions
cold/co-moving primordial seed: OPEN initial condition; origin not derived.
```

Neuere Drei-Körper-PBH-Star-Capture-Arbeiten zeigen reale Mechanismen in anderen Massen-/Hostregimen, liefern aber keinen Earth-delivery Rescue für den Projektbereich.

# Was noch wirklich fehlt

Die reduzierte Testsequenz bis A19 ist abgearbeitet. Die verbleibenden Entscheidungsblöcke sind fehlende physische Daten/Closures:

```text
1. raw Zenodo / direct SESAME-92141 Fe-isentrope ingestion
2. full Fe/Ni/light-element mixture + two-temperature WDM transport
3. exact screened electron scattering refinement
4. species/reaction-resolved final Mdot_BH(t), Q(t)
5. unique macroscopic H0 observable amplitude/profile
6. real PREM/seismic/heat/neutrino likelihood on that prediction
7. physically motivated formation/delivery mechanism.
```

# Zentrale aktuelle Dateien

- `TEST_STATUS.md`
- `VALIDATION_PROTOCOL_STAGE3_69_70.md`
- `STAGE3_69I_A13_GENERAL_EOS_MICHEL.md`
- `stage3_69i_a13_general_eos_michel.py`
- `STAGE3_69I_A13B_GRANT_FIT_ANCHOR.md`
- `stage3_69i_a13b_grant_fit_anchor.py`
- `STAGE3_69J_A14_ELECTRON_SCREENING.md`
- `stage3_69j_a14_electron_screening.py`
- `STAGE3_69K_A15_NET_THROUGHPUT.md`
- `stage3_69k_a15_net_throughput.py`
- `STAGE3_69L_A16_HEAT_AGE.md`
- `stage3_69l_a16_heat_age.py`
- `STAGE3_70A_A17_PRE_FALSIFICATION.md`
- `stage3_70a_a17_prefalsification.py`
- `STAGE3_70B_A18_REALDATA_AUDIT.md`
- `stage3_70b_a18_realdata_audit.py`
- `STAGE3_71_A19_FORMATION_RECHECK.md`
- `stage3_71_a19_formation_recheck.py`

# Open Science / Projekt-Governance

Originale Texte/Dokumentation/Grafiken stehen – soweit nicht anders gekennzeichnet – unter **CC BY 4.0**; originaler Quellcode unter **MIT**.

Wissenschaftliche Prüfung, Reproduktion, Kritik und eigene abgeleitete Arbeiten sind ausdrücklich erlaubt. Der **offizielle Projektstand** (`main`, Stages, Releases) wird jedoch nur über dieses Repository und die Freigabe des Projektinhabers definiert.

Siehe:

- `LICENSE`
- `ATTRIBUTION.md`
- `OPEN_SCIENCE.md`
- `OFFICIAL_PROJECT_POLICY.md`

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Reduced/partial numerischer Forschungsstand bis A19 / Stage 3.70B, Rheinland-Pfalz, Deutschland.
