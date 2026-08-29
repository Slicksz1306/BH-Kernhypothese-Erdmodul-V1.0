# Stage 3.95B / A35 – WDM Charge Closure Specification

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** MATHEMATISCH SPEZIFIZIERT / PHYSIKALISCHE DATENIDENTIFIZIERBARKEIT OPEN / REALES `Q_eq` BLOCKED BY MISSING CLOSURE DATA

```text
Stage 3.95B mathematisch spezifiziert: PASS
physikalische Datenidentifizierbarkeit: OPEN
Implementierung reales Q_eq: BLOCKED BY MISSING CLOSURE DATA
```

## Ziel und Aussagegrenze

Stage 3.95B spezifiziert die physikalische Erweiterung der analytischen
Stage-3.95A-Referenz:

```text
WDM-Elektronentransport
+ multikomponentiger Ionentransport
+ Poisson / Screening
+ Q-abhaengiger innerer Sink
-> F(Q)
-> alle physikalisch zulaessigen Q_eq-Kandidaten.
```

Diese Datei ist eine mathematische Modell- und Datenanforderung. Sie enthält
keinen realen `Q_eq`-Solver und keinen numerischen Erdwert für `Q_eq`.

Insbesondere gilt:

```text
Stage 3.95A bleibt die unveraenderte analytische Toy-Referenz.
Stage 3.95B behauptet keinen experimentellen BH-Nachweis.
Stage 3.95B schliesst keine fehlenden Materialdaten durch freie Parameter.
Ein spaeterer PASS wuerde nur die definierte Ladungsclosure schliessen.
```

## 1. Grundproblem und Notation

Für eine vorgegebene Ladung des zentralen Sinks wird zunächst ein stationäres,
sphärisch symmetrisches Randwertproblem auf

```text
r in [r_m, R]
```

formuliert.

Die zentrale physikalische Unterscheidung lautet:

```text
Q_bullet = tatsaechliche Ladung des zentralen Sinks
Q_m      = am Matchingradius r_m effektiv eingeschlossene Ladung.
```

Im geschirmten Fall gilt im Allgemeinen

```text
Q_m != Q_bullet.
```

Die Identifikation

```text
Q_m = Q_bullet
```

ist nur der ungeschirmte Stage-3.95A-Grenzfall. Stage 3.95B benötigt eine
explizite innere Matching-Abbildung

```text
Q_m = M_Q(Q_bullet, phi_m, T_e,m, T_i,m, {n_a,m}, inner state).
```

Damit wird verhindert, dass die nackte Sinkladung zusätzlich zu einer bereits
enthaltenen inneren Screeningwolke als Gauss-Randwert eingesetzt wird.

Für Elektronen und positive Ionenspezies `a=1,...,K` gilt

```text
q_e = -e
q_a = Z_a e.
```

`Z_a` bezeichnet eine ganzzahlige Ladungszahl. Eine mittlere Ionisation wie
`Zbar=2.76` kann in einem kontinuierlichen Average-Atom-Modell als
Materialparameter auftreten, darf aber nicht als nichtganzzahlige Sprungweite
in einer diskreten Ladungskette verwendet werden.

Die freie Ladungsdichte lautet

```text
rho_q(r) = e [sum_a Z_a n_a(r) - n_e(r)].
```

Im äußeren Transportgebiet kann als Newtonsche Referenz

```text
Phi_g(r) = -G M/r
```

verwendet werden. Relativistische und quantenmechanische Innenphysik zwischen
Horizont und `r_m` gehört in den inneren Sink-/Matchingoperator und darf nicht
durch eine unkontrollierte Newtonsche Fortsetzung ersetzt werden.

Für jede Spezies gilt

```text
1/r^2 d[r^2 J_s]/dr = S_s,
```

wobei `J_s>0` einen nach außen gerichteten Teilchenfluss bezeichnet. Ohne
Volumenreaktionen gilt `S_s=0`.

Werden Ionisation, Rekombination oder Ladungsaustausch aufgelöst, müssen die
Quellterme mindestens

```text
sum_s q_s S_s = 0
```

und, bis auf explizite Massenquellen oder -senken,

```text
sum_s m_s S_s = 0
```

erfüllen.

Die positive Capture-Rate ist

```text
dotN_s(r) = -4 pi r^2 J_s(r).
```

Für `S_s=0` folgt die radiale Flusserhaltung

```text
dotN_s(r) = const.
```

## 2. Elektronen-Teilmodell

Die Elektronen erhalten eine eigene WDM-/quantenkinetische Closure. Sie werden
nicht über eine frei gewählte skalare Diffusionskonstante `D_e` geschlossen.

Das elektrochemische Elektronenpotential ist

```text
mu_tilde_e
= mu_e^chem(n_e, {n_a}, T_e)
  - e phi
  + m_e Phi_g.
```

Ein minimaler lokaler Linear-Response-Ansatz kann formal als

