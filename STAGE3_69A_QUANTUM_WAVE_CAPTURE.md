# Stage 3.69A – Quantum/Wave-Capture-Regime

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** INITIALIZED / REGIME CLASSIFIED / FULL DIRAC SOLVER NOT PERFORMED

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

## 4. Literaturbenchmark fuer Fermionabsorption

Doran, Lasenby, Dolan & Hinder (Phys. Rev. D 71, 124020; arXiv:gr-qc/0503019) berechnen die Absorption massiver Spin-1/2-Teilchen durch direkte numerische Integration der Dirac-Gleichung auf einem Schwarzschild-Hintergrund mit rein einlaufender physikalischer Horizon-Loesung.

Wichtige Benchmarks aus dieser Arbeit:

- `alpha_g << 1`: starke Quanteneffekte; niedrigste Partialwellen dominieren.
- `alpha_g ~ 1`: energieabhaengige Abweichungen/Oszillationen um den klassischen Grenzwert.
- `alpha_g >> 1`: Annaeherung an die klassische Punktteilchen-Capture.
- hohe Energie: geometrisch-optischer Grenzwert.

Die dort angegebene Low-Energy-Unruh-Naherung wird fuer V1.5 **nicht** pauschal auf Protonen oder Fe-56 extrapoliert. Fuer `alpha_g~0.35` bzw. `~19.6` ist ein eigener numerischer Dirac-Lauf der sauberere naechste Schritt.

## 5. Klassischer Collisionless-Benchmark

Der exakte klassische Punktteilchen-Benchmark fuer ein Schwarzschild-BH kann als externer Grenzcheck verwendet werden. Bei `u=v/c=3.48091e-5` ergibt sich fuer `M_BH=1e11 kg`:

```text
sigma_classical ~= 2.28778e-22 m^2.
```

Diese Groesse ist **keine Michel-Rate**. Die naive Multiplikation

```text
rho * v * sigma_classical
```

mit zentraler PREM-Dichte beschreibt einen collisionless Ballistic-Flux aus einem asymptotischen Teilchenbad und nicht einen dissipativen dichten Fluidstrom. Sie darf daher nicht als Ersatz fuer Michel-Akkretion verwendet werden.

Gerade der grosse Unterschied zwischen Fluid-Supply und collisionless Capture zeigt, warum Stage 3.69 die kollisional/kinetische Uebergangszone und Recycling explizit loesen muss.

## 6. Konsequenz fuer die H0-Akkretionsgleichung

Die bisherige schematische Identifikation

```text
Mdot_BH = Mdot_Michel
```

ist nicht als abgeschlossene Mikrophysik zulässig. Stattdessen wird Stage 3.69 jetzt strukturell als

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

## 7. Naechster numerischer Schritt – Stage 3.69A-1

**Noch nicht durchgefuehrt.**

Zu implementieren ist ein reproduzierbarer Schwarzschild-Dirac-Partialwellensolver nach dem Prinzip:

1. Painleve-Gullstrand- oder horizon-regulaere Eddington-Finkelstein-Koordinaten.
2. Massive Dirac-Gleichung auf festem Schwarzschild-Hintergrund.
3. rein einlaufende/regelmaessige Horizon-Randbedingung.
4. radiale Integration nach aussen.
5. Matching auf ein-/auslaufende asymptotische Wellen.
6. Partialwellensumme fuer `sigma_abs(E,m,M_BH)`.
7. Reproduktion publizierter Benchmarkkurven vor Anwendung auf den Erdbranch.
8. danach Kopplung an die lokale Fe/Ni-Plasma-/Kernzusammensetzung aus Stage 3.69.

## Status

```text
Schroedinger-Aussenproxy: brauchbar fuer Regime-/Wellencheck, nicht fuer finale Horizon-Capture.
Dirac/Schwarzschild-Capture: erforderlich.
Teilchenspezifische Regime: identifiziert.
Volle Capture-Rate: OPEN.
H0 dadurch weder bestaetigt noch ausgeschlossen.
Stage 3.69A-1: NOT PERFORMED.
```

## Referenzen

- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
