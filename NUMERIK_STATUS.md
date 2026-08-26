# Numerischer und physikalischer Status – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Aktuelle Stufe:** numerischer Forschungsstand bis Stage 3.69E/A-9; Stage 3.69 Full-Multiphysics und Stage 3.70 offen

## Aussagegrenze

`PASS` bedeutet in dieser Datei nur, dass ein definierter Solver-/Regression-/Konvergenztest innerhalb seiner Annahmen bestanden wurde. Kein numerischer PASS ist eine experimentelle Bestaetigung eines Erdzentrum-BH.

```text
H+ = mit Standard-Hawking
H0 = ohne Hawking
```

Beide Branches bleiben parallel.

## Wichtige korrigierte Zwischenannahmen

```text
Hard-Cavity-Erdbranch -> verworfen
Bondi/Michel = automatisch finale Horizonrate -> verworfen
permanenter One-pass-Loss-Cone-Faktor -> verworfen
Fe-56 als Spin-1/2-Dirac-Teilchen -> korrigiert; 0+ -> scalar/composite
Unruh-Low-E-Protonenwert bei alpha_p~0.353 als Endwert -> ersetzt durch vollen Dirac-Matcher
A6 r_coll~lambda_geom als physischer collisionless transition -> korrigiert in A7
sonic point blockiert jede langfristige Rueckmeldung -> korrigiert; Backpressure/Shock kann nach aussen laufen
EC energetisch offen = sofortige Neutronisierung -> verworfen
small one-pass p = stationary chi_transport -> korrigiert durch repeated-encounter A9
```

## H+

```text
M_BH ~4.82e11 ... 5.49e11 kg im getesteten Standard-Hawking-Projektbranch
H+ Standard-Hawking: FAIL im getesteten SK-IV-Projekt-Reinterpretationsmodell
```

Keine offizielle Super-K-Erdzentrum-BH-Exklusion wird behauptet.

# Gemeinsame Materie-/Capture-/Transport-Numerik

## A-1 – Schwarzschild-Dirac

- massive Dirac-Radialgleichung: IMPLEMENTED
- regulaerer Horizon-Branch: IMPLEMENTED
- Wronskian/Stromerhaltung: PASS als Solver-Selfcheck
- In/Out-Matching: IMPLEMENTED
- Matchingradius-Konvergenz: PASS an getesteten Literaturpunkten
- Low-alpha externe Regression: PASS

## A-3 – Earth-speed neutrale Protonen

Bei `v=10.4355 km/s`:

```text
M=1e10 kg: sigma_p/sigma_classical ~0.03267
M=1e11 kg: ~0.95030
M=2e11 kg: ~1.00807
M=5e11 kg: ~0.99662
```

Referenz `1e11 kg`:

```text
sigma_p ~2.174e-22 m^2.
```

## A-4 – charged Proton Dirac

Bei `1e11 kg`:

```text
Q=0 e      -> sigma_p/sigma_classical ~0.949
Q=3.67 e   -> ~0.889
Q=10 e     -> ~0.765
Q=24.18 e  -> ~0.517
```

```text
charged proton channel: PARTIAL PASS / benchmarked
charged electron long-range Coulomb matcher: OPEN
```

## A-5 – Fe/Ni 0+ Klein-Gordon

Low-alpha skalare externe Regression: `~0.2%`.

```text
Fe-56 @1e11 kg: sigma/sigma_classical ~0.99754
Ni-58 @1e11 kg: sigma/sigma_classical ~0.99646
```

```text
large coherent Fe/Ni wave suppression: NOT FOUND
```

Dense-electron Screeningproxy:

```text
lambda_screen ~few 1e-11 ... 1e-10 m
r_B ~6.13e-8 m.
```

## A-6 – repeated encounters / Recycling

```text
Mdot_single ~3.1e-14 kg/s
historischer Michel-Supply @1e11 kg ~1.47e-8 ... 1.46e-7 kg/s
```

Repeated-encounter closure:

```text
chi = p/(p+e).
```

