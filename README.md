# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Stage 3.69A-1/A-3/A-4/A-5, Stage 3.69B/A-6, Stage 3.69C/A-7, Stage 3.69D/A-8 und Stage 3.69E/A-9 numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen  
**Stand:** 26.08.2026  
**Erstveröffentlichung Erdmodul V1.0:** 23.08.2026

> `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs-/Prioritätsarchiv. Der aktuelle Forschungsstand wird in Markdown + reproduzierbaren Python-Skripten fortgeschrieben.

## Wissenschaftlicher Status

Die SL/BH-Kernhypothese Erdmodul ist ein **theoretischer Forschungsentwurf, kein experimenteller Nachweis**. Untersucht wird, ob ein kleiner zentraler BH-Branch mit Erdbeobachtungen und etablierter GR/Quanten-/Materiephysik konsistent modelliert werden kann.

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben parallel. Gemeinsame Materie-/Capture-/Transportmodule gelten fuer beide; Hawking-spezifische Emissionen nur fuer H+.

## Branchstatus

### H+

Der relevante Standard-Hawking-Bereich liegt im getesteten Projektmodell bei etwa

```text
M_BH ~4.82e11 ... 5.49e11 kg.
```

Der Projekt-Greybody-/Neutrinofluss ueberschreitet im entscheidenden verwendeten SK-IV-Band den publizierten 90%-CL-Grenzwert.

```text
H+ Standard-Hawking: FAIL im getesteten Projekt-Reinterpretationsmodell.
```

Dies ist keine offizielle Super-K-Erdzentrum-BH-Exklusion. H+ bleibt als separater Branch dokumentiert.

### H0

```text
P_Hawking = 0
```

H0 ist von Hawking-basierten Neutrino-/Gamma-Grenzen getrennt, muss aber Akkretion, Transport, Langzeitstabilitaet, Formation und Real-Data-Tests bestehen.

```text
H0: OPEN / nicht nachgewiesen.
```

## Aktiver Erdbranch

Die starke Zentralmassenvariante ist verworfen. Aktiv ist der kleine `smooth compensated` Branch.

Zentraler PREM-/Supply-Proxy:

```text
rho_c = 13.0885 g/cm^3
c_eff = 10.4355 km/s
```

Bei `M_BH=1e11 kg`:

```text
r_B ~6.13e-8 m
r_s ~1.49e-16 m.
```

Die bisherigen reduzierten Makrotests liefern fuer diesen kleinen Branch keinen robusten Ausschluss durch Gesamtmasse/GM, Traegheitsmoment, reduzierte Hydrostatik, vereinfachte Seismik oder globale Waermeproxies. Das bedeutet Modellkompatibilitaet innerhalb der getesteten Proxies, nicht Evidenz fuer einen BH.

# Stage 3.69 – aktueller Capture-/Transportstack

## A-1/A-3 – Schwarzschild-Dirac und Earth-speed Protonen

Der massive Schwarzschild-Dirac-Solver mit regulaerem Horizon-Branch, konserviertem Strom und In/Out-Matching ist implementiert und benchmarkiert.

Bei `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
sigma_p ~2.174e-22 m^2
sigma_p/sigma_classical ~0.9503.
```

Die fruehere Unruh-Low-E-Protonenextrapolation wird bei `alpha_p~0.353` nicht mehr als finaler Earth-speed-Wert verwendet.

## A-4 – Charged Proton Dirac + Ladungsfeedback

Bei `M=1e11 kg`:

```text
Q=0 e       -> sigma_p/sigma_classical ~0.949
Q=3.67 e    -> ~0.889
Q=10 e      -> ~0.765
Q=24.18 e   -> ~0.517.
```

```text
charged proton capture: kontrollierter Subtest PASS
charged electron long-range Coulomb matching: OPEN.
```

Ladungsfeedback ist relevant, aber die getesteten positiven Ladungsskalen erzeugen keinen Orders-of-Magnitude-Protonenstopp.

## A-5 – Fe/Ni Spin-0 Composite-Capture

Dominante `Fe-56`/`Ni-58`-Kerne haben `0+`; deshalb wird fuer den kohärenten Composite-Proxy ein massiver Klein-Gordon-Solver verwendet.

Bei `M_BH=1e11 kg`:

```text
Fe-56: sigma/sigma_classical ~0.99754
Ni-58: sigma/sigma_classical ~0.99646.
```

```text
large coherent Fe/Ni wave suppression: NOT FOUND.
```

Dense-Fe Screening liegt im Reduced Proxy auf atomaren/sub-nm Skalen (`~few 1e-11 ... 1e-10 m`), also weit innerhalb `r_B`.

## A-6 – Recycling statt Single-pass-Faktor

Naiver Hintergrund-Single-pass-Proxy bei `1e11 kg`:

```text
Mdot_single ~3.1e-14 kg/s.
```

Historischer Michel-/Supply-Benchmark:

```text
Mdot_supply ~1.47e-8 ... 1.46e-7 kg/s.
```

Der Unterschied darf nicht automatisch als Quantum-Suppression interpretiert werden.

Bei repeated encounters mit Capture-Wahrscheinlichkeit `p` und permanentem Escape `e` gilt exakt

```text
chi_capture = p/(p+e).
```

## A-7 – korrigierte Kollisionalitaet + Backpressure-PDE

Fuer den strong-coupling/geometrischen Sensitivitaetsbranch und

```text
rho ~ r^-3/2
```

gilt

```text
lambda_mfp ~ r^3/2
Kn ~ r^1/2,
```

also abnehmendes `Kn` nach innen.

Der entgegengesetzte Spitzer-Trend gilt nur im weak-coupling-Coulombplasma und darf nicht ohne expliziten Kopplungs-/Ionisationsuebergang eingesetzt werden.

Ein 1-D-Bondi-Euler-Benchmark reproduziert den analytischen transsonischen Massenfluss auf Prozentniveau. Ein reflektierender Innenrand kann dagegen Backpressure und einen outward shock erzeugen.

## A-8 – Warm-Dense Fe/Ni + Weak-Reaction-Timescales

Im Reduced Scaling

```text
rho ~ x^-3/2
T ~ x^-1
x=r/r_B
```

bleibt die Ionenkomponente an den relevanten EC-Schwellen stark gekoppelt.

Energetische Free-Fermi-Schwellen:

```text
58Ni -> 58Co:
    x ~1.66e-4
    r ~6.84e4 r_s

