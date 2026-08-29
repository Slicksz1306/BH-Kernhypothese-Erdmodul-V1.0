# Stage 3.95C / A35 – WDM Theoretical Closure Architecture

**Projekt:** SL/BH-Kernhypothese Erdmodul

**Datum:** 30.08.2026

**Status:** ARCHITEKTUR-DEFINITIONSGATE PASS AS SPECIFICATION / CLOSURE-INTERFACES TEILWEISE OPEN / NUMERISCHER `Q_eq`-SOLVER NO-GO

```text
Stage 3.95B Daten-Gate:                         ABGESCHLOSSEN
Stage 3.95C Architektur-Definitionsgate:         PASS AS SPECIFICATION
Closure-Interface-Erfuellung:                   OPEN
Solverfreigabe-Gate:                             NOT PASSED
Implementierung eines realen Q_eq-Solvers:      NO-GO
experimenteller BH-Nachweis:                    NONE
```

## 1. Ziel und Aussagegrenze

Stage 3.95C definiert die mathematische Architektur, in die spaeter belastbare
Thermodynamik-, Transport-, Ionisations-, Elektrostatik- und Sinkmodelle
eingesetzt werden koennen. Diese Stufe implementiert keinen numerischen
`Q_eq`-Solver, setzt keine neuen numerischen Koeffizienten ein und wertet keine
neuen Proxies als physikalische Closure auf.

Die Architektur beantwortet ausschliesslich:

1. Welche Module und Abhaengigkeiten sind erforderlich?
2. Welche Groessen sind vorgegeben und welche sind unbekannt?
3. Wie viele unabhaengige Stoff- und Flussfreiheitsgrade existieren?
4. Welche Gleichungen und Randbedingungen bilden ein wohldefiniertes System?
5. Welche Interfaces sind datengetrieben, ableitbar, modellabhaengig oder offen?
6. Unter welchen Bedingungen muss das System analytisch auf Stage 3.95A
   zurueckfallen?
7. Welche Bedingungen muessen vor der Freigabe eines Solvers erfuellt sein?

Ein spaeterer stabiler Root wuerde nur einen Root des dann definierten
Closure-Modells darstellen. Er waere weder ein experimenteller Nachweis eines
zentralen Schwarzen Lochs noch eine Bestaetigung der gesamten Kernhypothese.

## 2. Kein linearer Ableitungspfad

Die schematische Folge

```text
bulk state -> Z_s -> mu_s -> L_st -> phi -> n_s -> kappa_s -> dotN_s -> dotQ
```

darf nicht als lineare Kausalkette interpretiert werden. Insbesondere gilt:

```text
mu_s bestimmt L_st nicht.
n_s bestimmt kappa_s nicht.
Leitfaehigkeit bestimmt keinen vollstaendigen Elektronenflussoperator.
Selbstdiffusion bestimmt keine multikomponentige Onsager-Matrix.
Q_bullet bestimmt Q_m nicht ohne eine innere Matchingclosure.
```

Gleichgewichtsthermodynamik und dynamischer Transport sind verschiedene
Informationsklassen. Ebenso ist die Sinkmikrophysik ein eigenes Randmodul und
keine algebraische Folge der aeusseren Randdichte.

## 3. Dependency-Graph

```text
                                      bulk state B(r)
                       ┌────────────────────┼────────────────────┐
                       │                    │                    │
                       ▼                    ▼                    ▼
              ionization closure   thermodynamic closure   dynamic transport data
                       │                    │                    │
                       ▼                    ▼                    ▼
              species set, q_s      f, mu_s, H_st          L_st / Dtilde_st
                       │                    │                    │
                       └──────────────┬─────┴──────────────┬─────┘
                                      │                    │
                                      ▼                    ▼
                            electrochemical forces   flux constitutive law
                                      │                    │
                                      └──────────┬─────────┘
                                                 ▼
 Q_bullet ──► inner charge matching ──► Q_m   coupled outer BVP at frozen Q_bullet
      │                                          │
      │                                          ├──► phi(r), E(r)
      │                                          ├──► n_s(r)
      │                                          └──► J_s(r)
      │                                                   │
      │                                                   ▼
      │                                        boundary moments y_s,m
      │                                          ┌────────┴────────┐
      │                                          ▼                 ▼
      │                                kinetic lifting B_s    moment closure Ktilde_s
      │                                          │                 │
      │                                          ▼                 │
      │                                      f_s(r_m,p)            │
      │                                          │                 │
      ▼                                          ▼                 │
 sink microphysics ───────────────────────────► K_s ◄──────────────┘
                                                        │
                                                        ▼
                                                  dotN_s(Q_bullet)
                                                        │
 additional audited currents I_other ───────────────────┤
                                                        ▼
                                          dotQ_bullet = F_tot(Q_bullet)
                                                        │
                                                        ▼
                                          roots, stability, uncertainty
```

Die Randmomente `y_s,m` stehen fuer die vom aeusseren BVP tatsaechlich
gelieferten Groessen, mindestens `n_s(r_m)`, `J_s(r_m)`, Temperatur und lokale
Felder. Ein verteilungsabhaengiger Capture-Operator `K_s[f_s]` darf nur verwendet
werden, wenn das kinetische Lifting `B_s:y_s,m->f_s(r_m,p)` geschlossen ist.
Alternativ muss die Capture-Physik direkt durch einen Momentenoperator
`Ktilde_s[y_s,m]` geschlossen werden.

Der Graph besitzt selbstkonsistente Rueckkopplungen: `phi` beeinflusst die
elektrochemischen Potentiale, die Dichten erzeugen freie Ladung und diese
bestimmt wiederum `phi`. Eine solche gekoppelte Schleife ist zulaessig. Nicht
zulaessig ist ein unmarkierter Pfeil, der eine fehlende Closure nur durch eine
andere Zustandsvariable ersetzt.

## 4. Notation und Speziesfreiheitsgrade

### 4.1 Aufgeloeste Spezies

Es seien `K` positive ionische Spezies oder explizit aufgeloeste ionische
Ladungszustaende und eine Elektronenspezies vorhanden:

```text
S_count = K + 1.
```

Jede diskrete Spezies besitzt eine ganzzahlige Ladungszahl `z_s` und

```text
q_s = z_s e.
```

Ein mittleres `Zbar` darf als Zustandsgroesse oder mittlere Closure-Groesse
auftreten, darf aber nicht als nichtganzzahlige Sprungweite einer diskreten
Mastergleichung verwendet werden.

### 4.2 Baryzentrischer Referenzrahmen

Mit

```text
rho = sum_s m_s n_s
u   = [sum_s m_s n_s v_s] / rho
```

werden die Diffusionsfluesse relativ zum baryzentrischen Bulkfluss definiert:

```text
j_s = n_s (v_s-u)
J_s = n_s u + j_s.
```

Daraus folgt identisch

```text
sum_s m_s j_s = 0.
```

Deshalb existieren nur `S_count-1` unabhaengige Diffusionsmoden. Die volle
`S_count x S_count`-Darstellung besitzt einen Erhaltungsnullraum und darf nicht
naiv invertiert werden.

### 4.3 Projektionsdarstellung

Es sei `C` eine vollrangige Matrix

```text
C in R^(S_count x (S_count-1))
```

mit

```text
m^T C = 0.
```

Dann kann geschrieben werden

```text
j = C j_hat
X_hat = C^T X.
```

Die exakte Wahl der Basis in `C` ist frei, solange Nullraum, Einheiten und
Ruecktransformation dokumentiert sind. Physikalische Aussagen duerfen nicht von
der willkuerlichen Basiswahl abhaengen.

