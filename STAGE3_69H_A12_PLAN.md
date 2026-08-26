# Stage 3.69H / A12 – Tabulated WDM EOS/Zbar + Dissipative Transport + Shock Convergence

**Status:** NEXT BLOCK / DEFINED / NOT YET CALCULATED

## Ziel

A12 soll die beiden wichtigsten A11-Restunsicherheiten gemeinsam angreifen:

```text
real/tabulated Fe-Ni EOS + ionization
+ explicit dissipative transport
+ high-resolution shock convergence
-> dynamic species-aware Mdot_BH band.
```

## Pflichtmodule

### 1. EOS / Ionization

Mindestens tabellierte/interpolierte bzw. explizit markiert extrapolierte Felder

```text
P(rho,T)
E(rho,T)
Zbar(rho,T)
mu_e(rho,T)
```

mit first-principles-Daten wo verfuegbar.

Direkte Datenanker:

- Fe QMD / five-phase EOS;
- Blanchet et al. PRE 111, 015206 (2025), bis 47.2 g/cm3 und 1e9 K;
- pressure-ionization / dense-plasma average-ionization Literatur.

### 2. Dissipative PDE-Terme

```text
thermal conductivity
viscosity
ion diffusion
electron-ion relaxation
ion-ion relaxation
```

sollen als explizite Energie-/Impuls-/Species-Terme eingehen.

### 3. Species / Charge

Reduced advection mindestens fuer

```text
Fe/Ni ions
electrons
proton/nucleon sensitivity
Ye / charge-neutrality proxy.
```

Charged-electron far-field capture bleibt separat als Unsicherheitsband, falls der volle Coulomb-Matcher bis dahin nicht geloest ist.

### 4. Shock-Branch Konvergenz

Besonderer Fokus `M=1e10 kg` / fast-envelope high-supply.

Pflicht:

```text
N >= 128, 256, 512, 1024 sensitivity
longer t_end
shock position convergence
inner Mdot convergence
mass/energy residual audit.
```

### 5. Massenscan

```text
1e10 kg
1e11 kg
2e11 kg
5e11 kg.
```

## Acceptance Criteria

A12 gilt nur als numerisch geschlossen, wenn:

1. EOS/Zbar-Datenquellen und Extrapolationsbereiche explizit sichtbar sind;
2. dissipative Koeffizienten nicht als freie unbeschraenkte Faktoren eingesetzt werden;
3. `1e10 kg` Shock-Branch-Mdot mit Gitter/Zeitschritt konvergiert oder als nichtkonvergent falsifiziert wird;
4. `>=1e11 kg` supply-processing branch unter EOS-/Transportvariationen getestet ist;
5. Massenerhaltung und Energieaudit dokumentiert bleiben;
6. resultierendes `Mdot_BH` als Unsicherheitsband statt Einzelzahl ausgegeben wird;
7. keine numerische Kompatibilitaet als experimenteller Nachweis bezeichnet wird.

## Entscheidungslogik

```text
if A12 keeps >=1e11 kg on stable absorbing/supply-processing branch:
    A9-A11 matter-transport result is substantially hardened.

if realistic EOS/dissipation creates sustained backpressure there:
    Mdot must be revised downward.

if 1e10 kg converges to a stable shock-regulated solution:
    report its dynamic Mdot band rather than classifying it merely OPEN.
```
