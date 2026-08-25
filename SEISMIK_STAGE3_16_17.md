# Stage 3.16–3.17 – Externe Geophysik-Einwände und Smooth-Branch-Seismik

**Stand:** 25.08.2026  
**Status:** Modellhärtung / Forward-Test, kein empirischer Nachweis

## 1. Ausgangspunkt

Ein externer geophysikalischer Einwand betraf zwei Punkte:

1. Eine wörtliche redistributive Ersatzinterpretation könnte eine mechanisch instabile, materiearme Zentralzone erzeugen.
2. Ein starker zentraler Streukörper müsste eine nahezu stationsunabhängige zentrale Streuphase im Bereich von rund 20 Minuten erzeugen.

## 2. Stage 3.16 – Hard-Replacement wird verworfen

Wenn `M_PREM(<r_rep)=M_SL` als harte Exzision gewöhnlicher Materie innerhalb `r_rep` interpretiert wird, entsteht eine zentrale Kavität.

Bei etwa `P_c≈364 GPa` ergibt sich eine charakteristische Kugelkavitäts-von-Mises-Skala von ungefähr

```text
sigma_VM ~ 1.5 P ~ 546 GPa.
```

Das liegt weit über dem früher verwendeten dynamischen hcp-Fe-Festigkeitsbereich. Die Druckkollaps-Zeitskala beträgt grob:

```text
M_SL=1e16 kg:         ~1.08 s
M_SL~1.28e11 kg:      ~0.025 s
M_SL~2.28e11 kg:      ~0.030 s.
```

Der `R_hard`-Zweig wird daher als statischer Erdbranch verworfen.

## 3. Smooth compensated branch

Die redistributive Buchhaltung wird stattdessen als glatte Massenkompensation formuliert:

```text
rho_new(r) = rho_PREM(r) - M_SL w(r)
```

mit

```text
integral 4 pi r^2 w(r) dr = 1.
```

Damit bleibt Materie in der Near Zone vorhanden; `r_rep` ist nur noch eine Buchhaltungs-Skala und keine physische Vakuumgrenze.

Für das Stage-3.15-Band `M_SL~1.28e11–2.28e11 kg` ist die nötige verteilte Dichtekompensation extrem klein. Bei `R_mix=500 km` liegt sie je nach Profil nur in der Größenordnung `~1e-11–1e-10` relativ.

## 4. Zentralstreu-Laufzeit

Mit dem PREM-basierten P-Wellenprofil ergibt sich

```text
Zentrum -> Oberfläche ~606.77 s.
```

Ein realer zentraler Streuer würde bei flachen Ereignissen daher ungefähr

```text
~1210–1214 s  (~20.2 min)
```

nach dem Ereignis eintreffen und wäre im kugelsymmetrischen 1-D-Modell nahezu unabhängig von der Epizentraldistanz der Station.

Die Zeitgeometrie des externen Einwands wird damit bestätigt.

## 5. Stage 3.17 – Seismik des glatten Branches

Seismometer koppeln nicht direkt an den Ereignishorizont, sondern an Dichte, Druck und elastische Eigenschaften des Materials.

Für die glatte Kompensation wurden dieselben fixed-elastic-moduli-Proxies wie in den früheren Earth-Forward-Tests verwendet:

```text
V_new/V_ref = sqrt(rho_ref/rho_new).
```

### Verteilte PKIKP-180°-Laufzeitänderung

Für das Stage-3.15-Massenband:

```text
R_mix=100 km:      ~21–86 ns
R_mix=500 km:      ~0.8–3.5 ns
R_mix=1221.5 km:   ~0.14–0.58 ns.
```

Diese Werte liegen viele Größenordnungen unter der bisher verwendeten `0.041 s`-Vergleichsskala hochwertiger Kernphasen-Differentialmessungen.

### Selbst eine absichtlich scharfe Kompensationsgrenze

Für `R_mix=100 km` liegt die Normalinzidenz-Impedanz-Reflexionsamplitude nur ungefähr bei

```text
~6e-10 ... 1e-9,
```

mit Energieanteilen um `~1e-18`.

Ein glatter Taper besitzt diesen führenden Sprung gar nicht.

Daher ist die starke ~1212-s-Hard-Cavity-Streuphase **keine automatische Vorhersage** des `R_smooth`-Zweigs.

## 6. Unbekannte innere Near Zone

Für das Stage-3.15-Band liegt die PREM-Buchhaltungsskala nur bei

```text
r_rep ~133–161 m.
```

Wenn die lokale P-Wellengeschwindigkeit in diesem gesamten Bereich hypothetisch erhöht würde, ergibt der PKIKP-180°-Timing-Proxy ungefähr:

```text
+1% Vp:     ~0.23–0.28 ms
+10% Vp:    ~2.1–2.6 ms
+50% Vp:    ~7.9–9.5 ms
+100% Vp:   ~11.8–14.3 ms.
```

Die extreme Speed-up-Obergrenze, bei der die normale Laufzeit durch diese Zone vollständig verschwände, beträgt nur etwa `0.024–0.029 s`.

Eine lokale Verlangsamung kann anders reagieren und ist durch diese Speed-up-Grenze nicht abgedeckt.

## 7. Aktueller Status

- `R_hard` / zentrale Leerkugel: mechanisch verworfen.
- Die ~1212-s-Zeitgeometrie gilt für einen echten zentralen Streuer.
- `R_smooth`: verteilte Kompensation ist im aktuellen Seismikproxy praktisch unsichtbar.
- Ein starker zentraler Streuer ist im glatten Branch nicht automatisch vorhanden.
- Die noch ungelöste `~100 m`-Near-Zone bleibt der relevante seismische Zielbereich.
- Die bisherigen Hard-Vacuum-Earth-Matching-Ergebnisse dürfen nicht automatisch als Validierung des neuen `R_smooth`-Branches gelten.

## 8. Nächster Härtetest

Erforderlich ist ein selbstkonsistentes Near-Zone-Profil

```text
rho(r), Vp(r), Vs(r)
```

mit anschließendem vollständigem elastischen Full-Wave-/Antipodal-Array-Synthetic.

Es wird keine direkte Detektion eines Schwarzen Lochs im Erdzentrum behauptet.
