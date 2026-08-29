# Stage 3.72 / A21 – Screened-electron Dirac matcher conditioning audit

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** CONDITIONING CALCULATED / EXISTING A4 MATCHER NOT CONTROLLED FOR EARTH-SPEED ELECTRONS / FULL S-MATRIX OPEN

## Ziel

A14 hat die bevorzugte Dense-Core-Ladung auf grob `Q=O(1...5 e)` eingeengt. A21 prueft, ob der vorhandene finite-radius charged-Dirac-Matcher aus A4 fuer den Elektronenkanal einfach wiederverwendet werden kann.

Antwort:

```text
Nein – nicht kontrolliert.
```

Der Grund ist numerische Konditionierung bei extrem kleinem asymptotischem Elektronenimpuls, nicht ein physikalischer Beweis fuer oder gegen Elektronencapture.

## Earth-speed Elektronenskalen bei `M_BH=1e11 kg`

```text
v = 10.4355 km/s
u = v/c ~3.4809e-5
alpha_e = G M m_e/(hbar c) ~1.92308e-4
pM ~6.69407e-9
r_g = GM/c^2 ~7.42616e-17 m
```

Reduzierte de-Broglie-Laenge:

```text
lambda_db = hbar/(m_e v) ~1.10936e-8 m.
```

A14 Thomas-Fermi-Screening:

```text
lambda_TF ~2.95e-11 ... 4.29e-11 m
x_TF=lambda_TF/r_g ~3.97e5 ... 5.78e5
lambda_TF/lambda_db ~0.00266 ... 0.00387.
```

Der elektrostatische Anteil ist damit im dichten Kern ein **kurzreichweitiger** Potentialanteil relativ zur Elektronen-De-Broglie-Laenge.

## Schwarzschild-Fernfeldproblem

Im A1/A4-Asymptotikterm tritt ein gravitativer Phasendrift `~E sqrt(2/x)` auf. Damit dieser kleiner als der winzige asymptotische Impuls `p` wird, braucht man grob

```text
x >> 2/u^2 ~1.65e9.
```

Der Screeningbereich selbst endet bereits um `x~few 1e5`, aber der gravitative In/Out-Matcher muss viel weiter hinaus stabil bleiben.

## Neutraler Kalibrationsmaßstab

Der bekannte neutrale Low-E-Unruh-Benchmark ergibt bei Earth-speed:

```text
sigma/M^2 ~6.26574e6
leading |kappa|=1 absorption sum ~8.94e-11
per leading kappa P_abs ~4.47e-11.
```

Damit muesste ein Verfahren, das

```text
P_abs = 1 - |S|^2
```

direkt bildet, eine Reflexion extrem nahe bei eins auf besser als etwa `1e-11` stabil aufloesen – zusaetzlich ueber sehr grosse Matchingradien und nahezu degenerierte In/Out-Moden.

Das ist nicht die Regimeklasse, fuer die der A4-Proton-Matcher gebaut und validiert wurde. Dort waren die interessierenden Absorptions-/Chargeeffekte `O(1)`.

## A21 Befund

```text
naive reuse of A4 proton finite-radius matcher for electrons:
REJECTED AS NUMERICALLY UNCONTROLLED
```

Das ist **kein** Nachweis, dass Elektronencapture klein oder gross ist. Es bedeutet nur, dass ein instabiles `1-|S|^2`-Ergebnis wissenschaftlich nicht verwendet werden darf.

## Erforderliche Architektur fuer den echten Abschluss

Ein kontrollierter Elektronenmatcher braucht mindestens:

1. flux-direct Jost-, Riccati- oder Log-Derivative-Formulierung;
2. finite-range screened Coulomb potential statt ungeschirmtem Coulomb-Fernfeld;
3. neutralen Earth-speed-Unruh-Benchmark als Regression;
4. Matchingradius-Konvergenz weit jenseits der Screeningzone;
5. erhoehte Praezision bzw. eine Formulierung ohne katastrophale Subtraktion;
6. erst danach `Q=O(1...5 e)`-Scan.

## Physikalische Einordnung

A14 bleibt als Dense-Core-Screening-Bracket gueltig:

```text
large electrostatic proton blocker: NOT FOUND.
```

A21 aendert diese Aussage nicht. Es verhindert lediglich, dass der noch offene Elektronen-S-Matrix-Kanal mit einem numerisch ungeeigneten Solver scheinbar geschlossen wird.

## Reproduzierbare Datei

- `stage3_72_a21_electron_matcher_conditioning.py`

## Schlussstatus

```text
Electron scale/conditioning audit:
COMPLETE / CALCULATED.

A4 matcher reuse for Earth-speed electrons:
REJECTED AS UNCONTROLLED.

Full screened-electron Dirac S-matrix:
OPEN.

Dense-core Q~O(1...5 e) bracket from A14:
remains PARTIAL / physically motivated.
```
