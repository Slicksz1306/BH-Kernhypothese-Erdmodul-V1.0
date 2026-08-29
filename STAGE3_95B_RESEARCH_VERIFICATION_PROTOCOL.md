# Stage 3.95B – Research Verification Protocol

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Status:** METHODIK / ORCHESTRATION  
**Stand:** 29.08.2026

## 0. Aussagegrenze

Stage 3.95B ist **kein neues physikalisches Ergebnis** und kein experimenteller Nachweis. Der Block definiert eine härtere Forschungs-, Verifikations- und Agentenpipeline für die bereits offenen Gates F12, A34/A35, H0 und Formation/Delivery.

Grundregel:

```text
Solver PASS != physikalische Closure != experimentelle Evidenz.
```

## 1. Verbindlicher Forschungsstack

```text
1. Deep Research / Quellenmatrix
2. GPT-5.6 Sol / Herleitung, Kritik, Gegenbeispiele
3. Codex / unabhängige Solver, Tests, Regressionen
4. Wolfram / unabhängiger CAS-/Numerikcheck
5. Adversarial Verifier / gezielte Fehlersuche
6. Lean / selektive formale Zertifizierung
7. Scientific Gate / Claim-Level + Rubric
```

Lean wird nur für exakt formulierbare mathematische Aussagen verwendet. Ein formal bewiesener Satz unter Annahmen beweist nicht die physikalische Wahrheit dieser Annahmen.

## 2. Problemzerlegung im FrontierScience-Stil

Jedes offene Forschungsproblem wird in klar definierte, verifizierbare Subtasks zerlegt. Jeder Subtask muss enthalten:

- explizite Variablen, Einheiten und Annahmen,
- definierte Inputs und Outputs,
- objektive Pass/Fail-Kriterien,
- Zwischenchecks statt nur Endergebnis,
- mindestens einen unabhängigen Review-Pfad.

Die Stage-3.95B-Gates erhalten eine 10-Punkte-Rubrik. Projektinterne Schwellen:

```text
0..6  = FAIL / unzureichend
7..8  = PARTIAL
9     = CONDITIONAL PASS
10    = SOLVER/ANALYTICAL GATE PASS
```

Auch 10/10 ist kein experimenteller Nachweis.

## 3. Prover–Verifier-Prinzip

Ein Ergebnis wird nicht von derselben Instanz gleichzeitig vorgeschlagen, begründet und endgültig akzeptiert.

```text
Problemdefinition
    |
    +--> Prover / Sol
    |
    +--> Codex Solver
              |
              v
           Resultat
              |
      +-------+--------+
      |                |
      v                v
  Wolfram Check   Adversarial Verifier
      |                |
      +-------+--------+
              |
              v
         ggf. Lean
              |
              v
         Scientific Gate
```

Der Verifier erhält bevorzugt Problemdefinition, Annahmen, Daten und behauptetes Resultat, nicht nur die Argumentationskette des Provers.

## 4. Unabhängige Konsistenzbedingungen

Solver-Übereinstimmung allein reicht nicht. Für jedes Gate sind – soweit anwendbar – zusätzlich zu prüfen:

- Dimensionsanalyse,
- analytische Grenzfälle,
- Erhaltungssätze,
- Monotonien,
- Symmetrien,
- bekannte Spezialfälle,
- asymptotische Limits,
- Residuen der Differentialgleichungen,
- Fluss-/Bilanzkonstanz,
- Parameter- und Gitterkonvergenz.

Numerische Konvergenz wird explizit verfolgt, z. B.

```text
N, 2N, 4N, 8N, ...
E_N = |Q_N - Q_2N|
p ~ log2(|Q_N-Q_2N| / |Q_2N-Q_4N|)
```

`solver.success == True` genügt nicht als Konvergenznachweis.

## 5. Gate-spezifische Anwendung

### F12

Pflichtblöcke:

- aktuelle PBH-/Primordial-Constraints,
- echtes `P_zeta(k)` statt Proxy,
- Nicht-Gaußförmigkeit mit klar definierter Konvention,
- Parameter-Sweeps und Sensitivität,
- unabhängiger numerischer/CAS-Check,
- Abgleich mit Formation/Delivery.

### A34/A35

Pflichtblöcke:

- multikomponentige Onsager-/Maxwell-Stefan-Mobilitätsmatrix,
- thermodynamische Ableitungen chemischer Potentiale,
- Screening,
- Sink-Boundary-Matching,
- unabhängige Lösung der Transportgleichungen,
- Grenzfälle `Q->0`, `T_e=T_i`, `D_e=D_i`, `Z=1`,
- diskrete/continuum Crosschecks bei kleinen Ladungszahlen.

Das Stage-3.95A-Toy-Theorem bleibt nur Toy-Modell-Resultat; reales `Q_eq` bleibt OPEN.

### H0

Pflichtblöcke:

- PREM-basierter Referenzzustand,
- massenkompensierte Perturbationen,
- `delta rho -> delta Vp/delta Vs -> delta t`-Closure,
- Messfehler/Sensitivität/Parameterdegenerationen,
- unabhängige Laufzeit-/Normalmodenrechnung,
- Suche nach einer **eindeutigen positiven H0-Signatur**.

### Formation/Delivery

Pflichtblöcke:

- Herkunft und Phase-Space-Dichte getrennt von lokaler Capture-Dynamik,
- Population-weighted statt nur konditionale Einzelszenarien,
- robuste Unsicherheitspropagation,
- keine Gleichsetzung von `candidate region` und astrophysikalischer Wahrscheinlichkeit.

## 6. Discovery Cascade

Jedes bestätigte Resultat wird als Input für Folgefragen verwendet:

```text
Hypothese
  -> quantitative Evaluation
  -> physikalisches Observable / Constraint
  -> abhängige Gates
  -> neue Hypothesen
```

Beispiel:

```text
A35 real Q_eq
  -> effektive Capture-Rate
  -> Wärme / Akkretion
  -> H+ oder H0-Folgen
  -> beobachtbare Constraints
```

## 7. Micro-Inspiration statt Kontextdump

Für Hypothesengenerierung werden kleine, sauber attribuierte Quellfragmente bevorzugt:

```text
Paper A -> relevanter Absatz
Paper B -> relevantes Constraint
PREM    -> relevanter Parameter
SK      -> relevanter Grenzwert
```

Erst danach werden Resultate zusammengeführt. Ziel: Kontextkontamination und unbemerkte Quellenvermischung reduzieren.

## 8. Capability Graph

Findings werden als `provides` / `requires` modelliert. Dadurch sollen querliegende Abhängigkeiten automatisch sichtbar werden, z. B.:

```text
A35_REAL_QEQ
requires:
  - mobility_matrix
  - chemical_potential_derivatives
  - screening
  - sink_boundary
provides:
  - charge_equilibrium
  - effective_capture_rate
```

Siehe `research/stage3_95b_capability_graph.yaml`.

## 9. Structured Result Contracts

Subagenten liefern keine unstrukturierte Freitextmeldung als alleinige Wahrheit. Mindestens zu liefern:

```text
task
searched
sources
equations_checked
tests_run
failures
result
confidence
limitations
```

Siehe `agent/stage3_95b_result_contract.schema.json`.

## 10. Quellen-/Methodik-Basis für Stage 3.95B

### Übernommen

1. **FrontierScience** – rubric-basierte, mehrstufig verifizierte Research-Subtasks; unabhängige Reviews und Bewertung von Zwischenrechnungen.
2. **Formal Mathematics Statement Curriculum Learning** – Lean/lean-gym, Expert Iteration, Zerlegung schwerer Beweise in ein Curriculum einfacherer Statements.
3. **Single-minus gluon tree amplitudes are nonzero** – Conjecture -> Proof -> unabhängige Konsistenzidentitäten/Recursion Checks.
4. **Planar Point Sets with Many Unit Distances** – automatisierte Lösung -> AI-Grading -> interne und externe mathematische Prüfung; strikte Trennung zwischen Teilfortschritt und vollständigem Beweis.
5. **Simplifying, Stabilizing & Scaling Continuous-Time Consistency Models** – methodischer Hinweis auf Diskretisierungsfehler, kontinuierliche Grenzfälle und separate Stabilitätsprüfung.
6. **Black Hat USA 2026 / Roblox** – Trust Boundaries, Network Isolation, adversarial review, runtime validation, agent sandboxing und untrusted GitHub input.
7. **HTTP Terminator / PortSwigger** – Ideation -> Evaluation -> Impact -> Cascade; Micro-Inspiration und deterministische Evaluation als Kern eines autonomen Research-Loops.
8. **onepct** – Capability Graph, Reseed/State Signature und strukturierte Subagent-Contracts gegen Long-Context-Verlust und Mehrdeutigkeit.

### Nicht übernommen

`9789402157574.pdf` (Minoan Linear A / Hurrian) ist fachlich nicht relevant für GR, PBH/BH-Physik, Akkretion, Seismik, Numerik oder Forschungsverifikation und wird deshalb nicht in die wissenschaftliche Quellenmatrix aufgenommen.

## 11. Öffentliche Quellen

- OpenAI FrontierScience paper (lokale Projektquelle / vom Nutzer bereitgestellt)
- OpenAI Formal Mathematics Statement Curriculum Learning (lokale Projektquelle / vom Nutzer bereitgestellt)
- OpenAI single-minus gluon amplitudes paper (lokale Projektquelle / vom Nutzer bereitgestellt)
- OpenAI unit-distance proof (lokale Projektquelle / vom Nutzer bereitgestellt)
- OpenAI continuous-time consistency models paper (lokale Projektquelle / vom Nutzer bereitgestellt)
- https://blackhat.com/us-26/briefings/schedule/
- https://about.roblox.com/newsroom/2026/07/roblox-unveils-security-research-tools-black-hat-bsides-las-vegas
- https://portswigger.net/research/can-ai-do-novel-security-research
- https://github.com/evanslify/onepct

## 12. Stage-3.95B Exit-Kriterium

Stage 3.95B selbst ist abgeschlossen, wenn die Forschungsinfrastruktur steht:

```text
[ ] Research Protocol versioniert
[ ] Agent Security Policy versioniert
[ ] Capability Graph vorhanden
[ ] Rubrics vorhanden
[ ] Result Contract vorhanden
[ ] F12/A35/H0 in die neue Pipeline überführt
[ ] erste unabhängige Cross-Solver-Artefakte erzeugt
```

Physikalische Gates bleiben so lange OPEN, bis deren eigene Exit-Kriterien erfüllt sind.
