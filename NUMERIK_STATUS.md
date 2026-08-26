# Numerischer und physikalischer Status - V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Theorie-Textstand:** V1.5  
**Aktuelle Stufe:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; Stage 3.69A/3.69A-1 Quantum-Capture-Teilmodul teilweise durchgefuehrt; Stage 3.69 Full-Multiphysics und Stage 3.70 nicht durchgefuehrt

## 1. Was „numerisch validiert“ bedeutet

Numerische Validierung bedeutet nur, dass ein definierter Solver-/Konvergenztest innerhalb seiner Gleichungen, Randbedingungen und Closures bestanden wurde. Sie bedeutet weder experimentelle Bestaetigung noch direkte Detektion eines Erdzentrum-BH.

## 2. Historischer Solverstack

Der Projektstack enthaelt unter anderem

- sphaerische GR-/TOV-/Matching-Grenztests,
- Layered-PREM-Closures,
- Horizon-/BH-konsistente Near-Zone-Randbehandlung,
- 1-D-Seismik-/Normalmodenproxies,
- Bondi-/Michel-Akkretionssolver,
- Rheologie-/EOS-/Coulomb-Sensitivitaeten,
- reduzierte Langzeit-ODEs,
- Knudsen-/kinetische und Loss-Cone-Proxies,
- Stage-3.69A-Regimecheck,
- Stage-3.69A-1 Schwarzschild-Dirac-Radialsolver mit Partialwellen-In/Out-Matching.

Die historischen `1e16 kg`, `r_c=500/300 km`-Matchingresultate bleiben als Solverentwicklung dokumentiert, validieren aber **nicht automatisch** den spaeteren kleinen smooth Branch.

## 3. Wichtige zurueckgezogene oder korrigierte Zwischenresultate

```text
Hard-Cavity als physischer Erdbranch -> verworfen
konstante Gamma~4 / ~54 r_s Langzeitgrenze -> zurueckgezogen
hcp-Fe 8-GPa-Mikrorettung in Coulombzone -> zurueckgezogen
getrennte Hawking/Michel-Schnittmengenlogik -> korrigiert
Stage-3.15 Hawking/Michel-Balance als aktueller H+-Rettungsbranch -> durch Stage 3.28/3.30 ueberholt
One-pass kinetic capture fraction als dauerhafte Suppression -> zurueckgezogen
100-m-Buchhaltungsradius als stark veraenderte physische Seismikzone -> korrigiert
Bondi/Michel als automatisch finale Horizon-Capture-Rate -> nicht zulaessig
Fe-56 als Spin-1/2-Dirac-Teilchen -> korrigiert; dominante Fe-56/Ni-58-Kerne haben 0+ und brauchen coherent scalar/composite treatment solange intakt
```

## 4. H+-Numerik

Die Hawking-Normierung wurde korrigiert und durch Greybody-Primaerspektren gehaertet. Der relevante H+-Bereich liegt bei etwa

```text
4.82e11 ... 5.49e11 kg.
```

Der Projektvergleich mit SK-IV ergibt im entscheidenden 25.29-31.29-MeV-Band eine Signal/Limit-Ueberschreitung.

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
```

## 5. H0-Numerik

Der H0-Stack behandelt Hawking nicht. Die getesteten reduzierten Proxies liefern:

- small-branch `GM`/Massenbuchhaltung: kompatibel;
- Traegheitsmoment/Rotation: Effekt extrem klein;
- starke physische Near Zone: mikro-/nanoskopisch statt ganze `r_rep`-Zone;
- vereinfachte Seismik: kein Ausschluss, aber direkter Mikrobereich nicht realistisch aufloesbar;
- zentraler PREM-Sound-Speed-Proxy: `c_eff=10.4355 km/s`;
- Michel-Supply: moegliche aeussere Kapazitaet, exakte Netto-Rate offen;
- Solid/Rotation/Radial-Supply: kein nachgewiesener robuster Blocker;
- Knudsen/Loss-Cone: keine einfache dauerhafte One-pass-Sperre;
- Quantum/Wave-Capture: teilweise numerisch umgesetzt;
- radiatives/QED-Feedback: kein robuster Eddington-artiger Stopp im getesteten kleinen Bereich;
- 4.54-Gyr-Massen-/Waerme-Stressmodelle: global kompatibel im kleinen Branch;
- globaler `47 +/- 2 TW`-Waerme-Sanity-Check: oberer bisheriger kleiner Michel-Benchmark bleibt deutlich darunter.

## 6. Stage 3.68E - externe Feedback-Integration

Externes Fachfeedback aus Numerical Relativity/HPC und globaler Seismologie wurde als Modellhaertung integriert. Es stellt keine externe Bestaetigung dar.

```text
c_eff(PREM center) = 10.4355 km/s
r_B(M=1e11 kg) ~61 nm
r_s(M=1e11 kg) ~1.5e-16 m
```

Die Multiskalenarchitektur lautet

```text
PREM global
 -> Elastoplastik/Rheologie
 -> Mikro-Hydrodynamik
 -> kinetische GR-Zone
 -> species/composition closure
 -> Quantum/Wave-Capture
 -> charge/nuclear feedback
 -> GR-Horizon-Sink.
