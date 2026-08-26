# Numerischer und physikalischer Status – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Aktuelle Stufe:** numerischer Forschungsstand bis Stage 3.69D/A-8; Stage 3.69 Full-Multiphysics und Stage 3.70 offen

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
```

## H+

```text
M_BH ~4.82e11 ... 5.49e11 kg im getesteten Standard-Hawking-Projektbranch
H+ Standard-Hawking: FAIL im getesteten SK-IV-Projekt-Reinterpretationsmodell
```

Keine offizielle Super-K-Erdzentrum-BH-Exklusion wird behauptet.

## Gemeinsame Materie-/Capture-Numerik

### A-1 – Schwarzschild-Dirac

- massive Dirac-Radialgleichung: IMPLEMENTED
- regulaerer Horizon-Branch: IMPLEMENTED
- Wronskian/Stromerhaltung: PASS als Solver-Selfcheck
- In/Out-Matching: IMPLEMENTED
- Matchingradius-Konvergenz: PASS an getesteten Literaturpunkten
- Low-alpha externe Regression: PASS

### A-3 – Earth-speed neutrale Protonen

Bei `v=10.4355 km/s`:

```text
M=1e10 kg: sigma_p/sigma_classical ~0.03267
M=1e11 kg: ~0.95030
M=2e11 kg: ~1.00807
M=5e11 kg: ~0.99662
```

Referenz `1e11 kg`:

```text
sigma_p ~2.174e-22 m^2
```

Damit keine starke Protonen-Wellenunterdrueckung an diesem Referenzpunkt.

### A-4 – charged Proton Dirac

Kontrollierter Schwarzschild+Test-Coulomb-Subtest bei `1e11 kg`:

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

### A-5 – Fe/Ni 0+ Klein-Gordon

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
r_B ~6.13e-8 m
```

Also kein ungescreenter Coulomb-Blocker auf Bondi-Radius-Skala.

### A-6 – repeated encounters / Recycling

Einzelpass und collisional Supply unterscheiden sich stark:

```text
Mdot_single ~3.1e-14 kg/s
historischer Michel-Supply ~1.47e-8 ... 1.46e-7 kg/s
```

Repeated-encounter closure:

```text
chi = p/(p+e)
```

mit Capture `p` und permanentem Escape `e`.

Ein kleiner `p_single` ist deshalb **kein** automatischer stationaerer `Mdot`-Suppressionsfaktor.

### A-7 – Kollisionalitaet + PDE-Backpressure

Strong-coupling/geometrischer Branch:

```text
rho~r^-3/2
lambda~r^3/2
Kn~r^1/2
```

=> Kn sinkt nach innen.

Weak-Coulomb/Spitzer:

```text
lambda_C~T^2/n
Kn_C~r^-3/2
```

=> entgegengesetzter Trend, aber nur bei `Gamma<<1` gerechtfertigt.

1-D Bondi-Euler-Benchmark (`Gamma=1.5`): analytischen Massenfluss auf Prozentniveau reproduziert. Reflektierender Innenrand erzeugt Druckaufbau und outward shock.

```text
absorbing Bondi PDE: PASS benchmark
reflecting boundary: backpressure extreme demonstrated
```

### A-8 – WDM/Strong-Coupling + Weak Timescales

Referenz:

```text
rho0=13.0885 g/cm^3
T0=6000 K
```

Reduzierter inward-Sensitivitaetsbranch:

```text
rho~x^-3/2
T~x^-1
Gamma_i~x^1/2
Kn_geom~x^1/2
```

Elektronen relativistisch degeneriert bei etwa

```text
x~3.39e-4 ~1.4e5 r_s.
```

EC-Energieschwellen:

```text
58Ni -> 58Co: Qkin~0.381 MeV
x~1.66e-4 ~6.84e4 r_s
Gamma_i(Zeff=26)~203

56Fe -> 56Mn: Qkin~3.696 MeV
x~5.08e-6 ~2.09e3 r_s
Gamma_i(Zeff=26)~35.6
```

Der weak-Spitzer-Branch ist an diesen Schwellen im reduzierten hochionisierten Fe-Proxy nicht selbstkonsistent (`Gamma_i>>1`).

Publizierter schneller `56Fe`-EC-Vergleich:

```text
rho*Ye=1e11 g/cm^3, T9=3
lambda_ec~1.59e4 s^-1
tau_ec~6.3e-5 s
```

gegen lokale Reduced-Dynamik am Fe-Schwellenradius:

```text
t_dyn~4.7e-20 s
```

Damit:

```text
prompt one-pass weak equilibrium/neutronization: NOT SUPPORTED
```

Ein langer Residence-/Recyclingzustand kann weak reactions wieder relevant machen und bleibt offen.

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
| prompt EC/NSE im Einzeltransit? | **NICHT SUPPORTED** |
| finale `chi_transport` bekannt? | **OPEN** |
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
Stage 3.69E / A-9:
residence-time/backpressure transport
+ charge-neutrality closure
+ minimal Fe/Ni weak network
-> chi_transport
-> net Mdot_BH
```

## Gesamtstatus

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell.
H0: OPEN / nicht nachgewiesen.
Stage 3.69 Materie-Capture-Submodule: stark fortgeschritten bis A-8.
Stage 3.69 Full-Multiphysics: OPEN.
Stage 3.70 Real-Data-Falsification: OPEN.
Empirischer Erdzentrum-BH-Nachweis: keiner.
```
