# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Stage 3.69A-1/A-3/A-4/A-5, Stage 3.69B/A-6, Stage 3.69C/A-7 und Stage 3.69D/A-8 numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen  
**Stand:** 26.08.2026  
**Erstveröffentlichung Erdmodul V1.0:** 23.08.2026

> `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs-/Prioritätsarchiv. Der aktuelle Forschungsstand wird in Markdown + reproduzierbaren Python-Skripten fortgeschrieben.

## Wissenschaftlicher Status

Die SL/BH-Kernhypothese Erdmodul ist ein **theoretischer Forschungsentwurf, kein experimenteller Nachweis**. Untersucht wird, ob ein kleiner zentraler BH-Branch mit Erdbeobachtungen und etablierter GR/Quanten-/Materiephysik konsistent modelliert werden kann.

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben parallel. Gemeinsame Materie-/Capture-Module gelten fuer beide; Hawking-spezifische Emissionen nur fuer H+.

## Branchstatus

### H+

Im getesteten Projekt-Reinterpretationsmodell liegt der relevante Standard-Hawking-Bereich bei etwa `4.82e11 ... 5.49e11 kg`. Der berechnete Greybody-/Neutrinofluss ueberschreitet im entscheidenden SK-IV-Band den verwendeten publizierten 90%-CL-Grenzwert.

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell.
```

Dies ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

### H0

```text
P_Hawking = 0
```

H0 ist dadurch von Hawking-basierten Neutrino-/Gamma-Grenzen getrennt, muss aber Akkretion, Transport, Langzeitstabilitaet, Formation und Real-Data-Tests bestehen.

```text
H0: OPEN / nicht nachgewiesen.
```

## Aktiver Erdbranch

Die starke Zentralmassenvariante ist verworfen. Aktiv ist der kleine `smooth compensated` Branch. Fuer den PREM-Supply-Proxy:

```text
c_eff = 10.4355 km/s
M_BH = 1e11 kg -> r_B ~6.13e-8 m
r_s ~1.49e-16 m
```

Die bisherigen reduzierten Makrotests liefern fuer diesen kleinen Branch keinen robusten Ausschluss durch Gesamtmasse/GM, Traegheitsmoment, reduzierte Hydrostatik, vereinfachte Seismik oder globale Waermeproxies. Das ist Modellkompatibilitaet, keine Evidenz.

# Stage 3.69 – aktueller Capture-/Transportstack

## A-1/A-3 – Schwarzschild-Dirac und Earth-speed Protonen

Der massive Schwarzschild-Dirac-Solver mit regulaerem Horizon-Branch, konserviertem Strom und In/Out-Matching ist implementiert und extern benchmarkiert.

Am Erd-Referenzpunkt `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
sigma_p ~2.174e-22 m^2
sigma_p/sigma_classical ~0.9503
```

Die fruehere Unruh-Low-E-Protonenextrapolation wird bei `alpha_p~0.353` nicht mehr als Endwert verwendet.

## A-4 – Charged Proton Dirac + Ladungsfeedback

Der stabilisierte charged-Proton-Subtest zeigt bei `M=1e11 kg`:

```text
Q=0 e       -> sigma_p/sigma_classical ~0.949
Q=3.67 e    -> ~0.889
Q=10 e      -> ~0.765
Q=24.18 e   -> ~0.517
```

Damit ist Ladungsfeedback relevant, aber in den getesteten positiven Ladungsskalen kein Orders-of-Magnitude-Protonenstopper.

```text
charged proton capture: kontrollierter Subtest PASS
charged electron long-range Coulomb matching: OPEN
```

## A-5 – korrekter Fe/Ni-Spin-0-Composite-Proxy

Dominante `Fe-56`/`Ni-58`-Kerne haben `0+`; deshalb wurde ein massiver Klein-Gordon-Solver statt des Spin-1/2-Dirac-Solvers verwendet.

Low-coupling externe Regression: `~0.2%` Abweichung.

Bei `M_BH=1e11 kg`:

```text
Fe-56: sigma/sigma_classical ~0.99754
Ni-58: sigma/sigma_classical ~0.99646
```

```text
large coherent Fe/Ni wave suppression: NOT FOUND
```

Dense-Fe Screening liegt im freien Elektronenproxy auf atomaren/sub-nm Skalen (`~few 1e-11 ... 1e-10 m`), also weit innerhalb `r_B`; nackte BH-Ladung ist damit kein ungescreenter `r_B`-weiter Supply-Stopper.

## A-6 – Recycling statt Single-pass-Faktor

Ein direkter Single-pass-Proxy liefert nur etwa

```text
Mdot_single ~3.1e-14 kg/s
```

gegenueber dem historischen Michel-Supply-Benchmark bei `1e11 kg`:

```text
Mdot_Michel ~1.47e-8 ... 1.46e-7 kg/s.
```

Die Luecke `~4.7e5 ... 4.7e6` darf nicht automatisch als Quantum-Suppression interpretiert werden.

Bei repeated encounters mit Capture-Wahrscheinlichkeit `p` und permanentem Escape `e` gilt exakt

```text
chi_capture = p/(p+e).
```

Damit ist ein kleiner Einzelpass-Capture nicht automatisch eine kleine Gesamtakkretion; ohne permanenten Escape koennen Misses recycelt werden.

## A-7 – korrigierte Kollisionalitaet + Backpressure-PDE

Eine wichtige A-6-Sensitivitaet wurde korrigiert.

Fuer strong-coupling/geometrische Kollisionen und

```text
rho ~ r^-3/2
```

