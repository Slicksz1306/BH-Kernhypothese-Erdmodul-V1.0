# Stage 3.72 / A27 – Kollektive Quasineutralitäts- und Charge-Response-Audit

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** COLLECTIVE RESPONSE TIMESCALE CALCULATED / NAIVE A26 CHARGE BUILDUP NOT SELF-CONSISTENT / EXACT `Q_eq` OPEN

## Ziel

A26 zeigte, dass isolierte A5-Ionen- und A25-Elektronen-Cross-Sections nicht als zwei unabhängige homogene `n v sigma`-Ströme zu einer realen `Q(t)`-Entwicklung kombiniert werden dürfen.

A27 prüft den nächsten notwendigen Punkt:

```text
Reagiert das dichte leitfähige Elektronensystem schnell genug,
um den A26-Strom-Mismatch kollektiv zu verändern,
bevor mehrere Elementarladungen naiv akkumulieren?
```

Die Antwort ist im Outer-Core-Referenzzustand klar **ja**.

## Physikalische Closure-Struktur

Für ein leitfähiges quasineutrales Plasma gilt außerhalb einer dünnen Ladungs-/Screeningzone näherungsweise

```text
n_e ~= sum_i Z_i n_i
```

und die Elektronenimpulsbilanz / generalisierte Ohm-Struktur enthält insbesondere den Elektronendruckterm

```text
E + v x B ~= [j x B - grad(P_e)]/(n_e e) + dissipative terms.
```

Im unmagnetisierten radialen Reduced-Limit bedeutet dies schematisch

```text
E_r ~= -(1/(e n_e)) dP_e/dr + resistive/current terms.
```

Der relevante Punkt für A27 ist nicht eine bestimmte klassische Boltzmann-Closure, sondern dass der Elektronenstrom und das elektrische Feld **selbstkonsistent gekoppelt** sind. Die unabhängigen A26-Gasströme dürfen daher nicht unverändert weiterlaufen, wenn sich Ladung trennt.

Literaturanker:

- Fernsler, Slinker & Joyce, *Quasineutral plasma models*, Phys. Rev. E 71, 026401 (2005), DOI `10.1103/PhysRevE.71.026401`.
- Stanton & Murillo, *Unified description of linear screening in dense plasmas*, Phys. Rev. E 91, 033104 (2015), DOI `10.1103/PhysRevE.91.033104`.
- Simoni & Daligault, *First-Principles Determination of Electron-Ion Couplings in the Warm Dense Matter Regime*, Phys. Rev. Lett. 122, 205001 (2019), DOI `10.1103/PhysRevLett.122.205001`.
- Pozzo et al., *Thermal and electrical conductivity of iron at Earth's core conditions*, Nature 485, 355–358 (2012), DOI `10.1038/nature11031`.
- Recent liquid-core calculations continue to place metallic outer-core conductivities around `O(1e6 S/m)`; A27 uses `1e6 S/m` only as an order-of-magnitude outer benchmark, not as a radial conductivity law.

## A14/A26 Elektronendichte

Am PREM-Zentrumsreferenzpunkt:

```text
low-ionization endpoint, Zbar~2.76:
n_e ~3.88e29 m^-3

fully-ionized upper proxy:
n_e ~3.66e30 m^-3
```

Daraus folgt die nichtrelativistische Elektronen-Plasmafrequenz

```text
omega_pe = sqrt(n_e e^2/(epsilon0 m_e)).
```

### Low-ionization endpoint

```text
omega_pe ~3.51e16 s^-1
1/omega_pe ~2.85e-17 s
2pi/omega_pe ~1.79e-16 s.
```

### Fully-ionized upper proxy

```text
omega_pe ~1.08e17 s^-1
1/omega_pe ~9.27e-18 s
2pi/omega_pe ~5.82e-17 s.
```

Damit liegt die elementare kollektive Elektronen-Antwort im Bereich

```text
~1e-17 ... few 1e-16 s.
```

## Thomas-Fermi-Layer-Transit

A14/A25:

```text
lambda_TF ~2.95e-11 ... 4.29e-11 m
v_F       ~2.61e6 ... 5.52e6 m/s.
```

Ein einfacher Screening-Layer-Transit liefert

```text
t_TF = lambda_TF/v_F
     ~5.3e-18 ... 1.64e-17 s.
```

Dies liegt in derselben ultrakurzen Antwortklasse wie `1/omega_pe`.

## Maxwell-Relaxationsbenchmark

Für einen leitfähigen homogenen Medium-Proxy ist die Ladungsrelaxationszeit

```text
tau_M = epsilon0/sigma.
```

Mit dem bewusst groben Earth-core-Metallbenchmark

```text
sigma = 1e6 S/m
```

folgt

```text
tau_M ~8.85e-18 s.
```

