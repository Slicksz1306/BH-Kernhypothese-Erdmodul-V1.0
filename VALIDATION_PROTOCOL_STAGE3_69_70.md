# Stage 3.69 / 3.70 – verbleibende Validierungsprotokolle

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Gesamtstatus:** Stage 3.69 Full-Multiphysics NOT PERFORMED; Stage 3.69A/3.69A-1 und Stage 3.69A-3 Quantum/Wave-Capture-Teilmodule numerisch bearbeitet; Stage 3.70 NOT PERFORMED

Diese Datei definiert die verbleibenden Endtests. Es wurde **kein vollstaendiger Stage-3.69-Multiphysik/HPC-Lauf und keine dedizierte Stage-3.70-Real-Data-Likelihood-Analyse** durchgefuehrt.

Projektbranches:

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben parallel. Gemeinsame Materie-/Capture-Module werden fuer beide gerechnet; H+ besitzt zusaetzliche Hawking-Quell-/Emissionskanaele.

## Stage 3.69 – High-Fidelity Multiphysics

**Gesamtstatus:** FULL STACK NOT PERFORMED  
**Teilstatus:** `3.69A/3.69A-1` und `3.69A-3` numerisch bearbeitet  
**Typ:** Validierungsprotokoll

### Ziel

Ein reproduzierbarer Multiphysik-Stack fuer den kleinen smooth BH-Branch um `M_BH ~1e10...5e11 kg`, der die bisher getrennt geprueften Regime selbstkonsistent koppelt und quantitative branch-spezifische Signaturen fuer Stage 3.70 erzeugt.

### PREM-basierter aeusserer Supply-Proxy

```text
rho_c = 13.0885 g/cm^3
V_P   = 11.2622 km/s
V_S   = 3.6678 km/s
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s.
```

Bei `M_BH~1e11 kg` folgt `r_B~61 nm`. `c_eff` ist ein aeusserer PREM-/Supply-Proxy und keine mikroskopische Protonen-/Elektronendispersionsrelation.

### Verschachtelte Architektur

```text
PREM global
 -> Elastoplastik/Rheologie
 -> Mikro-Hydrodynamik
 -> kinetische GR-Zone
 -> species/composition closure
 -> Quantum/Wave-Capture
 -> charge/nuclear feedback
 -> GR-Horizon-Sink
 -> branch-specific Hawking terms for H+ only.
```

### Physikalische Mindestmodule

1. **Innere GR-Hydro/Kinetik:** `nabla_mu T^{mu nu}=Q^nu` auf praktisch Schwarzschild-Hintergrund; RN-Kontrollrechnung falls noetig.
2. **Aeussere Elastoplastik:** dichte Fe/Ni-Materie.
3. **Dense-Matter-EOS:** `p(rho,T,Y_e,...)`, Energie, Kompressibilitaet, Yield/Phase.
4. **Transport:** Waermeleitung, Diffusion/Konvektion, Elektron-Ion-Kopplung, Strahlung.
5. **QED/Nuklear:** Bremsstrahlung, Compton, Pair- und Nuklearprozesse nach Zeitskalencheck.
6. **Loss Cone / Recycling:** Winkelimpulsdiffusion, Geodaeten, Capture.
7. **Quantum/Wave-Capture:** spin-/energie-/ladungs-/kompositionsabhaengige Absorptionsquerschnitte.
8. **Charge feedback:** `sigma_p,e(Q)` und selbstkonsistentes `Q(t)`.
9. **Composite nuclei:** dominante `Fe-56`/`Ni-58`-Kerne haben `0+`; solange kohärent, scalar/Klein-Gordon-artige Composite-Capture statt Spin-1/2-Dirac.
10. **Nuclear state transition:** bei Dissociation/Neutronisierung Umschaltung auf Nukleonen-/Elektronenkanäle.
11. **H+ only:** Hawking-Emission, Greybody-Spektren, branch-spezifische Energie-/Ladungsquellen.
12. **Aeussere Seismik:** nur falls die gekoppelte Loesung eine makroskopisch relevante Stoerung erzeugt.

## Stage 3.69A / 3.69A-1 – bereits bearbeitet

