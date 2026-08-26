# Stage 3.69E / A-9 – Residence-Time + Backpressure + Minimal Weak-Network Closure

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** REDUCED CLOSURE CALCULATED / `M>=~1e11 kg` STRONG-COUPLING BRANCH SUPPLY-PROCESSING CAPABLE / `1e10 kg` BACKPRESSURE-SENSITIVE / FULL WDM-HYDRO STILL OPEN

## Ziel

A-9 verbindet die bisherigen Teilresultate A-4 bis A-8 zu einer ersten quantitativen Transportclosure:

```text
outer supply
 -> collisional / atomic transition
 -> repeated loss-cone encounters
 -> residence time
 -> permanent escape OR recycling
 -> backpressure criterion
 -> charge-neutrality response
 -> minimal weak-reaction gate
 -> chi_transport
 -> net Mdot_BH.
```

Die zentrale Frage ist nicht mehr, ob ein einzelnes Fe/Ni-Teilchen eine kleine Einmal-Capture-Wahrscheinlichkeit besitzt, sondern ob **verfehlte Encounter das lokale System dauerhaft verlassen** oder kollisional rezykliert werden.

## 1. Literaturkonflikt, den A-9 direkt adressiert

Loeb (2024) argumentierte fuer quantenmechanische Akkretionsunterdrueckung kleiner PBHs in dichten Umgebungen. Cline (2024) kritisierte speziell den Schluss von einer Einzelteilchen-Verzoegerung auf eine stark reduzierte Gesamtakkretionsrate. Die bisherigen Projekt-Solver haben inzwischen gezeigt, dass der direkte Protonen- und Fe/Ni-Wellensink im relevanten `~1e11 kg`-Bereich selbst nicht stark unterdrueckt ist.

Damit lautet die fehlende Rechnung jetzt:

```text
small one-pass loss cone
+ repeated encounters
+ collisions / escape
= ? stationary net Mdot
```

A-9 rechnet genau diese reduzierte Closure.

## 2. Repeated-encounter-Gleichung

Pro Encounter seien

```text
p = Capture-Wahrscheinlichkeit
e = Wahrscheinlichkeit eines permanenten Escape
1-p-e = Recycling in einen neuen Encounter.
```

Dann ist die exakte eventual-capture-Fraktion

```text
chi_capture = p/(p+e).
```

Der mittlere Residence-/Capture-Zeitscale bei vernachlaessigbarem permanenten Escape lautet

```text
t_res = t_cycle/p.
```

Das ist der entscheidende Unterschied zu

```text
chi_capture = p
```

als einmaligem Loss-Cone-Faktor. Letzteres gilt nur, wenn fast jeder Miss das System dauerhaft verlaesst.

## 3. Reduziertes Loss-Cone-/Cycle-Modell

Wie in A-7 wird fuer `x=r/r_B`

```text
c_s(x) = c_inf / sqrt(x)
sigma_perp = c_s/sqrt(gamma)
ell_typ = r sigma_perp
ell_crit = 4 G M/c
p = min[1, 0.5 (ell_crit/ell_typ)^2].
```

Die lokale Cycle-Zeit ist

```text
t_cycle = r/v_ff,
v_ff = sqrt(2GM/r).
```

Dieser Block ist ein reduzierter Winkelimpuls-/Recyclingproxy und keine vollstaendige Boltzmann- oder Fokker-Planck-Loesung.

## 4. Strong-coupling Escape versus collisionless Gegenbranch

A-7 korrigierte die Kollisionalitaet: fuer einen strong-coupling/geometrischen Proxy mit

```text
rho ~ x^-3/2
lambda_mfp ~ x^3/2
Kn ~ x^1/2
```

wird die Materie nach innen **kollisionaler**.

Als optischer Escape-Proxy von einer inneren Skala `x_t` bis `r_B` folgt

```text
tau_coll = Integral dr/lambda
         = 2 r_B/lambda_0 [x_t^-1/2 - 1].
```

Die instantane 3-D-Maxwell-Fraktion oberhalb der lokalen Escape-Geschwindigkeit ist im A-7-Scaling etwa

```text
f(v>v_esc) ~0.343.
```

Aber permanent ballistisch entkommen kann davon im strong-coupling-Proxy nur etwa

```text
e_perm ~ f(v>v_esc) exp(-tau_coll).
```

Bei den getesteten atomaren Transition-Skalen ist `tau_coll` riesig; damit ist `e_perm` numerisch praktisch null. Ein nach aussen gerichtetes Teilchen kollidiert also im Proxy viele Male lange vor `r_B` und wird wieder Teil des lokalen Reservoirs.

Der **absichtlich gegenteilige collisionless Grenzbranch** setzt dagegen

