# Stage 3.95B – Harness and Evaluation Audit

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Status:** METHODIK / QA  
**Stand:** 29.08.2026

## 0. Zweck

Dieses Dokument ergänzt `STAGE3_95B_RESEARCH_VERIFICATION_PROTOCOL.md` um eine Meta-Ebene: Nicht nur Solver und Agent müssen geprüft werden, sondern auch **Aufgabenstellung, Test-Harness, Kontextverwaltung, Modalitäten und Bewertungslogik selbst**.

Grundregel:

```text
measured result = model/solver + harness + task spec + tests + context policy + data
```

Ein Benchmark-/Regressionsergebnis wird nicht isoliert vom Harness interpretiert.

## 1. Harness ist Teil des Experiments

OpenAIs ARC-AGI-3-Analyse zeigt, dass retained reasoning und Compaction die gemessene Leistung desselben Modells deutlich verändern können. Für unser Projekt folgt daraus:

Jeder agentische Research-/Solverlauf protokolliert soweit anwendbar:

```yaml
model:
reasoning_mode:
context_policy:
compaction_policy:
state_signature_version:
toolset:
harness_version:
repo_commit:
solver_version:
random_seed:
parameter_file:
```

Regel:

```text
Harness-Aenderung => Re-Baseline erforderlich.
```

Resultate verschiedener Harness-Versionen werden nicht ohne Reproduktion direkt verglichen.

## 2. Kein Rolling-Truncation-Blindflug

Bei langen Forschungslaeufen werden wichtige Statusinformationen nicht stillschweigend verworfen. Stattdessen:

```text
raw history
   -> compact verified state
   -> capability signature
   -> current assumptions / open gates
```

Die kompakte State-Signature darf nur verifizierte Statusinformationen enthalten und muss versioniert sein.

## 3. Eval-Quality Gate

Die OpenAI-Audit-Arbeit zu SWE-Bench Pro zeigt vier Fehlerklassen, die wir auf eigene wissenschaftliche Tests uebertragen:

1. **Overly strict test** – der Test erzwingt eine Implementierungsform statt physikalisch/mathematisch relevanter Funktionalitaet.
2. **Underspecified task** – der Test verlangt etwas, das in der Aufgaben-/Annahmenspezifikation fehlt.
3. **Low coverage** – ein PASS deckt den eigentlichen Claim nicht ausreichend ab.
4. **Misleading specification** – Aufgabenbeschreibung und Testziel laufen auseinander.

Vor einer Claim-Promotion muss daher nicht nur die Implementierung, sondern auch die Testqualitaet geprueft werden.

### Meta-Rubrik fuer jeden neuen Regressionstest

```yaml
spec_alignment:        true|false
physics_relevance:     true|false
coverage_target:       documented
false_positive_risk:   documented
false_negative_risk:   documented
independent_oracle:    available|partial|none
edge_cases:            listed
```

Ein 100%-PASS einer schwachen Suite ist kein starker wissenschaftlicher Befund.

## 4. External Oracle / Acceptance Target

Aus `Scientific computing in the age of agentic AI` uebernehmen wir die Forderung nach messbaren Akzeptanzzielen.

Bevor Codex einen wissenschaftlichen Block implementiert, wird mindestens ein Oracle definiert:

- exakte analytische Referenz,
- unabhaengiger CAS-Wert,
- Zweitimplementierung,
- etablierter Spezialfall,
- synthetische Daten mit bekannter Loesung,
- Erhaltungssatz / Invariante,
- publizierter Benchmarkwert, falls passend.

Ohne Oracle lautet der Status maximal:

```text
IMPLEMENTED / UNVERIFIED
```

nicht `PASS`.

## 5. Multimodal Audit

Die Distill/OpenAI-Arbeit `Multimodal Neurons in Artificial Neural Networks` zeigt, dass CLIP-artige Systeme semantische Konzepte modalitaetsuebergreifend repraesentieren und durch typografische Beschriftungen in Bildern stark beeinflusst werden koennen.

Daraus folgen fuer unseren Workflow zwei getrennte Regeln.

