# Stage 3.69A – Literatur-Crosscheck 2024 und Ladungsregulation

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** LITERATURE CONFLICT IDENTIFIED / OPEN

## 1. Warum dieser Crosscheck wichtig ist

Der Quantum/Wave-Capture-Block ist kein rein projektspezifisches Problem. Eine 2024 publizierte Arbeit von Abraham Loeb behandelt explizit eine moegliche quantenmechanische Unterdrueckung der Akkretion kleiner PBHs in dichten astrophysikalischen Umgebungen, einschliesslich Planeten- und Sterninneren.

Loeb argumentiert, dass bei sehr kleinen Ereignishorizonten die kontinuierliche hydrodynamische Beschreibung unzureichend sein kann und fuer zuverlaessige Raten Elektronen- und Protonen-Wellenfunktionen auf dem BH-Hintergrund berechnet werden sollten.

Direkt danach erschien jedoch ein Kommentar von James M. Cline (McGill / CERN Theory), der die starke Schlussfolgerung einer unterdrueckten **Gesamt-Akkretionsrate** kritisiert. Cline argumentiert, dass eine endliche Einzelatom-/Elektron-Verzoegerung nicht automatisch die hydrodynamische Rate pro Atom bzw. eines kontinuierlichen Stroms unterdrueckt.

Daraus folgt fuer dieses Projekt:

```text
Loeb-Quantum-Suppression darf nicht ungeprueft als Mdot-Suppressionsfaktor uebernommen werden.
Klassische Bondi/Michel-Hydrodynamik darf aber ebenfalls nicht ungeprueft bis zum Horizont extrapoliert werden.
```

Der Konflikt ist genau eine Motivation fuer Stage 3.69A-1.

## 2. Relevanter Massenbereich

Loeb diskutiert insbesondere PBHs im Bereich grob

```text
6e14 ... 4e19 g
= 6e11 ... 4e16 kg.
```

Der kleine Erd-H0-Branch liegt teilweise darunter bzw. am unteren Rand dieser Skala, z. B.

```text
M_BH ~ 1e11 ... 5e11 kg
     ~ 1e14 ... 5e14 g.
```

Eine quantitative Extrapolation von Loebs konkreten Suppressionsformeln in den gesamten Projektbereich wird deshalb **nicht** als validiertes Ergebnis gewertet.

## 3. Warum der Einzelteilchen-Ansatz trotzdem relevant bleibt

Doran et al. zeigen fuer freie massive Fermionen, dass die Schwarzschild-Dirac-Absorption vom dimensionslosen Parameter

```text
alpha_g = G M_BH m/(hbar c)
```

abhaengt. Der Stage-3.69A-Regimecheck findet bei `M_BH=1e11 kg`:

```text
alpha_e   = 1.923e-4
alpha_p   = 3.531e-1
alpha_Fe  = 1.961e1
```

und der Protonen-Uebergang `alpha_p=1` liegt bei

```text
M_BH ~= 2.832e11 kg.
```

Damit ist der Projektbereich fuer Protonen gerade kein reiner asymptotischer Grenzfall.

## 4. Selektive Capture und elektrische Ladung

Wenn Protonen, Elektronen oder Ionen unterschiedliche Capture-Wahrscheinlichkeiten besitzen, kann der BH eine kleine Nettoladung aufbauen. Bereits eine sehr kleine Ladung kann die weitere Capture stark regulieren, weil die Coulombkraft fuer Elementarladungen im Vergleich zur Gravitation sehr gross ist.

Fuer `M_BH=1e11 kg` folgt aus dem einfachen Kraftgleichgewicht

```text
k_e Q e / r^2 = G M_BH m / r^2
```

fuer Protonen:

```text
Q_grav=p ~= 7.75e-18 C ~= 48.4 e.
```

Fuer Elektronen liegt die entsprechende Schwelle nur bei

```text
Q_grav=e ~= 4.22e-21 C ~= 0.026 e.
```

