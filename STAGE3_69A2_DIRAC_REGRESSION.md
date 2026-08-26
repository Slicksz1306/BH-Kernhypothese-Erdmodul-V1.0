# Stage 3.69A-2 – Externe Schwarzschild-Dirac-Regression

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** LOW-ENERGY UNRUH/DORAN REGRESSION PASS / EARTH LOW-VELOCITY BRIDGE OPEN

## Ziel

Stage 3.69A-1 hatte bereits

- die radiale massive Dirac-Gleichung,
- den regulaeren Horizon-Branch,
- den konservierten Dirac-Strom,
- asymptotisches In/Out-Matching,
- und erste qualitative Doran-Benchmarks

implementiert.

Das reicht fuer einen wissenschaftlich belastbaren Solver aber nicht: Ein Solver darf nicht nur gegen seine eigenen internen Checks getestet werden. Stage 3.69A-2 fuegt deshalb einen **externen analytischen Regressionstest** ein.

Getestet wird gegen die von Doran et al. (2005) zitierte Unruh-Low-Energy-Naeherung

```text
sigma_abs/M^2 ~= 4 pi^2 (1+u^2) alpha
                 ----------------------------------------------
                 u^2 sqrt(1-u^2)
                 [1-exp(-2 pi alpha(1+u^2)/(u sqrt(1-u^2)))]
```

im Regime, in dem die beiden `|kappa|=1`-Partialwellen dominieren.

Ein nicht reproduzierter Benchmark wird als **FAIL des Solvers** behandelt und nicht als Aussage ueber H0 interpretiert.

## 1. Neue numerische Beobachtung: ein fester Matchingradius reicht nicht

Bei kleinen Kopplungen wird

```text
p M = alpha sqrt((E/m)^2 - 1)
```

sehr klein. Damit liegt die echte Fernzone nicht bei einem universellen Wert wie `x_match=1000`, sondern erfordert

```text
p * x_match >> 1.
```

Ein zu kleiner fester Radius kann deshalb scheinbar stabile, aber falsche Low-Energy-Cross-Sections erzeugen.

Der Regressionstest parametrisiert den Matchingradius daher ueber `p*x_match`.

## 2. Langstrecken-Stabilisierung

Direkte DOP853-Integration ueber `x ~ 1e5 ... 1e6` akkumuliert trotz sehr guter lokaler Genauigkeit einen kleinen numerischen Drift des konservierten Wronskians.

Stage 3.69A-2 integriert deshalb segmentiert. Nach jedem Segment wird die gemeinsame Amplitude wieder auf

```text
W = -1
```

normiert.

Das ist fuer das Streuverhaeltnis

```text
S_kappa = A_out/A_in
```

unschädlich, weil eine gemeinsame skalare Multiplikation von `U=(u1,u2)` das Verhaeltnis `A_out/A_in` nicht aendert.

Wichtig: Die Renormierung selbst wird **nicht** als Stromerhaltungsbeweis gewertet. Als Accuracy-Metrik wird der rohe Wronskian-Drift **vor jeder Renormierung** gespeichert.

Verwendete harte Einstellungen:

```text
DOP853
rtol = 5e-13
atol = 5e-15
Delta(p*x) <= 10 pro Fernzonen-Segment
max raw segment W drift < 1e-8
```

## 3. Externer Benchmark A

```text
alpha = 0.01
E/m   = 1.10
```

Unruh:

```text
sigma_U/M^2 = 16.59797190
```

Numerik:

| p*x_match | x_match | sigma_num/M^2 | Abweichung zu Unruh |
|---:|---:|---:|---:|
| 1000 | 218217.89 | 16.83332896 | 1.418 % |
| 2000 | 436435.78 | 16.84806418 | 1.507 % |

Konvergenz der letzten beiden Radien:

```text
|sigma_2000/sigma_1000 - 1| = 8.75e-4
```

Maximaler roher Segment-Wronskian-Drift:

