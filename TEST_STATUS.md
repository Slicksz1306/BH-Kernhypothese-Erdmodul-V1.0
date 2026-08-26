# SL/BH-Kernhypothese Erdmodul - Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 26.08.2026  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; 3.69/3.70 definiert, nicht durchgefuehrt

## Statusbegriffe

- **PASS/kompatibel** = innerhalb des konkret benannten reduzierten Modells kein Widerspruch gefunden; kein empirischer Nachweis.
- **FAIL** = der konkret benannte Branch/Mechanismus widerspricht dem verwendeten Test oder kann die erforderliche Bedingung nicht erfuellen.
- **OPEN** = mit vorhandenen Gleichungen/Daten nicht abschliessend entschieden.
- **nicht anwendbar** = der Test setzt Physik voraus, die der jeweilige Branch definitionsgemaess nicht besitzt.
- **zurueckgezogen/korrigiert** = fruehere Zwischenaussage durch einen haerteren Test ersetzt.

Kein Status in dieser Datei ist eine direkte Detektion eines Erdzentrum-BH.

## 1. Branch-Definition

```text
H+ = Standard-Hawking-Strahlung
H0 = P_Hawking = 0 (nichtstandardmaessige Gegenhypothese)
```

## 2. Strukturbranches

| Test | Status |
|---|---|
| starke Zentralmassenvariante | **FAIL** |
| Hard-Cavity/Hard-Replacement | **FAIL**, mechanisch verworfen |
| kleiner smooth-compensated Branch | mathematisch massenerhaltend; weiter getestet |
| Verwechslung `r_s=r_B=r_rep` | **FAIL**, drei getrennte Skalen |

## 3. H+ - Hawking/Greybody/Neutrinos

Stage 3.28 korrigierte die Hawking-Normierung. Der relevante H+-Bereich verschob sich auf etwa

```text
4.82e11 ... 5.49e11 kg.
```

Stage 3.30 verglich ein konservatives Greybody-Primaer-`anti-nu_e`-Signal mit publizierten spektrumsunabhaengigen SK-IV-Limits.

```text
25.29-31.29 MeV:
Projektfluss ~0.098 ... 0.122 cm^-2 s^-1 MeV^-1
SK-IV observed 90% CL = 0.04 cm^-2 s^-1 MeV^-1
```

**Status:**

```text
H+ Standard-Hawking: FAIL im Projekt-Reinterpretationstest.
```

Aussagegrenze: keine offizielle Super-K-Erdzentrum-BH-Exklusion.

## 4. H0 - Akkretion / Langzeit

Der Stage-3.12-Michel-Benchmark fuer `1e16 kg` lautet

```text
Mdot_Michel ~147 ... 1460 kg/s.
```

Fuer den zentralen PREM-Supply-Proxy wird jetzt explizit

```text
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s
```

mit `V_P=11.2622 km/s` und `V_S=3.6678 km/s` dokumentiert.

Die weiteren Stages prueften Yield, plastischen Supply, Rotation, Knudsen-Uebergang, kinetischen Capture, Loss-Cone-Recycling und radiatives/QED-Feedback.

| Teiltest | H0-Status |
|---|---|
| statische Festkoerperbarriere | kein robuster Blocker |
| Rotation/Winkelimpuls | kein robuster Blocker |
| radialer Supply | kein zwingender Engpass im getesteten Brueckenmodell |
| One-pass kinetic capture als permanenter Faktor | **zurueckgezogen** |
| Loss Cone / Recycling | eher full-loss-cone; exakte kinetische Loesung OPEN |
| Reservoir/Fokker-Planck-Closure | kein makroskopischer Stau zwingend erforderlich |
| radiativer Eddington-Stopp | kein robuster Stopp im getesteten Massenbereich |
| exakte MeV-Plasma/QED/Nuklearphysik | **OPEN** |
| Quantum/Wave-Capture bei kleiner Horizontskala | **OPEN / neu als Stage-3.69-Pflichtblock** |
| globaler 47-TW-Waerme-Sanity-Check | kein Ausschluss des getesteten kleinen Michel-Benchmarks |
| Erdalter-Masse/Waerme im kleinen Branch | kein Ausschluss in den reduzierten Stressproxies |

Der 47-TW-Sanity-Check verwendet `P_heat=eta Mdot c^2`. Fuer `eta=1` folgt `Mdot_max~1.65e4 kg/year`. Der obere bisherige Michel-Benchmark bei `5e11 kg` liegt bei etwa `115 kg/year` bzw. `0.328 TW`, also rund Faktor `143` darunter. Das ist ein globaler Proxy, keine lokale Multiphysik-Loesung.

## 5. Erdstruktur / Seismik

