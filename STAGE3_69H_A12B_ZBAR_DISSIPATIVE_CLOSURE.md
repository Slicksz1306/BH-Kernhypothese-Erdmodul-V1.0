# Stage 3.69H / A12b – More/TF Zbar + physisch skalierter dissipativer PDE-Test

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** PARTIAL CALCULATED / ZBAR-CLOSURE IMPLEMENTED / DISSIPATIVE BACKPRESSURE TEST CALCULATED / FULL FIRST-PRINCIPLES EOS TABLE STILL OPEN

## Ziel

A12b greift zwei offene Punkte aus A12 an:

```text
1. keine erfundene Zbar(rho,T)-Tabelle
2. reale Fe-Transportkoeffizienten nicht nur als Re/Pe-Audit, sondern als dissipative PDE-Sensitivitaet
```

Kein Resultat dieses Blocks ist ein experimenteller Nachweis eines schwarzen Lochs im Erdzentrum.

## 1. Average-ionization closure

Verwendet wird der analytische Thomas-Fermi-Fit nach More, der explizit fuer Hydro-/Plasma-Codes entwickelt wurde:

```text
Zbar = Z*x/(1+x+sqrt(1+2x))
```

mit der publizierten More-Parameterisierung fuer Dichte und Elektronentemperatur. Fuer Fe wird der in der Metall-EOS-Literatur angegebene Low-T-Korrekturfaktor

```text
factor_Fe = 0.270
```

verwendet.

Literaturanker:

- More/Thomas-Fermi fit, wie in modernen Transport-/Hydro-Implementierungen dokumentiert;
- Metall-EOS-Arbeit mit Fe-Korrekturfaktor `0.270`;
- Average-Atom-WDM-Arbeiten betonen, dass `Zbar` keine eindeutig modellunabhaengige Observable ist.

Daher wird `Zbar` als **bounded transport closure**, nicht als exakte atomare Ladungszahl interpretiert.

### Referenzpunkt Erdkern

Bei

```text
rho = 13.0885 g/cm3
T   = 6000 K = 0.517 eV
```

ergibt der korrigierte More-Fit

```text
Zbar_Fe ~2.761.
```

### Vergleich mit solid-density Average-Atom Daten

Eine publizierte warm-solid-density-Fe-Tabelle fuer die Definition `Z_WS,2` liefert ungefaehr

```text
T[eV] : 0.1  1    3    5    7    10
Z_WS2 : 2.47 2.52 2.69 2.89 3.09 3.37
```

Der korrigierte More-Fit bei `rho=7.874 g/cm3` liefert

```text
2.07, 2.16, 2.34, 2.52, 2.70, 2.97.
```

Damit liegt More in diesem Vergleich etwa `12...16 %` niedriger. Das wird als systematische `Zbar`-Unsicherheit sichtbar behalten.

## 2. Reduced inward-path Zbar map

Fuer den bisherigen Sensitivitaetspfad

```text
rho(x)=13.0885*x^-3/2 g/cm3
T(x)=6000/x K
x=r/r_B
```

folgt:

| x | rho [g/cm3] | T [eV] | Zbar_More |
|---:|---:|---:|---:|
| 1 | 13.09 | 0.517 | 2.76 |
| 0.65 | 24.98 | 0.795 | 3.83 |
| 0.425 | 47.24 | 1.217 | 5.15 |
| 0.1 | 4.14e2 | 5.17 | 10.99 |
| 0.01 | 1.31e4 | 51.7 | 19.23 |
| 1e-3 | 4.14e5 | 517 | 23.28 |
| 1e-4 | 1.31e7 | 5170 | 25.06 |

Der Fit geht tief innen erwartungsgemaess gegen Vollionisation, ist dort aber eine TF-Extrapolation und keine direkte DFT-MD-Tabelle.

## 3. Dissipative PDE-Sensitivitaet

A12 hatte fuer den Bondi-Massstab physische Bereiche gefunden:

```text
eta = 8.5...26 mPa s
k   = 67...87 W/m/K
Cp  = 850 J/kg/K.
```

Daraus:

```text
M=1e10 kg: Re~32...98,  Pe~8...11
M=1e11 kg: Re~322...985, Pe~82...106
```

A12b setzt diese Bereiche jetzt als **explizite radiale Newtonsche Viskositaets- und Waermefluss-Terme** in den kontrollierten `gamma=1.5`-PDE-Solver ein.

