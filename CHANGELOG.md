# Changelog

Dieses Changelog dokumentiert die oeffentlich sichtbaren Entwicklungsstaende des Erdmoduls. Historische Zwischenwerte bleiben als Entwicklungsstand erhalten; spaetere haertere Tests ersetzen nur ihre aktuelle Interpretation.

## V1.5 / Stage 3.69E/A-9 Residence + Backpressure + Reduced Transport Closure - 26.08.2026

A9 verbindet die bisherigen Wave-Capture-, Screening-, Recycling- und Weak-Timescale-Teilmodule erstmals zu einer quantitativen Reduced Transportclosure.

### Neue Closure

Fuer repeated encounters gilt exakt:

```text
chi_capture = p/(p+e_perm)
```

mit Einzelpass-Capture `p` und permanentem Escape `e_perm`.

Im aktuellen strong-coupling/geometrischen Sensitivitaetsbranch wird permanenter ballistischer Escape durch den kollisionalen optischen Tiefenfaktor unterdrueckt:

```text
e_perm ~ f(v>v_esc) exp(-tau_coll)

tau_coll = 2 r_B/lambda_0 [x_t^-1/2 - 1].
```

An den getesteten atomaren Transition-Skalen ist `tau_coll>>1`; Misses werden deshalb im Reduced Branch rezykliert statt dauerhaft zu entkommen.

### Processing-Capacity bei `M_BH=1e11 kg`

| `r_t` | `Mdot_capacity` [kg/s] | `Xi_high=Mdot_supply,high/Mdot_capacity` |
|---:|---:|---:|
| `3e-11 m` | `1.85e-5` | `0.0079` |
| `1e-10 m` | `9.13e-7` | `0.160` |
| `2e-10 m` | `1.61e-7` | `0.905` |

Damit ist der aktuelle `1e11 kg` Strong-Coupling/Recycling Reduced Branch fuer den gesamten historischen Supply-Benchmark processing-capable.

Massenscan:

```text
1e10 kg: BACKPRESSURE-SENSITIVE / OPEN
1e11 kg: supply-processing capable in tested strong-coupling bracket
2e11 kg: clear capacity reserve
5e11 kg: very large capacity reserve.
```

Kritischer Reduced-Massenbereich je nach Supply und atomarer Transition-Skala:

```text
Mcrit ~5.8e9 ... 9.6e10 kg.
```

### Weak-/Charge-Timescales

Bei `M=1e11 kg` verlangt eine Reaktion vor der Reduced Capture ungefaehr

```text
Ni threshold: lambda_required ~1.10e13 s^-1
Fe threshold: lambda_required ~6.69e16 s^-1.
```

Der publizierte schnelle `56Fe`-EC-Vergleich `~1.5916e4 s^-1` ist dafuer viele Groessenordnungen zu langsam. Promptes Weak-Equilibrium/one-pass-Neutronisierung wird im schnellen supply-processing Branch daher nicht gestuetzt.

Die Elektronen-Plasmaantwort ist wesentlich schneller als die Reduced Residence-Zeit; bulk-quasineutraler Transport ist als Reduced Closure motiviert, ohne den diskreten BH-Charge-State exakt zu loesen.

### Aussagegrenze

```text
A9 Reduced Strong-Coupling branch @M>=~1e11 kg:
    supply-processing capable
    chi_transport ~1 within this reduced closure

M=1e10 kg:
    backpressure-sensitive / OPEN

first-principles WDM transport:
    OPEN
final species-resolved net Mdot_BH:
    OPEN
Stage 3.69 Full-Multiphysics:
    OPEN
```

Neue/aktualisierte Dateien:

- `STAGE3_69E_A9_RESIDENCE_BACKPRESSURE_NETWORK.md`
- `stage3_69e_a9_residence_backpressure_network.py`
- `STAGE3_69E_A9_PLAN.md`
- `STAGE3_69F_A10_PLAN.md`
- `README.md`
- `TEST_STATUS.md`
- `NUMERIK_STATUS.md`
- `AKKRETION_STATUS.md`
- `VALIDATION_PROTOCOL_STAGE3_69_70.md`

H+ und H0 bleiben parallel. H+ bleibt im getesteten Standard-Hawking/SK-IV-Projekt-Reinterpretationsmodell FAIL; H0 bleibt OPEN / nicht nachgewiesen.

---

## V1.5 / Stage 3.69A-4 bis 3.69D/A-8 - 26.08.2026

### A4 – Charged Dirac / Charge Feedback

Bei `M_BH=1e11 kg`:

```text
Q=0 e      -> sigma_p ~0.949...0.950 classical
Q=3.67 e   -> ~0.889 classical
Q=10 e     -> ~0.765 classical
Q=24.18 e  -> ~0.517 classical
```

Charge-Feedback ist relevant; ein Orders-of-Magnitude-Protonenstopper wurde im getesteten Q-Bereich nicht gefunden. Charged-electron far-field Coulomb matching bleibt OPEN.

### A5 – Fe/Ni 0+ Klein-Gordon Capture

```text
Fe-56 @1e11 kg: sigma/sigma_classical ~0.9975
Ni-58 @1e11 kg: sigma/sigma_classical ~0.9965
```

Keine starke kohärente Composite-Wellenunterdrueckung gefunden. Dense-Screening liegt im Reduced Proxy auf atomaren/sub-nm Skalen, nicht ueber `r_B`.

### A6 – Kinetic Recycling Closure

Die Identifikation

```text
small p_single -> equally small stationary Mdot
```

