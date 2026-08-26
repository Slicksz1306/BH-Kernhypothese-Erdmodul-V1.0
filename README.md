# SL/BH-Kernhypothese Erdmodul

## Veroeffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller numerischer Forschungsstand:** bis Stage 3.69G/A-11 bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen  
**Stand:** 26.08.2026  
**Erstveroeffentlichung Erdmodul V1.0:** 23.08.2026

> `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unveraendert als Erstveroeffentlichungs-/Prioritaetsarchiv. Der aktuelle Forschungsstand wird in Markdown und reproduzierbaren Python-Skripten fortgeschrieben.

## Wissenschaftliche Aussagegrenze

Die SL/BH-Kernhypothese Erdmodul ist ein **theoretischer Forschungsentwurf, kein experimenteller Nachweis**. Untersucht wird, ob ein kleiner zentraler BH-Branch mit Erdbeobachtungen und etablierter GR-, Quanten-, Plasma- und Materiephysik konsistent modelliert werden kann.

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches werden getrennt und parallel gefuehrt. Gemeinsame Materie-/Capture-/Transportmodule gelten fuer beide; Hawking-spezifische Emissionen nur fuer H+.

## Branchstatus

### H+

Im getesteten Standard-Hawking-Projektbranch liegt der relevante Bereich bei etwa

```text
M_BH ~4.82e11 ... 5.49e11 kg.
```

Der berechnete Projekt-Greybody-/Neutrinofluss ueberschreitet im verwendeten SK-IV-Vergleichsband den publizierten Grenzwert.

```text
H+ Standard-Hawking: FAIL im getesteten Projekt-Reinterpretationsmodell.
```

Das ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

### H0

```text
P_Hawking = 0.
```

H0 ist von Hawking-basierten Neutrino-/Gamma-Grenzen getrennt, muss aber Akkretion, Transport, Langzeitstabilitaet, Formation und Real-Data-Tests bestehen.

```text
H0: OPEN / nicht nachgewiesen.
```

## Aktiver Erdbranch

Die starke Zentralmassenvariante wurde verworfen. Aktiv ist der kleine `smooth compensated` Branch.

PREM-/Supply-Referenz:

```text
rho_c = 13.0885 g/cm3
c_eff = 10.4355 km/s.
```

Bei `M_BH=1e11 kg`:

```text
r_B ~6.13e-8 m
r_s ~1.49e-16 m.
```

Die bisherigen reduzierten Makrotests liefern fuer diesen kleinen Branch keinen robusten Ausschluss durch Gesamtmasse/GM, Traegheitsmoment, reduzierte Hydrostatik, vereinfachte Seismik oder globale Waermeproxies. Das ist Modellkompatibilitaet innerhalb der getesteten Proxies, **keine Evidenz** fuer einen BH.

# Stage 3.69 – aktueller Materie-/Capture-/Transportstack

## A1/A3 – Schwarzschild-Dirac + Earth-speed Protonen

Der massive Schwarzschild-Dirac-Solver besitzt regulaeren Horizon-Branch, konservierten Strom und In/Out-Partialwellenmatching.

Bei `M=1e11 kg`, `v=10.4355 km/s`:

```text
sigma_p ~2.174e-22 m2
sigma_p/sigma_classical ~0.9503.
```

Eine starke Protonen-Wellenunterdrueckung wird an diesem Referenzpunkt nicht gefunden.

## A4 – Charged Proton Capture

Bei `M=1e11 kg`:

```text
Q=0 e       -> ~0.949 classical
Q=3.67 e    -> ~0.889
Q=10 e      -> ~0.765
Q=24.18 e   -> ~0.517.
```

Ladungsfeedback ist relevant, aber im getesteten Bereich kein Orders-of-Magnitude-Protonenstopper.

```text
charged proton subtest: CALCULATED / benchmarked
charged electron long-range Coulomb matcher: OPEN.
```

## A5 – Fe/Ni `0+` Composite-Wave-Capture

Dominante Fe-56/Ni-58-Kerne werden im ersten kohaerenten Proxy als massive skalare/Klein-Gordon-Zustaende behandelt.

Bei `M=1e11 kg`:

```text
Fe-56: sigma/sigma_classical ~0.99754
Ni-58: sigma/sigma_classical ~0.99646.
```

```text
large coherent Fe/Ni wave suppression: NOT FOUND.
```

## A6/A7 – Recycling, Kollisionalitaet und Backpressure

Ein kleiner Einzelpass-Loss-Cone darf nicht als stationaerer Mdot-Faktor verwendet werden.

Bei wiederholten Encountern:

```text
chi_capture = p/(p+e_perm).
```

A7 korrigierte ausserdem den Knudsen-Shortcut und zeigte mit einem kontrollierten 1-D-Bondi-Euler-Solver:

```text
absorbing inner boundary -> transsonischer Bondi-Flux
reflecting inner boundary -> pressure pile-up + outward shock.
```

Damit kann dauerhafter Backpressure den Supply beeinflussen; sonic shielding verhindert nicht jede langfristige Rueckwirkung.

## A8 – Dense Fe / Degeneration / Weak Timescales

Im Reduced-Inward-Proxy koennen Electron-Capture-Schwellen energetisch aufgehen, aber die lokalen dynamischen/Residence-Zeiten sind extrem kurz.

Ein aggressiver publizierter Fe-56-EC-Vergleich:

```text
lambda_ec ~1.5916e4 s^-1
```

liegt viele Groessenordnungen unter den fuer promptes Gleichgewicht erforderlichen Reduced-Raten.

```text
energetically open EC != prompt weak equilibrium
prompt one-pass neutronization: NOT SUPPORTED.
```

## A9 – Residence / Processing / Backpressure Closure

A9 koppelt repeated encounters, Reservoir-Masse, permanenten Escape, Plasmaresponse und Weak-Reaction-Gates.

Bei `M=1e11 kg` und atomaren Transition-Sensitivitaeten:

```text
Xi_high = Mdot_supply / Mdot_capacity
        ~0.0079 ... 0.905.
