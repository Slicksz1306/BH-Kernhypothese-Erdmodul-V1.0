# Stage 3.69A-4 – Charged Dirac Capture + Q-Feedback

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** CHARGED PROTON DIRAC PROXY NUMERICALLY EVALUATED / Q-FEEDBACK IMPORTANT / CHARGED ELECTRON FAR-FIELD MATCHING OPEN

## Ziel

Stage 3.69A-4 prueft, ob die in A-3 gefundene elektrische Rueckkopplung die Protonenaufnahme am Erd-Referenzpunkt stark unterdruecken kann.

Referenz:

```text
M_BH = 1e11 kg
v = 10.4355 km/s
alpha_p = 0.3531
```

Die Raumzeit wird weiter als Schwarzschild behandelt. Fuer die betrachteten Ladungen von wenigen bis einigen Dutzend Elementarladungen ist die Reissner-Nordstroem-Metrikkorrektur gegenueber der Extremalladung verschwindend klein; der Coulombterm kann die Bewegung geladener Teilchen trotzdem stark beeinflussen.

## 1. Charged-Dirac-Proxy

Der A-1-Dirac-Solver wird durch minimale Kopplung an ein schwaches zentrales Coulombfeld erweitert. In den dimensionslosen radialen Gleichungen wird lokal

```text
E_eff(x) = E_inf - zeta/x
zeta = N_e * alpha_EM
```

fuer ein Proton und `Q_BH=N_e e` verwendet.

Wichtig: Dies ist ein **Schwarzschild + Test-Coulomb**-Solver, kein vollstaendiger RN-Wellensolver. Bei den hier betrachteten extrem kleinen geometrischen Ladungen ist das die kontrollierte erste Naeherung.

Die Integration wird auf logarithmischen Radialsegmenten wiederholt normiert. Nur die Richtung des Spinors und damit `A_out/A_in` wird benoetigt; dadurch wird die grosse Dynamikspanne des Earth-speed-Problems numerisch stabilisiert.

## 2. Neutraler Regressionstest

Bei `Q=0` liefert der A-4-Solver fuer `x_match=5e5 M`

```text
sigma_p / sigma_classical = 0.94887
```

gegenueber dem staerker konvergierten A-3-Wert von etwa

```text
0.9503.
```

Die Differenz liegt im bekannten endlichen Matchingradius-/Partialwellenniveau. Der charged Solver reproduziert damit den neutralen Referenzpunkt.

## 3. Positive BH-Ladung – Protonen

Fuer `M=1e11 kg` ergibt sich, relativ zur neutralen klassischen Capture-Cross-Section:

| Q_BH | charged Dirac proxy |
|---:|---:|
| `0 e` | `0.949` |
| `3.67 e` | `0.889` |
| `10 e` | `0.765` |
| `24.18 e` | `0.517` |

`3.67 e` ist die auf diesen BH skalierte equal-temperature diffuse-plasma Groessenordnung aus der relativistischen Nakao-Analyse. `24.18 e` ist die fruehere equal-temperature Zajacek-Skala. Beide sind **Benchmarks**, keine Vorhersagen fuer dichte Fe/Ni-Erdkernmaterie.

Matchingradius-Spotchecks (`2e5, 5e5, 1e6 M`) zeigen fuer diese Ladungen nur kleine Schwankungen und keinen qualitativen Wechsel.

## 4. Unabhaengiger klassisch-relativistischer Benchmark

Aus dem charged-test-particle Effektivpotential der relativistischen Schwarzschild+Coulomb-Analyse kann die kritische Capture-Bahn als Doppelwurzel bestimmt werden.

Fuer die gleichen Ladungen ergibt der klassische charged-Capture-Proxy ungefaehr:

```text
Q=3.67 e  -> 0.925 x neutral classical
Q=10 e    -> 0.799 x neutral classical
Q=24.18 e -> 0.531 x neutral classical
```

Der Wellenlauf und der unabhaengige klassisch-relativistische Benchmark stimmen damit in der Groessenordnung und insbesondere bei `~24 e` eng ueberein. Bei `Q=0` bleibt die bereits bekannte Dirac-Wellenabweichung vom klassischen Wert bestehen.

