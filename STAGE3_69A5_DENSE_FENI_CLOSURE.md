# Stage 3.69A-5 – Dense Fe/Ni + Screening + Transport Closure

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** COHERENT FE/NI SCALAR CAPTURE NUMERICALLY EVALUATED / SCREENING SCALES CALCULATED / FINAL NET MDOT STILL OPEN

## Ziel

A-5 prueft den bislang fehlenden 0+-Composite-Capture-Kanal fuer dominante Fe/Ni-Kerne und verbindet ihn mit ersten dichten-Materie-Skalen fuer Screening, Granularitaet und Supply.

Die Kernfrage lautet nicht mehr nur, ob isolierte Protonen absorbiert werden, sondern:

```text
collisional PREM/material supply
 -> atomic/dense electronic zone
 -> coherent or dissociated nuclei
 -> wave capture
 -> charge-state recycling
 -> net Mdot_BH.
```

## 1. Warum Klein-Gordon statt Dirac

Dominante stabile `Fe-56`- und `Ni-58`-Kerne haben Grundzustandspin `0+`. Solange ein Kern als kohärentes zusammengesetztes Teilchen erhalten bleibt, ist ein massives skalares/Klein-Gordon-artiges Modell der passende erste Wellenproxy. Der Spin-1/2-Dirac-Solver wird dafuer nicht missbraucht.

Verwendet wird die massive skalare Schwarzschild-Gleichung

```text
d^2 psi/dr_*^2 + [omega^2 - V_l(r)] psi = 0
V_l = f [mu^2 + l(l+1)/r^2 + 2M/r^3]
f = 1 - 2M/r.
```

Am Horizont wird die rein einlaufende Loesung verwendet; am Fernfeld wird in ein- und auslaufende skalare Moden zerlegt.

## 2. Externe Low-Coupling-Regression

Testfall:

```text
alpha = 0.0025
E/m = 2
l = 0 dominant
```

Im kleinen-BH/Wellenlaengen-Grenzfall ist der bekannte 4-D-Unruh-Faktor

```text
sigma_Dirac / sigma_scalar -> 1/8.
```

Aus dem publizierten Dirac-Low-E-Wert folgt fuer den skalaren Benchmark

```text
sigma_scalar,target / M^2 ~59.9034.
```

Der neue KG-Solver liefert bei `x_match=40000 M`

```text
sigma_scalar,num / M^2 ~60.0227
relative deviation ~+0.20%.
```

Damit:

```text
scalar/Klein-Gordon low-alpha regression: PASS.
```

## 3. Fe-56 am Erd-Referenzpunkt

Fuer

```text
M_BH = 1e11 kg
v = 10.4355 km/s
alpha_Fe56 = 19.60335
4 alpha_Fe56 = 78.4134
```

liegt der scharfe Partialwellen-Uebergang um `l~78`.

Numerisch:

```text
l=77: P_abs ~0.9996948
l=78: P_abs ~0.3156162
l=79: P_abs ~6.22e-5
l=80: P_abs ~8.05e-9
```

Die niedrigeren Partialwellen sind bis auf numerische Rundung gesaettigt (`P_abs~1`). Die Summe ergibt

```text
sigma_Fe / sigma_classical ~0.99754
sigma_Fe ~2.28214e-22 m^2.
```

## 4. Ni-58 am Erd-Referenzpunkt

Fuer

```text
alpha_Ni58 = 20.30422
4 alpha_Ni58 = 81.2169
```

liegt der Uebergang entsprechend etwas hoeher:

```text
l=80: P_abs ~0.998268
l=81: P_abs ~0.074368
l=82: P_abs ~1.08e-5
l=83: P_abs ~1.39e-9
```

Gesamtergebnis:

```text
sigma_Ni / sigma_classical ~0.99646
sigma_Ni ~2.27968e-22 m^2.
```

**Befund:** Im kohärenten 0+-Composite-Proxy liegt Fe/Ni bei `1e11 kg` praktisch bereits im klassischen Capture-Regime. Eine grosse Wellenunterdrueckung des Kernkanals wird damit an diesem Referenzpunkt nicht gefunden.

## 5. Kleinerer Massenpunkt als Uebergangstest

Bei `M_BH=1e10 kg` liegt `alpha_Fe~1.96` und `alpha_Ni~2.03`. Dort sind die Quantenoszillationen noch sichtbar. Ein direkter Partialwellenscan ergibt als Orientierung

```text
Fe-56: sigma/scalar_classical ~1.03
Ni-58: sigma/scalar_classical ~0.98.
```

Das ist mit dem erwarteten Uebergang aus Wellenoszillationen zur klassischen Capture-Grenze konsistent. Der Haupt-Erdreferenzpunkt `1e11 kg` liegt fuer ganze Fe/Ni-Kerne bereits deutlich weiter im semiclassical/high-coupling Bereich.