```text
[j_e, J_E,e]^T
= L_e(P, T_e, T_i, X, B, ...)
  [-d(mu_tilde_e/T_e)/dr, d(1/T_e)/dr]^T
```

geschrieben werden. Dabei gilt

```text
J_e = n_e u + j_e,
```

mit der Bulkgeschwindigkeit `u`, dem Elektronenfluss `j_e` relativ zum
ionischen Bulk und dem elektronischen Energiefluss `J_E,e`.

`L_e` ist kein freier Fitparameter. Der Operator muss aus einem für den
benötigten Fe-Ni-Light-Element-Zustand gültigen kinetischen Modell, einer
QMD-/Kubo-Auswertung oder belastbaren experimentellen Transportdaten
abgeleitet werden.

Insbesondere gilt:

```text
elektrische Leitfaehigkeit != vollstaendiger Elektronen-Teilchenflussoperator.
```

Eine einzelne Leitfähigkeit bestimmt den Teilchenfluss bei gleichzeitig
vorhandenen chemischen, thermischen und elektrischen Gradienten nicht eindeutig.
Sie darf nicht ohne Herleitung über eine Nernst-Einstein-Relation in ein freies
`D_e` umgedeutet werden.

Eine mögliche mikroskopische Closure-Klasse ist schematisch

```text
v dot grad_r f_e + pdot_e dot grad_p f_e
= C_ee[f_e] + sum_a C_ea[f_e, f_a],
```

mit

```text
pdot_e = -e(E + v cross B) - m_e grad Phi_g
0 <= f_e <= 1.
```

Die Dichte und der relative Teilchenfluss sind Momente von `f_e`:

```text
n_e = 2 integral f_e d^3p/(2 pi hbar)^3

j_e = 2 integral (v_r-u) f_e d^3p/(2 pi hbar)^3.
```

Diese Schreibweise legt noch keinen universell gültigen Kollisionsoperator
fest. Ein konkreter Operator darf erst gewählt werden, wenn seine
Gültigkeitsdomäne für Dichte, Temperatur, Entartung, Kopplung und Zusammensetzung
dokumentiert ist.

Rightley und Baalrud, Phys. Rev. E 103, 063206 (2021), DOI
`10.1103/PhysRevE.103.063206`, liefern einen WDM-Quantenkinetikrahmen mit
Uehling-Uhlenbeck-Kollisionen, Pauli-Blocking, Korrelation und Beugung. Die
publizierten Anwendungen liefern aber keine direkt einsetzbare
Fe-Ni-Erdkern-Closure.

Falls

```text
omega_ce tau_e << 1
```

nicht nachgewiesen ist, muss der elektronische Transport tensorwertig behandelt
werden. Ein skalares sphärisches 1D-Modell ist dann nicht ohne weitere
Magnetotransportanalyse zulässig.

## 3. Ionen-Teilmodell

Für jede positive Spezies beziehungsweise jeden aufgelösten Ladungszustand gilt

```text
mu_tilde_a
= mu_a^chem({n_b}, n_e, T_i, T_e)
  + Z_a e phi
  + m_a Phi_g.
```

Der Gesamtfluss wird zerlegt in

```text
J_a = n_a u + j_a.
```

Im baryzentrischen Bezugssystem gilt

```text
sum_a m_a j_a = 0.
```

Eine minimale Onsager-Darstellung ist

```text
j_a
= sum_b L_ab^(i) [-d(mu_tilde_b/T_i)/dr]
  + L_aT^(i) d(1/T_i)/dr.
```

Bei verschwindendem Magnetfeld muss die auf `K-1` unabhängige Komponenten
projizierte Mobilitätsmatrix die Bedingungen

```text
L_ab^(i) = L_ba^(i)

x^T L^(i) x >= 0
```

erfüllen. Bei relevantem Magnetfeld gilt stattdessen die
Onsager-Casimir-Beziehung

```text
L(B) = L^T(-B),
```

während der symmetrische Anteil nichtnegative Entropieproduktion erzeugen muss.

Äquivalent kann der ionische Stofftransport in Maxwell-Stefan-Form über

```text
D_tilde_ab(P, T, X)
```

und thermodynamische Faktoren formuliert werden. Onsager- und
Maxwell-Stefan-Darstellung sind alternative Repräsentationen derselben
Transportinformation; sie dürfen nicht als unabhängige Zusatzdaten doppelt
gezählt werden.

Die thermodynamischen Faktoren benötigen insbesondere Ableitungen der Form

```text
Gamma_ab proportional
(partial mu_a^chem / partial x_b)_(P,T,x_c!=b).
```

Li et al., Scientific Reports 12, 21255 (2022), DOI
`10.1038/s41598-022-24594-8`, liefern entlang der betrachteten Kernadiabate für
Ni ungefähr

```text
D_Ni,self = 2.47e-9 ... 3.37e-9 m^2/s
```