```

Massensplit:

```text
1e10 kg: backpressure-/transition-sensitive
1e11 kg: supply-processing capable im Reduced strong-coupling Branch
2e11 kg: klare Processing-Reserve
5e11 kg: sehr grosse Processing-Reserve.
```

## A10 – First-Principles-Informed WDM Transport Envelope

A10 ersetzt den einzelnen geometrischen Mean-Free-Path-Proxy durch publiziert kalibrierte Fe-/Fe-Ni-Transportanker plus eine bewusst escape-freundliche innere Sensitivitaet.

Direkte Literaturabdeckung:

```text
WDM Fe QMD transport:
    rho ~12.5 ... 25 g/cm3
    T   ~0.5 ... 15 eV

2025 first-principles Fe EOS:
    rho ~7.874 ... 47.2 g/cm3
    T   ~5500 K ... 1e9 K.
```

Selbst im schnellsten/escape-freundlichsten Envelope:

| M_BH | tau_total | Xi_high |
|---:|---:|---:|
| `1e10 kg` | `~1.92e2` | `~1.47` |
| `1e11 kg` | `~1.93e3` | `~2.81e-3` |
| `2e11 kg` | `~3.86e3` | `~4.28e-4` |
| `5e11 kg` | `~9.66e3` | `~3.54e-5` |

Damit gilt im Reduced Envelope:

```text
local Kn~1 != permanent escape through the outer Fe/WDM reservoir.
```

A10 reproduziert den A9-Massensplit, ist aber **PARTIAL first-principles-informed**, weil die tiefste Zone nicht direkt tabelliert ist.

## A11 – Time-Dependent Partial-Sink PDE

A11 testet diesen Massensplit erstmals dynamisch.

Der sphaerische Finite-Volume-HLL-Solver verwendet eine kontinuierliche innere Randbedingung

```text
F_inner = A F_absorb + (1-A) F_reflect.
```

`A` ist eine PDE-Sensitivitaet und nicht automatisch identisch mit einer mikroskopischen Capture-Cross-Section.

### Numerische Regressionen

```text
absorbing Bondi: PASS auf Prozentniveau
reflecting boundary: outward Backpressure/Shock reproduziert
finite-volume mass residual: ~1e-16 ... few 1e-15
energy audit residual: ~1e-16 ... few 1e-15.
```

### Fe-like Sensitivitaet

Der A5-Wert `0.99754 classical` wird nur als Sensitivitaet `A=0.99754` getestet, nicht gleichgesetzt.

Bei `gamma=1.5` bleibt der Lauf praktisch auf dem voll absorbierenden Ast.

### Dynamische A10-Capacity-Closure

Als Transport-Capacity-Sensitivitaet:

```text
A_cap=min(1,1/Xi_high).
```

Damit im schnellsten A10-Envelope:

```text
1e10 kg:
    Xi_high~1.468 -> A_cap~0.681
    -> dynamischer Backpressure-Zweig entsteht
    -> innerer Flux stark reduziert

