# Stage 3.72 / A23 – Two-temperature + weak-reaction timescale gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** TIMESCALE GATE CALCULATED / UNIVERSAL `Te=Ti` CLOSURE REJECTED / PROMPT WEAK EQUILIBRIUM NOT SUPPORTED

## Primaerer WDM-Fe-Anker

Fernandez-Panella et al., *Reduction of electron-phonon coupling in warm dense iron*, Phys. Rev. B 101, 184309 (2020), untersuchen experimentell und mit DFT/Two-Temperature-Modellen die Elektron-Ion-Relaxation in warm-densem Eisen.

Die Arbeit zeigt:

- `G` sowie die thermophysikalischen Parameter muessen von `Te` **und** `Ti` abhaengig behandelt werden;
- ein konstantes low-temperature `G` beschreibt den WDM-Zerfall nicht;
- bei ihrem warm-dense Fe-Zustand liegt die charakteristische Relaxationszeit bei

```text
tau_ei ~2.6 +/-0.1 ps
```

mit einer modellierten Vergleichszeit von etwa `2.0 +/-0.1 ps`.

Diese Laborzeit wird in A23 **nicht** unkontrolliert auf hohe Dichten oder den gesamten BH-Inflow extrapoliert. Sie dient nur als publizierter Outer-/near-solid-density-Zeitskalenanker.

## Outer crossing comparison

Mit

```text
r_B = G M / c_eff^2
c_eff = 10.4355 km/s
t_cross = r_B/c_eff
```

folgt:

| M_BH | r_B [m] | t_cross [s] | tau_ei/t_cross |
|---:|---:|---:|---:|
| `1e10 kg` | `6.129e-9` | `5.873e-13` | `4.43` |
| `1e11 kg` | `6.129e-8` | `5.873e-12` | `0.443` |
| `2e11 kg` | `1.226e-7` | `1.175e-11` | `0.221` |
| `5e11 kg` | `3.064e-7` | `2.937e-11` | `0.0885` |

## Interpretation

### `1e10 kg`

Der experimentelle WDM-Fe-Relaxationsanker ist **laenger** als die einfache `r_B/c_eff`-Crossing-Zeit.

```text
advection can outrun this laboratory relaxation scale
```

Damit ist ein universelles `Te=Ti` gerade im low-mass/high-throughput-Uebergangsbereich nicht gerechtfertigt.

### `1e11...5e11 kg`

Der gleiche Laboranker ist kuerzer als die Outer-Crossing-Zeit. Eine lokale Temperaturangleichung ist daher im Outer-Bereich **timescale-plausibel**, aber nicht bewiesen, weil reale `G(rho,Te,Ti,X)`-Werte fuer die jeweilige Mischung fehlen.

Daher gilt fuer alle Massen:

```text
Te=Ti everywhere -> REJECTED as universal assumption
explicit Te/Ti sensitivity -> REQUIRED for Full-WDM closure
```

## Deep weak-reaction gate

A8/A9 hatten fuer `M=1e11 kg` im schnellen Reduced-Branch an den energetischen Electron-Capture-Schwellen:

```text
Ni threshold:
  t_res ~9.13e-14 s
  lambda_required ~1.10e13 s^-1

Fe threshold:
  t_res ~1.50e-17 s
  lambda_required ~6.67e16 s^-1
```

Der bereits verwendete aggressive publizierte `56Fe`-EC-Benchmark liegt bei

```text
lambda_ec ~1.5916e4 s^-1
tau_ec ~6.283e-5 s.
```

Am Fe-Gate:

```text
lambda_ec/lambda_required ~2.39e-13

tau_ec/t_res ~4.19e12.
```

Damit bleibt die fruehere Korrektur sehr robust:

```text
energetic EC threshold open != prompt weak equilibrium
```

Im schnellen Inflow ist promptes Weak-Equilibrium durch diesen Benchmark nicht unterstuetzt.

## Was bei Backpressure anders ist

A11/A12 zeigen, dass bei ueberlasteter Processing-Capacity ein Reservoir/Backpressure entstehen kann. Dann kann die Residence-Zeit stark gegenueber dem schnellen Transit wachsen.

Deshalb darf aus dem schnellen A23-Gate **nicht** geschlossen werden, dass schwache Reaktionen niemals relevant werden.

```text
fast through-flow: prompt weak processing NOT SUPPORTED
stalled/backpressure reservoir: weak processing OPEN
```

## Full-WDM-Anforderung nach A23

Eine finale Zwei-Temperatur-/Reaktionsclosure braucht entlang des tatsaechlichen radialen Pfades mindestens:

```text
G(rho,Te,Ti,X)
Ce(rho,Te,Ti,X)
Ci(rho,Te,Ti,X)
Ke/Ki(rho,Te,Ti,X)
Ye(t,r)
reaction network rates(rho,Te,Ti,composition)
```

plus die A22-Mischungs-EOS.

## Reproduzierbare Datei

- `stage3_72_a23_two_temperature_reaction_gate.py`

## A23 Schlussstatus

```text
Outer Te/Ti timescale comparison:
COMPLETE / CALCULATED.

Universal one-temperature assumption:
REJECTED.

Prompt weak equilibrium in fast A8/A9 branch:
NOT SUPPORTED.

Weak processing in stalled/backpressure branch:
OPEN.

Full two-temperature mixture reaction network:
OPEN / upstream data dependent.
```
