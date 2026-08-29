# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Reduced Stack A1–A19 abgeschlossen; A20–A31 / Stage 3.72 weitergeführt; Formation bis Stage 3.77 / F5  
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

```text
electron Dirac sink flux-direct: stabilized
nonlinear Thomas-Fermi screening: calculated and recoupled
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

# Formation / Delivery

## A19 – normaler Halo → fertige Erde

```text
DeltaE/E_inf ~1e-18 ... 5e-17
normal halo -> direct Earth capture: VERY STRONG FAIL.
```

## Stage 3.73 / F1 – Protosolar / co-moving Seed

```text
protoplanetary gas drag: insufficient
normal halo -> protostellar cloud: strongly negative
already solar-bound, dynamically cold seed: OPEN initial condition.
```

## Stage 3.73 / F2 – Hill / Pull-down Energy Gate

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

Konservativer zeitgewichteter Pull-down-Anteil bei `r>=0.1 r_H`:

| DeltaM/M | sigma=0.0 | sigma=0.1 | sigma=0.3 | Status |
|---:|---:|---:|---:|---|
| `0.01` | `0` | `0` | `0` | **FAIL in sampled gate** |
| `0.03` | `0` | `0` | `0` | **FAIL in sampled gate** |
| `0.10` | `0.0352%` | `0.0725%` | `0.0722%` | **PASS existence / inefficient** |
| `0.30` | `6.806%` | `6.302%` | `5.653%` | **PASS conditional channel** |

## Stage 3.75 / F3b – Multi-Pass / Residence Timing

```text
F3 first passage ~35.3 d
mean Earth TCO ~286 d
2020 CD3 median ~4 yr
extreme clone tail ~100 yr.
```

```text
multi-pass residence enhancement: PASS
multi-pass as generic random-impact timing rescue: FAIL
absolute delivery: OPEN.
```

## Stage 3.76 / F4 – Early permanent embryo-bound Seed

Collisionless terrestrischer Exchange-Capture ist physikalisch möglich. F4s analytischer Gate ergibt für einen Seed bei `f=0.3 r_H`:

```text
prograde stable-capture kick  ~0.748 v_H
retrograde stable-capture kick ~0.376 v_H.
```

Ein enger Embryo–Embryo-Stressproxy kann diese Größenordnung erreichen.

Im adiabatischen Wachstumsgrenzfall:

```text
a_seed ∝ 1/M_p
R_p    ∝ M_p^(1/3)
=> a_seed/R_p ∝ M_p^(-4/3).
```

Damit kann ein früh gebundener Seed durch Wachstum später body-crossing werden.

F4:

```text
collisionless early permanent binding: PASS kinematic existence
stable embryo-bound phase space: PASS
growth-assisted engulfment: PASS conditional
post-engulfment damping: feasibility only
absolute probability: OPEN.
```

## Stage 3.77 / F5 – Direct restricted 4-body Exchange Monte-Carlo

F5 integriert direkt

```text
Sun + Proto-Earth M1 + second embryo M2 + massless seed.
```

Jeder Lauf besitzt einen gepaarten Nullkontrolllauf mit identischem M1+Seed-Zustand aber `M2=0`.

### Kritische Korrektur

Ein Pilot mit `V~Omega R_H,mut` **am Perizentrum** wurde verworfen, weil er bei kleinen `b` unterhalb der gegenseitigen Escape-Speed liegen und künstlich embryo-bound Encounters erzeugen kann.

Final:

```text
V_p^2 = V_inf^2 + 2 G (M1+M2)/b
```

mit echten hyperbolischen Flybys.

### Ensembles

```text
M1 = 1e-3 ... 1e-1 M_E
seed r = 0.1 ... 1.0 r_H,1
seed beta=v/v_esc(local) = 1.00 ... 1.15
```

STRONG:

```text
q=0.3...1
kappa=b/R_H,mut=0.3...0.8
u_inf=V_inf/(Omega R_H,mut)=0.5...1.5
N=300.
```

BROAD:

```text
q=0.03...1
kappa=0.3...1.5
u_inf=0.5...3
N=300.
```

WEAK:

```text
q=0.03...0.1
kappa=0.9...1.5
u_inf=1.5...3
N=300.
```

### Persistenz bis 20 Omega^-1

`20 Omega^-1 ~3.18 yr` bei 1 AU.

| Ensemble | persistent stable | Status |
|---|---:|---|
| STRONG | `5/300 = 1.67%` | **PASS conditional** |
| BROAD | `3/300 = 1.00%` | **PASS conditional** |
| WEAK | `0/300` | **not found persistent** |

95%-Wilson-Brackets:

```text
STRONG ~0.71...3.84%
BROAD  ~0.34...2.90%
WEAK   0...~1.26% upper.
```

Alle zunächst nur `bound_unstable` exchange-attributable Zustände entkoppeln bis `20 Omega^-1` wieder.

Persistente Captures besitzen beispielsweise

```text
a_seed/r_H ~0.21 ... 0.58
```

während M2 nach dem Lauf bereits typischerweise `~55...150` mutual Hill radii entfernt ist.

Damit ist der lokale Exchange-Mechanismus nicht nur ein momentaner Perizentrum-Artefakt.

### Exchange-induced Body Crossings

FULL-only body crossings:

```text
STRONG 4/300
BROAD  3/300
WEAK   0/300.
```

Bereits negative planetozentrische Energie beim Body-Eintritt:

```text
STRONG 2/4
BROAD  3/3.
```

Die zwei positiven STRONG-crossings besitzen `v_inf~129...140 m/s`; selbst der absichtlich optimistische A19-Dragproxy mit `I=30` erreicht für `M_BH<=5e11 kg` nur etwa

```text
DeltaE_drag/E_inf <=~3e-7.
```

Damit:

```text
positive-E one-pass crossing + ordinary drag: FAIL
already exchange-bound body crossing: PASS existence.
```

### F5 Schluss

```text
direct Newtonian restricted 4-body solver: PASS
hyperbolic encounter correction: PASS
paired M2=0 counterfactual: PASS
persistent collisionless embryo-exchange capture: FOUND
conditional strong/broad capture fraction: O(1%) in defined ensemble
weak encounter persistent capture: not found in N=300
absolute Earth-delivery probability: OPEN.
```

F5 ist **keine Evidenz für einen Erdzentrum-BH**. Es zeigt nur, dass F4s lokaler Formation-Spezialkanal eine direkte Newtonsche Mehrkörperrechnung überlebt.

Der verbleibende Formation-Engpass ist nun:

```text
solar-bound seed phase-space density
x probability of Hill occupancy at embryo encounter
x realistic terrestrial embryo encounter history
x later survival/engulfment.
```

Zentrale F5-Dateien:

- `STAGE3_77_F5_RESTRICTED_4BODY_EXCHANGE_MC.md`
- `stage3_77_f5_restricted_4body_exchange_mc.py`

Nächster Formationstest:

```text
F6 = population-weighted formation gate
-> seed heliocentric a,e,i distribution
-> embryo encounter-rate distribution
-> Hill-occupancy duty cycle
-> F5 conditional capture kernel
-> later survival / engulfment
-> absolute P_delivery or required seed abundance.
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
| F4 growth-assisted engulfment | **PASS conditional / history OPEN** |
| F5 direct restricted 4-body exchange | **PASS conditional** |
| F5 strong persistent stable fraction | **1.67% in defined encounter-conditioned ensemble** |
| F5 broad persistent stable fraction | **1.00% in defined encounter-conditioned ensemble** |
| F5 weak persistent stable fraction | **0/300 found** |
| full formation/delivery probability | **OPEN** |
| direkte experimentelle BH-Detektion | **NONE** |
| eindeutige positive Signatur | **NONE** |

