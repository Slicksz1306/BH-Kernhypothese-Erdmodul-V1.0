# Stage 3.69 / 3.70 – verbleibende Validierungsprotokolle

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Gesamtstatus:** Stage 3.69 Full-Multiphysics OPEN; Reduced Teilmodule bis Stage 3.69E/A-9 numerisch bearbeitet; Stage 3.70 NOT PERFORMED

## Branches

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben parallel. Gemeinsame Materie-/Capture-/Transportmodule gelten fuer beide; H+ besitzt zusaetzliche Hawking-Quell-/Emissionskanaele.

# Stage 3.69 – High-Fidelity Multiphysics

Ziel ist eine selbstkonsistente Verbindung

```text
PREM/global supply
 -> Rheologie / Dense Fe-Ni EOS
 -> collisional transport
 -> kinetic/recycling transition
 -> species/composition closure
 -> wave capture
 -> charge feedback
 -> nuclear/reaction timescales
 -> horizon sink
 -> net Mdot_BH(t), Q(t).
```

## Bereits bearbeitete Teilmodule

### A1/A3 – Schwarzschild-Dirac + Earth-speed Proton

- massiver Schwarzschild-Dirac-Radialsolver: IMPLEMENTED
- regular horizon branch: IMPLEMENTED
- current/Wronskian self-check: PASS
- in/out partial-wave matching: IMPLEMENTED
- low-alpha externe Regression: PASS
- intermediate-alpha Struktur: PASS qualitativ/numerisch

Bei `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
sigma_p ~2.1741e-22 m^2
sigma_p/sigma_classical ~0.9503.
```

### A4 – Charged Proton Dirac + Charge Feedback

Bei `M_BH=1e11 kg`:

```text
Q=0 e      -> sigma_p ~0.949...0.950 classical
Q=3.67 e   -> ~0.889 classical
Q=10 e     -> ~0.765 classical
Q=24.18 e  -> ~0.517 classical.
```

```text
charge feedback: relevant
orders-of-magnitude proton stop: not found in tested Q range
charged electron far-field Coulomb matching: OPEN.
```

### A5 – Fe/Ni 0+ Composite Wave Capture

Bei `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
Fe-56: sigma/sigma_classical ~0.9975
Ni-58: sigma/sigma_classical ~0.9965.
```

Keine starke kohärente Wellenunterdrueckung gefunden.

Dense-screening Reduced Proxy:

```text
r_B ~6.13e-8 m
lambda_screen ~few 1e-11 ... 1e-10 m.
```

### A6 – Reduced Recycling Closure

Die naive Identifikation

```text
small single-pass capture fraction -> equally small stationary Mdot
```

ist nicht zulaessig, wenn Misses lokal verbleiben und erneut gestreut/rethermalisiert werden.

Exakt fuer repeated encounters:

```text
chi_capture = p/(p+e_perm).
```

### A7 – Collision-Regime + 1-D Bondi Backpressure

Strong-coupling/geometrischer Sensitivitaetsbranch:

```text
rho~r^-3/2
lambda_mfp~r^3/2
Kn~r^1/2
```

=> `Kn` sinkt nach innen.

Weak-coupling Coulomb/Spitzer-like:

```text
lambda_C~T^2/n
Kn~r^-3/2
```

=> entgegengesetzter Trend, aber nur bei tatsaechlichem weak coupling gerechtfertigt.

Der 1-D-Bondi-Euler-Benchmark reproduziert den analytischen transsonischen Massenfluss auf Prozentniveau. Ein reflektierender Innenrand kann Backpressure und einen outward shock erzeugen.

### A8 – Dense Fe Regime + Electron-Capture Timescales

Reduced inward Proxy:

```text
rho~x^-3/2
T~x^-1
Gamma_i~x^1/2.
```

Free-Fermi EC-Schwellen:

```text
58Ni -> 58Co: x~1.66e-4
56Fe -> 56Mn: x~5.08e-6.
```

An beiden Schwellen bleibt der hochionisierte Fe-Proxy strong-coupled (`Gamma_i>>1`).

Ein publizierter schneller `56Fe`-EC-Vergleich

```text
lambda_ec~1.5916e4 s^-1
```

ist bereits gegen die lokalen Einmal-/Transitzeiten viel zu langsam fuer promptes Weak-Equilibrium.

### A9 – Residence / Backpressure / Minimal Weak Network

A9 verbindet erstmals repeated encounters, permanenten Escape, Reservoir-Kapazitaet, Bulk-Quasineutralitaet und Weak-Reaction-Gates.

#### Exact repeated-encounter closure

```text
p       = capture per encounter
e_perm  = permanent escape per encounter
recycle = 1-p-e_perm

chi_capture = p/(p+e_perm).
```

Bei `e_perm~0`:

```text
t_res=t_cycle/p.
```

#### Strong-coupling escape bracket

Mit

```text
lambda=lambda_0 x^3/2
```

folgt

```text
tau_coll=2 r_B/lambda_0 [x_t^-1/2 - 1].
```

Die instantane Maxwell-Fraktion `v>v_esc` ist im A7-Scaling etwa `0.343`, aber permanenter ballistischer Escape wird durch `exp(-tau_coll)` unterdrueckt. An den getesteten atomaren Skalen ist `tau_coll~1e3...>1e5`; im Reduced Strong-Coupling-Branch ist daher `e_perm` praktisch null und `chi_capture~1`.

#### Processing capacity @ `1e11 kg`

