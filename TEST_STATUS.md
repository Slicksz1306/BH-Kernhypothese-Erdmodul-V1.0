# SL/BH-Kernhypothese Erdmodul - Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 25.08.2026  
**Theorie-Textstand:** Erdmodul V1.4  
**Aktueller Forschungsstand:** Stage 3.68

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
| Erdalter-Masse/Waerme im kleinen Branch | kein Ausschluss in den reduzierten Stressproxies |

## 5. Erdstruktur / Seismik

| Test | kleiner smooth H0-Branch |
|---|---|
| Gesamtmasse / `GM` | kompatibel durch redistributive Buchhaltung |
| Traegheitsmoment / Rotation | Effekt im kleinen Branch extrem klein |
| reduzierte Hydrostatik | kein Ausschluss |
| starke gesamte `r_rep`-Zone | frueherer Proxy **korrigiert**; physische starke Zone liegt viel tiefer |
| Body-wave Timing Proxy | kein messbarer robuster Ausschluss |
| Normalmodenproxy | kein messbarer robuster Ausschluss |
| echte 3-D-Full-Wave-Likelihood | **nicht durchgefuehrt** |

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

## 7. Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| starke Erd-SL-Variante | FAIL | FAIL |
| kleiner smooth PREM-Branch | kein eigener Ausschluss | kein eigener Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL** | nicht anwendbar |
| Akkretions-/Waermeaudit | H+-gekoppelt | exakte Rate OPEN; kein kleiner-Branch-Ausschluss |
| Seismik/Normalmoden reduziert | kein positiver Nachweis | kein positiver Nachweis |
| spaeter Earth-Capture | FAIL | FAIL |
| Standard-Formation/Delivery | stark negativ | stark negativ |
| direkte experimentelle Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## 8. Verbleibende Endstufen

1. High-Fidelity-Multiphysik/HPC inklusive echter 3-D-Full-Wave-Seismik.
2. Dedizierter experimenteller bzw. Real-Data-Test.

## 9. Konservativer Schluss

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 heutige Existenzhypothese: OPEN / durch bisherige Erdtests nicht ausgeschlossen.
H0 fundamentale Begruendung: OPEN.
H0 Formation: stark negativ / kein Standardweg gefunden.
Empirischer Nachweis: keiner.
```
