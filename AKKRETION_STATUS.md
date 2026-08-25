# Akkretions- und Langzeitstatus – Stage 2 bis 3.14

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.3  
**Stand:** 25.08.2026  
**Referenzmasse:** `M_SL = 1e16 kg`

## 1. Zweck

Dieses Dokument fasst ausschließlich den Akkretions-, Wärme-, Rheologie-, EOS- und Langzeitblock zusammen.

Es trennt bewusst:

- mathematische Referenzformeln,
- physikalische Modellannahmen,
- Grenzregime/Sensitivitäten,
- numerisch gehärtete Resultate,
- korrigierte oder zurückgezogene Zwischenresultate.

## 2. Kanonischer Bondi-Benchmark

Für den PREM-nahen Erdkern-Referenzzustand wurde als konservative Fluidreferenz verwendet:

```text
Mdot_Bondi ~ 1.28e4 kg/s
```

für `M_SL=1e16 kg`.

Die Bondi-Algebra wurde reproduziert. Der Streitpunkt ist nicht die Formel selbst, sondern ihre direkte Anwendbarkeit auf kondensierte, plastische und degenerierte Materie.

## 3. Hawking-Benchmark

Ein einfacher Standard-Hawking-Lebensdauerbenchmark ergibt für Überleben über `4.54 Gyr` eine Größenordnung

```text
M_Hawking,min ~ 1.19e11 kg.
```

Diese Zahl ist ein Benchmark innerhalb Standard-Hawking, keine experimentelle Messung des Erd-SL.

## 4. Stage 3.2 – mikrophysikalische Skalen

Für `M_SL=1e16 kg` wurden unter anderem bestimmt:

```text
r_s ~ 1.49e-11 m
r_B ~ 5.26e-3 m
```

sowie atomare Abstände, thermische Fe-Skalen und direkte Capture-Proxies.

Ein direkter ballistischer Grenzfall kann viele Größenordnungen unter Bondi liegen. Er ist aber kein allgemeines Gesetz für gebundene, kollektiv wechselwirkende Materie.

## 5. Stage 3.2–3.4 – Festkörpersupply

Als Grenzregime wurden untersucht:

- atomare/diskrete Capture-Proxies,
- Diffusion,
- Creep,
- Knudsen-/Kontinuumsübergänge,
- mechanische Energie und Wärmeleitung.

Wichtiger Befund:

> Ein fester innerer Kern verhält sich nicht automatisch wie ein ideales Bondi-Gas. Das allein beweist aber noch keine geologische Langzeitstabilität.

## 6. Stage 3.5/3.6 – Melt-Feedback

Eine frühe Melt-Abschätzung verwendete implizit die volle mechanische Leistung als lokalen Energieeintrag.

Stage 3.6 korrigierte dies zu

```text
P_local = f_th Mdot c_s^2.
```

Damit müssen mindestens zwei Bedingungen gleichzeitig erfüllt sein:

1. Schmelzzone erreicht die relevante Akkretionsskala,
2. Energiefeedback kann die Schmelze aufrechterhalten.

Für einen repräsentativen Fall war `f_th~1%` nicht automatisch ausreichend, um bis `r_B` zu schmelzen.

**Resultat:** Die einfache Aussage „Wärme schmilzt alles und Bondi startet zwangsläufig“ wird nicht verwendet.

## 7. Stage 3.7 – Bondi-Audit

Der klassische 4D-Bondi-Koeffizient wurde gegen die Literaturform reproduziert.

```text
kein algebraischer Bondi-Fehler gefunden
```

Die physikalische Frage lautet vielmehr:

```text
Welche Transportgleichung verbindet festen/plastischen Kernstoff mit dem SL-Sink?
```

## 8. Stage 3.8/3.9 – nichtlineare hcp-Fe-Rheologie

Konstante Viskosität wurde durch eine stressabhängige Potenzrheologie ersetzt.

Dadurch verschwand die einfache Vorstellung, eine langsame geophysikalische Viskosität könne unverändert in die stark belastete Near Zone übertragen werden.

Je nach Stress kann hcp-Fe sehr viel schneller deformieren.

## 9. Stage 3.10 – Stiff-EOS Toy-Modell

PREM-nahe lokale Stiffness-Werte lagen deutlich über `Gamma=5/3`.

Ein konstantes `Gamma~4`-Toy-Modell erzeugte zunächst eine scheinbare kritische effektive Capture-Grenze um

```text
~54 r_s.
```

Diese Grenze wird **nicht mehr als physikalische Langzeitgrenze verwendet**.

## 10. Stage 3.11 – Hochdruck-EOS

Smith-/Hakim-basierte Fe-EOS-Sensitivitäten zeigten:

- PREM ist für die Near Zone zu grob,
- echte Fe-EOS reicht bis in den TPa-Bereich,
- der mikroskopische Sonic-/Capture-Bereich liegt aber noch tiefer,
- konstantes `Gamma~4` ist über diesen gesamten Bereich nicht zulässig.

**Korrektur:** Die alte `~54 r_s`-Grenze ist nicht EOS-robust und bleibt zurückgezogen.

## 11. Stage 3.12 – voller relativistischer Michel-Test

Für Schwarzschild-Akkretion wurde die relativistische Michel-Kritikpunktstruktur implementiert.

