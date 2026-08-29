# Stage 3.72 / A25 – Flux-direct screened-electron Dirac prototype

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** FLUX-DIRECT ELECTRON SOLVER REGRESSION PASS / STATIC-SCREENED Q-SCAN CALCULATED / FULL COLLECTIVE `Q(t)` OPEN

## Motivation

A21 zeigte, dass der A4-Proton-Matcher fuer Earth-speed-Elektronen numerisch ungeeignet ist, weil die neutrale Absorptionswahrscheinlichkeit nur `O(1e-11)` betraegt und die Bildung

```text
P_abs = 1 - |S|^2
```

katastrophale Subtraktion erzeugt.

A25 ersetzt diese Auswertung durch einen **flux-direct** Ansatz.

Der regulaere Horizon-Modus wird auf

```text
W_H = -1
```

normiert. Nach logarithmisch renormalisierter radialer Integration wird nur der einlaufende Koeffizient `A_in` bestimmt. Die Absorption folgt direkt aus

```text
P_abs = (-W_H) / [(-W_in) |A_in|^2]
```

unter Rueckrechnung der Segment-Normierungen.

Damit wird `1-|S|^2` nicht mehr gebildet.

## Potentialmodell

A25 verwendet fuer ein Elektron um ein positiv geladenes BH einen endlichen Yukawa-Screening-Proxy

```text
V_C(r) proportional -Q exp(-r/lambda_TF)/r.
```

A14-Bracket:

```text
lambda_TF ~2.95e-11 ... 4.29e-11 m.
```

Wichtig: `lambda_TF` wird in A25 als **konstante Sensitivitaet** gehalten. Eine radiale, nichtlineare, dynamische Plasma-Screening-Closure ist damit nicht ersetzt.

Der Scan wird deshalb auf

```text
Q = 0 ... +5 e
```

beschraenkt. Groessere Ladungen liegen ausserhalb des bevorzugten A14-Linearresponse-/Screening-Brackets und werden nicht als physikalische Vorhersage verwendet.

## Elektronengeschwindigkeit korrigiert

Fuer Dense-Core-Elektronen ist `c_eff~10 km/s` nicht die bevorzugte Geschwindigkeitsverteilung.

A14 lieferte

```text
E_F ~19.4 ... 86.6 eV
```

und damit im nichtrelativistischen Fermi-Proxy

```text
v_F ~2.61e6 ... 5.52e6 m/s.
```

A25 testet sowohl Earth-speed als harte numerische Low-p-Regression als auch diese beiden Fermi-Endpunkte.

## Neutraler Unruh-Benchmark

Bei `M_BH=1e11 kg`:

### Earth-speed

```text
v = 10.4355 km/s
Unruh target sigma/M^2 ~6.26574e6
flux-direct result      ~6.26058e6
relative drift          ~-8.2e-4
```

### Low-Fermi endpoint

```text
v_F ~2.612e6 m/s
Unruh target sigma/M^2 ~772.219
flux-direct result      ~772.533
relative drift          ~+4.1e-4
```

### High-Fermi endpoint

```text
v_F ~5.519e6 m/s
Unruh target sigma/M^2 ~352.612
flux-direct result      ~352.655
relative drift          ~+1.2e-4
```

Damit gilt:

```text
neutral flux-direct electron regression: PASS
```

im definierten A25-Toleranzniveau von `~1e-3`.

## Partialwellen

Im getesteten `Q<=5`- und Fermi-Speed-Bereich dominiert `|kappa|=1` stark. `|kappa|=2,3` liegen viele Groessenordnungen darunter und aendern die angegebene Cross-Section nicht relevant.

## Matchingradius-Konvergenz

Representative `Q=5`, mittleres `lambda_TF`:

- bei `v_F~2.61e6 m/s` aendert sich die resultierende Cross-Section beim Matchingradius-Scan von etwa `1e7` bis `1e8` in der Groessenordnung weniger Promille bis wenige `1e-3`;
- bei `v_F~5.52e6 m/s` ist die Stabilitaet vergleichbar oder besser.

A21s Konditionierungsproblem ist damit durch die flux-direct Formulierung numerisch deutlich entschaerft.

## Static-screened Q-Scan

