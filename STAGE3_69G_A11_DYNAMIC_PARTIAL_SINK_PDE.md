# Stage 3.69G / A11 – Time-Dependent Partial-Sink PDE + EOS-Stiffness Envelope

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** PARTIAL DYNAMIC CLOSURE CALCULATED / A9-A10 MASS-REGIME SPLIT DYNAMICALLY REPRODUCED / FULL TABULATED WDM EOS+Zbar STILL OPEN

## Ziel

A11 testet die in A9/A10 gefundene Transporttrennung erstmals zeitabhaengig:

```text
outer supply
 -> spherical hydro
 -> partial inner sink
 -> self-generated pressure pile-up / shock
 -> dynamic Mdot_BH(t).
```

Der entscheidende Punkt ist, dass Backpressure nicht als freie Unterdrueckung eingesetzt wird. Sie muss aus der PDE entstehen.

## 1. Literatur-/EOS-Anker

Die Datenbasis bleibt bewusst zweigeteilt.

### Direkt first-principles abgedeckter Bereich

Blanchet et al., Phys. Rev. E 111, 015206 (2025), liefern Fe-EOS von

```text
rho = 7.874 ... 47.2 g/cm3
T   = 5500 K ... 1e9 K.
```

Wang et al., Phys. Rev. E 89, 023101 (2014), liefern WDM-Fe QMD-Transport fuer etwa

```text
rho = 12.5 ... 25 g/cm3
T   = 0.5 ... 15 eV.
```

Fe-Ni-QMD unter Erdkernbedingungen liefert Diffusionskoeffizienten um `few 1e-9 m2/s` und Viskositaeten im Bereich weniger mPa s.

### Noch nicht direkt abgedeckter Bereich

Der A8/A10 Reduced-Inward-Pfad steigt viel tiefer als diese publizierten Tabellen. Deshalb wird in A11 **kein erfundener full-Zbar(rho,T)-Datensatz** behauptet.

Stattdessen verwendet die PDE zunaechst einen transparenten EOS-Steifigkeits-Envelop

```text
gamma = 1.4, 1.5, 1.6
```

als Sensitivitaet. Die volle tabellierte Fe/Ni-EOS-/Ionisationsclosure bleibt Acceptance-Criterion OPEN.

## 2. PDE

Verwendet wird die sphaerische Euler-Gleichung in Bondi-Einheiten:

```text
partial_t rho + 1/r^2 partial_r(r^2 rho u) = 0

partial_t(rho u)
 + 1/r^2 partial_r[r^2(rho u^2+P)]
 = 2P/r - rho/r^2

partial_t E
 + 1/r^2 partial_r[r^2 u(E+P)]
 = -rho u/r^2.
```

Der Solver ist finite-volume, HLL, logarithmisches radiales Gitter.

### Partial inner sink

A11 ersetzt den binaeren A7-Rand durch

```text
F_inner = A * F_absorb + (1-A) * F_reflect,
```

mit `A in [0,1]`.

**Wichtig:** `A` ist eine PDE-Sensitivitaet und nicht automatisch identisch mit einer mikroskopischen Wave-Capture-Cross-Section.

## 3. Regressionen

### Absorbing Bondi

Fuer `gamma=1.5` gilt analytisch

```text
lambda_B = 0.5.
```

Der numerische Flux bei `r~r_B` liegt im kontrollierten Lauf bei etwa

```text
0.501 ... 0.503
```

zu fruehen Benchmarkzeiten und bleibt damit auf Prozentniveau beim analytischen Wert.

### Reflecting

Der reflektierende Grenzfall reproduziert den A7-Befund: innerer Massenfluss bricht zusammen, Dichte/Druck stauen sich und ein nach aussen laufender Backpressure-/Shock-Zweig entsteht.

Dies ist konsistent mit der bekannten starken Abhaengigkeit sphaerischer Akkretion von der inneren Randbedingung; reflektierende Oberflaechen koennen outward shocks erzeugen, waehrend ein BH-Sink den transsonischen Zufluss erhaelt.

## 4. Fe-like Partial-Sink Sensitivitaet

A5 ergab bei `M=1e11 kg` fuer coherent Fe-56

```text
sigma/sigma_classical ~0.99754.
```

Dieser Wert wird **nicht** als exakte PDE-Boundary-Probability identifiziert. Er wird lediglich als konservativer Fe-like Sensitivitaetswert `A=0.99754` getestet.

Bei `gamma=1.5` bleibt der Lauf fuer `A=0.99754` bis `t=2 r_B/c_inf` praktisch auf demselben inneren Flux wie `A=1`.

Im EOS-Steifigkeits-Envelop:

```text
gamma=1.4: A=0.9975 praktisch absorbierend
gamma=1.5: A=0.9975 praktisch absorbierend
gamma=1.6: etwas hoehere Sensitivitaet, aber weiterhin kein reflecting-artiger Kollaps.
```

Damit erzeugt eine nur subprozentige kuenstliche Reflexion in diesem Reduced PDE keinen starken Backpressure-Ast.

## 5. A10-Massenclosure als dynamischer Capacity-Limiter