| Test | kleiner smooth H0-Branch |
|---|---|
| Gesamtmasse / `GM` | kompatibel durch redistributive Buchhaltung |
| Traegheitsmoment / Rotation | Effekt im kleinen Branch extrem klein |
| reduzierte Hydrostatik | kein Ausschluss |
| starke gesamte `r_rep`-Zone | frueherer Proxy **korrigiert**; physische starke Zone liegt viel tiefer |
| Body-wave Timing Proxy | kein messbarer robuster Ausschluss |
| Normalmodenproxy | kein messbarer robuster Ausschluss |
| direkte Nano-/Mikrometer-Seismik | keine realistische raeumliche Aufloesung |
| echte 3-D-Full-Wave-Likelihood | **nicht durchgefuehrt; nur sinnvoll bei makroskopisch gekoppelter Signatur** |

Stage 3.68E stuft Seismik als H0-Hauptkanal herab: eine reine `r_B~61 nm`-Near-Zone ist nicht direkt global-seismisch aufloesbar. Stage 3.70 soll Seismik nur weiterverfolgen, falls Stage 3.69 eine makroskopische `Delta rho`, `Delta V_P`, `Delta V_S`-Struktur oder koharente Streu-/Normalmodensignatur erzeugt.

## 6. Formation

| Mechanismus | Status |
|---|---|
| In-situ-Kollaps normaler Fe/Ni-Erdmaterie | **FAIL** |
| spaeter direkter Earth-Capture | **FAIL** |
| Proto-Earth-Capture | **FAIL** unter getesteten Bedingungen |
| Planetesimal-Capture | **FAIL** unter getesteten Bedingungen |
| protoplanetarer Gasdrag fuer PBH | **FAIL** als ausreichender Bremsmechanismus |
| Halo -> Protosternwolke -> kalte Scheibe -> SI/Pebble | **FAIL** unter Standardbedingungen |
| bereits cold/co-moving Anfangsbedingung | mathematisch moeglich, Herkunft **OPEN / stark unmotiviert** |

## 7. Stage 3.68E - externes Fachfeedback

Technische Rueckmeldungen aus Numerical Relativity/HPC und globaler Seismologie wurden ohne private Mailtexte in den Modellstand integriert.

| Rueckmeldung | Konsequenz |
|---|---|
| Bondi-Raten benoetigen explizites `c_eff` | PREM-basierter Wert `10.4355 km/s` dokumentiert |
| klassischer Supply muss bei sehr kleiner Horizontskala nicht finale Capture-Rate sein | Quantum/Wave-Capture als Pflichtblock in Stage 3.69 |
| aeussere Newton-/Materialzone + innere GR-Zone ist bei konservativem Matching grundsaetzlich vertretbar | Domain-Decomposition bleibt Stage-3.69-Basisarchitektur |
| globale Waerme ist starker Sanity-Check | 47-TW-Proxy explizit gerechnet; kleiner Michel-Benchmark bleibt darunter |
| Nano-/Mikrometer-Near-Zone nicht direkt seismisch aufloesbar | Seismik nur noch konditional bei makroskopischer Kopplung |

Diese Punkte sind Modellhaertung, keine externe Bestaetigung der H0-Hypothese.

## 8. Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| starke Erd-SL-Variante | FAIL | FAIL |
| kleiner smooth PREM-Branch | kein eigener Ausschluss | kein eigener Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL** | nicht anwendbar |
| Akkretions-/Waermeaudit | H+-gekoppelt | exakte Netto-Rate OPEN; Quantum/Wave-Capture noch ausstehend |
| Seismik/Normalmoden reduziert | kein positiver Nachweis | kein positiver Nachweis; direkter Mikrobereich nicht aufloesbar |
| spaeter Earth-Capture | FAIL | FAIL |
| Standard-Formation/Delivery | stark negativ | stark negativ |
| direkte experimentelle Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## 9. Verbleibende Endstufen

- **Stage 3.69 – High-Fidelity Multiphysics:** `DEFINED / NOT PERFORMED`; jetzt inklusive Quantum/Wave-Capture.
- **Stage 3.70 – Experimental H0 Falsification:** `DEFINED / NOT PERFORMED`; Seismik nur bei makroskopisch gekoppelter Signatur.

Diese Definitionen sind keine bestandenen Tests. Der letzte tatsaechlich bearbeitete interne Teststand bleibt Stage 3.68. Stage 3.68E dokumentiert die Integration externen Fachfeedbacks. Details: [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md) und [`EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`](EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md).

## 10. Konservativer Schluss

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 heutige Existenzhypothese: OPEN / durch bisherige Erdtests nicht ausgeschlossen.
H0 exakte Netto-Akkretionsrate: OPEN; Quantum/Wave-Capture nicht geloest.
H0 fundamentale Begruendung: OPEN.
H0 Formation: stark negativ / kein Standardweg gefunden.
Empirischer Nachweis: keiner.
```
