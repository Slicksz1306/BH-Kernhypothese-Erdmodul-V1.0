# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Reduced Stack A1–A31; Formation/Delivery F1–F8a; Multi-Gate Closure bis Stage 3.94 (F12 / A34 / H0)  
**Stand:** 29.08.2026  
**Erstveröffentlichung Erdmodul V1.0:** 23.08.2026

> `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs-/Prioritätsarchiv. Neue Rechnungen werden versioniert in Markdown und reproduzierbaren Python-Skripten fortgeschrieben.

## Wissenschaftliche Aussagegrenze

Die **SL/BH-Kernhypothese Erdmodul** ist ein quantitativer, reproduzierbarer und falsifizierbarer **theoretischer Forschungsentwurf**. Sie ist **kein experimenteller Nachweis** und derzeit **keine etablierte physikalische Theorie**.

Aktuell gilt:

```text
keine direkte Detektion eines Erdzentrum-BH
keine eindeutige positive H0-Signatur
H+ negativ im stärksten projektintern verwendeten SK-IV-Hochenergievergleich
H0 OPEN / nicht nachgewiesen
F12 physical primordial closure OPEN
A34 final multicomponent electrical Q_eq OPEN
Formation/Delivery weiterhin OPEN und stark origin-fine-tuned
interne Solver-/Regressionstests bestehen mehrere definierte Teilgates
PASS bedeutet Solver-/Regression-PASS, nicht experimentelle Evidenz
```

## Branches

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

### H+

Projekt-Hawking/Greybody-Proxy im Band `25.29...31.29 MeV`:

```text
~0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Gegen den stärksten publizierten SK-IV-Binconstraint bleibt H+ in der **projektinternen Reinterpretation FAIL**. Dies ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

### H0

```text
P_Hawking = 0
H0 = OPEN / nicht nachgewiesen.
```

Der aktive Erdbranch bleibt ein kleiner **smooth-compensated Branch**. Starke Zentralmassen-/Hard-Cavity-Varianten wurden verworfen.

PREM-Zentrumsreferenz:

```text
rho_c      ~13.08848 g/cm3
c_eff      ~10.4355 km/s
Kappa_S    ~1.4253 TPa
Pressure   ~363.852 GPa
dK/dP      ~2.356
```

Bei `M=1e11 kg`:

```text
r_B ~6.13e-8 m
r_s ~1.49e-16 m
```

---

# Aktueller Endstand – Stage 3.94

Stage 3.94 bündelt drei verbliebene reduzierte Gates in einem gemeinsamen, reproduzierbaren Modul:

```text
F12 = primordial-origin / Poisson amplification proxies
A34 = stationary Nernst-Planck/Bondi drift-diffusion sink
H0  = compensated core-density / seismic sensitivity proxy
```

Zentrale Dateien:

- `STAGE3_94_MULTI_GATE_CLOSURE.md`
- `stage3_94_multi_gate_closure.py`
- `test_stage3_94_multi_gate_closure.py`

## F12

Default:

```text
N_seed = 5.0e9
delta_P = 1/sqrt(N_seed)
        = 1.414214e-5

A_amp,proxy   = 7.0711e4
A_power,proxy = 5.0000e9
Q_NG,proxy    = 4.999929e9
```

Diese Größen sind **explizit Proxies**.

```text
physical P_zeta peak = OPEN
physical f_NL        = OPEN
```

Sie werden nicht als echtes primordiales Leistungsspektrum oder gemessenes Nicht-Gauß-Signal interpretiert.

## A34

Korrigierter stationärer Drift-Diffusionsfluss:

```text
J_r = -D Phi [dc/dr + (alpha/r^2)c]
alpha = G M m/(k_B T)
```

Für `c(r_sink)=0` und `c(R)=c_inf` lautet das korrigierte analytische Profil:

```text
c(r) = c_inf
       [1 - exp(-alpha(1/r_sink - 1/r))]
       / [1 - exp(-alpha(1/r_sink - 1/R))].
```

Ein früher zusätzlich enthaltener Faktor `exp[alpha(1/r - 1/R)]` war mit der Differentialgleichung nicht vereinbar und wurde entfernt. Die stationäre Rate selbst bleibt unverändert.

Mit

```text
D_eff  = 3e-9 m^2/s
T      = 5500 K
M      = 1e11 kg
m      = 55.845 u
r_sink = 6.13e-8 m
R      = 1e5 m
c_inf  = 1 m^-3
Phi    = 1
```

folgt:

```text
alpha        = 8.1507e-6 m
alpha/r_sink = 132.96
dotN         ~3.07273e-13 s^-1
```

Die Rate ist eine Rate **pro gewählter Referenzkonzentration**. Sie ist kein finales reales `Mdot` und insbesondere kein finales elektrisches Gleichgewicht:

```text
final multicomponent Q_eq = OPEN
```

## H0

Korrigiertes Default-Kompensationsprofil:

```text
r_core      = 1 km
r_outer     = 2 km
delta_rho_0 = 100 kg/m^3
```

Die äußere konstante Kompensationsschale folgt aus

```text
integral 4 pi r^2 delta_rho(r) dr = 0
```

und ergibt:

```text
delta_rho_shell = -5.714286 kg/m^3
```

Damit ist der reduzierte Perturbationsbranch innerhalb `r_outer` massenkompensiert.

