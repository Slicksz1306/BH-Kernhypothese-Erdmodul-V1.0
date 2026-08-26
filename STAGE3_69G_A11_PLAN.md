# Stage 3.69G / A11 – Time-Dependent WDM Partial-Sink PDE + EOS/Ionization Closure

**Status:** PARTIAL DYNAMIC CLOSURE CALCULATED / MASS-REGIME SPLIT REPRODUCED / FULL WDM EOS+Zbar STILL OPEN

## Ergebnis

A11 hat die A9/A10-Transporttrennung erstmals in einem zeitabhaengigen sphaerischen Finite-Volume-PDE-Test untersucht.

```text
outer supply
 -> spherical hydro
 -> partial inner sink
 -> self-generated pressure pile-up / shock
 -> dynamic Mdot_BH(t).
```

### Numerisch bestanden

- stationaerer absorbing-Bondi-Benchmark: PASS auf Prozentniveau;
- reflektierender Grenzfall: Backpressure/outward-shock Verhalten reproduziert;
- kontinuierliche partial-sink Randbedingung implementiert;
- finite-volume Massenerhaltung: Residuen ~1e-16...few 1e-15;
- Energieaudit inklusive Gravitationsquelle: Residuen ~1e-16...few 1e-15;
- EOS-Steifigkeits-Sensitivitaet `gamma=1.4,1.5,1.6` gerechnet.

### Fe-like Sink Sensitivitaet

Der A5-Wert `Fe-56 sigma/sigma_classical~0.99754` wird **nicht** mit einer PDE-Wandwahrscheinlichkeit gleichgesetzt. Als reine Sensitivitaet wurde jedoch `A=0.99754` getestet.

Bei `gamma=1.5` bleibt dieser Lauf praktisch auf dem voll absorbierenden Ast. Eine subprozentige kuenstliche Reflexion erzeugt im Reduced PDE keinen starken Backpressure-Branch.

### Dynamischer A10-Massensplit

A10 fast-envelope high-supply:

```text
M=1e10 kg: Xi_high~1.468 -> A_cap~0.681
M=1e11 kg: Xi_high~2.811e-3 -> A_cap=1
M=2e11 kg: Xi_high~4.278e-4 -> A_cap=1
M=5e11 kg: Xi_high~3.537e-5 -> A_cap=1.
```

Als Transport-Capacity-Sensitivitaet wird

```text
A_cap=min(1,1/Xi_high)
```

verwendet.

Ergebnis:

```text
1e10 kg:
    A_cap~0.681 erzeugt dynamischen Backpressure und stark reduzierten inneren Flux.

>=1e11 kg:
    kein Capacity-Limiter; PDE bleibt auf dem absorbierenden/supply-processing Ast.
```

Damit wird die A9/A10-Massentrennung dynamisch reproduziert.

## Wichtige offene Acceptance Criteria

A11 wird **nicht** als Full-WDM-PASS bezeichnet, weil folgende Punkte offen bleiben:

1. echte tabellierte `P(rho,T), E(rho,T), Zbar(rho,T)` ueber den gesamten Inward-Pfad;
2. explizite Waermeleitung, Viskositaet und e-i/i-i Relaxation in der PDE;
3. composition-/charge-resolved Advektion;
4. charged-electron Coulomb-Fernfeldmatcher;
5. hochaufgeloeste Gitter-/Langzeitkonvergenz der exakten `1e10 kg` Shock-Mdot.

Der `1e10 kg` Shockbranch zeigt bei `gamma=1.5`, `t=0.6 r_B/c_inf` fuer steigende Aufloesung weiterhin eine fallende innere Fluxfolge grob

```text
N=80  -> ~0.027
N=120 -> ~0.025
N=160 -> ~0.023
N=200 -> ~0.021
N=240 -> ~0.019.
```

Die Regimeentscheidung ist stabil, die stationaere Endrate noch nicht.

## Reproduzierbare Dateien

- `STAGE3_69G_A11_DYNAMIC_PARTIAL_SINK_PDE.md`
- `stage3_69g_a11_dynamic_partial_sink_pde.py`

## Naechster Block

Stage 3.69H/A12 soll die verbleibende Reduced-EOS-/Dissipationsluecke schliessen:

```text
tabulated Fe/Ni EOS + Zbar
+ thermal conductivity / viscosity / relaxation
+ high-resolution shock convergence
+ species/charge advection
-> dynamic Mdot band with explicit EOS uncertainty.
```

Kein A11-Solverresultat ist ein experimenteller Nachweis eines Erdzentrum-BH.