### 5.1 Security

```text
text rendered inside an image == untrusted source content
```

Bildtext darf keine Agentenprivilegien oder Aktionen autorisieren.

### 5.2 Scientific provenance

Bei Abbildungen mit wissenschaftlich relevanten Zahlen/Labels:

```text
figure observation
    + caption
    + surrounding text
    + source/table/equation when available
        -> verified extracted claim
```

Ein Wert, der nur aus einem Plot visuell abgeschaetzt wurde, wird als `PLOT_ESTIMATE` markiert und nicht als exakter Literaturwert behandelt.

## 6. Polysemanticity / Interpretability Warning

Die Multimodal-Neuron-Arbeit zeigt zudem polysemantische bzw. konjungierte Features: ein einzelner interner Aktivierungsweg kann mehrere oberflaechlich oder semantisch gekoppelte Konzepte tragen.

Methodische Konsequenz:

```text
model explanation != mechanistic proof
```

Erklaerungen eines LLM ueber den Grund seines Ergebnisses dienen der Hypothesengenerierung, nicht als Beweis, dass genau dieser interne Mechanismus zum Resultat fuehrte.

## 7. Provisional Proof Status

OpenAIs `First Proof`-Bericht dokumentiert, dass ein zunaechst fuer wahrscheinlich korrekt gehaltener Beweisversuch nach Experten-/Community-Analyse als falsch eingestuft wurde.

Darum fuehren wir fuer mathematische Claims zusaetzlich ein:

```text
DRAFT
PROVISIONAL
INDEPENDENTLY_CHECKED
LEAN_VERIFIED
```

`PROVISIONAL` darf niemals automatisch zu einem physikalischen `PASS` hochgestuft werden.

## 8. Formal Certificate Boundary

Die OpenAI-Veröffentlichung zu zehn mathematischen Fortschritten beschreibt einen Workflow, in dem mathematische Argumente anschliessend formalisiert und als Lean-Zertifikate bereitgestellt wurden.

Fuer das SL/BH-Projekt gilt:

```text
Lean certificate
    proves formal statement under encoded assumptions
    does NOT prove empirical truth of those assumptions.
```

Der formale Satz muss deshalb gemeinsam mit seiner Annahmenliste versioniert werden.

## 9. Adversarial QA

Aus GPT-Red uebernehmen wir einen defensiven Self-Play-Loop fuer unsere Agenten:

```text
adversarial input generator
        -> research agent
        -> failure detector
        -> policy/test fix
        -> permanent regression case
```

Testklassen:

- Prompt Injection aus Tool-/Web-/Repo-Content,
- Bild-/Plot-Text als falsche Anweisung,
- erfundene Quelle,
- behaupteter, aber nicht ausgefuehrter Test,
- Claim-Promotion ohne Gate,
- falsche Einheiten,
- unvollstaendige Annahmenspezifikation,
- Kontextverlust nach Compaction.

## 10. Minimum Acceptance Record

Ein harter Stage-3.95B-Resultatdatensatz enthaelt mindestens:

```yaml
claim_id:
problem_spec_hash:
harness_version:
source_snapshot:
assumptions:
solver_commit:
tests:
meta_test_audit:
independent_oracle:
convergence:
adversarial_review:
formal_status:
limitations:
final_claim_level:
```

## 11. Quellen

- https://distill.pub/2021/multimodal-neurons/
- https://openai.com/de-DE/research/index/publication/
- https://openai.com/index/how-two-settings-tripled-our-arc-agi-3-scores/
- https://openai.com/index/scientific-computing-agentic-ai/
- https://openai.com/index/separating-signal-from-noise-coding-evaluations/
- https://openai.com/index/first-proof-submissions/
- https://openai.com/index/ten-advances-in-mathematics/
- https://openai.com/index/unlocking-self-improvement-gpt-red/

## 12. Aussagegrenze

Dieses Dokument verbessert die Zuverlaessigkeit der Forschungsinfrastruktur. Es liefert **keine neue BH-Evidenz** und aendert keinen physikalischen Gate-Status allein durch seine Existenz.
