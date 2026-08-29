# Stage 3.95A / A35 – Diagnostic Charge Theorem

**Projekt:** SL/BH-Kernhypothese Erdmodul
**Datum:** 29.08.2026
**Status:** TOY-A35 MONOTONIETHEOREM PASS / DISKRETE LADUNGSDIAGNOSTIK PASS / REALES `Q_eq` OPEN

## Ziel und Aussagegrenze

Stage 3.95A erweitert die korrigierte stationaere A34-Ein-Spezies-Loesung um einen mathematisch kontrollierten Elektron-Ion-Diagnostikblock.

Getestet werden:

```text
stabile Auswertung des Driftfaktors bei x -> 0
analytische Monotonie der ungeschirmten diagonalen Zwei-Spezies-Closure
Existenz und Stabilitaet des kontinuierlichen Toy-Nullpunkts
Sensitivitaet gegen D_e/D_i, Z und T_e/T_i
diskrete Ladungszustaende N=Q/e mit Elektronen- und Ionencapture
```

Nicht enthalten sind:

```text
reale Fe/Ni-Light-Element-Stofftransportmatrix
quantenkinetischer Elektron-Ion-Transport
nichtlineare Screening-/Poisson-Closure
mikroskopisch hergeleitete Q-abhaengige Sink-Capture-Kerne
physikalisch identifizierter Erdwert fuer Q_eq
```

Damit gilt ausdruecklich:

```text
Toy-A35 Mathematik:                       PASS
stabiler Toy-Q_eq innerhalb des Modells:  analytisch bewiesen
diskrete endliche Markov-Diagnostik:       PASS
numerischer Toy-Q_eq als Erdwert:          NICHT INTERPRETIERBAR
reales multikomponentiges A35-Q_eq:        OPEN
experimenteller BH-Nachweis:               NONE
```

## Kontinuierliches Referenzmodell

Fuer Spezies `s` mit Ladungszahl `z_s` gilt

```text
q_s = z_s e
z_e = -1
z_i = Z > 0.
```

Das absichtlich ungeschirmte Referenzpotential lautet

```text
U_s(r,N) = -G M m_s/r + k_e z_s e^2 N/r,
Q = N e.
```

Mit

```text
Delta = 1/r_match - 1/R > 0

alpha_s(N) = [G M m_s - k_e z_s e^2 N]/(k_B T_s)
x_s(N)     = alpha_s(N) Delta
```

und dem A34-Randwertproblem folgt

```text
dotN_s(N) = A_s h[x_s(N)]

A_s = 4 pi D_s Phi_s n_s,inf / Delta

h(x) = x/[1-exp(-x)].
```

`A_s` ist positiv. `D_s`, `Phi_s` und `n_s,inf` sind in Stage 3.95A freie Toy-Eingaben und keine vollstaendige WDM-Mobilitaetsclosure.

Die Ladungsdrift in Einheiten elementarer Ladungen pro Sekunde ist

```text
f(N) = dN/dt
     = sum_s z_s dotN_s(N)
     = Z dotN_i(N) - dotN_e(N).
```

In SI-Einheiten:

```text
F(Q) = dQ/dt = e f(N).
```

## Numerisch stabiler Driftfaktor

Direkte Auswertung von `1-exp(-x)` verliert fuer `x -> 0` Stellen. Die Implementierung verwendet deshalb `expm1` und lokal

```text
h(x) = 1 + x/2 + x^2/12 - x^4/720 + x^6/30240 + O(x^8)

h'(x) = 1/2 + x/6 - x^3/180 + x^5/5040 + O(x^7).
```

Fuer stark negatives `x` wird die algebraisch aequivalente Form

```text
h(x) = (-x) exp(x)/[1-exp(x)]
```

verwendet. Damit erzeugt starke Coulomb-Abstossung keine Exponential-Ueberlaeufe.

Die Grenzfaelle sind:

```text
x >> 1:   h(x) ~ x                    starke Anziehung
x -> 0:   h(x) -> 1                   verschwindender Nettodrift
x << -1:  h(x) ~ |x| exp(-|x|)        starke Abstossung
```

## Monotonietheorem

Fuer `x != 0` gilt

```text
h'(x) = [1-(1+x)exp(-x)]/[1-exp(-x)]^2.
```

Multiplikation des Zaehlerterms mit `exp(x)>0` reduziert die Vorzeichenfrage auf

```text
exp(x) - 1 - x > 0
```

fuer `x != 0`. Dies folgt aus der strikten Konvexitaet der Exponentialfunktion. Am hebbaren Punkt `x=0` gilt

```text
h'(0)=1/2>0.
```

Damit ist

```text
h'(x)>0
```

