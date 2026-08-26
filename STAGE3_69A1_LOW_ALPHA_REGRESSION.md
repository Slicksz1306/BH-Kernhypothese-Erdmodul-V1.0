# Stage 3.69A-1 – Low-alpha Dirac-Matching Regression

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** LOW-ALPHA ASYMPTOTIC MATCHING REGRESSION PASS / DENSE-EARTH CLOSURE OPEN

## Zweck

Dieser Regressionstest prueft ausschliesslich, ob der numerische Schwarzschild-Dirac-Solver die Fernfeld-In/Out-Koeffizienten korrekt genug extrahiert, um einen publizierten analytischen Grenzfall zu reproduzieren. Er ist **kein** Test einer Netto-Akkretionsrate im Erdzentrum.

Grundlage sind Doran, Lasenby, Dolan & Hinder (2005), insbesondere:

```text
U(r->infinity) = alpha_kappa U_in + beta_kappa U_out
sigma_abs = pi/[2 p (E-m)] * sum_(kappa != 0) |kappa|/|alpha_kappa|^2
```

und die von ihnen zitierte Unruh-Low-Energy-Naeherung.

## Testpunkt

```text
alpha = G M m/(hbar c) = 0.0025
E/m = 2.0
u = v/c = sqrt(3)/2 = 0.8660254038
kappa = -1,+1 only
```

Im kleinen-alpha-Regime dominieren nach Doran/Unruh die niedrigsten `|kappa|=1`-Partialwellen.

## Analytischer Referenzwert

Die Unruh/Doran-Naeherung ergibt

```text
sigma_Unruh / M^2 = 7.487924653281.
```

## Numerische Ergebnisse

DOP853 mit

```text
rtol = 1e-12
atol = 1e-14
```

und einer quadratischen `1/sqrt(x)`-Extrapolation der lokalen einlaufenden Amplitude im aeusseren Viertel des Integrationsintervalls liefert:

### x_max = 20 000

```text
sigma_num / M^2 = 7.502567618837
relative Abweichung zu Unruh = +0.195554 %

kappa=-1: |alpha_kappa| = 278.1737651422
          W_end = -0.9999999978754

kappa=+1: |alpha_kappa| = 160.5783000508
          W_end = -1.0000000002456
```

Groesste absolute Wronskian-Abweichung von `-1`:

```text
~2.13e-9.
```

### x_max = 40 000

```text
sigma_num / M^2 = 7.511515124475
relative Abweichung zu Unruh = +0.315047 %

kappa=-1: |alpha_kappa| = 278.0226063586
          W_end = -1.0000000109503

kappa=+1: |alpha_kappa| = 160.4798315844
          W_end = -1.0000000044365
```

Die Cross-Section aendert sich zwischen `x_max=20 000` und `40 000` nur um

```text
~0.1193 %.
```

Beide Werte liegen innerhalb `0.32 %` des publizierten analytischen Grenzfalls.

## Entscheidung

```text
Radiale Horizon->Fernfeld-Integration: PASS als Solver-Selfcheck.
Stromerhaltung im Regressionstest: PASS.
Asymptotische In/Out-Koeffizientenextraktion im getesteten low-alpha-Regime: PASS.
Unruh/Doran-Low-Energy-Regression: PASS (<0.32 %).
```

Das bedeutet **nicht**, dass die gesamte Doran-Kurve fuer alle `alpha`, Energien und Partialwellen bereits reproduziert ist. Insbesondere bleiben der Protonen-Uebergangsbereich `alpha~0.35...1`, hohe `|kappa|`, Ladungsfeedback und die dichte Fe/Ni-Transportclosure offen.

## Konsequenz fuer Stage 3.69A

Der offene numerische Kern ist jetzt enger:

```text
LOW-alpha single-fermion matching: validated
        -> intermediate-alpha proton scan: OPEN
        -> species/charge feedback: OPEN
        -> collisional/kinetic transport coupling: OPEN
        -> dense-core net Mdot_BH: OPEN
```

Der naechste harte Test ist deshalb ein Protonen-Massenscan durch den Bereich

```text
alpha_p ~ 0.1 ... 2
```

mit Partialwellenkonvergenz und Vergleich gegen den klassischen Grenzwert bei wachsendem `alpha`.

## Reproduzierbarkeit

Code:

- `stage3_69a1_lowalpha_regression.py`
- `stage3_69a1_dirac_prototype.py`

## Referenz

C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
