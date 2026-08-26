# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; Stage 3.69A/3.69A-1 Quantum-Capture-Teilmodul teilweise durchgefuehrt; Stage 3.69 Full-Multiphysics und Stage 3.70 nicht durchgefuehrt  
**Stand:** 26.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Archivhinweis:** `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs- und Prioritätsnachweis erhalten. Die aktuelle Forschungsfassung wird in den Markdown-Dateien dokumentiert.

## Wissenschaftlicher Status in einem Satz

Die SL/BH-Kernhypothese Erdmodul ist ein **theoretischer Forschungsentwurf, kein experimenteller Nachweis**. Der Standard-Hawking-Zweig H+ faellt im aktuellen Projekt-Reinterpretationstest gegen ein publiziertes Super-Kamiokande-`anti-nu_e`-Limit; der nichtstandardmaessige H0-Zweig ohne Hawking-Strahlung wird durch die bisherigen reduzierten Erdtests nicht ausgeschlossen, besitzt aber weder eine positive Detektion noch einen hergeleiteten Standard-Formationweg. Ein Schwarzschild-Dirac-Teilsolver fuer isolierte Spin-1/2-Capture ist inzwischen implementiert und numerisch selbstgeprueft; die exakte H0-Netto-Akkretionsrate in dichter Fe/Ni-Materie bleibt offen.

## Zwei getrennte Hypothesen

### H+ - mit Standard-Hawking

H+ verwendet die uebliche semiklassische Hawking-Strahlung.

Nach der Greybody-/Neutrino-Haertung liegt der relevante Projektbereich bei ungefaehr

```text
M_BH = 4.82e11 ... 5.49e11 kg
T_H  = 21.99 ... 19.31 MeV.
```

Der konservative Projektfluss im SK-IV-Band 25.29-31.29 MeV liegt ueber dem publizierten spektrumsunabhaengigen beobachteten 90%-CL-Grenzwert von `0.04 cm^-2 s^-1 MeV^-1`.

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
```

Dies ist eine **Reinterpretation** eines Super-Kamiokande-Limits, keine offizielle Super-Kamiokande-Erdzentrum-BH-Analyse.

### H0 - ohne Hawking

H0 setzt als nichtstandardmaessige Gegenhypothese

```text
P_Hawking = 0.
```

H0 ist damit kein Standard-GR/QFT-Zweig. Hawking-basierte Neutrino-/Gamma-Grenzen sind fuer H0 definitionsgemaess nicht anwendbar; die fundamentale Begruendung fuer `P_Hawking=0` bleibt offen.

## Aktiver Erdbranch

Die starke Variante mit einem wesentlichen Anteil der Erdmasse im zentralen BH ist verworfen. Der aktive kleine Branch ist **smooth compensated**:

```text
rho_new(r) = rho_PREM(r) - M_BH w(r)
Integral 4 pi r^2 w(r) dr = 1.
```

Eine harte leere Ersatzkugel ist mechanisch verworfen. Drei verschiedene Skalen duerfen nicht verwechselt werden:

```text
r_s = 2 G M_BH / c^2
r_B = G M_BH / c_eff^2
M_PREM(<r_rep) = M_BH.
```

Fuer den zentralen PREM-Supply-Proxy wird nun explizit

```text
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s
      ~ 10.44 km/s
```

mit `V_P=11.2622 km/s` und `V_S=3.6678 km/s` dokumentiert. Bei `M_BH~1e11 kg` folgt `r_B~61 nm`.

## Stand der Erdtests

Fuer den kleinen smooth H0-Zweig liefern die bisher ausgefuehrten reduzierten Tests keinen robusten Ausschluss durch

- Gesamtmasse / `GM`,
- Traegheitsmoment und Rotation,
- smooth PREM-Massenbuchhaltung,
- reduzierte Hydrostatik,
- vereinfachte Seismik/Normalmoden,
- Langzeitwaerme,
- den gestuften Akkretionsaudit aus Festigkeit, Yield, plastischem Supply, Rotation, Knudsen-Uebergang, Loss Cone und radiativem Feedback.

Das bedeutet **Kompatibilitaet innerhalb der getesteten Modelle**, nicht Evidenz fuer ein BH im Erdzentrum.

## Stage 3.68E – externes Fachfeedback integriert

Technische Rueckmeldungen aus Numerical Relativity/HPC und globaler Seismologie wurden am 26.08.2026 ausgewertet und ohne private Mailtexte in den Modellstand integriert.

Die wichtigsten Konsequenzen:

```text
1. c_eff fuer Bondi/Supply explizit dokumentiert: 10.4355 km/s.
2. Bondi/Michel nicht mehr automatisch als finale Horizont-Capture-Rate interpretiert.
3. Quantum/Wave-Capture als Pflichtblock in Stage 3.69 aufgenommen.
4. 47-TW-Waerme-Sanity-Check explizit gerechnet:
   oberer kleiner Michel-Benchmark ~0.328 TW bei eta=1 -> kein globaler Ausschluss.
5. Seismik fuer Stage 3.70 herabgestuft:
   nur aussichtsreich, wenn Stage 3.69 eine makroskopisch gekoppelte Signatur erzeugt.
```

Diese Integration ist **Modellhaertung, keine externe Bestaetigung der Hypothese**.

Details: [`EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`](EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md).

## Stage 3.69A / 3.69A-1 – Quantum/Wave-Capture-Teilmodul

Der zuvor nur definierte Quantum-Capture-Block wurde teilweise umgesetzt.

Aktueller reproduzierbarer Stand:

```text
Schroedinger-Regimecheck: DONE
Schwarzschild-Dirac radial solver: IMPLEMENTED
regular horizon branch: IMPLEMENTED
Dirac-current/Wronskian self-check: PASS numerically
in/out partial-wave matching: IMPLEMENTED
matching-radius convergence: PASS at tested alpha=0.2 benchmark points
full dense-core species-resolved net Mdot: OPEN
```

Fuer `alpha=0.2` liefert der Matching-Test beispielsweise

```text
E/m=1.5: sigma_A/M^2 ~123.259   (klassisch ~128.680)
E/m=2.0: sigma_A/M^2 ~103.965   (klassisch ~103.380)
E/m=5.0: sigma_A/M^2 ~89.682    (klassisch ~87.174)
```

und zeigt die erwartete Annaeherung an den geometrisch-optischen Grenzwert `27*pi ~84.823` bei steigender Energie. Dies ist ein Solver-/Literaturstruktur-Benchmark, kein Erdzentrum-Nachweis.

Am Erd-Referenzpunkt `M_BH=1e11 kg`, `v=10.4355 km/s` liefert die publizierte Unruh-Low-Energy-Naeherung als **isolierten Einzelteilchenbenchmark** ungefaehr

```text
electron sigma ~3.46e-26 m^2
proton   sigma ~6.34e-23 m^2
```

gegenueber einem klassischen collisionless Low-velocity-Benchmark von Groessenordnung `2.29e-22 m^2`.

Wichtig: dominante `Fe-56`- und `Ni-58`-Kerne haben Grundzustandspin `0+`; solange sie kohärent bleiben, ist fuer sie ein skalares/Klein-Gordon-artiges Composite-Capture-Modell statt des Spin-1/2-Dirac-Solvers erforderlich. Unterschiedliche Elektronen-/Ionen-Capture-Raten muessen zudem durch elektrostatisches Ladungsfeedback gekoppelt werden.

Details: [`STAGE3_69A_QUANTUM_WAVE_CAPTURE.md`](STAGE3_69A_QUANTUM_WAVE_CAPTURE.md) und [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md).

## Formation

Formation wurde separat getestet.

```text
In-situ-Kollaps normaler Erdmaterie: FAIL
spaeter direkter Earth-Capture: FAIL
Proto-Earth-/Planetesimal-Standardcapture: FAIL
normaler Halo -> kalte protoplanetare Scheibe: FAIL unter den getesteten Bedingungen
cold/co-moving Anfangsbedingung: mathematisch moeglich, Herkunftsmechanismus nicht hergeleitet
```

Formation ist damit der groesste negative Punkt des H0-Gesamtmodells.

## Endstatus Stage 3.68 / 3.68E / 3.69A-1

| Bereich | H+ Standard-Hawking | H0 ohne Hawking |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleiner smooth Erdbranch | kein eigener Erdstruktur-Ausschluss | kein eigener Erdstruktur-Ausschluss |
| Super-K / Hawking-Neutrinos | **FAIL im Projekt-Reinterpretationstest** | nicht anwendbar |
| Akkretion / Waerme | gekoppelte H+-Probleme | isoliertes Dirac-Capture-Teilmodul teilweise geloest; exakte dichte Netto-Rate OPEN |
| Seismik | kein positiver Nachweis | direkter Mikrobereich nicht aufloesbar; makroskopische Kopplung OPEN |
| spaetere Earth-Capture-Formation | FAIL | FAIL |
| Standard-Formation/Delivery | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| positive eindeutige Signatur | keine | keine |