>=1e11 kg:
    Xi_high<<1 -> A_cap=1
    -> dynamischer Lauf bleibt absorbing/supply-processing.
```

Der A9/A10-Massensplit wird damit dynamisch reproduziert.

### Noch offene A11-Konvergenz

Der `1e10 kg` Shockbranch ist in der Regimeentscheidung stabil, aber seine exakte Endrate noch nicht gitterkonvergiert.

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
exact 1e10 shock-branch Mdot: OPEN
full tabulated WDM EOS/Zbar PDE: OPEN.
```

# Aktueller Status

| Bereich | H+ | H0 |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleiner smooth Erdbranch | kein eigener Makro-Ausschluss | kein eigener Makro-Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL im getesteten Projektmodell** | nicht anwendbar |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Charge-/Screening | teilweise berechnet | teilweise berechnet |
| A9 Residence/Recycling | CALCULATED Reduced Closure | CALCULATED Reduced Closure |
| A10 WDM transport envelope | PARTIAL CALCULATED | PARTIAL CALCULATED |
| A11 dynamic PDE | PARTIAL CALCULATED | PARTIAL CALCULATED |
| `>=1e11 kg` aktueller Reduced Matter-Branch | absorbing / supply-processing | absorbing / supply-processing |
| `1e10 kg` aktueller Reduced Matter-Branch | dynamic backpressure moeglich; exact Mdot OPEN | dynamic backpressure moeglich; exact Mdot OPEN |
| Full-WDM species-resolved Mdot | OPEN | OPEN |
| Formation/Delivery | stark negativ | stark negativ |
| direkte experimentelle Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## Formation

Die getesteten Standardwege bleiben stark negativ:

```text
in-situ Kollaps normaler Erdmaterie: FAIL
spaeter direkter Earth-Capture: FAIL
Proto-Earth-/Planetesimal-Standardcapture: FAIL
normaler Halo -> protoplanetare cold disk: FAIL unter getesteten Bedingungen
cold/co-moving Anfangsbedingung: mathematisch moeglich, Herkunft nicht hergeleitet.
```

## Naechster Pflichtblock

```text
Stage 3.69H / A12:
tabulated Fe/Ni EOS + Zbar
+ thermal conductivity / viscosity / relaxation
+ species/charge advection
+ high-resolution shock convergence
-> dynamic Mdot band with explicit EOS uncertainty.
```

## Zentrale aktuelle Dateien

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
- `STAGE3_69E_A9_RESIDENCE_BACKPRESSURE_NETWORK.md`
- `stage3_69e_a9_residence_backpressure_network.py`
- `STAGE3_69F_A10_WDM_TRANSPORT_ENVELOPE.md`
- `stage3_69f_a10_wdm_transport_envelope.py`
- `STAGE3_69G_A11_DYNAMIC_PARTIAL_SINK_PDE.md`
- `stage3_69g_a11_dynamic_partial_sink_pde.py`
- `STAGE3_69H_A12_PLAN.md`
- `TEST_STATUS.md`
- `NUMERIK_STATUS.md`
- `AKKRETION_STATUS.md`
- `VALIDATION_PROTOCOL_STAGE3_69_70.md`
- `CHANGELOG.md`

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; numerischer Forschungsstand bis Stage 3.69G/A-11, Stage 3.69 Full-Multiphysics und Stage 3.70 offen, Rheinland-Pfalz, Deutschland.
