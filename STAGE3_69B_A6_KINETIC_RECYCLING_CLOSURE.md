# Stage 3.69B / A-6 – Kinetic Recycling + Charge-State + Composition Closure

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** REDUCED KINETIC BRIDGE CALCULATED / PERSISTENT SINGLE-PASS SUPPRESSION NOT SELF-CONSISTENT WITHOUT ESCAPE/BACKPRESSURE / FINAL TIME-DEPENDENT NET MDOT STILL OPEN

## Ziel

A-6 verbindet die bereits berechneten A-3/A-4/A-5-Sinks mit dem aeusseren collisionalen Supply.

Die zentrale Frage ist jetzt:

```text
outer collisional supply
 -> collisional/kinetic transition
 -> loss cone + recycling
 -> charge-state / screening
 -> nuclear composition
 -> horizon sink
 -> net Mdot_BH.
```

A-6 ist bewusst ein **reduzierter Closure-Test**. Er ersetzt noch keinen zeitabhaengigen Dense-Fe-Hydro/Boltzmann-Solver.

## 1. Externer methodischer Crosscheck

Cantiello et al. (2026) behandeln fuer kleine PBHs im Sterninneren genau dieselbe strukturelle Schwierigkeit: Der Bondi-Radius ist kollisional, weiter innen wird die Stroemung kinetisch/collisionless, und ein grosser Teil der Teilchen verfehlt auf einem einzelnen Durchgang den GR-Loss-Cone.

Ihr Appendix-B-Ergebnis ist methodisch wichtig:

```text
missed particles recycle,
density pile-up shortens the mean free path,
the recycling region can self-collisionalize,
and a permanent single-pass suppression is therefore not automatic.
```

Ihre stellaren Zahlen werden **nicht** auf die Erde uebertragen. Verwendet wird nur die Struktur des Recycling-/Knudsen-Arguments.

Dies passt zur Loeb/Cline-Debatte von 2024: Eine Einzelteilchen-Verzoegerung oder kleine direkte Capture-Fraktion darf nicht automatisch mit derselben Unterdrueckung der gesamten stationaeren Akkretionsrate gleichgesetzt werden.

## 2. Aeusserer Bondi-/Materialradius bleibt kollisional

Am Referenzpunkt

```text
M_BH = 1e11 kg
rho_inf = 13088.5 kg/m^3
c_inf = 10.4355 km/s
```

liegt

```text
r_B = 6.12885e-8 m.
```

Aus der Fe-Ionenzahlendichte folgt

```text
a_i ~1.193e-10 m.
```

Ein rein geometrischer stark-gekoppelter Collision-Length-Proxy

```text
sigma_geom = pi a_i^2
lambda_geom = 1/(sqrt(2) n_i sigma_geom)
```

liefert

```text
lambda_geom ~1.124e-10 m
Kn_B = lambda_geom/r_B ~1.83e-3.
```

Damit ist die **rate-setting aeussere r_B-Zone im Projektproxy klar kollisional**.

Wichtig: Die A-5-Thomas-Fermi-Laenge `lambda_TF~2.95e-11 m` ist eine Screening-Skala und wird in A-6 nicht als Collision Mean Free Path missbraucht.

## 3. Kinetischer Uebergang

Als Sensitivitaet wird

```text
r_coll ~ lambda_geom/3 ... 3 lambda_geom
       ~3.75e-11 ... 3.37e-10 m
       ~6.1e-4 ... 5.5e-3 r_B
```

verwendet.

Damit liegt der kinetische Uebergang tief innerhalb des Bondi-/Materialradius und nicht bereits in der aeusseren Supply-Zone.

## 4. Direkter Loss-Cone am Uebergang

Nach dem Cantiello-artigen Einzelpass-Proxy

```text
ell_crit = 4 G M/c
sigma_perp ~= c_s/sqrt(gamma)
ell_typ ~= r_coll sigma_perp
f_cap ~= 0.5 (ell_crit/ell_typ)^2
```