A27 verwendet dies **nicht** als exakte BH-Ladezeit. Es ist ein Benchmark dafür, wie schnell ein makroskopischer elektrischer Ladungs-/Feldfehler in einem hochleitfähigen Medium elektromagnetisch und durch Leitungsstrom reorganisiert wird.

## Vergleich mit A26

A26s absichtlich naive unabhängige Gasstromclosure ergab für den Aufbau von `+5e`:

```text
low-Zbar endpoint:       ~5.4e-12 s
fully-ionized endpoint:  ~5.7e-13 s.
```

Gegen `tau_M`:

```text
5.4e-12 / 8.85e-18 ~6.1e5
5.7e-13 / 8.85e-18 ~6.4e4.
```

Der kollektive elektrische Zustand kann sich damit grob **10^5–10^6-mal schneller** reorganisieren, als A26s unabhängige Gasströme mehrere Elementarladungen aufbauen würden.

A23-Vergleich:

```text
tau_ei ~2.6e-12 s
```

ist ebenfalls etwa

```text
~2.9e5 tau_M.
```

Bei `M=1e11 kg`:

```text
r_B/c_eff ~5.87e-12 s
          ~6.6e5 tau_M.
```

Damit ist die elektrostatische/ambipolare Antwort deutlich schneller als die äußeren hydrodynamischen und Electron-Ion-Energieaustauschzeiten.

## Konsequenz für `Q(t)`

A27 erlaubt eine wichtige Reduktion der Full-WDM-Architektur:

```text
Q(t) ist auf Hydro-Zeitskalen keine frei langsam driftende Variable,
die aus zwei unveränderten unabhängigen Gasströmen integriert werden darf.
```

Stattdessen ist im Reduced-Quasineutralitätslimit sinnvoll:

```text
dQ/dt = I_i[Q,E,n_s,u_s,...] + I_e[Q,E,n_e,f_e,...]

mit schneller Feld-/Screening-Antwort
und näherungsweise quasi-statischem current-balance constraint

I_i + I_e ~= 0
```

auf Zeitskalen, die gegenüber der Hydrodynamik sehr kurz sind.

Das ist analog zur allgemeinen Idee eines floating/current-balance Zustands eines absorbierenden Objekts in Plasma, **aber klassische OML-/dust-grain Formeln werden hier nicht als gültige WDM-BH-Closure übernommen**. Der Projektbereich ist degeneriert, stark gekoppelt, stark gescreent und besitzt zusätzlich Gravitation und einen absorbierenden Horizont.

## Was dadurch geschlossen wird

```text
A26 independent-particle multi-e charge buildup before collective response:
REJECTED AS TIMESCALE-INCONSISTENT.

collective electrostatic response faster than hydro:
CALCULATED / STRONGLY SUPPORTED in outer reference state.

Q(t) treatment on hydro timescales:
REDUCED TO QUASI-STATIC COLLECTIVE CURRENT-BALANCE VARIABLE.
```

## Was weiterhin offen bleibt

A27 bestimmt **nicht** den exakten stationären Ladungswert.

Dafür fehlen weiterhin:

```text
nonlinear finite-T degenerate screening
radial lambda_screen(r,Q,T,X)
species mobilities / diffusion coefficients
ambipolar field through the real WDM mixture
ionization/composition evolution
collective sink/sheath boundary around the horizon
recycling + backpressure coupling
```

Daher:

```text
Q_eq = specific number of e:
NOT YET IDENTIFIED.
```

A14s `O(1...5e)` bleibt eine **nonlinear-response/screening scale**, nicht ein bewiesener Gleichgewichtswert.

## Beziehung zu A25

A25s flux-direct screened-electron S-Matrix bleibt ein gültiger **lokaler Einzelteilchen-Sink-Baustein**.

A27 zeigt, wie er in die nächste Ebene eingeordnet werden muss:

```text
A25 microscopic sink kernel
+ collective WDM transport / ambipolar field
+ fast quasineutral response
-> eventual Q_eq/current-balance closure.
```

## Beziehung zu A24 / finaler Mdot

Die A24-Aussage bleibt bestehen:

```text
final species-resolved Mdot_BH(t):
NOT YET IDENTIFIABLE.
```

Aber ein offener Freiheitsgrad wurde reduziert: `Q(t)` muss nicht als beliebig langsame unabhängige History-Funktion behandelt werden. Im äußeren dichten Kern reagiert das Plasma elektrostatisch extrem schnell gegenüber der Hydro-Zeit.

## Reproduzierbare Datei

- `stage3_72_a27_collective_charge_response.py`

## Schlussstatus

```text
A26 naive independent charge buildup:
SELF-CONSISTENCY FAIL + TIMESCALE FAIL.

collective charge/field response hierarchy:
CALCULATED.

quasineutral/ambipolar response before hydro evolution:
STRONGLY SUPPORTED in reduced outer-core benchmark.

exact nonlinear WDM floating charge Q_eq:
OPEN.

experimental BH detection:
NONE.
```
