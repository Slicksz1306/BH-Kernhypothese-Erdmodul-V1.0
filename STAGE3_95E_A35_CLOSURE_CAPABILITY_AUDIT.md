# Stage 3.95E / A35 – Closure Capability Audit

**Datum:** 30.08.2026  
**Status:** `CAPABILITY AUDIT PASS AS SPECIFICATION` / `PHYSICAL CLOSURE OPEN` / `SOLVER RELEASE NOT PASSED` / `REAL Q_eq NO-GO`

## 1. Zweck

Stage 3.95E beantwortet nicht, **welchen Wert** die Gleichgewichtsladung `Q_eq` hat. Der Stage prüft stattdessen, ob die in Stage 3.95C spezifizierten physikalischen Schnittstellen inzwischen so geschlossen sind, dass ein realer numerischer A35-Solver wissenschaftlich freigegeben werden darf.

Es werden keine neuen Proxy-Koeffizienten eingeführt. Keine fehlende Transport-, Ionisations-, Screening-, Matching- oder Capture-Closure wird durch eine bequem verfügbare Ersatzgröße ersetzt.

## 2. Statusvokabular

```text
DATA-CLOSED
    Direktes, zielbereichstaugliches Closure-Dataset liegt vor und ist
    hinsichtlich Domain, Einheiten, Provenienz und Unsicherheit auditiert.

DERIVABLE
    Die benötigte Größe kann aus einem gemeinsamen belastbaren Ausgangsmodell
    abgeleitet werden. "DERIVABLE" allein bedeutet nicht automatisch, dass der
    vollständige Zielbereich abgedeckt ist.

THEORY-CLOSED
    Die benötigte Beziehung ist auf Gleichungsebene theoretisch geschlossen;
    ihre konkrete Anwendung kann weiterhin Randbedingungen oder Materialdaten
    benötigen.

MODEL-DEPENDENT
    Eine explizite Modellwahl ist notwendig und derzeit nicht hinreichend
    ausgewählt/validiert.

SENSITIVITY-ONLY
    Nur als kontrollierter Sensitivitätsbranch zulässig; keine physikalische
    Closure des Realmodells.

CURRENTLY UNAVAILABLE
    Für den Zielbereich fehlt gegenwärtig die notwendige Closure-Information.
```

## 3. Release-Regel

Ein realer `Q_eq`-Solver darf erst freigegeben werden, wenn jede für den gewählten Branch notwendige Schnittstelle

1. explizit geschlossen ist,
2. im tatsächlichen Fe-Ni-Light-WDM-Zielbereich gültig ist,
3. ihre Unsicherheit und Extrapolation dokumentiert,
4. mit den anderen Closures thermodynamisch und konservativ kompatibel ist,
5. die konkrete BVP/PDE-Wohlgestelltheit besteht.

`MODEL-DEPENDENT`, `SENSITIVITY-ONLY` oder `CURRENTLY UNAVAILABLE` zählen im gegenwärtigen Zustand **nicht** als Solverfreigabe. Eine `DERIVABLE`-Größe mit nur teilweiser Source-Domain-Abdeckung zählt ebenfalls nicht als vollständige Ziel-Closure.

## 4. Capability-Matrix – Ergebnis

Die maschinenlesbare Matrix liegt unter

`research/stage3_95e_a35_closure_capability_matrix.csv`.

Sie enthält 16 auditierten Schnittstellenblöcke. Im aktuellen Stand ist nur die lokale Poisson-Feldgleichung auf Gleichungsebene als `THEORY-CLOSED` und nicht selbst blockierend eingestuft. Die übrigen 15 Blöcke benötigen Daten, eine konkrete validierte Modellwahl, Domain-Nachweis oder nachgelagerte mathematische Prüfung.

```text
Interfaces auditiert:               16
aktuell nicht selbst blockierend:    1
aktuell blockierend:                15
Solver Release Gate:                NOT PASSED
Real Q_eq Implementation:           NO-GO
Physical Closure:                   OPEN
Experimental BH Evidence:           NONE
```

Die Zahl `15` ist kein physikalischer Messwert. Sie ist nur der aktuelle Projekt-Bookkeeping-Stand der in Stage 3.95C definierten Pflicht-/Branch-Schnittstellen.

## 5. Harte Blocker

### A35-ION – Ionisation / Ladungszustände

```text
current_class: CURRENTLY UNAVAILABLE
```

Die mathematische Schnittstelle ist definiert, aber zielbereichstaugliche Fe-Ni-Light-WDM-Populationen mit aufgelösten ganzzahligen Ladungszuständen fehlen. Ein mittleres `Zbar` darf weiterhin nicht als nichtganzzahlige Sprungweite einer diskreten Capture-Mastergleichung benutzt werden.

### A35-LST – multikomponentiger Ionen-Transport

