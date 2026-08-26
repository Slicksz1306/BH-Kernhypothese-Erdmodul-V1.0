# Akkretions- und Langzeitstatus – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Forschungsstand:** Matter-/Capture-/Transportstack bis A12c partiell bearbeitet; general-EOS Netto-`Mdot` offen

## Aussagegrenze

Die reale BH-Akkretionsrate ist eine gekoppelte Groesse:

```text
outer relativistic supply(EOS)
-> dense-matter transport/recycling/backpressure
-> charge/composition
-> inner wave capture
-> net Mdot_BH.
```

Daher gilt weiterhin:

```text
Mdot_net != automatisch Mdot_Michel
Mdot_net != automatisch p_single * Mdot_supply.
```

Neu seit A12c gilt zusaetzlich:

```text
historical Michel benchmark != universal supply rate.
```

Der historische Projektbereich wird ab jetzt nur noch als **LEGACY / EOS-SENSITIVE BENCHMARK** gefuehrt.

# 1. Referenzzustand Erde

PREM-Zentrum:

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

# 2. Innerer Wave-/Capture-Sink

## Proton

Bei Earth-speed `10.4355 km/s`, `M=1e11 kg`:

```text
sigma_p ~2.174e-22 m2
sigma_p/sigma_classical ~0.9503.
```

Keine Orders-of-Magnitude-Wellenunterdrueckung.

Charged-Proton-Sensitivitaet:

```text
Q=0 e      -> ~0.949 classical
Q=3.67 e   -> ~0.889
Q=10 e     -> ~0.765
Q=24.18 e  -> ~0.517.
```

Charged-electron long-range Coulomb matching bleibt OPEN.

## Fe/Ni

Dominante `Fe-56`/`Ni-58`-Kerne haben `0+`; kohärenter erster Composite-Proxy ist scalar/Klein-Gordon.

Bei `M=1e11 kg`:

```text
Fe-56 ~0.99754 classical
Ni-58 ~0.99646 classical.
```

```text
large coherent Fe/Ni wave suppression: NOT FOUND.
```

# 3. Recycling statt Single-pass-Faktor

Direkter Single-pass-Hintergrundproxy bei `1e11 kg` lag bei etwa

```text
Mdot_single ~3.1e-14 kg/s.
```

Ein kleiner one-pass Loss-Cone ist aber kein stationaerer Unterdrueckungsfaktor. Fuer wiederholte Encounters gilt exakt

```text
chi_capture = p/(p+e_perm)
```

mit permanentem Escape `e_perm`.

A10 zeigte, dass selbst ein lokaler `Kn~1`-Uebergang nicht automatisch permanenten Escape bedeutet, weil die aeussere Fe/WDM-Zone kollisionsoptisch dick bleibt.

# 4. A9-A12 inner processing capacity

A9 definierte

```text
Xi = Mdot_supply / Mdot_capacity.
```

Bei Verwendung des **historischen** Supply-Benchmarks war:

```text
M=1e10 kg: supply-/transition-sensitive, teils Xi>1
M=1e11 kg: Xi_high~0.0079...0.905 je nach transition proxy
M=2e11 kg: klare Processing-Reserve
M=5e11 kg: grosse Processing-Reserve.
```

A10s first-principles-informierter Transportenvelope verengte den Vergleich weiter. Im schnellsten/escape-freundlichsten Envelope:

```text
1e10 kg: Xi_high~1.468
1e11 kg: Xi_high~2.81e-3
2e11 kg: Xi_high~4.28e-4
5e11 kg: Xi_high~3.54e-5.
```

Damit war unter dem historischen hohen Supply nur der `1e10 kg`-Unterrand capacity-overloaded.

# 5. A11/A12 dynamischer Backpressure

Mit dem aus dem historischen A10-Supply abgeleiteten `1e10 kg` Capacity-Limiter

```text
A_cap~0.681
```

bildet der zeitabhaengige sphaerische PDE-Solver einen nach aussen laufenden Backpressure-/Shock-Zweig.

A12 Hochaufloesung bei `t=0.8 r_B/c_inf`:

```text
N=128  shock~1.269 r_B, inner mdot~2.10e-2
N=256  shock~1.254 r_B, inner mdot~1.63e-2
N=512  shock~1.233 r_B, inner mdot~1.12e-2
N=1024 shock~1.229 r_B, inner mdot~6.94e-3.
```

Long-domain:

```text
t=0.8 -> shock~1.26 r_B
t=1.2 -> ~1.74 r_B
t=1.6 -> ~2.22 r_B
t=2.0 -> ~2.68 r_B.
```

Daher:

```text
stationary 1e10 shock-regulated Mdot: NOT ESTABLISHED.
```

A12b koppelte literaturgebundene Fe-Viskositaet/Waermeleitung als Reduced Sensitivitaet in die PDE. Diese Terme entfernten den Backpressure-Ast unter der historischen Capacity-Randbedingung nicht.

# 6. A12b Ionisation

