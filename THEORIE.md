# SL/BH-Kernhypothese Erdmodul V1.3

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Stand:** 25.08.2026  
**Aktueller Forschungsstand:** Stage 3.14  
**Erstveröffentlichung V1.0:** 23.08.2026

## 1. Gegenstand und wissenschaftlicher Status

`SL` bezeichnet in diesem Projekt ein **Schwarzes Loch**.

Die definierende Hypothese des Erdmoduls lautet:

> Im Zentrum der Erde wird ein kleines Schwarzes Loch als zentrale kompakte Masse modelliert. Im redistributiven Basismodell ersetzt seine Masse eine gleich große Menge der sonst angenommenen zentralen PREM-Masse, statt zusätzlich zur gemessenen Erdmasse addiert zu werden.

Diese Aussage ist eine **theoretische Hypothese**, keine Beobachtung. Es liegt kein direkter experimenteller Nachweis eines Schwarzen Lochs im Erdzentrum vor.

Die Theorie wird absichtlich in getrennten Ebenen geprüft:

1. Massenbuchhaltung und Erdstruktur,
2. relativistischer Feldrahmen,
3. numerisches Earth Matching,
4. Seismologie und globale Observablen,
5. Near-Zone-Materiephysik,
6. Akkretion und Langzeitentwicklung,
7. Formation,
8. Falsifikations- und Messsignaturen.

## 2. Abgrenzung der starken Variante

Die starke Grenzvariante

```text
M_SL ~ M_Earth
```

ist nicht Bestandteil des aktuellen Erdmodells. Unter PREM und Standard-GR wäre eine starke Zentralisierung eines wesentlichen Anteils der Erdmasse mit radialer Massenverteilung, Trägheitsmoment und Seismologie nicht vereinbar.

Der aktuelle Forschungsgegenstand ist ein **kleiner redistributiver SL-Zweig**.

## 3. Redistributive Massenbuchhaltung

Als Nullmodell dient PREM.

Für eine gewählte Zentralmasse `M_SL` wird `r_rep` definiert durch

```text
M_PREM(<r_rep) = M_SL.
```

Im Basismodell wird genau diese PREM-Masse aus der Zentralregion entfernt und durch das SL ersetzt. Für `r >= r_rep` gilt im ideal kugelsymmetrischen Massenbuchhaltungsgrenzfall

```text
M_model(<r) = M_PREM(<r).
```

Die Massenbuchhaltung verhindert damit eine doppelte Zählung von SL-Masse und normaler Materie.

Sie garantiert noch keine hydrostatische, seismologische oder thermodynamische Konsistenz; diese müssen separat gelöst werden.

## 4. Drei physikalisch verschiedene Radien

### 4.1 Schwarzschildradius

```text
r_s = 2 G M_SL / c^2
```

### 4.2 Bondi-/Akkretionsskala

```text
r_B = G M_SL / c_eff^2
```

`c_eff` ist eine modellabhängige thermodynamische/akustische Referenzgröße und nicht automatisch identisch mit der seismischen `V_P`.

### 4.3 Struktureller Ersatzradius

```text
M_PREM(<r_rep) = M_SL.
```

Nahe dem Zentrum gilt größenordnungsmäßig

```text
r_rep ~ [3 M_SL / (4 pi rho_c)]^(1/3).
```

Es gilt ausdrücklich

```text
r_s != r_B != r_rep.
```

## 5. Relativistischer Minimalrahmen

Der aktuelle sphärische Minimalstack verwendet im Jordan Frame

```text
S = Integral sqrt(-g) [ 1/2 F(chi) R
                        -1/2 (nabla chi)^2
                        -V(chi) ] d^4x
    + S_mat + S_BH
```

mit

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4.
```

Die Metrik-/Skalarfeldgleichungen werden mit Materie und einer zentralen BH-Quelle gekoppelt.

Der Grenzfall

```text
xi -> 0
chi -> 0
dchi/dr -> 0
```

muss auf gewöhnliche GR zurückfallen.

Ein reales Schwarzes Loch besitzt einen Horizont und ist kein reguläres TOV-Zentrum. Deshalb wird die unmittelbare Near Zone über BH-/Horizon-konsistente Randbedingungen behandelt.

## 6. Earth-Matching-Referenzzweig

Der numerisch am weitesten ausgearbeitete Zweig verwendet

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14.
```

