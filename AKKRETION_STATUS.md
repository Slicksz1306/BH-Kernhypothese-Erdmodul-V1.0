# Akkretions- und Langzeitstatus – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Forschungsstand:** Materie-/Capture-/Transport-Closure bis Stage 3.69E/A-9 bearbeitet; first-principles Netto-`Mdot` offen

## Aussagegrenze

Bondi-/Michel-Raten bleiben aeussere Supply-/Kapazitaetsbenchmarks. Einzelteilchen-/Wellenquerschnitte sind innere Sink-Benchmarks. Die reale Rate muss beide ueber Transport, Recycling, Backpressure, Charge und Reaktionen koppeln.

```text
Mdot_net != automatisch Mdot_Michel
Mdot_net != automatisch p_single * Mdot_Michel
```

A9 liefert jetzt erstmals eine reduzierte Residence-/Processing-Closure zwischen diesen beiden Extremen.

## Referenzskalen bei `M_BH=1e11 kg`

```text
rho_c = 13.0885 g/cm^3
c_eff = 10.4355 km/s
r_B ~6.13e-8 m
r_s ~1.49e-16 m
```

Historischer Michel-Supply-Benchmark:

```text
Mdot_Michel ~1.47e-8 ... 1.46e-7 kg/s
             ~0.46 ... 4.61 kg/year.
```

## Wave-Sink-Ergebnisse

### Protonen

```text
neutral Earth-speed proton @1e11 kg:
sigma_p ~2.174e-22 m^2
~0.9503 sigma_classical
```

Keine starke Protonen-Wellenunterdrueckung.

Charged-Proton-Subtest:

```text
Q=0 e      -> ~0.949 classical
Q=3.67 e   -> ~0.889
Q=10 e     -> ~0.765
Q=24.18 e  -> ~0.517
```

Charge-Feedback ist relevant, aber im getesteten Bereich kein Orders-of-Magnitude-Protonenstopper.

### Fe/Ni

`Fe-56`/`Ni-58` sind `0+`; erster kohärenter Composite-Proxy ist Klein-Gordon/scalar.

```text
Fe-56 @1e11 kg: ~0.99754 classical
Ni-58 @1e11 kg: ~0.99646 classical
```

Keine grosse kohärente Fe/Ni-Wellenunterdrueckung gefunden.

## Screening

Dense-Fe Elektronenscreening liegt im reduzierten freien-Elektronenproxy auf atomaren/sub-nm Skalen:

```text
~few 1e-11 ... 1e-10 m << r_B.
```

Daher ist eine kleine BH-Nettoladung lokal wichtig, aber kein ungescreenter Coulomb-Blocker ueber die gesamte `r_B`-Supply-Zone.

## Single-pass versus Recycling

Direkter Hintergrund-Single-pass-Proxy:

```text
Mdot_single ~3.1e-14 kg/s
```

Luecke zum Michel-Supply:

```text
factor ~4.7e5 ... 4.7e6.
```

Diese Luecke ist **kein** nachgewiesener Suppressionsfaktor.

Fuer repeated encounters:

```text
chi_capture = p/(p+e_perm)
```

mit Einzelpass-Capture `p` und permanentem Escape `e_perm`.

Ohne permanenten Escape kann ein sehr kleines `p` durch Recycling zu hoher eventual capture fuehren. Eine Netto-Unterdrueckung nahe dem Single-pass-Wert erfordert dagegen einen physikalischen dauerhaften Escape-/Backpressure-Kanal.

## Kollisionalitaet – A7-Korrektur

Strong-coupling/geometrischer Branch:

```text
rho~r^-3/2
lambda_geom~r^3/2
Kn~r^1/2
```

=> `Kn` sinkt nach innen; kein automatischer collisionless transition.

Weak-Coulomb/Spitzer:

```text
lambda_C~T^2/n
Kn_C~r^-3/2
```

=> collisionless transition moeglich, aber nur falls die Materie tatsaechlich `Gamma<<1` erreicht.

## Backpressure-PDE

Ein eigener sphärischer 1-D-Bondi-Euler-Prototyp reproduziert den analytischen transsonischen Massenfluss auf Prozentniveau.

- absorbierender Innenrand: stationaerer Bondi-Flux bleibt erhalten;
- reflektierender Innenrand: Druckaufbau + outward shock.

```text
sonic shielding != Schutz gegen langfristiges Massestauen.
```

Ein echter reflektierender/Backpressure-Mechanismus kann Supply reduzieren; Recycling mit endlicher Capture ist physikalisch ein anderer Grenzfall.

## A8 – Strong Coupling und Weak-Reaction-Zeitskalen