```text
Schroedinger-Regimecheck: DONE
Schwarzschild-Dirac radial solver: IMPLEMENTED
regular horizon branch: IMPLEMENTED
current/Wronskian self-check: PASS numerically
in/out partial-wave matching: IMPLEMENTED
matching-radius convergence: PASS at tested benchmark points
low-alpha external regression: PASS
intermediate-alpha Doran structure: PASS qualitatively/numerically
```

Benchmark `alpha=0.2`:

```text
E/m=1.5: sigma_A/M^2 ~123.259 ; classical ~128.680
E/m=2.0: sigma_A/M^2 ~103.965 ; classical ~103.380
E/m=5.0: sigma_A/M^2 ~89.682  ; classical ~87.174
geometric-optics target: 27*pi ~84.823
```

Ein vollstaendiger datenpunktgenauer Regressionstest gegen eine digitalisierte Publikationskurve bleibt offen.

## Stage 3.69A-3 – Earth-speed Proton Dirac Capture

Referenz:

```text
v = 10.4355 km/s
u = 3.4809081e-5.
```

Fuer schwach absorbierte Partialwellen wird die Absorption zusaetzlich flux-stabil aus

```text
P_abs = (-W_H)/(2 q |A_in|^2)
q = p/(E+m), W_H=-1
```

bestimmt, um Catastrophic Cancellation in `1-|S|^2` zu vermeiden.

### Protonen-Massenscan

| `M_BH` | `alpha_p` | `kmax` | `x_match` | `sigma_D/sigma_classical` | `sigma_D` [m^2] |
|---:|---:|---:|---:|---:|---:|
| `1e10 kg` | `0.0353107` | 3 | `5e6` | `0.0326735` | `7.47496e-26` |
| `1e11 kg` | `0.353107` | 3 | `5e6` | `0.950295` | `2.17406e-22` |
| `2e11 kg` | `0.706215` | 5 | `2e6` | `1.008071` | `9.22496e-22` |
| `5e11 kg` | `1.76554` | 9 | `1e6` | `0.996621` | `5.70011e-21` |

Partialwellen-Konvergenz beim oberen Punkt:

```text
kmax=5 -> 0.6015 classical
kmax=6 -> 0.8420
kmax=7 -> 0.99630
kmax=8 -> 0.99662110
kmax=9 -> 0.99662113.
```

Matchingradius-Spotcheck `M=1e11 kg`:

```text
x_match=1e6 -> 0.95024543 classical
x_match=5e6 -> 0.95029487 classical
x_match=1e7 -> 0.95035969 classical.
```

### Konsequenz fuer die fruehere Unruh-Protonennaeherung

Frueherer analytischer Benchmark bei `M=1e11 kg`:

```text
sigma_Unruh,p ~6.3447e-23 m^2.
```

Voller Dirac-Matcher:

```text
sigma_Dirac,p ~2.1741e-22 m^2
             ~0.9503 sigma_classical.
```

Die Unruh-Naeherung bleibt als Low-E-/Low-Coupling-Benchmark erhalten, wird bei `alpha_p~0.353` aber nicht mehr als finale Earth-speed Protonen-Cross-Section verwendet.

## Stage 3.69A-3 – Charge-Feedback-Skalen

Bei `M_BH=1e11 kg` und `|Q|=e`:

```text
|F_C/F_G| proton   = 0.0206661
|F_C/F_G| electron = 37.9461.
```

Klassische Fernfeld-Kraftgrenzen:

```text
Q_max,p   = +48.3884 e = 7.75268e-18 C
|Q_max,e| =   0.026353 e = 4.22224e-21 C.
```

Stationaerer Equal-T-Plasma-Benchmark nach Zajacek et al.:

```text
Q_eq ~ +24.1810 e = 3.87423e-18 C.
```

RN-Extremalladungsskala:

```text
Q_extremal ~8.6175 C
Q_eq/Q_extremal ~4.50e-19.
```

Damit kann Ladungsfeedback die Dynamik geladener Teilchen schon bei winziger Nettoladung stark veraendern, waehrend die Raumzeitmetrikkorrektur praktisch vernachlaessigbar bleibt.

**Aussagegrenze:** Die Charge-Werte sind Referenzskalen, keine selbstkonsistente Erdkerngleichgewichtsloesung. Dense Fe/Ni-Screening, Kollisionen, Degeneration, Ionisation, Komposition und Transport bleiben offen.

Details:

- [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md)
- [`STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md`](STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md)
- [`stage3_69a3_earth_proton_charge.py`](stage3_69a3_earth_proton_charge.py)