Mit der gehärteten Layered-PREM-Earth-Closure wurden voll gekoppelte und cross-solver-validierte Lösungen bei

```text
r_c = 500 km
r_c = 300 km
```

erhalten.

`r_c = 250–275 km` bleibt Kandidatenbereich; kleinere Reichweiten sind als voll gekoppelte Lösungen nicht promoted.

Die GR-Baseline liegt ungefähr bei

```text
Delta R/R ~ 4.17e-9
Delta M/M ~ 4.44e-8.
```

## 7. Geophysikalische Sensitivitäten

Für die validierten Referenzzweige wurden unter anderem berechnet:

```text
max |Delta g/g|, r >=100 km ~ 1.8e-4 ... 2.1e-4
|Delta Vp/Vp|              ~ 3e-6
Delta r_ICB                ~ -44 ... -61 m
Delta r_CMB                ~ -35 ... -34 m
Delta T_P                  ~ +0.009 ... +0.012 s
Delta I/I                  ~ -(7...8)e-6.
```

Zusätzlich wurden 1D P-/PKP-/PKIKP-Raytracing und prototypische toroidale Normalmoden berechnet.

Diese Resultate sind Modellvorhersagen beziehungsweise Sensitivitäten. Sie sind keine bereits beobachteten SL-Anomalien.

## 8. Formation Rule

Normale Erdkernmaterie kollabiert unter Standard-GR nicht spontan zu einem kleinen SL der hier betrachteten Art.

Der Erd-SL-Zweig benötigt daher eine quantitative Entstehungs- oder frühe Einfanggeschichte. Ein gewöhnlicher heutiger galaktischer Capture-Ursprung ist nach einfachen PBH-Einfangraten stark unplausibel.

Formation bleibt ein eigenständiger harter Prüfstein.

## 9. Akkretion: von Bondi zu einem gestuften Near-Zone-Modell

Die klassische Bondi-Gleichung

```text
Mdot = 4 pi lambda rho G^2 M_SL^2 / c_eff^3
```

ist mathematisch korrekt innerhalb ihrer Annahmen. Die direkte Anwendung auf kristallinen Erdkernstoff ist jedoch keine algebraische Notwendigkeit, sondern eine physikalische Modellannahme.

Der Akkretionsblock wurde deshalb schrittweise gehärtet.

### 9.1 Ballistik, Diffusion und Creep

Als Grenzregime wurden untersucht:

- direkte Schwarzschild-Capture-Proxies,
- atomare/elektronische Skalen,
- Festkörperdiffusion,
- Creep-Supply,
- Kontinuums-/Knudsenchecks.

Diese Tests zeigen, dass verschiedene lokale Transportregime viele Größenordnungen unterschiedliche `Mdot` liefern können.

### 9.2 Wärme- und Melt-Feedback

Eine frühe vereinfachte Argumentation

```text
Akkretion -> lokale Wärme -> vollständige Schmelze -> automatisch Bondi
```

ist zu stark.

Stage 3.6 führte explizit die lokale Thermalisierungsfraktion ein:

```text
P_local = f_th Mdot c_s^2.
```

Ob eine Schmelzzone bis zur relevanten Akkretionsskala wächst, hängt von Wärmeleitung, latenter/sensibler Wärme, lokalem Energieeintrag und Materienachschub ab.

## 10. Nichtlineare hcp-Fe-Rheologie

Eine konstante geophysikalische Viskosität kann nicht über viele Größenordnungen der Deformationsrate in die SL-Nahzone extrapoliert werden.

Deshalb wurde ein stressabhängiges Potenzgesetz als Brückenmodell verwendet. Der Befund ist qualitativ wichtig:

> Bei starkem lokalem Stress kann hcp-Fe um viele Größenordnungen schneller deformieren als aus einer konstanten Langzeitviskosität folgen würde.

