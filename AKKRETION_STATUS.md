# Akkretions- und Langzeitstatus - Abschluss Stage 3.68

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026

## 1. Aussagegrenze

Bondi- und Michel-Raten sind Modellkapazitaeten innerhalb ihrer Annahmen. Eine reproduzierte Akkretionsformel ist kein Nachweis eines BH im Erdzentrum. Seit Stage 3.68E werden Bondi/Michel zudem ausdruecklich nur als aeussere Supply-/Benchmarkmodelle behandelt; die finale Netto-Capture-Rate kann im kleinen-Horizont-Regime quanten-/wellenmechanisch abweichen.

## 2. PREM-Sound-Speed-Proxy und Bondi-Skala

Die Bondi-Skala und klassische Bondi-Raten haengen kritisch von der verwendeten effektiven Schallgeschwindigkeit ab. Fuer den zentralen PREM-Proxy werden

```text
rho_c = 13.0885 g/cm^3
V_P   = 11.2622 km/s
V_S   = 3.6678 km/s
```

verwendet. Daraus folgt fuer den fluidartigen Bulk-Sound-Speed-Proxy

```text
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s
      ~ 10.44 km/s.
```

Damit gilt bei `M_BH=1e11 kg` grob

```text
r_B = G M_BH / c_eff^2 ~ 61 nm.
```

`c_eff` ist ein aeusserer PREM-/Supply-Proxy und keine mikroskopische Dispersionsrelation der tiefen Capture-Zone.

## 3. Michel-Benchmark

Der relativistische Michel-Solver bestand den analytischen `Gamma=2`-Selfcheck. Fuer den historischen `M=1e16 kg`-Benchmark ergab die getestete phaenomenologische condensed-to-degenerate EOS

```text
Mdot_Michel ~147 ... 1460 kg/s.
```

Mit der verwendeten `Mdot proportional M^2`-Skalierung:

```text
M=1e10 kg: ~1.47e-10 ... 1.46e-9 kg/s
M=1e11 kg: ~1.47e-8  ... 1.46e-7 kg/s
M=2e11 kg: ~5.88e-8  ... 5.84e-7 kg/s
M=5e11 kg: ~3.68e-7  ... 3.65e-6 kg/s
```

Diese Werte sind Supply-/Michel-Benchmarks, keine gemessenen oder finalen Netto-Capture-Raten.

## 4. H+ versus H0

### H+

Standard-Hawking ist nicht mehr als moeglicher Akkretions-Balance-Retter zu behandeln. Nach der Greybody-/Super-K-Haertung faellt der relevante H+-Branch bereits am Neutrinotest.

### H0

Fuer H0 entfaellt Hawking-Strahlung definitionsgemaess. Der Akkretionsaudit muss deshalb allein durch Materietransport, Capture, Langzeitwachstum und Waerme bestanden werden.

## 5. Yield und plastischer Supply

Aktuelle dynamische Festigkeitsdaten von Eisen nahe inner-core-artigen Bedingungen zeigen, dass ein statischer starrer Kaefig keine robuste Near-Zone-Loesung ist. Der BH-induzierte Stress kann die verwendeten Yield-Skalen in der tiefen Zone uebersteigen.

```text
statische Solid-Cage-Loesung: kein robuster Blocker.
```

## 6. Rotation

Die fuer die Michel-Supply-Raten erforderlichen Winkelimpuls-Torques sind klein. Ein pauschales Argument

```text
Erdrotation -> Circularization -> Michel blockiert
```

wurde deshalb zurueckgezogen.

```text
Rotation als generischer Blocker: FAIL.
```

## 7. Radialer Supply

Ein bewusst pessimistischer Bruecken-Sensitivity-Test zwischen geophysikalischer Rheologie und Hochraten-Daten fand keinen Radius, an dem die Michel-Supply zwingend scheitern muss.

```text
voller Michel-Supply als aeussere Kapazitaet: plausibel, aber nicht bewiesen.
exakte Rheologie: OPEN.
```

## 8. Kinetischer Uebergang

Knudsen-/Kollisionsproxies verschieben den kinetischen Uebergang in eine extrem kleine Zone. Eine naive Multiplikation der Michel-Rate mit einer einmaligen geometrischen Capture-Cone-Fraktion wurde spaeter zurueckgezogen, weil nicht sofort eingefangene Partikel in der kollisionalen Umgebung recycelt werden koennen.

## 9. Loss Cone und Reservoir

Der reduzierte Loss-Cone-Test deutet auf ein **full-loss-cone**-Regime statt auf einen leeren Loss Cone. Ein Reservoir-/Fokker-Planck-Closure benoetigt nur lokale Dichteverstaerkung, um die innere Sink-Kapazitaet an den aeusseren Supply anzupassen.

```text
permanenter 1e-4-One-pass-Suppressionsfaktor: zurueckgezogen.
exakte gekoppelte kinetische Loesung: OPEN.
```

## 10. Quantum/Wave-Capture – neuer offener Pflichtblock