Verwendete dimensionslose Terme:

```text
tau_rr = (4/3)/Re * (du/dr-u/r)
q_cond = -(Cp*T0/c_inf^2)/Pe * d(T/T0)/dr
```

mit

```text
T/T0 = gamma*P/rho
```

im aktuellen Gamma-EOS-Surrogat.

**Aussagegrenze:** Dies ist noch keine echte tabellierte Fe-EOS. Der dissipative Test beantwortet nur, ob die literaturgebundenen Transportgroessen den bereits gefundenen Backpressure-Ast qualitativ sofort zerstoeren.

## 4. Numerischer Test – 1e10 kg Capacity Branch

Getestet:

```text
A_cap ~0.681
Gamma = 1.5
rmax = 30 r_B
t = 0.8 r_B/c_inf
```

Bei `N=64`:

| Fall | Re | Pe | Shock [r_B] | innerer Flux |
|---|---:|---:|---:|---:|
| inviscid | sehr gross | sehr gross | ~1.39 | ~0.0241 |
| schwache Dissipation | 98.5 | 10.62 | ~1.39 | ~0.0243 |
| starke Dissipation | 32.2 | 8.18 | ~1.39 | ~0.0241 |

Bei `t=0.6` und staerkerer Dissipation:

```text
N=80: shock~1.083 r_B, inner flux~0.0276
N=96: shock~1.059 r_B, inner flux~0.0271
```

Die konservativen Bilanzen bleiben in den getesteten Laeufen auf etwa `1e-15` relativ.

### Befund

```text
literature-scale viscosity/conduction:
DO NOT remove the 1e10-kg backpressure branch
in the current reduced PDE.
```

Sie verschieben/broaden Details, erzeugen aber in diesem Test keinen Ruecksprung auf den voll absorbierenden Bondi-Ast.

## 5. >=1e11 kg

Mit steigender BH-Masse wachsen Re und Pe ungefaehr proportional zu `r_B`. Deshalb werden dieselben Fe-Transportkoeffizienten am Bondi-Massstab relativ schwächer.

A10/A11/A12 hatten dort bereits

```text
Xi_high << 1
A_cap = 1.
```

A12b findet keinen dissipativen Grund, den aktuellen Reduced supply-processing Ast automatisch umzukehren.

```text
>=1e11 kg Reduced matter branch:
SURVIVES A12b dissipative sensitivity.
```

Das ist weiterhin keine Full-WDM-Endrate.

## 6. Electron-ion relaxation

First-principles Arbeiten fuer WDM Fe/Ni zeigen, dass electron-ion energy exchange stark nichtideal und modellabhaengig ist. Moderne Kubo/QMD-Behandlungen koennen sich im WDM-Bereich deutlich von Landau-Spitzer unterscheiden. Eine 2026 erschienene Erratum-Historie fuer eine einschlaegige Average-Atom-Arbeit unterstreicht, dass hier keine unkritische Einzel-Formel als harte Closure eingesetzt werden sollte.

A12b fuehrt deshalb noch keinen frei gewaehlten `tau_ei`-Wert ein.

```text
e-i relaxation: literature-constrained uncertainty, still OPEN in full PDE.
```

## 7. Status

```text
More/TF Zbar implementation: DONE
solid-density Zbar comparison: DONE
Reduced inward Zbar map: CALCULATED
physical eta/k/Cp dimensionless coupling: IMPLEMENTED
1e10 dissipative backpressure sensitivity: CALCULATED
>=1e11 dissipative scaling audit: CALCULATED
full first-principles P(rho,T),E(rho,T): OPEN
full first-principles Zbar table: OPEN
thermodynamically exact Fe/Ni dissipative PDE: OPEN
charged-electron far-field capture: OPEN
Stage 3.69 Full-Multiphysics: OPEN
```

## 8. Konsequenz

A12b haertet den bisherigen Massensplit weiter:

```text
1e10 kg:
    outward/backpressure branch remains robust to literature-scale eta/k sensitivity
    stationary final Mdot still not established

>=1e11 kg:
    current reduced supply-processing branch survives
```

Naechster sinnvoller Unterblock:

```text
A12c:
Mie-Gruneisen / tabulated-Fe EOS surrogate with explicit T(rho,e)
+ Zbar uncertainty band
+ two-temperature/e-i relaxation bracket
+ repeat dissipative dynamic mass scan.
```
