# Akkretions- und Langzeitstatus – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 26.08.2026  
**Forschungsstand:** Materie-/Capture-Closure bis Stage 3.69D/A-8 bearbeitet; finale Netto-`Mdot` offen

## Aussagegrenze

Bondi-/Michel-Raten bleiben aeussere Supply-/Kapazitaetsbenchmarks. Einzelteilchen-/Wellenquerschnitte sind innere Sink-Benchmarks. Die reale Rate muss beide ueber Transport, Recycling, Backpressure, Charge und Reaktionen koppeln.

```text
Mdot_net != automatisch Mdot_Michel
Mdot_net != automatisch p_single * Mdot_Michel
```

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

`Fe-56`/`Ni-58` sind `0+`; korrekter erster Composite-Proxy ist Klein-Gordon/scalar.

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
chi_capture = p/(p+e)
```

mit Einzelpass-Capture `p` und permanentem Escape `e`.

Ohne permanenten Escape kann ein sehr kleines `p` durch Recycling zu hoher eventual capture fuehren. Eine Netto-Unterdrueckung nahe dem Single-pass-Wert erfordert dagegen fast vollstaendigen permanenten Escape der Misses.

## Kollisionalitaet – A7-Korrektur

Eine fruehere A6-Sensitivitaet `r_coll~lambda_geom` wurde korrigiert.

Strong-coupling/geometrischer Branch:

```text
rho~r^-3/2
lambda_geom~r^3/2
Kn~r^1/2
```

=> Kn sinkt nach innen; kein automatischer collisionless transition.

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

Daraus folgt:

```text
sonic shielding != Schutz gegen langfristiges Massestauen.
```

Ein echter reflektierender/Backpressure-Mechanismus kann Supply reduzieren; Recycling ohne permanenten Escape ist physikalisch ein anderer Grenzfall.

## A8 – Strong Coupling und Weak-Reaction-Zeitskalen

Reduzierter inward-Branch:

```text
rho~x^-3/2
T~x^-1
Gamma_i~x^1/2
Kn_geom~x^1/2
```

EC-Energieschwellen im freien Fermi-Proxy:

```text
58Ni -> 58Co:
Qkin~0.381 MeV
x~1.66e-4
r~6.84e4 r_s
Gamma_i(Zeff=26)~203

56Fe -> 56Mn:
Qkin~3.696 MeV
x~5.08e-6
r~2.09e3 r_s
Gamma_i(Zeff=26)~35.6
```

Der weak-Spitzer-Branch ist dort ohne expliziten EOS-/Ionisationsnachweis nicht selbstkonsistent.

Publizierter schneller `56Fe`-EC-Vergleich:

```text
lambda_ec~1.59e4 s^-1
tau_ec~6.3e-5 s
```

Lokale Reduced-Dynamik am Fe-Schwellenradius:

```text
t_dyn~4.7e-20 s
```

Damit wird eine **prompt one-pass Neutronisierung/NSE nicht gestuetzt**. Energetische Schwelle und Reaktionsgleichgewicht sind getrennte Fragen.

Bei sehr langen Residence-/Recyclingzeiten koennen weak reactions wieder relevant werden.

## Globaler Waerme-Sanity-Check

Bei `eta=1`:

```text
Mdot_max aus 47 TW ~5.23e-4 kg/s.
```

Der obere historische kleine Michel-Benchmark bei `5e11 kg` bleibt mit etwa `3.65e-6 kg/s` deutlich darunter. Das ist nur ein globaler Vergleich; lokale Energieablagerung bleibt offen.

## Was die finale Rate jetzt bestimmt

Der dominante offene Block ist nicht mehr ein unbekannter isolierter Wellenquerschnitt, sondern

```text
residence/recycling time
vs.
permanent escape/backpressure time
+
charge-neutrality/screening
+
minimal Fe/Ni weak network
+
EOS/transport
```

Formal:

```text
Mdot_BH = chi_transport * Mdot_supply
```

wobei `chi_transport` nicht mehr als freier Einmalfaktor behandelt werden darf.

## Status

```text
outer supply capacity: benchmarked, not final
proton wave sink: calculated
charged proton feedback: partially calculated
Fe/Ni scalar wave sink: calculated, near classical
long-range Coulomb blocking: not supported by screening proxy
single-pass suppression as net Mdot: rejected
strong-coupling inward branch: reduced self-consistent proxy
backpressure suppression: demonstrated as reflecting PDE extreme
prompt weak equilibrium: not supported
final chi_transport: OPEN
final species-resolved Mdot_BH: OPEN
```

## Naechster Block

```text
Stage 3.69E / A-9:
residence/backpressure transport
+ charge neutrality
+ minimal Fe/Ni weak network
-> chi_transport
-> net Mdot_BH
```

H+ und H0 bleiben parallel; diese Materieclosure ist gemeinsam, H+ besitzt zusaetzliche Hawking-Terme.