## 5. Physikalische Konsequenz

Positive Ladung unterdrueckt Protonen-Capture deutlich, aber fuer die plausiblen **unscreened benchmark charges** nicht um viele Groessenordnungen:

```text
few e     -> moderate suppression
~10 e     -> O(20-25%) reduction relative to neutral classical
~24 e     -> roughly factor-2 reduction
```

Damit ist Ladungsfeedback real und Pflichtbestandteil der Closure, aber es ist in diesem Modell **kein automatischer Protonen-Capture-Schalter auf null**.

## 6. Warum Q_eq noch nicht die Erdloesung ist

Die publizierten Gleichgewichtsladungen setzen diffuse Proton/Elektron-Plasmen bzw. vereinfachte stationaere Verteilungen voraus. Die dichte Fe/Ni-Umgebung besitzt dagegen

- starke Elektron-Ion-Kopplung,
- atomare/degenerierte elektronische Struktur,
- Screening,
- diskrete Ladungszustaende,
- Kerne mit `Z~26...28` statt unabhaengiger freier Protonen.

Schon ein einzelner ungescreenter Fe-Kern traegt `+26e`, also mehr als mehrere diffuse-plasma Gleichgewichtsskalen. Ein kontinuierliches `Q(t)` allein ist deshalb in der dichten Zone nicht ausreichend; eine diskrete Charge-State-/Transportbeschreibung ist physikalisch angemessener.

Schematisch kann die Ladungsverteilung durch eine Mastergleichung fuer ganzzahlige Zustande `P_N` beschrieben werden:

```text
dP_N/dt = Gamma_+(N-1) P_(N-1)
        + Gamma_-(N+1) P_(N+1)
        - [Gamma_+(N)+Gamma_-(N)] P_N.
```

Die Raten muessen aus der gescreenten lokalen Materie bestimmt werden.

## 7. Offener Elektronenkanal

Der Versuch, den gleichen endlichen lokalen In/Out-Matcher direkt auf Earth-speed-Elektronen zu uebertragen, besteht den neutralen Elektronenbenchmark **nicht**. Grund ist der extrem kleine asymptotische Impuls und die langreichweitige Coulomb-/Gravitationsphase.

Daher:

```text
charged proton Dirac proxy: PASS as controlled A-4 subtest
charged electron finite-radius local matcher: FAIL as numerical method
charged electron physical capture: OPEN
```

Fuer Elektronen ist ein explizites Coulomb-Fernfeldmatching erforderlich. Ein numerisch instabiler Wert wird nicht als Physikresultat verwendet.

## 8. A-4 Status

```text
Q=0 neutral regression: PASS
positive-Q proton suppression: CALCULATED
matching-radius stability: PASS at tested points
classical charged-orbit cross-check: CONSISTENT
RN metric correction at benchmark Q: negligible
continuous diffuse-plasma Q_eq -> dense Earth core: NOT TRANSFERABLE AS FINAL VALUE
charged electron Coulomb asymptotics: OPEN
```

**A-4-Fazit:** Ladungsfeedback veraendert die Teilchendynamik stark, liefert fuer Protonen aber im getesteten Benchmarkbereich keine Orders-of-Magnitude-Unterdrueckung. Die dichte Erdclosure muss Screening und diskrete Fe/Ni-Ladungszustaende explizit behandeln.

## Reproduzierbarkeit

- `stage3_69a4_charged_dirac_feedback.py`
- Vorstufen: `stage3_69a1_dirac_prototype.py`, `stage3_69a3_earth_proton_charge.py`

## Referenzen

- K. Nakao, K. Matsuo, H. Yoshino, H. Ishihara (2024), *Electrification of a non-rotating black hole*, arXiv:2409.17639.
- M. Zajacek et al. (2018), black-hole charge / surrounding plasma analysis.
- I. I. Cotaescu et al. (2016), partial-wave analysis of charged Dirac fermions in Reissner-Nordstroem backgrounds.