```text
e_perm = f(v>v_esc) ~0.343.
```

Er liefert winzige `chi_capture` und zeigt damit, dass die Dense-Matter-Kopplung/Transportphysik – nicht der Horizon-Wellenquerschnitt – der entscheidende Discriminator ist.

## 5. Reservoir-/Processing-Capacity

Fuer das adiabatische Dichteprofil

```text
rho = rho_0 x^-3/2
```

ist die vorhandene Reservoir-Masse zwischen `r_t` und `r_B`

```text
M_res = (8 pi/3) rho_0 r_B^3 [1-x_t^3/2].
```

Die reduzierte Recycling-Verarbeitungskapazitaet ist

```text
Mdot_capacity = M_res/t_res.
```

Definiert wird

```text
Xi_required = Mdot_supply/Mdot_capacity.
```

Interpretation:

```text
Xi_required <= 1:
    das vorhandene reduzierte Reservoir kann den Supply verarbeiten,
    ohne dass zusaetzlicher Pile-up fuer die Capture-Kapazitaet benoetigt wird.

Xi_required > 1:
    Pile-up / Backpressure / Supply-Reduktion wird relevant;
    die exakte Netto-Mdot bleibt in diesem Reduced Model offen.
```

`Xi_required<=1` beweist keinen exakten Michel-Fluss; es zeigt nur, dass der innere Recycling-Sink den aeusseren Supply in diesem Modell nicht kapazitiv drosseln muss.

## 6. Referenz `M_BH=1e11 kg`

Getestete atomar/elektronische Transition-Sensitivitaet:

| `r_t` | `p` | `t_res` [s] | `Mdot_capacity` [kg/s] | `Xi_low` | `Xi_high` | `tau_coll` | `chi_SC` | collisionless `chi` |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `3e-11 m` | `3.30e-5` | `1.36e-12` | `1.85e-5` | `7.94e-4` | `7.88e-3` | `4.82e4` | `~1` | `9.62e-5` |
| `1e-10 m` | `9.90e-6` | `2.76e-11` | `9.13e-7` | `1.61e-2` | `1.60e-1` | `2.59e4` | `~1` | `2.89e-5` |
| `2e-10 m` | `4.95e-6` | `1.56e-10` | `1.61e-7` | `9.11e-2` | `9.05e-1` | `1.80e4` | `~1` | `1.44e-5` |

Historischer Supply-Benchmark:

```text
Mdot_supply = 1.47e-8 ... 1.46e-7 kg/s.
```

**Befund:** Im strong-coupling/recycling Branch kann selbst die weiteste getestete Transition-Skala `2e-10 m` den oberen Supply-Benchmark gerade noch ohne zusaetzliche Reservoir-Verstaerkung verarbeiten (`Xi_high~0.905`). Fuer die engeren atomaren Skalen liegt grosse Kapazitaetsreserve vor.

Damit wird am `1e11 kg`-Referenzpunkt eine permanente `1e5...1e6`-Unterdrueckung der Gesamt-Mdot durch den kleinen Einmal-Loss-Cone **nicht** unterstuetzt, sofern die A-7/A-8 strong-coupling-Recyclingannahmen gelten.

## 7. Massenscan und Backpressure-Uebergang

### `1e10 kg`

Der Ausgang ist stark transition-scale-abhaengig:

```text
r_t=3e-11 m: Xi_low~0.25, Xi_high~2.49
r_t=1e-10 m: Xi_low~5.10, Xi_high~50.7
r_t=2e-10 m: Xi_low~29.0, Xi_high~288.
```

Damit bleibt der `1e10 kg`-Branch **BACKPRESSURE-SENSITIVE / OPEN**.

### `1e11 kg`

```text
r_t=3e-11 ... 2e-10 m:
Xi_high ~0.0079 ... 0.905.
```

Alle getesteten Skalen sind im Reduced Strong-Coupling-Branch supply-processing capable.

### `2e11 kg`

```text
Xi_high ~0.00139 ... 0.160.
```

Klare Kapazitaetsreserve.

### `5e11 kg`

```text
Xi_high ~1.41e-4 ... 1.62e-2.
```

Sehr grosse Kapazitaetsreserve.

## 8. Kritischer Transport-Uebergang

Fuer den `Mdot~M^2`-Supply-Scaling ist der kritische **fractional radius** praktisch massenunabhaengig:

```text
Xi=1, low supply : x_crit ~8.507e-3
Xi=1, high supply: x_crit ~3.397e-3.
```

Bei `1e11 kg` entspricht das

```text
r_crit,low  ~5.21e-10 m
r_crit,high ~2.08e-10 m.
```

