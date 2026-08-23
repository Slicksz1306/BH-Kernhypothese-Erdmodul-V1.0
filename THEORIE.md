# BH-Kernhypothese – Erdmodul V1.0

**Autor:** Daniel Marcel Schlicksupp  
**Geburtsdatum:** 13.06.1988  
**Region:** Rheinland-Pfalz  
**Land:** Deutschland  
**Version:** V1.0  
**Stand:** 23.08.2026

## 1. Forschungsfrage

Das Erdmodul untersucht die Hypothese, dass im Zentrum der Erde eine kompakte, schwarzlochartige Zentralmasse existieren könnte. Das Modell wird ausdrücklich gegen bekannte geophysikalische Randbedingungen geprüft und beansprucht keine experimentelle Bestätigung.

Die starke Variante, nach der ein Zentral-BH den überwiegenden Teil der Erdmasse beziehungsweise Erdgravitation trägt, wird in V1.0 verworfen. Geprüft bleibt nur eine deutlich kleinere Zentralmasse als separate Hypothese.

## 2. Nullmodell und Massenbuchhaltung

Als geophysikalisches Nullmodell dient PREM (Preliminary Reference Earth Model).

Die Zentralmasse wird nicht zusätzlich zur gemessenen Erdmasse addiert. Sie ersetzt im Modell genau die normale PREM-Masse innerhalb eines Ersatzradius `r_rep`:

```text
M_PREM(<r_rep) = M_c
```

Außerhalb dieser Region bleibt die eingeschlossene Gesamtmasse unverändert:

```text
M'(<r) = M_PREM(<r),  r >= r_rep
```

Damit bleibt im ideal kugelsymmetrischen Fall auch das äußere Gravitationsfeld unverändert:

```text
g'(r) = g_PREM(r)
```

Ein kleines Zentralobjekt wäre daher nicht allein durch eine Messung der Oberflächengravitation nachweisbar.

## 3. Referenzwerte

Verwendete zentrale PREM-Größen beziehungsweise Referenzwerte:

```text
R_IC ≈ 1221.5 km
rho_c ≈ 1.31e4 kg/m^3
v_P ≈ 11.26 km/s
M_IC ≈ 9.84e22 kg
```

Die im Modell integrierte Masse des inneren Erdkerns beträgt ungefähr:

```text
M_IC ≈ 9.8433e22 kg
```

## 4. Drei unterschiedliche Radien

Für eine Zentralmasse `M_c` sind drei physikalisch verschiedene Skalen zu unterscheiden.

Schwarzschildradius:

```text
r_s = 2 G M_c / c^2
```

Bondi-/Einflussradius in der hier verwendeten Konvention:

```text
r_B = G M_c / c_s^2
```

Struktureller Ersatzradius:

```text
M_PREM(<r_rep) = M_c
```

Beispiel für `M_c = 1e20 kg`:

```text
r_s   ≈ 1.49e-7 m
r_B   ≈ 52.6 m
r_rep ≈ 122 km
```

Der Ereignishorizont kann also mikroskopisch sein, während die zugehörige Massenumverteilung makroskopische geophysikalische Größenordnungen erreicht.

## 5. Ersatzradius nach Zentralmasse

Nahe dem Erdzentrum gilt näherungsweise:

```text
r_rep ≈ [3 M_c / (4 pi rho_c)]^(1/3)
```

Referenzwerte:

| M_c | r_rep |
|---:|---:|
| 1e10 kg | 56.7 m |
| 1e12 kg | 263 m |
| 1e14 kg | 1.22 km |
| 1e16 kg | 5.67 km |
| 1e18 kg | 26.3 km |
| 1e20 kg | 122 km |
| 1e21 kg | 263 km |
| 1e22 kg | 568 km |

## 6. Trägheitsmoment

Ein idealisierter Punkt-BH trägt bezüglich der Erdrotation praktisch kein internes Trägheitsmoment bei, während die ersetzte verteilte Materie eines besitzt. Im einfachen Ersatzmodell gilt daher:

```text
Delta C = -(8 pi / 3) Integral[0,r_rep] rho(r) r^4 dr
```

Beispielwerte aus dem V1.0-Sensitivitätsmodell:

```text
M_c = 1e20 kg  -> Delta C / C ≈ -7.45e-9
M_c = 1e22 kg  -> Größenordnung ≈ -16 ppm
```

Das normierte Trägheitsmoment der realen Erde ist daher ein wichtiger Constraint für große Zentralmassen.

## 7. Seismologie

PREM ist aus seismischen Laufzeiten, Normalmoden und globalen Erdparametern aufgebaut. Große Ersatzregionen können deshalb nicht beliebig im Zentrum verborgen werden.

Ein Objekt mit `M_c ≈ 1e20 kg` würde im Ersatzmodell eine zentrale Strukturregion von ungefähr 122 km erfordern. Das ist keine mikroskopische Störung mehr. Dagegen entspricht `M_c ≈ 1e12 kg` nur einer Ersatzregion von ungefähr 263 m und ist für globale Seismologie wesentlich schwieriger direkt aufzulösen.

Das V1.0-Ergebnis lautet daher qualitativ:

```text
große M_c -> Seismologie stark restriktiv
kleine M_c -> globale Seismologie zunehmend schwach
```

Eine präzise statistische Obergrenze erfordert einen vollständigen Normalmoden- beziehungsweise Laufzeit-Likelihood-Fit und wird in V1.0 nicht vorgetäuscht.

## 8. Akkretionsbenchmark

Als Referenzbenchmark wird klassische Bondi-Akkretion verwendet:

```text
dM/dt = 4 pi lambda G^2 rho_c M^2 / c_s^3
```