## 5. Bulk-Eingaben und Unknowns

### 5.1 Minimal erforderliche Bulk-Eingaben

Ein spaeterer physikalischer Branch benoetigt mindestens Profile oder ein
selbstkonsistentes Modell fuer

```text
T(r)
P(r)
rho(r)
Elementhaeufigkeiten X_a(r)
Phi_g(r)
B_field(r)
Omega
u(r)
r_m
R.
```

Wenn `u(r)` nicht extern vorgegeben wird, muss es aus einer eigenen Bulk-
Impuls-/Hydrodynamikclosure folgen. Die gegenwaertige Architektur setzt `u=0`
nicht automatisch voraus.

### 5.2 Outer Reservoir

Am aeusseren Rand seien EOS, Temperatur, Druck und Elementhaeufigkeiten gegeben.
Nach Quasineutralitaet verbleiben bei `S_count=K+1` insgesamt

```text
S_count - 2 = K - 1
```

unabhaengige Mischungsparameter, sofern keine weiteren Erhaltungsbedingungen die
Dimension weiter reduzieren.

## 6. Thermodynamische Kraefte

Die chemischen Potentiale muessen aus einer gemeinsamen thermodynamischen
Closure stammen:

```text
mu_s^chem = mu_s(T,{n_t}).
```

Die elektrochemischen Potentiale sind

```text
mu_tilde_s
= mu_s^chem + q_s phi + m_s Phi_g.
```

Eine konsistente Wahl thermodynamischer Kraefte ist

```text
X_s = - d/dr (mu_tilde_s/T)
X_T =   d/dr (1/T).
```

Im explizit isothermen Branch gilt

```text
X_T = 0.
```

Ein spaeterer nichtisothermer Branch muss den Waermefluss und die reziproken
thermischen Kreuzkoeffizienten gemeinsam behandeln; ein isolierter `L_sT X_T`-
Term ohne den zugehoerigen Waermeflussblock ist nicht closure-komplett.

## 7. Closure-Modul I: Ionisation und Reaktionen

Das Ionisationsmodul erhaelt den lokalen Bulkzustand und liefert

```text
I_Z: B, {n_s}, phi -> {
    aufgeloeste Spezies,
    ganzzahlige z_s fuer diskrete Zustaende,
    Gleichgewichts- oder Nichtgleichgewichtspopulationen,
    Reaktionsraten R_r
}.
```

Mit Stoechiometriekoeffizienten `nu_sr` lauten die Volumenquellen

```text
S_s = sum_r nu_sr R_r.
```

In Matrixform:

```text
S_vector = Nu_reac R_vector,
```

wobei `Nu_reac` die Spezies-mal-Reaktion-Stoechiometriematrix ist. Eine Matrix
`A_elem`, deren Zeilen die Zahl der Kerne jedes chemischen Elements in jeder
Spezies zaehlen, muss erfuellen:

```text
A_elem Nu_reac = 0.
```

Fuer jede interne Reaktion muessen mindestens gelten:

```text
sum_s q_s nu_sr = 0
sum_s m_s nu_sr = 0
Elementkerne werden fuer jedes Element separat erhalten.
```

Daraus folgen fuer interne Reaktionen lokal

```text
sum_s q_s S_s = 0
sum_s m_s S_s = 0.
```

Die Massenerhaltung ist dabei im nichtrelativistischen Transportbranch mit der
explizit gewaehlten Speziesmassendefinition zu verstehen. Ionisations- und
Bindungsenergien muessen in einem nichtisothermen/energetischen Branch separat
in der Energiebilanz erscheinen; sie duerfen nicht durch die reine Stoffbilanz
verschluckt werden.

Stage 3.95C trennt zwei Ionisationsbranches:

```text
frozen-charge-state branch:
    S_s = 0
    Ladungszustandspopulationen werden entlang des Transportgebiets eingefroren.

reactive-ionization branch:
    S_vector = Nu_reac R_vector({n_t},T,phi,...)
    Ladungs-, Massen- und Elementkernerhaltung sind Pflichtresiduen.
```

Der frozen-charge-state branch ist nur zulaessig, wenn die relevanten
Ionisations-, Rekombinations- und Ladungsaustauschzeiten gegen Transport- und
Ladungsrelaxationszeiten geprueft wurden. Der reactive-ionization branch benoetigt
die populations- und zustandsabhaengigen Raten als eigene Closure.

Sind die Reaktionsraten algebraische Funktionen des lokalen Zustands, aendert
sich die radiale Feldzaehlung nicht. Fuehrt ein kinetisches Reaktionsmodell
zusaetzliche Populations- oder Gedaechtnisfelder ein, muessen deren Gleichungen
und Rand-/Anfangsbedingungen separat gezaehlt werden.

Status:

```text
mathematische Schnittstelle:  SPECIFIED
frozen-charge-state branch:   SPECIFIED / PHYSICAL VALIDITY OPEN
reactive-ionization branch:   SPECIFIED AS INTERFACE
Fe-Ni-Light-WDM-Populationen: CURRENTLY UNAVAILABLE
Reaktionsraten:               CURRENTLY UNAVAILABLE
```

## 8. Closure-Modul II: Thermodynamik

Eine lokale thermodynamische Closure muss aus einem gemeinsamen Potential
stammen, beispielsweise einer freien Energiedichte

```text
f = f(T,{n_s}).
```

Dann gelten

```text
mu_s^chem = partial f/partial n_s

H_st = partial mu_s^chem/partial n_t
     = partial^2 f/(partial n_s partial n_t).
```

Die elektrochemischen Potentiale sind

```text
mu_tilde_s = mu_s^chem + q_s phi + m_s Phi_g.
```

Die Hesse-Matrix darf nicht im redundanten vollen Dichtekoordinatenraum
ungeprueft als positiv semidefinit verlangt werden. Es sei `C_th` eine
vollrangige Projektionsmatrix, deren Spalten genau den unter den gewaehlten
thermodynamischen Nebenbedingungen zulaessigen unabhaengigen
Zusammensetzungsvariationen entsprechen. Dann muessen gelten:

```text
H_st = H_ts
H_allowed = C_th^T H C_th
delta_y^T H_allowed delta_y >= 0
fuer alle zulaessigen delta_y.
```

Kurz:

```text
C_th^T H C_th >= 0
```

im Sinn positiver Semidefinitheit auf dem zulaessigen unabhaengigen Unterraum.
Wenn Transport- und Thermodynamikprojektion dieselben Nebenbedingungen und
dieselbe Basis verwenden, darf `C_th=C` gesetzt werden. Andernfalls muessen beide
Projektoren und ihre Transformation getrennt dokumentiert werden. Ob konstantes
Volumen, konstanter Druck, feste Elementbilanzen oder weitere Constraints gelten,
bestimmt ausserdem, welches thermodynamische Potential und welcher projizierte
Stabilitaetsoperator zulaessig sind.

Phaseninstabilitaet, Spinodalbereiche oder nichtkonvexe Mischungsmodelle muessen
als Domaenenfail behandelt werden. Ein EOS-Druckgitter allein bestimmt `H_st`
nicht.

Status nach dem Stage-3.95B-Daten-Gate:

```text
Zustands-/EOS-Anker:                       MEASURED/DATA-DRIVEN PARTIAL
begrenzter Fe-O-Si-Unterraum:              DERIVABLE IN SOURCE DOMAIN
vollstaendige Fe-Ni-Light-Hesse-Matrix:    CURRENTLY UNAVAILABLE
A35-Thermodynamikclosure:                  OPEN
```

