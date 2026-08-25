# BH-/SL-Kernhypothese – Erdmodul V1.2

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Theorie-Textstand:** V1.2  
**Numerischer Entwicklungsstand:** SL-TOV / Earth Matching 1.3C  
**Stand:** 25.08.2026  
**Erstveröffentlichung V1.0:** 23.08.2026

## 1. Gegenstand und Status

`SL` bezeichnet in diesem Projekt ein **Schwarzes Loch**.

Die definierende Modellannahme des Erdmoduls lautet:

> Im Zentrum der Erde befindet sich ein kleines Schwarzes Loch, dessen Masse im Basismodell nicht zusätzlich zur Erdmasse addiert wird, sondern eine gleich große Menge der sonst angenommenen zentralen PREM-Masse ersetzt.

Diese Aussage ist eine **Hypothese**, keine Beobachtung. Es gibt in diesem Projekt bislang keinen direkten experimentellen Nachweis eines Schwarzen Lochs im Erdzentrum.

V1.2 trennt drei Ebenen strikt:

1. **Massenbuchhaltung / redistributives Basismodell**,
2. **geophysikalische Konsistenztests**,
3. **dynamische numerische Erweiterung** durch den SL-TOV/Earth-Matching-Stack.

Damit wird vermieden, dass eine bestandene interne Rechenprüfung fälschlich als empirische Bestätigung ausgegeben wird.

## 2. Abgrenzung von der früheren starken Grenzvariante

Die frühere Grenzidee

```text
M_SL ~ M_Earth
```

als nahezu alleiniger Träger der Erdmasse beziehungsweise Erdgravitation ist **nicht** das finale Erdmodell.

Unter PREM und Standard-GR würde eine derart starke Zentralisierung die beobachtete radiale Massenverteilung, das Trägheitsmoment und die seismologische Struktur massiv verändern. Diese Variante bleibt deshalb verworfen beziehungsweise stark ausgeschlossen.

Das aktuelle Modell untersucht einen **wesentlich kleineren redistributiven SL-Zweig**. Die Aussage „die starke Variante scheitert“ ist logisch nicht identisch mit „jede beliebig kleine Zentralmasse ist ausgeschlossen“.

## 3. Nullmodell und Massenbuchhaltung

Als geophysikalische Referenz dient PREM (Preliminary Reference Earth Model).

Für eine gewählte Zentralmasse `M_SL` wird ein struktureller Ersatzradius `r_rep` definiert durch

```text
M_PREM(<r_rep) = M_SL
```

Das bedeutet: Im Basismodell wird genau diese normale PREM-Masse aus dem Zentralbereich entfernt und durch die kompakte Zentralmasse ersetzt.

Für `r >= r_rep` gilt in der ideal kugelsymmetrischen Massenbuchhaltung

```text
M_model(<r) = M_PREM(<r)
```

und damit für den monopolen Newton-Grenzfall

```text
g_model(r) = g_PREM(r).
```

Wichtig: Dies ist eine **Buchhaltungsidentität**, keine vollständige Aussage darüber, dass Druckprofil, Materialgleichung, Seismologie und relativistische Feldgleichungen automatisch identisch bleiben. Genau diese zusätzliche Selbstkonsistenz wird in den weiteren Modulen geprüft.

## 4. Drei physikalisch verschiedene Radien

### 4.1 Schwarzschildradius

```text
r_s = 2 G M_SL / c^2
```

`r_s` ist die Horizontskala eines nichtrotierenden, ungeladenen klassischen Schwarzschild-Lochs.

### 4.2 Bondi-/Referenzskala

Als hydrodynamischer Referenzbenchmark kann formal verwendet werden

```text
r_B = G M_SL / c_eff^2
```

wobei die Literatur teilweise eine Konvention mit Faktor 2 verwendet.

Im Erdinneren ist `c_eff` **nicht** unkritisch mit der seismischen P-Wellen-Geschwindigkeit gleichzusetzen. In einem festen beziehungsweise mehrphasigen Medium enthält `v_P` Beiträge der elastischen Module und ist nicht automatisch derselbe Parameter wie die adiabatische Schallgeschwindigkeit eines idealen Bondi-Fluids.

Daher ist `r_B` im Erdmodul eine **modellabhängige Referenzskala**, keine direkt gemessene Akkretionszone.

### 4.3 Struktureller Ersatzradius

```text
M_PREM(<r_rep) = M_SL
```

Nahe dem Zentrum folgt bei annähernd konstanter Dichte `rho_c`

```text
r_rep ~= [3 M_SL / (4 pi rho_c)]^(1/3).
```

Bei `rho_c ~ 1.31e4 kg/m^3` ergeben sich als Größenordnungswerte:

| `M_SL` | `r_rep` ungefähr |
|---:|---:|
| `1e10 kg` | `57 m` |
| `1e12 kg` | `0.26 km` |
| `1e14 kg` | `1.2 km` |
| `1e16 kg` | `5.7 km` |
| `1e18 kg` | `26 km` |
| `1e20 kg` | `122 km` |
| `1e22 kg` | `568 km` |

Der zentrale Punkt ist die Skalentrennung:

```text
r_s != r_B != r_rep.
```

Ein mikroskopischer Horizont bedeutet nicht automatisch eine mikroskopische strukturelle Änderung der umgebenden Erde.

## 5. Trägheitsmoment

Wird zentral verteilte Materie durch eine nahezu punktförmige Masse ersetzt, ändert sich ihr Beitrag zum axialen Trägheitsmoment. Im einfachen kugelsymmetrischen Ersatzmodell lautet die erste Ordnungsgröße

```text
Delta C = -(8 pi / 3) Integral[0,r_rep] rho(r) r^4 dr.
```

Deshalb werden größere `M_SL` beziehungsweise größere `r_rep` zunehmend durch das gemessene normierte Trägheitsmoment eingeschränkt.

Dieser Test ist unabhängig davon relevant, ob das äußere monopole Gravitationsfeld durch exakte Massenredistribution unverändert bleibt.

## 6. Seismologie

PREM kodiert die beobachtete radiale Erdstruktur über seismische Laufzeiten, Normalmoden und globale Parameter. Ein redistributives Modell darf daher nicht nur die Gesamtmasse reproduzieren; es muss auch mit den Wellen- und Strukturbeobachtungen vereinbar sein.

Qualitativ gilt:

```text
größeres r_rep -> stärkere strukturelle/seismologische Angriffsfläche
kleineres r_rep -> geringere direkte Auflösung durch globale Seismologie
```

V1.2 behauptet **keine** fertige statistische Seismologie-Obergrenze. Dafür wäre ein vollständiger Laufzeit-/Normalmoden-Likelihood-Fit mit konsistenter Materialphysik nötig.

## 7. Akkretion: Benchmark, nicht Beweis

Die klassische Bondi-Formel

```text
dM/dt = 4 pi lambda G^2 rho M^2 / c_eff^3
```

wird nur als Referenzbenchmark verwendet.

Der reale innere Erdkern ist kein unendliches, homogenes, ideales Bondi-Gas. Relevante Abweichungen können unter anderem entstehen durch

- Festkörper-/Flüssigkeitsstruktur,
- Druck- und Temperaturabhängigkeit der EOS,
- Viskosität und elastische Reaktion,
- Wärmeleitung und Konvektion,
- diskrete atomare beziehungsweise ballistische Capture-Prozesse,
- relativistische Nahzonenphysik.

Deshalb dürfen aus einer Bondi-Zeit allein **keine modellunabhängigen harten Ausschlussgrenzen** abgeleitet werden.

Der in V1.0 verwendete Übergang `r_B ~ atomarer Abstand` bei einer Masse der Größenordnung `10^8 kg` bleibt höchstens ein Marker dafür, wann ein Kontinuumsmodell selbst fragwürdig wird. Er ist keine fundamentale Naturkonstante und hängt unmittelbar von der gewählten `c_eff`- und Materiedefinition ab.

## 8. Wärme- und Langzeitbedingung

Wird ein Teil `eta` der akkretierten Ruheenergie lokal als Wärme deponiert,

```text
L_SL = eta (dM/dt) c^2,
```

muss diese zusätzliche Leistung mit dem terrestrischen Wärmehaushalt vereinbar bleiben.

Auch hier gilt: Die Stärke des Constraints hängt von der tatsächlichen Capture-Rate, der radiativen/thermischen Effizienz und dem Energieabtransport ab. V1.2 verwendet den Wärmehaushalt daher als Konsistenzbedingung und nicht als frei stehenden Beweis gegen oder für das Modell.

Über geologische Zeiten muss außerdem eine gemeinsame Lösung für

```text
M_SL(t), Erdstruktur(t), Energiefluss(t)
```

existieren. Ein statischer Snapshot allein genügt nicht.

## 9. Formation Rule

Normale Erdkernmaterie kollabiert unter Standard-GR nicht spontan zu einem kleinen Schwarzen Loch der hier betrachteten Art.

Das Modell benötigt deshalb eine explizite Entstehungs- beziehungsweise Einfanggeschichte. Denkbare Klassen sind beispielsweise eine primordiale Seed-Hypothese oder ein anderer klar formulierter Mechanismus. Solange ein solcher Mechanismus nicht quantitativ geschlossen ist, bleibt die **Formation Rule eine offene Physikfrage**.