Ein kleiner `p_single` ist kein automatischer stationaerer `Mdot`-Suppressionsfaktor.

## A-7 – Kollisionalitaet + PDE-Backpressure

Strong-coupling/geometrischer Branch:

```text
rho~r^-3/2
lambda~r^3/2
Kn~r^1/2
```

=> `Kn` sinkt nach innen.

Weak-Coulomb/Spitzer:

```text
lambda_C~T^2/n
Kn_C~r^-3/2
```

=> entgegengesetzter Trend, aber nur bei `Gamma<<1` gerechtfertigt.

1-D Bondi-Euler-Benchmark (`Gamma=1.5`) reproduziert den analytischen Massenfluss auf Prozentniveau. Reflektierender Innenrand erzeugt Druckaufbau und outward shock.

## A-8 – WDM/Strong-Coupling + Weak Timescales

Reduzierter inward-Sensitivitaetsbranch:

```text
rho~x^-3/2
T~x^-1
Gamma_i~x^1/2
Kn_geom~x^1/2.
```

EC-Energieschwellen:

```text
58Ni -> 58Co: x~1.66e-4 ~6.84e4 r_s
56Fe -> 56Mn: x~5.08e-6 ~2.09e3 r_s.
```

Der weak-Spitzer-Branch ist an diesen Schwellen im reduzierten hochionisierten Fe-Proxy nicht selbstkonsistent (`Gamma_i>>1`).

Publizierter `56Fe`-EC-Vergleich:

```text
rho*Ye=1e11 g/cm^3, T9=3
lambda_ec~1.5916e4 s^-1
tau_ec~6.28e-5 s.
```

```text
prompt one-pass weak equilibrium/neutronization: NOT SUPPORTED
```

## A-9 – Residence / Backpressure / Minimal Weak Network

### A9.1 Repeated-encounter residence

Pro Encounter:

```text
p = capture
e_perm = permanent escape
1-p-e = recycle
```

Exakt:

```text
chi_capture = p/(p+e_perm).
```

Bei vernachlaessigbarem permanenten Escape:

```text
t_res = t_cycle/p.
```

### A9.2 Strong-coupling permanent escape

Mit dem A7 strong-coupling/geometrischen Sensitivitaetsproxy

```text
lambda=lambda_0 x^3/2
```

folgt

```text
tau_coll = 2 r_B/lambda_0 [x_t^-1/2 - 1].
```

Die instantane Maxwell-Fraktion `v>v_esc` ist im Scaling `~0.343`, aber permanenter ballistischer Escape wird zu

```text
e_perm ~0.343 exp(-tau_coll).
```

An den getesteten atomaren Skalen ist `tau_coll~1e3...>1e5`, damit `e_perm` praktisch null und `chi_capture~1` im Reduced Strong-Coupling-Branch.

### A9.3 Processing capacity @`1e11 kg`

| `r_t` | `p` | `t_res` [s] | `Mdot_capacity` [kg/s] | `Xi_high` |
|---:|---:|---:|---:|---:|
| `3e-11 m` | `3.30e-5` | `1.36e-12` | `1.85e-5` | `0.0079` |
| `1e-10 m` | `9.90e-6` | `2.76e-11` | `9.13e-7` | `0.160` |
| `2e-10 m` | `4.95e-6` | `1.56e-10` | `1.61e-7` | `0.905` |

mit

```text
Xi = Mdot_supply / Mdot_capacity.
```

Damit:

```text
M=1e11 kg strong-coupling/recycling Reduced Branch:
SUPPLY-PROCESSING CAPABLE fuer alle getesteten r_t.
```

### A9.4 Massenscan

```text
M=1e10 kg:
    transition-scale/backpressure sensitive

M=1e11 kg:
    supply-processing capable in tested strong-coupling bracket

M=2e11 kg:
    clear capacity reserve

M=5e11 kg:
    very large capacity reserve.
```

Kritische Reduced-Skalen:

```text
xcrit low supply  ~8.507e-3
xcrit high supply ~3.397e-3.
```