Fuer feste physikalische atomare Transition-Skalen folgt der kritische BH-Massenbereich:

| `r_t` | `Mcrit` low supply | `Mcrit` high supply |
|---:|---:|---:|
| `3e-11 m` | `5.75e9 kg` | `1.44e10 kg` |
| `1e-10 m` | `1.92e10 kg` | `4.80e10 kg` |
| `2e-10 m` | `3.84e10 kg` | `9.61e10 kg` |

Das ist ein neuer quantitativ definierter Reduced-Closure-Uebergang:

```text
M deutlich oberhalb Mcrit -> inner recycling capacity > outer supply
M unter/nahe Mcrit         -> backpressure-sensitive.
```

Die genaue Schwelle ist keine Fundamentalkonstante; sie haengt von der echten WDM-Transition-/Transportskala und vom aeusseren Supply ab.

## 9. Charge-Neutrality-Zeitscale

Mit dem freien Elektronen-Dichteproxy

```text
omega_pe = sqrt(n_e e^2/(m_e epsilon_0))
t_plasma = 1/omega_pe
```

ist die elektrische Plasmaantwort an den getesteten Transition-Skalen viele Groessenordnungen schneller als `t_res`.

Beispiel `M=1e11 kg, r_t=1e-10 m`:

```text
t_plasma/t_res ~2.7e-9.
```

Auch an den A-8 Fe/Ni-Threshold-Radien bleibt die Plasmaantwort schneller als die reduzierte Residence-Zeit.

Damit ist **bulk quasineutrality** als Reduced-Closure gut motiviert. Dies ersetzt nicht den offenen exakten charged-electron Dirac/Coulomb-Matcher und bestimmt nicht die diskrete BH-Ladung `Q(t)` auf wenige Elementarladungen genau.

## 10. Minimal Weak-Network Gate

A-8 fand im freien Fermi-Proxy energetische continuum-EC-Schwellen bei

```text
58Ni -> 58Co: x ~1.66e-4
56Fe -> 56Mn: x ~5.08e-6.
```

A-9 fragt nun nicht nur, ob der Kanal offen ist, sondern welche Rate fuer eine Reaktion **vor der Capture** erforderlich waere:

```text
lambda_required ~ 1/t_res.
```

Bei `M=1e11 kg`:

```text
Ni-threshold:
    p ~9.73e-5
    t_res ~9.13e-14 s
    lambda_required ~1.10e13 s^-1

Fe-threshold:
    p ~3.18e-3
    t_res ~1.50e-17 s
    lambda_required ~6.69e16 s^-1.
```

Zum Vergleich gibt Liu (2013) fuer `56Fe` bei der **viel hoeheren** Bedingung `rho*Ye=1e11 g/cm^3, T9=3` einen screened EC-Wert

```text
lambda_ec(56Fe) = 1.5916e4 s^-1.
```

Dieser Vergleichswert ist kein lokaler Earth-BH-Rate-Ersatz; er ist ein bewusst aggressiver stellarer Timescale-Benchmark. Selbst er liegt jedoch viele Groessenordnungen unter `1/t_res`.

Daher gilt fuer den aktuellen strong-coupling/supply-processing Branch:

```text
energetically open EC != prompt weak equilibrium
prompt one-pass neutronization: NOT SUPPORTED
composition before Horizon capture: approximately frozen in this reduced timescale test.
```

Ein **lang lebender makroskopischer Backpressure-Stau** koennte die Residence-Zeit stark verlaengern und Weak-Reaktionen wieder aktivieren. Genau deshalb bleibt der `1e10 kg` backpressure-sensitive Branch offen.

## 11. Konsequenz fuer Netto-Mdot

### Strong-coupling / recycling Branch

Fuer `M>=~1e11 kg` und die getesteten `r_t=3e-11...2e-10 m` gibt es im Reduced Model keinen inneren Kapazitaetsengpass. Permanent ballistischer Escape ist wegen `tau_coll>>1` praktisch null, sodass

```text
chi_transport ~1
```

als **Reduced-Branch-Ergebnis** folgt.

Damit liegt die Netto-Mdot in diesem Branch nahe der aeusseren Supply-Skala, nicht nahe dem naiven Single-pass-Wert.

Insbesondere bei `M=1e11 kg`:

```text
Mdot_BH,reduced strong-coupling ~1.47e-8 ... 1.46e-7 kg/s.
```

Das ist **keine gemessene Rate und noch keine Full-Multiphysics-Endvorhersage**. Es ist die Konsequenz der gegenwaertig miteinander konsistenten Reduced-Closures A-5 bis A-9.

### Collisionless/permanent-escape Gegenbranch