## Naechster Teilblock: Stage 3.69A-4

```text
charged Dirac capture + self-consistent Q(t)
```

Schematisch:

```text
dQ/dt = e [Gamma_p(Q)-Gamma_e(Q)] + branch-specific source/sink terms
Mdot_BH = sum_i m_i Gamma_i(Q) + composite/nuclear channels.
```

Erst danach kann die Charge-Dynamik an dichte Fe/Ni-Materie und Transport gekoppelt werden.

## Keine automatische MeV-Equilibrierung

Eine viriale Ionenskala `kT_i~MeV` impliziert nicht automatisch `T_i=T_e=T_gamma`. Zu vergleichen sind `t_reaction`, `t_ei`, `t_gamma-e`, `t_pair`, `t_nuc` gegen Advektions-/Residenzzeiten.

## Globaler Waerme-Sanity-Check

Mit `P_Earth~47+/-2 TW` und `P_heat=eta Mdot c^2` folgt bei `eta=1`

```text
Mdot_max ~5.23e-4 kg/s ~1.65e4 kg/year.
```

Der obere bisherige kleine Michel-Benchmark bei `5e11 kg` (`~3.65e-6 kg/s`) entspraeche bei `eta=1` etwa `0.328 TW` bzw. `115 kg/year`. Das ist nur ein globaler Sanity-Check.

## Mindest-Meilenstein vor 3-D-HPC

Der Full-Stack-1-D/2-D-Prototyp muss mindestens liefern:

- `Mdot(t)`,
- `Q(t)`,
- selbstkonsistentes Near-Zone-Profil,
- Netto-Capture nach Supply + Kinetik + species-resolved Wave-Capture + Charge/Nuclear closure,
- branch-spezifische quantitative beobachtbare Signatur oder obere Grenze.

Dieser **Full-Stack-Meilenstein ist noch nicht erreicht**.

## Stage 3.70 – Experimental branch-specific falsification

**Status:** DEFINED / NOT PERFORMED

Stage 3.70 beginnt erst, wenn Stage 3.69 quantitative Endvorhersagen liefert.

### Signaturkanaele

1. **H+ Hawking-spezifisch:** Neutrino-/Gamma-Spektren und weitere branch-spezifische Emissionen.
2. **H0/H+ gemeinsame Materiesignaturen:** Waerme, Rotation/Magnetfeld, ggf. Material-/Transporteffekte.
3. **3-D-Full-Wave-Seismik – konditional:** nur bei makroskopisch gekoppelter Struktur.
4. **Flavor-spezifische Neutrinos aus Materieprozessen:** Detektorwahl nach Flavor/Energie/Reaktionskanal.

### Statistik

```text
L(D | H_branch, theta, eta)
q = -2 ln [ max_(theta,eta) L(D|H_branch,theta,eta)
            / max_eta L(D|H_ref,eta) ].
```

Ein Gesamtparameterraum darf nur ausgeschlossen werden, wenn kein zulaessiger Punkt mit den Daten vereinbar bleibt und Systematik/Look-elsewhere/Modellunsicherheiten angemessen behandelt sind.

## Offizielle Endmatrix V1.5

```text
Stages 1-3.68:
    bearbeitet und dokumentiert.

Stage 3.68E:
    externes Fachfeedback technisch integriert.

Stage 3.69A/3.69A-1:
    Schwarzschild-Dirac-Radialsolver + In/Out-Matching implementiert und benchmarkiert.

Stage 3.69A-3:
    Earth-speed neutral proton Dirac mass scan CALCULATED;
    flux-stable weak-partial-wave extraction IMPLEMENTED;
    charge-feedback reference scales CALCULATED.

Stage 3.69A-4:
    charged Dirac capture + Q(t) OPEN.

Stage 3.69 Full-Multiphysics:
    NOT PERFORMED / OPEN.

Stage 3.70:
    branch-specific experimental falsification NOT PERFORMED.

H+:
    FAIL im getesteten Standard-Hawking/SK-IV-Projekt-Reinterpretationsmodell;
    Branch bleibt separat dokumentiert.

H0:
    OPEN / nicht nachgewiesen.

Formation:
    stark negativ / unaufgeloest.

Positive eindeutige Erdzentrum-BH-Signatur:
    keine nachgewiesen.
```
