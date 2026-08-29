# Stage 3.94 – Multi-Gate Closure Solver (F12 / A34 / H0)

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Quelle dieses Stands:** Chat-Arbeitsstand „F2 quantitativ weiterrechnen“  
**Status:** CORRECTED REDUCED SOLVER / 11/11 REGRESSION TESTS PASS / 50-POINT SWEEP PASS / PHYSICAL CLOSURES REMAIN OPEN

## Zweck

Stage 3.94 bündelt drei verbliebene reduzierte Gates in einem reproduzierbaren Modul:

1. **F12** – Primordial-origin / Poisson-amplification proxies.
2. **A34** – stationärer sphärischer Nernst-Planck/Bondi Drift-Diffusions-Sink.
3. **H0** – kompensierte Dichteperturbation im Erdkern mit reduziertem Seismik-Sensitivitätsproxy.

Die drei Blöcke sind Solver-/Closure-Arbeit. Sie sind **kein experimenteller Nachweis** eines schwarzen Lochs im Erdzentrum.

---

# 1. F12 – korrigierte Proxy-Definition

Default:

```text
N_seed       = 5.0e9
delta_target = 1
```

Poisson-Amplitude:

```text
delta_P = 1/sqrt(N_seed)
        = 1.414214e-5
```

Daraus werden ausschließlich dimensionslose Verstärkungs-Proxies abgeleitet:

```text
A_amp,proxy   = delta_target / delta_P
              = 7.0711e4

A_power,proxy = A_amp,proxy^2
              = 5.0000e9

Q_NG,proxy    = A_power,proxy - A_amp,proxy
              = 4.999929e9
```

## Wichtige Korrektur

Diese Größen werden **nicht** mehr als physikalischer Peak des primordialen Krümmungsleistungsspektrums `P_zeta(k)` und **nicht** als echtes `f_NL` bezeichnet.

```text
physical P_zeta peak = OPEN
physical f_NL        = OPEN
```

Für eine physikalische Primordialvorhersage fehlen insbesondere ein explizites Transfer-/Collapse-Modell, die Skalenabbildung `k <-> M`, ein konsistentes Fenster/Threshold-Modell und eine definierte Nicht-Gauß-Verteilung.

Status:

```text
F12 reduced proxy arithmetic: CALCULATED / REGRESSION PASS
physical primordial closure:  OPEN
```

---

# 2. A34 – stationärer Drift-Diffusions-Sink

Der korrigierte reduzierte Fluss lautet

```text
J_r = -D * Phi * [ dc/dr + (alpha/r^2) c ]
```

mit

```text
alpha = G M m / (k_B T).
```

Für die Randbedingungen

```text
c(r_sink) = 0
c(R)      = c_inf
```

ergibt sich die stationäre nach innen gerichtete Teilchenrate

```text
dotN =
4 pi D Phi alpha c_inf
---------------------------------------------
1 - exp[-alpha(1/r_sink - 1/R)].
```

Defaultparameter:

```text
D_eff      = 3.0e-9 m^2/s
T_core     = 5500 K
M_seed     = 1.0e11 kg
m_particle = 55.845 u
r_sink     = 6.13e-8 m
R          = 1.0e5 m
c_inf      = 1 m^-3
Phi        = 1
```

Ergebnis:

```text
alpha             = 8.1507e-6 m
alpha/r_sink      = 132.96
dotN(c_inf=1 m^-3) ~ 3.07273e-13 s^-1
```

Die analytische Konzentrationslösung erfüllt die beiden Randbedingungen. Die Rate skaliert linear mit der gewählten Referenzkonzentration `c_inf`.

## Aussagegrenze

`c_inf=1 m^-3` ist eine Normierungs-/Referenzdichte. Die ausgegebene Rate ist deshalb **keine finale reale Akkretionsrate**.

Vor allem gilt:

```text
A34 != final electrical Q_eq.
```

Die volle elektrische Closure benötigt weiterhin die bereits in A31 identifizierten multikomponentigen Transportgrößen:

```text
Onsager / Maxwell-Stefan mobility matrix
+ thermodynamic chemical-potential derivatives
+ sink-boundary coupling
+ self-consistent species concentrations / charge state.
```