wurde verworfen. Repeated encounters verlangen eine explizite Escape-/Recycling-Closure.

### A7 – Collision Regime + Bondi Backpressure

Korrigierte Knudsen-Trends:

```text
strong-coupling/geometric: Kn ~ r^(1/2) -> nach innen kleiner
weak-Coulomb/Spitzer:     Kn ~ r^(-3/2) -> nach innen groesser.
```

Der 1-D-Bondi-Euler-Prototyp reproduziert den absorbierenden transsonischen Benchmark auf Prozentniveau. Ein reflektierender Innenrand erzeugt Backpressure und einen outward shock.

### A8 – Dense Fe / Degeneration / Reaktionszeitskalen

Electron-Capture-Schwellen koennen energetisch aufgehen, aber

```text
reaction threshold open != reaction equilibrium.
```

Promptes Weak-Equilibrium/instantane Neutronisierung wurde im Reduced Transit-Zeitscale nicht etabliert.

Aktuelle Dateien:

- `STAGE3_69A4_CHARGED_DIRAC_FEEDBACK.md`
- `stage3_69a4_charged_dirac_feedback.py`
- `STAGE3_69A5_DENSE_FENI_CLOSURE.md`
- `stage3_69a5_dense_feni_closure.py`
- `STAGE3_69B_A6_KINETIC_RECYCLING_CLOSURE.md`
- `stage3_69b_a6_reduced_closure.py`
- `STAGE3_69C_A7_COLLISION_RECYCLING_PDE.md`
- `stage3_69c_a7_collision_recycling_pde.py`
- `STAGE3_69D_A8_WDM_WEAK_TIMESCALES.md`
- `stage3_69d_a8_wdm_weak_timescales.py`

---

## V1.5 / Stage 3.69A-3 Earth-speed Proton Capture + Charge Feedback - 26.08.2026

- flux-stabile Absorptionsauswertung fuer schwache Partialwellen implementiert;
- Earth-speed Protonen-Massenscan `1e10...5e11 kg` berechnet;
- bei `1e11 kg`: `sigma_p~2.1741e-22 m^2 ~0.9503 classical`;
- frueherer Unruh-Protonenwert bleibt historischer Low-E-Benchmark, wird aber am Referenzpunkt durch den vollen Dirac-Matcher ersetzt;
- erste Charge-Kraft-/Gleichgewichtsskalen berechnet;
- H+/H0 weiterhin getrennt.

---

## V1.5 / Stage 3.69A-1 Quantum-Capture-Prototyp - 26.08.2026

- Schwarzschild-Dirac-Radialgleichung in Painleve-Gullstrand-Koordinaten implementiert;
- regulaerer Horizon-Branch und konservierter radialer Dirac-Strom implementiert;
- In/Out-Partialwellen-Matching und Matchingradius-Konvergenz getestet;
- qualitative Doran-Struktur und Low-alpha Regression reproduziert;
- Fe-56/Ni-58 Spinstatus auf `0+` korrigiert.

---

## V1.5 / Stage 3.68E Feedback-Integration - 26.08.2026

- externer Numerical-Relativity/HPC- und Seismologie-Input technisch integriert;
- `c_eff=10.4355 km/s` als PREM-Supply-Proxy explizit dokumentiert;
- `r_B~61 nm` bei `1e11 kg`;
- Bondi/Michel nicht mehr automatisch als finale Horizon-Rate interpretiert;
- Quantum/Wave-Capture als Pflichtblock aufgenommen;
- 47-TW-Waerme-Sanity-Check und konditionale Seismikstrategie dokumentiert.

---

## V1.5 / Definition Stage 3.69-3.70 - 25.08.2026

- Stage 3.69 als High-Fidelity-Multiphysik-Closure definiert;
- Stage 3.70 als branch-spezifischer Real-Data-/Falsifikationstest definiert;
- keine abgeschlossene Stage 3.69/3.70 behauptet.

---

## V1.4 / Stage 3.68 - 25.08.2026

- H+ und H0 strikt getrennt;
- H+ Standard-Hawking im getesteten SK-IV-Projekt-Reinterpretationsmodell FAIL;
- kleiner smooth-compensated Erdbranch weitergefuehrt;
- Hard-Cavity und mehrere fruehe Akkretions-/Coulomb-Proxies korrigiert oder verworfen;
- reduzierte Seismik, Langzeit, Loss-Cone und Formation gehaertet;
- Formation unter getesteten Standardwegen stark negativ.

---

## V1.3 / Stage 3.15-3.17 - 25.08.2026

- simultaner Hawking/Michel-Massenscan;
- smooth-compensated Branch eingefuehrt;
- erste Seismik-Haertetests.

---

## V1.3 / Stage 3.14 - 25.08.2026

- Bondi-/Michel-Akkretionsaudit;
- Hochdruck-EOS/Rheologie-Haertung;
- mehrere fruehe Toy-Grenzen zurueckgezogen;
- relativistischer Michel-Solver mit analytischem Selfcheck.

---

## V1.2 / Stage 1.7 - 25.08.2026

- Titel auf **SL/BH-Kernhypothese Erdmodul** vereinheitlicht;
- Layered-PREM-Earth-Closure dokumentiert.

---

## V1.0 - 23.08.2026

Erstveroeffentlichung des Erdmoduls.

- archivierte V1.0-PDF bleibt unveraendert als Prioritaets-/Archivnachweis;
- spaetere Forschungsstaende werden nicht rueckwirkend in die Archiv-PDF geschrieben.