fuer jedes endliche reelle `x`.

Weiter gilt

```text
dx_s/dN = -k_e z_s e^2 Delta/(k_B T_s).
```

Also folgt direkt

```text
f'(N)
= - sum_s A_s h'[x_s(N)]
    k_e z_s^2 e^2 Delta/(k_B T_s)
< 0.
```

Das Vorzeichen ist unabhaengig davon, ob die Spezies positiv oder negativ geladen ist, weil `z_s^2` auftritt.

Unter den Toy-Annahmen und fuer unbeschraenktes `N` gilt ausserdem:

```text
N -> -infinity:  Ionen stark angezogen, Elektronen abgestossen -> f(N)>0
N -> +infinity:  Elektronen stark angezogen, Ionen abgestossen -> f(N)<0.
```

Aus Stetigkeit und strenger Monotonie folgt:

```text
Es existiert genau ein kontinuierlicher Toy-Nullpunkt f(N_eq)=0.
Er ist stabil, weil f'(N_eq)<0.
```

Da `Q=eN` und `F=e f` gilt

```text
dF/dQ = f'(N)

tau_Q = -1/f'(N_eq).
```

`tau_Q` besitzt damit die Einheit Sekunden. Die numerische Groesse ist nur so physikalisch wie die eingesetzten Toy-Raten.

## Default-Skalen

Fuer die A34-Referenzwerte

```text
M       = 1e11 kg
T_i     = 5500 K
m_i     = 55.845 u
r_match = 6.13e-8 m
R       = 1e5 m
Zbar    = 2.76
```

folgt bei `N=0`:

```text
x_e = 1.30614e-3
x_i = 1.32964e2.
```

Pro zusaetzlichem `+e` aendern sich die Toy-Tiefen um

```text
Delta x_e = +4.95628e-2
Delta x_i = -1.36793e-1.
```

Im ungeschirmten Modell verschwindet der gravitative Driftterm bei

```text
Ion:      N ~ +972.004
Elektron: N ~ -0.0263531.
```

Der nichtganzzahlige Elektronenwert ist ein direktes Warnsignal gegen eine rein kontinuierliche Interpretation bei kleinen Ladungen.

## Kontinuierliche Sensitivitaetsdiagnostik

Bei aeusserer Toy-Quasineutralitaet

```text
n_e,inf = Zbar n_i,inf
```

reduziert sich die Bedingung `f(0)=0` unabhaengig vom Rootfinder auf

```text
(D_e/D_i)_crit
= (Phi_i/Phi_e) h(x_i)/h(x_e).
```

Fuer die Default-Transportfaktoren `Phi_i=Phi_e=1` gilt

```text
h(x_i) = 132.963571
h(x_e) = 1.000653

(D_e/D_i)_crit = 132.876774528.
```

Die Implementierung berechnet diesen Ausdruck separat von der direkten Ratenbilanz. Beide Wege stimmen auf Maschinenpraezision ueberein und der numerische Root liegt dann bei `N_eq~0`.

Der anschliessende Scan mit sonst gleichen Defaultwerten ergibt:

| `D_e/D_i` | kontinuierliches `N_eq=Q_eq/e` |
|---:|---:|
| `1` | `+713.484943` |
| `10` | `+210.219711` |
| `100` | `+11.539435` |
| `132.876775` | `~0` |
| `1000` | `-63.460952` |
| `2335.3` | `-85.587525` |

Alle Nullpunkte sind innerhalb des Toy-Modells stabil. Der Vorzeichenwechsel und die grossen Verschiebungen zeigen jedoch:

```text
Der numerische Wert ist ohne physikalisch geschlossene Elektronen-/Ionenraten
nicht identifizierbar.
```

`D_e/D_i` ist hier nur eine Scanachse. Insbesondere wird elektrische Leitfaehigkeit nicht als Elektronen-Selbstdiffusionskonstante umgedeutet.

## Diskrete Ladungszustaende

Fuer kleine Ladungszahlen ist

```text
N = Q/e in Z
```

die geeignetere Zustandsvariable. Fuer einen ganzzahligen Ionisationszustand `Z` werden die Uebergaenge

```text
Elektronencapture: N -> N-1  mit Rate dotN_e(N)
Ionencapture:      N -> N+Z  mit Rate dotN_i(N)
```

verwendet.

Die Mastergleichung lautet schematisch

```text
dP_N/dt
= dotN_e(N+1) P_(N+1)
+ dotN_i(N-Z) P_(N-Z)
- [dotN_e(N)+dotN_i(N)] P_N.
```

Der Solver baut auf einem endlichen Intervall eine Generator-Matrix `G` und loest

```text
G^T P = 0
sum_N P_N = 1.
```