und Fe-Selbstdiffusion in derselben Größenordnung. Diese Größen sind
Tracer-/Selbstdiffusionsdaten und keine vollständige gegenseitige Diffusions-
oder Ladungsmobilitätsmatrix.

White et al., Phys. Rev. E 100, 033213 (2019), DOI
`10.1103/PhysRevE.100.033213`, zeigen, dass multikomponentige WDM-Diffusion
Maxwell-Stefan-Koeffizienten, Onsager-Korrelationen und chemische
Potentialgradienten benötigt. Die dort untersuchten Beispielmischungen sind kein
fertiger Fe-Ni-Light-Element-Datensatz für Erdkernbedingungen.

Damit bleibt die Unterscheidung zwingend:

```text
self diffusion
!= mutual diffusion
!= Onsager matrix
!= charge mobility.
```

Elektron-Ion-Reibung und Energieaustausch müssen an der Modulschnittstelle
konservativ gekoppelt werden:

```text
R_e + sum_a R_a = 0

Q_E,e + sum_a Q_E,a = 0,
```

sofern keine explizite äußere Quelle oder Senke vorhanden ist.

## 4. Elektrostatik- und Screening-Teilmodell

Das elektrische Potential folgt aus Poisson und der gekoppelten materiellen
Antwort:

```text
1/r^2 d[r^2 dphi/dr]/dr = -rho_q/epsilon_0

rho_q = e [sum_a Z_a n_a - n_e]

E_r = -dphi/dr.
```

Die eingeschlossene Ladung ist

```text
Q_enc(r) = -4 pi epsilon_0 r^2 dphi/dr
```

und erfüllt

```text
dQ_enc/dr = 4 pi r^2 rho_q.
```

Screening entsteht durch die Reaktion von `n_e` und `n_a` auf `phi`, die
chemischen Potentiale und die Transportgleichungen. Korrelation, Entartung und
Nichtidealität gehören in eine konsistente freie Energie, ein Average-Atom-Modell
oder einen nichtlokalen Antwortoperator. Sie dürfen nicht zusätzlich zu derselben
bereits enthaltenen Antwort als separater Yukawa-Faktor addiert werden.

Für eine lokale thermodynamische Closure wäre beispielsweise eine freie
Energiedichte

```text
f = f(n_e, {n_a}, T_e, T_i)
```

mit

```text
mu_s^chem = partial f / partial n_s
```

erforderlich. Die Hesse-Matrix der stabilen Phase muss im physikalisch
zulässigen Unterraum thermodynamisch stabil sein.

A28 liefert als statischen Fixed-Ion-Referenzfall

```text
lambda_TF = 2.95e-11 ... 4.29e-11 m.
```

Der bisherige Wert

```text
r_m = 6.13e-8 m
```

liegt mehr als drei Größenordnungen über dieser Skala. Ein wesentlicher Teil der
mikroskopischen Screeningstruktur kann daher innerhalb der bisherigen
A34-Matchingfläche liegen. Die Abbildung `Q_bullet -> Q_m` ist deshalb ein
Pflichtbestandteil der Closure.

Die vorhandene nichtlineare relativistische Thomas-Fermi-Rechnung bleibt ein
statischer Fixed-Ion-Referenzfall. Sie ist kein stromtragendes WDM-Sheath-Modell.

## 5. Sink-Teilmodell

Der innere Sink wird durch eine eigene Capture-Abbildung beschrieben. Eine
allgemeine kinetische Randrate ist

```text
C_s
= g_s integral_(v_r<0)
  |v_r| f_s(r_m,p)
  P_cap,s(Q_bullet,p,phi_m,inner state)
  d^3p/(2 pi hbar)^3.
```

Dabei gilt

```text
0 <= P_cap,s <= 1.
```

Die innere Randbedingung lautet

```text
-J_s(r_m) = C_s.
```

Nur wenn diese kinetische Abbildung lokal und linear in der Randdichte ist,
darf sie als Robin-Bedingung geschrieben werden:

```text
-J_s(r_m)
= kappa_s(Q_bullet, T_e,m, T_i,m, phi_m, {n_a,m}, ...)
  n_s(r_m).
```

Dann folgt

```text
dotN_s(Q_bullet)
= 4 pi r_m^2 kappa_s(Q_bullet, ...) n_s(r_m; Q_bullet).
```

Die vorhandenen A25/A29-Elektronencapture-Rechnungen sind statische isolierte
Teilchen-/Screening-Referenzen. Sie liefern noch keine kollektiven Robin-Kerne
für ein stromtragendes Fe-Ni-Plasma.

## 6. Ladungsclosure

Für jeden vorgegebenen Wert `Q_bullet` wird das gekoppelte Randwertproblem
gelöst. Daraus folgen

```text
dotN_e(Q_bullet)
dotN_a(Q_bullet).
```

Der reine Capture-Strom ist

```text
F_cap(Q_bullet)
= e [sum_a Z_a dotN_a(Q_bullet) - dotN_e(Q_bullet)].
```

