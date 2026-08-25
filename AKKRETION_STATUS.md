# Akkretions- und Langzeitstatus - Abschluss Stage 3.68

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 25.08.2026

## 1. Aussagegrenze

Bondi- und Michel-Raten sind Modellkapazitaeten innerhalb ihrer Annahmen. Eine reproduzierte Akkretionsformel ist kein Nachweis eines BH im Erdzentrum.

## 2. Michel-Benchmark

Der relativistische Michel-Solver bestand den analytischen `Gamma=2`-Selfcheck. Fuer den historischen `M=1e16 kg`-Benchmark ergab die getestete phenomenologische condensed-to-degenerate EOS

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

Diese Werte sind Supply-/Michel-Benchmarks, keine gemessenen Raten.

## 3. H+ versus H0

### H+

Standard-Hawking ist nicht mehr als moeglicher Akkretions-Balance-Retter zu behandeln. Nach der Greybody-/Super-K-Haertung faellt der relevante H+-Branch bereits am Neutrinotest.

### H0

Fuer H0 entfaellt Hawking-Strahlung definitionsgemaess. Der Akkretionsaudit muss deshalb allein durch Materietransport, Langzeitwachstum und Waerme bestanden werden.

## 4. Yield und plastischer Supply

Aktuelle dynamische Festigkeitsdaten von Eisen nahe inner-core-artigen Bedingungen zeigen, dass ein statischer starrer Kaefig keine robuste Near-Zone-Loesung ist. Der BH-induzierte Stress kann die verwendeten Yield-Skalen in der tiefen Zone uebersteigen.

```text
statische Solid-Cage-Loesung: kein robuster Blocker.
```

## 5. Rotation

Die fuer die Michel-Supply-Raten erforderlichen Winkelimpuls-Torques sind klein. Ein pauschales Argument

```text
Erdrotation -> Circularization -> Michel blockiert
```

wurde deshalb zurueckgezogen.

```text
Rotation als generischer Blocker: FAIL.
```

## 6. Radialer Supply

Ein bewusst pessimistischer Bruecken-Sensitivity-Test zwischen geophysikalischer Rheologie und Hochraten-Daten fand keinen Radius, an dem die Michel-Supply zwingend scheitern muss.

```text
voller Michel-Supply: plausibel, aber nicht bewiesen.
exakte Rheologie: OPEN.
```

## 7. Kinetischer Uebergang

Knudsen-/Kollisionsproxies verschieben den kinetischen Uebergang in eine extrem kleine Zone. Eine naive Multiplikation der Michel-Rate mit einer einmaligen geometrischen Capture-Cone-Fraktion wurde spaeter zurueckgezogen, weil nicht sofort eingefangene Partikel in der kollisionalen Umgebung recycelt werden koennen.

## 8. Loss Cone und Reservoir

Der reduzierte Loss-Cone-Test deutet auf ein **full-loss-cone**-Regime statt auf einen leeren Loss Cone. Ein Reservoir-/Fokker-Planck-Closure benoetigt nur lokale Dichteverstaerkung, um die innere Sink-Kapazitaet an den aeusseren Supply anzupassen.

```text
permanenter 1e-4-One-pass-Suppressionsfaktor: zurueckgezogen.
exakte gekoppelte kinetische Loesung: OPEN.
```

## 9. MeV-/QED-/Strahlungsfeedback

Der viriale Ionen-Energiescale darf nicht automatisch als einthermische Elektronen-/Photonentemperatur interpretiert werden. Pair- und Nuklearprozesse koennen relevant werden, ihre Gleichgewichtseinstellung ist in der extrem schnellen Mikrozone aber nicht garantiert.

Selbst die extreme Obergrenze, die gesamte `Mdot c^2`-Leistung als outward radiation behandelt, bleibt im untersuchten kleinen Massenbereich unter einer Fe-artigen Eddington-Skala. Eine 2026 publizierte sphaerische PBH-Akkretionsstudie findet zudem fuer kleine PBHs ein Hot-Bondi-Regime ohne generischen radiativen Stopp (arXiv:2606.02726).

```text
radiativer/QED-Stopp: kein robuster Blocker gefunden.
exakte MeV-Mikrophysik: OPEN.
```

## 10. Langzeitwachstum

Bei rueckwaertiger Integration eines `dM/dt=kM^2`-Stressmodells muss zwischen **heutiger Masse** und **Anfangsmasse** unterschieden werden. Eine heutige Masse von z.B. `5e11 kg` bedeutet nicht automatisch einen vergangenen Runaway; die Anfangsmasse kann entsprechend kleiner gewesen sein.

Im getesteten kleinen H0-Bereich bleibt der ueber 4.54 Gyr akkretierte Anteil der gesamten Erdmasse global winzig.

## 11. Waerme

Selbst sehr konservative lokale Energieobergrenzen aus den Michel-Benchmarks bleiben fuer den kleinen H0-Branch klein gegen die gesamte terrestrische Waermeleistung. Das schliesst lokale Mikrophysik nicht, liefert aber keinen globalen Waermeausschluss.

## 12. Endstatus Akkretion

```text
H+:
    durch Standard-Hawking-Neutrinotest bereits FAIL; Akkretionsbalance rettet H+ nicht.

H0:
    exakte Akkretionsrate OPEN.
    kein bisher getesteter Solid-, Rotation-, Loss-Cone- oder radiativer Mechanismus
    liefert eine robuste vollstaendige Sperre.
    reduzierte Erdalter-Massen-/Waermetests schliessen den kleinen Branch nicht aus.
```

## 13. Stage 3.69 – ausstehende High-Fidelity-Schliessung

Die exakte H0-Akkretionsrate bleibt eine offene Multiphysikfrage. V1.5 definiert Stage 3.69 als `DEFINED / NOT PERFORMED`: GR-Hydro/Kinetik, Elastoplastik, Dense-Matter-EOS, Transport, QED-/Nuklear-Zeitskalen und Horizon-Capture muessen in einem reproduzierbaren verschachtelten Solver gekoppelt werden. Der erste realistische Meilenstein ist ein 1-D/2-D-Prototyp. Details: [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md).