56Fe -> 56Mn:
    x ~5.08e-6
    r ~2.09e3 r_s.
```

Publizierter schneller `56Fe`-EC-Vergleich bei `rho*Ye=1e11 g/cm^3`, `T9=3`:

```text
lambda_ec ~1.5916e4 s^-1
tau_ec ~6.28e-5 s.
```

Damit gilt bereits in A-8:

```text
energetically open EC != prompt weak equilibrium.
```

## A-9 – Residence + Backpressure + Weak-Network Closure

A-9 verbindet erstmals die repeated-encounter-Zeit mit Reservoir-Kapazitaet, permanentem Escape, Plasmaantwort und Weak-Reaction-Gates.

### Strong-coupling Escape

Fuer

```text
lambda_mfp = lambda_0 x^3/2
```

ist der Reduced collisional optical depth von `r_t` bis `r_B`

```text
tau_coll = 2 r_B/lambda_0 [x_t^-1/2 - 1].
```

Bei den getesteten atomaren Skalen ist `tau_coll` riesig (`~1e3 ... >1e5` je nach Masse/Skala). Damit ist permanenter **ballistischer** Escape im strong-coupling Proxy praktisch null; Misses werden rezykliert.

### `M=1e11 kg` Processing-Capacity

| `r_t` | `p` | `t_res` | `Mdot_capacity` | `Xi_high=Mdot_high/Mdot_capacity` |
|---:|---:|---:|---:|---:|
| `3e-11 m` | `3.30e-5` | `1.36e-12 s` | `1.85e-5 kg/s` | `0.0079` |
| `1e-10 m` | `9.90e-6` | `2.76e-11 s` | `9.13e-7 kg/s` | `0.160` |
| `2e-10 m` | `4.95e-6` | `1.56e-10 s` | `1.61e-7 kg/s` | `0.905` |

Damit kann das vorhandene Reduced Reservoir bei `1e11 kg` den gesamten historischen Supply-Benchmark fuer alle getesteten atomaren Transition-Skalen verarbeiten, ohne zusaetzlichen Capture-Pile-up zu benoetigen.

```text
M>=~1e11 kg strong-coupling/recycling reduced branch:
    SUPPLY-PROCESSING CAPABLE
    chi_transport ~1 within this reduced closure.
```

Dies ist keine Full-WDM-Endvorhersage.

### Massenscan

```text
M=1e10 kg:
    transition-scale/backpressure sensitive; OPEN

M=1e11 kg:
    tested strong-coupling transition bracket processing-capable

M=2e11 kg:
    clear processing-capacity reserve

M=5e11 kg:
    very large processing-capacity reserve.
```

Kritischer Reduced-Transport-Uebergang fuer `Xi=1`:

```text
x_crit low supply  ~8.507e-3
x_crit high supply ~3.397e-3.
```

Fuer physikalische Transition-Skalen `3e-11 ... 2e-10 m` entspricht das einem kritischen BH-Massenbereich von grob

```text
~5.8e9 ... 9.6e10 kg.
```

Damit ist `1e10 kg` der sensitive Unterrand, waehrend `~1e11 kg` und darueber im aktuellen Reduced Strong-Coupling-Branch keine riesige Loss-Cone-Unterdrueckung benoetigen.

### Quasineutralitaet

Der Elektronen-Plasmaresponse ist an den getesteten Skalen wesentlich schneller als die Residence-Zeit. Beispiel `M=1e11 kg, r_t=1e-10 m`:

```text
t_plasma/t_res ~2.7e-9.
```

Das motiviert bulk-quasineutrales Transportverhalten, ohne den offenen diskreten BH-Charge-State exakt zu loesen.

### Weak-Reaction Gate

Bei `M=1e11 kg`:

```text
Ni-threshold:
    t_res ~9.13e-14 s
    lambda_required ~1.10e13 s^-1