Eine reale Ladungsbilanz lautet allgemeiner

```text
F_tot(Q_bullet) = F_cap(Q_bullet) + I_other(Q_bullet).
```

`I_other` enthält nur explizit geprüfte zusätzliche Kanäle, beispielsweise
elektromagnetische Entladung, Paarerzeugung oder Teilchenemission. Der H0-Branch
setzt lediglich den Standard-Hawking-Term als Modellannahme auf null. Daraus
folgt nicht automatisch, dass alle elektromagnetischen oder QED-Kanäle null
sind.

Ein kontinuierlicher Kandidat erfüllt

```text
F_tot(Q_eq) = 0.
```

Die reduzierte skalare Ladungsdynamik ist lokal stabil, wenn

```text
F_tot'(Q_eq) < 0.
```

Diese Bedingung reicht nur bei einer klaren Zeitskalentrennung zwischen der
schnellen Plasma-/Transportrelaxation und der langsameren Ladungsentwicklung.
Andernfalls muss die vollständige gekoppelte zeitabhängige Stabilität untersucht
werden.

Für kleine Ladungszahlen gilt

```text
Q_bullet = N e
N in Z.
```

Ohne zusätzliche Emissionskanäle lautet die diskrete Mastergleichung

```text
dP_N/dt
= dotN_e(N+1) P_(N+1)
  + sum_a dotN_a(N-Z_a) P_(N-Z_a)
  - [dotN_e(N) + sum_a dotN_a(N)] P_N.
```

Das physikalisch relevante Ergebnis ist dann grundsätzlich die stationäre
Verteilung `P_N`, nicht nur ein kontinuierlicher Mittelwert.

## 7. Hintergrundströmung und Energie

Die minimale Charge-Closure ist nur geschlossen, wenn

```text
T_e(r), T_i(r), u(r), P(r), X(r)
```

als validierte Hintergrundprofile vorgegeben werden.

Soll Stage 3.95B diese Größen selbst vorhersagen, werden zusätzlich mindestens
Bulk-Massen-, Impuls- und getrennte Elektronen-/Ionen-Energiegleichungen
benötigt. Poisson plus Diffusion allein reicht dann nicht.

Diagnostische Gesamtgrößen sind

```text
Mdot_cap = m_e dotN_e + sum_a m_a dotN_a

I_cap = F_cap

P_dep = sum_s dotN_s <E_dep,s>.
```

Die Depositionsenergien `<E_dep,s>` dürfen nicht pauschal mit `m_s c^2`,
`k_B T` oder einem frei gewählten Wirkungsgrad identifiziert werden. Dafür wird
ein eigener Energie-Matching-Kern benötigt.

## 8. Randbedingungen

### 8.1 Äußerer Reservoirrand

Als Referenz gilt bei ausreichend großem `R`:

```text
n_a(R) = n_a,inf

n_e(R) = n_e,inf = sum_a Z_a n_a,inf

T_e(R) = T_e,inf

T_i(R) = T_i,inf.
```

Für das Potential gilt im unendlichen Gebiet

```text
phi(infinity) = 0.
```

Bei endlichem `R` wird dies durch

```text
phi(R) = 0
```

approximiert. `E(R)=0` darf dann nicht als zusätzliche unabhängige
Randbedingung aufgezwungen werden. Stattdessen ist die verbleibende
Fernfeldladung als Domänenfehler zu überwachen.

Für die Bulkströmung muss genau eine Randwahl getroffen werden:

```text
u(R) = u_inf
```

oder

```text
Mdot(R) = Mdot_inf.
```

Dichte, Geschwindigkeit und Massenfluss dürfen nicht unabhängig überbestimmt
werden.

### 8.2 Innerer Elektrostatikrand

Am Matchingradius gilt

```text
-4 pi epsilon_0 r_m^2 phi'(r_m+) = Q_m

Q_m = M_Q(Q_bullet, inner state).
```

`Q_m` ist keine freie Randzahl und im Allgemeinen nicht gleich `Q_bullet`.

### 8.3 Innerer Sinkrand

Für jede Spezies gilt

```text
-J_s(r_m) = C_s(Q_bullet, local distribution),
```

beziehungsweise im zulässigen Robin-Grenzfall

```text
-J_s(r_m) = kappa_s(Q_bullet, ...) n_s(r_m).
```

Der perfekt absorbierende Stage-3.95A-Randwert

```text
n_s(r_m) = 0
```

entspricht formal

```text
kappa_s -> infinity.
```

### 8.4 Thermische Randbedingungen

Werden `T_e` und `T_i` nicht als feste Hintergrundprofile verwendet, benötigt
jede Energiegleichung eine konsistente äußere und innere Randbedingung.
Temperatur und Wärmefluss dürfen am selben Rand nicht unabhängig überbestimmt
werden.

### 8.5 Matchingradius

