# Stage 3.69A-1 – Schwarzschild-Dirac-Prototyp

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** RADIAL DIRAC INTEGRATION IMPLEMENTED / CURRENT SELF-CHECK PASS / IN-OUT MATCHING IMPLEMENTED / EARTH DENSE-MATTER CLOSURE OPEN

## Ziel

Dieser Schritt implementiert den ersten echten relativistischen Wellen-Solver fuer den Quantum/Wave-Capture-Block. Er liefert noch **keine finale H0-Akkretionsrate**, schliesst aber zwei zuvor offene numerische Teilprobleme:

1. massive Dirac-Gleichung auf festem Schwarzschild-Hintergrund mit regulaerem Horizon-Branch;
2. robuste Zerlegung der Fernfeldloesung in ein- und auslaufende Partialwellen zur Bestimmung von `S_kappa=A_out/A_in`.

Die finale Erd-Capture-Closure benoetigt weiterhin dichte Fe/Ni-Materie, Kollisionen, Zusammensetzung, Kernkohärenz/-dissoziation, Ladungsfeedback und Transport.

## 1. Radiale Dirac-Gleichung

Verwendet wird das System nach Doran, Lasenby, Dolan & Hinder (2005), in geometrischen Einheiten `G=hbar=c=1`, mit `M=1` und `x=r/M`:

```text
(1 - 2/x) dU/dx = B(x) C(x) U,
U = (u1,u2)^T,
```

mit dem Painleve-Gullstrand-Faktor

```text
B(x) = [[1, sqrt(2/x)],
        [sqrt(2/x), 1]].
```

Dieser `sqrt(2/x)`-Term ist wesentlich. Mit ihm bleibt der publizierte radiale Dirac-Strom numerisch erhalten.

Der regulaere Horizon-Branch verwendet `s=0` und

```text
a0 = kappa - 2 i (E+m) + 1/4
b0 = kappa + 2 i (E-m) - 1/4.
```

Der erste Taylor-Koeffizient wird aus der regularisierten Gleichung um `x=2` bestimmt.

## 2. Konservierter Strom – Selfcheck

Der verwendete Wronskian ist

```text
W_kappa = (u1 u2* + u1* u2)
          - sqrt(2/x) (|u1|^2 + |u2|^2).
```

Fuer den Testfall

```text
alpha = M m = 0.2
u = v/c = 0.5
x_start = 2 + 1e-6
x_end = 1000
```

bleibt der Strom fuer die niedrigsten beiden Partialwellen auf besser als `1e-9` relativ erhalten:

```text
kappa=-1: relative Drift ~3.68e-10
kappa=+1: relative Drift ~1.45e-11.
```

```text
Horizon branch + radial ODE integration: PASS as numerical self-check.
```

Dies ist nur ein Solver-PASS, kein empirischer PASS fuer H0.

## 3. In/Out-Matching

Dolan, Doran & Lasenby (2006) schreiben die Absorption ueber das Partialwellen-S-Matrix-Verhaeltnis

```text
S_kappa = A_out / A_in
```

und

```text
sigma_A = pi/p^2 * sum_(kappa != 0) |kappa| [1 - |S_kappa|^2].
```

Im Prototyp wird die bei grossem Radius integrierte Horizon-Loesung auf lokale ein-/auslaufende Eigenmoden der **exakten radialen Matrix** projiziert. Die lokalen Moden werden auf die Doran-Fernfeldstroeme

```text
W_in  = -2p/(E+m)
W_out = +2p/(E+m)
```

normiert. Dadurch konvergiert das Matching deutlich schneller als ein reines punktweises Leading-Order-Matching.

### Matchingradius-Konvergenz

Fuer `alpha=0.2`:

| E/m | x_match | sigma_A / M^2 |
|---:|---:|---:|
| 1.5 | 500 | 123.2562 |
| 1.5 | 1000 | 123.2594 |
| 1.5 | 2000 | 123.2587 |
| 2.0 | 500 | 103.9639 |
| 2.0 | 1000 | 103.9655 |
| 2.0 | 2000 | 103.9650 |

Damit ist die extrahierte Cross Section in diesen Benchmarkpunkten gegen eine Verdopplung/Vervierfachung des Matchingradius auf wenige `1e-5 ... 1e-4` relativ stabil.

```text
Asymptotic in/out matching: IMPLEMENTED.
Matching-radius stability: PASS for the tested benchmark points.
```

## 4. Physikalische Benchmarkstruktur

Die publizierten Doran-Rechnungen verlangen fuer `alpha~0.2` energieabhaengige Oszillationen um den klassischen Punktteilchenwert und bei hoher Energie Konvergenz gegen

```text
sigma_geo / M^2 = 27 pi = 84.8230.
```

Der aktuelle Solver liefert:

