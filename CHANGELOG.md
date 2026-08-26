# Changelog

Dieses Changelog dokumentiert die oeffentlich sichtbaren Entwicklungsstaende des Erdmoduls.

## V1.5 / Stage 3.68E Feedback-Integration - 26.08.2026

Externes Fachfeedback aus Numerical Relativity/HPC und globaler Seismologie wurde technisch ausgewertet und ohne private Mailtexte in den Modellstand integriert. Dies ist **keine neue experimentelle Validierung** und keine externe Bestaetigung der H0-Hypothese.

### Neue Modellhaertung

- Der fuer Bondi-/Supply-Proxies verwendete zentrale PREM-Sound-Speed wird explizit dokumentiert:

```text
V_P = 11.2622 km/s
V_S = 3.6678 km/s
c_eff = sqrt(V_P^2 - 4/3 V_S^2) = 10.4355 km/s.
```

- Bei `M_BH~1e11 kg` folgt `r_B~61 nm`; `c_eff` ist nur ein aeusserer PREM-/Supply-Proxy.
- Bondi/Michel werden nicht mehr automatisch als finale Horizont-Capture-Rate interpretiert.
- **Quantum/Wave-Capture** wurde als neuer Pflichtblock in Stage 3.69 aufgenommen, weil bei `M~1e11 kg` der Schwarzschildradius `r_s~1.5e-16 m` betraegt und der geometrisch-optische Grenzfall fuer alle Materiekomponenten nicht vorausgesetzt werden darf.
- Die Stage-3.69-Architektur lautet nun:

```text
PREM global
 -> Elastoplastik/Rheologie
 -> Mikro-Hydrodynamik
 -> kinetische GR-Zone
 -> Quantum/Wave-Capture
 -> GR-Horizon-Sink / Capture-Randbedingung.
```

- Ein expliziter globaler Waerme-Sanity-Check gegen `47 +/- 2 TW` wurde hinzugefuegt. Fuer `eta=1` folgt `Mdot_max~1.65e4 kg/year`. Der obere bisherige kleine Michel-Benchmark bei `5e11 kg` liegt bei etwa `115 kg/year` bzw. `0.328 TW`, also rund Faktor `143` darunter. Das liefert keinen globalen Waermeausschluss, ersetzt aber keine lokale Multiphysikrechnung.
- Der Seismikkanal in Stage 3.70 wurde herabgestuft: eine reine Nano-/Mikrometer-Near-Zone ist nicht direkt global-seismisch aufloesbar. 3-D-Full-Wave-Seismik wird nur dann priorisiert, wenn Stage 3.69 eine makroskopisch gekoppelte `Delta rho`, `Delta V_P`, `Delta V_S`-Struktur oder koharente Normalmoden-/Streusignatur erzeugt.
- Neue Datei: `EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`.

### Status bleibt konservativ

```text
H+ Standard-Hawking: FAIL im getesteten Projekt-Reinterpretationsmodell.
H0: OPEN / nicht nachgewiesen.
H0 exakte Netto-Akkretionsrate: OPEN; Quantum/Wave-Capture nicht geloest.
Formation: stark negativ / unaufgeloest.
Stage 3.69: DEFINED / NOT PERFORMED.
Stage 3.70: DEFINED / NOT PERFORMED.
Empirischer Nachweis: keiner.
```

---

## V1.5 / Definition Stage 3.69-3.70 - 25.08.2026

V1.5 aendert den physikalischen Endbefund von Stage 3.68 nicht. Neu ist die formale Definition der zwei verbleibenden Validierungsprotokolle.

- **Stage 3.69 – High-Fidelity Multiphysics:** `DEFINED / NOT PERFORMED`. Verschachtelte PREM/Elastoplastik/Mikro-Hydro/kinetische-GR/GR-Capture-Architektur; explizite QED-/Pair-/Nuklear-Zeitskalen; erster realistischer Meilenstein ist ein reproduzierbarer 1-D/2-D-Multiphysik-Prototyp.
- **Stage 3.70 – Experimental H0 Falsification:** `DEFINED / NOT PERFORMED`. Dedizierter Real-Data-/Likelihood-Test einer erst aus Stage 3.69 abgeleiteten H0-Signatur.
- Die Formulierung `Stages 1-3.68 abgeschlossen` wird vermieden: diese Stages sind **bearbeitet und dokumentiert** und enthalten PASS/kompatibel, OPEN, FAIL sowie Korrekturen.
- H+ bleibt `FAIL` **im Projekt-Reinterpretationstest** des publizierten SK-IV-`anti-nu_e`-Limits; es wird keine offizielle Super-K-Erdzentrum-BH-Exklusion behauptet.
- Es wurde kein Stage-3.69-HPC-Lauf und keine dedizierte H0-Real-Data-Likelihood-Analyse durchgefuehrt.