```text
5.94e-9
```

Ergebnis:

```text
Wronskian: PASS
Matchingradius: PASS
Unruh-Regressionsfenster (<3%): PASS
```

## 4. Externer Benchmark B

```text
alpha = 0.005
E/m   = 1.20
```

Unruh:

```text
sigma_U/M^2 = 11.88026004
```

Numerik:

| p*x_match | x_match | sigma_num/M^2 | Abweichung zu Unruh |
|---:|---:|---:|---:|
| 1000 | 301511.34 | 11.93033527 | 0.421 % |
| 2000 | 603022.69 | 11.93339163 | 0.447 % |

Konvergenz der letzten beiden Radien:

```text
|sigma_2000/sigma_1000 - 1| = 2.56e-4
```

Maximaler roher Segment-Wronskian-Drift:

```text
8.32e-9
```

Ergebnis:

```text
Wronskian: PASS
Matchingradius: PASS
Unruh-Regressionsfenster (<2%): PASS
```

## 5. Was damit jetzt mathematisch feststeht

Der Stage-3.69A-1-Schwarzschild-Dirac-Solver reproduziert nicht nur intern Stromerhaltung und qualitative Oszillationsstruktur. Mit ausreichend weit entfernter Fernzone und stabilisierter Langstreckenintegration reproduziert er auch einen **extern publizierten Low-Energy-Benchmark** im getesteten Parameterbereich auf Prozent- bis Subprozentniveau.

Das ist ein echter Solver-Fortschritt.

Es ist **kein Beweis fuer H0** und noch keine Erd-Akkretionsrate.

## 6. Was weiterhin offen bleibt

Der relevante Erdbranch ist numerisch schwieriger als die obigen Regressionen. Fuer `M_BH ~ 1e11 kg` gilt ungefaehr

```text
alpha_p ~ 0.353
alpha_e ~ 1.92e-4
u_earth ~ 3.48e-5
```

Damit ist insbesondere fuer Protonen

```text
alpha_p ~ O(1)
```

aber gleichzeitig

```text
pM = alpha_p * u << 1.
```

Das ist ein extrem langwelliger, sehr langsamer Bereich. Ein naiver direkter Fernzonenlauf wuerde Matchingradien von vielen Millionen bis Milliarden `M` verlangen.

Der naechste Pflichtblock ist deshalb nicht einfach ein groesserer Brute-Force-Run, sondern eine kontrollierte **Low-Velocity-Bridge** zwischen

1. numerischem Schwarzschild-Dirac-Solver,
2. Unruh-/Matched-Asymptotic-Regime,
3. Protonenbereich `alpha ~ 0.1 ... 2`,
4. und dem realen Erdgeschwindigkeitsbereich `u ~ 1e-5 ... 1e-4`.

Danach erst darf die speziesaufgeloeste Capture-Rate in die Ladungs-/Plasma-Closure eingehen.

## 7. Status

```text
Radial Dirac ODE: PASS.
Regular horizon branch: PASS.
Current conservation at ordinary benchmark radii: PASS.
Asymptotic in/out matching: PASS.
Matching-radius convergence at alpha=0.2: PASS.
External Unruh low-energy regression: PASS at tested points.
Long-range segmented current stabilization: IMPLEMENTED / PASS.
Full digitized Doran Figure-1 regression: OPEN.
Earth proton alpha~O(1), u~1e-5 exact bridge: OPEN.
Charge-feedback / ambipolar closure: OPEN.
Dense-core net Mdot_H0: OPEN.
H0 thereby neither confirmed nor excluded.
```

## Reproduzierbarkeit

Code:

- `stage3_69a1_dirac_prototype.py`
- `stage3_69a2_dirac_regression.py`

## Referenzen

- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
- S. Dolan, C. Doran, A. Lasenby, *Fermion scattering by a Schwarzschild black hole*, Phys. Rev. D 74, 064005 (2006), arXiv:gr-qc/0605031.
- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