## 9. Closure-Modul III: Dynamischer Transport

### 9.1 Stofftransport

Im baryzentrischen Projektionsraum lautet der lineare nichtgleichgewichtige
Stofftransport allgemein

```text
j_hat_alpha
= sum_beta L_hat_alpha,beta(B,Omega) X_hat_beta
+ L_hat_alpha,T(B,Omega) X_T.
```

Die Matrix ist in mindestens folgende physikalische Informationsbloecke zu
trennen:

```text
L_ii   ion-ion / multicomponent ionic block
L_ee   electronic block
L_ei   electron-ion cross transport
L_ie   reciprocal/cross block
L_sT   thermodiffusive cross terms.
```

Selbstdiffusion darf nur als diagonale Validierung oder Modellgrenze auftreten,
nicht als Ersatz fuer den vollen multikomponentigen Transportoperator.

### 9.2 Onsager-Casimir

Bei Magnetfeld und Rotation darf nicht pauschal

```text
L_alpha,beta = L_beta,alpha
```

gesetzt werden. Fuer Variablen mit Zeitumkehrparitaeten `eta_alpha` gilt
schematisch

```text
L_alpha,beta(B,Omega)
= eta_alpha eta_beta L_beta,alpha(-B,-Omega).
```

Fuer raeumlich tensorwertige Koeffizienten kommt die entsprechende raeumliche
Transposition hinzu.

Die Onsager-Casimir-Pruefung gilt fuer den vollen Transportoperator. Die
Symmetrie des dissipativen Anteils

```text
L_diss = (L + L^T)/2
```

ist dagegen eine Definition und darf nicht selbst als Reziprozitaetsnachweis
gewertet werden.

### 9.3 Dissipation im isothermen Stoffbranch

Im explizit isothermen Branch `X_T=0` muss der dissipative Anteil auf dem
projizierten Stoffraum erfuellen

```text
X_hat^T L_hat_diss X_hat >= 0.
```

Dies ist ein Entropieproduktions-/Dissipationskriterium. Es ist kein automatischer
Nachweis der Koerzivitaet und kein Nachweis, dass das vollstaendige gekoppelte
PDE-System parabolisch ist.

### 9.4 Nichtisothermer Waerme-/Stoffbranch

Sobald `X_T != 0` zugelassen wird, muss der Waermefluss als eigener Fluss mit dem
Stofftransport gekoppelt werden. Mit

```text
X_ext = [X_hat, X_T]^T
J_ext = [j_hat, J_q]^T
```

ist ein erweiterter Operator erforderlich:

```text
J_ext
= L_ext X_ext

L_ext = [ L_hat    L_hat,T ]
        [ L_T,hat  L_TT    ].
```

Dabei ist `J_q` der in der gewaehlten Referenzrahmen- und Enthalpiekonvention
definierte Waermefluss. `L_hat,T` und `L_T,hat` muessen den korrekten
Onsager-Casimir-Beziehungen unterliegen; `L_TT` ist die thermische dissipative
Closure. Die nichtnegative Entropieproduktion verlangt fuer den dissipativen
Anteil

```text
X_ext^T L_ext,diss X_ext >= 0.
```

Ein Modell, das `L_hat,T X_T` behaelt, aber `J_q`, `L_T,hat` und `L_TT` nicht
definiert, ist fuer `X_T != 0` closure-unvollstaendig.

Status:

```text
isothermer Stofftransportblock:        SPECIFIED AS INTERFACE
nichtisothermer Waerme-/Stoffblock:    SPECIFIED AS INTERFACE
voller L_hat-Stoffoperator:            CURRENTLY UNAVAILABLE
L_hat,T / L_T,hat / L_TT:              CURRENTLY UNAVAILABLE
Elektron-Ion-Kreuztransport:           CURRENTLY UNAVAILABLE
```

### 9.5 Nullraum- und restringierte Koerzivitaetspruefung

Die baryzentrische Erhaltungsnullmode gehoert zur vollen redundanten
Speziesdarstellung. Vor jeder Reduktion muss deshalb geprueft werden:

```text
ker(L_full,diss)
= erwartete physikalische Erhaltungsnullraeume
```

bis auf numerische Toleranz und explizit dokumentierte weitere Symmetriemoden.
Ein nicht erwarteter zusaetzlicher Nullvektor ist ein Transport-Gate-FAIL.

Nach Projektion mit `C` darf die baryzentrische Nullmode nicht nochmals als
Nullmode des reduzierten `L_hat_diss` gefordert werden. Auf dem tatsaechlich
dissipativen reduzierten Unterraum wird stattdessen die restringierte
Koerzivitaet geprueft. Wenn dort keine weitere physikalische Nullmode verbleibt,
gilt als Spektralgate

```text
lambda_min(L_hat_diss) > 0.
```

Verbleiben explizit begruendete reduzierte Nullmoden, wird entsprechend der
kleinste positive Eigenwert auf deren orthogonalem Komplement geprueft:

```text
lambda_min^+(L_hat_diss) > 0.
```

Dieses Spektralgate prueft die Koerzivitaet des betrachteten dissipativen
Transportoperators. Es beweist nicht automatisch die Parabolizitaet des
vollstaendigen nichtlinearen, elektrostatisch und reaktiv gekoppelten
PDE/DAE-Systems. Ein spaeterer Solverstage benoetigt dafuer einen separaten
Principal-Symbol-/Well-posedness-Test.

## 10. Closure-Modul IV: Elektrostatik und Screening

Stage 3.95C erlaubt zwei getrennte Response-Branches. Sie duerfen nicht dieselben
Freiheitsgrade doppelt enthalten.

### 10.1 Lokaler expliziter Ladungsbranch

Wenn alle mobilen Ladungstraeger explizit durch `n_s` beschrieben werden,

```text
rho_free(r) = sum_s q_s n_s(r)
```

und

```text
dphi/dr = -E
1/r^2 d/dr [r^2 epsilon_0 E] = rho_free.
```

Materialpolarisation, die nicht bereits in den expliziten Freiheitsgraden steckt,
darf ueber eine separat dokumentierte konstitutive Relation fuer `D` oder eine
andere Response-Closure aufgenommen werden.

### 10.2 Nichtlokaler / nonlinearer Response-Branch

Alternativ kann ein Response-Operator verwendet werden:

```text
rho_ind(r)
= integral chi(r,r';B,state) phi(r') 4 pi r'^2 dr'.
```

Dann muss die Ladungspartition explizit sein:

```text
rho_total = rho_resolved + rho_ind
```

mit

```text
rho_resolved: nur explizit transportierte Freiheitsgrade
rho_ind:      nur nicht bereits aufgeloeste induzierte Freiheitsgrade.
```

Keine Elektronen- oder Ionenantwort darf gleichzeitig in `n_s` und im Kernel
`chi` enthalten sein.

Status:

```text
lokaler Poisson-Branch:                DERIVABLE ONCE MATERIAL CLOSURES CLOSE
nichtlokaler Response-Branch:          MODEL-DEPENDENT / CURRENTLY UNAVAILABLE
projektspezifische Screeningpartition: OPEN
```

## 11. Closure-Modul V: Inneres Ladungsmatching Q_bullet -> Q_m

`Q_bullet` ist die Ladung des inneren Sink-/BH-Freiheitsgrads. `Q_m` ist die von
der aeusseren WDM-Domaene am Matchingradius wahrgenommene eingeschlossene
Ladung. Unter Screening oder innerer Polarisation gilt im Allgemeinen