# Was noch wirklich fehlt

```text
1. exact multicomponent Onsager/Maxwell-Stefan charge closure -> Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F6 population-weighted formation/delivery probability
6. realistic post-capture growth/engulfment survival
7. physical origin / abundance / phase-space density of solar-bound cold seeds.
```

# Zentrale Statusdateien

- `TEST_STATUS.md`
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `STAGE3_74_F3_HILL_MONTE_CARLO.md`
- `STAGE3_75_F3B_RESIDENCE_TIMING_GATE.md`
- `STAGE3_76_F4_EARLY_EMBRYO_BOUND_SEED.md`
- `STAGE3_77_F5_RESTRICTED_4BODY_EXCHANGE_MC.md`
- `STAGE3_71_A19_FORMATION_RECHECK.md`
- `STAGE3_70B_A18_REALDATA_AUDIT.md`

# Open Science / Projekt-Governance

Originale Texte/Dokumentation/Grafiken stehen – soweit nicht anders gekennzeichnet – unter **CC BY 4.0**; originaler Quellcode unter **MIT**.

Wissenschaftliche Prüfung, Reproduktion, Kritik und eigene abgeleitete Arbeiten sind ausdrücklich erlaubt. Der **offizielle Projektstand** (`main`, Stages, Releases) wird nur über dieses Repository und die Freigabe des Projektinhabers definiert.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Reduced Stack A1–A19 plus Stage 3.72 A20–A31 und Formation bis Stage 3.77/F5, Rheinland-Pfalz, Deutschland.
