# Stage 3.72 / A29 – Nichtlineares TF-Screening -> flux-direct Elektronen-Dirac

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** NONLINEAR SCREENING RECOUPLED TO ELECTRON DIRAC / A25 STATIC-Q CONCLUSION ROBUST / COLLECTIVE `Q_eq` OPEN

## Ziel

A28 zeigte, dass der A25-lineare Yukawa-Screening-Proxy bei `Q=1...5e` bereits teilweise bis stark nichtlinear ist.

A29 prüft daher direkt:

```text
A28 nonlinear relativistic TF phi(r)
-> A25 flux-direct Dirac electron sink
-> revised sigma_e(Q).
```

Damit wird getestet, ob die starke positive-Q-Elektronenfokussierung aus A25 nur ein Artefakt des linearen Yukawa-Profils war.

## Numerische Kopplung

A28 liefert

```text
psi(r) = e phi(r)/E_F.
```

Im A25-Doran/Dirac-System wird daraus der dimensionslose lokale Energie-Shift

```text
delta E = alpha_e [E_F/(m_e c^2)] psi(r).
```

Der Horizon-Modus bleibt auf direkten radialen Fluss normiert und die Absorption wird weiterhin ohne die schlecht konditionierte Subtraktion

```text
1-|S|^2
```

ausgewertet.

Der Test verwendet die beiden A14/A25-Fermi-Endpunkte und `Q=1,3,5e`. `|kappa|=1` dominiert in diesem Bereich bereits in A25.

## Neutraler Referenzpunkt

Die neutrale Architektur ist identisch mit A25 und behält dessen Low-Energy-Unruh-Regression bei.

Die hier relevante Größe ist daher das Verhältnis

```text
sigma_e(Q)/sigma_e(0)
```

und der direkte Vergleich

```text
nonlinear-TF / linear-Yukawa.
```

## Low-Fermi Endpoint

```text
E_F ~19.4 eV
v_F ~2.61e6 m/s
lambda_TF ~4.292e-11 m.
```

| Q | linear Yukawa / neutral | nonlinear TF / neutral | nonlinear / linear |
|---:|---:|---:|---:|
| `+1e` | `~4.972` | `~4.675` | `~0.940` |
| `+3e` | `~14.594` | `~14.661` | `~1.005` |
| `+5e` | `~26.399` | `~25.526` | `~0.967` |

Maximale Abweichung in diesem Endpoint-Subset:

```text
~6 %.
```

## High-Fermi Endpoint

```text
E_F ~86.6 eV
v_F ~5.52e6 m/s
lambda_TF ~2.952e-11 m.
```

| Q | linear Yukawa / neutral | nonlinear TF / neutral | nonlinear / linear |
|---:|---:|---:|---:|
| `+1e` | `~2.468` | `~2.422` | `~0.982` |
| `+3e` | `~7.502` | `~7.430` | `~0.990` |
| `+5e` | `~12.521` | `~12.483` | `~0.997` |

Hier ist die nichtlineare Screeningkorrektur im getesteten Endpoint-Scan sogar kleiner als etwa `2 %`.

## Zentrale Erkenntnis

Obwohl A28 das statische Potential bei `r~lambda_TF` deutlich verändert, wird die A25-Elektronencapture nicht um Größenordnungen verschoben.

Im getesteten `Q<=5e`-Bereich gilt:

```text
nonlinear TF screening correction to endpoint-vF electron capture:
O(few percent).
```

Damit überlebt die zentrale A25-Aussage:

```text
positive BH charge strongly enhances isolated electron capture.
```

Sie ist im getesteten statischen Screeningbereich **nicht** nur ein Artefakt des linearen Yukawa-Potentials.

## Warum die Cross-Section robuster ist als phi(lambda)

A28 zeigte bei `r~lambda_TF` Potentialkorrekturen bis zu rund `31 %`. Die Dirac-Capture reagiert jedoch auf das gesamte radiale Potential und besonders auf den inneren Bereich, wo das Feld des zentralen positiven Ladungssinks wieder näher an die bare-Coulomb-Struktur heranläuft.

Daher muss eine lokale Potentialänderung am Screeningradius nicht proportional in die gesamte Absorptions-Cross-Section eingehen.

## Was A29 schließt

```text
A25 linear-Yukawa shape uncertainty as potential orders-of-magnitude electron-capture error:
NOT SUPPORTED.

static nonlinear-TF recoupling:
CALCULATED.

A25 positive-Q electron focusing:
ROBUST in tested Q<=5 endpoint-speed bracket.
```

## Was weiterhin offen bleibt

A29 ist weiterhin ein **statischer Einzelteilchen-Sinktest**.

Nicht enthalten:

```text
finite-T full Fermi-Dirac current integral with nonlinear TF profile
real Fe-Ni-light-element collective transport
ambipolar field under finite radial current
ion motion / strong ion correlations in the screening cloud
path-dependent Te/Ti
nonlinear current-carrying screening
self-consistent floating/current-balance Q_eq.
```

A27 bleibt daher für die Gesamtarchitektur entscheidend:

```text
Q_eq must come from collective current balance,
not from isolated cross sections alone.
```

## Konsequenz für A24

Die finale `Mdot_BH(t)` bleibt noch nicht eindeutig identifizierbar. A29 reduziert jedoch eine weitere numerische Unsicherheit:

```text
screened electron microscopic sink kernel:
substantially hardened.
```

Der nächste echte Engpass liegt nun stärker bei

```text
collective WDM mobility/current closure
+ mixture EOS/transport
+ current-balance Q_eq
```

und weniger bei der isolierten Elektronen-Dirac-Numerik.

## Reproduzierbare Datei

- `stage3_72_a29_nonlinear_tf_dirac_recoupling.py`

## Schlussstatus

```text
A28 nonlinear TF -> A25 flux-direct Dirac:
CALCULATED.

static-screening model sensitivity of sigma_e for Q<=5:
FEW-PERCENT LEVEL in tested endpoint-vF scan.

positive-Q electron focusing:
RETAINED / ROBUST IN TESTED STATIC BRACKET.

exact collective Q_eq:
OPEN.

final species-resolved Mdot_BH(t):
OPEN.

experimental BH detection:
NONE.
```