```text
Q_m != Q_bullet.
```

Die notwendige Matchingclosure ist

```text
Q_m
= M_Q[
    Q_bullet,
    phi_m,
    E_m,
    {n_s,m},
    T_m,
    B_m,
    inner state,
    r_m
].
```

`M_Q` ist nicht aus dem aeusseren Poisson-BVP allein ableitbar. Im lokalen Branch
tritt `Q_m` als innere Gauss-Bedingung auf:

```text
4 pi r_m^2 epsilon_0 E(r_m+) = Q_m
```

oder aequivalent

```text
-4 pi r_m^2 epsilon_0 phi'(r_m+) = Q_m.
```

Status:

```text
mathematische Schnittstelle Q_bullet->Q_m: SPECIFIED
physikalische Matchingclosure M_Q:         CURRENTLY UNAVAILABLE
```

## 12. Closure-Modul VI: Sink- und Capture-Mikrophysik

Das aeussere Momenten-BVP liefert am Matchingradius nur eine endliche Menge von
Randmomenten:

```text
y_s,m = {
    n_s(r_m),
    J_s(r_m),
    T_m,
    phi_m,
    E_m,
    B_m,
    weitere explizit geloeste Momente
}.
```

Es liefert nicht automatisch die volle Verteilungsfunktion `f_s(r_m,p)`.
Stage 3.95C definiert deshalb zwei alternative Capture-Branches.

### 12.1 Kinetischer Boundary-Layer-Branch

Soll die allgemeine Capture-Schnittstelle auf der lokalen Randverteilung
operieren, ist zunaechst ein kinetisches Boundary-Layer-Lifting erforderlich:

```text
f_s(r_m,p)
= B_s[y_s,m,Q_bullet,inner state].
```

Die geliftete Verteilung muss mindestens die vom aeusseren BVP gelieferten
Momente reproduzieren:

```text
integral f_s dGamma_s = n_s(r_m)
integral v_r f_s dGamma_s = J_s(r_m)
f_s ist zulaessig, normiert und mit Statistik sowie Energieannahmen konsistent.
```

Erst danach ist der verteilungsabhaengige Capture-Operator definiert:

```text
C_s
= K_s[f_s(r_m,p),Q_bullet,phi_m,E_m,inner state].
```

`B_s` ist eine eigenstaendige kinetische Matchingclosure. Eine lokale
Maxwell-, Fermi-Dirac- oder Driftverteilung darf nicht ohne Gueltigkeits- und
Knudsen-/Relaxationspruefung als Default eingesetzt werden.

Wird der Boundary Layer durch eine eigene kinetische Gleichung geloest, fuehrt
er zusaetzliche Orts-/Impulsvariablen, Gleichungen und Randbedingungen ein. Die
Minimalzaehlung des aeusseren Momenten-BVP gilt dann nicht fuer das Gesamtsystem;
der kinetische Teil benoetigt ein separates Feld- und Randwertgate.

### 12.2 Direkter Momenten-Capture-Branch

Alternativ muss der Capture-Operator direkt auf den geloesten Randmomenten
geschlossen werden:

```text
C_s
= Ktilde_s[y_s,m,Q_bullet,inner state].
```

Dieser Branch benoetigt kein rekonstruiertes `f_s`, aber `Ktilde_s` bleibt eine
eigene theoretische Momentenclosure. Er darf nicht dadurch konstruiert werden,
dass nicht geloeste hoehere Momente stillschweigend auf frei gewaehlte Werte
gesetzt werden.

### 12.3 Flussrand und Robin-Spezialfall

Die innere Flussbedingung lautet bei nach aussen positivem radialem Fluss

```text
-J_s(r_m) = C_s >= 0.
```

Nur wenn `K_s o B_s` beziehungsweise `Ktilde_s` lokal, markovsch und linear in
der Randdichte ist, darf die kombinierte Randclosure auf eine Robin-Form
reduziert werden:

```text
-J_s(r_m)
= kappa_s(Q_bullet,state) n_s(r_m)

[kappa_s] = m s^-1.
```

Die positive Capture-Rate ist dann

```text
dotN_s(Q_bullet)
= 4 pi r_m^2 C_s
= -4 pi r_m^2 J_s(r_m).
```

`kappa_s` ist kein aus `n_s` ableitbarer Koeffizient. Die kombinierte
Boundary-/Captureclosure ist eine eigenstaendige theoretische Closure. Ein
Energieeintrag benoetigt zusaetzlich einen separaten Depositionsoperator;
`m_s c^2`, `k_B T` oder ein frei gewaehlter Wirkungsgrad sind keine Defaults.

Status:

```text
kinetisches Lifting B_s:                    SPECIFIED AS INTERFACE / CURRENTLY UNAVAILABLE
verteilungsabhaengiger Operator K_s:        SPECIFIED AS INTERFACE / CURRENTLY UNAVAILABLE
direkter Momentenoperator Ktilde_s:         SPECIFIED AS ALTERNATIVE / CURRENTLY UNAVAILABLE
Robin-Spezialfall:                          DERIVABLE IF COMBINED CLOSURE IS LOCAL AND LINEAR
physikalische K_s/Ktilde_s/kappa_s:         CURRENTLY UNAVAILABLE
Energie-Matchingkern:                       CURRENTLY UNAVAILABLE
```

## 13. Gekoppelte frozen-`Q_bullet`-BVP-Familie

Fuer jeden festgehaltenen Parameterwert `Q_bullet` wird ein bedingt stationaeres
aeusseres Randwertproblem geloest:

```text
BVP solved conditionally at frozen Q_bullet.
```

Diese BVP-Loesung ist ein Punkt einer quasi-stationaeren Fortsetzungsfamilie in
`Q_bullet`. Sie ist bei `F_tot(Q_bullet)!=0` kein stationaerer Zustand des
vollstaendigen Systems, weil sich die Sinkladung auf der langsameren Zeitskala
weiterentwickelt.

Fuer den lokalen Poisson-Branch, eine vorgegebene gemeinsame Temperatur und
vorgegebenes `u(r)` besteht der minimale Mehrkomponentenbranch aus:

```text
1/r^2 d/dr [r^2 J_s] = S_s

projected transport law for S_count-1 modes

sum_s m_s J_s = rho u

dphi/dr = -E

1/r^2 d/dr [r^2 epsilon_0 E] = sum_s q_s n_s
```

mit

```text
S_s = sum_r nu_sr R_r
Q_m = M_Q[Q_bullet,local inner state]

kinetic branch:
    f_s(r_m,p) = B_s[y_s,m,Q_bullet,inner state]
    -J_s(r_m) = K_s[f_s,Q_bullet,inner state]

or moment branch:
    -J_s(r_m) = Ktilde_s[y_s,m,Q_bullet,inner state].
```

Ohne konkrete Funktionen `f`, `L_hat`, `R_r`, `M_Q` und entweder
`B_s` plus `K_s` oder `Ktilde_s` ist dies eine Architektur, kein numerisch
geschlossenes Gleichungssystem.

## 14. Gleichungs-, Feld- und Randbedingungszaehlung

### 14.1 Minimaler lokaler Poisson- und Momenten-Capture-Branch mit vorgegebenem `u(r)`

Die unabhaengige BVP-Zaehlung muss den baryzentrischen Nullraum bereits entfernt
haben. Deshalb wird fuer den fixed-`u`-Branch nicht mit allen `S_count` Flussfeldern
als unabhaengigen Differentialfreiheitsgraden gezaehlt, sondern mit
`S_count-1` unabhaengigen Diffusionsfluesse `j_hat`.