folgt

```text
lambda_mfp ~ r^3/2
Kn ~ r^1/2,
```

also **abnehmendes Kn nach innen**. Ein innerer collisionless switch entsteht in diesem Branch nicht automatisch.

Der entgegengesetzte Spitzer-Trend `Kn~r^-3/2` gilt nur im weak-coupling-Coulombplasma und darf nicht ohne Kopplungs-/Ionisationsnachweis eingesetzt werden.

Ein kontrollierter 1-D-Bondi-Euler-Test reproduziert den analytischen Transsonik-Massenfluss auf Prozentniveau. Ein reflektierender innerer Rand baut dagegen Backpressure auf und treibt einen outward shock. Damit gilt:

```text
sonic shielding blockiert kleine lineare Rueckmeldungen,
aber nicht dauerhaftes Aufstauen mit Schockbildung.
```

## A-8 – Warm-Dense Fe/Ni + Weak-Reaction-Timescales

Mit dem reduzierten Sensitivitaetsbranch

```text
rho ~ x^-3/2
T ~ x^-1
x=r/r_B
```

bleibt die Ionenkomponente an den relevanten Electron-Capture-Schwellen stark gekoppelt.

Elektronen werden relativistisch degeneriert bei etwa

```text
x ~3.39e-4
r ~1.4e5 r_s.
```

Energetische continuum-EC-Schwellen im freien Fermi-Proxy:

```text
58Ni -> 58Co: Q_kin ~0.381 MeV
x ~1.66e-4
r ~6.84e4 r_s
rho ~6.14e6 g/cm^3
T ~3.62e7 K
Gamma_i(Zeff=26) ~203

56Fe -> 56Mn: Q_kin ~3.696 MeV
x ~5.08e-6
r ~2.09e3 r_s
rho ~1.14e9 g/cm^3
T ~1.18e9 K
Gamma_i(Zeff=26) ~35.6
```

Im selben reduzierten vollionisierten Fe-Scaling waere `Gamma_i=1` erst bei etwa `1.66 r_s`. Das ist keine EOS-Extrapolation bis zum Horizont, sondern eine Konsistenzwarnung gegen einen frueh angesetzten Spitzer-Branch.

Publizierter schneller Fe-56-EC-Vergleich bei `rho*Ye=1e11 g/cm^3`, `T9=3`:

```text
lambda_ec ~1.59e4 s^-1
tau_ec ~6.3e-5 s.
```

Die lokale dynamische Zeit am Fe-Schwellenradius liegt im Reduced-Proxy nur bei `~4.7e-20 s`. Daher:

```text
energetically open EC != prompt weak equilibrium.
prompt one-pass neutronization/NSE: NOT SUPPORTED.
```

Lange Residence-/Recyclingzeiten koennen weak reactions wieder relevant machen und muessen mit Transport gemeinsam gerechnet werden.

# Was jetzt tatsaechlich entschieden ist

```text
Schwarzschild-Dirac Solver: PASS als numerischer/literaturbasierter Solver-Test
Earth-speed neutral proton capture: CALCULATED
charged proton feedback: CALCULATED fuer kontrollierte Q-Skalen
charged electron Coulomb matcher: OPEN
coherent Fe/Ni scalar capture: CALCULATED, nahezu klassisch
large wave suppression at 1e11 kg: NOT FOUND
long-range unscreened Coulomb supply blocking: NOT SUPPORTED by dense-screening proxy
single-pass factor as automatic net-Mdot suppression: REJECTED
strong-coupling inward collisionality branch: SELF-CONSISTENT reduced proxy
prompt one-pass weak equilibrium/neutronization: NOT SUPPORTED
final residence/backpressure + reaction-network net Mdot: OPEN
```

## Naechster entscheidender Block

```text
Stage 3.69E / A-9:
residence-time + backpressure transport
+ charge neutrality
+ minimal Fe/Ni weak network
-> chi_transport
-> species-resolved net Mdot_BH.
```

Das ist jetzt der zentrale offene Erd-Akkretionsblock.

## Formation

Die bisher getesteten Standardwege bleiben stark negativ:

```text
in-situ Kollaps normaler Erdmaterie: FAIL
spaeter direkter Earth-Capture: FAIL
Proto-Earth-/Planetesimal-Standardcapture: FAIL
normaler Halo -> protoplanetare cold disk: FAIL unter getesteten Bedingungen
cold/co-moving Anfangsbedingung: mathematisch moeglich, Herkunft nicht hergeleitet
```

## Aktuelle Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleiner smooth Erdbranch | kein eigener Erdstruktur-Ausschluss | kein eigener Erdstruktur-Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL im getesteten Projektmodell** | nicht anwendbar |
| Proton/Fe/Ni Wave-Capture | weitgehend berechnet | weitgehend berechnet |
| Charge-/Screening-Subtests | teilweise berechnet | teilweise berechnet |
| Residence/Backpressure + Weak Network | **OPEN** | **OPEN** |
| finale Dense-Matter-Netto-Mdot | **OPEN** | **OPEN** |
| Formation/Delivery | stark negativ | stark negativ |
| direkte experimentelle Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

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
- `TEST_STATUS.md`
- `NUMERIK_STATUS.md`
- `AKKRETION_STATUS.md`
- `VALIDATION_PROTOCOL_STAGE3_69_70.md`
- `CHANGELOG.md`

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; numerischer Forschungsstand bis Stage 3.69D/A-8, Stage 3.69 Full-Multiphysics und Stage 3.70 offen, Rheinland-Pfalz, Deutschland.
