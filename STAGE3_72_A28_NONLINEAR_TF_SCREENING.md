# Stage 3.72 / A28 – Nichtlineares relativistisches Thomas-Fermi-Screening

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** NONLINEAR STATIC SCREENING PROFILE CALCULATED / LINEAR YUKAWA REFINED / EXACT FLOATING `Q_eq` OPEN

## Ziel

A25 verwendete für den Elektronen-Dirac-Solver einen konstanten linearen Yukawa-Screening-Proxy

```text
phi(r) ~ Q exp(-r/lambda_TF)/r.
```

A27 zeigte anschließend, dass die elektrostatische Antwort des dichten Elektronensystems extrem schnell ist. Damit ist als nächster Schritt sinnvoll zu prüfen, ob der A14/A25-Bereich `Q=1...5e` überhaupt noch in linearer Thomas-Fermi-Antwort liegt.

A28 löst deshalb eine **sphärische nichtlineare relativistische Thomas-Fermi-Poisson-Closure** für einen positiven Punktladungssink in einem uniformen positiven Ionenhintergrund.

Sie bestimmt **nicht** den stationären BH-Ladungswert. Sie härtet nur die statische Screeningstruktur.

## Electron EOS im Screening-Layer

Für ein bei `T=0` degeneriertes Elektronengas wird die elektrochemische Bedingung verwendet

```text
sqrt(p_F(r)^2 c^2 + m_e^2 c^4) - e phi(r)
    = sqrt(p_F0^2 c^2 + m_e^2 c^4).
```

Mit

```text
psi = e phi / E_F
mu0 = 1 + E_F/(m_e c^2)
```

folgt

```text
n_e(psi)/n_e0 = [ ((mu0 + eps psi)^2 - 1)/(mu0^2 - 1) ]^(3/2)
```

mit

```text
eps = E_F/(m_e c^2).
```

Damit bleibt die Elektronendichte auch bei größeren lokalen Potentialen relativistisch konsistent; die nichtrelativistische `n~(1+psi)^(3/2)`-Form ist nur der kleine-`eps` Grenzfall.

## Nichtlineare Poisson-Gleichung

Außerhalb der Punktladung gilt im statischen Ionenbackground

```text
n_i Z = n_e0
```

und

```text
nabla^2 phi = e [n_e(phi)-n_e0]/epsilon0.
```

Der Radialsolver erzwingt am Innenrand den Punktladungsfluss

```text
-4 pi epsilon0 r^2 dphi/dr -> Q e
```

und außen

```text
phi -> 0.
```

Die linearisierte Länge des Solvers reproduziert die A14-TF-Endpunkte:

```text
low-Zbar endpoint:
lambda_TF ~4.292e-11 m

fully-ionized upper endpoint:
lambda_TF ~2.952e-11 m.
```

Literaturkontext für Dense-Plasma-Screening:

- Stanton & Murillo, *Unified description of linear screening in dense plasmas*, Phys. Rev. E 91, 033104 (2015), DOI `10.1103/PhysRevE.91.033104`.
- Ichimaru, *Strongly coupled plasmas: high-density classical plasmas and degenerate electron liquids*, Rev. Mod. Phys. 54, 1017 (1982), DOI `10.1103/RevModPhys.54.1017`.
- Moldabekov et al., *Structural characteristics of strongly coupled ions in a dense quantum plasma*, Phys. Rev. E 98, 023207 (2018), DOI `10.1103/PhysRevE.98.023207`.

## Low-Zbar Endpoint

Eingabe:

```text
n_e ~3.88e29 m^-3
E_F ~19.4 eV
lambda_TF ~4.292e-11 m.
```

Am Radius `r=lambda_TF`:

| Q | `psi=e phi/E_F` | `n_e/n_e0` | Potential relativ zu linear-Yukawa |
|---:|---:|---:|---:|
| `1e` | `0.560` | `1.95` | `0.880` |
| `2e` | `1.034` | `2.90` | `0.812` |
| `3e` | `1.457` | `3.85` | `0.763` |
| `4e` | `1.845` | `4.80` | `0.725` |
| `5e` | `2.207` | `5.74` | `0.694` |

Damit ist bereits `Q=1...5e` deutlich nichtlinear. Insbesondere bei `+5e` ist die lokale Elektronendichte am linearen Screeningradius in diesem statischen Proxy fast sechsfach erhöht.