Das bedeutet: Bereits **eine einzige positive Elementarladung** erzeugt auf ein Elektron eine elektrische Anziehung, die dessen BH-Gravitationskraft bei diesem Massenpunkt deutlich uebersteigt. Einige Dutzend positive Elementarladungen koennen die Protonen-Capture stark rueckkoppeln.

Eine publizierte stationaere Plasmaabschaetzung fuer gleiche Elektronen-/Protonentemperaturen liefert schematisch

```text
Q_eq = 2 pi epsilon_0 G (m_p-m_e) M_BH / e.
```

Fuer `M_BH=1e11 kg` ergibt das nur etwa

```text
Q_eq ~= 3.87e-18 C ~= 24.2 e.
```

Diese Zahl ist **kein Erdzentrum-Ergebnis**; die zugrunde liegende stationaere Plasmaannahme unterscheidet sich stark vom dichten Fe/Ni-Erdkern. Sie zeigt aber die extreme Empfindlichkeit der speziesselektiven Capture gegen selbst winzige Nettoladungen.

Zum Vergleich liegt die extremale Reissner-Nordstroem-Ladung fuer `1e11 kg` bei Groessenordnung

```text
Q_ext ~= 8.62 C.
```

Damit ist `Q_eq/Q_ext ~ 4.5e-19`: Die fuer Capture-Regulation relevante Ladung kann elektromagnetisch wichtig sein, waehrend ihre Rueckwirkung auf die Schwarzschild-Geometrie vernachlaessigbar klein bleibt. Ein erster Solver darf daher zunaechst Schwarzschild + Test-EM-Potential verwenden, bevor volle Einstein-Maxwell-Rueckkopplung noetig wird.

## 5. Konsequenz fuer Stage 3.69A-1

Der naechste Solver darf nicht nur eine neutrale freie Protonen- oder Elektronenwelle einzeln behandeln. Mindestanforderung:

```text
1. Schwarzschild-Dirac-Absorption fuer e-, p und relevante Ionen/Kerne.
2. lokale Energie-/Geschwindigkeitsverteilungen aus dem kinetischen Uebergang.
3. dynamische Ladungsvariable Q(t).
4. Coulomb-Potential im Teilchen-Hamiltonoperator / in der Dirac-Gleichung.
5. Ambipolare bzw. quasineutrale Rueckkopplung.
6. Debye-/Screening-Skala im lokalen Medium.
7. Vergleich der Einzelteilchen-Verzoegerung mit dem kollektiven Nachstrom.
8. erst danach Netto-Mdot.
```

Formal muss die Capture-Closure erweitert werden zu

```text
Mdot_BH = sum_i Integral dE [Mdot_i,supply(E,Q,t) * Gamma_i(E,Q,t)]

dQ/dt = sum_i q_i Ndot_i,capture.
```

## 6. Status

```text
Starke pauschale Quantum-Suppression: NICHT etabliert; in der Literatur bestritten.
Reine klassische Horizon-Extrapolation: ebenfalls nicht ausreichend begruendet.
Speziesabhaengige Dirac-Capture: erforderlich.
Ladungs-/Ambipolar-Regulation: neu als Pflichtblock identifiziert.
Netto-H0-Akkretionsrate: OPEN.
```

## Referenzen

- A. Loeb (2024), *Quantum-mechanical Suppression of Accretion by Primordial Black Holes*, Astrophysical Journal Letters 975 L15, arXiv:2409.09081.
- J. M. Cline (2024), *Comment on "Quantum-Mechanical Suppression of Gas Accretion by Primordial Black Holes"*, arXiv:2409.12989; CERN Document Server record 2912898.
- C. Doran, A. Lasenby, S. Dolan, I. Hinder (2005), *Fermion absorption cross section of a Schwarzschild black hole*, Phys. Rev. D 71, 124020, arXiv:gr-qc/0503019.
- M. Zajacek et al. (2018), *On the charge of the Galactic centre black hole*, MNRAS 480, 4408–4423.
- K. Nakao et al. (2025), *Electrification of a nonrotating black hole*, Phys. Rev. D 112, 064033.
