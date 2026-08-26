# Stage 3.69 / 3.70 – verbleibende Validierungsprotokolle

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Gesamtstatus:** Stage 3.69 Full-Multiphysics OPEN; Teilmodule bis A8 numerisch bearbeitet; Stage 3.70 NOT PERFORMED

## Branches

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben parallel. Gemeinsame Materie-/Capture-Module gelten fuer beide; H+ besitzt zusaetzliche Hawking-Quell-/Emissionskanaele.

## Stage 3.69 – High-Fidelity Multiphysics

Ziel ist eine selbstkonsistente Verbindung

```text
PREM/global supply
 -> Rheologie / Dense Fe-Ni EOS
 -> collisional transport
 -> kinetic/recycling transition
 -> species/composition closure
 -> wave capture
 -> charge feedback
 -> nuclear/reaction timescales
 -> horizon sink
 -> net Mdot_BH(t), Q(t)
```

### Bereits bearbeitete Teilmodule

#### A1 – Schwarzschild-Dirac

- massiver Schwarzschild-Dirac-Radialsolver: IMPLEMENTED
- regular horizon branch: IMPLEMENTED
- current/Wronskian self-check: PASS
- in/out partial-wave matching: IMPLEMENTED
- low-alpha externe Regression: PASS
- intermediate-alpha Doran-Struktur: PASS qualitativ/numerisch

#### A3 – Earth-speed Protonen-Capture

Bei `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
sigma_p ~2.1741e-22 m^2
sigma_p/sigma_classical ~0.9503
```

Keine starke Protonen-Wellenunterdrueckung an diesem Referenzpunkt.

#### A4 – Charged Proton Dirac + Charge Feedback

Schwarzschild + Test-Coulombfeld als kontrollierter erster charged-capture Proxy.

Bei `M_BH=1e11 kg`:

```text
Q=0 e      -> sigma_p ~0.949...0.950 classical
Q=3.67 e   -> sigma_p ~0.889 classical
Q=10 e     -> sigma_p ~0.765 classical
Q=24.18 e  -> sigma_p ~0.517 classical
```

Interpretation:

```text
charge feedback: relevant
orders-of-magnitude proton stop: not found in tested Q range
charged electron far-field Coulomb matching: OPEN
```

#### A5 – Fe/Ni 0+ Composite Wave Capture

Fe-56 und Ni-58 werden im kohärenten ersten Proxy als massive skalare/Klein-Gordon-Zustaende behandelt.

Bei `M_BH=1e11 kg`, `v=10.4355 km/s`:

```text
Fe-56: sigma/sigma_classical ~0.9975
Ni-58: sigma/sigma_classical ~0.9965
```

Damit wird auch fuer ganze dominante 0+-Kerne keine starke Wellenunterdrueckung gefunden.

Dense-screening Proxy:

```text
r_B ~6.13e-8 m
lambda_TF ~2.95e-11 m
r_B/lambda_TF ~2.08e3
```

Eine nackte Zentralcharge ist damit kein ungescreenter `r_B`-weiter Supply-Blocker.

#### A6 – Reduced Recycling Closure

Die naive Identifikation

```text
small single-pass capture fraction -> equally small stationary Mdot
```

ist nicht selbstkonsistent, wenn nicht eingefangene Teilchen lokal verbleiben und erneut gestreut/rethermalisiert werden.

Bei wiederholten Encounter-Zyklen mit Einzelpass-Capture `p` und permanentem Escape `e` gilt

```text
chi_capture = p / (p + e).
```

Mit `p~8.8e-6` ist eine stationaere Gesamtunterdrueckung bis fast auf `p` nur moeglich, wenn fast alle verfehlten Teilchen permanent entkommen.

#### A7 – Collision-Regime + 1-D Bondi Backpressure

Wichtige Korrektur zu frueheren Knudsen-Proxies:

```text
strong-coupling / roughly geometric collisions:
  lambda_mfp ~ rho^-1 ~ r^(3/2)
  Kn ~ lambda/r ~ r^(1/2)
  -> Kn decreases inward

weak-coupling Coulomb / Spitzer-like:
  lambda_C ~ T^2/n ~ r^(-1/2)
  Kn ~ r^(-3/2)
  -> Kn increases inward
```

Welche Richtung realisiert wird, ist eine Dense-Matter-/Ionisationsfrage und darf nicht vorweggenommen werden.

Kontrollierter 1-D-sphaerischer Bondi-Euler-Benchmark (`Gamma=1.5`): numerische dimensionslose Akkretionsrate reproduziert den analytischen transsonischen Wert `lambda_B~0.5` auf Prozentniveau.