## 6. Dense-Fe Elektronenskalen

Mit dem PREM-Zentraldichteproxy

```text
rho = 13088.5 kg/m^3
```

und einem freien-Elektronen-Fe-Proxy `Z=26, A=56` folgen:

```text
n_i ~1.41e29 m^-3
n_e ~3.66e30 m^-3
ion Wigner-Seitz radius a_i ~1.19e-10 m
electron Wigner-Seitz radius a_e ~4.03e-11 m
```

Der freie degenerierte Elektronenproxy liefert

```text
E_F ~86.6 eV
v_F ~5.52e6 m/s
p_F/(m_e c) ~0.0184
lambda_TF ~2.95e-11 m.
```

`lambda_TF` ist hier nur eine Screening-Skala, keine exakte Bandstruktur-/Many-Body-Rechnung fuer inner-core Fe.

Vergleich mit den BH-Skalen bei `1e11 kg`:

```text
r_s ~1.49e-16 m
r_B ~6.13e-8 m
r_B/lambda_TF ~2.08e3
lambda_TF/r_s ~1.99e5.
```

Damit liegt die elektromagnetische Screeningzone **weit innerhalb des Bondi-/Material-Supply-Radius**, aber noch viele Groessenordnungen ausserhalb des Horizonts.

Ein einfaches Yukawa-Bild wuerde eine nackte Zentralcharge am `r_B` um `exp(-r_B/lambda_TF)` unterdruecken; bei `r_B/lambda_TF~2076` ist das aeussere Coulombfeld praktisch vollständig gescreent. Daraus folgt:

```text
BH charge can be locally important;
it is not a long-range r_B-scale supply stopper in dense Fe.
```

## 7. Granularitaet des Screenings

Der freie-Elektronen-Proxy enthaelt innerhalb einer Kugel mit Radius `lambda_TF` nur etwa

```text
N_e(lambda_TF sphere) ~0.39.
```

Deshalb darf `lambda_TF=2.95e-11 m` nicht als perfekt kontinuierliche mikroskopische Abschirmhuelle interpretiert werden. Physikalisch robuster ist die Aussage:

```text
screening / charge rearrangement occurs on atomic/electronic scales
~few 1e-11 ... 1e-10 m,
not on r_B ~6e-8 m.
```

Dies staerkt die Notwendigkeit einer diskreten Charge-State-/Kollisionsclosure aus A-4.

## 8. Coulomb-Energieskalen

Die ungescreente Coulombenergie fuer eine Elementarladung betraegt grob

```text
at r_s:       ~9.70 MeV
at lambda_TF: ~48.8 eV
at a_i:       ~12.1 eV.
```

Damit kann eine winzige BH-Nettoladung die innerste geladene Teilchendynamik stark beeinflussen, waehrend das Feld in der aeusseren dichten Materie schnell abgeschirmt wird.

## 9. Wie lange bleibt ein Fe-Kern kohärent?

Als reine Tidal-Binding-Skala fuer Fe-56 mit

```text
R_n ~4.6 fm
binding ~8.8 MeV per nucleon
```

liefert der Vergleich BH-Tidalenergie gegen Bindungsenergie bei `M=1e11 kg`

```text
r_tidal ~5.5e-15 m ~37 r_s.
```

Das bedeutet nur: **BH-Tiden allein** zerlegen einen Fe-Kern in diesem groben Proxy erst in der unmittelbaren Femtometer-Near-Zone. Hohe Kompression, Stosse, Elektroneneinfang, Neutronisierung oder andere Reaktionen koennen die Zusammensetzung schon vorher aendern und muessen separat ueber Zeitskalen entschieden werden.

Der kohärente KG-Fe/Ni-Wert ist deshalb ein kontrollierter Zwischenkanal, nicht automatisch die Horizon-Komposition.

## 10. Innerer Single-pass-Flux gegen aeusseren Supply

Nur als diagnostischer Hintergrundfluss kann man

```text
Mdot_single = rho * v * sigma_Fe
```

mit `rho=PREM center` und `v=c_eff` bilden. Daraus folgt

```text
Mdot_single ~3.12e-14 kg/s
            ~9.84e-7 kg/year
rest-energy equivalent ~2.8 kW.
```

Dies ist **keine untere Grenze und keine finale Rate**. `c_eff` ist keine mikroskopische Teilchengeschwindigkeit, und dichte Materie ist innerhalb `r_B` kollisional/recyclingfaehig.

Der historische Michel-Supply-Benchmark fuer `1e11 kg` lautet dagegen

```text
1.47e-8 ... 1.46e-7 kg/s
= 0.464 ... 4.61 kg/year.
```

Die Luecke zwischen beiden Proxies betraegt damit