Unabhaengige radiale Felder:

| Feldblock | Anzahl |
|---|---:|
| Speziesdichten `n_s` | `S_count` |
| unabhaengige Diffusionsfluesse `j_hat` | `S_count - 1` |
| Potential `phi` und Feld `E` | `2` |
| **Summe** | **`2 S_count + 1`** |

Die vollen Gesamtfluesse sind daraus abgeleitet:

```text
j = C j_hat
J_s = n_s u + j_s.
```

Unabhaengige Gleichungen:

| Gleichungsblock | Anzahl |
|---|---:|
| Spezieskontinuitaet | `S_count` |
| projizierte Transportgleichungen | `S_count - 1` |
| `dphi/dr=-E` | `1` |
| Gauss/Poisson | `1` |
| **Summe** | **`2 S_count + 1`** |

Die baryzentrische Beziehung

```text
sum_s m_s J_s = rho u
```

ist in dieser reduzierten Darstellung bereits durch `m^T C=0` und die
Rekonstruktion der Gesamtfluesse erfuellt. Sie ist deshalb keine zusaetzliche
unabhaengige Differentialgleichung.

Unabhaengige Randbedingungen:

| Randblock | Anzahl |
|---|---:|
| aeussere Reservoirwerte `n_s(R)=n_s,inf` | `S_count` |
| unabhaengige innere Capture-/Flussbedingungen | `S_count - 1` |
| aeussere Potentialeichung `phi(R)=0` | `1` |
| innere Gauss-/Matchingbedingung mit `Q_m` | `1` |
| **Summe** | **`2 S_count + 1`** |

Bei vorgegebenem `u(r_m)` duerfen die `S_count` einzelnen Capture-Raten nicht
beliebig unabhaengig gewaehlt werden. Die fehlende lineare Kombination ist eine
Kompatibilitaetsbedingung:

```text
sum_s m_s C_s
= - rho(r_m) u(r_m).
```

Aequivalent mit `dotN_s=4 pi r_m^2 C_s`:

```text
sum_s m_s dotN_s
= -4 pi r_m^2 rho(r_m) u(r_m).
```

Diese Beziehung ist ein Pflichtresiduum der kombinierten Capture-/Bulkclosure,
keine `S_count`-te unabhaengige BVP-Randbedingung. Liefert eine Captureclosure
`S_count` Raten, die diese Identitaet nicht erfuellen, ist der fixed-`u`-Branch
inkompatibel und muss FAIL liefern; die BVP-Zaehlung darf nicht durch eine
zusaetzliche BC kuenstlich auf `2 S_count+2` angehoben werden.

Die aeusseren Dichten sind ebenfalls nicht beliebig: EOS, Elementhaeufigkeiten
und Quasineutralitaet muessen als Eingangskompatibilitaet erfuellt sein. Am selben
Rand duerfen nicht zusaetzlich alle `mu_s` unabhaengig vorgegeben werden.

Die innere Gauss-Bedingung darf nicht gleichzeitig durch einen unabhaengigen
Wert fuer `phi(r_m)` ergaenzt werden. `phi(r_m)` ist ein Output des BVP.

### 14.2 Volle `J_s`-DAE-Darstellung

Alternativ duerfen alle `S_count` Gesamtfluesse `J_s` als Variablen mitgefuehrt
werden. Dann besitzt die Darstellung formal

```text
S_count n_s
+ S_count J_s
+ phi,E
= 2 S_count + 2 Variablen.
```

Sie benoetigt aber zusaetzlich die algebraische baryzentrische Nebenbedingung

```text
sum_s m_s J_s - rho u = 0.
```

Damit entsteht ein Differential-Algebraisches System. Die algebraische Bedingung
ist keine zusaetzliche BVP-Ordnung; auch hier verbleiben nur `2 S_count+1`
unabhaengige Randbedingungen. Insbesondere koennen weiterhin nicht alle
`S_count` inneren Capture-Fluesse unabhaengig neben fest vorgegebenem `u(r_m)`
erzwungen werden.

### 14.3 Selbstkonsistenter Bulkbranch

Ist `u(r)` nicht vorgegeben, muss eine konkrete Bulk-Dynamikclosure hinzukommen.
Im minimalen Fall kann `u` als zusaetzliches Feld mit einer passenden
Bulk-Impuls-/Hydrodynamikgleichung eingefuehrt werden. Gegenueber der reduzierten
fixed-`u`-Zaehlung gilt dann schematisch:

```text
+1 unbekanntes Feld u
+1 unabhaengige Bulk-Dynamikgleichung
+1 passende Bulk-Randbedingung, zum Beispiel u(R) oder Mdot(R), nicht beide.
```

Damit ergibt sich im entsprechenden first-order Minimalbranch

```text
2 S_count + 2
```

fuer unabhaengige Felder, Gleichungen und Randbedingungen. Die konkrete Ordnung
muss neu gezaehlt werden, wenn statt einer first-order Closure eine hoehere
Hydrodynamik-, Energie- oder Impulsstruktur verwendet wird.

### 14.4 Nichtlokaler Branch

Die formale Zahl der Felder `phi,E` bleibt zwei. Die Operatorordnung und die
erforderlichen Randfunktionale folgen jedoch nicht allein aus der lokalen
Poisson-Zaehlung. Deshalb gilt:

```text
chi nicht vollstaendig spezifiziert
-> Randwertzaehlung nicht abgeschlossen
-> Architektur-Gate FAIL
-> Solver NO-GO.
```

### 14.5 Expliziter kinetischer Boundary-Layer-Branch

Wenn `f_s` aus einer kinetischen Differential- oder Integro-Differentialgleichung
im inneren Uebergangsgebiet bestimmt wird, kommen mindestens hinzu:

```text
f_s(r,p) als zusaetzliche Phasenraumfelder
kinetische Evolutions-/Stationaritaetsgleichungen
aeussere Momenten-Matchingbedingungen
innere Capture-/Absorptionsbedingungen
gegebenenfalls Kollisions- und Reaktionsrandbedingungen.
```

Die Zahl dieser Freiheitsgrade kann nicht aus `S_count` allein abgeleitet
werden. Vor einer Solverfreigabe muss fuer den konkret gewaehlten kinetischen
Operator eine separate Phasenraum-, Momenten- und Randbedingungszaehlung
vorliegen.

## 15. Randbedingungen und Vorzeichenkonvention

### 15.1 Aussenrand

Eine moegliche Reservoirform ist

```text
n_s(R) = n_s,inf
sum_s q_s n_s,inf = 0
phi(R) = 0.
```

Die Quasineutralitaet ist Kompatibilitaet der Reservoirzusammensetzung und keine
zusaetzliche unabhaengige BVP-Bedingung. Alternativ koennen unabhaengige
elektrochemische Potentiale vorgegeben werden; dann duerfen nicht zugleich alle
Dichten als unabhaengige Randwerte gesetzt werden.

### 15.2 Innenrand Elektrostatik

Im lokalen Poisson-Branch

```text
4 pi r_m^2 epsilon_0 E(r_m+) = Q_m.
```

`Q_m` folgt aus `M_Q`; `E(r_m)` ist kein zusaetzlicher frei waehlbarer Wert.

### 15.3 Innenrand Capture

Mit nach aussen positivem `J_s`:

```text
-J_s(r_m) = C_s >= 0

dotN_s = 4 pi r_m^2 C_s
       = -4 pi r_m^2 J_s(r_m).
```