und den einfachen inneren adiabatischen Skalen

```text
rho ~ r^(-3/2)
c_s ~ r^(-1/2)
```

folgt am nominalen `r_coll=lambda_geom`:

```text
ell_crit ~8.91e-8 m^2/s
ell_typ  ~2.12e-5 m^2/s
f_cap    ~8.81e-6.
```

Die Sensitivitaet ueber `lambda_geom/3 ... 3 lambda_geom` ergibt

```text
f_cap ~2.64e-5 ... 2.94e-6.
```

Damit ist bestaetigt:

```text
direct single-pass capture at the kinetic boundary is small.
```

Aber daraus folgt noch **nicht** dieselbe Unterdrueckung der stationaeren Netto-Mdot.

## 5. Recycling-Selbstkonsistenz

Fuer einen stationaeren Recyclingzustand schreibt die von Cantiello verwendete Skalierung schematisch

```text
xi ~ 2/f_eff,
```

wobei `xi` die residence-time/pile-up-Dichteerhoehung ist.

Wuerde man am nominalen Erd-Uebergang `f_eff=f_cap` setzen, ergäbe sich

```text
xi_direct ~2.27e5.
```

Gleichzeitig skaliert fuer kollisionsdominierte Materie grob

```text
lambda_mfp proportional 1/rho,
Kn_eff ~= Kn_0/xi.
```

Da `r_coll` gerade durch `Kn_0~1` charakterisiert wird, wuerde der direct-only-Zustand liefern

```text
Kn_eff ~4.4e-6.
```

Das ist ein Selbstwiderspruch der Annahme einer dauerhaft collisionless direct-single-pass Zone: Die zur Aufrechterhaltung des stationaeren Nachstroms notwendige Dichteanreicherung wuerde die Zone stark re-kollisionalisieren.

**A-6-Befund:**

```text
persistent global Mdot suppression = f_single * Mdot_supply
```

ist **nicht selbstkonsistent**, solange verfehlte Teilchen nicht effizient aus dem System entfernt werden, sondern in die kollisionsreiche Umgebung zurueckkehren.

Ein echter starker Suppressionsbranch braucht deshalb einen zusaetzlichen, quantitativ geloesten

```text
escape / back-pressure / outflow mechanism.
```

Ohne diesen Mechanismus fuehrt Recycling zur erneuten Angular-Momentum-Redistribution.

## 6. Sonic-Point-Sensitivitaet

Im einfachen adiabatischen Bondi-Proxy gilt fuer `1 < gamma < 5/3`

```text
r_sonic/r_B = (5 - 3 gamma)/4.
```

Am nominalen

```text
r_coll/r_B = 1.835e-3
```

liegt die Grenzsteifigkeit

```text
gamma_crit ~=1.66422,
```

bei der `r_sonic=r_coll`.

Beispiele:

```text
gamma=1.50 -> r_sonic=0.125 r_B
gamma=1.60 -> r_sonic=0.050 r_B
gamma=1.65 -> r_sonic=0.0125 r_B
gamma=1.664 -> r_sonic=0.0020 r_B.
```

Fuer `gamma_eff` merklich unter `5/3` liegt der kinetische Uebergang damit **innerhalb der bereits transsonischen/supersonischen inneren Zone**. Dann kann eine kleine innerste Loss-Cone-Aenderung den aeusseren Bondi-Supply nicht einfach quasistatisch beliebig reduzieren.

Bei einem nahezu exakt `gamma=5/3`-artigen degenerierten EOS liegt der Fall dagegen am Rand und muss numerisch geloest werden. Deshalb wird dieser Test als Sensitivitaet und nicht als endgueltiger PASS bezeichnet.

## 7. Kernzusammensetzung am kinetischen Uebergang

Unter dem gleichen adiabatischen Dichteproxy liegt am nominalen `r_coll`

```text
E_F,e ~47.2 keV.
```

Selbst bei der kleineren Sensitivitaetslaenge `lambda_geom/3` steigt der Proxy nur auf ungefaehr