Fuer `r_t=3e-11...2e-10 m`:

```text
Mcrit ~5.8e9 ... 9.6e10 kg.
```

### A9.5 Plasma-response / Quasineutralitaet

Beispiel `M=1e11 kg, r_t=1e-10 m`:

```text
t_plasma/t_res ~2.7e-9.
```

Bulk quasineutrality ist damit als Reduced Transportclosure gut motiviert; die diskrete BH-Ladung bleibt trotzdem nicht exakt geloest.

### A9.6 Weak-reaction Gate

Bei `M=1e11 kg`:

```text
Ni-threshold:
    t_res ~9.13e-14 s
    lambda_required ~1.10e13 s^-1

Fe-threshold:
    t_res ~1.50e-17 s
    lambda_required ~6.69e16 s^-1.
```

Vergleich:

```text
published fast 56Fe scale ~1.5916e4 s^-1.
```

Damit bleibt promptes Weak-Equilibrium im schnellen supply-processing Branch klar ungestuetzt.

### A9.7 Reduced Mdot consequence

Fuer `M>=~1e11 kg` im aktuellen Strong-Coupling/Recycling Reduced Branch:

```text
chi_transport ~1
```

und damit bei `1e11 kg`

```text
Mdot_BH,reduced ~1.47e-8 ... 1.46e-7 kg/s.
```

Dies ist eine reduzierte Modellvorhersage, keine Messung und noch keine first-principles WDM-Endrate.

## Aktuelle numerische Endmatrix

| Frage | Status |
|---|---|
| Schwarzschild-Dirac-Solver numerisch belastbar? | **PASS als Solver-/Regressionstest** |
| neutrale Earth-speed Protonen-Cross-Section bekannt? | **CALCULATED** |
| charged Proton Feedback teilweise berechnet? | **JA** |
| charged Electron Coulomb-Fernfeld geloest? | **OPEN** |
| Fe/Ni 0+ Composite-Wellensink berechnet? | **CALCULATED** |
| grosse Wellenunterdrueckung bei `1e11 kg` gefunden? | **NEIN** |
| ungescreenter BH-Coulombblocker bis `r_B` plausibel? | **NEIN im Screeningproxy** |
| Single-pass-Faktor = Netto-Mdot? | **NEIN** |
| strong-coupling inward collisionality moeglich? | **JA, reduzierter selbstkonsistenter Branch** |
| Backpressure kann Supply reduzieren? | **JA als reflektierender PDE-Grenzfall** |
| A9 `>=~1e11 kg` supply-processing test | **PASS within Reduced Strong-Coupling closure** |
| A9 `1e10 kg` transport | **OPEN / backpressure-sensitive** |
| prompt EC/NSE im schnellen Einzel-/Recyclingtransit? | **NICHT SUPPORTED** |
| finale first-principles `chi_transport` bekannt? | **OPEN** |
| finale species-resolved `Mdot_BH` bekannt? | **OPEN** |

## Formation

```text
in-situ collapse: FAIL
spaeter direct Earth capture: FAIL
Proto-Earth/Planetesimal Standardcapture: FAIL
Halo-to-cold-disk Standarddelivery: stark negativ
cold/co-moving Anfangsbedingung: Herkunft OPEN
```

## Naechster numerischer Block

```text
Stage 3.69F / A-10:
first-principles-informed WDM transport
+ time-dependent hydro/kinetic sink coupling
+ A4/A5 absorptive inner boundary
-> replace geometric mean-free-path proxy
-> final reduced species-resolved Mdot band.
```

## Gesamtstatus

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell.
H0: OPEN / nicht nachgewiesen.
Stage 3.69 Materie-Capture-/Transport-Submodule: stark fortgeschritten bis A-9.
A9 Reduced Strong-Coupling branch: >=~1e11 kg supply-processing capable; 1e10 kg backpressure-sensitive.
Stage 3.69 Full-Multiphysics: OPEN.
Stage 3.70 Real-Data-Falsification: OPEN.
Empirischer Erdzentrum-BH-Nachweis: keiner.
```
