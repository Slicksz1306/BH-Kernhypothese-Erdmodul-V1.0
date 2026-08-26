# Numerischer und physikalischer Status - V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Theorie-Textstand:** V1.5  
**Aktuelle Stufe:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; Stage 3.69A/3.69A-1 sowie Stage 3.69A-3 Quantum/Wave-Capture-Teilmodule numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 nicht durchgefuehrt

## 1. Aussagegrenze

Numerische Validierung bedeutet nur, dass ein definierter Solver-/Konvergenztest innerhalb seiner Gleichungen, Randbedingungen und Closures bestanden wurde. Sie bedeutet weder experimentelle Bestaetigung noch direkte Detektion eines Erdzentrum-BH.

Die Projektbranches bleiben getrennt:

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung.
```

Stage 3.69A-3 entscheidet nicht zwischen H+ und H0; Capture- und Charge-Feedback sind zunaechst gemeinsame Materiebausteine.

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
- Stage-3.69A-1 Schwarzschild-Dirac-Radialsolver mit Partialwellen-In/Out-Matching,
- Stage-3.69A-3 Earth-speed Protonen-Massenscan und erste Charge-Feedback-Skalen.

## 3. Wichtige Korrekturen

```text
Hard-Cavity als physischer Erdbranch -> verworfen
konstante Gamma~4 / ~54 r_s Langzeitgrenze -> zurueckgezogen
hcp-Fe 8-GPa-Mikrorettung in Coulombzone -> zurueckgezogen
getrennte Hawking/Michel-Schnittmengenlogik -> korrigiert
One-pass kinetic capture fraction als dauerhafte Suppression -> zurueckgezogen
Bondi/Michel als automatisch finale Horizon-Capture-Rate -> nicht zulaessig
Fe-56 als Spin-1/2-Dirac-Teilchen -> korrigiert; dominante Fe-56/Ni-58-Kerne haben 0+
Unruh-Low-Energy-Protonenwert bei alpha_p~0.353 als finale Earth-speed Cross-Section -> ersetzt durch vollen Dirac-Matcher
1-|S_kappa|^2 fuer extrem schwache Partialwellen -> durch flux-stabile Auswertung ergaenzt
```

## 4. H+-Numerik

Die Hawking-Normierung wurde korrigiert und durch Greybody-Primaerspektren gehaertet. Der relevante H+-Bereich liegt im getesteten Modell bei etwa

```text
4.82e11 ... 5.49e11 kg.
```

Der Projektvergleich mit SK-IV ergibt im entscheidenden 25.29-31.29-MeV-Band eine Signal/Limit-Ueberschreitung.

```text
H+ Standard-Hawking: FAIL im getesteten Projekt-Reinterpretationsmodell.
```

Das ist keine offizielle Super-K-Erdzentrum-BH-Exklusion.

## 5. H0-/gemeinsame Akkretionsnumerik

Die bisher getesteten reduzierten Proxies liefern:

- small-branch `GM`/Massenbuchhaltung: kompatibel;
- Traegheitsmoment/Rotation: Effekt extrem klein;
- vereinfachte Seismik: kein Ausschluss, direkter Mikrobereich nicht realistisch aufloesbar;
- zentraler PREM-Sound-Speed-/Supply-Proxy: `c_eff=10.4355 km/s`;
- Michel/Bondi: aeussere Supply-Vergleichsskala, keine finale Horizon-Rate;
- Solid/Rotation/Radial-Supply: kein nachgewiesener robuster Blocker;
- Knudsen/Loss-Cone: keine einfache dauerhafte One-pass-Sperre;
- Quantum/Wave-Capture: numerisch weiter gehaertet;
- radiatives/QED-Feedback: kein robuster Eddington-artiger Stopp im getesteten kleinen Bereich;
- globaler `47 +/- 2 TW`-Waerme-Sanity-Check: bisheriger kleiner Michel-Benchmark bleibt deutlich darunter.

## 6. Stage 3.68E - externe Feedback-Integration

```text
c_eff(PREM center) = 10.4355 km/s
r_B(M=1e11 kg) ~61 nm
r_s(M=1e11 kg) ~1.5e-16 m
```

Multiskalenarchitektur:

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

## 7. Stage 3.69A-1 – Schwarzschild-Dirac-Solver

### 7.1 Radialsolver und Strom

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

Das Verhalten ist qualitativ konsistent mit der publizierten Doran-Struktur. Ein vollstaendiger datenpunktgenauer Kurvenregressionstest bleibt offen.

## 8. Stage 3.69A-3 – Earth-speed Proton Capture

Referenz:

```text
v = 10.4355 km/s
u = 3.4809081e-5.
```

Die schwach absorbierten Partialwellen werden zusaetzlich ueber den konservierten Horizon-/Incoming-Flux ausgewertet:

```text
P_abs = (-W_H)/(2 q |A_in|^2),
q = p/(E+m),
W_H=-1.
```

Damit wird die numerisch schlecht konditionierte Subtraktion `1-|S|^2` fuer extrem kleine Absorptionswahrscheinlichkeiten vermieden.

### 8.1 Protonen-Massenscan

| `M_BH` | `alpha_p` | `kmax` | `x_match` | `sigma_D/sigma_classical` | `sigma_D` [m^2] |
|---:|---:|---:|---:|---:|---:|
| `1e10 kg` | `0.0353107` | 3 | `5e6` | `0.0326735` | `7.47496e-26` |
| `1e11 kg` | `0.353107` | 3 | `5e6` | `0.950295` | `2.17406e-22` |
| `2e11 kg` | `0.706215` | 5 | `2e6` | `1.008071` | `9.22496e-22` |
| `5e11 kg` | `1.76554` | 9 | `1e6` | `0.996621` | `5.70011e-21` |

Bei `5e11 kg` ist der Partialwellenschnitt relevant:

```text
kmax=5 -> 0.6015 classical
kmax=6 -> 0.8420
kmax=7 -> 0.99630
kmax=8 -> 0.99662110
kmax=9 -> 0.99662113.
```

### 8.2 Matchingradius-Spotcheck bei `1e11 kg`

```text
x_match=1e6 -> 0.95024543 classical
x_match=5e6 -> 0.95029487 classical
x_match=1e7 -> 0.95035969 classical.
```

Der zentrale Befund ist damit robust: beim neutralen `1e11 kg`-Referenzpunkt liegt der Protonenquerschnitt bei etwa `95%` des klassischen collisionless Vergleichswerts.

### 8.3 Korrektur des Unruh-Protonenbenchmarks

Frueherer analytischer Low-E-Wert bei `1e11 kg`:

```text
sigma_Unruh,p ~6.3447e-23 m^2.
```

Voller Dirac-Matcher:

```text
sigma_Dirac,p ~2.1741e-22 m^2.
```

Der Unruh-Wert bleibt als asymptotischer Low-E-/Low-Coupling-Benchmark dokumentiert, ist bei `alpha_p~0.353` aber nicht die finale Earth-speed Protonen-Cross-Section.

## 9. Stage 3.69A-3 – Charge-Feedback-Skalen

Bei `M_BH=1e11 kg` und `|Q|=e`:

```text
|F_C/F_G| proton   = 0.0206661
|F_C/F_G| electron = 37.9461.
```

Klassische Fernfeld-Kraftgrenzen:

```text
Q_max,p   = +48.3884 e = 7.75268e-18 C
|Q_max,e| =   0.026353 e = 4.22224e-21 C.
```

Stationaerer Equal-T-Plasma-Benchmark nach Zajacek et al.:

```text
Q_eq ~ +24.1810 e = 3.87423e-18 C.
```

RN-Extremalladungsskala:

```text
Q_extremal ~8.6175 C
Q_eq/Q_extremal ~4.50e-19.
```

Damit kann die elektrostatische Teilchendynamik schon bei winziger Nettoladung stark sein, obwohl die Raumzeitmetrikkorrektur praktisch vernachlaessigbar bleibt.

Diese Charge-Werte sind **keine** selbstkonsistente Erdkerngleichgewichtsloesung. Dichte Fe/Ni-Materie, Screening, Kollisionen, Degeneration, Ionisation, Kernreaktionen und Transport fehlen noch.

## 10. Formation-Numerik

```text
in-situ collapse -> FAIL
spaeter direct Earth capture -> FAIL
Proto-Earth / Planetesimal capture -> FAIL unter getesteten Bedingungen
gas drag -> unzureichend
halo -> cold disk -> pebble/SI delivery -> FAIL unter Standardbedingungen
cold/co-moving initial condition -> nicht hergeleitet
```

## 11. Was jetzt tatsaechlich entschieden ist

| Frage | Ergebnis |
|---|---|
| Ist ein grosses Erdzentrum-BH mit Erdstruktur vereinbar? | Nein. |
| Ueberlebt H+ Standard-Hawking den aktuellen Neutrinotest? | Nein, im getesteten Modell. |
| Ist ein kleines smooth H0 durch die bisherigen reduzierten Erdtests ausgeschlossen? | Nein. |
| Ist H0 dadurch bestaetigt? | Nein. |
| Funktioniert der isolierte Schwarzschild-Dirac-Radialsolver numerisch? | Ja, Selfchecks/Benchmarks bestanden. |
| Ist der neutrale Earth-speed Protonen-Capture bei `1e10...5e11 kg` berechnet? | Ja, als isolierter Dirac-Einzelteilchenbenchmark. |
| Liegt der `1e11 kg`-Protonenwert stark unter klassischem Capture? | Nein; numerisch etwa `0.9503 sigma_classical`. |
| Ist Ladungsfeedback potentiell dynamisch relevant? | Ja; bereits wenige bis einige Dutzend `e` sind relevante Kraftskalen. |
| Ist die selbstkonsistente `sigma_p,e(Q)`-Closure bekannt? | Nein. |
| Ist die finale Dense-Matter-Netto-Akkretionsrate bekannt? | Nein. |
| Gibt es einen hergeleiteten Standard-Formationweg? | Nein. |
| Gibt es eine eindeutige positive Messsignatur? | Nein. |

## 12. Nicht numerisch abgeschlossen

1. charged Dirac capture `sigma_p,e(Q)` und selbstkonsistentes `Q(t)`;
2. coherent Fe/Ni scalar/composite capture bzw. Dissociations-/Nukleonenclosure;
3. Screening, dichte Transport-/Reaktionsphysics und species-resolved Netto-`Mdot`;
4. Full-Stack Stage 3.69;
5. Stage 3.70: dedizierte Real-Data-/Experiment-Likelihood einer eindeutigen branch-spezifischen Signatur.

## 13. Endstatus

```text
H+ Standard-Hawking: FAIL im getesteten Projektmodell; Branch bleibt separat dokumentiert.
H0 heutige Existenzhypothese: OPEN / nicht durch die bisherigen reduzierten Erdtests ausgeschlossen.
Gemeinsamer neutraler Earth-speed Proton Dirac Capture: CALCULATED.
Charge-feedback force/equilibrium scales: CALCULATED as benchmarks.
Charged Dirac capture + self-consistent Q(t): OPEN.
Dense Fe/Ni species-resolved Netto-Akkretionsrate: OPEN.
Formation: stark negativ / kein Standardweg hergeleitet.
Empirischer Nachweis eines Erdzentrum-BH: keiner.
```

Siehe:

- [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md)
- [`STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md`](STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md)
- [`stage3_69a3_earth_proton_charge.py`](stage3_69a3_earth_proton_charge.py)
- [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md)