Verwendete Generatorkonvention:

```text
Zeile i = Ausgangszustand
G_ij >= 0 fuer i != j
G_ii <= 0
sum_j G_ij = 0
dP/dt = G^T P.
```

Fuer `Z>1` ist der Prozess im Allgemeinen nicht detailed-balanced. Ein Ionensprung `N->N+Z` besitzt keinen einzelnen direkten Ruecksprung; der Rueckweg besteht aus `Z` aufeinanderfolgenden Elektronencaptures. Stage 3.95A beschreibt daher einen stationaeren Toy-Nichtgleichgewichtsprozess, kein hergeleitetes thermisches Ladungsgleichgewicht.

Uebergaenge ausserhalb des Intervalls werden zensiert. Deshalb gibt der Solver die Randwahrscheinlichkeit aus; nur bei vernachlaessigbarer Randmasse ist die Trunkierung akzeptabel.

Integer-Referenz mit `Z=3` und so gewaehltem Toy-`D_e/D_i`, dass der kontinuierliche Root bei `N=0` liegt:

```text
Zustaende             = -100 ... +100
kontinuierliches N_eq = 0
diskretes <N>         = -0.609144506
diskreter Modus       = -1
Var(N)                = 77.4584685
sigma_N               = 8.80105
Randwahrscheinlichkeit= 5.70e-16.
```

Dies ist keine Vorhersage fuer die BH-Ladung. Es zeigt reproduzierbar, dass ein kontinuierlicher Root die durch ungleiche Sprungweiten entstehende stationaere Ladungsverteilung nicht vollstaendig beschreibt. Insbesondere ist nicht `f(<N>)=0`, sondern die Verteilungsbilanz

```text
<Z dotN_i(N) - dotN_e(N)>_P = 0
```

die korrekte stationaere Bedingung fuer das erste Moment.

Die unabhaengig ausgewerteten ersten beiden Sprungmomentbilanzen sind

```text
sum_N P_N [Z dotN_i(N)-dotN_e(N)] = 0

sum_N P_N {
    dotN_e(N)(-2N+1)
  + dotN_i(N)(2ZN+Z^2)
} = 0.
```

Im Referenzlauf betragen die normierten Residuen

```text
erstes Moment:  1.58e-15
zweites Moment: 2.22e-14.
```

Die Loesungen fuer symmetrische Zustandsintervalle `[-100,100]`, `[-150,150]` und `[-200,200]` stimmen fuer Mittelwert, Varianz und Modus innerhalb der gesetzten Regressionstoleranzen ueberein.

Als weiterer unabhaengiger Linear-Noise-Crosscheck werden die Kramers-Moyal-Koeffizienten

```text
A(N) = Z dotN_i(N) - dotN_e(N)
B(N) = Z^2 dotN_i(N) + dotN_e(N)
```

am stabilen kontinuierlichen Root `N_*` verwendet. Mit

```text
kappa = -A'(N_*) > 0
Var_OU(N) = B(N_*)/(2 kappa)
```

folgt

```text
Var_OU(N)      = 77.2371816
Var_diskret(N) = 77.4584685
relative Differenz ~0.286%.
```

Die gute Uebereinstimmung ist ein Crosscheck der stationaeren Verteilung innerhalb des Toy-Modells, kein Beleg fuer die realen Capture-Raten.

## Bedeutung von `r_match`

Der verwendete Wert

```text
r_match = 6.13e-8 m
```

ist numerisch der bisherige projektinterne Bondi-/Materialradius `r_B`, den A34 als absorbierende innere Randflaeche verwendet. Er ist nicht der Ereignishorizont:

```text
r_Schw = 1.48523e-16 m
r_match/r_Schw = 4.12730e8.
```

Stage 3.95A benennt die Groesse deshalb `r_match` statt `r_sink`. Damit wird keine neue physikalische Herleitung behauptet. Offen bleibt die Abbildung

```text
Bondi-/Materialtransport bei r_match
-> innere kollisional-kinetische Zone
-> Screening
-> quantenmechanischer Horizon-Capture.
```

Eine spaetere Robin-Randbedingung darf erst dann als physikalisch gelten, wenn ihre Capture-Kerne aus dieser Innenstruktur abgeleitet oder belastbar parametrisiert wurden.

## Screening-Aussagegrenze

Die vorhandene kurze Thomas-Fermi-Skala gegenueber `r_match` spricht gegen ein nacktes `1/r`-Coulombfeld ueber das gesamte A34-Gebiet.

