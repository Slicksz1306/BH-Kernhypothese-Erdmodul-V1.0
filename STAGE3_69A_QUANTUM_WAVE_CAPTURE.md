# Stage 3.69A – Quantum/Wave-Capture-Regime

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** REGIME CLASSIFIED / DIRAC RADIAL PROTOTYPE IMPLEMENTED / FULL ABSORPTION MATCHING OPEN

## Ziel

Stage 3.69A prueft, ob die bisherige klassische Bondi-/Michel-Supplyrate bis zum Ereignishorizont als Capture-Rate interpretiert werden darf. Die Antwort ist derzeit **nein**: Bondi/Michel bleiben aeussere Supply-/Benchmarkmodelle. Die eigentliche Absorption muss teilchenspezifisch als Wellen-/GR-Capture berechnet werden.

## Referenzpunkt

Fuer den ersten Regimecheck wird verwendet:

```text
M_BH = 1.0e11 kg
c_eff = 10.4355 km/s
r_s = 1.48523e-16 m
r_B = 6.12885e-8 m = 61.29 nm
u = v/c = 3.48091e-5
```

Dabei ist `c_eff` der bereits in V1.5 dokumentierte PREM-Supply-Proxy.

## 1. Nichtrelativistischer Schrödinger-Aussenproxy

Ausserhalb der horizonnahen relativistischen Zone kann als erster Wellenproxy

```text
[-hbar^2/(2m) nabla^2 - G M_BH m/r] psi = E psi
```

verwendet werden. Fuer eine Partialwelle `l` folgt schematisch

```text
d2u_l/dr2 + [k^2 + 2 G M_BH m^2/(hbar^2 r) - l(l+1)/r^2] u_l = 0.
```

Diese Gleichung besitzt bei rein reellem Potential **keinen physikalischen BH-Sink**. Eine Absorption muss durch eine innere Randbedingung oder durch den relativistischen Horizon-Problemteil geliefert werden. Daher kann ein reiner Schrödinger-Solver die physikalische BH-Capture-Rate nicht allein bestimmen.

## 2. Wellenlaengen

Mit

```text
lambda_dB = h/(m v)
```

ergibt sich:

| Spezies | lambda_dB [m] | lambda_dB / r_s |
|---|---:|---:|
| Elektron | 6.97034e-8 | 4.69310e8 |
| Proton | 3.79616e-11 | 2.55594e5 |
| Fe-56-Kern | 6.83613e-13 | 4.60274e3 |

Damit ist der Horizont fuer alle drei Beispielteilchen deutlich kleiner als die de-Broglie-Wellenlaenge beim aeusseren PREM-Geschwindigkeitsproxy. Dieser Vergleich allein entscheidet die Absorption jedoch nicht.

## 3. Schwarzschild-Dirac-Kopplung

Doran et al. definieren fuer massive Spin-1/2-Teilchen die dimensionslose gravitative Kopplung

```text
alpha_g = G M_BH m/(hbar c).
```

Fuer den Referenzpunkt:

| Spezies | alpha_g | Regime-Hinweis |
|---|---:|---|
| Elektron | 1.92308e-4 | klarer Low-coupling/Quantum-Fall |
| Proton | 3.53107e-1 | Zwischenregime; volle Dirac-Integration erforderlich |
| Fe-56-Kern | 1.96084e1 | hoher Kopplungsbereich; klassischer Grenzwert naeherliegend, falls der Kern koharent bleibt |

Der wichtige Befund ist deshalb:

```text
lambda_dB >> r_s  bedeutet nicht fuer alle Teilchensorten dasselbe Capture-Regime.
```

Die Teilchenmasse und die Schwarzschild-Dirac-Kopplung muessen explizit beruecksichtigt werden.

### 3.1 Kopplungs-Uebergang im Projekt-Massenbereich

Die Masse, bei der `alpha_g=1` erreicht wird, ist

```text
M_transition = hbar c/(G m).
```

Damit folgt:

| Spezies | M_transition fuer alpha_g=1 [kg] |
|---|---:|
| Elektron | 5.200e14 |
| Proton | 2.832e11 |
| Fe-56-Kern | 5.100e9 |

Fuer typische Projektmassen:

| M_BH [kg] | alpha_e | alpha_p | alpha_Fe56 |
|---:|---:|---:|---:|
| 1e10 | 1.923e-5 | 3.531e-2 | 1.961 |
| 1e11 | 1.923e-4 | 3.531e-1 | 19.608 |
| 2e11 | 3.846e-4 | 7.062e-1 | 39.217 |
| 5e11 | 9.615e-4 | 1.766 | 98.042 |

Das ist fuer Stage 3.69A wesentlich: Elektronen bleiben im gesamten kleinen Projektbranch im schwachen Quantenkopplungsregime; Protonen durchlaufen innerhalb des interessanten Massenbereichs den Uebergang `alpha_g~1`; ein intakter Fe-56-Kern liegt bereits bei kleinen Projektmassen im starken Kopplungsbereich. Daher ist eine einzige universelle geometrische Capture-Fraktion nicht gerechtfertigt.

## 4. Literaturbenchmark fuer Fermionabsorption

Doran, Lasenby, Dolan & Hinder (Phys. Rev. D 71, 124020; arXiv:gr-qc/0503019) berechnen die Absorption massiver Spin-1/2-Teilchen durch direkte numerische Integration der Dirac-Gleichung auf einem Schwarzschild-Hintergrund mit rein einlaufender physikalischer Horizon-Loesung.

Wichtige Benchmarks aus dieser Arbeit:

- `alpha_g << 1`: starke Quanteneffekte; niedrigste Partialwellen dominieren.
- `alpha_g ~ 1`: energieabhaengige Abweichungen/Oszillationen um den klassischen Grenzwert.
- `alpha_g >> 1`: Annaeherung an die klassische Punktteilchen-Capture.
- hohe Energie: geometrisch-optischer Grenzwert.