EC-Energieschwellen im freien Fermi-Proxy:

```text
58Ni -> 58Co:
x~1.66e-4
r~6.84e4 r_s
Gamma_i(Zeff=26)~203

56Fe -> 56Mn:
x~5.08e-6
r~2.09e3 r_s
Gamma_i(Zeff=26)~35.6
```

Der weak-Spitzer-Branch ist dort ohne expliziten EOS-/Ionisationsnachweis nicht selbstkonsistent.

Publizierter schneller `56Fe`-EC-Vergleich:

```text
lambda_ec~1.5916e4 s^-1
tau_ec~6.28e-5 s.
```

Energetische Schwelle und Reaktionsgleichgewicht sind getrennte Fragen.

# A9 – Residence / Processing / Backpressure Closure

## A9.1 Exact repeated-encounter closure

```text
p       = capture per encounter
e_perm  = permanent escape per encounter
recycle = 1-p-e_perm

chi_capture = p/(p+e_perm).
```

Bei `e_perm~0`:

```text
t_res = t_cycle/p.
```

## A9.2 Strong-coupling permanent escape

Im A7 strong-coupling/geometrischen Sensitivitaetsbranch

```text
lambda=lambda_0 x^3/2
```

ist der collisional optical depth bis `r_B`

```text
tau_coll = 2 r_B/lambda_0 [x_t^-1/2 - 1].
```

Die instantane Maxwell-Fraktion oberhalb `v_esc` ist im Scaling etwa `0.343`, aber permanenter **ballistischer** Escape wird durch

```text
exp(-tau_coll)
```

unterdrueckt.

An den getesteten atomaren Transition-Skalen gilt typischerweise

```text
tau_coll ~1e3 ... >1e5.
```

Damit ist `e_perm` im Reduced Strong-Coupling-Branch praktisch null und `chi_capture~1`.

Der collisionless Gegenbranch (`e_perm~0.343`) liefert dagegen `chi~1e-6...1e-4`; genau dieser Kontrast zeigt, dass first-principles WDM-Transport der entscheidende Discriminator ist.

## A9.3 Reservoir processing capacity

Fuer

```text
rho=rho_0 x^-3/2
```

ist die Reduced Reservoir-Masse zwischen `r_t` und `r_B`

```text
M_res=(8 pi/3) rho_0 r_B^3 [1-x_t^3/2].
```

Processing capacity:

```text
Mdot_capacity=M_res/t_res.
```

Definiert wird

```text
Xi_required=Mdot_supply/Mdot_capacity.
```

```text
Xi<=1:
    vorhandenes Reduced Reservoir kann den Supply ohne zusaetzlichen Capture-Pile-up verarbeiten.

Xi>1:
    Backpressure/Pile-up/Supply-Rueckkopplung wird relevant; exakte Mdot bleibt offen.
```

## A9.4 `M=1e11 kg`

| `r_t` | `p` | `t_res` [s] | `Mdot_capacity` [kg/s] | `Xi_low` | `Xi_high` |
|---:|---:|---:|---:|---:|---:|
| `3e-11 m` | `3.30e-5` | `1.36e-12` | `1.85e-5` | `7.94e-4` | `7.88e-3` |
| `1e-10 m` | `9.90e-6` | `2.76e-11` | `9.13e-7` | `1.61e-2` | `1.60e-1` |
| `2e-10 m` | `4.95e-6` | `1.56e-10` | `1.61e-7` | `9.11e-2` | `9.05e-1` |

**Befund:** Der gesamte historische Supply-Benchmark ist fuer alle drei getesteten Transition-Skalen im Reduced Strong-Coupling/Recycling-Branch processing-capable.

Damit wird bei `1e11 kg` eine permanente `1e5...1e6`-Gesamtunterdrueckung durch den kleinen Einmal-Loss-Cone nicht gestuetzt, solange die aktuelle strong-coupling-Recyclingclosure gilt.

## A9.5 Massenscan

```text
M=1e10 kg:
    r_t=3e-11 m -> Xi_low~0.25, Xi_high~2.49
    r_t=1e-10 m -> Xi_low~5.10, Xi_high~50.7
    r_t=2e-10 m -> Xi_low~29, Xi_high~288
    => BACKPRESSURE-SENSITIVE / OPEN

M=1e11 kg:
    Xi_high~0.0079 ... 0.905
    => supply-processing capable

M=2e11 kg:
    Xi_high~0.00139 ... 0.160
    => clear capacity reserve

M=5e11 kg:
    Xi_high~1.4e-4 ... 1.62e-2
    => very large capacity reserve.
```