`r_m` muss in einem Überlappungsbereich liegen, in dem sowohl die äußere
WDM-Transportbeschreibung als auch die innere Capture-/Screeningbeschreibung
gültig sind. Nach konsistenter Transformation von `Q_m` und `kappa_s` darf eine
Verschiebung von `r_m` innerhalb dieses Bereichs die physikalischen Outputs
nicht wesentlich verändern.

Der bisherige Wert `r_m=6.13e-8 m` ist ein projektinterner
Bondi-/Materialradius, kein mikroskopisch hergeleiteter universeller Sinkrand.

## 9. Benötigte Eingabedaten und Repo-Stand

| Block | Erforderliche Daten | Repo-Stand | Bewertung für Stage 3.95B |
|---|---|---|---|
| Geometrie | `M`, `r_m`, `R`, innere Metrik | teilweise vorhanden | `M=1e11 kg`, `r_m=6.13e-8 m`, `R=1e5 m` sind Referenzwerte; `r_m` ist nicht mikroskopisch geschlossen |
| Thermischer Zustand | `P(r)`, `rho(r)`, `T_e(r)`, `T_i(r)`, `X(r)` | teilweise | einzelne Outer-Core-Referenzen, kein vollständiger validierter Zwei-Temperatur-Zustand |
| Mischungs-EOS | freie Energie oder konsistente `P,e,s,mu_s` für Fe-Ni-Light | Quelle verifiziert, numerische Closure offen | Liu/Asimow-Datensatz aus A22 ist ein Ausgangspunkt, aber im Repo noch keine vollständige numerische Mischungsclosure |
| Chemische Potentiale | `mu_s^chem` und `partial mu_s/partial n_t` | fehlt | für thermodynamische Faktoren und Screening zwingend |
| Ionisation | ganzzahlige `Z_a`, Populationen, Reaktionsraten | fehlt | `Zbar=2.76` und `Z=26` sind nur Proxy-/Stressendpunkte |
| Ionen-Selbstdiffusion | `D_Fe,self`, `D_Ni,self` | Literaturanker vorhanden | strukturelle Zeitskalenanker, keine Charge-Closure |
| Ionen-Mehrkomponententransport | `D_tilde_ab` oder `L_ab^(i)` samt Unsicherheit | fehlt | expliziter A31-Blocker |
| Elektronenleitfähigkeit | `sigma_e(P,T,X)` | Untergrenzenanker vorhanden | nicht ausreichend für den vollständigen Elektronenflussoperator |
| Elektronen-WDM-Kinetik | Kollisionskern, chemische/thermische Antwort, Relaxationszeiten | fehlt für Fe-Ni-Light | methodische Literaturanker vorhanden, kein direkt einsetzbarer Projektdatensatz |
| Screening | `n_e`, `E_F`, `v_F`, `lambda_TF`, statische Profile | teilweise vorhanden | A28 ist Fixed-Ion-/Nullstrom-Referenz, keine dynamische Closure |
| Sink-Capture | `P_cap,e`, `P_cap,a`, `kappa_e`, `kappa_a` | Teilproxies | A25/A29 sind statische Elektronenreferenzen, keine kollektiven Robin-Kerne |
| Inneres Ladungsmatching | `Q_bullet -> Q_m` | fehlt | zentraler Pflichtinput |
| Magnetotransport | `B(r)`, Hallparameter, tensorielle Koeffizienten | fehlt | vor Freigabe eines skalaren 1D-Modells zu prüfen |
| Reaktionen | Ionisation, Rekombination, Ladungsaustausch, gegebenenfalls QED | fehlt | nur nach quantitativer Zeitskalenprüfung vernachlässigbar |
| Energie | Elektron-Ion-Kopplung, Wärmeleitung, Depositionskern | unvollständig | Heizleistung sonst nur bedingte Diagnostik |
| Unsicherheiten | Fehler, Kovarianzen, Gültigkeitsdomänen | unvollständig | für ein belastbares `Q_eq` zwingend |

Liu und Asimow, JGR Solid Earth (2025), DOI `10.1029/2024JB030419`,
behandeln Fe-Ni sowie Fe-O, Fe-Si, Fe-S, Fe-C, Fe-H und ausgewählte
Mehrkomponentenmischungen. Der zugehörige CaltechDATA-Datensatz hat DOI
`10.22002/dxgqf-tw269`. Nach A22 sind Quelle, Dateiinventar und Lizenz
verifiziert; die numerische Workbook-Ingestion und daraus abgeleitete freie
Energie bleiben offen.

Ohta et al., Physics of the Earth and Planetary Interiors 363, 107351 (2025),
DOI `10.1016/j.pepi.2025.107351`, liefern für Fe-Ni-Si am oberen Außenkern eine
elektrische Leitfähigkeitsuntergrenze von ungefähr

```text
sigma_e >= 9.2e5 S/m.
```

Dieser Wert bleibt ein Leitfähigkeitsanker und keine vollständige
elektrochemisch-thermische Elektronen-Transportmatrix.

