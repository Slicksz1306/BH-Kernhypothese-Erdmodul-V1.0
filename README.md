# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Reduced Stack A1–A19 abgeschlossen im definierten Umfang; A20–A31 / Stage 3.72 weitergeführt; Formation Stage 3.73 bis F2  
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

Geprüft wurden frühere Capture-Stufen.

```text
protoplanetary gas drag: insufficient
normal halo -> protostellar cloud: strongly negative
already solar-bound, dynamically cold seed: remains OPEN initial condition.
```

F1 rettet keinen normalen Halo-Delivery-Kanal. Offen bleibt nur ein Seed, der **bereits solar gebunden und relativ kalt** ist.

## Stage 3.73 / F2 – Hill-Sphäre / Pull-down Capture

F2 prüft einen solchen bereits solar gebundenen Seed in der Hill-Sphäre eines wachsenden terrestrischen Embryos.

Hill-Skalen bei 1 AU:

| Embryomasse | r_H | v_H |
|---:|---:|---:|
| `0.01 M_E` | `3.224e8 m` | `64.19 m/s` |
| `0.10 M_E` | `6.946e8 m` | `138.30 m/s` |
| `0.50 M_E` | `1.188e9 m` | `236.49 m/s` |
| `1.00 M_E` | `1.497e9 m` | `297.96 m/s` |

Für einen impulsiven Massensprung `delta=DeltaM/M_p` bei `r=f r_H` gilt der reduzierte Energie-Gate

```text
v_inf,max = sqrt(2 G DeltaM/r)
          = sqrt(6 delta/f) v_H.
```

Am Hill-Rand (`f=1`) ergibt sich:

| M_p | delta=0.01 | delta=0.10 | delta=0.30 |
|---:|---:|---:|---:|
| `0.01 M_E` | `15.72 m/s` | `49.72 m/s` | `86.13 m/s` |
| `0.10 M_E` | `33.88 m/s` | `107.13 m/s` | `185.55 m/s` |
| `0.50 M_E` | `57.93 m/s` | `183.19 m/s` | `317.29 m/s` |
| `1.00 M_E` | `72.99 m/s` | `230.80 m/s` | `399.76 m/s` |

Die Seed-/BH-Masse kürzt sich aus der spezifischen Energiebedingung heraus; der Gate gilt daher für den Projektbereich `1e10...5e11 kg` im Testmassenlimit.

F2 Status:

```text
temporary Hill capture: PASS / dynamically allowed
static permanent capture without dissipation or potential evolution: FAIL
smooth terrestrial pull-down: FAIL as generic channel
very long-lived separatrix temporary capture: OPEN tail
giant-impact impulsive mass jump: PASS as kinematic existence test
real permanent-capture probability: OPEN.
```

Damit ist Formation/Delivery **nicht gelöst**, aber F2 zeigt einen bisher nicht ausgeschlossenen Spezialkanal:

```text
already solar-bound cold seed
+ temporary Hill residence
+ sufficiently rapid embryo mass jump
=> permanent capture kinematically possible.
```

Der verbleibende Engpass ist nun primär eine **Phasenraum-/Timing-Wahrscheinlichkeit**, nicht mehr nur die Bindungsenergie.

Zentrale F2-Dateien:

- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
- `stage3_73_f2_hill_pulldown_capture.py`

Nächster Formationstest:

```text
F3 = restricted/N-body Monte-Carlo
-> solar-bound seed a,e,i distribution
-> repeated Hill encounters
-> temporary-capture residence times
-> stochastic embryo growth / giant-impact epochs
-> permanent-capture fraction.
```

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
| giant-impact pull-down energy gate | **PASS kinematic existence** |
| full F2 delivery probability | **OPEN** |
| direkte experimentelle BH-Detektion | **NONE** |
| eindeutige positive Signatur | **NONE** |

# Was noch wirklich fehlt

```text
1. exact multicomponent Onsager/Maxwell-Stefan charge closure -> Q_eq
2. final Fe/Ni/light-element Full-WDM species-resolved Mdot_BH(t)
3. unique macroscopic H0 observable amplitude/profile
4. real-data likelihood on that prediction
5. F3 N-body/Monte-Carlo formation-delivery probability
6. physical origin / phase-space density of the already solar-bound cold seed.
```

# Zentrale Statusdateien

- `TEST_STATUS.md`
- `STAGE3_72_A31_AMBIPOLAR_MOBILITY_GATE.md`
- `STAGE3_73_F2_HILL_PULLDOWN_CAPTURE.md`
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

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Reduced Stack A1–A19 plus Stage 3.72 A20–A31 und Formation Stage 3.73/F2, Rheinland-Pfalz, Deutschland.
