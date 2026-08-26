# Stage 3.69A-3 – Earth-speed Proton Dirac Capture + Charge Feedback

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** EARTH-SPEED NEUTRAL PROTON DIRAC CAPTURE NUMERICALLY EVALUATED / CHARGE SCALES CALCULATED / DENSE-MATTER CHARGE CLOSURE OPEN

## Ziel

Stage 3.69A-3 schliesst zwei konkrete Luecken des vorherigen Quantum/Wave-Capture-Blocks:

1. den isolierten **Protonen-Capture bei der Erd-Referenzgeschwindigkeit** `v=10.4355 km/s` mit dem vollen Schwarzschild-Dirac-Matcher statt einer unkontrollierten Extrapolation der Unruh-Low-Energy-Naeherung;
2. die erste quantitative Skala fuer **elektrostatisches Ladungsfeedback** zwischen Protonen und Elektronen.

Dieser Schritt ist weiterhin **keine** dichte Fe/Ni-Netto-Akkretionsrechnung und kein empirischer Nachweis eines Erdzentrum-BH.

## 1. Referenzgeschwindigkeit

Verwendet wird der bereits dokumentierte PREM-Supply-Proxy

```text
v = c_eff = 10.4355 km/s
u = v/c = 3.4809081e-5.
```

`c_eff` ist ein aeusserer Supply-/Skalenproxy und keine vollstaendige mikroskopische Protonen- oder Elektronendispersionsrelation.

## 2. Numerische Verbesserung: flux-stabile Absorptionswahrscheinlichkeit

Im bisherigen Prototyp wurde

```text
P_abs = 1 - |S_kappa|^2
```

verwendet. Fuer sehr schwach absorbierte hohe Partialwellen kann diese Form durch Subtraktion fast gleicher Zahlen numerisch schlecht konditioniert sein.

Der konservierte Doran-Strom lautet asymptotisch

```text
W = -2 p/(E+m) * (|A_in|^2 - |A_out|^2).
```

Da der numerische Horizon-Branch auf `W_H=-1` normiert ist, kann die Absorptionswahrscheinlichkeit direkt aus dem eingehenden Fluss bestimmt werden:

```text
q = p/(E+m)
P_abs = (-W_H) / (2 q |A_in|^2).
```

Diese Form vermeidet die direkte Differenz `1-|S|^2`. Sie wird in `stage3_69a3_earth_proton_charge.py` fuer die Massenscans verwendet.

Wichtig: Bei extrem schwach absorbierten Partialwellen kann auch die direkte Auswertung des Fernfeld-Wronskians relativ schlecht konditioniert sein. Deshalb werden Konvergenz der Cross-Section, Partialwellenschnitt und Matchingradius getrennt kontrolliert.

## 3. Earth-speed Protonen-Massenscan

Die Kopplung ist

```text
alpha_p = G M_BH m_p / (hbar c).
```

Der klassische collisionless Punktteilchenwert bei festem `u` dient nur als Vergleichsskala.

| `M_BH` | `alpha_p` | verwendetes `kmax` | `x_match` | `sigma_Dirac/sigma_classical` | `sigma_Dirac` [m^2] |
|---:|---:|---:|---:|---:|---:|
| `1e10 kg` | `0.0353107` | 3 | `5e6` | `0.0326735` | `7.47496e-26` |
| `1e11 kg` | `0.353107` | 3 | `5e6` | `0.950295` | `2.17406e-22` |
| `2e11 kg` | `0.706215` | 5 | `2e6` | `1.008071` | `9.22496e-22` |
| `5e11 kg` | `1.76554` | 9 | `1e6` | `0.996621` | `5.70011e-21` |

### Partialwellen-Konvergenz bei `5e11 kg`

Der hohe Massenpunkt benoetigt deutlich mehr Partialwellen:

```text
kmax=5 -> sigma/sigma_classical ~0.6015
kmax=6 -> ~0.8420
kmax=7 -> ~0.99630
kmax=8 -> ~0.99662110
kmax=9 -> ~0.99662113
```

Damit ist `kmax=9` fuer diesen Projektpunkt praktisch konvergiert.

### Matchingradius-Spotcheck bei `1e11 kg`

```text
x_match=1e6  -> sigma/sigma_classical = 0.95024543
x_match=5e6  -> sigma/sigma_classical = 0.95029487
x_match=1e7  -> sigma/sigma_classical = 0.95035969
```

Die Aenderung ueber eine Dekade im Matchingradius liegt damit bei rund `1.2e-4` relativ zur klassischen Vergleichsskala bzw. rund `1.2e-4` absolut im Quotienten. Der dominante Befund `~95% des klassischen Werts` ist robust gegen diesen Spotcheck.

## 4. Konsequenz fuer die fruehere Unruh-Protonenextrapolation

Am Referenzpunkt `M_BH=1e11 kg` ergab die zuvor verwendete analytische Unruh-Low-Energy-Naeherung

```text
sigma_Unruh,p ~6.3447e-23 m^2.
```

Der volle numerische Dirac-Matcher ergibt dagegen

```text
sigma_Dirac,p ~2.1741e-22 m^2
             ~0.9503 sigma_classical.
```

Die fruehere Unruh-Zahl bleibt als **Low-Energy-/Low-Coupling-Benchmark** dokumentiert, wird aber bei `alpha_p~0.353` nicht mehr als finaler Protonen-Capture-Wert verwendet.

Das ist qualitativ konsistent mit Doran et al.: kleine Kopplung kann starke Wellenabweichungen zeigen; bei groesserer Kopplung naehert sich der Absorptionsquerschnitt dem klassischen Capture an und zeigt im Uebergangsbereich Oszillationen um den klassischen Wert.

