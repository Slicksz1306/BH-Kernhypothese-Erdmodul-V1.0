# Changelog

Dieses Changelog dokumentiert die oeffentlich sichtbaren Entwicklungsstaende des Erdmoduls. Historische Zwischenwerte bleiben als Entwicklungsstand erhalten; spaetere haertere Tests ersetzen nur ihre aktuelle Interpretation.

## V1.5 / Stage 3.69A-4 bis 3.69D/A-8 - 26.08.2026

### A4 – Charged Dirac / Charge Feedback

Der neutrale Earth-speed Protonenlauf wurde um ein Test-Coulombfeld erweitert.

Bei `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
Q=0 e      -> sigma_p ~0.949...0.950 classical
Q=3.67 e   -> sigma_p ~0.889 classical
Q=10 e     -> sigma_p ~0.765 classical
Q=24.18 e  -> sigma_p ~0.517 classical
```

Befund:

```text
charge feedback: relevant
orders-of-magnitude proton stop: not found in tested Q range
charged-electron far-field Coulomb matching: OPEN
```

Neue Dateien:

- `STAGE3_69A4_CHARGED_DIRAC_FEEDBACK.md`
- `stage3_69a4_charged_dirac_feedback.py`

### A5 – Dense Fe/Ni + 0+ Klein-Gordon Capture

Dominante Fe-56/Ni-58-Kerne werden im kohärenten ersten Proxy als massive skalare `0+`-Zustaende behandelt.

Low-alpha KG-Regression: PASS (~0.2%).

Earth-speed bei `M_BH=1e11 kg`:

```text
Fe-56: sigma/sigma_classical ~0.9975
Ni-58: sigma/sigma_classical ~0.9965
```

Damit wird keine starke Composite-Wellenunterdrueckung gefunden.

Dense-screening Referenz:

```text
r_B ~6.13e-8 m
lambda_TF ~2.95e-11 m
r_B/lambda_TF ~2.08e3
```

Eine kleine BH-Nettoladung kann lokal wichtig sein, ist aber im dichten Fe-Proxy kein ungescreenter `r_B`-weiter Supply-Blocker.

Neue Dateien:

- `STAGE3_69A5_DENSE_FENI_CLOSURE.md`
- `stage3_69a5_dense_feni_closure.py`

### A6 – Kinetic Recycling Closure

Die fruehere Idee, eine kleine Einzelpass-Capture-Fraktion direkt als dauerhaften `Mdot`-Suppressionsfaktor zu verwenden, wurde weiter gehaertet.

Fuer Capture `p`, permanenten Escape `e` und sonstiges Recycling gilt exakt:

```text
chi_capture = p/(p+e).
```

Bei `p~8.8e-6` erfordert eine stationaere Gesamtunterdrueckung bis nahe an den Single-pass-Wert, dass fast alle verfehlten Teilchen permanent aus dem lokalen System entfernt werden. Recycling allein liefert daher keine dauerhafte 5-6-OOM-Suppression.

Neue Dateien:

- `STAGE3_69B_A6_KINETIC_RECYCLING_CLOSURE.md`
- `stage3_69b_a6_reduced_closure.py`

### A7 – Collision Regime + Bondi Backpressure

Wichtige Korrektur der Knudsen-Skalierung:

```text
strong-coupling/geometric collisions:
  Kn ~ r^(1/2) -> nach innen kleiner

weak-coupling Coulomb/Spitzer:
  Kn ~ r^(-3/2) -> nach innen groesser
```

Welche Richtung realisiert wird, ist eine Dense-Matter-/Ionisationsfrage.

Ein kontrollierter 1-D-sphaerischer Bondi-Euler-Prototyp reproduziert fuer `Gamma=1.5` die analytische dimensionslose Rate `lambda_B~0.5` auf Prozentniveau.

Ein reflektierender innerer Grenzfall kann Backpressure und einen nach aussen laufenden Schock erzeugen. Die fruehere pauschale Aussage `innerhalb des sonic point -> keine globale Rueckwirkung` wurde deshalb korrigiert.

Neue Dateien:

- `STAGE3_69C_A7_COLLISION_RECYCLING_PDE.md`
- `stage3_69c_a7_collision_recycling_pde.py`

### A8 – Dense Fe / Degeneration / Reaktionszeitskalen

Der adiabatische Reduced Proxy zeigt starke Elektronendegeneration und eine innerwaerts steigende Fermi-Energie. Electron-Capture-Schwellen fuer Ni/Fe koennen energetisch aufgehen, aber die lokale dynamische Transitzeit wird in der inneren Zone extrem kurz.

Daher gilt:

```text
reaction threshold open != reaction equilibrium
instantaneous full neutronization: NOT ESTABLISHED
weak-rate equilibrium before horizon: NOT ESTABLISHED
```

Unter dem getesteten dichten Fe-Proxy bleibt der strong-coupling/degenerate Ast in relevanten Schwellenzonen selbstkonsistenter als ein vorschnell angenommener Spitzer-Weak-Coupling-Ast.