Die Formation Rule darf nicht nachträglich so gewählt werden, dass sie lediglich die gewünschten heutigen Parameter reproduziert; sie muss eigene überprüfbare Konsequenzen besitzen.

## 10. Ergebnis des redistributiven V1.2-Erdmoduls

Der kleine redistributive Zweig wurde gegen die bislang implementierten Modell- und Konsistenzbedingungen geprüft. Innerhalb dieser Randbedingungen wurde **kein ausschließender Widerspruch** gefunden in Bezug auf

- Massenbuchhaltung,
- äußeres monopoles Gravitationsfeld,
- Trägheitsmoment-Größenordnung,
- seismologische Größenordnungseinordnung,
- Skalentrennung,
- Akkretionsregime,
- Wärme-/Langzeitbenchmark.

Das ist der Sinn von „V1.2 hat die internen Konsistenztests bestanden“.

Es bedeutet ausdrücklich **nicht**:

```text
BH im Erdkern experimentell nachgewiesen.
```

Die empirische Frage bleibt offen.

## 11. Dynamische Erweiterung: SL-TOV-Minimalmodell

Um über die reine Massenredistribution hinauszugehen, wurde ein numerisch ausführbares sphärisches Modell im Jordan Frame implementiert.

Verwendet werden die Funktionen

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4.
```

Der Zustandsvektor lautet

```text
y = [m, nu, p, chi, psi]
psi = dchi/dr.
```

Implementiert sind unter anderem

- die gekoppelte sphärische Massen-/Metrik-/Druckentwicklung,
- die Skalarfeldgleichung,
- Materieerhaltung/TOV-Hydrostatik,
- eine algebraische Spurengleichung für die Krümmung,
- ein Matching-Shell-Integrator außerhalb der SL-Nahzone,
- ein harter GR-Grenztest.

Im Grenzfall

```text
xi -> 0
chi -> 0
psi -> 0
```

muss das System auf die gewöhnliche GR-TOV-Struktur zurückfallen.

## 12. Earth-Closure und Matching

Die aktuelle Earth-Closure verwendet PREM als Referenz. Aus der PREM-Dichte wird eine hydrostatische Referenzdruckkurve konstruiert; die Paare `(p,rho)` definieren eine numerische barotrope Closure `epsilon(p)`.

Diese Closure ist **keine fundamentale Hochdruck-Fe/Ni-Mineralgleichung**. Sie ist ein PREM-kalibriertes erstes Earth-Matching-Modell.

Die Integration wird nicht blind durch den Horizont geführt. Sie beginnt bei

```text
r_a > r_h
r_h = 2 G M_SL / c^2.
```

Am Matching-Radius werden die notwendigen Außenwerte für

```text
m(r_a), p(r_a), chi(r_a), chi'(r_a)
```

gesetzt beziehungsweise geshootet.

Die unmittelbare SL-Nahzone bleibt ein separates Problem für Capture, Akkretion, Thermodynamik und Hochdruck-Mikrophysik.

## 13. Nichttrivialer Skalarzweig

Im Minimalmodell ist

```text
chi = 0
```

immer eine Lösung. Ein unbeschränkter Optimierer kann daher trivial auf den GR-Zweig zurückfallen.

Nichttriviale scalarisierte Lösungen werden deshalb über Eigenwertsuche, Seed und numerische Continuation verfolgt. Die Erdobservablen dürfen dabei nicht beliebig als freie Fitparameter missbraucht werden; in den fortgeschrittenen Läufen werden Radius und ADM-Masse als Forward-Ausgaben des gewählten Zweigs kontrolliert.

## 14. Numerischer Status Earth Matching 1.3C

Für den konkret fortgesetzten voll gekoppelten Zweig

```text
M_SL = 1e16 kg
q0   = 1e-14
```

werden als Promotionskriterien unter anderem verwendet:

```text
|normalized Robin residual| < 1e-5
q_max < 1e-13
endlicher Oberflächenradius
endliche ADM-Masse
```

Der Zweig ist mit dem aktuellen Präzisions-Single-Shooting validiert bei

```text
r_c = 1000 km
r_c =  750 km
r_c =  500 km.
```

Die zugehörigen differentiellen Radius-/Massenabweichungen gegenüber dem verwendeten GR-/PREM-Closurelauf liegen in diesem numerischen Zweig ungefähr in der Größenordnung weniger `1e-5`.

Bei

```text
r_c = 300 km
```

wird das aktuelle Randwertproblem schlecht konditioniert; bei kürzeren Skalen versagt die Single-Shooting-Formulierung zunehmend numerisch.

Für `r_c = 100 km` wurde zusätzlich eine sparse Collocation untersucht. Die Gleichungsresiduen können bis in die Größenordnung `1e-6` reduziert werden, aber verschiedene Mesh-Auflösungen liefern noch keine konvergenten Vorhersagen für Erdradius und Masse. Diese Lösung ist daher **Kandidat, nicht validiertes Resultat**.

Die konservative Aussage lautet:

> Für den speziellen Fortsetzungsweg `M_SL=1e16 kg`, `q0=1e-14` liegt die derzeit numerisch validierte Frontier bei `r_c >= 500 km`. Kürzere Skalen sind aktuell numerisch offen und nicht physikalisch ausgeschlossen.

## 15. Explorative Tensor-Realisierung

Zusätzlich wurde eine effektive schwache-Feld-Parametrisierung untersucht, beispielsweise mit einem Tensorfenster der Form

```text
S_mu^nu = W(r) diag(-s_t, s_r, s_perp, s_perp)
```

und einer redistributiven Gewichtsfunktion `W`.

Dieser Ansatz ist derzeit **keine bewiesene ghost-freie kovariante Tensorfeldtheorie**. Insbesondere sind tangentiale und zeitartige Komponenten ohne vollständige Wirkung beziehungsweise konstitutive Gleichungen nicht unabhängig identifizierbar.

Dieser Stage-4A-Ansatz bleibt deshalb explorativ und wird nicht als abgeschlossene Fundamentaltheorie ausgegeben.

## 16. Falsifikationsbedingungen

Eine konkrete Erd-SL-Version muss mit **einem festen Parametersatz** gleichzeitig bestehen gegen:

1. Erdmasse und Radius,
2. normiertes Trägheitsmoment,
3. PREM-Seismologie und Normalmoden,
4. terrestrischen Wärmehaushalt,
5. geologisches Alter und Langzeitentwicklung,
6. physikalisch konsistente Formation,
7. physikalisch konsistente Capture-/Akkretionsgeschichte,
8. robuste numerische Konvergenz,
9. mindestens eine unabhängige vorab definierte Beobachtungssignatur.

Nicht zulässig ist, für jeden Test neue unabhängige freie Parameter einzuführen, bis der Test automatisch bestanden wird.

## 17. Offene Arbeit

Die nächsten wissenschaftlich relevanten Schritte sind:

- steifer BVP-/Multiple-Shooting-Solver mit analytischen oder sparsamen Jacobians,
- Mesh- und Continuation-Richtungs-Konvergenz für `r_c < 500 km`,
- fundamentale Hochdruck-EOS statt PREM-Barotrop-Proxy,
- explizite Near-Zone-Capture-/Akkretionsgleichungen,
- thermischer Transportabschluss,
- Formation Rule mit eigener Vorhersage,
- vollständiger Seismologie-/Normalmoden-Likelihood-Fit,
- vorregistrierte Messsignaturen, die das SL-Modell von PREM/GR unterscheiden.

## 18. Schlussfolgerung V1.2 / 1.3C

Das Erdmodul hat sich seit V1.0 in zwei wichtigen Punkten verändert:

1. Der **kleine redistributive SL-Zweig** ist nun die klar definierte Erd-Hypothese; die erdmassige starke Grenzvariante ist ausdrücklich nicht das finale Modell.
2. Zusätzlich existiert ein **dynamischer SL-TOV/Earth-Matching-Stack**, der nichttriviale gekoppelte Lösungen numerisch verfolgt und seine derzeitige Konvergenzgrenze offen dokumentiert.

Die aktuelle wissenschaftlich zulässige Aussage ist daher:

> Innerhalb der implementierten V1.2-Basistests und des spezifizierten numerisch validierten 1.3C-Zweigs wurde kein interner ausschließender Widerspruch gefunden. Eine direkte empirische Detektion eines Schwarzen Lochs im Erdzentrum liegt damit nicht vor. Formation, Near-Zone-Mikrophysik, vollständige Geophysik-Likelihood und robuste Short-Range-Lösungen bleiben offene Prüfsteine.

## Primärreferenz

A. M. Dziewonski & D. L. Anderson (1981), *Preliminary Reference Earth Model*, Physics of the Earth and Planetary Interiors 25, 297–356. DOI: 10.1016/0031-9201(81)90046-7.

## Zitierform

Daniel Marcel Schlicksupp (2026), *BH-/SL-Kernhypothese – Erdmodul V1.2*, Theorie- und Forschungsentwurf, numerischer Entwicklungsstand Earth Matching 1.3C, Rheinland-Pfalz, Deutschland.
