# BH-Kernhypothese - Erdmodul V1.0

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Geburtsdatum:** 13.06.1988  
**Region:** Rheinland-Pfalz  
**Land:** Deutschland  
**Version:** Erdmodul V1.0  
**Veröffentlichungsdatum:** 23.08.2026  

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

## Status

Dieses Repository veröffentlicht das eingefrorene **Erdmodul V1.0** der BH-Kernhypothese als Theorie- und Forschungsentwurf. Es wird keine experimentelle Bestätigung eines Schwarzen Lochs im Erdzentrum behauptet.

## Kernaussage

Geprüft wird, ob im Zentrum der Erde eine kompakte, schwarzlochähnliche Zentralmasse existieren könnte, ohne die bekannten globalen und geophysikalischen Beobachtungen zu verletzen.

Die starke Variante - ein Zentral-BH als dominierende Quelle der Erdmasse beziehungsweise Erdgravitation - wird in V1.0 verworfen. Offen bleibt nur eine deutlich kleinere Zentralmasse als separate Hypothese.

## Modellbasis

Als Nullmodell dient PREM (Preliminary Reference Earth Model). Die Zentralmasse wird in V1.0 nicht zusätzlich zur gemessenen Erdmasse addiert, sondern ersetzt die entsprechende PREM-Masse im Zentrum:

```text
M_PREM(<r_rep) = M_c
```

Außerhalb der Ersatzregion gilt im ideal kugelsymmetrischen Modell:

```text
M'(<r) = M_PREM(<r)
g'(r) = g_PREM(r)
```

Wichtige Skalen:

```text
r_s = 2 G M_c / c^2
r_B = G M_c / c_s^2
```

Horizontgröße, Akkretions-/Einflussradius und strukturelle Ersatzregion sind nicht identisch.

Beispiel für `M_c = 1e20 kg`:

```text
r_s   ~ 1.49e-7 m
r_B   ~ 52.6 m
r_rep ~ 122 km
```

## Prüffelder

Das Modell wird gegen folgende Beobachtungsklassen konfrontiert:

- Erdmasse und Radius
- PREM-Seismologie und Normalmoden
- normiertes Trägheitsmoment
- Akkretions- und Langzeitentwicklung
- terrestrischer Wärmehaushalt
- Entstehungs- und Einfangmechanismen

## Akkretionsbenchmark

Als Referenz wird klassische Bondi-Akkretion verwendet:

```text
dM/dt = 4 pi lambda G^2 rho_c M^2 / c_s^3
```

Dieser Ausdruck ist im Erdmodul ausdrücklich ein Benchmark und keine bewiesene Akkretionsgleichung für den realen, dichten und mehrphasigen Erdkern.

## Ergebnis V1.0

**Verworfen bzw. stark disfavored:**

- Zentral-BH als Hauptträger der Erdmasse/Erdgravitation.
- Große Zentralmassen mit makroskopischen Ersatzregionen, die mit Seismologie, Rotation, Wärmehaushalt oder Langzeitentwicklung kollidieren.

**Offen:**

- Wesentlich kleinere zentrale kompakte Objekte.
- Der mikroskopische Akkretionsbereich unterhalb der klassischen Kontinuumsgrenze, der eine eigene atomare/quantitative Transporttheorie erfordert.

## Falsifikationsbedingung

Eine konkrete Erd-BH-Version muss mit **demselben Parametersatz** gleichzeitig bestehen gegen:

1. Erdmasse und Radius,
2. Trägheitsmoment,
3. Seismologie/Normalmoden,
4. Wärmehaushalt,
5. geologisches Alter,
6. physikalisch konsistente Entstehungs- und Akkretionsgeschichte.

## Primärreferenz

A. M. Dziewonski & D. L. Anderson (1981), *Preliminary Reference Earth Model*, Physics of the Earth and Planetary Interiors 25, 297-356. DOI: 10.1016/0031-9201(81)90046-7.

## Zitierform

Daniel Marcel Schlicksupp (2026), *BH-Kernhypothese - Erdmodul V1.0*, Theorie- und Forschungsentwurf, Rheinland-Pfalz, Deutschland.