Die dort angegebene Low-Energy-Unruh-Naherung wird fuer V1.5 **nicht** pauschal auf Protonen oder Fe-56 extrapoliert. Fuer `alpha_g~0.35` bzw. `~19.6` ist ein eigener numerischer Dirac-Lauf der sauberere Schritt.

## 5. Klassischer Collisionless-Benchmark

Der klassische Punktteilchen-Benchmark fuer ein Schwarzschild-BH kann als externer Grenzcheck verwendet werden. Bei `u=v/c=3.48091e-5` ergibt sich fuer `M_BH=1e11 kg` grob

```text
sigma_classical ~= 2.28778e-22 m^2.
```

Diese Groesse ist **keine Michel-Rate**. Die naive Multiplikation

```text
rho * v * sigma_classical
```

mit zentraler PREM-Dichte beschreibt einen collisionless Ballistic-Flux aus einem asymptotischen Teilchenbad und nicht einen dissipativen dichten Fluidstrom. Sie darf daher nicht als Ersatz fuer Michel-Akkretion verwendet werden.

## 6. Konsequenz fuer die H0-Akkretionsgleichung

Die bisherige schematische Identifikation

```text
Mdot_BH = Mdot_Michel
```

ist nicht als abgeschlossene Mikrophysik zulaessig. Stattdessen wird Stage 3.69 strukturell als

```text
Mdot_supply
 -> kollisionaler/kinetischer Uebergang
 -> species- und energy-abhaengige Wave/GR-Capture
 -> Mdot_BH
```

formuliert.

Formal:

```text
Mdot_BH = sum_i Integral dE [ Mdot_i,supply(E) * Gamma_i(E) ]
```

wobei `Gamma_i(E)` erst aus einer horizon-konsistenten relativistischen Wellenrechnung bzw. einer daran kalibrierten Transportclosure stammen darf.

## 7. Stage 3.69A-1 – Schwarzschild-Dirac-Prototyp

**Teilweise durchgefuehrt am 26.08.2026.**

Implementiert wurden:

1. radiale massive Dirac-Gleichung in horizon-regulaeren Painleve-Gullstrand-Koordinaten,
2. regulaerer `s=0`-Horizon-Branch,
3. erster Taylor-Koeffizient zur stabilen Initialisierung direkt ausserhalb `r=2M`,
4. radiale DOP853-Integration,
5. konservierter Dirac-Strom/Wronskian als harter Solver-Selfcheck.

Benchmark:

```text
alpha=0.2, u=0.5, x=r/M: 2+1e-6 -> 1000
```

Ergebnis:

```text
kappa=-1: relative Wronskian drift ~3.68e-10
kappa=+1: relative Wronskian drift ~1.45e-11
```

Damit gilt nur fuer dieses numerische Teilmodul:

```text
regular horizon branch + radial Dirac integration: SELF-CHECK PASS.
```

### Noch nicht bestanden: asymptotisches Matching

Die physikalische Absorptionsrate erfordert die stabile Zerlegung

```text
U(r->infinity) = alpha_kappa U_in + beta_kappa U_out
```

und danach die Partialwellensumme. Ein erster Leading-Order-Matching-Versuch war bei kleinen Impulsen noch zu sensitiv gegen den Matchingradius. Daher wird daraus bewusst **keine** physikalische `sigma_abs` berichtet.

Akzeptanzkriterien fuer den naechsten Substep:

- stabile `|alpha_kappa|` gegen Matchingradius und Matchingfenster,
- Reproduktion der publizierten Doran-Kurve bei `alpha=0.2`,
- Reproduktion des Unruh-Low-Energy-Limits bei `alpha<<1`,
- High-energy-Konvergenz gegen den geometrisch-optischen Grenzwert.

Details: [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md).

## 8. Analytischer Low-Energy-Grenzcheck

Am Projekt-Referenzpunkt `M_BH=1e11 kg`, `u=10.4355 km/s / c` ergibt die publizierte Unruh/Doran-Low-Energy-Naeherung fuer das Elektron

```text
alpha_e = 1.92308e-4
sigma_lowE,e ~= 3.4554e-26 m^2.
```

Dieser Elektronenwert liegt klar im schwachen Kopplungsregime und ist ein sinnvoller spaeterer Solver-Benchmark. Fuer das Proton liefert dieselbe Formel formal `~6.3447e-23 m^2`, wird bei `alpha_p~0.353` aber **nicht als finale Projektabsorption akzeptiert**, bis das volle numerische Matching funktioniert. Fuer Fe-56 wird die schwach gekoppelte Low-Energy-Naeherung nicht extrapoliert.

## Status

```text
Schroedinger-Aussenproxy: DONE als Regime-/Wellencheck.
Teilchenspezifische Regime: identifiziert.
Protonen-Uebergang alpha_g~1: ~2.83e11 kg.
Dirac radial equation: IMPLEMENTED.
Regular horizon boundary: IMPLEMENTED.
Wronskian/current conservation: SELF-CHECK PASS.
Asymptotic in/out matching: OPEN.
Partial-wave sigma_abs: OPEN.
Species-resolved net Mdot: OPEN.
H0 dadurch weder bestaetigt noch ausgeschlossen.
Stage 3.69 insgesamt: weiterhin NOT PERFORMED als kompletter Multiphysik-Endtest.
```

## Reproduzierbarkeit

- [`stage3_69a_quantum_capture_regime.py`](stage3_69a_quantum_capture_regime.py)
- [`stage3_69a1_dirac_prototype.py`](stage3_69a1_dirac_prototype.py)
- [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md)

## Referenzen

- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
