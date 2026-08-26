# Stage 3.69C / A-7 – Collision-Regime Correction + Recycling/Escape + 1-D Bondi Boundary Test

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** A-6 COLLISION-TRANSITION SHORTCUT CORRECTED / REPEATED-ENCOUNTER CLOSURE SOLVED / 1-D BONDI BOUNDARY EXTREMES NUMERICALLY TESTED / REAL DENSE-FE TRANSPORT STILL OPEN

## Ziel

A-7 greift die letzte offene Transportfrage aus A-6 an und korrigiert dabei eine zu grobe Zwischenannahme.

Die zentrale Frage lautet nun genauer:

```text
Welche radiale Kollisionsphysik gilt im komprimierten Fe/Ni-Medium?

strongly coupled / condensed
    vs.
weakly coupled Coulomb plasma

und falls ein kinetischer Bereich entsteht:

miss -> recycle -> recapture
    vs.
miss -> permanent escape / back-pressure.
```

Diese Unterscheidung entscheidet, ob eine kleine Einzelpass-Capture-Fraktion die Gesamt-Mdot stark unterdruecken kann.

## 1. Korrektur zu A-6: `r_coll ~ lambda_geom` war nur ein grober Sensitivitaetsansatz

A-6 setzte als ersten Uebergangsproxy eine konstante geometrische Fe-Collision-Length von etwa

```text
lambda_geom,inf ~1.12e-10 m
```

in Beziehung zum Radius.

Gleichzeitig wurde fuer den inneren adiabatischen Branch

```text
rho ~ r^(-3/2)
T   ~ r^(-1)
```

verwendet.

Diese beiden Aussagen muessen radial selbstkonsistent kombiniert werden.

Wenn die effektive Collision-Cross-Section im **strong-coupling/geometric** Grenzfall nur schwach temperaturabhaengig ist, gilt

```text
lambda_mfp ~ 1/rho ~ r^(3/2)
Kn = lambda_mfp/r ~ r^(1/2).
```

Damit wird das Medium nach innen **kollisionaler**, nicht collisionless.

Am Bondi-Radius ist fuer den geometrischen Proxy

```text
Kn_B,geom ~1.83e-3.
```

Daraus folgt beispielsweise

```text
r/r_B = 1e-2 -> Kn_geom ~1.83e-4
r/r_B = 1e-4 -> Kn_geom ~1.83e-5
r/r_B = 1e-6 -> Kn_geom ~1.83e-6.
```

Unter diesem Grenzmodell existiert **kein innerer collisionless Uebergang**.

Daher wird die A-6-Aussage `r_coll~lambda_geom` nicht als physischer Endwert weiterverwendet.

## 2. Warum Cantiello trotzdem einen inneren collisionless Uebergang findet

Cantiello et al. (2026) behandeln ein heisses, schwach gekoppeltes Stellarplasma. Dort gilt fuer Coulomb-Streuung naeherungsweise

```text
lambda_C ~ T^2/(n lnLambda).
```

Mit

```text
T ~ r^-1
n ~ r^-3/2
```

folgt

```text
lambda_C ~ r^-1/2
Kn_C ~ r^-3/2.
```

Dann **waechst** der Knudsen-Parameter nach innen und ein kinetischer Uebergang ist moeglich.

Das ist kein Widerspruch: strong-coupling und weak-Coulomb sind verschiedene Transportregime.

Fuer den Erdkern ist gerade der Uebergang zwischen diesen Regimen Teil des noch fehlenden Dense-Fe-Transportmodells.

## 3. Ion-Coupling-Sensitivitaet

Mit

```text
T_inf = 6000 K
rho_inf = 13088.5 kg/m^3
a_i ~1.19e-10 m
```

als geophysikalische Referenzskala und

```text
Gamma_i = Z_eff^2 e^2/(4 pi eps0 a_i kT)
```

folgt am aeusseren Referenzzustand bereits fuer `Z_eff=1`

```text
Gamma_B ~23.35.
```

Das ist stark gekoppelt. Fuer groessere effektive Ionenladung steigt `Gamma` quadratisch.

Unter `rho~r^-3/2`, `T~r^-1` gilt

```text
Gamma(r) ~ Gamma_B sqrt(r/r_B).
```

Die reine `Gamma=1`-Sensitivitaet liegt bei

```text
Zeff=1:  r/r_B ~1.83e-3
Zeff=2:  ~1.15e-4
Zeff=4:  ~7.16e-6
Zeff=8:  ~4.48e-7
Zeff=26: ~4.01e-9 ~1.66 r_s.
```

Diese Zahlen sind **keine Ionisationsrechnung**. Sie zeigen aber, warum eine sofortige Spitzer/weak-plasma-Behandlung von dichter Erdkernmaterie nicht gerechtfertigt ist.

## 4. Weak-Coulomb-Branch als parametrischer Gegen-Grenzfall

Falls ein schwach gekoppeltes Coulombplasma entsteht, kann man die unbekannte aeussere Coulomb-Kollisionalitaet durch

```text
Kn_C(r_B) = K_B
```

