# Stage 3.72 / A26 – Charge-current consistency audit

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** INDEPENDENT-PARTICLE `Q(t)` CLOSURE TESTED / SELF-CONSISTENCY FAIL / COLLECTIVE PLASMA CLOSURE REQUIRED

## Ziel

A25 liefert erstmals einen numerisch kontrollierten isolierten screened-electron Capture-Proxy. A26 prueft, ob man nun einfach

```text
ion capture current - electron capture current
```

bilden und daraus `Q(t)` ableiten darf.

Diese **naive unabhängige Teilchenclosure scheitert** deutlich.

Das ist ein Test der Closure, nicht der Hypothese selbst.

## Eingaben

A5 Fe-56 Referenz bei `M=1e11 kg`:

```text
n_i ~1.4075e29 m^-3
v_i ~1.04355e4 m/s
sigma_Fe ~2.28214e-22 m^2
```

Damit ergibt ein bewusst naiver homogener Einzelteilchenfluss

```text
Gamma_i = n_i v_i sigma_Fe ~3.35e11 ions/s.
```

A25 liefert fuer `Q=+5e`, mittleres `lambda_TF`, den `T=0`-Fermi-Sphere-Proxy `<sigma_e v>`.

## Low-ionization / A12b-A14 endpoint

```text
Zbar ~2.76
n_e ~3.88e29 m^-3
```

Naive positive Ladungszufuhr:

```text
Zbar Gamma_i ~9.25e11 e/s.
```

A25 isolierter Elektronenstrom bei `Q=+5e`:

```text
Gamma_e ~2.07e8 e/s.
```

Verhaeltnis:

```text
positive ion current / electron current ~4.47e3.
```

Ohne kollektive Gegenreaktion wuerde der naive Proxy `+5e` bereits in nur

```text
~5.4e-12 s
```

aufbauen.

## Fully-ionized upper proxy

```text
Z=26
n_e ~3.66e30 m^-3.
```

Naive positive Ladungszufuhr:

```text
~8.72e12 e/s.
```

A25 isolierter Elektronenstrom bei `Q=+5e`:

```text
~7.85e8 e/s.
```

Verhaeltnis:

```text
positive ion current / electron current ~1.11e4.
```

Naive `+5e`-Aufbauzeit:

```text
~5.7e-13 s.
```

## Warum das kein riesiges reales Q beweist

Diese Rechnung nimmt absichtlich eine **inkonsistente unabhängige Gasbeschreibung**:

- A5 isolierte Fe-Capture-Cross-Section;
- A25 isolierte Elektronen-Cross-Section;
- homogene `n v sigma`-Fluesse;
- keine kollektive Quasineutralitaet;
- keine ambipolaren elektrischen Felder;
- keine radiale/nonlineare Screening-Antwort;
- kein Recycling-/Bulk-Flow-Coupling.

Gerade in einem dichten, stark gekoppelten, gescreenten Plasma sind diese Teilstroeme nicht frei voneinander waehlbar.

Daher bedeutet der starke Strom-Mismatch **nicht**:

```text
actual BH charge >>5e
```

sondern:

```text
independent-particle current balance is not a self-consistent dense-core Q(t) model.
```

## Beziehung zu A14

A14s `Q~O(1...5e)` war ein **screened electrostatic response scale**, kein bereits geloester stationaerer Ladungszustand.

A26 praezisiert diese Aussage:

```text
A14 Q scale:
useful nonlinear-response / screening scale
NOT established equilibrium charge.
```

## Beziehung zu A25

A25 bleibt ein numerisch kontrollierter isolierter screened-electron S-Matrix-Proxy. A26 zeigt aber, dass selbst ein guter Einzelteilchen-Solver nicht automatisch die kollektive Dense-Matter-Chargeentwicklung schliesst.

## Erforderliche Q(t)-Closure

Mindestens noetig sind:

```text
bulk quasineutral continuity for ions + electrons
ambipolar electric field / electrochemical potential
nonlinear and radial screening
species-resolved advection + diffusion
recycling/permanent escape
ionization/composition evolution
screened electron and ion sink currents
Q(t) coupled back to all species
```

## Konsequenz fuer finale Mdot

A24 wird dadurch bestaetigt:

```text
final species-resolved Mdot_BH(t):
NOT YET IDENTIFIABLE.
```

Denn `Q(t)` kann nicht durch das einfache Subtrahieren isolierter A5/A25-Ströme ersetzt werden.

## Reproduzierbare Datei

- `stage3_72_a26_charge_current_consistency.py`

## Schlussstatus

```text
naive independent ion/electron current balance:
CALCULATED / SELF-CONSISTENCY FAIL.

huge actual BH charge:
NOT ESTABLISHED.

collective dense-plasma Q(t):
REQUIRED / OPEN.

A25 isolated screened electron solver:
RETAINED as partial input.
```
