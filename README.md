# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Reduced Stack A1–A19 abgeschlossen im definierten Umfang; A20–A31 / Stage 3.72 weitergeführt; Formation bis Stage 3.75 / F3b  
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
Formation/Delivery weiterhin OPEN und stark eingeschränkt.
```

## Branches

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Die Branches werden strikt getrennt.

### H+

Der Projekt-Hawking/Greybody-Proxy im Band `25.29...31.29 MeV` liegt bei ungefähr

```text
0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Gegen den stärksten publizierten SK-IV-Binconstraint bleibt H+ in der **projektinternen Reinterpretation FAIL**. Dies ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

### H0

```text
P_Hawking = 0
H0 = OPEN / nicht nachgewiesen.
```

H0 ist von Hawking-Emissionsgrenzen getrennt und muss Full-WDM-Akkretion, Formation/Delivery und eine eindeutige Real-Data-Signatur bestehen.

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

Wesentliche Resultate:

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

A20–A31 wurden nach dem ursprünglichen Reduced Stack weitergeführt.

Aktueller konsolidierter Stand:

```text
electron Dirac sink flux-direct: stabilized
nonlinear Thomas-Fermi screening: calculated and recoupled to Dirac solver
collective charge response: much faster than hydrodynamic evolution
independent naive ion/electron n*v*sigma current model: REJECTED
ambipolar/electronic transport hierarchy: strongly constrained
exact Q_eq: OPEN
```

Der verbleibende Charge-Engpass ist jetzt präzise:

```text
multicomponent Onsager / Maxwell-Stefan mobility matrix
+ thermodynamic chemical-potential derivatives
+ sink-boundary coupling.
```

A31 zeigt ausdrücklich:

```text
self diffusion != mutual diffusion != charge mobility
```

und verwirft einen naiven Nernst-Einstein-Ionenstrom als finale WDM-Closure.

Zentrale Datei:

- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `stage3_72_a31_ambipolar_mobility_gate.py`

# Formation / Delivery

## A19 – normaler Halo → fertige Erde

Ein capture-freundlicher direct-Earth Dynamical-Friction-Proxy bei `v_inf=220 km/s` liefert nur

```text
DeltaE/E_inf ~1e-18 ... 5e-17
```

für `1e10...5e11 kg`.

Damit:

```text
normal halo -> direct Earth capture: VERY STRONG FAIL.
```

## Stage 3.73 / F1 – Protosolar / co-moving Seed

```text
protoplanetary gas drag: insufficient
normal halo -> protostellar cloud: strongly negative
already solar-bound, dynamically cold seed: remains OPEN initial condition.
```

F1 rettet keinen normalen Halo-Delivery-Kanal. Offen bleibt nur ein Seed, der **bereits solar gebunden und relativ kalt** ist.

## Stage 3.73 / F2 – Hill-Sphäre / Pull-down Energy Gate

F2 prüfte einen solchen Seed in der Hill-Sphäre eines wachsenden terrestrischen Embryos.

Für einen impulsiven Massensprung `delta=DeltaM/M_p` bei `r=f r_H` gilt lokal

```text
v_inf,max = sqrt(2 G DeltaM/r)
          = sqrt(6 delta/f) v_H.
```

Damit existiert ein kinematischer Pull-down-Bereich. F2-Status:

```text
temporary Hill capture: dynamically allowed
static permanent capture without potential evolution: FAIL
smooth terrestrial pull-down: FAIL as generic channel
giant-impact impulsive jump: PASS as local kinematic existence test
absolute probability: OPEN.
```

## Stage 3.74 / F3 – Adaptive Hill-Monte-Carlo + Jacobi Closure

F3 härtet F2 durch explizite Solartiden im planaren Hill-Modell.

```text
x'' - 2 y' - 3x = -3x/r^3
y'' + 2 x'      = -3y/r^3

C = 3x^2 + 6m/r - v^2
C_L1/L2 = 9 m^(2/3).
```

Nach einem Massensprung `m=1+delta` gilt permanente topologische Einschließung im idealisierten post-impact Hill-System, wenn