Mit `lambda = 1/4` und den verwendeten zentralen Referenzwerten ergibt sich näherungsweise:

```text
dM/dt ≈ 1.28e-28 M^2  kg/s
```

und damit die charakteristische Bondi-Zeit:

```text
t_B = M/(dM/dt) = 1/(k M)
```

Referenzwerte:

| M_c | r_B | t_B |
|---:|---:|---:|
| 1e10 kg | 5.3 nm | 24.7 Mrd. Jahre |
| 1e12 kg | 0.53 µm | 247 Mio. Jahre |
| 1e14 kg | 52.6 µm | 2.47 Mio. Jahre |
| 1e16 kg | 5.3 mm | 24,700 Jahre |
| 1e18 kg | 0.53 m | 247 Jahre |
| 1e20 kg | 52.6 m | 2.47 Jahre |
| 1e22 kg | 5.26 km | etwa 9 Tage |

Diese Werte sind ausdrücklich **modellabhängige Benchmarks**. Der reale Erdinnenraum ist kein ideales Bondi-Gas; Festkörperphysik, Mehrphasenstruktur, Viskosität, Wärmeleitung und mikroskopischer Transport können relevant sein.

## 9. Kontinuumsgrenze

Aus der zentralen Eisendichte ergibt sich grob ein atomarer Abstand in der Größenordnung:

```text
d ≈ 1.9e-10 m
```

Setzt man als grobe Trennung `r_B ≈ d`, erhält man eine charakteristische Masse von ungefähr:

```text
M_continuum ≈ 3.6e8 kg
```

Für deutlich kleinere Massen wird eine klassische hydrodynamische Bondi-Beschreibung zunehmend selbst inkonsistent. Dort wäre eine ballistische, atomare beziehungsweise quantenmechanische Mikroakkretionstheorie erforderlich.

## 10. Langzeitentwicklung

Das Erdalter beträgt ungefähr 4.54 Milliarden Jahre. Im einfachen Bondi-Benchmark liegt die Massenskala, bei der `t_B` ungefähr dem Erdalter entspricht, bei:

```text
M_* ≈ 5.4e10 kg
```

Diese Zahl ist **keine experimentelle harte Obergrenze**. Sie ist nur die charakteristische Langzeit-/Runaway-Skala dieses speziellen Akkretionsbenchmarks.

## 11. Wärmehaushalt

Der gesamte terrestrische Oberflächenwärmefluss liegt in der Größenordnung von etwa 47 TW. Wird ein Anteil `eta` der akkretierten Ruheenergie im Erdinneren als Wärme deponiert,

```text
L_BH = eta (dM/dt) c^2
```

entsteht ein zusätzlicher Constraint. Seine Stärke hängt jedoch direkt von der unbekannten Energie- und Transporteffizienz `eta` ab. Deshalb wird daraus in V1.0 keine modellunabhängige harte Massengrenze abgeleitet.

## 12. Entstehungsproblem

Normales Erdkernmaterial ist unter Standard-GR nicht annähernd kompakt genug, um spontan zu einem Schwarzen Loch der betrachteten Masse zu kollabieren.

Für `M_c = 1e20 kg` gilt ungefähr:

```text
r_rep ≈ 122 km
r_s   ≈ 1.5e-7 m
```

Ein Zentralobjekt müsste daher beispielsweise primordial gewesen, später eingefangen worden oder durch einen bisher unbekannten Bildungsmechanismus entstanden sein.

## 13. Starke und schwache Version

### Verworfen / stark disfavored in V1.0

```text
M_c ~ M_Earth
```

als Erklärung des überwiegenden Anteils der Erdmasse beziehungsweise Erdgravitation. Eine solche Zentralisierung wäre mit der beobachteten Massenverteilung, Seismologie und dem Trägheitsmoment der Erde nicht vereinbar.

### Offen als separate Hypothese

Eine wesentlich kleinere zentrale kompakte Masse ist durch die vorherige Aussage nicht automatisch ausgeschlossen. Für kleine Massen verschiebt sich der zentrale theoretische Engpass von der äußeren Gravitation zu Formation und Mikroakkretion.

## 14. Falsifikationsbedingungen

Eine konkrete Erd-BH-Version muss mit **demselben festen Parametersatz** gleichzeitig bestehen gegen:

1. Erdmasse und Radius,
2. normiertes Trägheitsmoment,
3. PREM-Seismologie und Normalmoden,
4. terrestrischen Wärmehaushalt,
5. geologisches Alter und Langzeitstabilität,
6. eine physikalisch konsistente Entstehungs- und Akkretionsgeschichte.

Ad-hoc-Cavities oder nachträglich eingeführte freie Parameter dürfen nicht für jeden einzelnen Test unabhängig angepasst werden.

## 15. Abschluss V1.0

Das Erdmodul kommt zu folgendem Ergebnis:

> Ein dominanter Zentral-BH als Quelle der Erdmasse beziehungsweise Erdgravitation ist mit der bekannten Erdstruktur nicht vereinbar. Ein wesentlich kleineres zentrales kompaktes Objekt ist eine andere, derzeit nicht bestätigte Hypothese. Deren entscheidende offene Physik liegt insbesondere bei Entstehung, Mikroakkretion und einem vollständig selbstkonsistenten Materiemodell des innersten Kerns.

## Primärreferenz

A. M. Dziewonski & D. L. Anderson (1981), *Preliminary Reference Earth Model*, Physics of the Earth and Planetary Interiors 25, 297–356. DOI: 10.1016/0031-9201(81)90046-7.

## Zitierform

Daniel Marcel Schlicksupp (2026), *BH-Kernhypothese – Erdmodul V1.0*, Theorie- und Forschungsentwurf, Rheinland-Pfalz, Deutschland.