| E/m | Dirac `sigma/M^2` | klassisch `sigma/M^2` |
|---:|---:|---:|
| 1.5 | 123.259 | 128.680 |
| 2.0 | 103.965 | 103.380 |
| 5.0 | 89.682 | 87.174 |

Das reproduziert die **erwartete qualitative Benchmarkstruktur**: Unter-/Ueberschwingen relativ zur klassischen Kurve und Annaeherung an `27 pi` bei steigender Energie.

Wichtig: Eine pixel-/datenpunktgenaue Reproduktion der publizierten Doran-Figur ist noch nicht als separater Regressionstest hinterlegt. Daher wird der Status nicht als vollstaendige externe Kurvenvalidierung bezeichnet.

## 5. Erdbranch – analytischer Low-Energy-Einzelteilchenbenchmark

Am Referenzpunkt

```text
M_BH = 1e11 kg
v = c_eff = 10.4355 km/s
u = 3.4809e-5
```

liefert die von Doran zitierte Unruh-Low-Energy-Naeherung fuer isolierte Spin-1/2-Teilchen:

```text
electron:
  alpha_e = 1.92308e-4
  sigma_lowE ~= 3.4554e-26 m^2

proton:
  alpha_p = 3.53107e-1
  sigma_lowE ~= 6.3447e-23 m^2.
```

Zum Vergleich liegt der klassische collisionless Low-velocity-Punktteilchenbenchmark hier bei ungefaehr

```text
sigma_classical ~= 2.2878e-22 m^2.
```

Damit ist der isolierte Elektronenquerschnitt im schwachen Kopplungsregime stark quantenmechanisch unterdrueckt, waehrend der Protonenbenchmark wesentlich naeher am klassischen Wert liegt.

Diese Zahlen sind **keine Netto-Akkretionsrate der Erde**. Insbesondere duerfen unterschiedliche Elektronen-/Ionen-Capture-Raten nicht ohne elektrostatisches Ladungsfeedback fortgeschrieben werden.

## 6. Korrektur zur Fe/Ni-Komponente

Der fruehere reine Massen-/Kopplungscheck fuer einen `Fe-56`-Kern bleibt als Skalenhinweis brauchbar, aber **Fe-56 darf nicht mit demselben Dirac-Solver wie Protonen/Elektronen behandelt werden**:

```text
Fe-56 ground-state spin = 0+
Ni-58 ground-state spin = 0+.
```

Solange ein solcher Kern als kohärentes zusammengesetztes Teilchen erhalten bleibt, ist der passende erste Wellenproxy ein **skalare/Klein-Gordon-artige Capture-Rechnung plus Kernstruktur-/Finite-Size-Korrekturen**, nicht die Spin-1/2-Dirac-Gleichung.

Falls die Near Zone die Kerne dissoziiert oder neutronisiert, muss stattdessen auf Nukleonen-/Elektronenkomponenten und ihre jeweiligen Reaktions-/Transportzeiten umgeschaltet werden.

## 7. Konsequenz fuer Stage 3.69

Der Capture-Stack lautet jetzt genauer:

```text
outer PREM / material supply
 -> collisional-to-kinetic transition
 -> species/composition state
 -> electron/proton/neutron Dirac capture where applicable
 -> coherent Fe/Ni scalar/composite capture where applicable
 -> electrostatic charge feedback
 -> nuclear dissociation/reaction closure
 -> net Mdot_BH.
```

Formal bleibt

```text
Mdot_BH = sum_i Integral dE [ Mdot_i,supply(E,Q,t) * Gamma_i(E,Q,t) ],
```

aber `Gamma_i` ist nun explizit spin-, energie-, ladungs- und kompositionsabhaengig.

## 8. Status

```text
Schroedinger-Regimecheck: DONE.
Dirac radial equation: IMPLEMENTED.
Regular horizon boundary: IMPLEMENTED.
Current/Wronskian conservation: PASS as solver self-check.
In/out matching: IMPLEMENTED.
Matching-radius convergence: PASS at tested alpha=0.2 benchmark points.
Qualitative Doran benchmark behavior: reproduced.
Pixel/data-point regression against published Doran curve: OPEN.
Earth electron/proton isolated-particle low-E benchmarks: CALCULATED.
Coherent Fe/Ni capture: OPEN; requires scalar/composite treatment.
Charge-feedback closure: OPEN.
Dense-core species-resolved net Mdot: OPEN.
H0 thereby neither confirmed nor excluded.
```

## Reproduzierbarkeit

Code:

- `stage3_69a1_dirac_prototype.py`
- `stage3_69a_quantum_capture_regime.py`

## Referenzen

- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
- S. Dolan, C. Doran, A. Lasenby, *Fermion scattering by a Schwarzschild black hole*, Phys. Rev. D 74, 064005 (2006), arXiv:gr-qc/0605031.
- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
- NIST Atomic Data for Iron: dominant stable `Fe-56` isotope has nuclear spin `0`.