parametrisieren.

Aus

```text
Kn_C(r)=K_B (r/r_B)^(-3/2)
```

folgt der kinetische Uebergang

```text
r_coll/r_B = K_B^(2/3).
```

A-7 scannt bewusst mehrere Werte statt einen nicht belegten Earth-Wert vorzugeben:

| `K_B` | `r_coll/r_B` | `p_single` | Recycling-Sinkkapazitaet / oberer Michel-Benchmark |
|---:|---:|---:|---:|
| `1e-4` | `2.15e-3` | `7.50e-6` | `3.12` |
| `3e-4` | `4.48e-3` | `3.61e-6` | `0.50` |
| `1e-3` | `1.00e-2` | `1.62e-6` | `0.067` |
| `3e-3` | `2.08e-2` | `7.77e-7` | `0.0107` |
| `1e-2` | `4.64e-2` | `3.48e-7` | `0.00143` |

Die Sinkkapazitaet ist hier nur

```text
M_reservoir / (t_cycle/p_single)
```

im adiabatischen Reduced Model.

Der Befund ist wichtig:

```text
Ein weak-Coulomb-Uebergang weit ausserhalb des alten A-6-Proxyradius
kann die innere Transportkapazitaet deutlich unter den Michel-Supply druecken.
```

Dann muss Back-pressure/Dichteaufbau die aeussere Rate korrigieren.

Im strong-coupling-Grenzfall entsteht dieser collisionless Flaschenhals dagegen nicht.

**Die unbekannte Dense-Fe-Kopplungs-/Ionisationsphysik ist damit der entscheidende Regime-Schalter.**

## 5. Exakte repeated-encounter Closure

Unabhaengig vom konkreten `r_coll` kann ein kinetischer Recyclingprozess als geometrischer Prozess geschrieben werden.

Pro Begegnung:

```text
p = capture probability
e = permanent escape probability
1-p-e = recycle probability.
```

Die Gesamtwahrscheinlichkeit, irgendwann eingefangen zu werden, ist exakt

```text
chi_capture = p/(p+e).
```

Das ist die mathematische Trennung zwischen Einzelpass-Capture und Gesamtakkretion.

Fuer den A-6-Referenzwert

```text
p_ref = 8.806e-6
```

braucht man fuer verschiedene dauerhafte Netto-Suppressionen:

| `chi_capture` | benoetigtes `e` pro Begegnung |
|---:|---:|
| `1.0` | `0` |
| `0.7` | `3.77e-6` |
| `0.3` | `2.05e-5` |
| `0.1` | `7.93e-5` |
| `0.01` | `8.72e-4` |
| `1e-3` | `8.80e-3` |
| `1e-4` | `8.81e-2` |
| `1e-5` | `0.881` |

Damit gilt:

```text
chi ~ p_single
```

nur dann, wenn **fast jeder verfehlte Durchgang dauerhaft entfernt wird**.

Wenn verfehlte Materie stattdessen re-thermalisiert und erneut eingespeist wird (`e -> 0`), dann gilt

```text
chi_capture -> 1
```

trotz sehr kleinem `p_single`.

Dies formalisiert den zentralen Cline-/Cantiello-Punkt ohne Meinungskomponente.

## 6. 1-D-Euler-Benchmark: absorbierender BH-Sink

A-7 enthaelt zusaetzlich einen eigenen zeitabhaengigen sphärischen Euler-Solver in dimensionslosen Bondi-Einheiten.

Gleichungen:

```text
d rho/dt + 1/r^2 d[r^2 rho v]/dr = 0

d(rho v)/dt + 1/r^2 d[r^2(rho v^2+p)]/dr
    = 2p/r - rho/r^2

dE/dt + 1/r^2 d[r^2 v(E+p)]/dr
    = -rho v/r^2.
```

Numerik:

```text
finite volume
HLL flux
logarithmic radial grid
Gamma=1.5 controlled ideal-gas benchmark
r_min=0.03 r_B
r_max=10 r_B.
```

Der analytische Bondi-Eigenwert ist fuer `Gamma=1.5`

```text
lambda_B = 0.5.
```

Mit absorbierender innerer Grenze liefert der numerische Lauf nach `0.4 r_B/c_inf`:

```text
r~0.04 r_B: Mdot/(4pi rho_inf c_inf r_B^2) ~0.490
r~0.20 r_B: ~0.490
r~0.50 r_B: ~0.497
r~1.00 r_B: ~0.501
r~2.00 r_B: ~0.501
r~5.00 r_B: ~0.501.
```

Damit reproduziert der einfache PDE-Prototyp den transsonischen Bondi-Massenfluss auf etwa Prozentniveau.

```text
1-D absorbing Bondi benchmark: PASS as reduced numerical self-check.
```

Dies ist kein Dense-Fe-EOS-PASS.

## 7. Reflektierende Grenze: wichtige Korrektur zur Sonic-Point-Interpretation

Als Gegenextrem wurde die innere Grenze voll reflektierend gesetzt.

