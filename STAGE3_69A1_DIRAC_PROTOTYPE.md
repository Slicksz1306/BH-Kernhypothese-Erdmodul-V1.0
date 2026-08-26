# Stage 3.69A-1 – Schwarzschild-Dirac-Prototyp

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** RADIAL DIRAC INTEGRATION IMPLEMENTED / CURRENT-CONSERVATION SELF-CHECK PASS / ASYMPTOTIC CROSS-SECTION MATCHING OPEN

## Ziel

Dieser Schritt implementiert den ersten echten relativistischen Wellen-Solver fuer den Quantum/Wave-Capture-Block. Er soll noch **keine finale H0-Akkretionsrate** liefern. Der aktuelle Meilenstein ist enger:

1. massive Dirac-Gleichung auf festem Schwarzschild-Hintergrund,
2. horizon-regulaere Painleve-Gullstrand-Darstellung,
3. physikalischer regulaerer Horizon-Branch,
4. radiale Integration nach aussen,
5. numerischer Erhaltungstest des radialen Dirac-Stroms.

Erst wenn anschliessend die asymptotische In-/Out-Amplitudenextraktion gegen publizierte Absorptionskurven reproduziert ist, wird eine numerische `sigma_abs` als physikalisches Projektergebnis akzeptiert.

## Gleichung

Verwendet wird das radiale System nach Doran, Lasenby, Dolan & Hinder (2005), in geometrischen Einheiten und mit `M=1`, `x=r/M`:

```text
(1 - 2/x) dU/dx = A(x) U,
U = (u1,u2)^T.
```

Die Painleve-Gullstrand-Kopplungsmatrix enthaelt `sqrt(2/x)`. Diese Form ist wesentlich: Mit ihr bleibt der publizierte radiale Strom/Wronskian numerisch erhalten.

Der regulaere Horizon-Branch verwendet `s=0` und den Horizon-Eigenvektor

```text
a0 = kappa - 2 i (E+m) + 1/4
b0 = kappa + 2 i (E-m) - 1/4.
```

Der erste Taylor-Koeffizient wird aus der regularisierten Gleichung um `x=2` bestimmt, statt direkt am singulaeren Nenner zu starten.

## Konservierter Strom

Der Selfcheck verwendet den radialen Wronskian

```text
W_kappa = (u1 u2* + u1* u2)
          - sqrt(2/x) (|u1|^2 + |u2|^2).
```

Fuer reale ungebundene Energien muss `W_kappa` entlang der Integration konstant bleiben.

## Benchmarklauf

Bewusst wird zuerst ein Literatur-nahegelegter dimensionsloser Testfall verwendet und **nicht** sofort die extrem kleine Erdgeschwindigkeit:

```text
alpha = M m = 0.2
u = v/c = 0.5
kappa = -1, +1
x_start = 2 + 1e-6
x_end = 1000
Integrator: DOP853
rtol = 1e-10
atol = 1e-12
```

Ergebnis:

| kappa | W_start | W_end | relative Drift |
|---:|---:|---:|---:|
| -1 | -1.10333333333345 | -1.10333333373963 | `3.68e-10` |
| +1 | -1.10333333333357 | -1.10333333334951 | `1.45e-11` |

Damit besteht die aktuelle radiale Integration den Stromerhaltungs-Selfcheck auf deutlich besser als `1e-9` relativ.

```text
Horizon branch + radial ODE integration: PASS as numerical self-check.
```

Das ist **kein** experimenteller oder physikalischer PASS fuer H0; validiert wird nur die interne Solver-Konsistenz dieses Teilmoduls.

## Asymptotisches Matching – noch offen

Die publizierte Absorptionsquerschnittsrechnung benoetigt fuer jede Partialwelle die Zerlegung

```text
U(r -> infinity) = alpha_kappa U_in + beta_kappa U_out
```

und danach die Partialwellensumme. Ein erster Leading-Order-Matching-Versuch zeigte noch zu starke Sensitivitaet gegen den Matchingradius bei kleinen Impulsen. Daher wird daraus **noch keine** `sigma_abs` berichtet.

Akzeptanzkriterien fuer den naechsten Substep:

1. Erhaltung des Wronskians weiterhin besser als `1e-8`.
2. Stabilitaet der extrahierten `|alpha_kappa|` gegen Matchingradius/-fenster.
3. Reproduktion der Doran-Kurve bei `alpha=0.2` innerhalb definierter numerischer Toleranz.
4. Reproduktion des Unruh-Low-Energy-Limits fuer `alpha << 1`.
5. High-energy-Konvergenz gegen den geometrisch-optischen Grenzwert.

Erst danach wird der Solver auf Protonen/Elektronen im Erdbranch angewandt.

## Analytischer Low-Energy-Grenzcheck

Doran et al. geben fuer niedrige Energie die Unruh-Naeherung

```text
sigma_abs/(GM/c^2)^2
 ~= 4 pi^2 (1+u^2) alpha
    / [u^2 sqrt(1-u^2)
       {1-exp(-2 pi alpha(1+u^2)/(u sqrt(1-u^2)))}].
```

Am Projekt-Referenzpunkt `M_BH=1e11 kg`, `u=10.4355 km/s / c` ergibt dies:

```text
electron: alpha_e = 1.92308e-4
          sigma_lowE ~= 3.4554e-26 m^2

proton:   alpha_p = 3.53107e-1
          formula gives ~= 6.3447e-23 m^2,
          but this is NOT accepted as final because alpha_p is already
          outside the clearly weak-coupling regime and full matching is required.
```

Fuer Fe-56 wird diese Low-Energy-Naeherung im starken Kopplungsbereich nicht extrapoliert.

## Konsequenz fuer Stage 3.69

Der aktuelle Stand ist jetzt feiner als zuvor:

```text
Schroedinger-Regimecheck: DONE.
Dirac radial equation: IMPLEMENTED.
Regular horizon boundary: IMPLEMENTED.
Current/Wronskian conservation: PASS as solver self-check.
Asymptotic in/out matching: OPEN.
Partial-wave sigma_abs: OPEN.
Species-resolved net Mdot: OPEN.
```

Damit ist Stage 3.69A-1 **teilweise durchgefuehrt**, aber noch nicht abgeschlossen.

## Reproduzierbarkeit

Code:

- `stage3_69a1_dirac_prototype.py`
- `stage3_69a_quantum_capture_regime.py`

## Referenzen

- C. Doran, A. Lasenby, S. Dolan, I. Hinder, *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020 (2005), arXiv:gr-qc/0503019.
- W. G. Unruh, *Absorption cross section of small black holes*, Phys. Rev. D 14, 3251 (1976).
