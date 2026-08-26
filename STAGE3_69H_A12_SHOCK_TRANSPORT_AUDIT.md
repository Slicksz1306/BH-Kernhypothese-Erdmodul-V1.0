# Stage 3.69H / A12 – Shock-Konvergenz + literaturgebundener Transportaudit

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** PARTIAL A12 CALCULATED / HIGH-RES SHOCK REGIME HARDENED / FULL TABULATED EOS+ZBAR+DISSIPATIVE PDE STILL OPEN

## Ziel

A12 sollte die zwei groessten A11-Restunsicherheiten angreifen:

```text
1e10-kg shock branch convergence
+
physically anchored viscosity / heat transport
+
EOS / ionization audit
```

Der aktuelle Block liefert einen echten Hochaufloesungs- und Transportaudit, aber noch keine vollstaendige tabellierte Fe/Ni-WDM-PDE.

## 1. Literaturkorrektur zu A10

A10 verwendete Wang et al. (Phys. Rev. E 89, 023101, 2014) als einen WDM-Fe-QMD-Transportanker.

Sjostrom & Crockett (Phys. Rev. E 97, 053209, 2018) untersuchten die Hochdruck-Pseudopotentialbehandlung kritisch und fanden eine deutliche Verbesserung gegenueber den frueheren Wang-QMD-EOS-Rechnungen. Deshalb wird Wang 2014 ab A12 nur noch als **Legacy-/Sensitivity-Anker**, nicht als alleinige harte WDM-Referenz, gefuehrt.

Der outer-core Transportanker bleibt unabhaengig durch Fe/FeNi first-principles/QMD gestuetzt, u.a.:

- Li et al., Scientific Reports 12, 21255 (2022): FeNi unter Erdkernbedingungen; `D_Fe~5.2e-9 m2/s`, `eta~8.5 mPa s` als zitierter Fe-Referenzpunkt; Ni-Diffusion `~2.47e-9...3.37e-9 m2/s` entlang der Kernadiabate.
- Vočadlo et al., Faraday Discussions 106 (1997): `D~5e-9 m2/s`, Viskositaetsproxy `~0.026 Pa s`.
- Li et al., JGR Planets 127 (2022): liquid-Fe `Cp` nahe Kernbedingungen wird mit `~850 J kg^-1 K^-1` gut approximiert.
- Xu et al., PRL 121, 096601 (2018) / accepted-manuscript discussion: outer-core thermal-conductivity scale around `77+/-10 W m^-1 K^-1`.

## 2. EOS-/Ionisationsdatenlage

Die belastbaren EOS-Anker sind inzwischen breiter:

- Sjostrom & Crockett 2018: QMD/five-phase Fe EOS, `rho~7...30 g/cm3`, `T~1...100 eV`.
- Blanchet et al., Phys. Rev. E 111, 015206 (2025): first-principles Fe EOS von `7.874...47.2 g/cm3` und `5500 K...1e9 K`, inklusive Analyse von Druck-/Thermalionisation.

Aber: Die veroeffentlichten Arbeiten liefern in der hier direkt zugaenglichen Form **keine vollstaendige numerische `Zbar(rho,T)`-Tabelle**, die ohne weitere Modellannahmen in die A11-PDE eingesetzt werden kann.

Daher wird kein erfundener `Zbar`-Datensatz konstruiert.

```text
full P(rho,T), E(rho,T), Zbar(rho,T), mu_e(rho,T) table:
OPEN
```

## 3. Physikalische Transportzahlen am Bondi-Massstab

Verwendete dokumentierte Sensitivitaetsbaender:

```text
rho0 = 13088.5 kg/m3
c_inf = 10.4355 km/s
Cp = 850 J/kg/K
eta = 8.5...26 mPa s
k = 67...87 W/m/K
```

Daraus fuer `L=r_B`:

| M_BH | r_B [m] | Re | Pe |
|---:|---:|---:|---:|
| `1e10 kg` | `6.129e-9` | `32.2...98.5` | `8.18...10.62` |
| `1e11 kg` | `6.129e-8` | `322...985` | `81.8...106` |
| `2e11 kg` | `1.226e-7` | `644...1970` | `164...212` |
| `5e11 kg` | `3.064e-7` | `1610...4924` | `409...531` |

**Befund:** reale Viskositaet und Waermeleitung sind relativ am wichtigsten am `1e10 kg`-Unterrand. Bei `>=1e11 kg` wird der Bondi-scale Flow deutlich advektionsdominierter.

