# Akkretions- und Langzeitstatus – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Forschungsstand:** Materie-/Capture-/Transportstack bis A13 partiell bearbeitet; reale tabellierte Fe/Ni-Supply und finale Netto-`Mdot` offen

## Aussagegrenze

Die reale BH-Akkretionsrate ist eine gekoppelte Groesse:

```text
outer relativistic supply(EOS)
-> dense-matter transport/recycling/backpressure
-> charge/composition
-> inner wave capture
-> net Mdot_BH.
```

Daher gilt:

```text
Mdot_net != automatisch Mdot_Michel
Mdot_net != automatisch p_single * Mdot_supply
historical Michel benchmark != universal supply rate.
```

Der historische Projektbereich bleibt **LEGACY / EOS-SENSITIVE**.

# 1. PREM outer boundary

Am Erdzentrum:

```text
rho_inf ~13.08848 g/cm3
P_inf   ~363.8521 GPa
K_S     ~1.4253 TPa
dK/dP   ~2.356
c_s     ~10.4355 km/s.
```

Bei `M=1e11 kg`:

```text
r_B ~6.13e-8 m
r_s ~1.49e-16 m.
```

# 2. Innerer Capture-Sink

Bei `M=1e11 kg`, Earth-speed:

```text
proton: sigma/sigma_classical ~0.9503
Fe-56:  ~0.99754
Ni-58:  ~0.99646.
```

Eine grosse Wellenunterdrueckung wurde nicht gefunden.

Charged-Proton-Sensitivitaet:

```text
Q=0 e      -> ~0.949 classical
Q=3.67 e   -> ~0.889
Q=10 e     -> ~0.765
Q=24.18 e  -> ~0.517.
```

Charged-electron long-range Coulomb matching bleibt OPEN.

# 3. Recycling / permanenter Escape

Ein kleiner one-pass Loss-Cone ist kein stationaerer Unterdrueckungsfaktor. Fuer wiederholte Encounters:

```text
chi_capture = p/(p+e_perm).
```

A10 zeigt zusaetzlich:

```text
local Kn~1 != permanent escape through the outer dense Fe/WDM reservoir.
```

# 4. A9-A12 Processing Capacity

Unter dem historischen hohen Supply lieferte A10-fast:

```text
M=1e10 kg: Xi_high~1.468
M=1e11 kg: Xi_high~2.81e-3
M=2e11 kg: Xi_high~4.28e-4
M=5e11 kg: Xi_high~3.54e-5.
```

Damit war nur der `1e10 kg`-Unterrand capacity-overloaded.

A11/A12 zeigten fuer diesen historischen `1e10 kg` Capacity-Limiter einen nach aussen laufenden Backpressure-Shock. Die Shockposition konvergierte, eine stationaere endliche `Mdot` aber nicht.

A12b zeigte, dass literaturgebundene Fe-Viskositaet/Waermeleitung den Backpressure-Ast unter dieser historischen Randbedingung qualitativ nicht entfernen.

# 5. A12b Ionisation

More/Thomas-Fermi Fe-Closure am Erdkernreferenzpunkt:

```text
rho=13.0885 g/cm3
T=6000 K
Zbar~2.76.
```

Gegen eine publizierte solid-density Average-Atom-Definition liegt der korrigierte Fit bei `0.1...10 eV` etwa `12...16 %` niedriger. `Zbar` bleibt ein Modell-/Definitionsband.

# 6. A12c – Supply-Korrektur

Historischer Benchmark bei `M=1e11 kg`:

```text
1.47e-8 ... 1.46e-7 kg/s.
```

Dieser Bereich ist nicht universell. Im relativistischen constant-Gamma Sensitivitaetstest:

| Gamma | Mdot [kg/s] |
|---:|---:|
| `1.75` | `1.19e-7` |
| `1.80` | `2.89e-8` |
| `1.85` | `8.02e-9` |
| `2.00` | `3.35e-10` |
| `2.20` | `1.50e-11` |
| `2.356` local PREM proxy | `2.40e-12` |

`Gamma=2.356` darf nicht unveraendert bis zum Horizon fortgesetzt werden. Die letzte Zahl ist ein **constant-stiffness Stresslimit**, keine bevorzugte Endrate.

# 7. A13 – general-EOS relativistischer Supply

A13 implementiert die Michel-Kritikalitaet fuer eine allgemeine thermodynamisch konsistente barotrope/isentrope EOS.

```text
4 pi r^2 rho0 u = Mdot
h sqrt(1 - 2M/r + u^2) = h_inf
```

Am kritischen Punkt:

```text
u_s^2 = a_s^2/(1+3 a_s^2)
r_s/M = (1+3 a_s^2)/(2 a_s^2)
h_s/sqrt(1+3 a_s^2) = h_inf.
```

Der Solver reproduziert die A12c constant-Gamma-Werte mit relativen Drifts von etwa `1e-5...1e-4`:

```text
general-EOS solver regression: PASS.
```

## Kontrolliertes variable-EOS Surrogat

A13 matched PREM `P`, `K_S` und `dK/dP` am Aussenrand. Die lokale PREM-Steifigkeit wird nur bis

```text
rho_soft=30 ... 47.2 g/cm3
```

gehalten. Danach wird transparent

```text
beta_mid=1.4 ... 1.8
```

variiert; tief innen geht der Surrogatast um den Elektronen-Relativitaetsmarker mit Sensitivitaet `1e5...1e7 g/cm3` gegen `beta=4/3`.

Dies ist kein statistisches Konfidenzintervall und keine finale Fe/Ni-EOS.

Bei `M=1e11 kg` ergibt dieser kontrollierte Scan:

```text
Mdot_supply,surrogate ~4.64e-8 ... 1.37e-6 kg/s.
```

Damit gilt:

```text
constant PREM stiffness to horizon -> stress limit only
variable EOS softening -> supply can return to historical range or above.
```

# 8. Neue Capacity-Reklassifikation

A13-Surrogat gekoppelt an die bereits berechneten A10-fast Processing-Capacities:

| M_BH | Mdot_min [kg/s] | Mdot_max [kg/s] | Xi_min | Xi_max |
|---:|---:|---:|---:|---:|
| `1e10` | `4.64e-10` | `1.37e-8` | `0.467` | `13.76` |
| `1e11` | `4.64e-8` | `1.37e-6` | `8.94e-4` | `2.64e-2` |
| `2e11` | `1.86e-7` | `5.47e-6` | `1.36e-4` | `4.01e-3` |
| `5e11` | `1.16e-6` | `3.42e-5` | `1.12e-5` | `3.32e-4` |

Daraus folgt fuer das **getestete A13-Surrogat**:

```text
M>=1e11 kg:
Xi_max <<1 -> inner processing-capable result survives robustly.

M=1e10 kg:
Xi crosses 1 -> Backpressure remains supply/EOS conditional.
```

Der fruehere Satz `1e10 kg -> Backpressure` bleibt damit korrigiert: nur ausreichend weiche/high-supply EOS-Aeste ueberlasten die aktuelle innere Capacity.

# 9. Realer Liquid-Fe-Anker fuer A13b

Grant et al. (2021) messen eine elevated liquid-Fe isentrope von etwa `275...400 GPa` und berichten sehr gute Uebereinstimmung mit SESAME 92141.

Publizierte Fitparameter bei der 7000-K-Referenz:

```text
K0     = 25.3 +/- 4.0 GPa
K0'    = 6.60 +/- 0.33
gamma0 = 2.42 +/- 0.12
rho0   = 5.187 g/cm3 reference.
```

Die Arbeit verweist auf einen oeffentlichen Datensatz unter Zenodo DOI `10.5281/zenodo.4464112`. Der Datensatz konnte in der aktuellen Tool-Session nicht stabil maschinenlesbar abgerufen werden; es wurden daher **keine Punkte aus Figuren erfunden oder per Hand digitalisiert**.

# 10. Aktueller Netto-Mdot-Status

```text
historical Michel supply: LEGACY / EOS-SENSITIVE
A13 general-EOS machinery: PASS regression
A13 variable-EOS surrogate: CALCULATED
M>=1e11 inner processing: robust in tested surrogate
M=1e10 backpressure: supply/EOS conditional
real tabulated Fe/Ni outer supply: OPEN
charged-electron capture: OPEN
final species-resolved net Mdot: OPEN.
```

# 11. Langzeit-/Waerme-Tests

Fruehere Langzeit-/Waermechecks wurden mit dem historischen Supply ausgefuehrt. Sie muessen nach A13b mit einem realeren tabellierten `Mdot_supply`-Band neu gerechnet werden.

# 12. Naechster Pflichtblock – A13b

```text
public liquid-Fe isentrope / SESAME-consistent data ingestion
-> thermodynamic h(rho) reconstruction
-> general-EOS Michel directly on tabulated/interpolated data
-> final defensible outer-supply bracket
-> recouple A9-A12
-> rerun heat/age constraints.
```

H+ und H0 bleiben parallel. Diese Matter-Closure ist gemeinsam; H+ besitzt zusaetzliche Hawking-Terme und den bereits dokumentierten H+-Neutrinobefund.