Neue Dateien:

- `VALIDATION_PROTOCOL_STAGE3_69_70.md`
- `PUBLIC_UPDATE_V1_5.md`

---

## V1.4 / Stage 3.68 - 25.08.2026

Abschluss und Konsolidierung der Stage-3-Haertetestserie.

### Zentrale Aenderungen

- H+ und H0 werden nun strikt getrennt dokumentiert.
- **H+** verwendet Standard-Hawking-Strahlung.
- **H0** setzt als nichtstandardmaessige Gegenhypothese `P_Hawking=0` und ist damit kein Standard-GR/QFT-Zweig.
- Stage 3.28 korrigierte die fruehere Hawking-Normierung; der relevante H+-Bereich verschob sich auf etwa `4.82e11 ... 5.49e11 kg`.
- Stage 3.30 verwendete Greybody-Primaerneutrinos und publizierte spektrumsunabhaengige Super-Kamiokande-Grenzen. Der H+-Projektfluss im Band `25.29-31.29 MeV` liegt ueber dem publizierten SK-IV-90%-CL-Limit. **H+ wird deshalb innerhalb des getesteten Modells als FAIL markiert.**
- Der kleine H0-Branch wurde durch Langzeitakkretion, Festigkeit/Yield, radialen Supply, Rotation, Knudsen-/kinetische Transition, Loss-Cone-Recycling, reduzierten Fokker-Planck/Reservoir-Closure und radiatives/QED-Feedback gehaertet. Keine robuste vollstaendige Akkretionssperre wurde gefunden; die exakte Multiphysik-Rate bleibt OPEN.
- Die physische starke Near Zone wurde von der `~100 m`-Buchhaltungszone getrennt; starke Materialaenderungen liegen im kleinen Branch auf mikro-/nanoskopischen Skalen. Fruehere zu grosse Seismikproxies wurden entsprechend korrigiert.
- Formation wurde separat abgeschlossen: In-situ-Kollaps, spaeter Earth-Capture, Proto-Earth-/Planetesimal-Capture und normale Halo-to-disk Delivery scheitern unter den getesteten Standardbedingungen. Ein extrem cold/co-moving Zustand bleibt nur als unhergeleitete Anfangsbedingung.
- Neuer Endstatus: `FINAL_STATUS_STAGE3_68.md`.
- Neue oeffentliche Kurzfassung: `PUBLIC_UPDATE_V1_4.md`.

### Konservativer Endstatus

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 heutige Existenzhypothese: OPEN / durch bisherige Erdtests nicht ausgeschlossen.
H0 fundamentale Begruendung fuer kein Hawking: OPEN.
H0 Formation: stark negativ / kein Standardweg gefunden.
Empirischer Nachweis: keiner.
```

### Verbleibende Endstufen

- High-Fidelity-Multiphysik/HPC inklusive 3-D-Full-Wave-Seismik.
- Dedizierter experimenteller bzw. Real-Data-Test.

---

## V1.3 / Stage 3.15-3.17 - 25.08.2026

- simultaner Hawking/Michel-Massenscan statt getrennt geschnittener Einzelgrenzen;
- instabiles reduziertes Kompensationsband im damaligen einfachen Hawking/Michel-Modell;
- Hard-Cavity mechanisch verworfen;
- smooth-compensated Branch eingefuehrt;
- erste Smooth-Branch-Seismikproxies dokumentiert.

Diese Zwischenstaende wurden durch V1.4/Stage 3.68 teilweise korrigiert bzw. ueberholt.

---

## V1.3 / Stage 3.14 - 25.08.2026

- Bondi-/Michel-Akkretionsaudit;
- Hochdruck-EOS- und Rheologie-Haertung;
- `~54 r_s`-Toygrenze zurueckgezogen;
- relativistischer Michel-Solver mit analytischem Selfcheck;
- Coulomb-Plastizitaets-Sensitivitaeten;
- hcp-Fe-`8 GPa`-Mikrorettung als Coulomb-Langzeitgrenze zurueckgezogen.

---

## V1.2 / Stage 1.7 - 25.08.2026

- Titel auf **SL/BH-Kernhypothese Erdmodul** vereinheitlicht.
- Layered-PREM-Earth-Closure und fruehe geophysikalische Sensitivitaeten dokumentiert.

---

## V1.0 - 23.08.2026

Erstveroeffentlichung des Erdmoduls.

- archivierte V1.0-PDF bleibt unveraendert als Prioritaets-/Archivnachweis;
- spaetere Forschungsstaende werden nicht rueckwirkend in die Archiv-PDF geschrieben.
