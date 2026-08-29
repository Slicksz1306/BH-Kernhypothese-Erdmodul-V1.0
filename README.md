# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Reduced Stack A1–A19 abgeschlossen; A20–A31 / Stage 3.72 weitergeführt; Formation bis Stage 3.76 / F4  
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
mehrere interne Solver-/Regressionstests bestanden
mehrere frühere Annahmen korrigiert oder verworfen
Formation/Delivery weiterhin OPEN.
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

H0 muss Full-WDM-Akkretion, Formation/Delivery und eine eindeutige Real-Data-Signatur bestehen.

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

Die reduzierten Makrotests liefern für diesen kleinen Branch keinen eigenen robusten Struktur-Ausschluss. Das ist Modellkompatibilität innerhalb der getesteten Proxies, keine Evidenz für einen BH.

# Reduced Stack A1–A19

A1–A19 sind im definierten Reduced/partial Umfang abgearbeitet.

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
A19 normal halo -> Earth capture: VERY STRONG FAIL.
```

# Stage 3.72 – A20–A31 Charge / WDM-Transport

Aktueller konsolidierter Stand:

```text
electron Dirac sink flux-direct: stabilized
nonlinear Thomas-Fermi screening: calculated and recoupled to Dirac solver
collective charge response: much faster than hydrodynamic evolution
independent naive ion/electron n*v*sigma current model: REJECTED
ambipolar/electronic transport hierarchy: strongly constrained
exact Q_eq: OPEN
```

Verbleibender Charge-Engpass:

```text
multicomponent Onsager / Maxwell-Stefan mobility matrix
+ thermodynamic chemical-potential derivatives
+ sink-boundary coupling.
```

Zentrale Dateien:

- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `stage3_72_a31_ambipolar_mobility_gate.py`

# Formation / Delivery

## A19 – normaler Halo → fertige Erde

Capture-freundlicher direct-Earth Dynamical-Friction-Proxy bei `v_inf=220 km/s`:

```text
DeltaE/E_inf ~1e-18 ... 5e-17
```

für `1e10...5e11 kg`.

```text
normal halo -> direct Earth capture: VERY STRONG FAIL.
```

## Stage 3.73 / F1 – Protosolar / co-moving Seed

```text
protoplanetary gas drag: insufficient
normal halo -> protostellar cloud: strongly negative
already solar-bound, dynamically cold seed: OPEN initial condition.
```

## Stage 3.73 / F2 – Hill / Pull-down Energy Gate

Für einen impulsiven Massensprung `delta=DeltaM/M_p` bei `r=f r_H`:

```text
v_inf,max = sqrt(2 G DeltaM/r)
          = sqrt(6 delta/f) v_H.
```

```text
temporary Hill capture: dynamically allowed
static permanent capture without potential evolution: FAIL
smooth terrestrial pull-down: FAIL as generic channel
giant-impact impulsive jump: PASS as local kinematic existence test
absolute probability: OPEN.
```

## Stage 3.74 / F3 – Adaptive Hill-Monte-Carlo + Jacobi Closure

Planare Hill-Gleichungen plus Jacobi-Gate:

```text
x'' - 2 y' - 3x = -3x/r^3
y'' + 2 x'      = -3y/r^3