Wenn man die gleiche lokale Maxwell-Tail-Fraktion als *permanenten* Escape behandelt, ergeben sich `chi~1e-6...1e-4`. Dieser Branch reproduziert eine starke Suppression, benoetigt aber einen physikalischen Mechanismus, der die in A-7/A-8 gefundene starke Kollisionalitaet ueberwindet.

Damit ist die eigentliche offene Frage jetzt sehr scharf formuliert:

```text
first-principles WDM transport determines
whether e_perm << p  or  e_perm >> p.
```

## 12. Was A-9 entscheidet

```text
single-pass loss cone as automatic stationary Mdot factor: REJECTED
repeated-encounter exact probability closure: IMPLEMENTED
strong-coupling ballistic escape optical-depth proxy: CALCULATED
collisionless opposite escape bracket: CALCULATED
reservoir processing capacity: CALCULATED
critical transition radius/mass: CALCULATED
bulk plasma-response/quasineutrality timescale: CALCULATED
weak-reaction activation gate: CALCULATED

M>=~1e11 kg strong-coupling/recycling reduced branch:
    SUPPLY-PROCESSING CAPABLE
    chi_transport ~1 in this reduced closure

M=1e10 kg:
    BACKPRESSURE-SENSITIVE / OPEN

full first-principles dense Fe/Ni transport:
    OPEN
final Stage 3.69 species-resolved Mdot:
    not yet promoted to full-physics result.
```

## 13. Konsequenz fuer H+ und H0

A-9 ist ein gemeinsamer Materie-/Transportblock fuer beide Branches.

```text
H+:
    bleibt separat durch den getesteten Standard-Hawking/SK-IV-Projektvergleich belastet/FAIL;
    A-9 hebt diesen Hawking-spezifischen Befund nicht auf.

H0:
    kein Hawking-Term;
    der aktuelle >=1e11-kg Reduced Strong-Coupling-Branch benoetigt keine riesige Akkretionsunterdrueckung,
    weil bereits die historischen Michel-Supply-Raten in den reduzierten Erdalter-/Waermechecks nicht zum Ausschluss fuehrten.
    H0 bleibt OPEN / nicht nachgewiesen.
```

## 14. Naechster Pflichtblock

Der naechste Schritt ist nicht mehr ein weiterer frei parametrischer Suppressionsfaktor, sondern

```text
Stage 3.69F / A-10:
first-principles-informed WDM transport closure
+ time-dependent spherical hydro/kinetic sink coupling
+ real absorptive horizon boundary
-> e_perm(r,E,species)
-> chi_transport without geometric-mfp proxy
-> final reduced species-resolved Mdot band.
```

Prioritaet:

1. WDM Fe/Ni collision/relaxation coefficients statt geometrischer `lambda_0`-Naeherung;
2. EOS/average-ionization along the compressed trajectory;
3. couple to the existing A-7 time-dependent Euler solver;
4. inner boundary from A-4/A-5 capture, not a hand-set reflecting wall;
5. rerun the `1e10...5e11 kg` mass scan.

## Reproduzierbarkeit

- `stage3_69e_a9_residence_backpressure_network.py`
- `STAGE3_69D_A8_WDM_WEAK_TIMESCALES.md`
- `stage3_69d_a8_wdm_weak_timescales.py`
- `STAGE3_69C_A7_COLLISION_RECYCLING_PDE.md`
- `stage3_69c_a7_collision_recycling_pde.py`

## Referenzen

- A. Loeb (2024), *Quantum-Mechanical Suppression of Accretion by Primordial Black Holes*, ApJL 975 L15, arXiv:2409.09081.
- J. M. Cline (2024), *Comment on "Quantum-Mechanical Suppression of Gas Accretion by Primordial Black Holes"*, arXiv:2409.12989.
- M. Cantiello et al. (2026), *Accretion of Primordial Black Holes in Stellar Interiors*, arXiv:2606.02726. Used only for multiscale/time-dependent methodology; stellar numerical parameters are not transplanted to Earth.
- J.-J. Liu (2013), *Electron capture of strongly screening nuclides 56Fe, 56Co, 56Ni, 56Mn, 56Cr and 56V in pre-supernovae*, MNRAS 433, 1108–1113.
- J. Simoni & J. Daligault (2019), *First-Principles Determination of Electron-Ion Couplings in the Warm Dense Matter Regime*, Phys. Rev. Lett. 122, 205001.
- S. Rightley & S. D. Baalrud (2021), *Kinetic model for electron-ion transport in warm dense matter*, Phys. Rev. E 103, 063206.
- L. V. Pourovskii et al. (2020), *Electronic correlations and transport in iron at Earth’s core conditions*, Nature Communications 11, 4105.