Mit dieser Konvention ist `J_s<0` ein Einwaertsfluss und `dotN_s>0` eine positive
Capture-Rate.

Im fixed-`u`-Branch ist zusaetzlich das Massenkompatibilitaetsresiduum

```text
sum_s m_s C_s + rho u = 0
```

am Matchingradius zu pruefen. Es ist keine weitere unabhaengige Randbedingung.

### 15.4 Matchingradius-Invarianz

`r_m` muss in einem Ueberlappungsgebiet liegen, in dem aeussere WDM-Beschreibung
und innere Matchingtheorie beide gelten. Nach konsistenter Transformation von
`Q_m`, `M_Q` und `K_s` duerfen physikalische Outputs nicht wesentlich von einer
Verschiebung von `r_m` innerhalb dieses Ueberlappungsgebiets abhaengen.

## 16. Ladungsbilanz, Roots und Stabilitaet

Die aeusseren Profile werden fuer jeden Wert von `Q_bullet` unter der
frozen-`Q_bullet`-Bedingung bestimmt. Formal definiert dies eine Familie

```text
Y_star(r;Q_bullet)
= {n_s,J_s,phi,E}_star(r;Q_bullet),
```

deren Mitglieder stationaere Loesungen des bedingten schnellen BVP sind. Die
Familie darf nur als quasi-stationaere Reduktion des Gesamtsystems verwendet
werden, wenn

```text
tau_relax << tau_Q.
```

`tau_relax` ist die langsamste relevante Relaxationszeit des aeusseren
Transport-/Screening-BVP. `tau_Q` ist die lokale Zeitskala der
Sinkladungsentwicklung; in Rootnaehe wird sie aus der linearisierten
Ladungsdynamik bestimmt. Ohne diese Trennung ist ein zeitabhaengiges gekoppeltes
Plasma-/Sinkmodell erforderlich.

Aus den positiven Capture-Raten folgt

```text
F_cap(Q_bullet)
= sum_s q_s dotN_s(Q_bullet).
```

Weitere Stroeme duerfen nur als einzeln auditierte Kanaele aufgenommen werden:

```text
F_tot(Q_bullet)
= F_cap(Q_bullet) + I_other(Q_bullet).
```

Die langsame reduzierte Ladungsdynamik waere

```text
dQ_bullet/dt = F_tot(Q_bullet).
```

Fuer `F_tot(Q_bullet)!=0` ist nur das bedingte aeussere BVP stationaer. Das
Gesamtsystem ist dann nicht stationaer, sondern bewegt sich entlang der
quasi-stationaeren Fortsetzungsfamilie. Erst bei

```text
F_tot(Q_eq)=0
```

kann die Ladungskomponente einen echten stationaeren Gleichgewichtskandidaten
bilden.

Bei nachgewiesener Zeitskalentrennung ist er lokal stabil, wenn

```text
F_tot'(Q_eq)<0
```

und das Vorzeichen auch unter Daten- und Modellunsicherheiten negativ bleibt.
Ohne Zeitskalentrennung muss die Stabilitaet des vollstaendigen zeitabhaengigen
gekoppelten Systems untersucht werden. Stage 3.95C berechnet weder `F_tot` noch
einen Root.

Fuer quantisierte Sinkladung `Q_bullet=N e` benoetigt ein spaeteres diskretes
Modell ganzzahlige Ladungsspruenge und eine generatorerhaltende Mastergleichung.
Ein kontinuierlicher Root ersetzt die stationaere diskrete Verteilung nicht.

## 17. Status der Closure-Interfaces

Die Statusbegriffe sind:

```text
MEASURED/DATA-DRIVEN  direkt durch gepruefte Daten verankert
DERIVABLE             ohne freie Koeffizienten aus vorhandener Closure ableitbar
MODEL-DEPENDENT       mathematische Form gewaehlt, physikalische Wahl nicht eindeutig
CURRENTLY UNAVAILABLE im Stage-3.95B-Audit nicht closure-komplett identifiziert
```

| Interface | Output | Status | Solverrolle |
|---|---|---|---|
| Bulkzustand | `T,P,rho,X,B,Omega,u,Phi_g` | `MEASURED/DATA-DRIVEN PARTIAL` | Pflichtinput; vollstaendige Profile offen |
| frozen Ladungszustaende | `S_s=0` | `SPECIFIED / PHYSICAL VALIDITY OPEN` | nur nach Zeitskalenpruefung |
| reaktive Ionisation | Speziesmenge, `z_s`, Populationen, `Nu_reac`, `R_r`, `S_s` | `CURRENTLY UNAVAILABLE` | Pflichtclosure im reaktiven Branch |
| Thermodynamik | `f,mu_s,H_st` | `DATA-DRIVEN PARTIAL / DERIVABLE IN LIMITED FE-O-SI DOMAIN` | volle Fe-Ni-Light-Closure offen |
| ionischer Transport | `L_ii` oder `Dtilde_ij` | `DATA-DRIVEN DIAGONAL VALIDATION ONLY / CURRENTLY UNAVAILABLE FULL MATRIX` | Pflichtclosure |
| elektronischer Transport | `L_ee,L_eT` | `DATA-DRIVEN PROJECTIONS / CURRENTLY UNAVAILABLE FULL OPERATOR` | Pflichtclosure |
| Elektron-Ion-Kreuztransport | `L_ei,L_ie` | `CURRENTLY UNAVAILABLE` | Nullsetzen nur als Toy-Branch |
| nichtisothermer Waerme-/Stoffblock | `L_hat,T,L_T,hat,L_TT,J_q` | `CURRENTLY UNAVAILABLE` | Pflichtclosure fuer `X_T!=0` |
| lokales Poisson | `phi,E` aus expliziter Ladung | `DERIVABLE ONCE MATERIAL MODULES CLOSE` | Branch P |
| nichtlokaler Response | `chi` und Randfunktionale | `MODEL-DEPENDENT / CURRENTLY UNAVAILABLE` | alternativer Branch NL |
| inneres Ladungsmatching | `Q_m=M_Q[...]` | `MODEL-DEPENDENT / CURRENTLY UNAVAILABLE` | Pflichtclosure |
| kinetisches Boundary-Lifting | `f_s(r_m,p)=B_s[y_s,m,...]` | `MODEL-DEPENDENT / CURRENTLY UNAVAILABLE` | Pflicht vor verteilungsabhaengigem `K_s` |
| Sink-Capture | `K_s`, alternativ `Ktilde_s`, gegebenenfalls `kappa_s` | `MODEL-DEPENDENT / CURRENTLY UNAVAILABLE` | Pflichtclosure |
| Capture-Raten | `dotN_s` | `DERIVABLE AFTER BVP` | Output |
| Ladungsstrom | `F_tot` | `DERIVABLE AFTER ALL CURRENT CHANNELS` | Output |
| quasi-stationaere Reduktion | `Y_star(r;Q_bullet)` und Zeitskalentrennung | `DERIVABLE AFTER DYNAMIC CLOSURE / CURRENTLY OPEN` | Pflicht vor frozen-Q-Fortsetzung |
| Transport-Nullraum/Koerzivitaet | `ker(L_full,diss)`, `lambda_min` oder `lambda_min^+` | `DERIVABLE AFTER TRANSPORT CLOSURE` | Pflicht-Operatorgate vor Solver |
| Root/Stabilitaet | `Q_eq`, `F_tot'(Q_eq)` | `DERIVABLE AFTER CLOSURE` | derzeit NO-GO |