Damit ist „der feste Kern bremst automatisch genug“ kein hinreichender Langzeitbeweis.

## 11. Hochdruck-EOS

PREM ist kein fundamentaler Multi-TPa-Fe/Ni-EOS.

Der Near-Zone-Stack wurde deshalb mit experimentellen und DFT-gestützten Eisen-EOS-Sensitivitäten gehärtet.

Wichtigste Korrektur:

> Eine konstante lokale `Gamma~4`-EOS darf nicht von Erdkernbedingungen bis in die mikroskopische Near Zone extrapoliert werden.

Die aus einem solchen Toy-Modell abgeleitete alte `~54 r_s`-Capture-Grenze ist als physikalische Langzeitgrenze zurückgezogen.

Bei zunehmender Kompression ändern sich Ionisation, Elektronenentartung und schließlich Zusammensetzung. Der thermodynamische Pfad muss daher regimeabhängig behandelt werden.

## 12. Relativistische Michel-Akkretion

Die Newtonsche Bondi-Topologie ist für sehr steife EOS kein ausreichender Schwarzschild-Near-Zone-Test.

Stage 3.12 implementiert deshalb die relativistische Michel-Kritikpunktstruktur.

Für eine allgemeine barotrope EOS gilt am kritischen Punkt schematisch

```text
u_c^2 = a_c^2 / (1 + 3 a_c^2)
r_c/M = (1 + 3 a_c^2) / (2 a_c^2),
```

wobei die relativistische Bernoulli-Bedingung den kritischen Zustand bestimmt.

Der allgemeine Solver wurde gegen eine analytische `Gamma=2`-Lösung getestet und reproduzierte die Akkretionsrate mit relativer Abweichung von ungefähr

```text
~2e-14.
```

## 13. Stage-3.12-Dense-Matter-Sensitivität

Mit einer phenomenologischen Übergangs-EOS von kondensierter Materie zu einem degenerierten Elektronenfluid wurden über einen `Y_e`-Sensitivitätsbereich für

```text
M_SL = 1e16 kg
```

ungefähr

```text
Mdot_Michel ~ 147 ... 1460 kg/s
```

erhalten.

Für nur `+1%` Masse über `4.54 Gyr` wäre dagegen im Mittel ungefähr

```text
Mdot_1% ~ 6.98e-4 kg/s
```

zulässig.

Der Referenzzweig benötigt damit in diesem Modell eine reale Unterdrückung von ungefähr

```text
2e5 ... 2e6
```

gegenüber der ununterdrückten Michel-Kapazität.

Dies ist derzeit der stärkste Langzeit-Gegentest des `1e16 kg`-Zweigs.

## 14. Hawking/Michel-Überlappung

Unter dem verwendeten einfachen Standard-Hawking-Benchmark liegt die Erdalter-Überlebensuntergrenze ungefähr bei

```text
M_Hawking,min ~ 1.19e11 kg.
```

Aus der Stage-3.12-Michel-Skalierung folgen für weniger als `1%` geologisches Wachstum Massenobergrenzen grob bei

```text
M_Michel,max ~ 4.8e9 ... 4.8e10 kg.
```

Damit gilt innerhalb **dieses konkreten Standard-Hawking + ununterdrückten Michel-Modells**:

```text
M_Michel,max < M_Hawking,min
```

und es existiert kein überlappendes Langzeitfenster.

Das ist ein starker negativer Modellbefund, aber noch kein empirischer Ausschluss der gesamten Erd-SL-Hypothese, weil der reale nichtstationäre Materialtransport noch nicht vollständig geschlossen ist.

## 15. Solid/Michel-Kopplung

Stage 3.13 koppelte reduzierten hcp-Fe-Creep direkt an eine innere Michel-Kapazität.

Bei Millimeterradien genügen in diesem Modell kleine subprozentige Druckabweichungen vom hydrostatischen Zustand, um nahezu die volle Stage-3.12-Michel-Rate zu speisen.

Damit liefert ein gewöhnlicher hcp-Fe-Festkörper auf Millimeterskala **nicht** die benötigte `10^5–10^6`-Unterdrückung.

## 16. Coulombkristall und Stage 3.14