Nach `0.4 r_B/c_inf` ist der innerste Inflow praktisch zusammengebrochen und eine Druck-/Schockstoerung hat bereits ungefaehr `0.5 r_B` erreicht, waehrend der Inflow bei `r~1 r_B` zu diesem Zeitpunkt noch nahezu unveraendert ist.

Nach `2 r_B/c_inf` liegt die Stoerfront bereits zwischen etwa `2` und `5 r_B`.

Damit ist eine A-6-Zwischenformulierung zu korrigieren:

```text
"inside sonic point -> outer supply can never react"
```

ist **zu stark**.

Richtig ist:

```text
Ein supersonischer Inflow ist gegen kleine lineare Rueckmeldungen von innen kausal abgeschirmt.

Aber eine dauerhaft reflektierende Grenze kann Materie/Druck aufbauen,
einen Schock erzeugen und die Stoerung langfristig nach aussen tragen.
```

Eine echte starke Akkretionsunterdrueckung durch Back-pressure ist damit physikalisch moeglich, wenn die innere Materie tatsaechlich reflektiert/gestaut wird.

## 8. Warum die reflektierende PDE-Grenze nicht mit kinetischem Recycling gleichgesetzt werden darf

Der PDE-Grenzfall wirft verfehlte Masse direkt wieder nach aussen und erzeugt maximalen Back-pressure.

Ein echter kinetischer Loss-Cone dagegen kann

```text
miss -> orbit -> return -> collision -> new angular momentum -> new attempt
```

durchlaufen.

Das ist ein anderer Prozess.

Deshalb sind die beiden A-7-Grenzen bewusst getrennt:

```text
A) perfect absorbing/recycling sink -> supply-nahe Mdot moeglich
B) perfect reflection/back-pressure -> starke Suppression moeglich.
```

Die reale `chi_transport` liegt zwischen diesen Grenzfaellen und wird durch

```text
permanent escape/outflow probability
+ collisional re-thermalization
+ cooling/circularization
+ EOS/compressibility
```

bestimmt.

## 9. Konsequenz fuer den bisherigen Erdbranch

A-7 **bestaetigt nicht** einfach Michel und **bestaetigt nicht** die Single-pass-Unterdrueckung.

Es schliesst stattdessen zwei falsche Kurzschluesse:

```text
FALSE 1:
small p_single -> automatically Mdot = p_single * Mdot_Bondi

FALSE 2:
kinetic transition inside sonic point -> inner back-pressure can never affect outer supply.
```

Der korrekte Status ist jetzt:

```text
Mdot_net is controlled by the fate of missed/recycled material.
```

Das ist deutlich enger als vor A-6/A-7.

## 10. Status A-7

```text
A-6 r_coll~lambda_geom as physical value: CORRECTED / withdrawn as endpoint
strong-coupling geometric radial Kn trend: CALCULATED -> more collisional inward
weak-Coulomb radial Kn trend: CALCULATED -> more collisionless inward
Earth dense-Fe regime switch: OPEN; requires ionization/coupling/EOS transport
repeated-encounter capture/escape closure: SOLVED analytically
absorbing 1-D Bondi benchmark: PASS at percent level
perfect-reflection back-pressure test: PASS as numerical counterexample
permanent sonic-point shielding claim: CORRECTED
exact Earth chi_transport: OPEN
final net Mdot: OPEN
```

## 11. Naechster Block

Der naechste Test ist jetzt nicht mehr ein abstraktes "Full HPC"-Problem, sondern konkret:

```text
Stage 3.69D / A-8:
Dense-Fe/Ni coupling + ionization + collision-frequency map
across r/r_B

-> determine whether/where Kn=1 actually occurs
-> feed that r_coll and charge state into the A-7 recycling/back-pressure solver
-> obtain the first defensible interval for chi_transport and net Mdot.
```

Danach kann ein 1-D real-EOS PDE-Lauf die verbleibende Spanne weiter schliessen.

H+ und H0 bleiben parallel. A-7 ist ein gemeinsamer Materie-/Transportblock.

## Reproduzierbarkeit

- `stage3_69c_a7_collision_recycling_pde.py`
- `stage3_69b_a6_reduced_closure.py`
- `stage3_69a5_dense_feni_closure.py`
- `stage3_69a4_charged_dirac_feedback.py`

## Referenzen

- M. Cantiello et al. (2026), *Accretion of Primordial Black Holes in Stellar Interiors*, arXiv:2606.02726, insbesondere Sec. II.2 und Appendix B. Dort gilt im weak-Coulomb Hot-Bondi-Regime `lambda_C ~ T^2/(n lnLambda)` und Recycling/self-collisionalization verhindert eine automatische Single-pass-Unterdrueckung.
- A. Loeb (2024), *Quantum-mechanical Suppression of Accretion by Primordial Black Holes*, arXiv:2409.09081.
- J. M. Cline (2024), Kommentar zu Loeb, arXiv:2409.12989.
- P. I. Dorogokupets et al. (2017), *Thermodynamics and Equations of State of Iron to 350 GPa and 6000 K*, Sci. Rep. 7, 41863, fuer die ~6000-K-Erdkern-Referenzskala.
