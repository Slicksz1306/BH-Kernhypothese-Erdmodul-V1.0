# Stage 3.69A-3 – Low-Velocity-Bridge fuer den Erdbranch

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** ISOLATED-PARTICLE LOW-ENERGY SCAN CALCULATED / DENSE-MATTER CLOSURE OPEN

## Ziel

Nach dem externen Unruh/Doran-Regressionstest aus Stage 3.69A-2 wird jetzt der fuer den Erdbranch relevante sehr langsame Bereich untersucht.

Referenzgeschwindigkeit:

```text
v_ref = 10.4355 km/s
u = v/c = 3.4809081e-5
```

Verglichen werden zwei klar definierte Einteilchen-Benchmarks:

1. klassische collisionless Punktteilchen-Capture nach Doran et al. Eq. (3);
2. Unruh-Low-Energy-Naeherung fuer massive Spin-1/2-Teilchen, Doran et al. Eq. (31).

Definiert wird

```text
R_i(M) = sigma_Unruh,i / sigma_classical.
```

`R<1` bedeutet im **isolierten Einteilchenbenchmark** einen kleineren Querschnitt als klassisch, `R~1` einen vergleichbaren und `R>1` einen groesseren Querschnitt.

Das ist noch keine Aussage ueber die Netto-Akkretionsrate dichter Fe/Ni-Materie.

## 1. Numerische Stabilitaet der klassischen Referenz

Die direkte Formel

```text
sigma_cl/M^2 = pi/(2 u^4) [8u^4 + 20u^2 - 1 + (1+8u^2)^(3/2)]
```

leidet fuer `u ~ 1e-5` in normaler Float64-Auswertung unter Subtraktionsausloeschung zwischen `-1` und `(1+8u^2)^(3/2)`.

Der neue Code wertet den kleinen Differenzterm deshalb stabil ueber `expm1/log1p` aus.

Fuer den Referenzpunkt ergibt sich

```text
sigma_classical/M^2 ~= 4.1484393e10.
```

## 2. Protonenbenchmark

| M_BH [kg] | alpha_p | R_p = sigma_Unruh/sigma_classical |
|---:|---:|---:|
| 1.000e11 | 0.353107 | 0.277330 |
| 2.000e11 | 0.706215 | 0.554660 |
| 2.832e11 | 1.000000 | 0.785398 |
| 3.600e11 | 1.271186 | 0.998387 |
| 4.000e11 | 1.412429 | 1.109319 |
| 5.000e11 | 1.765536 | 1.386649 |

Der Einteilchen-Low-Energy-Benchmark kreuzt

```text
R_p = 1
```

bei

```text
M_BH ~= 3.6058153e11 kg.
```

Das ist wichtig: Im betrachteten H0-Massenbereich ergibt der Unruh-Benchmark fuer Protonen **keine pauschale starke Quantenunterdrueckung**.

Bei `1e11 kg` ist der isolierte Protonenquerschnitt gegenueber dem klassischen Punktteilchenwert um einen Faktor von etwa `3.6` kleiner. Schon um `3.6e11 kg` ist der Unterschied praktisch verschwunden; oberhalb davon liegt die Unruh-Naeherung sogar ueber dem klassischen Benchmark.

## 3. Elektronenbenchmark

| M_BH [kg] | alpha_e | R_e = sigma_Unruh/sigma_classical |
|---:|---:|---:|
| 1.000e11 | 1.92308e-4 | 1.51039e-4 |
| 2.000e11 | 3.84616e-4 | 3.02077e-4 |
| 2.832e11 | 5.44617e-4 | 4.27741e-4 |
| 3.600e11 | 6.92310e-4 | 5.43739e-4 |
| 4.000e11 | 7.69233e-4 | 6.04154e-4 |
| 5.000e11 | 9.61541e-4 | 7.55193e-4 |

Elektronen bleiben in diesem BH-Massenbereich im sehr schwachen Kopplungsregime und ihr isolierter Low-Energy-Capturequerschnitt liegt weit unter dem klassischen Punktteilchenwert.

Der entsprechende `R_e=1`-Uebergang liegt erst bei Groessenordnung

