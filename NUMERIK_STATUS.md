# Numerischer und physikalischer Status - Abschluss Stage 3.68

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Theorie-Textstand:** V1.5  
**Aktuelle Stufe:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; Stage 3.69/3.70 definiert, nicht durchgefuehrt

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
- Knudsen-/kinetische und Loss-Cone-Proxies.

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
Bondi/Michel als automatisch finale Horizon-Capture-Rate -> nicht mehr zulaessig; Quantum/Wave-Capture OPEN
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
- zentraler PREM-Sound-Speed-Proxy explizit: `c_eff=10.4355 km/s`;
- Michel-Supply: moegliche aeussere Kapazitaet, exakte Netto-Rate offen;
- Solid/Rotation/Radial-Supply: kein nachgewiesener robuster Blocker;
- Knudsen/Loss-Cone: innere kinetische Capture nicht als einfache dauerhafte `1e-4`-Sperre haltbar;
- Quantum/Wave-Capture: neuer offener Pflichtblock fuer kleine Horizontskala;
- radiatives/QED-Feedback: kein robuster Eddington-artiger Stopp im getesteten kleinen Bereich;
- 4.54-Gyr-Massen-/Waerme-Stressmodelle: global kompatibel im kleinen Branch;
- globaler `47 +/- 2 TW`-Waerme-Sanity-Check: oberer bisheriger kleiner Michel-Benchmark bleibt deutlich darunter.

## 6. Stage 3.68E - externe Feedback-Integration

Externes Fachfeedback aus Numerical Relativity/HPC und globaler Seismologie wurde als Modellhaertung integriert. Es stellt keine externe Bestaetigung dar.

Numerische Konsequenzen:

```text
c_eff(PREM center) = 10.4355 km/s
r_B(M=1e11 kg) ~61 nm
r_s(M=1e11 kg) ~1.5e-16 m
```

Die ausstehende Multiskalenarchitektur lautet nun

```text
PREM global
 -> Elastoplastik/Rheologie
 -> Mikro-Hydrodynamik
 -> kinetische GR-Zone
 -> Quantum/Wave-Capture
 -> GR-Horizon-Sink.
```

Eine aeussere Newton-/Materialzone mit innerer GR-Zone bleibt als Domain-Decomposition grundsaetzlich sinnvoll, sofern Matching, Erhaltung und Schnittstellenfehler explizit kontrolliert werden.

Der globale Waerme-Sanity-Check verwendet

```text
P_heat = eta Mdot c^2.
```

Bei `P_Earth=47 TW` und `eta=1` folgt `Mdot_max~5.23e-4 kg/s ~1.65e4 kg/year`. Der obere bisherige Michel-Benchmark bei `M=5e11 kg`, `Mdot~3.65e-6 kg/s`, entspraeche `~0.328 TW` bzw. `~115 kg/year` und bleibt damit etwa Faktor `143` unter dieser Vergleichsskala.

## 7. Formation-Numerik

Die Formationstests sind keine Beweise fuer eine Herkunft, sondern Eliminations-/Feasibility-Tests.

```text
in-situ collapse -> FAIL
spaeter direct Earth capture -> FAIL
Proto-Earth / Planetesimal capture -> FAIL unter getesteten Bedingungen
gas drag -> unzureichend
halo -> cold disk -> pebble/SI delivery -> FAIL unter Standardbedingungen
cold/co-moving initial condition -> nicht hergeleitet
```

Die reduzierte PREM-/Chandrasekhar-Capture-Grenze zeigt fuer `~1e11 kg`, dass spaeter Earth-Capture nur bei extrem kleinen hyperbolischen Ueberschussgeschwindigkeiten im mm/s- bis cm/s-Bereich moeglich waere.

## 8. Was Stage 3.68 / 3.68E tatsaechlich entscheidet

| Frage | Ergebnis |
|---|---|
| Ist ein grosses Erdzentrum-BH mit Erdstruktur vereinbar? | Nein. |
| Ueberlebt H+ Standard-Hawking den aktuellen Neutrinotest? | Nein, im getesteten Modell. |
| Ist ein kleines smooth H0 durch die bisherigen reduzierten Erdtests ausgeschlossen? | Nein. |
| Ist H0 dadurch bestaetigt? | Nein. |
| Ist die finale H0-Netto-Akkretionsrate bekannt? | Nein; Quantum/Wave-Capture fehlt. |
| Gibt es einen hergeleiteten Standard-Formationweg? | Nein. |
| Gibt es eine eindeutige positive Messsignatur? | Nein. |

## 9. Nicht numerisch abgeschlossen

Zwei Endstufen bleiben ausserhalb des derzeitigen Stacks:

1. gekoppelte relativistische Elastoplastik + Dense Plasma/QED/Nuklearreaktionen + kinetischer Transport + Quantum/Wave-Capture + Horizon-Sink und bei makroskopischer Kopplung anschliessende 3-D-Full-Wave-Seismik;
2. dedizierte Real-Data-/Experiment-Likelihood auf eine eindeutige H0-Signatur.

## 10. Endstatus

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 heutige Existenzhypothese: OPEN / nicht durch die bisherigen Erdtests ausgeschlossen.
H0 exakte Netto-Akkretionsrate: OPEN; Quantum/Wave-Capture nicht geloest.
H0 fundamentale Basis: OPEN.
H0 Formation: stark negativ.
Empirischer Nachweis: keiner.
```

## Stage 3.69/3.70 – nur Protokolldefinition

V1.5 definiert die High-Fidelity-Multiphysik- und H0-Real-Data-Endtests. Es wurde **kein** Stage-3.69-HPC-Lauf und **keine** dedizierte Stage-3.70-H0-Likelihood-Analyse durchgefuehrt. Stage 3.68E dokumentiert nur die technische Integration externen Fachfeedbacks. Siehe [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md) und [`EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`](EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md).