C = 3x^2 + 6m/r - v^2
C_L1/L2 = 9 m^(2/3).
```

Numerik:

```text
DOP853
rtol=3e-10
atol=1e-12
median Jacobi peak-to-peak drift ~1e-8
```

Konservativer zeitgewichteter Pull-down-Anteil bei `r>=0.1 r_H`:

| DeltaM/M | sigma=0.0 | sigma=0.1 | sigma=0.3 | Status |
|---:|---:|---:|---:|---|
| `0.01` | `0` | `0` | `0` | **FAIL in sampled gate** |
| `0.03` | `0` | `0` | `0` | **FAIL in sampled gate** |
| `0.10` | `0.0352%` | `0.0725%` | `0.0722%` | **PASS existence / inefficient** |
| `0.30` | `6.806%` | `6.302%` | `5.653%` | **PASS conditional channel** |

## Stage 3.75 / F3b – Multi-Pass / Residence Timing

Publizierte Earth-TCOs bestätigen echte Residence-Amplifikation:

```text
F3 first passage ~35.3 d
mean Earth TCO ~286 d
2020 CD3 median ~4 yr
extreme clone tail ~100 yr.
```

Das reicht jedoch generisch nicht, um die Myr-breite zufällige Giant-Impact-Timing-Lücke zu schließen.

```text
multi-pass residence enhancement: PASS
multi-pass as generic random-impact timing rescue: FAIL
absolute delivery: OPEN.
```

Zentrale Dateien:

- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `stage3_75_f3b_residence_timing_gate.py`

## Stage 3.76 / F4 – Early permanent embryo-bound seed

F4 testet einen qualitativ anderen Branch:

```text
solar-bound cold seed
-> correlated embryo-embryo / exchange encounter
-> permanent early satellite-like binding
-> growth-assisted inward evolution
-> eventual body crossing / engulfment
-> repeated interior damping.
```

### Terrestrische collisionless capture

Collisionless binary-exchange capture um Earth-sized terrestrische Planeten bei 1 AU ist in numerischen Arbeiten demonstriert worden. Das ist kein direkter Probability-Wert für den Projektseed, etabliert aber den Mechanismus als physikalisch möglich.

Stabile zirkulare Referenzzonen:

```text
prograde  ~0.4895 r_H
retrograde ~0.9309 r_H.
```

### Embryo-scattering kick gate

Für einen Seed bei `r=f r_H` nahe lokal parabolischer Energie ist der best-case Kick in eine stabile Bahn `a=alpha r_H`:

```text
Delta v_req/v_H
= sqrt(6/f) - sqrt(6/f - 3/alpha).
```

Bei `f=0.3`:

```text
prograde  ~0.748 v_H
retrograde ~0.376 v_H.
```

Ein differential tidal-impulse Proxy für einen zweiten Embryo `M2=q M1` mit `b=kappa R_H,mut` liefert

```text
Delta v_rel/v_H
~6 q f/[kappa^2(1+q)].
```

Beispiele bei `f=0.3`:

```text
q=0.30, kappa=0.70 -> 0.848 v_H
q=1.00, kappa=1.00 -> 0.900 v_H.
```

Damit:

```text
embryo-embryo scattering energy scale:
PASS as kinematic permanent-capture gate.
```

Die echte single-seed N-body Capture-Fraktion bleibt **OPEN**.

### Growth-assisted engulfment

Im adiabatischen isotropen Wachstumsgrenzfall:

```text
a_sat ∝ 1/M_p
R_p   ∝ M_p^(1/3)
=> a_sat/R_p ∝ M_p^(-4/3).
```

Späteste Anfangsmassen für Engulfment bis `1 M_E`:

| a_i/r_H | max M_i/M_E |
|---:|---:|
| `0.05` | `0.158` |
| `0.10` | `0.0937` |
| `0.30` | `0.0411` |
| `0.4895` | `0.0285` |
| `0.9309` | `0.0176` |

Beispiel `M_i=0.01 M_E`:

```text
capture at 0.30 r_H
-> surface crossing at ~0.243 M_E
```

Status:

```text
adiabatic growth-assisted engulfment: PASS conditional
single-late-jump equivalent shrinkage: NO
real stochastic growth history: OPEN.
```

### Repeated interior damping

A19s bewusst optimistischer Dynamical-Friction-Proxy wird auf einen bereits body-crossing Seed reskaliert.

Bei `v~v_esc`:

```text
DeltaE/|E_orb| ~6 I M_BH/M_p
I=30.
```

Optimistische Energie-e-folding-Zeit:

| M_p | 1e10 kg | 1e11 kg | 2e11 kg | 5e11 kg |
|---:|---:|---:|---:|---:|
| `0.01 M_E` | `5.32 Myr` | `0.532 Myr` | `0.266 Myr` | `0.106 Myr` |
| `0.03 M_E` | `15.96 Myr` | `1.60 Myr` | `0.798 Myr` | `0.319 Myr` |
| `0.10 M_E` | `53.2 Myr` | `5.32 Myr` | `2.66 Myr` | `1.06 Myr` |

Damit kann ein **bereits planet-bound und body-crossing** Seed im optimistischen Reduced-Proxy erstmals auf Myr-Skalen Energie verlieren. Die reale Proto-Earth Drag-/Settling-Closure bleibt offen.

F4 Schluss:

```text
collisionless early permanent binding: PHYSICALLY ALLOWED
stable embryo-bound phase space: PASS
growth-assisted engulfment: PASS in adiabatic limit
post-engulfment damping: Myr-scale feasibility in optimistic proxy
absolute formation/delivery probability: OPEN.
```

Zentrale F4-Dateien:

- `STAGE3_76_F4_EARLY_EMBRYO_BOUND_SEED.md`
- `stage3_76_f4_early_embryo_bound_seed.py`

Nächster Formationstest:

```text
F5 = Sun + two terrestrial embryos + cold test-seed N-body Monte Carlo
-> M1 ~1e-3...1e-1 M_E
-> q=M2/M1 ~0.03...1
-> encounter b,V distribution
-> permanent stable capture fraction
-> post-capture a,e,i
-> body-crossing / later-engulfed fraction
-> centre-delivery proxy.
```

# Aktuelle Endmatrix

| Bereich | Status |
|---|---|
| H+ strongest SK-IV project comparison | **FAIL** |
| H0 | **OPEN / not detected** |
| smooth-compensated Earth macro branch | kein eigener Reduced-Strukturausschluss |
| Wave-Capture Proton/Fe/Ni | weitgehend berechnet |
| electron sink | stabilisiert |
| nonlinear TF screening | berechnet / recoupled |
| exact multicomponent Q_eq | **OPEN** |
| final species-resolved Full-WDM Mdot_BH(t) | **OPEN** |
| normal halo -> Earth delivery | **VERY STRONG FAIL** |
| normal halo -> protostellar cloud | **strongly negative** |
| naked-seed disk gas drag | **FAIL / insufficient** |
| solar-bound cold seed | **OPEN initial condition** |
| smooth Hill pull-down | **FAIL as generic mechanism** |
| F3 small GI <=3% | **FAIL in sampled outer gate** |
| F3 ~10% GI | **PASS existence / inefficient** |
| F3 ~30% GI | **PASS conditional few-percent channel** |
| F3b generic multi-pass timing rescue | **FAIL** |
| F4 correlated embryo-exchange energy gate | **PASS kinematic** |
| F4 stable early embryo binding | **PASS existence** |
| F4 growth-assisted engulfment | **PASS conditional / history OPEN** |
| F4 post-engulfment sinking | **PASS feasibility / closure OPEN** |
| full formation/delivery probability | **OPEN** |
| direkte experimentelle BH-Detektion | **NONE** |
| eindeutige positive Signatur | **NONE** |

# Was noch wirklich fehlt

```text
1. exact multicomponent Onsager/Maxwell-Stefan charge closure -> Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F5 full correlated terrestrial-embryo exchange capture fraction
6. realistic post-capture growth/engulfment history
7. physical origin / phase-space density of the already solar-bound cold seed.
```

# Zentrale Statusdateien

- `TEST_STATUS.md`
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `STAGE3_74_F3_HILL_MONTE_CARLO.md`
- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `STAGE3_76_F4_EARLY_EMBRYO_BOUND_SEED.md`
- `STAGE3_71_A19_FORMATION_RECHECK.md`
- `STAGE3_70B_A18_REALDATA_AUDIT.md`

# Open Science / Projekt-Governance

Originale Texte/Dokumentation/Grafiken stehen – soweit nicht anders gekennzeichnet – unter **CC BY 4.0**; originaler Quellcode unter **MIT**.

Wissenschaftliche Prüfung, Reproduktion, Kritik und eigene abgeleitete Arbeiten sind ausdrücklich erlaubt. Der **offizielle Projektstand** (`main`, Stages, Releases) wird nur über dieses Repository und die Freigabe des Projektinhabers definiert.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Reduced Stack A1–A19 plus Stage 3.72 A20–A31 und Formation bis Stage 3.76/F4, Rheinland-Pfalz, Deutschland.