```

## 7. Stage 3.69A / 3.69A-1 – numerischer Quantum-Capture-Fortschritt

### 7.1 Radialsolver

Massive Dirac-Gleichung auf Schwarzschild-Hintergrund in horizon-regulaeren Painleve-Gullstrand-Koordinaten implementiert.

Benchmark `alpha=0.2, u=0.5`:

```text
kappa=-1: relative Wronskian drift ~3.68e-10
kappa=+1: relative Wronskian drift ~1.45e-11
```

```text
radial Dirac current conservation: PASS as solver self-check.
```

### 7.2 In/Out-Matching

Absorption wird ueber

```text
S_kappa = A_out/A_in
sigma_A = pi/p^2 sum |kappa| (1-|S_kappa|^2)
```

bestimmt. Lokale grosse-r-In/Out-Eigenmoden der exakten radialen Matrix werden auf die publizierten asymptotischen Stroeme normiert.

Matchingradius-Test:

```text
alpha=0.2, E/m=1.5:
  x=500   sigma/M^2=123.2562
  x=1000  sigma/M^2=123.2594
  x=2000  sigma/M^2=123.2587

alpha=0.2, E/m=2.0:
  x=500   sigma/M^2=103.9639
  x=1000  sigma/M^2=103.9655
  x=2000  sigma/M^2=103.9650
```

Weitere Struktur:

```text
E/m=1.5: Dirac ~123.259 ; classical ~128.680
E/m=2.0: Dirac ~103.965 ; classical ~103.380
E/m=5.0: Dirac ~89.682  ; classical ~87.174
geometric optics: 27*pi ~84.823
```

Das Verhalten ist qualitativ konsistent mit Doran: energieabhaengige Unter-/Ueberschwingungen um den klassischen Grenzwert und Hochenergie-Annaeherung. Ein datenpunktgenauer Regressionstest gegen eine digitalisierte Publikationskurve bleibt offen.

### 7.3 Erd-Referenzpunkt – isolierte Einzelteilchen

Bei `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
electron: alpha=1.923e-4, Unruh-lowE sigma ~3.46e-26 m^2
proton:   alpha=3.531e-1, Unruh-lowE sigma ~6.34e-23 m^2
classical collisionless low-v sigma ~2.29e-22 m^2
```

Dies zeigt starke Speziesabhaengigkeit im isolierten Wellenproblem, ist aber **keine** dichte Netto-Akkretionsrate.

### 7.4 Noch offene Closure

- dominante `Fe-56`/`Ni-58`-Kerne: `0+`, daher coherent scalar/Klein-Gordon/composite capture solange intakt;
- bei Dissoziation: Nukleonen-/Elektronen-Dirac-Kanaele;
- elektrostatisches Ladungsfeedback zwischen Elektronen-/Ionen-Capture;
- Kollisions-/Transportclosure zwischen Fluid-Supply und Einzelteilchen-Wellenproblem;
- Nuklear-/Pair-/Reaktionszeitskalen;
- daraus erst: species-resolved dense-core Netto-`Mdot`.

## 8. Formation-Numerik

```text
in-situ collapse -> FAIL
spaeter direct Earth capture -> FAIL
Proto-Earth / Planetesimal capture -> FAIL unter getesteten Bedingungen
gas drag -> unzureichend
halo -> cold disk -> pebble/SI delivery -> FAIL unter Standardbedingungen
cold/co-moving initial condition -> nicht hergeleitet
```

## 9. Was jetzt tatsaechlich entschieden ist

| Frage | Ergebnis |
|---|---|
| Ist ein grosses Erdzentrum-BH mit Erdstruktur vereinbar? | Nein. |
| Ueberlebt H+ Standard-Hawking den aktuellen Neutrinotest? | Nein, im getesteten Modell. |
| Ist ein kleines smooth H0 durch die bisherigen reduzierten Erdtests ausgeschlossen? | Nein. |
| Ist H0 dadurch bestaetigt? | Nein. |
| Funktioniert der isolierte Schwarzschild-Dirac-Radialsolver numerisch? | Ja, Selfcheck bestanden. |
| Ist In/Out-Matching fuer getestete Literaturpunkte stabil? | Ja, im getesteten `alpha=0.2`-Benchmark. |
| Ist die finale Dense-Matter-H0-Netto-Akkretionsrate bekannt? | Nein. |
| Gibt es einen hergeleiteten Standard-Formationweg? | Nein. |
| Gibt es eine eindeutige positive Messsignatur? | Nein. |

## 10. Nicht numerisch abgeschlossen

1. Full-Stack Stage 3.69: relativistische Elastoplastik + Dense Plasma/QED/Nuklear + kinetischer Transport + species-resolved Wave-Capture + Charge/Nuclear feedback + Horizon-Sink;
2. Stage 3.70: dedizierte Real-Data-/Experiment-Likelihood einer eindeutigen H0-Signatur.

## 11. Endstatus

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 heutige Existenzhypothese: OPEN / nicht durch die bisherigen Erdtests ausgeschlossen.
H0 isolierte Spin-1/2-Capture: teilweise numerisch geloest/benchmarkiert.
H0 exakte Dense-Matter-Netto-Akkretionsrate: OPEN.
H0 fundamentale Basis: OPEN.
H0 Formation: stark negativ.
Empirischer Nachweis: keiner.
```

Siehe [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md) und [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md).