Neue Dateien:

- `STAGE3_69D_A8_DENSE_FE_REACTION_TIMESCALES.md`
- `stage3_69d_a8_dense_fe_reaction_timescales.py`

### Status nach A8

```text
isolierter Protonen-Wellenquerschnitt: stark eingeengt
coherent Fe/Ni-Wellenquerschnitt: stark eingeengt
charge feedback: relevant, aber kein getesteter OOM-Protonenstopper
single-pass suppression as stationary Mdot: nicht selbstkonsistent ohne Escape/Backpressure
Knudsen branch: Dense-Matter-abhaengig
instant neutronization: nicht etabliert
final species-resolved net Mdot_BH: OPEN
Stage 3.69 Full-Multiphysics: OPEN
Stage 3.70: NOT PERFORMED
```

H+ und H0 bleiben parallel:

```text
H+ = mit Standard-Hawking
H0 = ohne Hawking
```

H+ bleibt im getesteten Standard-Hawking/SK-IV-Projekt-Reinterpretationsmodell FAIL; H0 bleibt OPEN / nicht nachgewiesen.

---

## V1.5 / Stage 3.69A-3 Earth-speed Proton Capture + Charge Feedback - 26.08.2026

- flux-stabile Absorptionsauswertung fuer schwache Partialwellen implementiert;
- Earth-speed Protonen-Massenscan `1e10...5e11 kg` berechnet;
- bei `1e11 kg`: `sigma_p~2.1741e-22 m^2 ~0.9503 classical`;
- frueherer Unruh-Protonenwert bleibt historischer Low-E-Benchmark, wird aber am Referenzpunkt durch den vollen Dirac-Matcher ersetzt;
- erste Charge-Kraft-/Gleichgewichtsskalen berechnet;
- H+/H0 weiterhin getrennt.

Neue Dateien:

- `STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md`
- `stage3_69a3_earth_proton_charge.py`

---

## V1.5 / Stage 3.69A-1 Quantum-Capture-Prototyp - 26.08.2026

- Schwarzschild-Dirac-Radialgleichung in Painleve-Gullstrand-Koordinaten implementiert;
- regulaerer Horizon-Branch und konservierter radialer Dirac-Strom implementiert;
- In/Out-Partialwellen-Matching und Matchingradius-Konvergenz getestet;
- qualitative Doran-Struktur und Low-alpha Regression reproduziert;
- Fe-56/Ni-58 Spinstatus auf `0+` korrigiert.

---

## V1.5 / Stage 3.68E Feedback-Integration - 26.08.2026

- externer Numerical-Relativity/HPC- und Seismologie-Input technisch integriert;
- `c_eff=10.4355 km/s` als PREM-Supply-Proxy explizit dokumentiert;
- `r_B~61 nm` bei `1e11 kg`;
- Bondi/Michel nicht mehr automatisch als finale Horizon-Rate interpretiert;
- Quantum/Wave-Capture als Pflichtblock aufgenommen;
- 47-TW-Waerme-Sanity-Check und konditionale Seismikstrategie dokumentiert.

---

## V1.5 / Definition Stage 3.69-3.70 - 25.08.2026

- Stage 3.69 als High-Fidelity-Multiphysik-Closure definiert;
- Stage 3.70 als branch-spezifischer Real-Data-/Falsifikationstest definiert;
- keine abgeschlossene Stage 3.69/3.70 behauptet.

---

## V1.4 / Stage 3.68 - 25.08.2026

- H+ und H0 strikt getrennt;
- H+ Standard-Hawking im getesteten SK-IV-Projekt-Reinterpretationsmodell FAIL;
- kleiner smooth-compensated Erdbranch weitergefuehrt;
- Hard-Cavity und mehrere fruehe Akkretions-/Coulomb-Proxies korrigiert oder verworfen;
- reduzierte Seismik, Langzeit, Loss-Cone und Formation gehaertet;
- Formation unter getesteten Standardwegen stark negativ.

---

## V1.3 / Stage 3.15-3.17 - 25.08.2026

- simultaner Hawking/Michel-Massenscan;
- smooth-compensated Branch eingefuehrt;
- erste Seismik-Haertetests.

---

## V1.3 / Stage 3.14 - 25.08.2026

- Bondi-/Michel-Akkretionsaudit;
- Hochdruck-EOS/Rheologie-Haertung;
- mehrere fruehe Toy-Grenzen zurueckgezogen;
- relativistischer Michel-Solver mit analytischem Selfcheck.

---

## V1.2 / Stage 1.7 - 25.08.2026

- Titel auf **SL/BH-Kernhypothese Erdmodul** vereinheitlicht;
- Layered-PREM-Earth-Closure dokumentiert.

---

## V1.0 - 23.08.2026

Erstveroeffentlichung des Erdmoduls.

- archivierte V1.0-PDF bleibt unveraendert als Prioritaets-/Archivnachweis;
- spaetere Forschungsstaende werden nicht rueckwirkend in die Archiv-PDF geschrieben.
