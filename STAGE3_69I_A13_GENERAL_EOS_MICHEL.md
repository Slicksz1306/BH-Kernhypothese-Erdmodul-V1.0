# Stage 3.69I / A13 – General-EOS relativistischer Michel-Supply

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** PARTIAL GENERAL-EOS CLOSURE CALCULATED / VARIABLE-EOS SURROGATE SCAN DONE / REAL TABULATED Fe/Ni ISENTROPE STILL OPEN

## 1. Warum A13 noetig wurde

A12c zeigte, dass der bisherige historische Supply-Benchmark

```text
M=1e11 kg:
Mdot ~1.47e-8 ... 1.46e-7 kg/s
```

nicht als universelle Rate behandelt werden darf. Ein konstantes steifes `Gamma` kann die relativistische Michel-Rate um viele Groessenordnungen verschieben.

Gleichzeitig war der extrem kleine A12c-Wert fuer den lokalen PREM-Stiffness-Proxy

```text
Gamma=2.356 -> Mdot~2.40e-12 kg/s @1e11 kg
```

nur ein Stresslimit, weil reale Fe/Ni-Materie bei steigender Kompression ionisiert, degeneriert und ihre effektive Steifigkeit aendert.

A13 ersetzt deshalb `Gamma=const` erstmals durch einen **allgemeinen thermodynamisch konsistenten barotropen/isentrope Solver**.

## 2. Relativistische general-EOS Michel-Gleichungen

Fuer stationaere, sphaerische, adiabatische Akkretion auf ein Schwarzschild-BH gelten Restmassen- und Bernoulli-Erhaltung:

```text
4 pi r^2 rho0 u = Mdot

h sqrt(1 - 2M/r + u^2) = h_inf.
```

Mit

```text
a^2 = dP/d epsilon
```

folgen am regulaeren kritischen Punkt fuer eine allgemeine kausale EOS:

```text
u_s^2 = a_s^2/(1+3 a_s^2)

r_s/M = (1+3 a_s^2)/(2 a_s^2)

h_s/sqrt(1+3 a_s^2) = h_inf.
```

Der A13-Solver sucht daher direkt in der EOS nach der Dichte, an der die letzte Gleichung erfuellt ist. Danach folgt `Mdot` ohne Newton-Bondi-Approximation.

Literaturanker:

- Michel (1972), relativistische sphaerische Akkretion;
- Baumgarte & Shapiro, *Relativistic Bondi accretion for stiff equations of state*, MNRAS 502 (2021) 3003;
- Aguayo-Ortiz et al., *Spherical accretion: Bondi, Michel, and rotating black holes*, MNRAS 504 (2021) 5039.

## 3. Outer Boundary – PREM wird jetzt vollstaendiger benutzt

PREM Table II am Zentrum:

```text
rho_inf    = 13.08848 g/cm3
P_inf      = 363.8521 GPa
K_S,inf    = 1.4253 TPa
dK/dP      = 2.3560
c_eff      = sqrt(K_S/rho) ~10.4355 km/s.
```

Damit wird nicht mehr nur `rho` und `c_eff`, sondern auch der reale zentrale Druck explizit in die EOS-Closure aufgenommen.

Referenz: Dziewonski & Anderson (1981), PREM.

## 4. Thermodynamisch konsistenter variable-EOS Surrogat

Die aktuelle A13-Stufe benutzt noch **keine erfundene first-principles Fe-Tabelle**. Stattdessen wird eine kontrollierte piecewise isentrope Familie verwendet.

Jedes Segment erfuellt

```text
B = rho dP/drho

dB/dP = beta

B(rho)=B0 (rho/rho0)^beta

P(rho)=P0 + B0/beta [(rho/rho0)^beta - 1]
```

und die Enthalpie wird thermodynamisch konsistent ueber

```text
dh = dP/(rho c^2)
```

integriert. `P`, `B` und `h` sind an allen Segmentgrenzen stetig.

### Outer segment

```text
beta_outer = PREM dK/dP = 2.356
```

wird nur bis zum Ende der direkt belastbaren High-P-Fe-Domaene gehalten.

Getestete Softening-Grenzen:

```text
rho_soft = 30 g/cm3
rho_soft = 47.2 g/cm3.
```

Diese Werte orientieren sich an:

- Sjostrom & Crockett 2018: WDM-Fe-QMD bis etwa `30 g/cm3`, `1...100 eV`;
- Blanchet et al. 2025: first-principles Fe-EOS bis `47.2 g/cm3` und `1e9 K`.

### Intermediate segment

Da zwischen `~47 g/cm3` und der tiefen relativistisch/degenerierten Zone noch keine direkt eingelesene isentrope Fe/Ni-Tabelle vorliegt, wird nur ein **Sensitivity-Envelop** getestet:

```text
beta_mid = 1.4, 1.5, 1.6, 5/3, 1.75, 1.8.
```

Das ist kein statistisches Konfidenzintervall und keine Behauptung ueber die reale Fe-Steifigkeit.

### Inner segment

Als innerer Softening-Marker wird der freie vollionisierte Fe-Proxy `p_F=m_e c` verwendet:

```text
rho_e,rel ~2.10e6 g/cm3.
```

Sensitivity:

```text
rho_rel = 1e5 ... 1e7 g/cm3.
```

Darueber geht der Surrogatast gegen

```text
beta_inner = 4/3.
```

Auch dies ist ein kontrollierter asymptotischer Proxy, keine vollstaendige Dense-Fe-QED-EOS.

## 5. Solver-Regression gegen A12c

Der general-EOS-Solver wird zuerst auf ein einzelnes konstantes `beta` reduziert.

Bei `M=1e11 kg`:

| beta | A13 general EOS | A12c | rel. Differenz |
|---:|---:|---:|---:|
| 1.50 | `3.22370e-6` | `3.22342e-6` | `+8.65e-5` |
| 1.80 | `2.88988e-8` | `2.88980e-8` | `+3.10e-5` |
| 2.00 | `3.35248e-10` | `3.35239e-10` | `+2.48e-5` |
| 2.356 | `2.40007e-12` | `2.40003e-12` | `+1.83e-5` |

```text
general-EOS Michel regression: PASS
```

Die kleine Differenz entsteht vor allem dadurch, dass A13 den realen PREM-Druck und einen expliziten `h_inf`-Offset mitfuehrt.

## 6. Variable-EOS Surrogat – Supply-Ergebnis

Ueber den kontrollierten Scan

```text
rho_soft = 30 ... 47.2 g/cm3
beta_mid = 1.4 ... 1.8
rho_rel  = 1e5 ... 1e7 g/cm3
beta_inner = 4/3
```

folgt bei `M=1e11 kg`:

```text
Mdot_supply,surrogate ~4.64e-8 ... 1.37e-6 kg/s.
```

### Unterer Rand

```text
rho_soft=47.2 g/cm3
beta_mid=1.8
rho_rel=1e7 g/cm3
Mdot~4.64e-8 kg/s.
```

### Oberer Rand

```text
rho_soft=30 g/cm3
beta_mid=1.4
rho_rel=1e5 g/cm3
Mdot~1.37e-6 kg/s.
```

**Wichtig:** Dies ist ein Surrogat-Envelop, kein finales physikalisches Unsicherheitsband.

Der alte historische Bereich `1.47e-8...1.46e-7 kg/s` liegt damit nicht als universelle Rate fest. Teile davon werden reproduziert; weichere variable-EOS-Aeste koennen auch darueber liegen.

## 7. Zentrale Slice bei `rho_soft=47.2 g/cm3`

Mit `rho_rel=p_F=m_e c`:

| beta_mid | Mdot @1e11 kg [kg/s] | rho_crit [g/cm3] |
|---:|---:|---:|
| 1.40 | `8.10e-7` | `2.32e2` |
| 1.50 | `7.14e-7` | `3.66e2` |
| 1.60 | `5.82e-7` | `1.03e3` |
| 5/3 | `4.28e-7` | `2.10e6` |
| 1.70 | `2.69e-7` | `2.41e6` |
| 1.75 | `1.32e-7` | `2.88e6` |
| 1.80 | `6.34e-8` | `3.33e6` |

