# Stage 3.69D / A-8 – Warm-Dense Fe/Ni + Weak-Reaction Timescales

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** STRONG-COUPLING REGIME MAP CALCULATED / EC THRESHOLDS LOCATED / PROMPT WEAK EQUILIBRIUM NOT SUPPORTED / FULL NETWORK-TRANSPORT CLOSURE OPEN

## Ziel

A-8 entscheidet, ob die in A-7 noch offene Regimegabel

```text
strong-coupling / condensed-WDM
versus
weak-coupling Coulomb / Spitzer
```

im relevanten inneren Fe/Ni-Bereich bereits durch einfache Skalen getrennt werden kann, und ob energetisch erlaubte Electron-Capture-Kanaele schnell genug sind, um die Zusammensetzung waehrend eines einzelnen inward transit wesentlich zu neutronisieren.

Dies ist bewusst **keine** NSE-/Reaktionsnetzwerkrechnung.

## 1. Aeusserer Referenzzustand

Verwendet werden weiterhin

```text
M_BH = 1e11 kg
rho_0 = 13088.5 kg/m^3
T_0 = 6000 K
c_eff = 10.4355 km/s
r_B = 6.12885e-8 m
r_s = 1.48523e-16 m.
```

Eisen bei etwa `13 g/cm^3` und `6000 K` liegt im Bereich etablierter inner-core EOS-/Transportrechnungen. Der Referenzzustand ist daher ein geophysikalischer Proxy, nicht bereits ein Plasma-Modell.

## 2. Reduzierte adiabatische Sensitivitaet

Als bewusst einfacher innerer Sensitivitaetsbranch wird verwendet

```text
x = r/r_B
rho ~ x^(-3/2)
T ~ x^(-1).
```

Damit folgen fuer einen stark gekoppelten geometrischen Kollisionsproxy

```text
a_i ~ x^(1/2)
Gamma_i ~ Z_eff^2/(a_i T) ~ x^(1/2)
lambda_geom ~ rho^(-1) ~ x^(3/2)
Kn_geom = lambda/r ~ x^(1/2).
```

Wesentlich:

```text
Kn_geom wird nach innen KLEINER.
```

Der strong-coupling-Branch erzeugt daher keinen inneren collisionless transition von selbst.

Am Bondi-Radius ergibt sich fuer voll ionisiertes Fe formal

```text
Gamma_i(Z=26) ~1.58e4
Kn_geom ~1.83e-3.
```

Die enorme Kopplung bedeutet nicht, dass das Material dort voll ionisiert ist; sie zeigt nur, dass eine weak-coupling-Spitzer-Formel nicht als Startannahme gerechtfertigt ist.

## 3. Elektronendegeneration

Der freie degenerierte Elektronenproxy aus A-5 liefert am aeusseren Referenzpunkt

```text
p_F/(m_e c) ~0.01841.
```

Da `n_e ~ x^-3/2` gilt,

```text
p_F ~ x^-1/2.
```

Relativistische Degeneration `p_F=m_e c` tritt im Sensitivitaetsbranch bei

```text
x_rel ~3.39e-4
r ~2.08e-11 m
  ~1.40e5 r_s.
```

auf.

## 4. Continuum Electron-Capture Schwellen

Aus den Atommasse-Differenzen werden als reduzierte kinetische continuum-EC-Schwellen verwendet:

```text
58Ni + e- -> 58Co + nu_e:
Q_kin ~0.381 MeV

56Fe + e- -> 56Mn + nu_e:
Q_kin ~3.696 MeV.
```

### 4.1 Ni-58

Der freie Fermi-Proxy erreicht `E_F,kin ~0.381 MeV` bei

```text
x_Ni ~1.66e-4
r ~1.02e-11 m
  ~6.84e4 r_s
rho ~6.14e6 g/cm^3
T ~3.62e7 K.
```

Ion coupling dort:

```text
Gamma_i(Zeff=26) ~203
Gamma_i(Zeff=20) ~120
Gamma_i(Zeff=10) ~30.
```

Damit bleibt die Ionenkomponente in diesem Sensitivitaetsbranch selbst bei deutlich reduzierter effektiver Ionisation stark gekoppelt.

### 4.2 Fe-56

Die Fe-Schwelle `E_F,kin ~3.696 MeV` liegt bei

```text
x_Fe ~5.08e-6
r ~3.11e-13 m
  ~2.09e3 r_s
rho ~1.14e9 g/cm^3
T ~1.18e9 K.
```

Ion coupling dort:

```text
Gamma_i(Zeff=26) ~35.6
Gamma_i(Zeff=20) ~21.0
Gamma_i(Zeff=10) ~5.26.
```

Auch hier ist `Gamma_i>1` fuer plausible hohe Ionisationszustaende.

## 5. Wann wuerde Gamma_i=1 erreicht?

Mit dem reduzierten vollionisierten Fe-Scaling folgt

```text
Gamma_i=1 erst bei x ~4.0e-9
r ~2.46e-16 m
  ~1.66 r_s.
```

Das ist keine Aussage, dass der simple EOS-Branch bis `1.66 r_s` physisch unveraendert gilt. Es ist eine wichtige **Konsistenzwarnung**:

```text
Eine weak-coupling Coulomb/Spitzer mean-free-path closure darf nicht schon bei viel groesseren Radien eingesetzt werden,
ohne dass eine explizite EOS-/Ionisations-/Kopplungsrechnung Gamma<<1 nachweist.
```

A-7s strong-coupling- und weak-Coulomb-Aeste sind deshalb keine gleichberechtigten willkuerlichen Fits; der aktuelle reduzierte Fe-Branch bevorzugt strong coupling bis sehr tief in die Near Zone.

## 6. Weak-Reaction-Zeitskala

Eine publizierte Rechnung fuer screened stellar electron capture auf `56Fe` liefert bei

```text
rho*Ye = 1e11 g/cm^3
T9 = 3
```

einen Wert von etwa

```text
lambda_ec(56Fe) = 1.5916e4 s^-1
```

also

```text
tau_ec ~6.28e-5 s.
```

Dieser Benchmark liegt bei **viel hoeherer Elektronendichte** als unser Fe-Schwellenpunkt und wird deshalb hier bewusst als aggressive, schnelle Vergleichsskala verwendet, nicht als interpolierte Erd-BH-Rate.

Am Fe-Schwellenradius liefert die lokale dynamische Sensitivitaet nur

```text
t_dyn ~4.75e-20 s.
```

Damit

```text
tau_ec / t_dyn ~1.3e15.
```

Bereits dieser extrem konservative Vergleich entscheidet:

```text
EC energetisch offen != weak equilibrium erreicht.
```

Ein einzelner inward transit ist viel zu kurz, um aus der blossen energetischen Oeffnung eines EC-Kanals sofortige Neutronisierung/NSE abzuleiten.

## 7. Externer astrophysikalischer Crosscheck

Stellare EC-Raten auf `56Fe` werden mit finite-temperature RPA/QRPA und experimentellen Gamow-Teller-Verteilungen berechnet und koennen modellabhaengig um ein bis zwei Groessenordnungen variieren. Das bestaetigt, dass ein einzelner Q-Wert keine Reaktionsrate festlegt.

Auch Type-Ia-Supernova-Modelle unterscheiden explizit zwischen hydrodynamisch/thermonuklear kurzen Zeitskalen und langsameren weak-reaction timescales; bei hinreichend schnellem Durchgang kann `Y_e` trotz hoher Temperatur weitgehend eingefroren bleiben.

## 8. Konsequenz fuer A-6/A-7

A-8 verschiebt die wahrscheinlichere reduzierte Closure in Richtung:

```text
outer dense Fe/Ni
 -> strongly coupled / degenerate inward compression
 -> no justified early Spitzer-collisionless switch
 -> wave sink near classical for coherent Fe/Ni
 -> repeated recycling unless a real backpressure/escape mechanism develops
 -> composition approximately frozen over one rapid inner transit
```

Das ist **noch kein Beweis**, dass die Michel-Rate bis zum Horizont unveraendert durchgeht. A-7 hat gezeigt, dass ein echter reflektierender Massestau einen outward shock/backpressure erzeugen kann.

Der zentrale offene Parameter bleibt daher:

```text
residence/recycling time versus escape/backpressure time.
```

Wenn Recycling die Aufenthaltszeit um viele Groessenordnungen verlaengert, koennen weak reactions trotz kurzer Einzeltransitzeit wieder relevant werden. Genau deshalb muss die finale Closure Transport und Reaktionsnetz gemeinsam entwickeln.

## 9. Status

```text
Earth-core Fe reference EOS scale: externally plausible
strong-coupling radial proxy: CALCULATED
weak-Spitzer branch before EC thresholds: NOT SELF-CONSISTENTLY JUSTIFIED
relativistic electron degeneracy radius: CALCULATED
58Ni EC energetic threshold: CALCULATED
56Fe EC energetic threshold: CALCULATED
prompt one-pass weak equilibrium/neutronization: NOT SUPPORTED
full residence-time + reaction-network closure: OPEN
final net Mdot_BH: OPEN
```

## 10. Naechster Schritt

A-9 muss nicht noch einen neuen Einzelteilchenquerschnitt rechnen. Der naechste entscheidende Block ist

```text
Stage 3.69E / A-9:
residence-time / backpressure transport
+ charge neutrality
+ minimal Fe/Ni weak network
-> self-consistent chi_transport
-> net Mdot_BH.
```

Dabei bleiben H+ und H0 parallel. Die Materieclosure ist fuer beide gemeinsam; H+ enthaelt zusaetzlich Hawking-Quellen/Senken.

## Reproduzierbarkeit

- `stage3_69d_a8_wdm_weak_timescales.py`

## Referenzen

- Dorogokupets et al. (2017), *Thermodynamics and Equations of State of Iron to 350 GPa and 6000 K*.
- Pourovskii et al. (2020), *Electronic correlations and transport in iron at Earth's core conditions*.
- Fantina et al. (2012), stellar electron-capture rates on `54,56Fe`.
- Ravlic et al. (2020), finite-temperature relativistic stellar electron-capture rates including `56Fe`.
- Liu & Luo (2013), screened EC rates for A=56 nuclei in pre-supernova conditions.
- Cantiello et al. (2026), multiscale collisional/kinetic PBH accretion methodology; stellar numerical values are not transplanted to Earth.