```text
E_F,e ~142 keV.
```

Zum Vergleich aus Atommasse/Q-Werten:

```text
Fe-56 -> Mn-56 electron-capture threshold ~3.696 MeV
Ni-58 -> Co-58 electron-capture threshold ~0.386 MeV.
```

Damit erzwingt die einfache Kompression bis zum kinetischen Uebergang noch keine Fe/Ni-Neutronisierung.

Die BH-Gravitationsenergie pro Nukleon liegt dort nur bei ungefaehr

```text
0.2 ... 1.9 keV/nucleon
```

gegenueber typischen Kernbindungsenergien von mehreren MeV/Nukleon.

Daher bleibt am Uebergang der A-5-Kanal

```text
coherent/highly-ionized Fe/Ni nucleus
```

als plausibler erster Massentraeger erhalten. Nukleare Dissoziation/Neutronisierung kann tiefer innen auftreten und bleibt ein eigener Near-Horizon-Reaktionsblock.

## 8. Ladungsfeedback fuer die Bulk-Kerne

Eine positive BH-Ladung wirkt auf einen voll ionisierten Fe-/Ni-Kern schwaecher relativ zur Gravitation als auf ein Proton, weil `Z/A<1`.

Der einfache Fernfeld-Kraftgleichgewichtswert lautet bei `M_BH=1e11 kg`:

```text
Q_balance(Fe-56, Z=26) ~104 e
Q_balance(Ni-58, Z=28) ~100 e.
```

Die A-4-Regulationsbenchmarks liegen dagegen bei wenigen `e` bis etwa `24 e`.

Damit gilt selbst **ohne** Screening:

```text
A-4-sized positive charge does not fully repel the bulk Fe/Ni mass channel.
```

A-5 zeigt zusaetzlich, dass das Coulombfeld in dichter Fe-Materie auf atomaren/sub-nm Skalen gescreent wird und kein `r_B`-weiter Supply-Blocker ist.

Ein exakter charged-Klein-Gordon-Fe/Ni-Querschnitt bleibt fuer Feinheiten offen, aber ein kompletter elektrostatischer Bulk-Massenstopp wird durch die derzeitigen Ladungsskalen nicht gestuetzt.

## 9. Konsequenz fuer Loeb vs. Cline

Die bisherigen Projektresultate trennen nun drei Aussagen:

```text
1. Loeb-Punkt:
   Einzelteilchen-/Wellenphysik ist relevant und klassische Horizon-Extrapolation darf nicht blind benutzt werden.

2. Cline-Punkt:
   Eine Einzelteilchen-Verzoegerung oder kleine Einzelpass-Fraktion ist nicht automatisch dieselbe Unterdrueckung der Gesamt-Mdot.

3. Projektresultat A-3...A-6:
   Protonen- und Fe/Ni-Wellensinks sind bei 1e11 kg nicht stark unterdrueckt;
   ein direct-single-pass Transportfaktor ist wegen Recycling/Pile-up nicht selbstkonsistent als dauerhafter globaler Faktor.
```

Damit wird der Literaturstreit im Projekt nicht durch Meinung, sondern durch getrennte Solver-/Transporttests behandelt.

## 10. Was bedeutet das fuer die Netto-Mdot?

A-6 liefert **noch keinen exakten numerischen Earth-suppression factor** `chi`.

Der derzeit sinnvollste reduzierte Branch ist

```text
Mdot_net = chi_transport * Mdot_Michel,
```

wobei

```text
0 < chi_transport <= 1
```

und `chi_transport` aus dem noch fehlenden zeitabhaengigen Hydro/Kinetic-Interface folgen muss.

Die Ergebnisse sprechen gegen

```text
chi_transport ~= f_single ~1e-5
```

als stationaeren Wert ohne zusaetzlichen Escape-/Backpressure-Mechanismus.

Sie beweisen aber **nicht** `chi_transport=1`.

Als reine Sensitivitaet fuer `chi=0.1, 0.3, 0.7, 1` und die historischen Michel-Benchmarks bei `1e11 kg`:

```text
chi=0.1: Mdot ~1.47e-9 ... 1.46e-8 kg/s
chi=0.3: Mdot ~4.41e-9 ... 4.38e-8 kg/s
chi=0.7: Mdot ~1.03e-8 ... 1.02e-7 kg/s
chi=1.0: Mdot ~1.47e-8 ... 1.46e-7 kg/s.
```

Selbst `chi=1` entspricht nur

```text
0.464 ... 4.607 kg/year
P_rest(eta=1) ~0.00132 ... 0.0131 TW.
```

Im historischen `dM/dt=kM^2`-Stressproxy ergibt sich ueber 4.54 Gyr bei heutiger Masse `1e11 kg`

```text
M_initial/M_today ~0.979 ... 0.827
```

fuer den vollen Michel-Benchmark.

Damit ist bemerkenswert:

```text
Der 1e11-kg-H0-Branch benoetigt fuer den globalen Alters-/Waerme-Sanity-Check
keine gigantische Quantum-Suppression, um nicht sofort zu scheitern.
```

Lokale Waermeablagerung, EOS und reale Effizienz bleiben trotzdem Full-Stack-Outputs.

## 11. Status A-6

```text
outer r_B collisionality proxy: PASS (Kn_B~1.8e-3)
inner direct loss-cone fraction: CALCULATED (~1e-5 scale)
persistent global single-pass factor: NOT SELF-CONSISTENT without escape/backpressure
recycling/self-collisionalization: STRONGLY INDICATED in reduced closure
sonic-point causal shielding: FAVORED for gamma_eff <~1.664; exact dense-Fe EOS OPEN
Fe/Ni forced dissociation at r_coll: NOT FOUND
Fe/Ni forced electron-capture neutronization at r_coll: NOT FOUND
A-4-sized charge as complete Fe/Ni barrier: NOT SUPPORTED
exact chi_transport: OPEN
final dense-core net Mdot: OPEN but substantially narrowed conceptually
```

## 12. Naechster echter Solver

Der verbleibende Bossfight ist jetzt klar und deutlich kleiner als vorher:

```text
Stage 3.69C / A-7:
Time-dependent 1-D Dense-Fe Hydro/Kinetic Interface
+ realistic EOS
+ reflective/recycling kinetic boundary
+ charge-state transport
+ reaction source terms
-> solve chi_transport and net Mdot.
```

Das ist kein kompletter 3-D-HPC-Lauf. Ein konservativer 1-D radialer Solver reicht als naechster Falsifikationstest, weil die aktive Hypothese im ersten Schritt sphaerisch-zentral ist.

H+ und H0 bleiben parallel. A-6 ist ein gemeinsamer Materie-/Transportblock; H+ erhaelt zusaetzlich Hawking-Emission, H0 nicht.

## Reproduzierbarkeit

- `stage3_69b_a6_reduced_closure.py`
- `STAGE3_69A4_CHARGED_DIRAC_FEEDBACK.md`
- `STAGE3_69A5_DENSE_FENI_CLOSURE.md`

## Referenzen

- M. Cantiello, O. Gottlieb, C. Norton, M. Kleban, K. Van Tilburg (2026), *Accretion of Primordial Black Holes in Stellar Interiors*, arXiv:2606.02726, besonders Abschnitt 2.2 und Appendix B.
- A. Loeb (2024), *Quantum-mechanical Suppression of Accretion by Primordial Black Holes*, ApJL 975 L15, arXiv:2409.09081.
- J. M. Cline (2024), *Comment on "Quantum-Mechanical Suppression of Gas Accretion by Primordial Black Holes"*, arXiv:2409.12989.
- W. G. Unruh (1976), *Absorption cross section of small black holes*.
- C. Doran et al. (2005), *Fermion absorption cross section of a Schwarzschild black hole*.
- IAEA/KAERI nuclear mass/Q-value data for Fe-56, Mn-56, Ni-58 and Co-58.
