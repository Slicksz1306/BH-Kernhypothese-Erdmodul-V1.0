# Stage 3.69L / A16 — Wärme- und 4.54-Gyr-Alterstest nach A13b

## Status

**UPDATED HEAT/AGE SENSITIVITY CALCULATED / NO HARD-BUDGET EXCLUSION / FULL THERMAL HISTORY STILL OPEN**

A16 wiederholt den früheren Wärme-/Alterstest mit dem neuen A13b Grant-Fit-Outer-Supply-Band.

Referenzen:

- Davies & Davies (2010): globaler Erdoberflächen-Wärmefluss `47 +/- 2 TW`.
- USGS radiometrische Altersskala: best estimate der Erde `4.54 Ga`.

Der `47 TW`-Wert wird hier ausschließlich als **harte Gesamtbudget-Vergleichsskala** benutzt. Eine zusätzliche zentrale Quelle dürfte in einem realen geophysikalischen Modell nicht automatisch das gesamte bekannte Budget beanspruchen.

## A13b Supply-Band

Bei `M=1e11 kg`:

```text
Mdot = 8.27e-8 ... 6.13e-6 kg/s.
```

Für den stationären Michel-Outer-Proxy wird lokal `Mdot~M^2` skaliert.

## Momentane maximale Restmassenleistung

Für die extreme Obergrenze `eta=1`:

```text
P = Mdot c^2.
```

| M_BH | P_min [TW] | P_max [TW] |
|---:|---:|---:|
| `1e10` | `7.43e-5` | `5.51e-3` |
| `1e11` | `7.43e-3` | `5.51e-1` |
| `2e11` | `2.97e-2` | `2.20` |
| `5e11` | `1.86e-1` | `13.76` |

Damit liegt selbst der höchste getestete A13b-Supply-Rand bei `5e11 kg` unter `47 TW`.

```text
hard total-heat-budget pre-test:
NO EXCLUSION within tested A13b supply envelope.
```

Das ist **kein vollständiger Wärme-PASS**. Der bekannte terrestrische Wärmefluss enthält radiogene, primordiale, Kern-/Mantel- und andere Beiträge. Ein BH-Beitrag von mehreren TW müsste in einem vollständigen Wärmehaushalt mit diesen Komponenten gemeinsam gefittet werden.

## 4.54-Gyr `Mdot=k M^2` Sensitivität

Wenn die momentane lokale Skalierung

```text
dM/dt = k M^2
```

über die gesamte Zeit mit konstantem `k` und unveränderter Umgebung fortgesetzt wird, gilt rückwärts

```text
M_initial = M_now / [1 + (Mdot_now/M_now) t_age].
```

Diese Annahme ist bewusst stark und dient nur als analytischer Sensitivitätstest; die Erde, EOS, Zusammensetzung und Backpressure-Randbedingungen waren über 4.54 Gyr nicht konstant.

### Niedriger A13b-Rand

| M_now | M_initial(4.54 Ga ago) | heutige M/Mdot |
|---:|---:|---:|
| `1e10` | `9.88e9 kg` | `383 Gyr` |
| `1e11` | `8.94e10 kg` | `38.3 Gyr` |
| `2e11` | `1.62e11 kg` | `19.2 Gyr` |
| `5e11` | `3.14e11 kg` | `7.66 Gyr` |

### Hoher A13b-Rand

| M_now | M_initial(4.54 Ga ago) | heutige M/Mdot |
|---:|---:|---:|
| `1e10` | `5.33e9 kg` | `5.17 Gyr` |
| `1e11` | `1.02e10 kg` | `0.517 Gyr` |
| `2e11` | `1.08e10 kg` | `0.259 Gyr` |
| `5e11` | `1.11e10 kg` | `0.103 Gyr` |

Alle algebraischen Rückwärtslösungen bleiben positiv. Es entsteht daher in diesem vereinfachten `kM^2`-Test **kein mathematischer Alterswiderspruch**.

Die hohen Raten zeigen aber eine wichtige neue Einschränkung: heutige Wachstumsskalen von `~0.10...0.52 Gyr` sind kurz gegenüber dem Erdalter. Solche Äste sind stark evolutionsempfindlich und würden bedeuten, dass sich die heutige Masse erst relativ spät stark vergrößert hat. Das ist ein **Fine-Tuning-/Evolution-pressure**, kein formaler Ausschluss.

Für `1e10 kg` ist diese einfache Integration besonders nicht selbstkonsistent, weil A15 dort über große Teile des Supply-Bands `Xi>1` findet und A11/A12 zeitabhängige Backpressure erzeugt.

## Integrierte Massenzunahme und mittlere Leistung

Selbst am hohen Supply-Rand bleibt die über 4.54 Gyr in dieser analytischen Rückwärtslösung hinzugekommene Masse winzig relativ zur Erdmasse. Der größte Fall (`M_now=5e11 kg`) hat

```text
Delta M ~4.89e11 kg
Delta M / M_Earth ~8.2e-14.
```

Die entsprechende über das Erdalter gemittelte `eta=1` Restmassenleistung beträgt nur etwa

```text
0.307 TW,
```

weil `Mdot~M^2` in der Vergangenheit bei kleinerer Masse stark niedriger war.

## Interpretation

A16 verschärft die frühere Aussage:

```text
A13b heat hard-budget:
not excluded by 47-TW total surface heat-flow scale.

A13b age algebra:
no direct 4.54-Gyr contradiction under fixed-k M^2 sensitivity.

high-supply branches:
strong nonlinear evolutionary/fine-tuning pressure.
```

Der nächste entscheidende Schritt ist Stage 3.70A: prüfen, ob Wärme, seismische Makrostruktur, Neutrinos oder andere reale Observablen eine strengere Grenze liefern als der rohe `47 TW`-Gesamtbudgetvergleich.

## Reproducibility

- `stage3_69l_a16_heat_age.py`

## Claims boundary

A16 ist kein Nachweis eines Erdzentrum-BH und kein vollständiges geothermisches Evolutionsmodell. Es ist ein aktualisierter harter Budget-/Alters-Sensitivitätstest auf Basis des A13b-Supply-Bands.
