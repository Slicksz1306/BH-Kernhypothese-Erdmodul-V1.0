# Stage 3.69F / A-10 – First-Principles-Informed WDM Transport + Time-Dependent Sink Coupling

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** NEXT BLOCK / DEFINED / NOT YET CALCULATED

## Motivation

Stage 3.69E/A-9 hat die bisherige Transportunsicherheit deutlich eingegrenzt:

```text
M>=~1e11 kg:
    current strong-coupling/recycling Reduced Branch is supply-processing capable
    for tested atomic transition scales.

M=1e10 kg:
    backpressure-/transition-scale sensitive.
```

Der dominante verbleibende Modellproxy ist nun die angenommene strong-coupling/geometrische Mean-Free-Path-Skalierung

```text
lambda_mfp = lambda_0 x^(3/2).
```

A-10 muss diesen Proxy durch publizierte bzw. first-principles-informierte Warm-Dense-Matter-Transportphysik ersetzen.

## Ziel

```text
PREM/core boundary state
 -> WDM Fe/Ni EOS + average ionization
 -> electron-ion / ion-ion relaxation
 -> diffusion / conductivity / viscosity / stopping
 -> species- and energy-dependent escape/rethermalization
 -> time-dependent radial hydro/kinetic coupling
 -> A4/A5 absorptive inner boundary
 -> e_perm(r,E,species)
 -> chi_transport
 -> species-resolved Mdot_BH band.
```

## Mindestmodule

### 1. WDM EOS / Ionization

Fuer den komprimierten Fe/Ni-Pfad werden mindestens benoetigt:

```text
P(rho,T)
E(rho,T)
Zbar(rho,T)
mu_e(rho,T)
Gamma_i(rho,T,Zbar)
theta_e=kT/E_F.
```

Die bisherige einfache adiabatische Skalierung bleibt nur als Regression-/Sensitivity-Grenzfall.

### 2. Transportkoeffizienten

Statt einer konstanten geometrischen Collision-Cross-Section werden mindestens Sensitivitaetsbaender fuer

```text
nu_ei
nu_ii
D_i
eta_visc
kappa_thermal
stopping / momentum relaxation
```

benoetigt.

Methodisch bevorzugt:

- first-principles / DFT-MD / Kubo-Greenwood Daten wo verfuegbar;
- Potential-of-Mean-Force / effective-potential kinetic models fuer WDM;
- klar dokumentierte Extrapolationen ausserhalb publizierter Tabellenbereiche.

### 3. Escape-/Recycling-Closure

A-9 verwendete als Reduced Strong-Coupling-Proxy

```text
e_perm ~ f(v>v_esc) exp(-tau_coll).
```

A-10 soll stattdessen aus lokalen Transport-/Relaxationsraten ableiten:

```text
P_escape(r,E,species)
P_rethermalize(r,E,species)
P_capture(r,E,species).
```

Damit

```text
chi_transport
```

nicht als freier Faktor oder geometrischer Proxy eingeht.

### 4. Zeitabhaengige Hydro/Kinetik

Der bestehende A-7 1-D-sphaerische Euler-Prototyp wird erweitert um

```text
real absorptive inner sink
partial reflection/rethermalization from transport closure
energy source/sink terms
composition / charge advection
```

und muss Massenerhaltung explizit pruefen.

### 5. Innere Capture-Randbedingung

Die innere Randbedingung darf nicht als frei gewaehlt `absorbing` oder `reflecting` gesetzt werden.

Sie soll aus den bereits berechneten Teilmodulen folgen:

```text
A4: charged proton capture
A5: coherent Fe/Ni scalar capture
A8/A9: composition/weak-timescale gates.
```

Der charged-electron Coulomb-Fernfeldmatcher bleibt ein eigener offener Unsicherheitskanal und muss als Band behandelt werden, solange er nicht geloest ist.

## Massenscan

Pflichtpunkte:

```text
M_BH = 1e10 kg
       1e11 kg
       2e11 kg
       5e11 kg.
```

Besondere Aufmerksamkeit gilt dem von A-9 identifizierten kritischen Reduced-Bereich

```text
Mcrit ~5.8e9 ... 9.6e10 kg
```

weil dort kleine Aenderungen der Transportclosure in Backpressure oder freien Supply umschlagen koennen.

## Acceptance Criteria

A-10 gilt nur als numerisch bearbeitet, wenn:

1. `rho,T,Zbar` entlang des Pfads reproduzierbar berechnet oder tabelliert werden;
2. Transport-/Relaxationskoeffizienten Quellen und Gueltigkeitsbereiche besitzen;
3. `e_perm` aus Transportzeiten statt als freier Parameter entsteht;
4. der 1-D-Solver Massenerhaltung innerhalb definierter Toleranz zeigt;
5. absorbing- und reflecting-Grenzfaelle als Regression reproduziert werden;
6. der `1e10...5e11 kg` Massenscan konvergiert;
7. `Mdot_BH` als Unsicherheitsband ausgegeben wird;
8. WDM-/EOS-Extrapolationsunsicherheiten sichtbar bleiben;
9. kein Reduced PASS als experimentelle Bestaetigung bezeichnet wird.

## Falsifikationslogik

A-10 kann den Materiebranch in beide Richtungen haerten:

```text
if first-principles-informed transport gives e_perm << p
and no sustained backpressure:
    chi_transport -> near unity
    Mdot -> near outer supply benchmark.

if e_perm >> p or a stable backpressure solution forms:
    chi_transport << 1
    Mdot can be strongly suppressed.
```

Danach werden Langzeitmasse, lokale Energieablagerung und observables erneut mit der resultierenden `Mdot`-Spanne getestet.

## Branches

A-10 ist gemeinsamer Materietransport fuer H+ und H0.

```text
H+ additionally includes Hawking source/emission terms.
H0 has no Hawking term by definition.
```

Der bisherige H+-Neutrinobefund wird durch A-10 nicht aufgehoben.

## Referenzmethoden fuer A-10

Als methodische Ausgangspunkte dienen u.a. Arbeiten zu

- first-principles electron-ion coupling in warm dense matter;
- kinetic/effective-potential WDM transport;
- elektronischem Transport von Eisen unter Erdkernbedingungen;
- multiscale PBH accretion methodology.

Konkrete Werte werden erst nach Gueltigkeitspruefung in den Erdbranch uebernommen; stellare Parameter werden nicht numerisch auf den Erdkern transplantiert.