Das zeigt direkt, warum eine konstante PREM-Steifigkeit bis zum Horizon keine belastbare Zentralannahme war: Sobald die EOS im Zwischenbereich softet, kann der transsonische Eigenwert wieder stark ansteigen.

## 8. Rueckkopplung an A9-A12 Processing Capacity

A13 verwendet die bereits berechneten A10-fast inneren Processing-Capacities und ersetzt nur den aeusseren Supply.

Ueber das kontrollierte variable-EOS Surrogat:

| M_BH | Mdot_min [kg/s] | Mdot_max [kg/s] | Xi_min | Xi_max |
|---:|---:|---:|---:|---:|
| `1e10` | `4.64e-10` | `1.37e-8` | `0.467` | `13.76` |
| `1e11` | `4.64e-8` | `1.37e-6` | `8.94e-4` | `2.64e-2` |
| `2e11` | `1.86e-7` | `5.47e-6` | `1.36e-4` | `4.01e-3` |
| `5e11` | `1.16e-6` | `3.42e-5` | `1.12e-5` | `3.32e-4` |

Damit wird ein wichtiger Teil des bisherigen Bildes **robuster**:

```text
M>=1e11 kg:
Xi_max << 1 im gesamten kontrollierten A13-Surrogat.
=> inner processing-capable result survives.
```

Beim Unterrand:

```text
M=1e10 kg:
Xi crosses 1.
=> supply/EOS-conditional bleibt korrekt.
```

Ein weicher/high-supply EOS-Ast kann den Backpressure-Zweig aktivieren; ein steiferer/lower-supply Ast kann ihn entfernen.

## 9. Korrektur der A12c-Interpretation

A12c war methodisch wichtig, aber seine extrem kleinen konstant-steifen Raten duerfen nicht als bevorzugte Supply-Prognose gelesen werden.

Ab A13 gilt:

```text
constant PREM-stiffness to horizon:
STRESS LIMIT ONLY
```

und

```text
variable-EOS softening can restore Mdot by many orders relative to that stress limit.
```

Der historische Michelbereich bleibt **LEGACY/EOS-sensitive**, wird aber nicht durch A12c pauschal nach unten ersetzt.

## 10. Was A13 noch nicht geschlossen hat

Noch offen:

- echte tabellierte Fe/Ni-Isentrope ueber den kompletten relevanten Dichtebereich;
- direkte numerische Nutzung einer SESAME-/first-principles-Free-Energy-Tabelle;
- thermische statt rein barotrope `P(rho,T), e(rho,T)`-Integration;
- Fe/Ni/light-element mixture sensitivity;
- Two-temperature electron/ion closure tief innen;
- charged-electron Coulomb-Fernfeldmatcher;
- finale species-resolved `Mdot_net`;
- erneuter Langzeit-/Waerme-Scan mit finalem Supply-Band.

Grant et al. (2021) stellen Daten zu liquid-Fe Isentropen/Ramp-Compression oeffentlich bereit und berichten sehr gute Uebereinstimmung mit SESAME 92141 im Erdkernbereich. Diese Daten sind ein sinnvoller naechster A13b-Anker.

## 11. Status

```text
A13 general-EOS critical equations: IMPLEMENTED
A13 constant-Gamma/A12c regression: PASS
A13 PREM P+K+dK/dP outer boundary: IMPLEMENTED
A13 variable stiffness barotrope: CALCULATED
A13 controlled supply surrogate: CALCULATED
A13 >=1e11 processing reclassification: ROBUST IN TESTED SURROGATE
A13 1e10 classification: EOS/SUPPLY CONDITIONAL
A13 real tabulated Fe/Ni isentrope: OPEN
A13 final Mdot uncertainty band: OPEN
Stage 3.69 Full-Multiphysics: OPEN
```

## 12. Naechster Unterblock – A13b

```text
public liquid-Fe isentrope / SESAME-consistent data ingestion
+ interpolate rho-P-(T where available)
+ thermodynamic h(rho) reconstruction
+ general-EOS Michel critical solve directly on data
+ compare against A13 surrogate family
+ final outer-supply bracket
+ recouple A9-A12
+ rerun heat/age constraints.
```

A13 ist damit **substanziell bearbeitet, aber noch PARTIAL**.
