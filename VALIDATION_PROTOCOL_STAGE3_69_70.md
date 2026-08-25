# Stage 3.69 / 3.70 – verbleibende Validierungsprotokolle

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 25.08.2026  
**Status:** DEFINED / NOT PERFORMED

Diese Datei definiert die zwei verbleibenden Endtests. Sie dokumentiert **keinen durchgefuehrten HPC-Lauf und keine dedizierte H0-Real-Data-Likelihood-Analyse**.

## Stage 3.69 – High-Fidelity Multiphysics

**Status:** DEFINED / NOT PERFORMED  
**Typ:** Validierungsprotokoll

### Ziel

Ein reproduzierbarer Multiphysik-Stack fuer einen kleinen H0-BH-Zweig um `M_BH ~ 1e11 kg`, der die bisher nur getrennt geprueften Regime selbstkonsistent koppelt und daraus quantitative Signaturen fuer Stage 3.70 erzeugt.

### Verschachtelte Architektur

Ein einziges 3-D-Gitter vom Erdradius bis zur Bondi- oder Horizontskala ist wegen der extremen Skalenhierarchie nicht sinnvoll. Fuer `M_BH~1e11 kg` gilt grob

```text
r_B ~ 60 nm
r_s ~ 1.5e-16 m
R_Earth/r_B ~ 1e14
r_B/r_s ~ 4e8.
```

Daher:

```text
PREM global
 -> Elastoplastik/Rheologie
 -> Mikro-Hydrodynamik
 -> kinetische GR-Zone
 -> GR-Capture-Randbedingung.
```

Der Horizont wird nicht direkt bis auf `r_s` aufgeloest, sondern durch eine horizon-konsistente Excision-, Absorbing-Boundary- oder Subgrid-Capture-Behandlung vertreten.

### Physikalische Mindestmodule

1. **Innere GR-Hydro/Kinetik:** `nabla_mu T^{mu nu}=Q^nu` auf Schwarzschild-Hintergrund; Newton-Hydro wird nicht bis zum Horizont extrapoliert.
2. **Aeussere Elastoplastik:** gekoppelte Impuls-/Spannungsgleichungen fuer dichte Fe/Ni-Materie.
3. **Dense-Matter-EOS:** `p(rho,T,Y_e,...)`, Energie, Kompressibilitaet, Scher-/Yield-Eigenschaften und relevante Phasenwechsel.
4. **Transport:** Waermeleitung, Diffusion/Konvektion, Elektron-Ion-Kopplung und Strahlungstransport.
5. **QED/Nuklear:** Bremsstrahlung, Compton, Pair-Prozesse und Nuklearreaktionen nur nach explizitem Zeitskalencheck.
6. **Loss Cone / Recycling:** kinetische Winkelimpulsdiffusion, Geodaeten und Capture-Raten.
7. **Aeussere Seismik:** Export eines selbstkonsistenten `rho(r), Vp(r), Vs(r)` bzw. 3-D-Materialmodells fuer Full-Wave-Seismik, z. B. SPECFEM3D_GLOBE oder vergleichbar.

### Keine automatische MeV-Equilibrierung

Eine viriale Ionenskala `kT_i ~ MeV` impliziert nicht automatisch

```text
T_i = T_e = T_gamma.
```

Explizit zu vergleichen sind

```text
t_reaction, t_ei, t_gamma-e, t_pair, t_nuc
```

gegen Advektions-/Residenzzeiten. Pair-Equilibrierung erfordert mindestens `t_pair << t_adv` zusammen mit ausreichender Wechselwirkungs-/optischer Tiefe und schneller Energieumverteilung.

### Numerik und Validierung

- AMR oder verschachtelte Domain-Decomposition,
- MPI/GPU-HPC nach Bedarf,
- Konvergenz- und Erhaltungstests,
- Benchmarks gegen PREM-Hydrostatik, Bondi, Michel und vereinfachte GR-Hydro-Testfaelle,
- dokumentierte Sensitivitaet gegen EOS-, Transport- und Randbedingungsvarianten.

### Mindest-Meilenstein vor 3-D-HPC

```text
reproduzierbarer 1-D/2-D Multiphysik-Prototyp
```

Dieser muss mindestens liefern:

- eine stabile oder zeitabhaengige `Mdot(t)`,
- ein selbstkonsistentes Near-Zone-Profil,
- eine quantitative beobachtbare Signatur bzw. belastbare obere Grenze.

## Stage 3.70 – Experimental H0 Falsification

**Status:** DEFINED / NOT PERFORMED  
**Typ:** Validierungsprotokoll

### Voraussetzung

Stage 3.70 beginnt erst, wenn Stage 3.69 quantitative Vorhersagen liefert, z. B.

```text
Delta t_seismic(M_BH),
dPhi_nu_alpha/dE,
Delta Omega(t),
Delta B(t).
```

### Signaturkanaele

1. **3-D-Full-Wave-Seismik:** PREM gegen PREM+BH-Output aus Stage 3.69 in globalen Seismogrammen/Normalmoden.
2. **Flavor-spezifische Neutrinos:** zuerst `dPhi_nu_e/dE`, `dPhi_anti-nu_e/dE`, `dPhi_nu_mu/dE`, `dPhi_nu_tau/dE`; danach Auswahl des passenden Detektors und Energiekanals.
3. **Rotation/Magnetfeld:** nur falls Stage 3.69 nichtvernachlaessigbare Torques oder magnetohydrodynamische Kopplungen vorhersagt.

SK-Gd, JUNO, DUNE und IceCube/Upgrade werden nicht als austauschbare Detektoren behandelt; Flavor, Energie, Reaktionskanal, Richtung und Hintergrund muessen zum vorhergesagten Spektrum passen.

Stage 3.54 deutet im bisherigen schnellen-Flow-Proxy auf sehr kleine Akkretions-Neutrinofluesse fuer H0 hin; das ist keine Stage-3.70-Detektorvorhersage und muss durch Stage 3.69 neu bestimmt werden.

### Formale Statistik

Der primaere Vergleich soll als Likelihood-/Profile-Likelihood-Problem formuliert werden:

```text
L(D | H0, theta, eta)
```

mit physikalischen Parametern `theta` und Mess-/Hintergrund-Nuisanceparametern `eta`.

Schematisch:

```text
q = -2 ln [ max_(theta,eta) L(D|H0,theta,eta)
            / max_eta L(D|H_ref,eta) ].
```

Eine Widerlegung des gesamten definierten H0-Parameterraums darf erst behauptet werden, wenn **kein zulaessiger H0-Parameterpunkt** mehr mit den Daten vereinbar ist und Look-elsewhere-, Systematik- und Modellunsicherheiten angemessen behandelt wurden.

## Offizielle Endmatrix V1.5

```text
Stages 1-3.68:
    bearbeitet und dokumentiert; enthalten PASS/kompatibel, OPEN, FAIL und Korrekturen.

Stage 3.69:
    High-Fidelity Multiphysics – DEFINED / NOT PERFORMED.

Stage 3.70:
    Experimental H0 Falsification – DEFINED / NOT PERFORMED.

H+:
    FAIL im getesteten Standard-Hawking/SK-IV-Projekt-Reinterpretationsmodell.

H0:
    OPEN / nicht nachgewiesen.

Formation:
    stark negativ / unaufgeloest.

Positive H0-Signatur:
    keine nachgewiesen.
```

Der letzte tatsaechlich bearbeitete Teststand bleibt Stage 3.68. V1.5 fuegt die beiden verbleibenden Validierungsprotokolle hinzu; sie werden nicht als durchgefuehrte Stages gezaehlt.