Ausgewiesen ist das Verhaeltnis zur neutralen isolierten Elektronen-Cross-Section.

### `v_F ~2.61e6 m/s`

Ueber den A14-Screeningbereich (inklusive mittlerem Sensitivitaetspunkt):

| Q | sigma_e(Q)/sigma_e(0) |
|---:|---:|
| `+1e` | `~4.57 ... 4.97` |
| `+2e` | `~10.20 ... 11.34` |
| `+3e` | `~14.29 ... 14.60` |
| `+4e` | `~18.39 ... 20.54` |
| `+5e` | `~25.65 ... 26.90` |

### `v_F ~5.52e6 m/s`

| Q | sigma_e(Q)/sigma_e(0) |
|---:|---:|
| `+1e` | `~2.47 ... 2.55` |
| `+2e` | `~4.88 ... 4.90` |
| `+3e` | `~7.42 ... 7.50` |
| `+4e` | `~9.95 ... 9.96` |
| `+5e` | `~12.52 ... 12.62` |

Positive BH-Ladung zieht Elektronen an und erhoeht die isolierte Capture-Cross-Section im getesteten Screening-Proxy wie physikalisch erwartet.

## Degenerierter Fermi-Sphere-Proxy

A25 enthaelt zusaetzlich einen `T=0` Fermi-Sphere-Quadraturproxy fuer

```text
<sigma v> = integral f_F(v) sigma(v) v dv.
```

Am mittleren `lambda_TF` ergibt sich relativ zum neutralen Wert ungefaehr:

### Low-Fermi endpoint

```text
Q=+1e -> ~8.34 x
Q=+3e -> ~17.8 x
Q=+5e -> ~46.3 x
```

### High-Fermi endpoint

```text
Q=+1e -> ~3.70 x
Q=+3e -> ~10.4 x
Q=+5e -> ~19.7 x
```

Dies ist ein **isolierter degenerierter Teilchenflux-Proxy**, keine kollektive Plasma-Netto-Capture-Rate.

## Was A25 korrigiert

A21 hatte den vollen Elektronenkanal wegen Solver-Konditionierung offen gelassen. A25 zeigt nun:

```text
flux-direct isolated screened-electron S-matrix:
NUMERICALLY TRACTABLE / PARTIAL CALCULATED.
```

Der alte Satz

```text
charged-electron S-matrix completely numerically inaccessible
```

waere damit zu stark und wird praezisiert.

## Was weiterhin offen bleibt

A25 schliesst **nicht** die Dense-Core-Charge-Kinetik. Dafuer fehlen unter anderem:

```text
lambda_TF(r,t,Q)
nonlinear screening at larger potential
collective quasineutral plasma response
actual finite-T Fermi-Dirac distribution
bulk advection + recycling
species-resolved ion currents
stochastic Q(t)
```

Insbesondere darf aus einer isolierten Cross-Section nicht direkt

```text
Gamma_e = n_e <sigma v>
```

gegen einen unabhaengigen Ionengasstrom bilanziert werden, ohne das kollektive quasineutrale WDM-Transportproblem zu loesen.

## Konsequenz fuer A14/A24

A14 bleibt qualitativ gehaertet:

- ein positives `Q=O(1...5 e)` erzeugt starke **anziehende** Elektronen-Rueckkopplung;
- gleichzeitig zeigte A4 in diesem Q-Bereich nur order-unity Protonensuppression;
- kein großer statischer Protonenblocker wurde gefunden.

A24 bleibt ebenfalls gueltig:

```text
final Q(t) and final species-resolved Mdot_BH(t):
NOT YET IDENTIFIABLE.
```

A25 reduziert aber eine der offenen numerischen Unsicherheiten erheblich.

## Reproduzierbare Datei

- `stage3_72_a25_flux_direct_screened_electron.py`

## Schlussstatus

```text
flux-direct electron numerical architecture:
PASS regression.

static Yukawa screened Q<=5 S-matrix proxy:
CALCULATED.

Fermi-speed sensitivity:
CALCULATED.

radial/nonlinear collective screening:
OPEN.

stochastic dense-plasma Q(t):
OPEN.

final electron contribution to Mdot_BH:
OPEN / coupled Full-WDM problem.
```