In der tiefen degenerierten Region ist hcp-Fe nicht mehr die richtige Festkörperbeschreibung. Deshalb wurden Coulombkristall-Skalierungen und Plastizitätsmodelle geprüft.

Der aktuelle reduzierte Befund lautet:

1. Die Michel-Kritikpunkte liegen im oder nahe am untersuchten dimensionslosen Coulomb-Plastizitätsratenbereich.
2. Die hydrostatisch-vs-Michel Druckabweichung am Kritikpunkt liegt deutlich über der verwendeten Coulomb-Yield-Skala.
3. Ein rein elastischer Coulombkristall würde daher vor Erreichen des Michel-Zustands yielden.
4. Plastisches Weiterfließen nach dem Yield ist ein ernstzunehmender Kandidat und keine automatische Akkretionsblockade.

Damit ist ein generisches Argument

```text
"Coulombkristall ist stark -> Michel wird um 1e6 unterdrückt"
```

nicht nachgewiesen.

## 17. Korrektur der Stage-3.13-8-GPa-Mikrogrenze

Eine frühere Sensitivität hatte bei einem mikroskopischen Interface und einem `8 GPa`-Stresscap eine mögliche geologische Unterdrückung gezeigt.

Dieser `8 GPa`-Cap stammte aus hcp-Fe-Physik und ist in der tiefen Coulomb-Zone nicht übertragbar.

Die daraus abgeleitete einfache „Mikrorettung“ wird daher als **physikalischer Langzeitmechanismus zurückgezogen**.

## 18. Aktueller Gesamtstatus des Erdmoduls

### Gut ausgearbeitete Teile

- klare redistributive Massenbuchhaltung,
- relativistischer Minimalrahmen,
- Horizon-/BH-konsistente Randbedingungen,
- Layered-PREM-Earth-Matching,
- cross-solver-validierte Referenzpunkte,
- Erdobservablen-/Seismologie-Sensitivitäten,
- gestufter Akkretions-/EOS-/Rheologie-Audit,
- relativistischer Michel-Solver mit analytischem Selfcheck,
- dokumentierte Korrektur früherer zu starker Zwischenresultate.

### Harte offene beziehungsweise belastende Teile

- `1e16 kg`-Langzeitakkretion,
- voll gekoppelte nichtstationäre Coulomb-/Plasma-/Thermaltransportgleichungen,
- realistische Elektroneneinfang-/Kompositionsentwicklung,
- Formation Rule,
- vollständiger Real-Data-Seismologie-/Normalmoden-Fit,
- unabhängige experimentelle Detektionssignatur.

## 19. Falsifikationsprinzip

Eine konkrete Parameterwahl muss mit **demselben Parametersatz** gleichzeitig gegen bestehen:

1. Erdmasse und Radius,
2. Trägheitsmoment,
3. PREM-Seismologie,
4. Normalmoden,
5. Wärmehaushalt,
6. Langzeitakkretion,
7. Formation,
8. numerische Konvergenz,
9. mindestens eine unabhängige vorab definierte Messsignatur.

Parameter dürfen nicht für jeden Test separat nachjustiert werden.

## 20. Nächster entscheidender Test

Der nächste prioritäre Schritt ist ein systematischer Massenscan

```text
M_SL ~ 1e8 ... 1e16 kg
```

mit demselben physikalischen Stack:

```text
Earth Matching
+ Standard-Hawking
+ relativistische Michel-Akkretion
+ Coulomb-/Plasma-Transport
+ Earth-age-Wachstum.
```

Ziel ist ausdrücklich nicht, einen bevorzugten Massenpunkt zu retten, sondern zu bestimmen, ob ein konsistentes Erd-SL-Massenfenster verbleibt oder im gewählten Modell ausgeschlossen wird.

## 21. Aussagegrenze

Der aktuelle Stand ist eine **ausgearbeitete, falsifizierbare SL-Kernhypothese mit relativistischem und numerischem Forschungsrahmen**.

Er ist keine etablierte oder empirisch bestätigte neue Fundamentaltheorie und kein Nachweis eines Schwarzen Lochs im Erdzentrum.