```text
current_class: CURRENTLY UNAVAILABLE
```

Selbstdiffusion bleibt `VALIDATION_ONLY`. Sie bestimmt weder eine vollständige Mutual-Diffusion-Struktur noch die projizierte Onsager-/Maxwell-Stefan-Matrix `L_st`.

### A35-THERMO – Thermodynamik

```text
current_class: DERIVABLE
current_domain: PARTIAL_DOMAIN_ONLY
```

Begrenzte Fe-O-Si-Derivate können innerhalb der jeweiligen Source-Domain abgeleitet werden. Das schließt keine vollständige Fe-Ni-Light-Hesse-Matrix über den A35-Zielbereich. Daher bleibt die Thermodynamik solverblockierend.

### A35-ELECTRON – Elektronentransport

```text
current_class: MODEL-DEPENDENT
```

Leitfähigkeits- und Kubo-Greenwood-Daten sind wertvolle Methoden-/Validierungsanker. Sie dürfen aber nicht als freies Elektronendiffusionskoeffizient `D_e` oder als vollständiger elektronischer Flussoperator eingesetzt werden.

### A35-MQ – inneres Ladungsmatching

```text
current_class: MODEL-DEPENDENT
```

Unter Screening gilt weiterhin

```text
Q_bullet != Q_m
```

solange kein expliziter, validierter Matching-Operator `M_Q` geschlossen ist. Dieser Block ist primär eine theoretische Closure-Aufgabe und nicht lediglich ein fehlender Tabellenwert.

### A35-K / A35-BS – Capture und kinetisches Lifting

```text
A35-K:  MODEL-DEPENDENT
A35-BS: MODEL-DEPENDENT, conditional
```

Ein verteilungsabhängiger Capture-Operator `K_s[f_s]` ist nur zulässig, wenn das Lifting `B_s:y_s,m -> f_s(r_m,p)` geschlossen ist. Alternativ darf ein direkt geschlossener Momentenoperator `Ktilde_s[y_s,m]` verwendet werden. Keine der beiden Capture-Routen ist derzeit physikalisch geschlossen.

## 6. Weitere Release-Blocker

- vollständiger Bulkzustand/Komposition/Flow über den Zielbereich,
- Reaktionsraten oder ein validierter Frozen-Charge-State-Zeitmaßstab,
- Material-/Screeningresponse zusätzlich zur Poisson-Gleichung,
- kompatible äußere Randbedingungen,
- Validierung des isothermen Branches oder vollständiger reziproker Wärmeflussblock,
- Audit aller zusätzlichen Ladungsströme `I_other`,
- konkrete Coercivity/Principal-Symbol/BVP-Wohlgestelltheit,
- gemeinsame Domain-/Unsicherheitsfortpflanzung bis zu Root und Stabilität.

## 7. Anti-Proxy-Gates

Die begleitenden Regressionstests verhindern explizit einige wissenschaftlich unzulässige Status-Promotionen:

```text
self diffusion -> DATA-CLOSED L_st:         REJECT
conductivity -> DATA-CLOSED electron op.:   REJECT
unclosed Q_bullet -> Q_m -> THEORY-CLOSED:  REJECT
unclosed capture K -> THEORY-CLOSED:        REJECT
```

Damit wird nicht bewiesen, dass die Matrix vollständig oder endgültig ist. Es wird nur verhindert, dass bekannte Stage-3.95B/C-Grenzen stillschweigend wieder aufgeweicht werden.

## 8. Priorisierung der nächsten Closure-Arbeit

Die wissenschaftlich höchste externe Datenpriorität bleibt:

```text
species-resolved Fe-Ni-Light AIMD / first-principles trajectories
at liquid-core P-T-X
```

weil solche Trajektorien am ehesten direkten Fortschritt für multikomponentigen Ionen-Transport und dessen Unsicherheit ermöglichen.

Parallel, aber getrennt davon, müssen die theoretischen inneren Interfaces `M_Q` und `K_s/Ktilde_s` geschlossen werden. Mehr äußere Materialdaten allein lösen diese beiden BH/WDM-Randprobleme nicht.

## 9. Stop-Regel

Bis die blockierenden Pflichtinterfaces geschlossen und validiert sind:

```text
Stage 3.95C Architecture:       PASS AS SPECIFICATION
Stage 3.95E Capability Audit:   PASS AS SPECIFICATION
Physical Closure:               OPEN
Solver Release:                 NOT PASSED
Real Q_eq Solver:               NO-GO
Experimental BH Evidence:       NONE
```

Ein numerisch konvergierender Root mit frei gewählten Ersatzkoeffizienten wäre in diesem Zustand nur ein neuer Toy-/Sensitivity-Branch und darf nicht als physikalisches `Q_eq` ausgewiesen werden.