Für `Q=5e` bleibt vom ursprünglichen eingeschlossenen Punktladungsfluss nur noch

```text
50% bei r ~1.11 lambda_TF
10% bei r ~3.33 lambda_TF
1%  bei r ~6.13 lambda_TF.
```

In Metern:

```text
r_50 ~4.78e-11 m
r_90screen ~1.43e-10 m
r_99screen ~2.63e-10 m.
```

## Fully-ionized Upper Endpoint

Eingabe:

```text
n_e ~3.66e30 m^-3
E_F ~86.6 eV
lambda_TF ~2.952e-11 m.
```

Am Radius `r=lambda_TF`:

| Q | `psi` | `n_e/n_e0` | Potential relativ zu linear-Yukawa |
|---:|---:|---:|---:|
| `1e` | `0.197` | `1.31` | `0.949` |
| `2e` | `0.378` | `1.62` | `0.912` |
| `3e` | `0.548` | `1.93` | `0.882` |
| `4e` | `0.710` | `2.24` | `0.856` |
| `5e` | `0.864` | `2.55` | `0.834` |

Auch hier ist die Antwort bei mehreren Elementarladungen nicht mehr streng linear, aber schwächer nichtlinear als am niedrigen Fermi-Energie-Endpunkt.

Für `Q=5e`:

```text
50% remaining charge: r ~1.38 lambda_TF ~4.08e-11 m
10% remaining:        r ~3.62 lambda_TF ~1.07e-10 m
1% remaining:         r ~6.39 lambda_TF ~1.89e-10 m.
```

## Zentrale Erkenntnis

A14s Bereich `O(1...5e)` war zu Recht als **nonlinear-response/screening scale** und nicht als bewiesener Gleichgewichtswert zu verstehen.

A28 zeigt jetzt quantitativ:

```text
Q=1...5e:
already partially to strongly nonlinear in the TF electron response.
```

Der lineare A25-Yukawa-Proxy überschätzt das Potential bei `r~lambda_TF` im getesteten Bereich um etwa

```text
~5% ... 31%
```

je nach Endpoint und Q.

Die erhöhte Elektronendichte schirmt größere positive Ladung **stärker** ab als die lineare Yukawa-Antwort.

## Was A28 nicht bedeutet

A28 beweist nicht

```text
Q_eq = 1...5e.
```

Der BH könnte prinzipiell einen anderen Nettoladungszustand besitzen, während das umgebende Plasma einen starken neutralisierenden Screening-Cloud bildet.

Der Gleichgewichtswert verlangt weiterhin den gekoppelten Stromabschluss aus A27:

```text
I_i(Q,phi,n_s,u_s,...) + I_e(Q,phi,f_e,...) = 0
```

mit realem WDM-Transport.

## Offene Korrekturen

Der A28-Solver enthält noch nicht:

```text
finite-T Fermi-Dirac electrons
exchange-correlation corrections
strong ion correlations in the Poisson response
ion motion during slower evolution
real Fe-Ni-light-element mixture
path-dependent Te/Ti
recycling/backpressure
self-consistent current-carrying nonequilibrium screening.
```

Der Solver ist daher ein **static nonlinear screening proxy**, kein finales WDM-Sheath-Modell.

## Beziehung zu A25

A25 bleibt numerisch wertvoll, aber sein statisches lineares Yukawa-Potential ist jetzt als Sensitivitätsmodell eingeordnet.

Der nächste kontrollierte Elektronenschritt kann A25s flux-direct Dirac-Solver mit dem A28-nichtlinearen Potentialprofil koppeln:

```text
A28 nonlinear phi(r)
-> A25 flux-direct Dirac sink
-> revised sigma_e(Q)
```

Das würde einen weiteren offenen numerischen Unsicherheitsanteil reduzieren, ohne schon die kollektive `Q_eq`-Closure zu behaupten.

## Reproduzierbare Datei

- `stage3_72_a28_nonlinear_tf_screening.py`

## Schlussstatus

```text
linear TF/Yukawa at Q=1...5e:
REFINED / PARTLY NONLINEAR.

static relativistic nonlinear TF screening:
CALCULATED.

screening cloud size:
O(few lambda_TF) / CALCULATED.

exact collective floating Q_eq:
OPEN.

next controlled step:
nonlinear-TF profile -> flux-direct Dirac recoupling.

experimental BH detection:
NONE.
```
