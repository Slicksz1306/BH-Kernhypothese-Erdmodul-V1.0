# Stage 3.69A-2 – Earth Single-Particle Validity Map

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** ELECTRON LOW-ENERGY BENCHMARK CONTROLLED / PROTON INTERMEDIATE-ALPHA NUMERICS REQUIRED

## Ziel

Dieser Schritt trennt zwei Fragen, die zuvor zu leicht vermischt werden konnten:

1. Wann ist die analytische Unruh/Doran-Low-Energy-Naeherung als Einzelteilchenbenchmark kontrolliert?
2. Wann muss der volle numerische Schwarzschild-Dirac-Matcher verwendet werden?

Dies bleibt eine **isolierte Einzelteilchenrechnung** und ist noch keine dichte Fe/Ni-Nettoakkretionsrate.

## Kontrollparameter

Unruh (1976) betrachtet die Dirac-Gleichung im Regime, in dem die dimensionslosen Energien in Einheiten der Schwarzschildskala klein sind. Mit Doran-

```text
alpha = G M_BH m/(hbar c)
E/m = gamma
```

ist ein nuetzlicher konservativer Gueltigkeitsindikator

```text
epsilon_U ~ 2 M E = 2 alpha gamma.
```

```text
epsilon_U << 1 : analytischer small-hole/low-energy Benchmark kontrolliert
epsilon_U ~ 1  : Uebergangsbereich; direkte numerische Regression erforderlich
epsilon_U > 1  : Unruh-Formel nicht als alleinige Projektantwort verwenden
```

Der aeussere PREM-Geschwindigkeitsproxy ist

```text
v = 10.4355 km/s
u=v/c = 3.48091e-5
gamma ~= 1.
```

## Kopplungs-/Gueltigkeitstabelle

| M_BH [kg] | alpha_e | epsilon_U,e | alpha_p | epsilon_U,p | Proton-Status |
|---:|---:|---:|---:|---:|---|
| 1e10 | 1.923e-5 | 3.846e-5 | 3.531e-2 | 7.062e-2 | low-energy/small-hole Benchmark gut kontrolliert |
| 1e11 | 1.923e-4 | 3.846e-4 | 3.531e-1 | 7.062e-1 | Uebergangs-/marginales Regime |
| 2e11 | 3.846e-4 | 7.692e-4 | 7.062e-1 | 1.412 | voller numerischer Matcher erforderlich |
| 5e11 | 9.615e-4 | 1.923e-3 | 1.766 | 3.531 | voller numerischer Matcher erforderlich |

Damit bleibt die Elektronen-Low-Energy-Naeherung ueber den gesamten kleinen Projektbereich sehr tief im kontrollierten Regime. Fuer Protonen verliert die analytische Naeherung dagegen gerade dort ihre alleinige Aussagekraft, wo der Projektmassenbereich durch `alpha_p~1` laeuft.

## Analytische Einzelteilchenwerte – nur mit Gueltigkeitskennzeichnung

Die Unruh/Doran-Formel liefert am PREM-Geschwindigkeitsproxy folgende **isolierte** Cross-Section-Benchmarks. Sie werden nicht automatisch als Netto-Capture-Raten verwendet.

| M_BH [kg] | sigma_classical [m^2] | sigma_e,Unruh [m^2] | sigma_e/classical | sigma_p,Unruh [m^2] | Proton-Verwendung |
|---:|---:|---:|---:|---:|---|
| 1e10 | 2.288e-24 | 3.566e-29 | 1.559e-5 | 6.345e-26 | kontrollierter Benchmark |
| 1e11 | 2.288e-22 | 3.455e-26 | 1.510e-4 | 6.345e-23 | nur Uebergangsbenchmark |
| 2e11 | 9.151e-22 | 2.764e-25 | 3.021e-4 | 5.076e-22 | nicht als finale Protonen-Cross-Section akzeptiert |
| 5e11 | 5.719e-21 | 4.319e-24 | 7.552e-4 | 7.931e-21 | nicht als finale Protonen-Cross-Section akzeptiert |

Der Elektronenbenchmark zeigt eine starke isolierte Wave-Capture-Unterdrueckung relativ zum klassischen collisionless Punktteilchenwert. Dies darf in dichter Materie **nicht** direkt als identischer Unterdrueckungsfaktor fuer die gesamte Massenakkretion interpretiert werden: elektrostatisches Ladungsfeedback, Kollisionen, Ionenbindung, Rekombination und Nachlieferung koppeln die Spezies.

## Numerische Konsequenz

Stage 3.69A ist damit jetzt aufgeteilt:

```text
A-1a: radial Dirac + current selfcheck                         PASS
A-1b: low-alpha asymptotic regression vs Unruh/Doran          PASS
A-2e: isolated electron low-energy benchmark                  CONTROLLED
A-2p: proton intermediate-alpha full matching                 OPEN
A-3 : charge/species feedback                                 OPEN
A-4 : dense collisional/kinetic closure -> net Mdot_BH        OPEN
```

Der naechste numerische Schwerpunkt ist der Protonenbereich

```text
alpha_p ~ 0.3 ... 2
```

mit einer asymptotischen Basis, deren hoehere Ordnungen bzw. Zwei-Seiten-Matching so weit gehaertet werden, dass publizierte Doran-Benchmarkkurven quantitativ und nicht nur qualitativ reproduziert werden.

## Referenzen

- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