```text
factor ~4.7e5 ... 4.7e6.
```

Genau diese Luecke ist jetzt der zentrale offene Transportparameter:

```text
outer collisional supply
<-> kinetic recycling / phase-space refill
<-> inner absorbing sink.
```

Da der Fe/Ni-Wellensink selbst nahezu klassisch absorbiert, kann diese Luecke **nicht mehr pauschal auf Quantum/Wave-Suppression geschoben werden**.

## 11. Langzeit-Stressproxy

Wenn man rein als Stressgrenze die bisherigen Michel-Benchmarks weiter mit `dM/dt=kM^2` behandelt, ergeben sich fuer eine heutige Masse `M` und 4.54 Gyr Rueckwaertsintegration folgende ungefaehren Anfangs-/Heute-Verhaeltnisse:

```text
M=1e10 kg: 0.998 ... 0.980
M=1e11 kg: 0.979 ... 0.827
M=2e11 kg: 0.960 ... 0.705
M=5e11 kg: 0.905 ... 0.489
```

Dies ist kein Formationmodell und keine Vorhersage. Es zeigt lediglich, dass selbst der obere bisherige kleine Michel-Stressproxy bei `1e11 kg` keinen historischen Massenrunaway erzwingt; der `5e11 kg`-Oberrand ist deutlich sensibler.

Bei `1e11 kg` entsprechen die Michel-Benchmarks nur etwa

```text
0.0013 ... 0.013 TW
```

als extreme `eta=1` Restmassenleistungs-Skala und liegen damit weit unter dem globalen terrestrischen `~47 TW` Waermevergleich. Lokale Energieablagerung und reale Effizienz bleiben trotzdem offen.

## 12. Was A-5 jetzt tatsaechlich entscheidet

```text
Fe/Ni als falsche Spin-1/2-Behandlung: CLOSED/CORRECTED
massive scalar solver: PASS low-alpha external regression
coherent Fe-56 capture at 1e11 kg: CALCULATED, ~0.998 classical
coherent Ni-58 capture at 1e11 kg: CALCULATED, ~0.996 classical
large composite-wave suppression at 1e11 kg: NOT FOUND
charge screening scale: CALCULATED as atomic/sub-nm proxy
long-range Coulomb blocking of r_B supply: NOT SUPPORTED by screened proxy
final dense-core net Mdot: OPEN
```

## 13. Warum A-5 kein finaler Mdot-PASS ist

Die entscheidende unbekannte Groesse ist jetzt eine Transport-/Kompositionsclosure, nicht mehr der isolierte Wellenquerschnitt. Erforderlich sind mindestens:

1. Boltzmann/Fokker-Planck- oder aequivalente kinetische Recyclingloesung zwischen `r_B` und innerem Sink;
2. diskrete Fe/Ni-/Elektronen-Ladungszustaende und Screening;
3. Kollisionszeiten gegen Advektions-/Residenzzeit;
4. EOS-/Kompressionsprofil;
5. Kernreaktions-, Elektroneneinfang-, Dissoziations- und ggf. Neutronisationszeiten;
6. daraus die tatsaechliche species-resolved `Mdot_BH`.

Daher lautet der Status bewusst:

```text
Stage 3.69A-5: PARTIAL PASS / CLOSURE NARROWED
Stage 3.69 Full-Multiphysics: OPEN
```

## 14. Naechster Block

Der naechste echte Entscheidungsblock ist

```text
Stage 3.69B / A-6:
Kinetic Recycling + Charge-State + Nuclear/Composition Closure
-> actual net Mdot_BH.
```

Erst dieser Block kann entscheiden, wo innerhalb der grossen Spanne zwischen einem naiven Hintergrund-Single-pass-Flux und dem collisionalen Michel-Supply die reale Nettoakkretion liegt.

H+ und H0 bleiben dabei parallel. A-4/A-5 sind gemeinsame Materie-/Capture-Module; H+ erhaelt zusaetzlich Hawking-Emission, H0 nicht.

## Reproduzierbarkeit

- `stage3_69a5_dense_feni_closure.py`
- `STAGE3_69A4_CHARGED_DIRAC_FEEDBACK.md`
- `stage3_69a4_charged_dirac_feedback.py`

## Referenzen

- W. G. Unruh (1976), *Absorption cross section of small black holes*.
- C. Doran et al. (2005), *Fermion absorption cross section of a Schwarzschild black hole*.
- E. Jung, S. Kim, D. K. Park (2004), massive scalar/Dirac low-energy absorption and 4-D `1/8` relation.
- M. Cantiello et al. (2026), *Accretion of Primordial Black Holes in Stellar Interiors*, for the general collisional-outer / microphysical-inner multiscale methodology; their stellar parameter range is not numerically transplanted to Earth.
