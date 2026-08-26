# SL/BH-Kernhypothese Erdmodul

## Veroeffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller numerischer Forschungsstand:** Stage 3.69 bis A12c partiell bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen  
**Stand:** 26.08.2026  
**Erstveroeffentlichung Erdmodul V1.0:** 23.08.2026

> `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unveraendert als Erstveroeffentlichungs-/Prioritaetsarchiv. Neue Tests werden in Markdown und reproduzierbaren Python-Skripten fortgeschrieben.

## Wissenschaftliche Aussagegrenze

Die SL/BH-Kernhypothese Erdmodul ist ein **theoretischer Forschungsentwurf, kein experimenteller Nachweis**. Es gibt derzeit keine direkte Detektion und keine eindeutige positive Signatur eines schwarzen Lochs im Erdzentrum.

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben getrennt und parallel.

## Branchstatus

### H+

Im getesteten Projektmodell liegt der Standard-Hawking-H+-Bereich etwa bei

```text
M_BH ~4.82e11 ... 5.49e11 kg.
```

Der Projekt-Greybody-/Neutrinofluss ueberschreitet im verwendeten SK-IV-Reinterpretationsband den publizierten Grenzwert.

```text
H+ Standard-Hawking:
FAIL im getesteten Projekt-Reinterpretationsmodell.
```

Dies ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

### H0

```text
P_Hawking = 0.
```

H0 ist von Hawking-basierten Emissionsgrenzen getrennt, muss aber Materieakkretion, Langzeitstabilitaet, Formation und Real-Data-Tests bestehen.

```text
H0: OPEN / nicht nachgewiesen.
```

# Aktiver kleiner Erdbranch

Die starke Zentralmassen-/Hard-Cavity-Variante ist verworfen. Aktiv bleibt der kleine smooth-compensated Branch.

PREM-Referenz am Zentrum:

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

Die bisherigen reduzierten Makro-/PREM-/Seismiktests liefern fuer diesen kleinen Branch keinen robusten eigenen Ausschluss. Das ist **Modellkompatibilitaet innerhalb der getesteten Proxies, keine Evidenz fuer einen BH**.

# Stage 3.69 – Materie-/Capture-/Transportstack

## A1/A3 – Schwarzschild-Dirac Protonen

Bei Earth-speed `10.4355 km/s` und `M=1e11 kg`:

```text
sigma_p ~2.174e-22 m2
sigma_p/sigma_classical ~0.9503.
```

Keine grosse Protonen-Wellenunterdrueckung.

## A4 – Charged Proton Capture

Bei `M=1e11 kg`:

```text
Q=0 e      -> ~0.949 classical
Q=3.67 e   -> ~0.889
Q=10 e     -> ~0.765
Q=24.18 e  -> ~0.517.
```

Charged-electron long-range Coulomb matching bleibt OPEN.

## A5 – Fe/Ni `0+` Composite-Capture

```text
Fe-56 @1e11 kg ~0.99754 classical
Ni-58 @1e11 kg ~0.99646 classical.
```

```text
large coherent Fe/Ni wave suppression: NOT FOUND.
```

## A6-A10 – Recycling und WDM-Transport

Ein kleiner Single-pass-Loss-Cone ist nicht automatisch die stationaere Nettoakkretionsfraktion.

```text
chi_capture = p/(p+e_perm).
```

A10 zeigt ausserdem:

```text
local Kn~1 != permanent escape through the outer dense Fe/WDM reservoir.
```

Unter dem **historischen** hohen Michel-Supply war der innere Reduced Processing-Stack ab etwa `1e11 kg` klar processing-capable; `1e10 kg` lag nahe/ueber der Capacity-Grenze.

## A11/A12 – Dynamic Backpressure

Ein sphärischer Finite-Volume/HLL-PDE-Solver reproduziert den absorbierenden Bondi-Grenzfall und erzeugt bei reflektierender/kapazitaetslimitierter innerer Randbedingung einen nach aussen laufenden Backpressure-Shock.

Unter dem historischen `1e10 kg` Capacity-Limiter:

```text
N=128  shock~1.269 r_B
N=256  shock~1.254 r_B
N=512  shock~1.233 r_B
N=1024 shock~1.229 r_B
```

Die Shock-Lage konvergiert; eine stationaere endliche innere `Mdot` wurde nicht nachgewiesen. Im Long-domain-Test wandert die Front weiter nach aussen.

## A12b – Zbar + dissipative Sensitivitaet

More/Thomas-Fermi Fe-Closure:

```text
rho=13.0885 g/cm3
T=6000 K
Zbar~2.76.
```

Gegen eine publizierte solid-density Average-Atom-Definition liegt der korrigierte Fit bei `0.1...10 eV` etwa `12...16 %` niedriger; `Zbar` bleibt daher ein Modellband.

Literaturgebundene Bereiche

```text
eta=8.5...26 mPa s
k=67...87 W/m/K
Cp~850 J/kg/K
```

wurden in einen Reduced dissipativen PDE-Test eingebaut. Unter der historischen hohen Supply-Randbedingung entfernen diese Terme den `1e10 kg` Backpressure-Ast nicht.

# A12c – wichtigste aktuelle Korrektur: Supply ist EOS-abhaengig

Der fruehere Michelbereich

```text
M=1e11 kg:
1.47e-8 ... 1.46e-7 kg/s
```

wird ab A12c **nicht mehr als feste aeussere Supply-Rate** verwendet.

Er stammt aus einem frueheren phenomenologischen Dense-Matter-Michel-Solver und ist ein

```text
LEGACY / EOS-SENSITIVE BENCHMARK.
```

Fuer `Gamma>5/3` verwendet A12c die relativistische Michel-Kritikalitaet. Bei gleicher PREM-Aussenbedingung liefert der konstante-Gamma Sensitivitaetsscan bei `M=1e11 kg`:

| Gamma | Mdot [kg/s] |
|---:|---:|
| `1.75` | `1.19e-7` |
| `1.80` | `2.89e-8` |
| `1.85` | `8.02e-9` |
| `2.00` | `3.35e-10` |
| `2.20` | `1.50e-11` |
| `2.356` local PREM proxy | `2.40e-12` |

Der historische Projektbereich entspricht in diesem einfachen konstanten-Gamma-GR-Surrogat etwa

```text
Gamma~1.743...1.826.
```

**Wichtig:** Der lokale PREM-Stiffness-Wert `dK/dP~2.356` darf nicht als konstantes globales Gamma bis zum Horizon fortgesetzt werden. Reales Fe/Ni ionisiert, degeneriert und wechselt sein EOS-Regime. `2.40e-12 kg/s` ist daher **keine finale Endrate**.

## Korrigierter Massensplit

Der fruehere Kurzsatz

```text
1e10 kg -> dynamic backpressure
```

war zu allgemein. Aktuell gilt:

```text
1e10 kg:
backpressure CONDITIONAL ON SUPPLY EOS.
soft/high supply -> capacity overload possible
stiff/lower supply -> overload can disappear.
```

Im konstanten-Gamma GR-Sensitivitaetsscan liegt die A10-fast `Xi=1`-Grenze bei etwa

```text
Gamma~1.756.
```

Fuer `>=1e11 kg` bleibt der innere Processing-Befund bestehen. Ein niedrigerer stiff-EOS Supply vergroessert die Processing-Reserve, bestimmt aber noch nicht die finale Netto-Mdot.

# Aktuelle Statusmatrix

| Bereich | H+ | H0 |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleiner smooth Erdbranch | kein eigener Makro-Ausschluss | kein eigener Makro-Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL im getesteten Projektmodell** | nicht anwendbar |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Charge-/Screening | teilweise berechnet | teilweise berechnet |
| A9-A12 inner processing/transport | stark gehaertet / PARTIAL | stark gehaertet / PARTIAL |
| historical Michel supply | **LEGACY / EOS-SENSITIVE** | **LEGACY / EOS-SENSITIVE** |
| `1e10 kg` Backpressure | supply/EOS-conditional | supply/EOS-conditional |
| `>=1e11 kg` inner processing | processing-capable in current models | processing-capable in current models |
| general-EOS outer supply | OPEN | OPEN |
| final net `Mdot_BH` | OPEN | OPEN |
| Formation/Delivery | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

# Formation

Die getesteten Standardwege bleiben stark negativ:

```text
in-situ Kollaps normaler Erdmaterie: FAIL
spaeter direkter Earth-Capture: FAIL
Proto-Earth-/Planetesimal-Standardcapture: FAIL
normaler Halo -> protoplanetare cold disk: FAIL unter getesteten Bedingungen
cold/co-moving Anfangsbedingung: mathematisch moeglich, Herkunft nicht hergeleitet.
```

# Naechster Pflichtblock – Stage 3.69I / A13

```text
PREM outer state
-> general/piecewise Fe/Ni EOS
-> thermodynamic P(rho,T), E(rho,T), T(rho,e)
-> bounded Zbar uncertainty
-> relativistic variable-EOS sonic/critical point
-> Mdot_supply(EOS) band
-> recouple A9-A12 transport/capture
-> revised net Mdot_BH band
-> rerun long-term/heat constraints.
```

# Zentrale aktuelle Dateien

- `STAGE3_69H_A12_SHOCK_TRANSPORT_AUDIT.md`
- `stage3_69h_a12_shock_transport_audit.py`
- `STAGE3_69H_A12B_ZBAR_DISSIPATIVE_CLOSURE.md`
- `stage3_69h_a12b_zbar_dissipative_closure.py`
- `STAGE3_69H_A12C_STIFF_EOS_GR_SUPPLY.md`
- `stage3_69h_a12c_stiff_eos_gr_supply.py`
- `STAGE3_69I_A13_PLAN.md`
- `AKKRETION_STATUS.md`
- `TEST_STATUS.md`

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; numerischer Forschungsstand bis Stage 3.69H/A12c partiell, Stage 3.69 Full-Multiphysics und Stage 3.70 offen, Rheinland-Pfalz, Deutschland.