Fe-threshold:
    t_res ~1.50e-17 s
    lambda_required ~6.69e16 s^-1.
```

Der publizierte `56Fe`-Vergleichswert `1.5916e4 s^-1` ist damit viele Groessenordnungen zu langsam fuer promptes Weak-Equilibrium innerhalb dieser Reduced Residence-Zeiten.

```text
prompt one-pass neutronization: NOT SUPPORTED in the supply-processing strong-coupling branch.
```

Ein lang lebender makroskopischer Backpressure-Stau koennte die Residence-Zeit verlaengern; deshalb bleibt der `1e10 kg`-Branch offen.

# Aktueller physikalischer Status

```text
Schwarzschild-Dirac Solver: PASS als numerischer/literaturbasierter Solver-Test
Earth-speed neutral proton capture: CALCULATED
charged proton feedback: CALCULATED fuer kontrollierte Q-Skalen
charged electron Coulomb matcher: OPEN
coherent Fe/Ni scalar capture: CALCULATED, nahezu klassisch
large wave suppression at 1e11 kg: NOT FOUND
long-range unscreened Coulomb supply blocking: NOT SUPPORTED by dense-screening proxy
single-pass factor as automatic net-Mdot suppression: REJECTED
strong-coupling inward collisionality branch: internally consistent Reduced Proxy
A9 repeated-residence/processing closure: CALCULATED
M>=~1e11 kg Reduced Strong-Coupling branch: supply-processing capable
M=1e10 kg: backpressure-sensitive / OPEN
prompt weak equilibrium/neutronization: NOT SUPPORTED in fast-transit branch
final first-principles WDM species-resolved Mdot: OPEN.
```

## Konsequenz fuer die aktuelle Mdot

Fuer den `M=1e11 kg` Strong-Coupling/Recycling Reduced Branch folgt derzeit

```text
Mdot_BH,reduced ~ Mdot_supply
                ~1.47e-8 ... 1.46e-7 kg/s.
```

Das ist eine reduzierte Modellvorhersage, keine Messung und noch kein Full-Multiphysics-Ergebnis.

Die bisherigen Erdalter-/globalen Waerme-Stressproxies hatten diese Supply-Skala bereits nicht ausgeschlossen; daher falsifiziert A-9 H0 nicht automatisch.

## Formation

Die getesteten Standardwege bleiben stark negativ:

```text
in-situ Kollaps normaler Erdmaterie: FAIL
spaeter direkter Earth-Capture: FAIL
Proto-Earth-/Planetesimal-Standardcapture: FAIL
normaler Halo -> protoplanetare cold disk: FAIL unter getesteten Bedingungen
cold/co-moving Anfangsbedingung: mathematisch moeglich, Herkunft nicht hergeleitet.
```

## Aktuelle Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleiner smooth Erdbranch | kein eigener Erdstruktur-Ausschluss | kein eigener Erdstruktur-Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL im getesteten Projektmodell** | nicht anwendbar |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Charge-/Screening-Subtests | teilweise berechnet | teilweise berechnet |
| A9 Residence/Recycling Closure | **CALCULATED als Reduced Common-Matter-Block** | **CALCULATED als Reduced Common-Matter-Block** |
| `>=~1e11 kg` Strong-Coupling Transport | supply-processing capable im Reduced Branch | supply-processing capable im Reduced Branch |
| `1e10 kg` Transport | OPEN / backpressure-sensitive | OPEN / backpressure-sensitive |
| finale First-Principles Dense-Matter-Netto-Mdot | **OPEN** | **OPEN** |
| Formation/Delivery | stark negativ | stark negativ |
| direkte experimentelle Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## Naechster Pflichtblock

```text
Stage 3.69F / A-10:
first-principles-informed WDM transport closure
+ time-dependent hydro/kinetic sink coupling
+ A4/A5 absorptive inner boundary
-> replace geometric lambda_mfp proxy
-> e_perm(r,E,species)
-> final reduced species-resolved Mdot band.
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
- `TEST_STATUS.md`
- `NUMERIK_STATUS.md`
- `AKKRETION_STATUS.md`
- `VALIDATION_PROTOCOL_STAGE3_69_70.md`
- `CHANGELOG.md`

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; numerischer Forschungsstand bis Stage 3.69E/A-9, Stage 3.69 Full-Multiphysics und Stage 3.70 offen, Rheinland-Pfalz, Deutschland.