```text
M_BH ~ 6.6e14 kg,
```

also weit oberhalb des hier betrachteten kleinen Erd-H0-Bereichs.

## 4. Warum das wissenschaftlich relevant ist

Damit ist eine einfache Aussage wie

```text
"Quantenmechanik unterdrueckt die gesamte Akkretion um einen riesigen gemeinsamen Faktor"
```

mathematisch nicht haltbar.

Schon im isolierten Spin-1/2-Modell ist die Wirkung stark spezies- und massenabhaengig:

```text
electron: R << 1
proton:   R ~ 0.28 ... 1.39 im gescannten Bereich
```

Das bestaetigt, warum eine einzige universelle `quantum suppression factor`-Zahl fuer H0 unzureichend waere.

## 5. Aber: noch keine Erd-Nettoakkretion

Der Erdkern ist kein freies Elektron-Proton-Gas.

Insbesondere:

- Fe-56 und Ni-58 sind zusammengesetzte Kerne und keine Dirac-Protonen;
- dominante Fe/Ni-Grundzustandskerne besitzen Spin `0+` und benoetigen bei kohärenter Capture einen skalaren/composite Ansatz;
- die lokale Materie ist dicht und kollisional;
- Ionisations-, Dissoziations- und Reaktionszeiten koennen entscheiden, wann Nukleonen als freie Fermionen behandelt werden duerfen;
- unterschiedliche Capture-Raten erzeugen Ladungsfeedback;
- Debye-Screening und ambipolare Rueckkopplung koennen den Nachstrom regulieren.

Deshalb darf aus `R_p` oder `R_e` **nicht** direkt

```text
Mdot_H0 = R * Mdot_Bondi
```

gebaut werden.

## 6. Konsequenz fuer die Loeb/Cline-Frage

Der neue Rechenschritt stuetzt keine Seite per Autoritaet, sondern praezisiert den mathematischen Kern des Streits:

- Einteilchen-Quantenabsorption kann stark vom klassischen Wert abweichen.
- Diese Abweichung ist nicht universell; sie haengt von `alpha`, Energie und Spezies ab.
- Fuer Protonen im kleinen Erd-H0-Bereich ist eine extrem starke pauschale Unterdrueckung durch den Unruh-Benchmark gerade **nicht** gegeben.
- Ob daraus eine kleinere **Gesamt-Mdot** folgt, bleibt ein Viele-Teilchen-/Transport-/Ladungsproblem.

Damit wird der naechste Block klarer statt diffuser.

## 7. Naechster Pflichtblock

```text
Stage 3.69A-4:
Charge / ambipolar capture closure
```

Minimalgleichungen:

```text
dQ/dt = sum_i q_i Ndot_i(Q)

Mdot_BH = sum_i m_i Ndot_i(Q)
```

mit speziesabhaengigen Capture-Raten und Coulomb-Rueckkopplung.

Parallel bleibt fuer intakte Fe/Ni-Kerne offen:

```text
coherent scalar/composite capture + finite nuclear size.
```

## 8. Status

```text
External low-energy Dirac regression: PASS at tested points.
Stable Earth-velocity classical benchmark: DONE.
Electron low-energy single-particle scan: DONE.
Proton low-energy single-particle scan: DONE.
Proton R=1 transition: ~3.606e11 kg.
Universal strong quantum suppression: NOT supported by this single-particle scan.
Dense Fe/Ni net accretion: OPEN.
Charge-feedback / ambipolar closure: OPEN.
Coherent Fe/Ni capture: OPEN.
H0 neither confirmed nor excluded.
```

## Reproduzierbarkeit

Code:

- `stage3_69a1_dirac_prototype.py`
- `stage3_69a2_dirac_regression.py`
- `stage3_69a3_low_velocity_bridge.py`

## Referenzen

- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
- A. Loeb, *Quantum-mechanical Suppression of Accretion by Primordial Black Holes*, ApJL 975 L15 (2024), arXiv:2409.09081.
- J. M. Cline, Comment on the above accretion-suppression argument (2024), arXiv:2409.12989.