Ein reflektierender innerer Grenzfall baut Backpressure auf und kann einen Schock nach aussen schicken. Daher ist die fruehere pauschale Aussage `innerhalb sonic point -> keine Rueckwirkung` korrigiert: fuer kleine lineare Stoerungen gilt sonic shielding, langfristige Akkumulation kann aber global rueckwirken.

#### A8 – Dense Fe Regime + Electron-Capture Timescales

Adiabatischer Reduced Proxy ab `r_B`:

```text
rho ~ r^(-3/2)
T ~ r^(-1)
E_F grows strongly inward
```

Elektronendegeneration bleibt stark; relativistische Degeneration setzt im Reduced Proxy tief innerhalb `r_B` ein.

Energetische Electron-Capture-Kanaele fuer Ni/Fe koennen in der inneren Zone aufgehen. Aber:

```text
reaction threshold open != reaction equilibrium
```

Publizierte starke stellar-nukleare EC-Raten liegen selbst bei viel hoeheren Dichten/Temperaturen viele Groessenordnungen langsamer als die lokale dynamische Transitzeit des aktuellen inneren Reduced Proxy.

Daraus folgt fuer Stage 3.69:

```text
instantaneous full neutronization before horizon: NOT ESTABLISHED
weak-rate equilibrium: NOT ESTABLISHED
strong-coupling / degenerate transport remains plausible in reduced map
```

## Aktuelle entscheidende Unbekannte

Der isolierte Wellenquerschnitt ist nicht mehr der Hauptunsicherheitsfaktor. Entscheidend ist nun

```text
Dense Fe/Ni EOS + ionization/coupling
 -> Knudsen branch
 -> recycling versus permanent escape/backpressure
 -> charge-state redistribution
 -> reaction/composition timescales
 -> chi_transport
 -> net Mdot_BH
```

## Mindest-Meilenstein fuer Abschluss von Stage 3.69

Ein gekoppelter 1-D/2-D-Prototyp muss mindestens liefern:

```text
Mdot_BH(t)
Q(t)
rho(r,t), T(r,t), Ye(r,t)
charge-state / composition fractions
transport/recycling efficiency chi_transport
energy deposition / escaping luminosity
branch-specific observables
```

Bis dahin bleibt

```text
Stage 3.69 Full-Multiphysics: OPEN
final species-resolved net Mdot_BH: OPEN
```

## Stage 3.70 – Experimental branch-specific falsification

**Status:** DEFINED / NOT PERFORMED

Stage 3.70 beginnt erst mit quantitativen Stage-3.69-Endvorhersagen.

Moegliche Kanaele:

1. H+ Hawking-spezifisch: Neutrino-/Gamma-Spektren.
2. H+/H0 gemeinsame Materiesignaturen: Waerme, Rotation/Magnetfeld, Transportprodukte.
3. 3-D-Seismik nur bei makroskopisch gekoppelter Struktur.
4. Materieprozess-Neutrinos nur nach species-/reaction-resolved Vorhersage.

## Konservativer Projektstatus

```text
H+ Standard-Hawking:
    FAIL im getesteten SK-IV-Projekt-Reinterpretationsmodell;
    Branch bleibt separat dokumentiert.

H0:
    OPEN / nicht nachgewiesen.

A1/A3/A4/A5:
    wave/capture Teilprobleme deutlich eingeengt.

A6/A7/A8:
    transport/recycling/coupling/reaction closure deutlich eingeengt;
    mehrere fruehere pauschale Suppressionsannahmen korrigiert.

Formation:
    stark negativ / kein Standardweg hergeleitet.

Empirischer Nachweis eines Erdzentrum-BH:
    keiner.
```

## Reproduzierbare aktuelle Stage-Dateien

- `STAGE3_69A4_CHARGED_DIRAC_FEEDBACK.md`
- `stage3_69a4_charged_dirac_feedback.py`
- `STAGE3_69A5_DENSE_FENI_CLOSURE.md`
- `stage3_69a5_dense_feni_closure.py`
- `STAGE3_69B_A6_KINETIC_RECYCLING_CLOSURE.md`
- `stage3_69b_a6_reduced_closure.py`
- `STAGE3_69C_A7_COLLISION_RECYCLING_PDE.md`
- `stage3_69c_a7_collision_recycling_pde.py`
- `STAGE3_69D_A8_WDM_WEAK_TIMESCALES.md`
- `stage3_69d_a8_wdm_weak_timescales.py`
