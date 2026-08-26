# Stage 3.69H / A12 – Tabulated WDM EOS/Zbar + Dissipative Transport + Shock Convergence

**Stand:** 26.08.2026  
**Status:** PARTIAL CALCULATED / SHOCK+TRANSPORT AUDIT DONE / TABULATED EOS+ZBAR DISSIPATIVE CLOSURE OPEN

## Ziel

A12 greift die zwei wichtigsten A11-Restunsicherheiten an:

```text
real/tabulated Fe-Ni EOS + ionization
+ explicit dissipative transport
+ high-resolution shock convergence
-> dynamic species-aware Mdot_BH band.
```

## Bereits in A12 gerechnet

- Literaturkorrektur Wang 2014 -> Sjostrom/Crockett 2018 high-pressure EOS revision;
- Fe/FeNi-Transportanker aus outer-core QMD/first-principles Literatur;
- Bondi-scale Reynolds-/Peclet-Massenscan `1e10...5e11 kg`;
- `1e10 kg` Shock-Konvergenz `N=128,256,512,1024`;
- long-domain Shock-Propagation bis `t=2 r_B/c_inf`;
- Mass-/Energieaudit weiterhin auf Rundungsniveau.

Zentrale neue Aussage:

```text
1e10 kg capacity-limited branch:
    outward-propagating backpressure shock
    NOT a demonstrated stationary shock-regulated Mdot.

>=1e11 kg:
    A10/A11 supply-processing branch survives the new transport-timescale audit.
```

## Pflichtmodule – Status

### 1. EOS / Ionization

Direkte Datenanker:

- Sjostrom & Crockett 2018 five-phase/QMD Fe EOS;
- Blanchet et al. PRE 111, 015206 (2025), bis `47.2 g/cm3` und `1e9 K`;
- liquid-Fe thermodynamic data/`Cp` near core conditions.

```text
P(rho,T): PARTIAL literature domain known; numerical table not yet imported
E(rho,T): PARTIAL literature domain known; numerical table not yet imported
Zbar(rho,T): OPEN as a reusable numerical table
mu_e(rho,T): OPEN as a reusable numerical table
```

Keine erfundene `Zbar`-Tabelle wird eingesetzt.

### 2. Dissipative PDE-Terme

Literaturgebundene Transportzahlen sind gerechnet. Physikalische

```text
thermal conductivity
viscosity
electron-ion relaxation
```

werden aber noch nicht direkt an die A11-Gamma-Energiegleichung gekoppelt, weil dort keine thermodynamisch konsistente physische `T(rho,e)`-Variable existiert.

```text
consistent dissipative PDE: OPEN
```

### 3. Species / Charge

```text
Fe/Ni/e-/p reduced advection: OPEN
charged-electron far-field capture: OPEN
```

### 4. Shock-Branch Konvergenz

Erledigt bis `N=1024` fuer den zentralen `1e10 kg` Capacity-Limit-Test.

Bei `t=0.8 r_B/c_inf`:

```text
N=128  shock~1.269 r_B, inner mdot~2.1e-2
N=256  shock~1.254 r_B, inner mdot~1.63e-2
N=512  shock~1.233 r_B, inner mdot~1.12e-2
N=1024 shock~1.229 r_B, inner mdot~6.94e-3
```

Shock-Lage konvergiert; stationaere endliche innere `Mdot` nicht.

Long-domain:

```text
t=0.8 -> rshock~1.26 r_B
t=1.2 -> ~1.74 r_B
t=1.6 -> ~2.22 r_B
t=2.0 -> ~2.68 r_B
```

=> outward-propagating Backpressure, nicht stationaerer Shock.

### 5. Massenscan

Transportzahlen:

```text
M=1e10 kg: Re~32...98, Pe~8...11
M=1e11 kg: Re~322...985, Pe~82...106
M=2e11 kg: Re~644...1970, Pe~164...212
M=5e11 kg: Re~1610...4924, Pe~409...531
```

Dissipation ist relativ am wichtigsten am `1e10 kg`-Unterrand.

## Acceptance Criteria – aktueller Stand

1. EOS/Zbar Quellen/Extrapolation sichtbar: **PARTIAL PASS**
2. Dissipative Koeffizienten nicht frei: **PASS fuer Audit / PDE-Einbau OPEN**
3. `1e10 kg` Shock-Mdot konvergiert oder Nichtkonvergenz gezeigt: **PASS – stationaere Endrate nicht etabliert**
4. `>=1e11 kg` unter Transportvariationen getestet: **PARTIAL PASS**
5. Mass-/Energieaudit: **PASS im aktuellen Euler-PDE**
6. Mdot als Unsicherheitsband: **OPEN fuer Full dissipative closure**
7. keine Kompatibilitaet als Nachweis: **PASS**

## Naechster Unterblock: A12b

```text
thermodynamically consistent Fe EOS table
+ T(rho,e) inversion
+ bounded Zbar(rho,T)
+ physical viscosity / conduction / e-i relaxation
+ repeat dynamic 1e10 and >=1e11 scans
```

A12 bleibt bis dahin PARTIAL; Stage 3.69 Full-Multiphysics bleibt OPEN.