Entscheidend bleibt:

```text
unique H0 delta_rho/delta_Vp/delta_Vs prediction = OPEN
direct H0 detection = NONE
```

## Stage-3.94 Tests

`test_stage3_94_multi_gate_closure.py`:

```text
14/14 regression tests PASS
```

Die drei ergänzten A34-Regressionen prüfen unabhängig von den Randwerten:

```text
ODE-Residual auf 400 logarithmischen Radialpunkten: max epsilon < 1e-6
radiale Flusserhaltung dotN(r):              relative Streuung < 1e-6
Innenprofil bei r=2 r_sink:                  keine exponentielle Überhöhung
```

Damit bedeutet der A34-PASS eine konsistente reduzierte stationäre Ein-Spezies-Lösung. Das finale multikomponentige elektrische `Q_eq` bleibt **OPEN**; daraus folgt kein experimenteller Nachweis eines Erdzentrum-BH.

Zusätzlich läuft der gemeinsame Smoke-Sweep:

```text
F12: 50 Punkte
A34: 50 Punkte
H0 : 50 Punkte
```

ohne Solverfehler.

---

# Reduced Stack A1–A31

Wichtige bisherige Resultate:

```text
Schwarzschild-Dirac Regressionen: PASS
Proton @1e11 kg: ~0.9503 classical
Fe-56 @1e11 kg: ~0.99754 classical
Ni-58 @1e11 kg: ~0.99646 classical
large coherent Fe/Ni wave suppression: NOT FOUND
repeated-encounter recycling included
naive local Kn~1 = permanent escape: REJECTED
A13/A13b relativistic outer supply: PARTIAL CALCULATED
A14 dense-core screening: PARTIAL
A15 reduced throughput >=1e11 kg: processing-capable in tested stack
A16 hard 47-TW total-budget pretest: NO EXCLUSION
A17 microscopic near-zone seismics: not a useful direct channel
A18 H+ strongest-SK-IV project comparison: FAIL
A19 normal halo -> Earth capture: VERY STRONG FAIL
A20-A31 charge/WDM transport: partial closure
exact multicomponent Q_eq: OPEN
```

Der verbleibende Transportengpass ist insbesondere:

```text
multicomponent Onsager / Maxwell-Stefan mobility matrix
+ thermodynamic chemical-potential derivatives
+ sink-boundary coupling
```

---

# Formation / Delivery F1–F8a

Kurzstatus:

```text
normal halo -> direct Earth: VERY STRONG FAIL
protoplanetary gas drag: insufficient
normal halo -> protostellar cloud: insufficient as generic terrestrial supply
temporary Hill capture: dynamically allowed
smooth terrestrial pull-down: FAIL as generic channel
giant-impact / embryo-exchange routes: conditional kinematic existence
absolute delivery probability: OPEN
```

## F5 – Restricted 4-body Exchange

Persistenz bis `20 Omega^-1 ~3.18 yr`:

```text
STRONG 5/300 = 1.67%
BROAD  3/300 = 1.00%
WEAK   0/300
```

Status:

```text
local collisionless embryo-exchange mechanism: PASS conditionally
generic formation probability: NOT ESTABLISHED
```

## F6 – Population-weighted Gate

Referenz:

```text
M1=0.03 M_E
K_F5=5/300
N_enc=10
S_post=0.5
P_target=0.5
mu_H,50=8.318 seeds per Proto-Earth Hill volume
```

Normaler Galactic-halo-Abundance-Branch reicht nicht aus.

## F7 / F8a – Origin Rescue

Standard-Galactic-Origin-Channels bleiben für die notwendige kalte 1-AU-Phasenraumdichte stark negativ.

F8a findet konditionale präsolare Minihalo-/Stream-Kandidaten sowie einen post-collapse co-orbital Torus-Target-State-Parameterraum, aber:

```text
candidate grid cells != astrophysical probability
formation origin != established
long-term retention != established
present-day compatibility != established
absolute Earth delivery = OPEN
```

Zentrale Datei:

- `STAGE3_80_F8_SUBSTRUCTURE_SCAN.md`

---

# Reproduktion

Python-Abhängigkeiten:

```bash
pip install -r requirements.txt
```

Stage 3.94:

```bash
python stage3_94_multi_gate_closure.py
python -m unittest -v test_stage3_94_multi_gate_closure.py
```

F8a:

```bash
python -m unittest -v test_stage3_80_f8_substructure_scan.py
```

---

# Projektstruktur / zentrale Statusdateien

- `THEORIE.md` – theoretischer Rahmen.
- `TEST_STATUS.md` – historischer Test-/Validierungsstand bis F8a.
- `STAGE3_94_MULTI_GATE_CLOSURE.md` – aktueller Multi-Gate-Closure-Stand.
- `AKKRETION_STATUS.md` – Akkretions-/Transportstatus.
- `REDUCED_STACK_CLOSURE_A19.md` – A1–A19 Reduced Stack.
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md` – verbleibende multikomponentige Charge-Closure.
- `STAGE3_80_F8_SUBSTRUCTURE_SCAN.md` – F8a Origin-/Substructure-Gate.
- `CHANGELOG.md` – öffentliche Entwicklungshistorie.
- `CITATION.cff` – Zitiermetadaten.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; aktueller Rechenstand bis Stage 3.94, Rheinland-Pfalz, Deutschland.