```text
C_new > C_L1/L2,new.
```

Ein früher fixed-step RK4-Test wurde wegen künstlichem Jacobi-Drift bei tiefen Encounters verworfen.

Final:

```text
DOP853
rtol=3e-10
atol=1e-12
median Jacobi peak-to-peak drift ~1e-8
maximum ~2.5e-7
adaptive Hill/Jacobi solver: PASS.
```

Konservativer zeitgewichteter Pull-down-Anteil für `r>=0.1 r_H`:

| DeltaM/M | sigma=0.0 | sigma=0.1 | sigma=0.3 | Status |
|---:|---:|---:|---:|---|
| `0.01` | `0` | `0` | `0` | **FAIL in sampled outer gate** |
| `0.03` | `0` | `0` | `0` | **FAIL in sampled outer gate** |
| `0.10` | `0.0352%` | `0.0725%` | `0.0722%` | **PASS existence / inefficient** |
| `0.30` | `6.806%` | `6.302%` | `5.653%` | **PASS conditional channel** |

Ein zweiter unabhängiger `sigma=0.1`-Seed-Lauf reproduzierte die Größenordnung:

```text
DeltaM/M=0.10 -> 0.0624%
DeltaM/M=0.30 -> 6.580%.
```

Mean first Hill residence:

```text
~35 d at 1 AU.
```

Damit war der offene F3-Hebel wiederholte / long-lived residence.

## Stage 3.75 / F3b – Multi-Pass / Residence Timing Gate

F3b koppelt F3 an publizierte Earth-temporary-capture-Zeitskalen.

Literaturanker:

```text
Granvik et al. 2012:
mean Earth TCO duration = 286 +/-18 d
mean revolutions        = 2.88 +/-0.82

2020 CD3 reconstruction:
median capture ~4 yr
some clone orbits nearly 100 yr

Earth horseshoe examples:
co-orbital states up to O(10^3 yr).
```

Wichtig:

```text
co-orbital lifetime != Hill-sphere occupancy.
```

Residence-Amplifikation gegenüber F3s `35.3 d`:

| Zustand | cumulative residence proxy | Faktor |
|---|---:|---:|
| F3 first passage | `35.3 d` | `1x` |
| mittlerer Earth TCO | `286 d` | `~8.1x` |
| 2020-CD3-artig | `4 yr` | `~41.5x` |
| extremer 100-yr Tail | `100 yr` | `~1.0e3x` |
| 3300-yr co-orbital 100%-Hill Stress-U.B. | `3300 yr` | `~3.4e4x` |

Für zufällige relevante Impactzeiten wird als Nullmodell verwendet:

```text
P_overlap = 1 - exp[-N_GI t_res/T_epoch].
```

Bei `T_epoch=10 Myr` und einem mittleren Earth-TCO:

```text
N_GI=1   -> P_overlap ~7.83e-8
N_GI=10  -> P_overlap ~7.83e-7
N_GI=100 -> P_overlap ~7.83e-6.
```

Für einen extremen `100 yr` Capture-Tail:

```text
N_GI=1   -> ~1.0e-5
N_GI=10  -> ~1.0e-4
N_GI=100 -> ~1.0e-3.
```

Das sind bereits capture-freundliche Timingwerte **vor** jedem zusätzlichen Jacobi-/Impact-Gate.

Der `3300 yr` co-orbital Stressfall behandelt unrealistisch die gesamte co-orbitale Zeit als Hill-residence. Selbst diese obere Grenze liefert für `N_GI=10`, `T=10 Myr` nur

```text
P_overlap ~3.29e-3.
```

F3b Schluss:

```text
multi-pass / long-lived residence enhancement:
PASS.

mean enhancement:
~8x gegenüber F3 first passage.

extreme ~100 yr tail:
~1e3x enhancement.

multi-pass as generic cure of Myr random-impact timing:
FAIL.

absolute delivery probability:
OPEN.
```