Wichtig: Diese Zahlen rechtfertigen **nicht**, physikalische `k`/`eta` blind in den A11-constant-gamma-Energiesolver einzukleben. A11 besitzt keine thermodynamisch konsistente physische Temperaturvariable; dafuer wird zuerst eine echte EOS-/T-Abbildung benoetigt.

## 4. Hochaufloesungs-Shock-Konvergenz

Getesteter Branch:

```text
M=1e10 kg
Xi_high_fast=1.468052
A_cap=1/Xi_high~0.6812
gamma=1.5
```

Bei `t=0.8 r_B/c_inf`:

| N | shock_r/r_B | inner mdot (dimensionless, r~0.04r_B) |
|---:|---:|---:|
| 128 | `1.2692` | `~2.10e-2` |
| 256 | `1.2542` | `~1.63e-2` |
| 512 | `1.2328` | `~1.12e-2` |
| 1024 | `1.2293` | `~6.94e-3` |

Die Schockposition konvergiert deutlich schneller als der innere Flux.

```text
shock location: converging
finite nonzero stationary inner Mdot: NOT converged
```

## 5. Long-domain Test – der Shock ist nicht stationaer

Mit `N=256`, `rmax=30 r_B`:

| t [r_B/c_inf] | shock_r/r_B | inner mdot |
|---:|---:|---:|
| 0.8 | `1.260` | `~1.76e-2` |
| 1.2 | `1.741` | `~1.45e-2` |
| 1.6 | `2.220` | `~1.27e-2` |
| 2.0 | `2.682` | `~1.15e-2` |

Lineare Groessenordnung der Frontbewegung:

```text
d r_shock / dt ~1.19 c_inf
```

also etwa `12 km/s` in der aktuellen dimensionslosen Skalierung.

Damit wird die A11-Interpretation praezisiert:

```text
1e10 kg / capacity-limited branch:
NOT a demonstrated stationary shock-regulated solution.
It is an outward-propagating backpressure state in the current PDE/domain.
```

## 6. Conservation audit

Auch bei den Hochaufloesungslaeufen bleiben die diskreten Finite-Volume-Bilanzen auf Rundungsniveau:

```text
mass residual: typically ~1e-16...few 1e-15
energy residual: typically ~1e-16...few 1e-15
```

Die Nichtkonvergenz der inneren `Mdot` ist daher kein offensichtlicher Massenerhaltungsfehler.

## 7. Konsequenz fuer den Massensplit

### `1e10 kg`

A12 haertet den Backpressure-Befund, aber **nicht** zu einer stationaeren Endrate.

```text
outward shock / time-dependent suppression: CALCULATED
stationary shock-regulated Mdot: NOT ESTABLISHED
```

### `>=1e11 kg`

A10/A11 hatten `Xi_high<<1` und keinen capacity-driven partial sink. A12 findet keine neue Transportzahl, die diesen Ast automatisch umkehrt; `Re`/`Pe` werden mit Masse sogar groesser.

```text
>=1e11 kg current reduced supply-processing branch:
SURVIVES A12 transport-timescale audit
```

Dies ist weiterhin keine Full-WDM-Endvorhersage.

## 8. Was A12 noch nicht erfuellt

Die urspruenglichen Acceptance Criteria sind noch nicht komplett erreicht:

```text
full tabulated EOS: OPEN
full Zbar table: OPEN
physical viscosity term in EOS-consistent PDE: OPEN
physical heat conduction term in EOS-consistent PDE: OPEN
e-i relaxation term: OPEN
species-resolved advection: OPEN
charged-electron capture closure: OPEN
```

Der Grund fuer das bewusste Stoppschild ist methodisch: physikalische Transportkoeffizienten duerfen nicht an eine unphysikalische Temperaturabbildung gekoppelt werden.

## 9. Status

```text
A12 literature correction: DONE
A12 Re/Pe transport audit: CALCULATED
A12 N=128...1024 shock-position convergence: CALCULATED
A12 long-domain shock propagation: CALCULATED
A12 stationary 1e10 shock Mdot: NOT ESTABLISHED
A12 tabulated EOS/Zbar dissipative closure: OPEN
Stage 3.69 Full-Multiphysics: OPEN
```

Naechster Unterblock innerhalb A12:

```text
A12b:
obtain/reconstruct thermodynamically consistent Fe EOS table
+ explicit T(rho,e)
+ bounded Zbar(rho,T)
+ then add viscosity/conduction/e-i relaxation consistently
+ repeat 1e10 and >=1e11 dynamic scan.
```
