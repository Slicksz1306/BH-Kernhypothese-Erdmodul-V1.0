# Stage 3.69 / 3.70 – aktuelles Validierungsprotokoll

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 29.08.2026  
**Status:** Reduced/partial stack bis A19 gerechnet; Full-Multiphysics und eindeutige H0 Real-Data-Likelihood weiterhin offen

## Branches

```text
H+ = Standard-Hawking
H0 = ohne Hawking
```

H+ und H0 bleiben strikt getrennt. Gemeinsame Materie-/Capture-/Transportmodule gelten fuer beide; H+ besitzt zusaetzliche Hawking-Quell-/Emissionskanaele.

# Stage 3.69 – Multiphysics-Closure

Ziel:

```text
PREM / real Fe-Ni-light EOS
 -> thermodynamic outer supply
 -> WDM transport + Te/Ti relaxation
 -> recycling / permanent escape
 -> charge-state kinetics
 -> species wave capture
 -> weak/nuclear reactions
 -> time-dependent hydro feedback
 -> Mdot_BH(t), Q(t), energy deposition
 -> macroscopic observable profiles.
```

## Erledigte reduzierte/partielle Module

```text
A1/A3  Schwarzschild-Dirac + Earth-speed proton      PASS/CALCULATED
A4     charged proton + charge feedback              PARTIAL
A5     Fe-56/Ni-58 composite scalar capture          CALCULATED
A6/A9  repeated-encounter recycling closure          DONE
A7     collision-regime + Bondi backpressure         PARTIAL
A8     WDM/weak timescale gates                      CALCULATED
A10    first-principles-informed WDM transport shell PARTIAL
A11/A12 dynamic partial-sink/backpressure PDE        PARTIAL
A12b   Zbar + eta/k dissipative sensitivity          PARTIAL
A12c   relativistic stiff-EOS supply correction      CALCULATED
A13    general-EOS relativistic Michel solver        PASS regression / PARTIAL physical
A13b   Grant-2021 empirical-fit liquid-Fe anchor     PARTIAL CALCULATED
A14    dense-core electron screening/charge bracket  PARTIAL CALCULATED
A15    integrated reduced net-throughput audit       PARTIAL CALCULATED
A16    heat + 4.54-Gyr growth sensitivity            CALCULATED.
```

## Aktueller Supply-/Processing-Befund

A13b konservativer Grant-fit/T/intermediate-EOS Corner-Scan bei `M=1e11 kg`:

```text
Mdot_supply ~8.27e-8 ... 6.13e-6 kg/s.
```

Recoupling an A10 fast-envelope capacity:

```text
1e10 kg: Xi ~0.832 ... 61.60 -> supply/EOS/backpressure conditional
1e11 kg: Xi ~1.59e-3 ... 1.18e-1 -> processing-capable in tested stack
2e11 kg: Xi ~2.42e-4 ... 1.80e-2 -> processing-capable
5e11 kg: Xi ~2.00e-5 ... 1.48e-3 -> processing-capable.
```

Diese Aussagen sind **keine finale species-resolved Nettoakkretionsrate**.

## Stage-3.69 Abschlusskriterien

Stage 3.69 ist erst physisch geschlossen, wenn ein reproduzierbarer gekoppelter Solver mindestens liefert:

```text
Mdot_BH(t)
Q(t)
rho(r,t)
T_e(r,t), T_i(r,t)
Ye(r,t)
Fe/Ni/light-element composition fractions
transport / recycling / permanent escape
reaction-rate history
energy deposition / escaping luminosity
delta-rho, delta-Vp, delta-Vs or another unique macro observable.
```

Noch zwingend offen:

```text
- direct raw Zenodo / SESAME-92141 Fe-isentrope ingestion
- real mixture EOS over the intermediate/deep domain
- full two-temperature WDM transport/relaxation
- exact screened Coulomb-Dirac electron refinement
- stochastic few-e charge-state kinetics
- species/reaction-resolved final Mdot_BH(t).
```

# Stage 3.70 – branch-specific experimental falsification

## A17 / Stage 3.70A – Observability gate

Ergebnis:

```text
H+ Hawking anti-nu_e: real-data comparison available
H0 direct microscopic r_B seismology: not useful
H0 heat hard-budget: available, no exclusion
H0 macro seismology: model amplitude/profile missing
H0 matter-process neutrinos: model spectrum missing
exact spherical compensated surface monopole: degenerate.
```

Direkte r_B-Skalen-Seismik ist extrem sub-wavelength. Ein `lambda=1 km` Größenparameter liegt bei

```text
ka ~3.9e-11 ... 1.9e-9
```

fuer `1e10...5e11 kg`; ein `(ka)^4` Rayleigh-Proxy ist entsprechend winzig.

## A18 / Stage 3.70B – Current real-data audit

2026 SK-Gd Publikation, `25.29...31.29 MeV`:

```text
SK-IV observed 90% CL        0.04 cm^-2 s^-1 MeV^-1
SK-VI+VII NN observed        0.13
SK-VI+VII BDT observed       0.16.
```

Projekt-H+ Proxy:

```text
0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Damit bleibt:

```text
H+ FAIL in project reinterpretation vs strongest published SK-IV bin limit.
```

Die standalone 2026 SK-Gd-only Limits allein sind schwächer und würden den Projektproxy nicht ausschließen. Es wird keine offizielle Super-K-Erdzentrum-BH-Exklusion behauptet.

H0:

```text
REAL-DATA LIKELIHOOD NOT YET IDENTIFIABLE.
```

Grund: Es fehlt noch eine eindeutige vorhergesagte makroskopische Observable-Amplitude.

## Stage-3.70 Abschlusskriterium fuer H0

Mindestens eine aus Stage 3.69 kommende, **nicht frei fitbare** Vorhersage muss vorliegen, z.B.:

```text
predicted delta-rho(r), delta-Vp(r), delta-Vs(r)
OR predicted normal-mode frequency shifts
OR predicted central-scattering waveform amplitude/time structure
OR predicted thermal deposition profile with constrained background
OR predicted species/flavor/energy neutrino spectrum.
```

Dann:

```text
H0 model prediction
vs
PREM / seismic / heat / neutrino null model
-> detector/forward model
-> nuisance parameters fixed or physically prior-bounded
-> likelihood / Bayes factor / confidence interval
-> falsification or surviving parameter region.
```

Bis dahin darf Stage 3.70 fuer H0 nicht als PASS bezeichnet werden.

# Formation / Delivery – A19

Formation bleibt separat und stark negativ.

Optimistischer direct-Earth drag proxy bei `v_inf=220 km/s`:

```text
DeltaE/E_inf ~1e-18 ... 5e-17
```

fuer `1e10...5e11 kg`.

Capture-freundliche Ein-Durchgang-Geschwindigkeitsschwelle im selben Proxy:

```text
~0.004 ... 0.031 m/s.
```

Damit:

```text
normal halo -> direct Earth capture: VERY STRONG FAIL
standard Proto-Earth/planetesimal delivery: FAIL under tested conditions
cold/co-moving primordial seed: OPEN initial condition, origin not derived.
```

Neuere Drei-Koerper-PBH-Star-Capture-Arbeiten zeigen reale Mechanismen in anderen Massen-/Hostregimen, liefern aber keinen Earth-delivery Rescue fuer den Projektbereich.

# Aktueller Gesamtstatus

```text
H+:
  negative in strongest project Hawking-neutrino real-data comparison.

H0:
  internally quantitative reduced stack;
  not experimentally detected;
  full real-data likelihood not yet identifiable.

M>=1e11 kg:
  reduced inner processing-capable across tested A13b stack.

1e10 kg:
  supply/EOS/backpressure conditional.

Formation:
  one of the strongest remaining negatives.
```

# Naechste echte Pflichtpunkte

Nicht noch ein frei erfundener Reduced-Test, sondern die fehlenden physischen Closures:

```text
1. raw Fe isentrope / SESAME ingestion
2. full mixture + two-temperature WDM closure
3. final species/reaction-resolved Mdot_BH(t), Q(t)
4. unique macroscopic H0 observable
5. real Stage-3.70 likelihood on that observable
6. physically motivated formation/delivery mechanism.
```

Der wissenschaftliche Status bleibt:

**quantitative, reproduzierbare, falsifizierbare Hypothese; keine experimentell bestaetigte Theorie.**