| `r_t` | `p` | `t_res` [s] | `Mdot_capacity` [kg/s] | `Xi_high` |
|---:|---:|---:|---:|---:|
| `3e-11 m` | `3.30e-5` | `1.36e-12` | `1.85e-5` | `0.0079` |
| `1e-10 m` | `9.90e-6` | `2.76e-11` | `9.13e-7` | `0.160` |
| `2e-10 m` | `4.95e-6` | `1.56e-10` | `1.61e-7` | `0.905` |

```text
Xi = Mdot_supply/Mdot_capacity.
```

Damit kann der aktuelle Reduced Strong-Coupling/Recycling-Branch bei `1e11 kg` den gesamten historischen Supply-Benchmark fuer alle getesteten atomaren Transition-Skalen verarbeiten.

#### Massenscan

```text
1e10 kg: BACKPRESSURE-SENSITIVE / OPEN
1e11 kg: supply-processing capable in tested strong-coupling bracket
2e11 kg: clear capacity reserve
5e11 kg: very large capacity reserve.
```

Kritischer Reduced-Uebergang:

```text
xcrit low supply  ~8.507e-3
xcrit high supply ~3.397e-3.
```

Fuer feste `r_t=3e-11...2e-10 m` ergibt sich grob

```text
Mcrit ~5.8e9 ... 9.6e10 kg.
```

#### Weak-reaction gate

Bei `M=1e11 kg`:

```text
Ni threshold:
  t_res~9.13e-14 s
  lambda_required~1.10e13 s^-1

Fe threshold:
  t_res~1.50e-17 s
  lambda_required~6.69e16 s^-1.
```

Damit bleibt der schnelle Reduced Supply-Processing-Branch weit von promptem Weak-Equilibrium entfernt.

#### Reduced Mdot consequence

Fuer `M>=~1e11 kg` im aktuellen Strong-Coupling/Recycling Reduced Branch:

```text
chi_transport~1.
```

Am `1e11 kg`-Referenzpunkt:

```text
Mdot_BH,reduced ~1.47e-8 ... 1.46e-7 kg/s.
```

Dies ist **keine Messung und keine first-principles WDM-Endrate**. Es ist die Konsequenz der aktuell miteinander konsistenten Reduced Closures.

# Naechster Pflichtblock – Stage 3.69F / A10

A10 soll den entscheidenden geometrischen Mean-Free-Path-/Strong-Coupling-Proxy durch first-principles-informierte Dense-Matter-Transportkoeffizienten ersetzen.

Mindestziel:

```text
WDM Fe/Ni EOS + average ionization
 -> electron-ion / ion-ion relaxation and transport
 -> species/energy-dependent e_perm(r,E)
 -> time-dependent hydro/kinetic coupling
 -> A4/A5 absorptive inner sink
 -> chi_transport without hand-set geometric lambda
 -> final reduced species-resolved Mdot band.
```

Akzeptanzkriterien:

1. keine freie Wahl von `chi_transport`;
2. Transportkoeffizienten aus publizierten WDM-/core-Fe-Modellen oder klarer Sensitivitaetsbracket;
3. Massenerhaltung im zeitabhaengigen radialen Solver;
4. absorbierender und Backpressure-Grenzfall reproduziert;
5. `1e10...5e11 kg` Massenscan;
6. Unsicherheitsband fuer `Mdot`, `Q`, Residence und Escape;
7. keine Promotion zum Full-Physics-PASS, solange first-principles EOS/transport nicht ausreichend geschlossen ist.

# Mindest-Meilenstein fuer Abschluss von Stage 3.69

Ein gekoppelter 1-D/2-D-Prototyp muss mindestens liefern:

```text
Mdot_BH(t)
Q(t)
rho(r,t), T(r,t), Ye(r,t)
charge-state / composition fractions
transport/recycling efficiency chi_transport
energy deposition / escaping luminosity
branch-specific observables.
```

Bis dahin bleibt

```text
Stage 3.69 Full-Multiphysics: OPEN
final first-principles species-resolved net Mdot_BH: OPEN.
```

# Stage 3.70 – Experimental branch-specific falsification

**Status:** DEFINED / NOT PERFORMED

Stage 3.70 beginnt erst mit quantitativen Stage-3.69-Endvorhersagen.

Moegliche Kanaele:

1. H+ Hawking-spezifisch: Neutrino-/Gamma-Spektren.
2. H+/H0 gemeinsame Materiesignaturen: Waerme, Rotation/Magnetfeld, Transportprodukte.
3. 3-D-Seismik nur bei makroskopisch gekoppelter Struktur.
4. Materieprozess-Neutrinos nur nach species-/reaction-resolved Vorhersage.

# Konservativer Projektstatus

```text
H+ Standard-Hawking:
    FAIL im getesteten SK-IV-Projekt-Reinterpretationsmodell;
    Branch bleibt separat dokumentiert.

H0:
    OPEN / nicht nachgewiesen.

A1/A3/A4/A5:
    wave/capture Teilprobleme deutlich eingeengt.

A6/A7/A8/A9:
    transport/recycling/coupling/reaction closure deutlich eingeengt;
    >=~1e11 kg supply-processing capable im aktuellen Reduced Strong-Coupling-Branch;
    1e10 kg backpressure-sensitive.

Formation:
    stark negativ / kein Standardweg hergeleitet.

Empirischer Nachweis eines Erdzentrum-BH:
    keiner.
```

# Reproduzierbare aktuelle Stage-Dateien

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
- `STAGE3_69F_A10_PLAN.md`