Bei `M_BH ~ 1e11 kg` liegt

```text
r_s ~ 1.5e-16 m.
```

Damit ist nicht garantiert, dass der geometrisch-optische bzw. klassische Teilchengrenzfall bis zum Horizont gilt. Wenn relevante de-Broglie-/Compton-/Streuskalen groesser oder vergleichbar zur Horizontskala sind, muessen Absorptionsquerschnitte quanten-/wellenmechanisch bestimmt werden.

```text
Bondi/Michel -> aeusserer Supply-Benchmark
kinetische Zone -> Phasenraumzufuhr
Quantum/Wave-Capture -> tatsaechliche Absorptionswahrscheinlichkeit
GR-Horizon-Sink -> innere Randbedingung
```

Die finale H0-Netto-Akkretionsrate ist daher bis zur Kopplung dieses Blocks **OPEN**.

## 11. MeV-/QED-/Strahlungsfeedback

Der viriale Ionen-Energiescale darf nicht automatisch als einthermische Elektronen-/Photonentemperatur interpretiert werden. Pair- und Nuklearprozesse koennen relevant werden, ihre Gleichgewichtseinstellung ist in der extrem schnellen Mikrozone aber nicht garantiert.

Selbst die extreme Obergrenze, die gesamte `Mdot c^2`-Leistung als outward radiation behandelt, bleibt im untersuchten kleinen Massenbereich unter einer Fe-artigen Eddington-Skala. Eine 2026 publizierte sphaerische PBH-Akkretionsstudie findet zudem fuer kleine PBHs ein Hot-Bondi-Regime ohne generischen radiativen Stopp (arXiv:2606.02726).

```text
radiativer/QED-Stopp: kein robuster Blocker gefunden.
exakte MeV-Mikrophysik: OPEN.
```

## 12. Langzeitwachstum

Bei rueckwaertiger Integration eines `dM/dt=kM^2`-Stressmodells muss zwischen **heutiger Masse** und **Anfangsmasse** unterschieden werden. Eine heutige Masse von z.B. `5e11 kg` bedeutet nicht automatisch einen vergangenen Runaway; die Anfangsmasse kann entsprechend kleiner gewesen sein.

Im getesteten kleinen H0-Bereich bleibt der ueber 4.54 Gyr akkretierte Anteil der gesamten Erdmasse global winzig, sofern die verwendete Supply-/Capture-Rate in dieser Groessenordnung liegt.

## 13. Globaler Waerme-Sanity-Check

Als konservative globale Vergleichsskala wird der terrestrische Oberflaechen-Waermefluss `~47 +/- 2 TW` verwendet (Davies & Davies 2010).

Fuer

```text
P_heat = eta Mdot c^2
```

folgt

```text
Mdot_max = P_Earth/(eta c^2).
```

Bei `eta=1`:

```text
Mdot_max ~5.23e-4 kg/s
         ~1.65e4 kg/year.
```

Der obere bisherige Michel-Benchmark des kleinen Branches bei `M=5e11 kg` ist

```text
Mdot ~3.65e-6 kg/s
     ~115 kg/year
P_heat(eta=1) ~0.328 TW.
```

Damit liegt dieser Benchmark um etwa Faktor `143` unter der globalen 47-TW-Vergleichsskala.

```text
47-TW global heat sanity check:
    kein Ausschluss des getesteten kleinen H0-Michel-Benchmarks.
```

Dies ist keine vollstaendige thermische Simulation. Lokale Energieablagerung, Transport und die reale Effizienz `eta` bleiben Stage-3.69-Outputs. Kleinere `eta` lockern die globale Massenraten-Obergrenze proportional zu `1/eta`.

## 14. Endstatus Akkretion

```text
H+:
    durch Standard-Hawking-Neutrinotest bereits FAIL; Akkretionsbalance rettet H+ nicht.

H0:
    exakte Netto-Akkretionsrate OPEN.
    kein bisher getesteter Solid-, Rotation-, Loss-Cone- oder radiativer Mechanismus
    liefert eine robuste vollstaendige Sperre.
    Quantum/Wave-Capture ist als zusaetzlicher Pflichtblock noch nicht geloest.
    reduzierte Erdalter-Massen-/Waermetests schliessen den kleinen Branch nicht aus.
```

## 15. Stage 3.69 – ausstehende High-Fidelity-Schliessung

Die exakte H0-Akkretionsrate bleibt eine offene Multiphysikfrage. V1.5 definiert Stage 3.69 als `DEFINED / NOT PERFORMED`: GR-Hydro/Kinetik, Elastoplastik, Dense-Matter-EOS, Transport, QED-/Nuklear-Zeitskalen, Quantum/Wave-Capture und Horizon-Sink muessen in einem reproduzierbaren verschachtelten Solver gekoppelt werden. Der erste realistische Meilenstein ist ein 1-D/2-D-Prototyp.

Details: [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md) und [`EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`](EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md).