A12b implementiert einen More/Thomas-Fermi-`Zbar(rho,T)`-Fit mit Fe-Korrekturfaktor `0.270`.

Erdkernreferenz:

```text
rho=13.0885 g/cm3
T=6000 K
Zbar~2.76.
```

Gegen eine publizierte solid-density Average-Atom-Definition liegt dieser Fit im Bereich `0.1...10 eV` etwa `12...16 %` niedriger. `Zbar` wird deshalb als Modell-/Definitionsband und nicht als exakte Observable verwendet.

# 7. A12c – historischer Supply wird korrigiert

## 7.1 Herkunft des Legacy-Benchmarks

Der historische Projekt-Supply war bei `M=1e16 kg` mit einer phenomenologischen Dense-Matter-Michel-EOS zu

```text
147 ... 1460 kg/s
```

berechnet und mit `Mdot~M^2` auf `M=1e11 kg` skaliert:

```text
1.47e-8 ... 1.46e-7 kg/s.
```

Dieser Bereich wird weiterhin als Regressions-/Legacy-Benchmark archiviert, aber nicht mehr als feste aeussere Rate verwendet.

## 7.2 Relativistischer stiff-EOS Michel-Test

Fuer `Gamma>5/3` ist die Newton-Bondi-Lösung nicht die richtige kritische Loesung; A12c verwendet deshalb die relativistische Michel-Kritikalitaet.

Bei gleicher PREM-Aussenbedingung und `M=1e11 kg` ergibt der **konstante-Gamma Sensitivitaetsscan**:

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

PREM besitzt am Zentrum lokal

```text
dK/dP~2.356.
```

Fuer einen reinen lokalen Polytropen ist `dK/dP=Gamma`. **Das ist nur ein lokaler stiffness proxy**. Er darf nicht unveraendert bis zum Horizon fortgesetzt werden, weil Fe/Ni vorher ionisiert, degeneriert und sein EOS-Regime wechselt.

Damit ist die Zahl `2.40e-12 kg/s` **keine neue Endrate**.

## 7.3 Korrigierter 1e10-Status

Der fruehere Satz

```text
1e10 kg -> dynamic backpressure
```

war zu allgemein. Er galt fuer den historischen hohen/soft-EOS Supply.

Mit dem A10-fast Processing-Capacity-Denominator ergibt der stiff-EOS Supply-Test etwa:

```text
Gamma=1.80  -> Xi~0.29
Gamma=1.85  -> Xi~0.081
Gamma=2.00  -> Xi~0.0034
Gamma=2.356 -> Xi~2.4e-5.
```

Im konstanten-Gamma Vergleich liegt der Capacity-Uebergang bei ungefaehr

```text
Xi=1 -> Gamma~1.756.
```

Daher lautet der aktuelle Status:

```text
M=1e10 kg:
BACKPRESSURE CONDITIONAL ON SUPPLY EOS.

soft/high supply -> capacity overload and dynamic backpressure possible
stiff/lower supply -> no capacity overload required.
```

## 7.4 >=1e11 kg

Eine niedrigere stiff-EOS Supply-Rate verschlechtert den inneren Processing-Befund nicht. Sie vergroessert die Processing-Reserve.

```text
M>=1e11 kg:
inner A9-A12 processing-capable result survives,
but the actual supply/net Mdot is reopened and EOS-dependent.
```

# 8. Aktueller Netto-Mdot-Status

Es gibt derzeit **keine belastbare einzelne finale Mdot-Zahl**.

```text
historical Michel supply: LEGACY / EOS-SENSITIVE
single-pass wave sink: not the net rate
inner processing capacity: quantitatively constrained
1e10 backpressure: conditional on outer supply EOS
>=1e11 processing: robust within current inner-transport models
final outer supply: OPEN
final net Mdot: OPEN.
```

Der aktuell wichtigste fehlende Schritt ist nicht mehr ein weiterer freier Unterdrueckungsfaktor, sondern ein **general-EOS relativistischer Michel-Eigenwert**.

# 9. Langzeit-/Waerme-Kontext

Fruehere globale Waerme-/Erdalter-Proxies wurden gegen historische Supply-Raten getestet. Da A12c die reale Supply-Spanne wieder oeffnet, muessen diese Langzeittests nach A13 mit dem neuen `Mdot_supply(EOS)`-Band erneut ausgefuehrt werden.

Keine alte Waerme-Kompatibilitaet wird als positiver Nachweis interpretiert.

# 10. Naechster Pflichtblock

```text
Stage 3.69I / A13:
PREM outer state
-> general/piecewise Fe/Ni EOS
-> relativistic variable-EOS critical point
-> Mdot_supply(EOS) band
-> A9-A12 transport/capture coupling
-> revised net Mdot_BH band
-> rerun long-term/heat constraints.
```

H+ und H0 bleiben parallel. Diese Materieclosure ist gemeinsam; H+ besitzt zusaetzliche Hawking-Terme und den bereits dokumentierten H+-Neutrinobefund.