**Konservatives Fazit:**

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 als heutige versteckte Zentralmasse: OPEN / durch bisherige Erdtests nicht ausgeschlossen.
H0 isolierte Spin-1/2-Wave-Capture: numerisch teilweise geloest/benchmarkiert.
H0 exakte Dense-Matter-Netto-Akkretionsrate: OPEN.
H0 fundamentale Begruendung fuer kein Hawking: OPEN.
H0 Formation: stark negativ / kein Standardweg gefunden.
Empirischer Nachweis: keiner.
```

## Verbleibende Validierungsprotokolle

Die zwei Endstufen bleiben als Gesamtstufen offen:

1. **Stage 3.69 – High-Fidelity Multiphysics:** Full-Stack **nicht durchgefuehrt**. Ein Teilmodul (`3.69A/3.69A-1`, Quantum/Dirac-Capture) ist inzwischen teilweise implementiert und getestet. Offen bleiben insbesondere Dense-Matter-Komposition, coherent Fe/Ni scalar/composite capture, Ladungsfeedback, Transport und die selbstkonsistente Netto-`Mdot`-Closure.
2. **Stage 3.70 – Experimental H0 Falsification:** **nicht durchgefuehrt**; dedizierter Real-Data-/Likelihood-Test einer erst aus dem vollstaendigen Stage-3.69-Output abgeleiteten Signatur.

Details: [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md).

## Dateien

- [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md) - Stage 3.69/3.70 Gesamtprotokolle.
- [`STAGE3_69A_QUANTUM_WAVE_CAPTURE.md`](STAGE3_69A_QUANTUM_WAVE_CAPTURE.md) - Regimeklassifikation fuer Quantum/Wave-Capture.
- [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md) - Schwarzschild-Dirac-Teilsolver und Matching-Benchmarks.
- [`stage3_69a_quantum_capture_regime.py`](stage3_69a_quantum_capture_regime.py) - reproduzierbarer Regimecheck.
- [`stage3_69a1_dirac_prototype.py`](stage3_69a1_dirac_prototype.py) - reproduzierbarer Dirac-/Matching-Prototyp.
- [`EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`](EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md) - technische Integration externen Fachfeedbacks.
- [`FINAL_STATUS_STAGE3_68.md`](FINAL_STATUS_STAGE3_68.md) - Endmatrix der internen Stages bis 3.68.
- [`PUBLIC_UPDATE_V1_5.md`](PUBLIC_UPDATE_V1_5.md) - Definition der verbleibenden Endtests.
- [`PUBLIC_UPDATE_V1_4.md`](PUBLIC_UPDATE_V1_4.md) - Abschlusszusammenfassung Stage 3.68.
- [`THEORIE.md`](THEORIE.md) - aktueller Theorierahmen.
- [`TEST_STATUS.md`](TEST_STATUS.md) - Test- und Falsifikationsmatrix.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) - numerischer Status und Aussagegrenzen.
- [`AKKRETION_STATUS.md`](AKKRETION_STATUS.md) - Akkretions-/Langzeitstatus.
- [`MASSENSCAN_STAGE3_15.md`](MASSENSCAN_STAGE3_15.md) - historischer Stage-3.15-Massenscan.
- [`SEISMIK_STAGE3_16_17.md`](SEISMIK_STAGE3_16_17.md) - historischer Seismik-Haertetest.
- [`CHANGELOG.md`](CHANGELOG.md) - Korrektur- und Versionshistorie.
- [`CITATION.cff`](CITATION.cff) - Zitiermetadaten.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` - unveraenderte Erstveroeffentlichung.

## Literatur-Kernreferenzen

- Dziewonski, A. M. & Anderson, D. L. (1981), *Preliminary Reference Earth Model*.
- Davies, J. H. & Davies, D. R. (2010), *Earth's surface heat flux*, `47 +/- 2 TW`.
- Doran, C., Lasenby, A., Dolan, S. & Hinder, I. (2005), *Fermion absorption cross section of a Schwarzschild black hole*, arXiv:gr-qc/0503019.
- Dolan, S., Doran, C. & Lasenby, A. (2006), *Fermion scattering by a Schwarzschild black hole*, arXiv:gr-qc/0605031.
- Super-Kamiokande Collaboration, arXiv:2305.05135, Tabelle 2.
- Arbey & Auffinger, BlackHawk, arXiv:1905.04268; BlackHawk v3.0, arXiv:2606.06355.
- Cantiello et al. (2026), *Accretion of Primordial Black Holes in Stellar Interiors*, arXiv:2606.02726.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; Stages 1-3.68 bearbeitet und dokumentiert, Stage 3.68E externes Fachfeedback integriert, Stage 3.69A/3.69A-1 als Quantum-Capture-Teilmodul teilweise durchgefuehrt, Stage 3.69 Full-Multiphysics und Stage 3.70 nicht durchgefuehrt, Rheinland-Pfalz, Deutschland.
