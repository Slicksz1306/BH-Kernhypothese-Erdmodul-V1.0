# Stage 3.69H / A12 – WDM EOS/Zbar, Dissipation und Supply-Rekalibrierung

**Stand:** 26.08.2026  
**Status:** PARTIAL CALCULATED THROUGH A12c / INNER TRANSPORT HARDENED / OUTER SUPPLY REOPENED AS EOS-SENSITIVE

## Ziel

A12 haertet gleichzeitig den inneren Transport und den aeusseren Supply:

```text
Fe/Ni EOS + ionization
+ dissipative transport
+ high-resolution backpressure tests
+ relativistic stiff-EOS Michel supply
-> dynamic Mdot_BH band.
```

## A12 – Shock/Transport Audit

Erledigt:

- Literaturkorrektur Wang 2014 -> Sjostrom/Crockett 2018;
- Fe/FeNi-Transportanker aus first-principles/QMD Literatur;
- Bondi-scale Reynolds-/Peclet-Massenscan `1e10...5e11 kg`;
- `1e10 kg` Shock-Konvergenz `N=128,256,512,1024`;
- long-domain Shock-Propagation bis `t=2 r_B/c_inf`;
- Mass-/Energieaudit auf Rundungsniveau.

A12-Befund unter dem **historischen hohen Supply**:

```text
1e10 kg:
    outward-propagating backpressure shock
    no demonstrated stationary shock-regulated Mdot

>=1e11 kg:
    reduced supply-processing branch survives transport-timescale audit.
```

## A12b – Zbar + dissipative sensitivity

### Bounded Zbar

A12b implementiert den More/Thomas-Fermi-Fit fuer `Zbar(rho,T)` mit dem publizierten Fe-Low-T-Korrekturfaktor

```text
factor_Fe = 0.270.
```

Erdkernreferenz:

```text
rho=13.0885 g/cm3
T=6000 K
Zbar_Fe~2.761.
```

Gegen eine publizierte solid-density Average-Atom-Definition liegt der korrigierte More-Fit bei `0.1...10 eV` etwa `12...16 %` niedriger. Diese Definition-/Modellunsicherheit bleibt sichtbar.

Reduced inward map:

```text
x=1       -> Zbar~2.76
x=0.65    -> ~3.83
x=0.425   -> ~5.15
x=0.1     -> ~10.99
x=0.01    -> ~19.23
x=1e-3    -> ~23.28
x=1e-4    -> ~25.06
```

Tief innen ist dies eine TF-Extrapolation, keine direkte DFT-MD-Tabelle.

### eta/k in der PDE

Literaturgebundene Bereiche

```text
eta=8.5...26 mPa s
k=67...87 W/m/K
Cp=850 J/kg/K
```

wurden als radiale Newtonsche Spannung und Waermefluss in den kontrollierten Gamma-PDE-Solver gekoppelt.

Unter dem historischen `1e10 kg` Capacity-Limiter bleibt der outward/backpressure Ast qualitativ erhalten. Die realistischen eta/k-Werte entfernen den Backpressure-Ast in diesem Reduced Test nicht.

## A12c – relativistische stiff-EOS Supply-Rekalibrierung

A12c korrigiert einen wichtigeren Punkt: Der historische Michel-Supply ist selbst stark EOS-abhaengig.

PREM-Zentrum:

```text
rho       ~13.08848 g/cm3
Kappa_S   ~1.4253 TPa
Pressure  ~363.852 GPa
dK/dP     ~2.356
c_eff     ~10.4355 km/s.
```

Fuer einen **lokalen** Polytropen ist `dK/dP=Gamma`. Daher ist `Gamma~2.356` ein lokaler Stiffness-Proxy, aber keine globale Fe-EOS bis zum Horizon.

Fuer `Gamma>5/3` wird die volle relativistische Michel-Kritikalitaet verwendet; die Newton-Bondi-Grenze ist dort nicht zulaessig.

Bei `M=1e11 kg` ergibt der konstante-Gamma GR-Sensitivitaetsscan ungefaehr:

| Gamma | Mdot [kg/s] |
|---:|---:|
| `1.75` | `1.19e-7` |
| `1.80` | `2.89e-8` |
| `1.85` | `8.02e-9` |
| `2.00` | `3.35e-10` |
| `2.20` | `1.50e-11` |
| `2.356` local PREM proxy | `2.40e-12` |

Der historische Projektbereich

```text
1.47e-8 ... 1.46e-7 kg/s
```

entspricht im einfachen konstanten-Gamma GR-Surrogat etwa

```text
Gamma ~1.743 ... 1.826.
```

Damit gilt ab A12c:

```text
historical Michel supply = LEGACY / EOS-SENSITIVE BENCHMARK
not a universal outer-supply rate.
```

### Konsequenz fuer 1e10 kg

Der bisherige A10-fast Wert

```text
Xi_high(1e10)~1.468
```

war an den historischen hohen/soft-EOS Supply gekoppelt.

Mit stiff-EOS GR-Supply sinkt `Xi` stark:

```text
Gamma=1.80  -> Xi~0.29
Gamma=1.85  -> Xi~0.081
Gamma=2.00  -> Xi~0.0034
Gamma=2.356 -> Xi~2.4e-5.
```

Im einfachen konstanten-Gamma Vergleich liegt `Xi=1` bei etwa

```text
Gamma~1.756.
```

Daher wird die fruehere Kurzform

```text
1e10 kg -> dynamic backpressure
```

korrigiert zu

```text
1e10 kg -> backpressure CONDITIONAL on sufficiently high/soft-EOS supply.
           A stiff-EOS supply can remove the capacity overload.
```

### Konsequenz fuer >=1e11 kg

Eine niedrigere reale Supply-Rate macht den bereits gefundenen processing-capable Ast nicht schwieriger, sondern leichter:

```text
>=1e11 kg inner processing capability:
SURVIVES / STRENGTHENED under lower stiff-EOS supply.
```

Das liefert noch keine finale Netto-Mdot.

## Acceptance Criteria – aktueller Stand

1. WDM/EOS Quellen sichtbar: **PARTIAL PASS**
2. bounded `Zbar(rho,T)` closure: **CALCULATED via More/TF**
3. eta/k nicht frei: **PASS fuer sensitivity**
4. eta/k in Reduced PDE: **PARTIAL PASS**
5. high-resolution 1e10 shock regime: **CALCULATED**
6. stationary 1e10 shock Mdot: **NOT ESTABLISHED**
7. relativistischer stiff-EOS Supply: **CALCULATED als constant-Gamma sensitivity**
8. historical Michel benchmark universell: **REJECTED / DOWNGRADED TO LEGACY**
9. full general-EOS relativistic Michel supply: **OPEN**
10. full `P(rho,T), E(rho,T), mu_e(rho,T)` table: **OPEN**
11. two-temperature e-i relaxation: **OPEN**
12. final species-resolved net Mdot: **OPEN**

## Naechster Pflichtblock – Stage 3.69I / A13

```text
PREM outer state
-> piecewise/general Fe/Ni EOS
-> P(rho,T), E(rho,T), T(rho,e)
-> bounded Zbar uncertainty
-> relativistic Michel critical point with variable EOS
-> Mdot_supply(EOS)
-> A9-A12 transport/capture sink
-> final reduced net-Mdot band.
```

A12 bleibt PARTIAL; Stage 3.69 Full-Multiphysics bleibt OPEN.
