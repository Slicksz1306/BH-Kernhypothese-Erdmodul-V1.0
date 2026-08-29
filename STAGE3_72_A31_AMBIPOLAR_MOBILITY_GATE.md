# Stage 3.72 / A31 – Ambipolare Mobilität und Stromgleichgewicht: Identifizierbarkeits-Gate

**Projekt:** SL/BH-Kernhypothese Erdmodul  
**Datum:** 29.08.2026  
**Status:** ELECTRON/ION TRANSPORT HIERARCHY CALCULATED / NERNST-EINSTEIN AS FINAL CLOSURE REJECTED / EXACT `Q_eq` REQUIRES ONSAGER-MATRIX

## Ziel

A27–A30 haben die Zeitskalenhierarchie des Charge-Problems stark eingeengt:

```text
~1e-17 s      elektronische Feld-/Screeningantwort
~0.26-0.75 ps Fe/Ni-Ionenstruktur über lambda_TF
~2.6 ps       publizierter warm-dense Fe e-i Energieaustauschanker
~5.9 ps       r_B/c_eff bei M=1e11 kg.
```

A31 prüft nun, ob die publizierten Fe/Ni-Selbstdiffusionskoeffizienten zusammen mit der hohen elektronischen Leitfähigkeit bereits ausreichen, um eine ambipolare Stromclosure und damit `Q_eq` zu bestimmen.

Die Antwort lautet:

```text
Nein – aber die Transporthierarchie kann weiter eingegrenzt werden.
```

## Literaturanker

### Fe/Ni-Selbstdiffusion

Li et al., Scientific Reports 12, 21255 (2022), DOI `10.1038/s41598-022-24594-8`:

```text
D_Ni ~2.47e-9 ... 3.37e-9 m^2/s
D_Fe ~gleiche Größenordnung entlang der Kernadiabate.
```

### Multikomponenten-WDM-Diffusion

White et al., Phys. Rev. E 100, 033213 (2019), DOI `10.1103/PhysRevE.100.033213`, formulieren warm-dense Mehrkomponentendiffusion über Maxwell-Stefan-Koeffizienten und Onsager-Terme. Die makroskopischen Diffusionsströme hängen damit nicht nur von den tracer/self-Diffusionskoeffizienten ab, sondern auch von Kreuzkorrelationen und chemischen Potentialgradienten.

### Elektrische Leitfähigkeit des Core-Alloys

Aktuelle Hoch-P/T-Arbeiten für Fe-Ni-Si liefern eine Outer-Core-Untergrenze von ungefähr

```text
sigma_e >=9.2e5 S/m.
```

Theoretische Arbeiten für metallische flüssige Kernlegierungen liegen ebenfalls typischerweise bei `O(1e6 S/m)`.

A31 verwendet `9.2e5 S/m` als konservativen elektronischen Vergleichsanker.

## Naiver Nernst-Einstein-Stressproxy

Nur um die Größenordnung maximal transparent zu vergleichen, wird

```text
sigma_i,NE = n_i (Zbar e)^2 D/(k_B T)
```

mit

```text
n_i = 1.4075e29 m^-3
T   = 6000 K
D   = 2.47e-9 ... 3.37e-9 m^2/s
```

berechnet.

**Diese Relation wird ausdrücklich nicht als exakte WDM-Multikomponentenclosure verwendet.** Sie nimmt unabhängige Ionenbewegung an und ignoriert Onsager-Kreuzterme, starke Korrelation und reale Mehrkomponenten-Chemie.

## Low-ionization Endpoint

Für

```text
Zbar=2.76
```

folgt

```text
sigma_i,NE ~8.21e2 ... 1.12e3 S/m.
```

Gegen den elektronischen Untergrenzenanker

```text
sigma_e >=9.2e5 S/m
```

ist die Elektronenleitfähigkeit damit mindestens

```text
~8.2e2 ... 1.1e3
```

mal größer.

## Fully-ionized Stressendpoint

Für den absichtlich extremen oberen Proxy

```text
Z=26
```

folgt

```text
sigma_i,NE ~7.28e4 ... 9.94e4 S/m.
```

Selbst hier bleibt

```text
sigma_e/sigma_i,NE >=~9.3 ... 12.6.
```

Damit ist in beiden getesteten Endpunkten die schnelle elektrische Stromantwort elektronisch dominiert.

## Was dieser Vergleich aussagt

A31 stützt die A27/A30-Hierarchie:

```text
electronic charge transport >> ionic charge transport
```

im Outer-Core-Referenzbereich.

Das macht es plausibel, dass das ambipolare Feld sehr schnell den Elektronenstrom an die langsamere Ionen-/Bulkbewegung anpasst.