Stage 3.95A behauptet aber nicht, dass das reale Sinkpotential universell ein homogenes lineares Yukawa-Potential ist oder dass seine Wirkung durch einen einzelnen Faktor `exp(-r_match/lambda_TF)` gegeben wird. Die reale Rueckkopplung kann nichtlineare Screening-, Korrelations-, Degenerations-, Nichtgleichgewichts- und Randgeometrieeffekte enthalten.

Die robuste Aussage ist daher nur:

```text
bare A34-weite Coulomb-Rueckkopplung: keine physikalische Closure
genaue effektive Innen-/Sink-Rueckkopplung: OPEN
```

## Transportbloecke fuer Stage 3.95B

Das spaetere physikalische Modell soll nicht als unbelegte universelle `2x2`-Elektron-Ion-Onsager-Matrix formuliert werden. Es sind mindestens vier Bloecke getrennt zu schliessen:

```text
1. ionischer Fe/Ni/Light-Element-Stofftransport
2. elektronischer Ladungs- und Energietransport
3. Poisson/Screening/elektrochemische Rueckkopplung
4. Q-abhaengiger innerer Sink-Capture
```

White et al., Phys. Rev. E 100, 033213 (2019), DOI `10.1103/PhysRevE.100.033213`, behandeln multikomponentige WDM-Mutual-Diffusion in Maxwell-Stefan-/Onsager-Form. In der Born-Oppenheimer-Variante werden dabei Ionen klassisch und Elektronen quantenmechanisch per orbitalfreier DFT behandelt. Das Paper ist daher ein Anker fuer ionische Mehrkomponentendiffusion, nicht fuer eine fertige Elektron-Ion-Ladungsclosure.

Rightley und Baalrud, Phys. Rev. E 103, 063206 (2021), DOI `10.1103/PhysRevE.103.063206`, behandeln Elektron-Ion-Transport in WDM mit einer quantenkinetischen Uehling-Uhlenbeck-Beschreibung, Potential of Mean Force, Pauli-Blocking, Korrelation und Beugung. Auch dieser Literaturanker liefert keine direkt einsetzbaren Fe/Ni-Erdkern-Capture-Raten, zeigt aber, warum `D_e` nicht als frei aus einer Leitfaehigkeit abgeleitete skalare Diffusionskonstante geschlossen werden darf.

## Regressionen

`test_stage3_95a_a35_diagnostic_charge_theorem.py` prueft:

```text
01 stabiler x->0-Grenzwert und starke Driftgrenzen
02 h'(x)>0 auf dichtem reellen Testgitter
03 analytische Ableitung gegen unabhaengige finite Differenz
04 x_e, x_i und Delta-x pro Elementarladung
05 Gravitations-Cancellation-Skalen und r_match/r_Schw
06 f'(N)<0 ueber D-, Z-, T- und N-Gitter
07 bekannte Root-Sensitivitaetswerte
08 neutraler Toy-Root beim kritischen D_e/D_i
09 27-Punkte-D/Z/T-Scan mit ausschliesslich stabilen Roots
10 Generator-Sprungstruktur und Wahrscheinlichkeitserhaltung
11 stationaere diskrete Mastergleichung und kleine Randmasse
12 Schutz gegen nichtganzzahlige/mismatched diskrete Ionenladung
13 analytischer kritischer D_e/D_i-Quotient gegen Ratenbilanz und Root
14 erste und zweite stationaere Sprungmomentbilanz
15 Trunkierungskonvergenz fuer N_max=100, 150, 200
16 Kramers-Moyal/Ornstein-Uhlenbeck-Varianz gegen diskrete Varianz
```

```text
Stage-3.95A Regressionen: 16/16 PASS
```

## Reproduzierbare Dateien

- `stage3_95a_a35_diagnostic_charge_theorem.py`
- `test_stage3_95a_a35_diagnostic_charge_theorem.py`

Ausfuehrung:

```bash
python stage3_95a_a35_diagnostic_charge_theorem.py
python -m unittest -v test_stage3_95a_a35_diagnostic_charge_theorem.py
```

## Schlussstatus

```text
stabiler Driftfaktor h(x):                 PASS
analytisches h'(x)>0:                      PASS
analytisches f'(N)<0:                      PASS im diagonalen ungeschirmten Toy-Modell
eindeutiger stabiler kontinuierlicher Root: PASS im selben Toy-Modell
diskrete finite Ladungsdiagnostik:          PASS
Generator-/Momenten-/Trunkierungschecks:    PASS
Kramers-Moyal/OU-Varianz-Crosscheck:         PASS im Referenzfall
physikalischer Wert dieses Toy-Roots:       NICHT IDENTIFIZIERT
Stage 3.95B WDM/Screening/Sink-Closure:     OPEN
finales reales Q_eq:                        OPEN
experimenteller BH-Nachweis:                NONE
```
