# Stage 3.70A / A17 — Observational Pre-Falsification Gate

## Status

**CALCULATED AS A READINESS/GATING TEST / FULL REAL-DATA LIKELIHOOD NOT YET IDENTIFIABLE FOR H0**

Stage 3.70A prüft nicht erneut interne Solverdetails, sondern welche realen Beobachtungskanäle mit dem heutigen A13b/A16-Modell überhaupt quantitativ testbar sind.

## Referenzdaten

- PREM (Dziewonski & Anderson 1981) wurde aus ungefähr 1000 Normalmodenperioden, hunderten Travel-Time-Zusammenfassungen, Q-Daten sowie Masse/Trägheitsmoment konstruiert; zusätzlich gingen sehr große P-/S-Phasendatensätze ein.
- Das IRIS/SAGE Earth Model Collaboration stellt PREM in maschinenlesbaren Tabellen öffentlich bereit.
- Für kleine elastische Inklusionen gilt im Low-frequency/Rayleigh-Regime `ka<<1`; die Streuung fällt mit einer hohen Potenz von `ka`. Dieser Block verwendet `(ka)^4` nur als Größenordnungs-Proxy, nicht als vollständige elastische Streuamplitude.

## Kanal 1 — H+ Standard-Hawking

Unverändert:

```text
H+ Standard-Hawking:
FAIL im getesteten Projekt-SK-IV-Reinterpretationsmodell.
```

Stage 3.70A ändert daran nichts und behauptet keine offizielle Super-K-Erdzentrum-BH-Exklusion.

## Kanal 2 — direkte Seismik der Near Zone

Mit

```text
r_B = G M / c_eff^2,
c_eff = 10.4355 km/s
```

folgt:

| M_BH | r_B |
|---:|---:|
| `1e10` | `6.13e-9 m` |
| `1e11` | `6.13e-8 m` |
| `2e11` | `1.23e-7 m` |
| `5e11` | `3.06e-7 m` |

Für eine bewusst aggressive kurze Vergleichswellenlänge von `1 km` ist

```text
ka = 2 pi r_B/lambda
```

nur

```text
3.85e-11 ... 1.93e-9.
```

Der einfache Rayleigh-Größenproxy `(ka)^4` liegt damit etwa bei

```text
2.2e-42 ... 1.4e-35.
```

Bei `10...100 km` Wellenlänge fällt der Proxy nochmals um 4 bis 8 Größenordnungen.

Daraus folgt:

```text
direct seismic scattering by the microscopic r_B-scale near zone:
NOT A USEFUL OBSERVATIONAL CHANNEL.
```

Das ist keine Aussage darüber, ob **makroskopische** Dichte-/Elastizitätsänderungen durch langfristige Akkretion/Backpressure messbar wären.

## Kanal 3 — makroskopische zentrale Streustruktur

Externes geophysikalisches Feedback hat einen sinnvollen Test vorgeschlagen: Eine hinreichend große zentrale Dichte-/Geschwindigkeitsanomalie könnte nach großen Erdbeben eine nahezu weltweit kohärente, zentrumsgebundene Streuphase erzeugen; als PREM-Zeitskala wurde ungefähr `1212 s` für flache Ereignisse genannt.

Der heutige smooth-compensated Branch enthält jedoch **noch keine berechnete km-skalige**

```text
delta rho(r)
delta Vp(r)
delta Vs(r)
Q_mu(r), Q_kappa(r)
```

für eine solche Struktur. Deshalb kann eine Nichtbeobachtung dieser Phase noch nicht in eine Likelihood gegen den heutigen kleinen Branch übersetzt werden.

Der Test wird als Stage-3.70-Ziel beibehalten:

```text
PREM null model
vs
PREM + predicted macroscopic central perturbation
-> synthetic waveforms / normal modes / travel-time residuals
-> likelihood against public seismic data.
```

## Kanal 4 — Wärme

A16 liefert für `eta=1`:

```text
M=1e11: max ~0.551 TW
M=2e11: max ~2.20 TW
M=5e11: max ~13.76 TW.
```

Alle liegen unter der groben globalen `47 +/-2 TW`-Oberflächen-Wärmefluss-Skala.

```text
hard total-budget test:
NO EXCLUSION.
```

Ein strenger Test muss aber die bekannte radiogene/primordiale/core-mantle Aufteilung gemeinsam fitten. Mehrere TW einer neuen Quelle können nicht allein deshalb als kompatibel gelten, weil sie kleiner als 47 TW sind.

## Kanal 5 — Materieprozess-Neutrinos

A8 zeigte, dass energetisch erlaubte Electron-Capture-Schwellen nicht automatisch promptes Weak-Equilibrium bedeuten. Stage 3.70 kann diesen Kanal erst nutzen, wenn A15/Full-WDM eine species- und residence-time-resolved Reaktionsrate sowie ein Neutrinospektrum liefert.

```text
matter-process neutrino likelihood:
NOT READY.
```

## Kanal 6 — äußeres Gravitationsfeld

Für eine exakt sphärische, massenerhaltende Redistribution innerhalb eines Radius bleibt das äußere Newtonsche Monopolfeld nach dem Schalentheorem unverändert.

Damit ist

```text
surface g alone
```

kein eindeutiger Test eines perfekt sphärisch kompensierten Branches.

Empfindlich bleiben dagegen, falls das Modell entsprechende makroskopische Änderungen erzeugt:

- Trägheitsmoment / radiale Massenverteilung,
- Normalmoden,
- nicht-sphärische Komponenten,
- Rotations-/Magnetfeldkopplung,
- zeitabhängige Strukturänderungen.

## A17 Observability Gate

| Kanal | heutiger Status |
|---|---|
| H+ Hawking-Neutrino | **FAIL im getesteten Projektmodell** |
| H0 direkte r_B-Seismik | **physikalisch unbrauchbar / extrem sub-wavelength** |
| H0 makroskopische Seismik | **OPEN — amplitude/profile prediction fehlt** |
| totaler Wärme-Hard-Budget-Test | **NO EXCLUSION** |
| vollständiger Wärmequellen-Fit | **OPEN** |
| Materieprozess-Neutrinos | **OPEN — spectrum/rate fehlt** |
| äußeres sphärisches Monopolfeld | **degeneriert bei exakter Kompensation** |
| Trägheitsmoment/Normalmoden | **OPEN — final macro profile fehlt** |
| direkte Detektion | **keine** |
| eindeutige positive Signatur | **keine** |

## Zentrale Schlussfolgerung

Stage 3.70 ist heute **nicht primär dadurch blockiert, dass öffentliche Erddaten fehlen**. PREM, Normalmoden- und seismologische Referenzdaten existieren.

Der Engpass ist, dass H0 noch keine eindeutige, makroskopische und quantitativ vorhergesagte Observable liefert, die gegen diese Daten gefittet werden kann.

Damit wird der nächste wissenschaftliche Pflichtsatz:

```text
Full-WDM/multiphysics must output a unique macro observable amplitude/profile.
Without that, a real-data likelihood cannot confirm or falsify H0 uniquely.
```

## Reproducibility

- `stage3_70a_a17_prefalsification.py`

## Claims boundary

A17 ist ein Falsifikations-Readiness-Test, kein experimenteller Nachweis und kein H0-PASS.