## 10. Fehlende Daten und Identifizierbarkeits-Gate

Vor jeder realen `Q_eq`-Implementierung müssen mindestens vier absolute
Blocker geschlossen oder als kontrollierte, quellengestützte Sensitivitätsachsen
deklariert sein:

```text
1. multikomponentige ionische Transportmatrix
2. elektronischer WDM-Transportoperator
3. thermodynamisch konsistente Mischungsableitungen
4. innere Sink-/Screening-Abbildung.
```

Konkret fehlen:

```text
L_ij^(i)(P,T,X) oder vollstaendige Maxwell-Stefan-Matrix
thermodynamische Faktoren und chemical-potential derivatives
Fe-Ni-Light Elektronen-Response j_e(E,grad mu_e,grad T_e,...)
ganzzahlige Ladungszustandsverteilung
Q_bullet -> Q_m
kappa_e(Q_bullet,state)
kappa_a(Q_bullet,state)
T_e/T_i- und Energieaustausch-Closure
Magnetisierungspruefung
Reaktions-/Entladungskanal-Audit
vollstaendige Unsicherheiten und Kovarianzen
datengetragener zulaessiger Q_bullet-Bereich.
```

Das Daten-Gate gilt erst als bestanden, wenn für jeden numerisch verwendeten
Koeffizienten dokumentiert sind:

```text
Quelle / DOI / Datensatz
physikalische Definition
SI-Einheit
P-T-X- und gegebenenfalls Q-Gueltigkeitsbereich
Interpolationsverfahren
Extrapolationsverbot oder begruendete Extrapolationsregel
Unsicherheit und Kovarianz
Lizenz und lokale Pruefsumme.
```

Bis dahin bleibt der Status exakt:

```text
Stage 3.95B mathematisch spezifiziert: PASS
physikalische Datenidentifizierbarkeit: OPEN
Implementierung reales Q_eq: BLOCKED BY MISSING CLOSURE DATA
```

## 11. Regressionen gegen Stage 3.95A

Stage 3.95A bleibt unverändert die analytische Referenz. Stage 3.95B muss im
folgenden künstlichen Grenzfall exakt auf sie zurückfallen:

```text
eine positive Ionenspezies mit ganzzahligem Z
keine Reaktionen: S_e=S_i=0
keine Bulkstroemung: u=0
konstante T_e und T_i
ideale chemische Potentiale
diagonaler Nernst-Planck-Transport ohne Kreuzterme
keine induzierte Screeningladung: Q_m=Q_bullet
ungeschirmtes Coulombpotential
perfekt absorbierender Sink: kappa_s -> infinity.
```

Dann muss gelten

```text
J_s
= -D_s [dn_s/dr + n_s/(k_B T_s) dU_s/dr]

dotN_s = A_s h(x_s)

h(x) = x/[1-exp(-x)]

A_s = 4 pi D_s Phi_s n_s,inf / (1/r_m - 1/R).
```

Pflichtregressionen sind:

```text
h(0)=1 durch stetige Fortsetzung
h'(0)=1/2
h'(x)>0 fuer alle endlichen Testwerte
h(x)~x fuer x->+infinity
h(x)~|x| exp(-|x|) fuer x->-infinity
A34-ODE-Residual auf 400 logarithmischen Radialpunkten
radiale Flusserhaltung dotN_s(r)=const.
exakte A34-Randwerte
Regression gegen das alte falsche exponentielle Innenprofil
F'(Q)<0 im ungeschirmten diagonalen Toy-Grenzfall
(D_e/D_i)_crit=132.876774528 im Default-Grenzfall
vorhandene kontinuierliche Toy-Roots des D_e/D_i-Scans
diskrete Generator-, Momenten-, Trunkierungs- und OU-Checks.
```

Zusätzliche interne Grenztests:

```text
Fixed-Ion / Nullstrom / identisches Elektronen-EOS -> A28
isolierter Elektronencapture / identisches Potential -> A25/A29
Fe/Ni self-D -> nur A30-Zeitskalenanker, keine Mobility-Closure.
```

Außerhalb des künstlichen Stage-3.95A-Grenzfalls sind weder globale Monotonie
von `F(Q)` noch Eindeutigkeit des Roots analytisch garantiert. Ein späterer
Solver muss alle Nullpunkte im datenmäßig zulässigen Bereich suchen und
klassifizieren.

## 12. Erwartete Outputs

Für jeden datenmäßig zulässigen Wert von `Q_bullet`:

```text
n_e(r;Q_bullet)
n_a(r;Q_bullet)
phi(r;Q_bullet)
E_r(r;Q_bullet)
rho_q(r;Q_bullet)
Q_enc(r;Q_bullet)
Q_m(Q_bullet)
J_e(r;Q_bullet)
J_a(r;Q_bullet)
dotN_e(Q_bullet)
dotN_a(Q_bullet).
```

Für die Ladungsclosure:

```text
F_cap(Q_bullet)
F_tot(Q_bullet)
alle Roots {Q_eq,k}
F_tot'(Q_eq,k)
Stabilitaetsklassifikation
Root-Brackets und Datengueltigkeitsflags.
```

Für kleine Ladungszahlen zusätzlich:

```text
stationaere Verteilung P_N
<Q>
Var(Q)
Modus und Quantile
Ladungsfluktuationszeit.
```

Globale Diagnostiken:

```text
Mdot_cap
I_cap
P_dep
elektronische und ionische Stromanteile
Entropieproduktion
Elektron-Ion-Energieaustausch
gegebenenfalls lokales Heizprofil.
```

Jeder physikalische Output benötigt zusätzlich:

```text
Datenquellen und Versionen
Gültigkeitsdomänen
Unsicherheitsensemble
Mesh- und Domaenenkonvergenz
Matchingradius-Sensitivitaet
Differential- und Integralresiduen
Interpolations-/Extrapolationsstatus
Warnungen zu fehlenden physikalischen Kanaelen.
```

Ein einzelner nominaler Wert für `Q_eq` ohne Unsicherheitsband, Root-Bracket,
Gültigkeitsflags und `Q_bullet/Q_m`-Unterscheidung ist kein zulässiger
Stage-3.95B-Output.

## 13. Numerische Residual- und Konvergenzkriterien

Mit

```text
L = R-r_m
```

und explizit deklarierten numerischen Floors gelten als Mindestschwellen:

### 13.1 Kontinuität

```text
epsilon_cont,s
= ||r^-2 (r^2 J_s)' - S_s||_inf
  / max(||S_s||_inf, ||J_s||_inf/L, S_floor)
<= 1e-8.
```

Für `S_s=0`:

```text
epsilon_flux,s
= max_r |dotN_s(r)-mean(dotN_s)|
  / max(|mean(dotN_s)|, dotN_floor)
<= 1e-8.
```

### 13.2 Poisson und Gauss

```text
epsilon_P
= ||r^-2 (r^2 phi')' + rho_q/epsilon_0||_inf
  / max(||rho_q/epsilon_0||_inf, ||phi||_inf/L^2, P_floor)
<= 1e-8.
```

```text
epsilon_G
= |Q_enc(R)-Q_m-4 pi integral_(r_m)^R rho_q r^2 dr|
  / max(e, |Q_m|, 4 pi integral_(r_m)^R |rho_q| r^2 dr)
<= 1e-8.
```

### 13.3 Sinkrand

```text
epsilon_R,s
= |-J_s(r_m)-C_s|
  / max(|J_s(r_m)|, |C_s|, J_floor)
<= 1e-10.
```

### 13.4 Root

```text
epsilon_F
= |F_tot(Q_eq)|
  / max(sum_s |q_s dotN_s|, F_floor)
<= 1e-10.
```

Die Normierung über die Summe der absoluten Teilströme verhindert, dass eine
schlechte Subtraktion zweier großer Ströme als guter Root erscheint.

### 13.5 Diskretisierung und Domäne

Bei mindestens einer Verdopplung der Radialauflösung und verschärfter
Solver-Toleranz müssen gelten:

```text
|Delta Q_eq|/max(e,|Q_eq|) <= 1e-4

|Delta dotN_s|/max(|dotN_s|,dotN_floor) <= 1e-4.
```

Der äußere Radius `R` ist so zu vergrößern, dass dieselben Größen innerhalb
dieser Schwelle stabil bleiben.

Nach konsistenter Transformation der inneren Matchingdaten soll eine Variation
von `r_m` innerhalb des nachgewiesenen Überlappungsintervalls die physikalischen
Outputs um höchstens `1%` verändern. Eine stärkere Abhängigkeit zeigt ein
unzureichendes Innen-/Außenmatching.

Für die diskrete Mastergleichung müssen bei Vergrößerung des Ladungsintervalls
gelten:

```text
|sum_N P_N - 1| <= 1e-12
P_boundary < 1e-12
kein stationaerer Wahrscheinlichkeitsstrom aus dem Trunkierungsrand
relative Momentaenderungen < 1e-6.
```

### 13.6 Transport- und Thermodynamikchecks

Bei `B=0`:

```text
||L-L^T||/||L|| <= 1e-10

lambda_min[(L+L^T)/2] >= -1e-12 lambda_max.
```

Zusätzlich:

```text
n_s(r) > 0
T_e(r) > 0
T_i(r) > 0
0 <= f_e <= 1
nichtnegative Gesamtentropieproduktion
konservative Elektron-Ion-Impuls- und Energiebilanz.
```

Ein Koeffizient außerhalb seines publizierten `P-T-X-Q`-Bereichs führt zu

```text
OUT OF DATA DOMAIN
```

und nicht zu einem extrapolierten physikalischen Ergebnis.

## 14. Stabilitäts- und Falsifikationskriterien

