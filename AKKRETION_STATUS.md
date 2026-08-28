# Akkretions- und Langzeitstatus – V1.5

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Stand:** 29.08.2026  
**Forschungsstand:** Reduced/partial Materie-/Supply-/Transportstack bis A19; finale Full-WDM species-resolved Netto-`Mdot_BH` offen

## Aussagegrenze

Die reale BH-Akkretionsrate ist eine gekoppelte Größe:

```text
outer relativistic supply(EOS)
-> dense-matter transport/recycling/backpressure
-> composition + Te/Ti + reactions
-> stochastic charge state
-> inner wave capture
-> net Mdot_BH(t).
```

Daher gilt weiterhin:

```text
Mdot_net != automatisch Mdot_Michel
Mdot_net != automatisch p_single * Mdot_supply
historical Michel benchmark != universal supply rate.
```

# PREM-Außenrand

```text
rho_inf ~13.08848 g/cm3
P_inf   ~363.8521 GPa
K_S     ~1.4253 TPa
dK/dP   ~2.356
c_eff   ~10.4355 km/s.
```

Bei `M=1e11 kg`:

```text
r_B ~6.13e-8 m
r_s ~1.49e-16 m.
```

# Inner Capture / Recycling

Bei `M=1e11 kg`, Earth-speed:

```text
proton ~0.9503 classical
Fe-56  ~0.99754 classical
Ni-58  ~0.99646 classical.
```

Große kohärente Wave-Suppression wurde nicht gefunden.

Repeated encounters:

```text
chi_capture = p/(p+e_perm).
```

Deshalb ist ein single-pass capture factor kein stationärer Netto-Throughput-Faktor, wenn Misses im optisch dicken Reservoir verbleiben.

# A13 / A13b Outer Supply

A13 general-EOS Michel regression: **PASS**.

A13 Surrogat bei `1e11 kg`:

```text
Mdot_supply ~4.64e-8 ... 1.37e-6 kg/s.
```

A13b verwendet die publizierte Grant-2021 Liquid-Fe-Fitform bis `400 GPa` als experimentell verankerten Outer-EOS-Abschnitt.

Nominaler PREM-Randcheck:

```text
B_Grant ~1.419 TPa
K_PREM  ~1.425 TPa
ratio   ~0.9957.
```

Konservativer Grant-fit/T/intermediate-EOS Corner-Scan bei `1e11 kg`:

```text
Mdot_supply ~8.27e-8 ... 6.13e-6 kg/s.
```

Dies ist **kein finales physikalisches Konfidenzintervall**. Raw Zenodo / direct SESAME-92141 ingestion bleibt offen.

# A14 Dense-Core Charge

Diffuse equal-T Plasmaformel:

```text
Q_eq,diffuse ~+24.18e @1e11 kg.
```

Dense Thomas-Fermi-Screening über `Zbar~2.76...26`:

```text
E_F       ~19.4 ... 86.6 eV
lambda_TF ~4.29e-11 ... 2.95e-11 m
screened charge-response scale ~O(1...5e).
```

Recoupled Proton-Dirac:

```text
Q~+1.6e -> ~0.925 classical
Q~+4.9e -> ~0.867 classical.
```

```text
large electrostatic proton blocker: NOT FOUND
full screened Coulomb-Dirac electron S-matrix: OPEN refinement.
```

# A15 Integrated Reduced Throughput

A13b Supply gegen A10-fast Processing-Capacity:

| M_BH | Xi_min | Xi_max | Status |
|---:|---:|---:|---|
| `1e10` | `0.832` | `61.60` | **SUPPLY/EOS + BACKPRESSURE CONDITIONAL** |
| `1e11` | `1.59e-3` | `1.18e-1` | **PROCESSING-CAPABLE in tested stack** |
| `2e11` | `2.42e-4` | `1.80e-2` | **PROCESSING-CAPABLE** |
| `5e11` | `2.00e-5` | `1.48e-3` | **PROCESSING-CAPABLE** |

Damit ist für `M>=1e11 kg` im getesteten A13b-Stack die modellierte innere Processing-Capacity nicht der Engpass.

Für `1e10 kg` kreuzt der Supply die Capacity stark. A11/A12 zeigen bei Überlastung einen nach außen laufenden Backpressure-Shock; eine stationäre endliche Innenrate wurde nicht etabliert.

```text
final Full-WDM species-resolved net Mdot_BH: OPEN.
```

# A16 Wärme und Alter

A13b `eta=1` Restmassenleistung:

| M_BH | P_min [TW] | P_max [TW] |
|---:|---:|---:|
| `1e10` | `7.43e-5` | `5.51e-3` |
| `1e11` | `7.43e-3` | `0.551` |
| `2e11` | `2.97e-2` | `2.20` |
| `5e11` | `0.186` | `13.76` |

Vergleich mit `47 +/-2 TW` globalem Oberflächen-Wärmefluss:

```text
hard total-budget pre-test: NO EXCLUSION.
```

Das ist kein vollständiger geothermischer Quellenfit.

Beim analytischen fixed-environment `dM/dt=kM^2`-Rückwärtstest über `4.54 Gyr` bleiben alle Anfangsmassen positiv. Hohe Supply-Aeste haben jedoch kurze heutige `M/Mdot`-Zeiten bis `~0.10...0.52 Gyr` und damit starken Evolutions-/Fine-Tuning-Druck.

# Aktueller Netto-Mdot-Status

```text
historical Michel supply: LEGACY / EOS-SENSITIVE
A13 general-EOS machinery: PASS regression
A13b empirical-fit supply anchor: PARTIAL CALCULATED
A14 dense-core charge: PARTIAL, strongly constrained
M>=1e11 reduced inner processing: processing-capable in tested A13b stack
M=1e10: supply/EOS/backpressure conditional
raw tabulated Fe/Ni supply: OPEN
full mixture/two-temperature WDM: OPEN
final species/reaction-resolved net Mdot_BH(t), Q(t): OPEN.
```

# Was physisch noch fehlt

```text
1. raw Zenodo / direct SESAME-92141 isentrope ingestion
2. Fe/Ni/light-element mixture EOS over intermediate/deep density
3. Te/Ti relaxation + species transport
4. stochastic few-e charge kinetics / screened electron scattering refinement
5. weak/nuclear reactions where residence times permit
6. time-dependent hydro feedback with final sinks
7. final Mdot_BH(t), Q(t), energy deposition and macro profile.
```

Bis dahin darf der A13b Supply nicht als gemessene oder finale Earth-BH-Akkretionsrate bezeichnet werden.