## A9.6 Kritischer Reduced-Transport-Uebergang

```text
xcrit low supply  ~8.507e-3
xcrit high supply ~3.397e-3.
```

Bei `1e11 kg`:

```text
rcrit,low  ~5.21e-10 m
rcrit,high ~2.08e-10 m.
```

Fuer feste physikalische Transition-Skalen:

| `r_t` | `Mcrit` low | `Mcrit` high |
|---:|---:|---:|
| `3e-11 m` | `5.75e9 kg` | `1.44e10 kg` |
| `1e-10 m` | `1.92e10 kg` | `4.80e10 kg` |
| `2e-10 m` | `3.84e10 kg` | `9.61e10 kg` |

Die genaue Schwelle ist transport-/EOS-abhaengig; sie ist keine Fundamentalkonstante.

## A9.7 Charge-neutrality timescale

Elektronen-Plasmaresponse:

```text
omega_pe=sqrt(n_e e^2/(m_e epsilon_0))
t_plasma=1/omega_pe.
```

Beispiel `M=1e11 kg, r_t=1e-10 m`:

```text
t_plasma/t_res~2.7e-9.
```

Bulk-quasineutraler Transport ist damit im Reduced Model gut motiviert. Der diskrete BH-Charge-State bleibt trotzdem nicht exakt geloest.

## A9.8 Minimal Weak-Network Gate

Bei `M=1e11 kg`:

```text
Ni-threshold:
t_res~9.13e-14 s
lambda_required~1.10e13 s^-1

Fe-threshold:
t_res~1.50e-17 s
lambda_required~6.69e16 s^-1.
```

Der publizierte `56Fe`-Vergleichswert

```text
lambda_ec~1.5916e4 s^-1
```

liegt viele Groessenordnungen darunter.

```text
prompt weak equilibrium / one-pass neutronization:
NOT SUPPORTED in the fast supply-processing branch.
```

Ein langlebiger makroskopischer Backpressure-Stau kann Residence-Zeiten vergroessern und Weak-Reaktionen wieder relevant machen; das betrifft vor allem den offenen `1e10 kg`-Unterrand.

## Reduced Netto-Mdot consequence

Fuer `M>=~1e11 kg` im aktuellen Strong-Coupling/Recycling Reduced Branch gilt

```text
chi_transport~1.
```

Damit am `1e11 kg`-Referenzpunkt:

```text
Mdot_BH,reduced ~1.47e-8 ... 1.46e-7 kg/s
                ~0.46 ... 4.61 kg/year.
```

Dies ist **keine Messung und keine first-principles WDM-Endrate**. Es ist die Konsequenz der aktuell miteinander konsistenten Reduced Closures A5-A9.

## Globaler Waerme-/Langzeit-Kontext

Bei `eta=1`:

```text
Mdot_max aus 47 TW ~5.23e-4 kg/s.
```

Der obere historische kleine Michel-Benchmark bei `5e11 kg` bleibt mit etwa `3.65e-6 kg/s` deutlich darunter. Die frueheren Erdalter-/Massen-Stressproxies hatten die Supply-Skalen ebenfalls nicht automatisch ausgeschlossen.

Damit falsifiziert die A9-Nahe-Supply-Rate H0 im bisherigen reduzierten Langzeit-/Waermerahmen nicht automatisch. Lokale Energieablagerung und echte Effizienz bleiben Full-Stack-Fragen.

## Aktueller Status

```text
outer supply capacity: benchmarked, not final
proton wave sink: calculated
charged proton feedback: partially calculated
Fe/Ni scalar wave sink: calculated, near classical
long-range Coulomb blocking: not supported by screening proxy
single-pass suppression as net Mdot: rejected
strong-coupling inward branch: reduced self-consistent proxy
backpressure suppression: demonstrated as reflecting PDE extreme
A9 repeated-encounter/processing closure: calculated
M>=~1e11 strong-coupling branch: supply-processing capable
M=1e10: backpressure-sensitive / OPEN
prompt weak equilibrium: not supported in fast branch
final first-principles chi_transport: OPEN
final species-resolved Mdot_BH: OPEN
```

## Naechster Block

```text
Stage 3.69F / A-10:
first-principles-informed WDM transport
+ time-dependent hydro/kinetic sink coupling
+ A4/A5 absorptive inner boundary
-> replace geometric mean-free-path proxy
-> determine e_perm(r,E,species)
-> final reduced species-resolved Mdot band.
```

H+ und H0 bleiben parallel; diese Materieclosure ist gemeinsam, H+ besitzt zusaetzliche Hawking-Terme.