## 5. Erste Charge-Feedback-Skalen

Schon sehr kleine BH-Nettoladungen koennen die Dynamik geladener Teilchen stark veraendern, obwohl die Metrikkorrektur winzig bleibt.

### 5.1 Kraftvergleich fuer eine Elementarladung

Bei `M_BH=1e11 kg` gilt fuer `|Q|=e`:

```text
|F_C/F_G| proton   = 0.0206661
|F_C/F_G| electron = 37.9461.
```

Eine einzige Elementarladung entspricht also bereits etwa `2.07%` der Protonengravitation, waehrend der Coulombterm fuer Elektronen die gravitative Kraftskala um fast Faktor `38` uebertrifft.

### 5.2 Klassische Kraftgrenzen

Aus `F_C=F_G` folgt

```text
Q_max,p = 4 pi eps0 G M m_p / e
|Q_max,e| = 4 pi eps0 G M m_e / e.
```

Fuer `M_BH=1e11 kg`:

```text
Q_max,p   = +48.3884 e = 7.75268e-18 C
|Q_max,e| =   0.026353 e = 4.22224e-21 C.
```

Das sind Fernfeld-Kraftskalen, keine selbstkonsistente Akkretionsloesung.

### 5.3 Stationaerer Equal-T-Plasma-Benchmark

Zajacek et al. (2018) geben fuer ein stationaeres sphaerisches Proton/Elektron-Plasma bei `T_e=T_p`

```text
Q_eq = 2 pi eps0 G (m_p-m_e) M / e.
```

Fuer `1e11 kg`:

```text
Q_eq ~ +24.1810 e
     ~ 3.87423e-18 C.
```

Diese Formel wurde fuer ein idealisiertes Plasma abgeleitet und ist **nicht** direkt auf dichte Fe/Ni-Erdkernmaterie uebertragbar. Screening, Kollisionen, Degeneration, Ionisation, Kernstruktur und Transport muessen in Stage 3.69 gekoppelt werden.

### 5.4 Raumzeit bleibt praktisch Schwarzschild

Die Reissner-Nordstroem-Extremalladungsskala ist bei `1e11 kg`

```text
Q_extremal ~8.6175 C.
```

Damit

```text
Q_eq / Q_extremal ~4.50e-19.
```

Die metrische RN-Korrektur ist auf diesen Charge-Feedback-Skalen vernachlaessigbar, waehrend die Bewegung geladener Teilchen bereits stark beeinflusst werden kann. Das rechtfertigt als naechsten Schritt zunaechst einen geladenen Teilchen-/Dirac-Capture auf praktisch Schwarzschild-Geometrie; eine vollstaendige RN-Metrik bleibt als Kontrollrechnung moeglich.

## 6. Branch-Trennung H+ / H0

Die Capture- und Charge-Feedback-Physik ist zunaechst ein gemeinsamer Block fuer beide Projektbranches:

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung.
```

Stage 3.69A-3 entscheidet **nicht** zwischen H+ und H0.

- Fuer **H+** muessen spaeter zusaetzlich Hawking-Emission, Ladungsabgabe/-aufnahme und die bereits getesteten Neutrino-/Gamma-Signaturen gekoppelt werden.
- Fuer **H0** entfallen Hawking-Quellterme definitionsgemaess, aber Akkretion, Charge Feedback, Dense-Matter-Transport und Langzeitstabilitaet bleiben vollstaendig zu bestehen.

## 7. Neuer Status

```text
Schroedinger-Regimecheck: DONE
Schwarzschild-Dirac radial solver: PASS as numerical solver benchmark
Low-alpha external regression: PASS
Intermediate-alpha benchmark structure: PASS qualitatively/numerically
Earth-speed neutral proton Dirac capture: CALCULATED
Earth-speed proton mass scan 1e10...5e11 kg: CALCULATED
flux-stable weak-partial-wave extraction: IMPLEMENTED
Unruh proton extrapolation at alpha~0.35: REPLACED by full Dirac result
charge force scales: CALCULATED
stationary equal-T plasma charge benchmark: CALCULATED
charged Dirac capture sigma_p,e(Q): OPEN
dense Fe/Ni screening/transport charge closure: OPEN
coherent Fe/Ni scalar/composite capture: OPEN
species-resolved dense-core net Mdot: OPEN
Stage 3.69 Full-Multiphysics: OPEN
Stage 3.70 experimental falsification: OPEN
```

## 8. Naechster Schritt

```text
Stage 3.69A-4:
charged Dirac capture + self-consistent Q(t)
```

Schematisch:

```text
dQ/dt = e [Gamma_p(Q) - Gamma_e(Q)] + branch-specific source/sink terms

Mdot_BH = sum_i m_i Gamma_i(Q) + composite/nuclear channels.
```

Erst nach Kopplung an Screening, Fe/Ni-Komposition, Kollisionen und Transport kann daraus eine belastbare Erdzentrum-Netto-Akkretionsrate abgeleitet werden.

## Reproduzierbarkeit

Code:

- `stage3_69a1_dirac_prototype.py`
- `stage3_69a3_earth_proton_charge.py`

## Referenzen

- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
- S. Dolan, C. Doran, A. Lasenby, *Fermion scattering by a Schwarzschild black hole*, Phys. Rev. D 74, 064005 (2006), arXiv:gr-qc/0605031.
- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
- M. Zajaček et al., *On the charge of the Galactic centre black hole*, MNRAS 480, 4408-4423 (2018).
- K. Nakao, K. Matsuo, H. Yoshino, H. Ishihara, *Electrification of a non-rotating black hole*, arXiv:2409.17639 (2024).