Kein `CURRENTLY UNAVAILABLE`-Pflichtinterface darf durch einen stillen Default
ersetzt werden. Ein expliziter Hypothesenbranch muss als `MODEL-DEPENDENT`, mit
Domaene und Falsifikationskriterium, getrennt von einem datengetriebenen Branch
gefuehrt werden.

## 18. Analytischer Stage-3.95A-Regressionsvertrag

Die neue Architektur muss exakt auf Stage 3.95A zurueckfallen koennen. Dieser
Grenzfall ist ein Fixed-Background-/Tracer-Toy-Branch und kein physikalischer
Vollmischungsbranch.

Die Reduktion lautet:

```text
electron + one positive ion species
no volume reactions
fixed background / tracer branch
u = 0 fuer die geloesten Tracer
constant T
ideal chemical potentials
diagonal Nernst-Planck transport
no cross terms
X_T = 0
no induced screening
Q_m = Q_bullet
unshielded Coulomb potential
kappa_s -> infinity
n_s(r_m)=0
n_s(R)=n_s,inf.
```

Dann muss gelten

```text
U_s(r)
= -G M m_s/r + k_e z_s e^2 N/r

Q_bullet = N e

Delta = 1/r_m - 1/R

alpha_s
= [G M m_s - k_e z_s e^2 N]/(k_B T_s)

x_s = alpha_s Delta

dotN_s = A_s h(x_s)

A_s
= 4 pi D_s Phi_s n_s,inf / Delta

h(x)
= x/[1-exp(-x)].
```

Analytische Identitaeten:

```text
h(0)=1
h'(0)=1/2
h'(x)>0 fuer alle reellen x.
```

Fuer eine positive Ionenspezies mit Ladung `+Z e`:

```text
f(N)
= Z dotN_i(N) - dotN_e(N)

f'(N)<0.
```

Im Projekt-Default muss unabhaengig vom Rootfinder reproduziert werden:

```text
(D_e/D_i)_crit
= h(x_i)/h(x_e)
= 132.876774528.
```

Der Toy-Branch muss ausserdem die vorhandenen Regressionen reproduzieren:

```text
A34-ODE-Residual auf 400 logarithmischen Radialpunkten
radiale Flusserhaltung
exakte Randwerte
Regression gegen das alte falsche exponentielle Innenprofil
kontinuierliche Root-Sensitivitaeten
diskrete Generator-, Momenten-, Trunkierungs- und OU-Checks.
```

Ein Fehler in diesem Toy-Branch ist ein Architektur-/Implementierungsfail. Ein
PASS uebertraegt das Toy-Monotonietheorem nicht auf die reale WDM-Closure; dort
sind globale Monotonie, Rootexistenz und Eindeutigkeit weiterhin offen.

Die gegenwaertigen `42/42` bestehenden Regressionstests sind nur ein
Rueckwaertskompatibilitaetscheck:

```text
Stage 3.94:  14/14
Stage 3.95A: 16/16
F8a:         12/12
```

Sie sind keine numerische Validierung von Stage 3.95C, da Stage 3.95C selbst
keinen Solver implementiert.

## 19. Architektur-Gate vor jeder Solverfreigabe

Ein numerischer Solver darf erst angelegt werden, wenn alle folgenden Punkte
fuer mindestens einen klar benannten physikalischen Branch bestanden sind.

### G1 – Dependency- und Interface-Vollstaendigkeit

```text
jeder Pfeil besitzt ein benanntes Interface
jeder Interface-Input und -Output besitzt Einheit und Konvention
keine lineare Scheinableitung mu_s->L_st oder n_s->kappa_s
verteilungsabhaengiges K_s besitzt B_s:y_s,m->f_s oder wird durch Ktilde_s ersetzt
keine zyklische Abhaengigkeit ohne definiertes gekoppeltes BVP.
```

### G2 – Freiheitsgrad- und Referenzrahmenkonsistenz

```text
S_count und Ladungszustaende explizit
S_count-1 unabhaengige Diffusionsmoden
baryzentrischer oder transformierter Rahmen dokumentiert
Nullraum und Ruecktransformation dokumentiert
Bulk-Massenfluss mit den Capture-Raten kompatibel.
```

### G3 – Gleichungs- und Randwertzaehlung

```text
Anzahl unabhaengiger Felder = Anzahl unabhaengiger Gleichungen
Gesamtordnung = Anzahl unabhaengiger Randbedingungen
fixed-u-Minimalbranch: 2 S_count+1 / 2 S_count+1 / 2 S_count+1
S_count Capture-Raten bei festem u erfuellen das Massenkompatibilitaetsresiduum
volle J_s-Darstellung als DAE markiert, algebraische Nebenbedingung nicht als BVP-Ordnung gezaehlt
keine doppelte Vorgabe von n_s und mu_s
keine doppelte Vorgabe von phi und E am selben Rand
keine unabhaengige Vorgabe von Q_m neben M_Q
expliziter kinetischer Boundary Layer besitzt eine eigene Feld-/Randwertzaehlung.
```

### G4 – Thermodynamische Konsistenz

```text
gemeinsames Potential oder dokumentierte Nichtgleichgewichtsclosure
Hesse-Symmetrie im Gleichgewichtsbranch
C_th^T H C_th positiv semidefinit auf dem zulaessigen Unterraum
thermodynamische Nebenbedingungen und Potentialwahl dokumentiert
keine unkontrollierte P-T-X-Extrapolation.
```

### G5 – Transportkonsistenz

```text
Onsager-Casimir am vollen L statt pauschaler Symmetrie
nichtnegative dissipative Entropieproduktion
isothermer Branch setzt X_T=0 explizit
nichtisothermer Branch fuehrt J_q, L_hat,T, L_T,hat und L_TT gemeinsam
keine self-D->mutual-D-Umdeutung
keine sigma_e->freies D_e-Umdeutung
Magnetisierungs-/Rotationsbranch geprueft
Nullraum des vollen dissipativen Operators entspricht nur erwarteten Erhaltungsmoden
restringierte Koerzivitaet nach Projektion geprueft
Koerzivitaet nicht als automatischer Nachweis voller PDE-Parabolizitaet ausgegeben.
```

### G6 – Elektrostatik-Branch-Exklusivitaet

```text
lokaler oder nichtlokaler Branch eindeutig gewaehlt
Freiheitsgradpartition dokumentiert
kein doppeltes Screening
Gauss- und Ladungsbilanz geschlossen.
```

### G7 – Inneres Matching und Sink

```text
M_Q physikalisch definiert oder expliziter Hypothesenbranch
B_s plus K_s oder alternativ Ktilde_s physikalisch definiert
kappa_s nur als hergeleiteter lokaler linearer Spezialfall
0<=P_cap<=1 fuer kinetische Capture-Wahrscheinlichkeiten
Matchingradius-Invarianz pruefbar
Energie-Matching getrennt dokumentiert.
```

### G8 – Stage-3.95A-Regression

```text
analytische Reduktion dokumentiert
alle vorhandenen 3.95A/A34-Regressionen unveraendert PASS
Tracer-/Toy-Charakter des u=0-Grenzfalls explizit
42 bestehende Tests nicht als numerische 3.95C-Validierung ausgeben.
```

### G9 – Daten- und Hypothesenprovenienz

```text
jeder numerische Koeffizient besitzt Quelle oder Hypothesenlabel
Einheit, Unsicherheit, Kovarianz und Gueltigkeitsdomaene dokumentiert
Interpolation dokumentiert
Extrapolation standardmaessig verboten
Sensitivitaetsbranch nicht als physikalischer Bestwert ausgegeben.
```