Der allgemeine barotrope Solver reproduziert den analytischen `Gamma=2`-Test mit relativer `Mdot`-Abweichung von ungefähr

```text
~2e-14.
```

Mit einer phenomenologischen condensed -> degenerierte-Elektronen-EOS und einem `Y_e`-Sensitivitätsscan ergibt sich:

```text
Mdot_Michel ~ 147 ... 1460 kg/s
```

für `M_SL=1e16 kg`.

Daraus:

```text
t(+1%) ~ 2.1e3 ... 2.1e4 yr
```

und zur geologischen Stabilität ist eine Unterdrückung von grob

```text
~2e5 ... 2e6
```

gegenüber Michel nötig.

## 12. Stage 3.12 – Michel/Hawking-Massenfenster

Bei gleicher äußerer Referenz skaliert der Michel-Benchmark ungefähr mit `M^2`.

Die <1%-Wachstums-Massenobergrenze liegt in der `Y_e`-Sensitivität grob bei

```text
~4.8e9 ... 4.8e10 kg.
```

Vergleich mit Standard-Hawking:

```text
M_Hawking,min ~1.19e11 kg.
```

Somit gilt innerhalb dieses konkreten Modells:

```text
kein Standard-Hawking + ununterdrücktes-Michel Langzeit-Overlap.
```

## 13. Stage 3.13 – hcp-Fe Solid/Michel Interface

Eine reduzierte serielle Kopplung wurde gelöst:

```text
Mdot_solid(Delta P) = Mdot_Michel(P_inner).
```

Bei einer Millimeter-Grenzfläche genügten kleine subprozentige Druckabweichungen, um nahezu die volle Michel-Kapazität zu speisen.

Damit liefert normaler hcp-Fe-Creep auf dieser Skala keine `1e5–1e6`-Unterdrückung.

Eine Sensitivität mit einem mikroskopischen Interface und `8 GPa`-Stresscap konnte geometrisch eine Unterdrückung von Größenordnung `1e6` erzeugen.

Diese Sensitivität wurde ausdrücklich nicht als physische Lösung akzeptiert, weil die tiefe Materie dort kein gewöhnliches hcp-Fe mehr ist.

## 14. Stage 3.14 – Coulombkristall

Die tiefe degenerierte Materie wurde deshalb mit Coulombkristall-Skalierungen geprüft.

Verwendet wurden:

- Coulomb-Schermodul-Skalierungen,
- Bruch-/Haltbarkeitskinetik,
- dimensionslose Ionenplasmafrequenz `omega_p`,
- aktuelle Perfect-Plasticity-Sensitivitäten.

### Kritischer Befund

Die Stage-3.12-Michel-Kritikpunkte liegen im oder nahe am untersuchten dimensionslosen Coulomb-Plastizitätsratenbereich.

Die reduzierte hydrostatisch-vs-Michel Druckabweichung am kritischen Punkt übersteigt die verwendete Coulomb-Yield-Skala grob um

```text
~1.6e2 ... 1.1e3.
```

Damit ist ein rein elastischer Coulombkristall nicht selbstkonsistent als dauerhafte Barriere gegen den Michel-Zustand.

Nach Yield ist plastisches Weiterfließen ein relevanter Kandidat.

## 15. Korrektur der Stage-3.13-8-GPa-Mikrorettung

Der `8 GPa`-Cap stammte aus dynamischer hcp-Fe-Physik.

Im tiefen Coulomb-Regime skaliert die relevante Festigkeit mit der lokalen Coulomb-Energieskala und kann absolut extrem viel größer sein.

Daher ist die Stage-3.13-`8 GPa`-Mikrogrenze **nicht übertragbar** und als physikalischer Langzeit-Rettungsmechanismus zurückgezogen.

## 16. Was derzeit nicht gezeigt wurde

Nicht gezeigt wurde ein realer Mechanismus, der für `M_SL=1e16 kg` zuverlässig

```text
10^5 ... 10^6
```

Unterdrückung gegenüber der relativistischen Michel-Kapazität erzeugt.

Ebenso nicht gezeigt wurde, dass Michel in der realen Erde exakt ununterdrückt realisiert wird.

Beide Aussagen wären stärker als die vorhandenen Modelle zulassen.

## 17. Aktuelle konservative Aussage

Für `M_SL=1e16 kg` ist die Langzeitakkretion derzeit der stärkste negative Test des Erd-SL-Modells.

Innerhalb

```text
Standard-Hawking
+ phenomenologische Dense-Matter-EOS
+ ununterdrückte Michel-Akkretion
```

ist der Zweig geologisch nicht lebensfähig.

Ein verbleibender Erd-SL-Zweig benötigt daher entweder

- deutlich kleinere Masse,
- modifizierte Verdampfungsphysik,
- oder einen quantitativ nachgewiesenen starken Transport-Suppressionsmechanismus.

## 18. Nächster Test

Der nächste harte Schritt ist ein konsistenter Massenscan:

```text
M_SL ~ 1e8 ... 1e16 kg
```

mit demselben Stack aus

```text
Earth Matching
+ Hawking
+ Michel
+ Coulomb/Plasma-Transport
+ geologischem Alter.
```

Ziel ist die Feststellung, ob überhaupt ein gemeinsames Parameterfenster existiert.