Es bedeutet aber **nicht**, dass die Ionen irrelevant sind. A30 zeigte bereits, dass ihre Struktur auf Sub-ps-Zeiten über eine Screeninglänge reagieren kann.

## Warum Nernst-Einstein `Q_eq` nicht schließt

Für eine reale Fe-Ni-Light-Element-Mischung benötigt die lineare irreversible Thermodynamik schematisch

```text
J_i = - sum_j L_ij grad(mu_j/T) + electrical-force terms + ...
```

mit einer Onsager-Matrix `L_ij`.

Äquivalent kann die Massendiffusion in Maxwell-Stefan-Form geschrieben werden, wobei gegenseitige Diffusionskoeffizienten und thermodynamische Faktoren auftreten.

Die vorhandenen Größen

```text
D_Fe,self
D_Ni,self
sigma_e
```

reichen daher nicht aus, um

```text
J_Fe(E,grad mu,...)
J_Ni(E,grad mu,...)
J_light(E,grad mu,...)
J_e(E,grad mu_e,...)
```

eindeutig zu bestimmen.

Insbesondere gilt:

```text
self diffusion != mutual diffusion != charge mobility.
```

## Konsequenz für den ambipolaren Zustand

A27s Reduced-Bedingung

```text
I_i(Q,E,...) + I_e(Q,E,...) ~=0
```

bleibt die richtige Zielstruktur.

A31 zeigt aber, dass aus den aktuell öffentlich verifizierten Transportinputs noch kein eindeutiges

```text
E_amb(r)
```

und damit kein eindeutiges

```text
Q_eq
```

berechnet werden kann.

Der Grund ist jetzt präzise lokalisiert:

```text
fehlende multicomponent Onsager/Maxwell-Stefan mobility matrix
+ chemical-potential derivatives
+ sink-boundary coupling.
```

## Bezug zu A26

A26s unabhängige `n v sigma`-Ströme verfehlten den Stromausgleich bei `Q<=5e` um etwa `10^4`.

A31 zeigt, warum dieser Mismatch nicht als direkte Ladeentwicklung interpretiert werden darf:

- elektronische Leitfähigkeit ist sehr groß;
- Strom und Feld sind kollektiv gekoppelt;
- ionische Tracer-Diffusion beschreibt den Ladungsstrom nicht vollständig;
- Kreuzkorrelationen/ambipolare Felder können die relativen Ströme stark ändern.

Das ist keine Garantie, dass der reale Gleichgewichtswert innerhalb `1...5e` liegt. Es erklärt nur, warum A26 kein valider `Q_eq`-Solver war.

## Was A31 schließt

```text
Nernst-Einstein from Fe/Ni self-D as exact ionic current closure:
REJECTED.

electronic conductivity dominance in tested outer-core stress bracket:
CALCULATED / STRONGLY SUPPORTED.

self-D + sigma_e sufficient to identify Q_eq:
NO.
```

## Was als echter nächster Input fehlt

Um den Charge-Block weiter physikalisch zu schließen, braucht man mindestens eines von:

```text
1. published Fe-Ni-light-element Onsager coefficients under relevant P/T/X;
2. Maxwell-Stefan mutual diffusion matrix + thermodynamic factors;
3. QMD trajectories/data from which the required cross-current correlations can be evaluated;
4. a first-principles multicomponent transport calculation tied to the project radial state.
```

Der öffentliche Liu/Asimow-Mischungsdatensatz aus A22 bleibt dafür interessant, enthält aber nach bisheriger Verifikation EOS/thermodynamische Rohdaten, nicht automatisch die komplette benötigte Charge-Mobility-Matrix.

## Konsequenz für Full-WDM / Mdot

A24 bleibt gültig:

```text
final species-resolved Mdot_BH(t):
NOT YET IDENTIFIABLE.
```

A31 reduziert den offenen Block jedoch weiter auf eine klarere Größe:

```text
microscopic electron sink: hardened by A25/A29
screening hierarchy: hardened by A27/A28/A30
remaining charge bottleneck:
MULTICOMPONENT AMBIPOLAR MOBILITY / ONSAGER CURRENT CLOSURE.
```

## Reproduzierbare Datei

- `stage3_72_a31_ambipolar_mobility_gate.py`

## Schlussstatus

```text
naive ionic Nernst-Einstein stress proxy:
CALCULATED.

electronic transport dominance:
ROBUST in tested outer-reference bracket.

Nernst-Einstein as full WDM current model:
REJECTED.

exact ambipolar E(r), Q_eq:
OPEN / NOT IDENTIFIABLE FROM CURRENT TRANSPORT INPUTS.

experimental BH detection:
NONE.
```