### G10 – Solverfreigabeentscheidung

```text
G1 bis G9 PASS -> Solverprototyp darf separat geplant werden.
mindestens ein Pflichtgate OPEN oder FAIL -> Solver NO-GO.
```

Aktueller Gate-Stand:

| Gate | Status Stage 3.95C |
|---|---|
| G1 Dependency-/Interface-Topologie | `PASS AS SPECIFICATION` |
| G2 Freiheitsgrade/Referenzrahmen | `PASS AS SPECIFICATION` |
| G3 lokale Momenten-BVP-Gleichungs-/BC-Zaehlung | `PASS AS SPECIFICATION` |
| G4 vollstaendige Thermodynamikclosure | `OPEN` |
| G5 vollstaendige Transportclosure | `OPEN` |
| G6 projektspezifische Screeningpartition | `OPEN` |
| G7 `M_Q`, `B_s` und `K_s/Ktilde_s/kappa_s` | `OPEN` |
| G8 analytischer Regressionsvertrag | `SPECIFIED / NOT IMPLEMENTED IN 3.95C` |
| G9 vollstaendige Daten-/Hypothesenprovenienz | `OPEN` |
| G10 Solverfreigabe | `NO-GO` |

Das Architektur-Definitionsgate bewertet ausschliesslich, ob die mathematischen
Schnittstellen, Freiheitsgrade, Branches und No-Go-Regeln vollstaendig benannt
und intern konsistent sind. Es ist nicht identisch mit G10. Fuer den aktuellen
Post-Edit-Stand gilt:

```text
Stage 3.95C Architecture Definition Gate: PASS AS SPECIFICATION
Physical Closure Completeness:           OPEN
Solver Release Gate:                     NOT PASSED
Real Q_eq Implementation:                NO-GO
Experimental BH Evidence:                NONE
```

## 20. Harte No-Go- und Falsifikationskriterien

### 20.1 No-Go vor Solverbau

```text
kein mu_s -> L_st ohne dynamische Daten/Closure
kein n_s -> kappa_s ohne Sinkmikrophysik
kein Q_m = Q_bullet unter Screening ohne Matchingnachweis
kein doppeltes Screening
keine Inversion der baryzentrischen Nullmode
keine pauschale L_symmetrie bei B/Omega != 0
kein nichtisothermer L_sT-Term ohne reziproken Waermeflussblock
keine Gleichsetzung von Entropie-PSD und voller PDE-Parabolizitaet
kein u=0 plus positive Vollmischungs-Massenakkretion
keine nichtganzzahlige Zbar-Sprungweite in diskreter Ladungskette
keine S_count unabhaengigen Capture-BCs neben festem u ohne Massenkompatibilitaet
keine falsche Gleichungs-/Feld-/BC-Zaehlung
keine stillen Defaults fuer offene Pflichtinterfaces
keine Extrapolation ausserhalb dokumentierter Domaene
keine numerische Q_eq-Ausgabe aus unvollstaendiger Closure.
```

### 20.2 Falsifikationskriterien nach spaeterer Closure

Erst fuer einen vollstaendig definierten und numerisch validierten Branch waeren
physikalische Kriterien anwendbar:

```text
kein Root im vollstaendig abgedeckten physikalischen Q-Bereich
alle Roots dynamisch instabil
Felder oder Potentiale verletzen die verwendete Response-/Transporttheorie
vernachlaessigte Reaktions-, Entladungs-, Magnet- oder QED-Kanaele sind relevant
Akkretions-, Strom- oder Heizleistung verletzt vorab gesetzte Bounds.
```

Interpretationsregel:

```text
fehlende Closure                         -> OPEN / NO-GO
Architektur- oder Residualfail           -> MODEL/SOLVER FAIL
kein Root in zu kleiner Datendomaene     -> OPEN
stabiler Root eines geschlossenen Modells -> CLOSURE PASS, kein BH-Nachweis.
```

## 21. Vorgeschlagene spaetere Dateistruktur

In Stage 3.95C wird nur diese Architekturspezifikation angelegt. Nach einem
separaten Auftrag koennte die maschinenlesbare Gate-Struktur folgen:

```text
STAGE3_95C_A35_WDM_THEORETICAL_CLOSURE_ARCHITECTURE.md

research/
    stage3_95c_a35_closure_interfaces.yaml
    stage3_95c_a35_architecture_gate.yaml
```

Erst nach bestandenem Architektur-Gate duerfte ein spaeterer, separat
freizugebender Implementierungsstage folgende Modulgrenzen verwenden:

```text
stage3_a35_wdm/
    contracts.py
    species_and_ionization.py
    thermodynamics.py
    transport_frame.py
    electron_transport.py
    ion_transport.py
    electrostatics_local.py
    electrostatics_nonlocal.py
    inner_charge_matching.py
    sink_capture.py
    stationary_bvp.py
    charge_dynamics.py
    diagnostics.py

tests/
    test_stage3_a35_frame_and_dof.py
    test_stage3_a35_onsager_casimir.py
    test_stage3_a35_thermodynamic_stability.py
    test_stage3_a35_electrostatic_branch_exclusivity.py
    test_stage3_a35_matching_and_sink_contracts.py
    test_stage3_a35_conservation.py
    test_stage3_a35_stage3_95a_regression.py
```

Die Dateinamen sind ein Architekturvorschlag, keine Implementierungsfreigabe.

## 22. Schlussstatus

```text
Dependency-Graph statt linearer Pipeline:
SPECIFIED.

Thermodynamik / Transport / Ionisation / Elektrostatik / Sink getrennt:
SPECIFIED.

Onsager-Casimir mit B- und Omega-Umkehr:
SPECIFIED.

baryzentrischer Referenzrahmen und S_count-1 Diffusionsmoden:
SPECIFIED.

lokaler Poisson- und nichtlokaler Response-Branch:
STRICTLY SEPARATED.

Q_bullet -> Q_m und (Q_bullet,state) -> K_s/kappa_s:
SEPARATE THEORETICAL CLOSURES / CURRENTLY UNAVAILABLE.

Unabhaengige Felder, Gleichungen und Randbedingungen im lokalen fixed-u-Minimalbranch:
2 S_count + 1 / 2 S_count + 1 / 2 S_count + 1.

Volle J_s-DAE-Darstellung:
2 S_count + 2 Variablen/Gleichungen inklusive einer algebraischen baryzentrischen Nebenbedingung,
aber weiterhin nur 2 S_count + 1 unabhaengige BVP-Randbedingungen.

Selbstkonsistenter u-Branch mit einer Bulk-Dynamikclosure:
2 S_count + 2 / 2 S_count + 2 / 2 S_count + 2.

Stage-3.95A-Regressionsvertrag:
ANALYTICALLY SPECIFIED / NOT IMPLEMENTED IN 3.95C.

Stage 3.95C mathematische Architektur:
SPECIFIED.

Stage 3.95C Architektur-Definitionsgate:
PASS AS SPECIFICATION.

Nichtisothermer Waerme-/Stoffblock:
SPECIFIED AS INTERFACE / PHYSICAL CLOSURE OPEN.

Transport-Nullraum / restringierte Koerzivitaet:
SPECIFIED AS OPERATOR GATE / DERIVABLE AFTER CLOSURE.

Architektur-Gate fuer realen Solver:
NOT PASSED.

Implementierung reales Q_eq:
NO-GO.

experimenteller BH-Nachweis:
NONE.
```