A10 liefert fuer den schnellsten/escape-freundlichsten Transportenvelop am oberen Supply:

```text
M=1e10 kg: Xi_high = 1.468
M=1e11 kg: Xi_high = 2.811e-3
M=2e11 kg: Xi_high = 4.278e-4
M=5e11 kg: Xi_high = 3.537e-5.
```

Als **Transport-Capacity-Sensitivitaet**, nicht als mikroskopischer Capturefaktor, wird definiert

```text
A_cap = min(1, 1/Xi_high).
```

Damit:

```text
1e10 kg: A_cap ~0.681
>=1e11 kg: A_cap = 1.
```

### `1e10 kg`, fast-envelope high-supply

Der dynamische Lauf mit `A~0.681` bildet von selbst einen Backpressure-Zweig.

Bei `gamma=1.5`, `t=1 r_B/c_inf` liegt der innere dimensionslose Flux nur noch grob bei

```text
~0.02
```

gegen `~0.41 ... 0.44` im absorbierenden Lauf derselben Diskretisierung/Zeit.

Das ist eine starke dynamische Unterdrueckung, **aber noch keine konvergierte stationaere Endrate**. Schocklage und innerer Flux zeigen weiterhin Aufloesungssensitivitaet.

### `M>=1e11 kg`

Da A10 fuer diese Massen `Xi_high <<1` liefert, setzt die Capacity-Closure keinen partiellen Sink:

```text
A_cap=1.
```

Der A11-Lauf verbleibt deshalb auf dem absorbierenden/supply-processing Ast.

Damit wird der A9/A10 Massensplit dynamisch reproduziert:

```text
1e10 kg:
    backpressure-sensitive / dynamic suppression branch possible

>=1e11 kg:
    no capacity-driven backpressure in the current Reduced closure.
```

## 6. Massenerhaltung und Energieaudit

Der Finite-Volume-Solver bilanziert explizit

```text
Delta M + integrated boundary mass flux
```

und

```text
Delta E + integrated boundary energy flux - integrated gravity source.
```

Fuer die getesteten `N=80...240`-Laeufe liegen die diskreten relativen Residuen typisch bei

```text
mass:   ~1e-16 ... few 1e-15
energy: ~1e-16 ... few 1e-15.
```

Damit ist die konservative Buchhaltung selbst numerisch sauber.

## 7. Gitterkonvergenz – wichtiger offener Punkt

Absorbierende und Fe-like nahezu absorbierende Laeufe sind stabil.

Der `1e10 kg / A~0.681`-Shockbranch zeigt bei `t=0.6` fuer `gamma=1.5` noch sichtbare Aufloesungsabhaengigkeit des inneren Fluxes:

```text
N=80:  ~0.027
N=120: ~0.025
N=160: ~0.023
N=200: ~0.021
N=240: ~0.019.
```

Die Richtung ist konsistent (starker Backpressure), aber eine stationaere extrapolierte `Mdot` wird noch **nicht** als konvergiert behauptet.

Daher:

```text
A11 dynamic regime split: CALCULATED
A11 exact shock-branch Mdot: OPEN
A11 full tabulated WDM EOS/Zbar: OPEN.
```

## 8. Physikalische Konsequenz

A11 staerkt einen sehr konkreten Punkt:

```text
Backpressure kann die Rate stark reduzieren,
aber nur wenn die Transport-/Processing-Kapazitaet den Supply tatsaechlich nicht aufnehmen kann.
```

Im aktuellen A10-Envelope trifft das nur den empfindlichen `~1e10 kg`-Unterbereich.

Fuer `>=1e11 kg` entsteht im Reduced Modell kein kuenstlicher Reflexionsbedarf, weil die Processing Capacity deutlich oberhalb des Supply liegt.

## 9. Aussagegrenze

A11 ist **keine** finale Earth-core-Akkretionssimulation.

Noch offen:

- echte tabellierte `P(rho,T), E(rho,T), Zbar(rho,T)` ueber den gesamten Inward-Pfad;
- Waermeleitung und Viskositaet als explizite PDE-Terme;
- electron-ion / ion-ion Relaxation in der Energiegleichung;
- charged-electron Coulomb-Fernfeldmatcher;
- composition-/charge-resolved Fe/Ni/e/p Advektion;
- hochaufgeloeste Shock-Konvergenz fuer den `1e10 kg`-Branch.

Kein Solver-PASS ist ein experimenteller Nachweis eines Erdzentrum-BH.

## 10. Status

```text
absorbing Bondi regression: PASS
reflecting backpressure regression: PASS qualitatively/numerically
partial-sink interpolation: CALCULATED
finite-volume mass conservation: PASS
finite-volume energy accounting: PASS
Fe-like ~0.9975 sensitivity: remains near absorbing branch
A10 1e10 capacity-limited branch: dynamic backpressure found
>=1e11 A10 capacity branch: remains absorbing/supply-processing
exact shock-branch Mdot convergence: OPEN
full WDM EOS/Zbar PDE: OPEN
Stage 3.69 Full-Multiphysics: OPEN.
```