Damit bleibt Giant-Impact-Pull-down mathematisch möglich, wird aber auf zunehmend spezielle Szenarien beschränkt: sehr hohe cumulative Hill occupancy, Korrelation zwischen Seed- und Impact-Dynamik oder bereits frühe permanente Bindung an einen Embryo.

Zentrale Formation-Dateien:

- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `stage3_73_f2_hill_pulldown_capture.py`
- `STAGE3_74_F3_HILL_MONTE_CARLO.md`
- `stage3_74_f3_hill_monte_carlo.py`
- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `stage3_75_f3b_residence_timing_gate.py`

Nächster Formationstest:

```text
F4 = early permanent embryo-bound seed test

Could a cold solar-bound seed become permanently bound to a small embryo
before the late giant-impact epoch through early three-body exchange,
embryo-embryo encounters or an early dissipative environment?
```

Ein vollständiger globaler direct-N-body Formation-run bleibt ebenfalls sinnvoll, benötigt für eine absolute Wahrscheinlichkeit jedoch weiterhin eine physisch motivierte Seed-Anfangsverteilung.

# Aktuelle Endmatrix

| Bereich | Status |
|---|---|
| H+ strongest SK-IV project comparison | **FAIL** |
| H0 | **OPEN / not detected** |
| smooth-compensated Earth macro branch | kein eigener Reduced-Strukturausschluss |
| Wave-Capture Proton/Fe/Ni | weitgehend berechnet |
| electron sink | stabilisiert im Reduced Stack |
| nonlinear TF screening | berechnet / recoupled |
| exact multicomponent Q_eq | **OPEN** |
| final species-resolved Full-WDM Mdot_BH(t) | **OPEN** |
| normal halo → Earth delivery | **VERY STRONG FAIL** |
| normal halo → protostellar cloud | **strongly negative** |
| gasdrag protoplanetary disk | **FAIL / insufficient** |
| already solar-bound cold seed | **OPEN initial condition** |
| smooth Hill pull-down | **FAIL as generic mechanism** |
| F2 giant-impact local energy gate | **PASS kinematic existence** |
| F3 DeltaM/M<=0.03 outer-Hill gate | **FAIL in sampled gate** |
| F3 DeltaM/M~0.10 | **PASS existence / inefficient** |
| F3 DeltaM/M~0.30 | **PASS conditional few-percent channel** |
| F3b multi-pass residence | **PASS amplification** |
| F3b generic random-impact timing rescue | **FAIL** |
| early permanent embryo-bound seed | **OPEN / F4** |
| full formation/delivery probability | **OPEN** |
| direkte experimentelle BH-Detektion | **NONE** |
| eindeutige positive Signatur | **NONE** |

# Was noch wirklich fehlt

```text
1. exact multicomponent Onsager/Maxwell-Stefan charge closure -> Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F4 early permanent embryo-bound seed / full global formation N-body
6. physical origin / phase-space density of the already solar-bound cold seed.
```

# Zentrale Statusdateien

- `TEST_STATUS.md`
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `STAGE3_74_F3_HILL_MONTE_CARLO.md`
- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `STAGE3_71_A19_FORMATION_RECHECK.md`
- `STAGE3_70B_A18_REALDATA_AUDIT.md`

# Open Science / Projekt-Governance

Originale Texte/Dokumentation/Grafiken stehen – soweit nicht anders gekennzeichnet – unter **CC BY 4.0**; originaler Quellcode unter **MIT**.

Wissenschaftliche Prüfung, Reproduktion, Kritik und eigene abgeleitete Arbeiten sind ausdrücklich erlaubt. Der **offizielle Projektstand** (`main`, Stages, Releases) wird jedoch nur über dieses Repository und die Freigabe des Projektinhabers definiert.

Siehe:

- `LICENSE`
- `ATTRIBUTION.md`
- `OPEN_SCIENCE.md`
- `OFFICIAL_PROJECT_POLICY.md`

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Reduced Stack A1–A19 plus Stage 3.72 A20–A31 und Formation bis Stage 3.75/F3b, Rheinland-Pfalz, Deutschland.