Status:

```text
stationary reduced drift-diffusion solution: PASS
boundary/profile regression:                PASS
final multicomponent electrical Q_eq:       OPEN
```

---

# 3. H0 – kompensierte Kernperturbation

Der korrigierte Default verwendet einen positiven inneren Kern

```text
r_core      = 1 km
delta_rho_0 = 100 kg/m^3
```

mit Profil

```text
delta_rho(r)
= delta_rho_0 [1 - (r/r_core)^2],
0 <= r <= r_core.
```

Bis

```text
r_outer = 2 km
```

wird eine konstante negative Kompensationsschale eingesetzt. Ihre Dichte wird nicht frei gewählt, sondern aus

```text
integral 4 pi r^2 delta_rho(r) dr = 0
```

bestimmt.

Für den Default folgt exakt

```text
delta_rho_shell = -5.714286 kg/m^3.
```

Damit besitzt der reduzierte Perturbationsbranch keine Netto-Zusatzmasse innerhalb `r_outer`.

Das Python-Modul enthält zusätzlich einen transparenten Travel-Time-Sensitivitätsproxy, der lokal einen konstanten Bulkmodul annimmt:

```text
Vp(r) = Vp0 sqrt[rho0 / (rho0 + delta_rho(r))].
```

Dieser Term dient nur dazu, die Größenordnung einer durch das **gewählte** Perturbationsprofil verursachten Laufzeitänderung zu reproduzieren.

## Aussagegrenze

Die entscheidende offene Größe ist nicht die numerische Integration, sondern die physikalisch eindeutige Vorhersage von

```text
delta_rho(r),
delta_Vp(r),
delta_Vs(r)
```

aus dem H0-Branch selbst.

Daher:

```text
unique H0 prediction = OPEN
direct H0 detection  = NONE
```

Status:

```text
mass-compensated profile construction: PASS
mass-compensation regression:          PASS
reduced travel-time sensitivity:       CALCULATED
unique PREM/H0 seismic prediction:      OPEN
```

---

# 4. Regressionen

`test_stage3_94_multi_gate_closure.py` enthält 11 deterministische Regressionen:

```text
01 F12 Poisson delta
02 F12 amplitude proxy
03 F12 power proxy
04 F12 non-Gaussianity bookkeeping proxy
05 A34 alpha
06 A34 alpha/r_sink
07 A34 sink/outer boundary conditions
08 A34 linear c_inf rate scaling
09 H0 compensation-shell density
10 H0 zero-net-mass compensation
11 complete 50-point F12+A34+H0 smoke sweep
```

Lokaler Reproduktionstest dieses Repo-Updates:

```text
11/11 PASS
```

Der vollständige Sweep erzeugt je Gate 50 Punkte:

```text
F12: 50
A34: 50
H0 : 50
```

ohne Solverfehler.

---

# 5. Aktueller wissenschaftlicher Status nach Stage 3.94

| Gate | Stage-3.94 Ergebnis | Physische Closure |
|---|---|---|
| F12 | Proxy-Arithmetik + Sweep **PASS** | `P_zeta(k)` / echtes `f_NL` **OPEN** |
| A34 | stationärer Drift-Diffusionssolver **PASS** | finales multicomponent `Q_eq` **OPEN** |
| H0 | exakte Massenkompensation + Sensitivitätsproxy **PASS** | eindeutige `delta rho / delta Vp / delta Vs` Vorhersage **OPEN** |
| Experimentelle BH-Evidenz | keine | **NONE** |

Stage 3.94 schließt damit mehrere **numerische/formale** Fehlerquellen, aber nicht die drei zugrunde liegenden physikalischen Restbarrieren.

---

# 6. Reproduzierbare Dateien

```text
STAGE3_94_MULTI_GATE_CLOSURE.md
stage3_94_multi_gate_closure.py
test_stage3_94_multi_gate_closure.py
```

Ausführen:

```bash
python stage3_94_multi_gate_closure.py
python -m unittest -v test_stage3_94_multi_gate_closure.py
```