Ein kontinuierlicher Root ist im reduzierten Modell nur dann stabil, wenn

```text
F_tot'(Q_eq) + delta F' < 0,
```

das Vorzeichen also auch unter numerischer und datenseitiger Unsicherheit
negativ bleibt. `F'` muss mit mehreren Schrittweiten oder einem unabhängigen
Tangentenproblem überprüft werden.

Die quasi-stationäre Reduktion ist nur zulässig, wenn als vorab definiertes Gate

```text
tau_fast/tau_Q <= 0.1

tau_Q = -1/F_tot'(Q_eq)
```

gilt. Andernfalls ist die vollständige zeitabhängige Stabilität erforderlich.
Nach Entfernung reiner Eich- und Erhaltungsmoden muss dann für jede physikalische
Eigenmode gelten

```text
Re(lambda_k) < 0.
```

Stage 3.95B scheitert für einen vollständig spezifizierten Datenbranch, wenn
mindestens eines gilt:

```text
kein Root im gesamten physikalisch und datenmaessig zulaessigen Q-Bereich
alle Roots instabil
Root nur ausserhalb der Daten-/Modellgueltigkeit
Feld oder Potential sprengt Screening-/Transportannahmen
vernachlaessigter Reaktions-, Magnet-, Entladungs- oder QED-Kanal ist relevant
negative Dichten, ungueltige Besetzungen oder negative Entropieproduktion
Teilchen-, Ladungs- oder Energiebilanzen schliessen nicht
keine Mesh-, Domaenen- oder Matchingradius-Konvergenz
Akkretions-, Strom- oder Heizleistung verletzt vorab gesetzte Bounds
unkontrollierte Extrapolation ist fuer den Root erforderlich.
```

Interpretationsregel:

```text
Kein Vorzeichenwechsel innerhalb eines zu kleinen Datenintervalls -> OPEN.
Unterschiedliche Roots fuer zulaessige Datensaetze -> NOT IDENTIFIED.
Numerischer Residual-Fail -> SOLVER FAIL, nicht physikalische Falsifikation.
Stabiler datengetragener Root -> Modellclosure PASS, kein BH-Nachweis.
```

## 15. Empfohlene spätere Dateistruktur

Eine spätere Implementierung soll die vier Physikblöcke auch im Code trennen:

```text
stage3_95b_a35/
    __init__.py
    contracts.py
    electron_transport.py
    ion_transport.py
    electrostatics.py
    sink_boundary.py
    charge_closure.py
    diagnostics.py

data/stage3_95b/
    manifest.yaml
    README.md
    checksums.txt

tests/
    test_stage3_95b_electron_transport.py
    test_stage3_95b_ion_transport.py
    test_stage3_95b_electrostatics.py
    test_stage3_95b_sink_boundary.py
    test_stage3_95b_charge_closure.py
    test_stage3_95b_stage3_95a_regression.py
    test_stage3_95b_conservation_and_residuals.py
```

Verantwortlichkeiten:

```text
contracts.py
    Einheiten, Zustandsobjekte, Datenprovenienz und Modulschnittstellen

electron_transport.py
    ausschliesslich quellengestuetzte Elektronenkinetik/-Response

ion_transport.py
    Onsager-/Maxwell-Stefan-Transport und Reaktionskopplung

electrostatics.py
    Poisson, Q_enc, Screening und Gauss-Audit

sink_boundary.py
    Q_bullet -> Q_m, Capture-Kerne und Robin-Randoperatoren

charge_closure.py
    gekoppeltes Randwertproblem, F(Q), Roots und Stabilitaet

diagnostics.py
    Residuen, Konvergenz, Unsicherheiten und Ergebnis-Audit

manifest.yaml
    nur zitierte Daten mit Einheiten, Gueltigkeit und Pruefsummen.
```

Vor bestandenem Daten-Gate werden keine dieser Solverdateien angelegt.

Die vorhandenen Stage-3.95A-Dateien bleiben unverändert:

```text
STAGE3_95A_A35_DIAGNOSTIC_CHARGE_THEOREM.md
stage3_95a_a35_diagnostic_charge_theorem.py
test_stage3_95a_a35_diagnostic_charge_theorem.py
```

## Schlussstatus

```text
strikte Trennung Elektronen / Ionen / Elektrostatik / Sink:
SPECIFIED.

Q_bullet versus Q_m:
SPECIFIED / NICHT GLEICHGESETZT.

Stage-3.95A-Grenzregressionen:
SPECIFIED / NOCH NICHT IMPLEMENTIERT.

Material-/EOS-/Transportdaten:
PARTIAL / ZENTRALE CLOSURE-DATEN FEHLEN.

Stage 3.95B mathematisch spezifiziert:
PASS.

physikalische Datenidentifizierbarkeit:
OPEN.

Implementierung reales Q_eq:
BLOCKED BY MISSING CLOSURE DATA.

experimenteller BH-Nachweis:
NONE.
```
