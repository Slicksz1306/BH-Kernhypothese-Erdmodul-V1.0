# Stage 3.69I / A13 – General-EOS Relativistic Michel Supply + Net-Mdot Closure

**Stand:** 26.08.2026  
**Status:** NEXT BLOCK / DEFINED / NOT YET CALCULATED

## Motivation

A12c zeigt, dass der bisherige historische Michel-Benchmark

```text
M=1e11 kg:
1.47e-8 ... 1.46e-7 kg/s
```

nicht als universelle Supply-Rate verwendet werden darf. Im konstanten-Gamma relativistischen Vergleich variiert die Rate bei gleicher PREM-Aussenbedingung um viele Groessenordnungen, sobald die EOS steifer wird.

Gleichzeitig darf der lokale PREM-Stiffness-Wert `dK/dP~2.356` nicht unveraendert bis zum Horizon extrapoliert werden, weil Fe/Ni auf dem Kompressionspfad ionisiert, degeneriert und sein thermodynamisches Regime wechselt.

A13 muss deshalb den **aeusseren Supply first-principles-informierter und mit variabler EOS** neu bestimmen.

## Zielkette

```text
PREM center state
-> thermodynamically consistent Fe/Ni EOS path
-> pressure + energy + sound speed + enthalpy
-> bounded ionization Zbar(rho,T)
-> relativistic general-EOS sonic/critical point
-> Mdot_supply(EOS)
-> A9-A12 transport/recycling/capture closure
-> net Mdot_BH uncertainty band.
```

## Pflichtmodule

### 1. Outer boundary

Mindestens:

```text
rho_inf
P_inf
K_S,inf
c_s,inf
T_inf
composition Fe/Ni sensitivity.
```

PREM bleibt Null-/Referenzmodell.

### 2. Thermodynamische EOS

Benötigt werden entlang des relevanten Pfads konsistente Funktionen oder Tabellen fuer

```text
P(rho,T)
e(rho,T)
h(rho,T)
c_s^2=(partial P/partial e)_s / appropriate relativistic form
T(rho,e)
```

mit expliziten Gültigkeitsbereichen.

Bevorzugte Datenanker:

- PREM zentraler Bulkmodul/Druck;
- Sjostrom & Crockett 2018 high-pressure Fe EOS;
- Blanchet et al. 2025 extended first-principles Fe EOS;
- weitere tabellierte Fe/Ni EOS nur nach Konsistenzpruefung.

### 3. Ionisation

A12b More/TF bleibt ein bounded closure:

```text
Zbar_More(rho,T)
```

mit systematischem Unsicherheitsband gegen Average-Atom-Definitionen.

Ionisation darf die EOS-/Transportparameter radial veraendern; ein konstanter `Gamma` ist nur Regression.

### 4. General-EOS relativistische Kritikalitaet

Der Solver soll nicht eine Newton-Bondi-Formel fuer `Gamma>5/3` verwenden.

Er muss die relativistischen stationaeren Erhaltungsgleichungen fuer sphaerische Akkretion mit allgemeiner barotroper/thermischer EOS loesen und den transsonischen Eigenwert bestimmen.

Kontrollregressionen:

```text
constant-Gamma 1.5 -> known Michel/Bondi limit
constant-Gamma 5/3 -> relativistic transition
constant-Gamma >5/3 -> Baumgarte/Shapiro stiff-EOS results
```

### 5. Supply uncertainty band

Aus EOS-/Zbar-/T-Unsicherheiten wird ausgegeben:

```text
Mdot_supply_min(M)
Mdot_supply_central(M)
Mdot_supply_max(M)
```

fuer

```text
M=1e10, 1e11, 2e11, 5e11 kg.
```

### 6. Coupling an A9-A12

Fuer jeden Supply-Wert:

```text
Xi = Mdot_supply / Mdot_capacity
```

und danach dynamischer Branch:

```text
Xi <<1 -> no capacity-driven backpressure
Xi ~1  -> transition-sensitive
Xi >1  -> dynamic backpressure test required.
```

A4/A5 Capture und A10-A12 Transport bleiben innere Sink-/Transportmodule.

## Acceptance Criteria

A13 gilt nur als numerisch bearbeitet, wenn:

1. der constant-Gamma GR-Solver A12c reproduziert;
2. eine thermodynamisch konsistente variable-EOS Route implementiert ist;
3. kein PREM-local `Gamma` unveraendert zum Horizon fortgesetzt wird;
4. Sonic-/Critical-Point-Loesung numerisch eindeutig und konvergent ist;
5. EOS-Gültigkeitsmasken sichtbar bleiben;
6. ein `Mdot_supply`-Band statt einer Scheingenauigkeit ausgegeben wird;
7. `1e10...5e11 kg` gescannt werden;
8. A9-A12 Processing/Backpressure mit dem neuen Supply neu klassifiziert wird;
9. keine Modellkompatibilitaet als experimenteller Nachweis bezeichnet wird.

## Entscheidungslogik

```text
if realistic variable-EOS supply lies far below historical Michel range:
    capacity-driven backpressure weakens;
    >=1e11 processing branch is strengthened.

if EOS softening raises supply into/above historical range:
    1e10 backpressure branch can return;
    higher masses must be rechecked quantitatively.

if no thermodynamically consistent transsonic solution exists for part of the EOS band:
    that supply branch is rejected rather than patched by a free factor.
```

## Wissenschaftliche Aussagegrenze

A13 bestimmt auch im Erfolgsfall nur eine theoretische Matter-Accretion-Closure. Es ist kein experimenteller Nachweis eines zentralen BH.

H+ und H0 bleiben getrennt:

```text
H0: Mdot_net = matter closure
H+: Mdot_net = matter closure - Hawking mass loss, plus existing H+ observational constraints.
```

Der bereits dokumentierte H+ Standard-Hawking-Neutrinobefund wird durch A13 nicht aufgehoben.
