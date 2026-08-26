# Stage 3.69H / A12 – Tabulated WDM EOS/Zbar + Dissipative Transport + Shock Convergence

**Stand:** 26.08.2026  
**Status:** PARTIAL CALCULATED THROUGH A12b / SHOCK+TRANSPORT+ZBAR SENSITIVITY DONE / FULL THERMODYNAMIC WDM CLOSURE OPEN

## Ziel

A12 greift die wichtigsten A11-Restunsicherheiten an:

```text
Fe/Ni EOS + ionization
+ explicit dissipative transport
+ high-resolution shock convergence
-> dynamic species-aware Mdot_BH band.
```

## A12 – bereits gerechnet

- Literaturkorrektur Wang 2014 -> Sjostrom/Crockett 2018 high-pressure EOS revision;
- Fe/FeNi-Transportanker aus outer-core QMD/first-principles Literatur;
- Bondi-scale Reynolds-/Peclet-Massenscan `1e10...5e11 kg`;
- `1e10 kg` Shock-Konvergenz `N=128,256,512,1024`;
- long-domain Shock-Propagation bis `t=2 r_B/c_inf`;
- Mass-/Energieaudit auf Rundungsniveau.

A12-Hauptbefund:

```text
1e10 kg capacity-limited branch:
    outward-propagating backpressure shock
    NOT a demonstrated stationary shock-regulated Mdot.

>=1e11 kg:
    current reduced supply-processing branch survives transport-timescale audit.
```

## A12b – neu gerechnet

### 1. Bounded Zbar closure

A12b implementiert den analytischen More/Thomas-Fermi-Fit fuer `Zbar(rho,T)` mit dem publizierten Fe-Low-T-Korrekturfaktor

```text
factor_Fe = 0.270.
```

Bei der Erdkernreferenz

```text
rho=13.0885 g/cm3
T=6000 K
```

folgt

```text
Zbar_Fe ~2.761.
```

Gegen eine publizierte solid-density Average-Atom-Definition `Z_WS,2` liegt der korrigierte More-Fit im Bereich `0.1...10 eV` etwa `12...16 %` niedriger. Diese Differenz wird als systematische Definition-/Modellunsicherheit behalten.

### 2. Reduced inward Zbar map

```text
x=1       -> Zbar~2.76
x=0.65    -> ~3.83
x=0.425   -> ~5.15
x=0.1     -> ~10.99
x=0.01    -> ~19.23
x=1e-3    -> ~23.28
x=1e-4    -> ~25.06
```

Tief innen ist das eine TF-Extrapolation, keine direkte DFT-MD-Tabelle.

### 3. Physische Viskositaet/Waermeleitung im PDE-Sensitivitaetstest

A12b koppelt die dokumentierten Bereiche

```text
eta=8.5...26 mPa s
k=67...87 W/m/K
Cp=850 J/kg/K
```

explizit als radiale Newtonsche Spannung und Waermefluss in den kontrollierten A11-Gamma-PDE-Solver.

Beim `1e10 kg` Capacity-Branch (`A_cap~0.681`) bleibt der outward/backpressure Ast fuer inviscid, weak-dissipation und strong-dissipation Tests qualitativ erhalten.

Beispiel `N=64, t=0.8 r_B/c_inf`:

```text
inviscid:             shock~1.39 r_B, inner flux~0.0241
Re=98.5, Pe=10.62:    shock~1.39 r_B, inner flux~0.0243
Re=32.2, Pe=8.18:     shock~1.39 r_B, inner flux~0.0241
```

Bei `t=0.6` und staerkerer Dissipation:

```text
N=80 -> shock~1.083 r_B, inner flux~0.0276
N=96 -> shock~1.059 r_B, inner flux~0.0271.
```

```text
literature-scale eta/k do not remove the 1e10-kg backpressure branch
in this reduced dissipative sensitivity.
```

### 4. >=1e11 kg

Da Re/Pe mit `r_B` wachsen und A10/A11 dort bereits `Xi_high<<1` ergaben, findet A12b keinen neuen dissipativen Mechanismus, der den aktuellen Reduced supply-processing Ast automatisch umkehrt.

## Acceptance Criteria – aktueller Stand

1. EOS/Zbar Quellen und Extrapolation sichtbar: **PARTIAL PASS**
2. reusable bounded `Zbar(rho,T)` closure: **CALCULATED via More/TF fit**
3. dissipative Koeffizienten nicht frei: **PASS fuer eta/k sensitivity**
4. physische eta/k direkt im PDE: **PARTIAL PASS im Gamma-EOS-Surrogat**
5. `1e10 kg` Backpressure unter eta/k: **SURVIVES**
6. `>=1e11 kg` supply-processing unter eta/k scaling: **SURVIVES REDUCED AUDIT**
7. full `P(rho,T),E(rho,T),mu_e(rho,T)` table: **OPEN**
8. thermodynamically exact `T(rho,e)` Fe/Ni inversion: **OPEN**
9. electron-ion relaxation in two-temperature PDE: **OPEN**
10. species-resolved final Mdot band: **OPEN**

## Naechster Unterblock: A12c

```text
Mie-Gruneisen / tabulated-Fe thermodynamic surrogate
+ explicit T(rho,e) inversion
+ More/AA Zbar uncertainty band
+ two-temperature electron/ion relaxation bracket
+ viscosity / conduction on the physical temperature field
+ repeat 1e10, 1e11, 2e11, 5e11 dynamic scan
```

A12 bleibt PARTIAL; Stage 3.69 Full-Multiphysics bleibt OPEN.
