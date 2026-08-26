# Stage 3.69A-1 – Intermediate-alpha Transition Scan

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** QUALITATIVE/NUMERICAL TRANSITION BENCHMARK PASS / FULL PUBLISHED-CURVE REGRESSION OPEN

## Zweck

Dieser Test prueft bei festem `u=0.5`, ob der numerische Schwarzschild-Dirac-Matcher im Uebergang von kleinen zu groesseren gravitativen Kopplungen die von Doran et al. publizierte Struktur zeigt:

```text
intermediate alpha -> quantenmechanisches Ueber-/Unterschwingen um klassisch
wachsendes alpha   -> Annaeherung an klassische Punktteilchen-Capture.
```

Dies ist absichtlich **kein Erdgeschwindigkeitswert** und noch keine dichte Fe/Ni-Nettoakkretion.

## Numerische Filterung

Die Partialwellensumme verwendet nur Moden, fuer die

```text
|W_end + 1| < 1e-4
```

und eine physikalische Absorptionswahrscheinlichkeit `0 <= P_abs <= 1` vorliegt. Numerisch instabile sehr hohe `|kappa|`-Tail-Moden werden verworfen; ihre berechnete physikalische Absorption ist im gewaehlt konvergierten `kmax` bereits sehr klein.

Der klassische Referenzwert bei `u=0.5` ist

```text
sigma_classical / M^2 = 243.6908897541.
```

## Ergebnisse

### alpha = 0.2

```text
x_match=500:  sigma/M^2 = 253.8887859923 = 1.041848 x klassisch
x_match=1000: sigma/M^2 = 254.2743618748 = 1.043430 x klassisch
```

Matchingradius-Variation: etwa `0.152 %`.

### alpha = 0.35

```text
x_match=500:  sigma/M^2 = 227.7519037534 = 0.934593 x klassisch
x_match=1000: sigma/M^2 = 227.8655068440 = 0.935060 x klassisch
```

Matchingradius-Variation: etwa `0.050 %`.

### alpha = 0.7

```text
x_match=500:  sigma/M^2 = 237.6437273015 = 0.975186 x klassisch
x_match=1000: sigma/M^2 = 237.6288421706 = 0.975124 x klassisch
```

Matchingradius-Variation: etwa `0.006 %`.

## Physikalische Struktur

Die drei Punkte zeigen:

```text
alpha=0.2  -> ~4.2 % ueber klassisch
alpha=0.35 -> ~6.5 % unter klassisch
alpha=0.7  -> ~2.5 % unter klassisch
```

Damit reproduziert der Solver die von Doran et al. erwartete **oszillatorische Abweichung um den klassischen Grenzwert** und eine Annaeherung an diesen Grenzwert mit wachsender Kopplung.

## Aussagegrenze

```text
qualitative Doran-Uebergangsstruktur: PASS
Matchingradius-Stabilitaet der getesteten Summen: PASS
vollstaendige digitale Regression gegen publizierte Doran-Figur: OPEN
Earth proton u~3.48e-5 full numerical matching: OPEN
```

Die extrem kleine Erdgeschwindigkeit darf nicht einfach durch `u=0.5` ersetzt werden. Der Test validiert nur das Verhalten des numerischen Capture-Moduls im `alpha`-Uebergang.

## Reproduzierbarkeit

Code:

- `stage3_69a1_transition_scan.py`
- `stage3_69a1_dirac_prototype.py`

## Referenz

C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
