# Stage 3.95D / H0 – Seismic Reference-Model Audit

**Datum:** 30.08.2026  
**Status:** `PASS AS REFERENCE-MODEL SENSITIVITY AUDIT` / `H0 PHYSICAL CLOSURE OPEN` / `EXPERIMENTAL BH EVIDENCE NONE`

## 1. Ziel

Stage 3.95D trennt zwei bisher leicht vermischbare Fragen:

1. **Lokale H0-Differenz:** Wie groß ist die Laufzeitanomalie einer zentralen, kompensierten Struktur im innersten Bereich?
2. **Absoluter Referenzpfad:** Wie stark verschiebt sich die absolute Zentrum→Oberfläche- bzw. Zentrum-Streuer-Laufzeit, wenn ein anderes plausibles radiales Kernmodell verwendet wird?

Der Test ist ein Robustheits-/Systematiktest. Er liefert **keinen Nachweis eines Schwarzen Lochs**.

## 2. PREM-Reproduktion

Die Standard-PREM-Polynome werden direkt implementiert. Für einen radialen P-Wellenweg ergibt sich

```text
PREM Zentrum -> Oberfläche = 606.7743332118 s
PREM äußerer Kern           = 240.8321366279 s
```

Damit wird die frühere dokumentierte Größenordnung `~606.77 s` reproduziert.

Referenz: Dziewonski & Anderson (1981), PREM; IRIS EMC DOI `10.17611/DP/10131390`.

## 3. EPOC-Vinet-Rekonstruktion

Irving, Cottaar & Lekić (2018) bestimmen **Elastic Parameters of the Outer Core (EPOC)**. Die verwendeten Medianparameter sind

```text
K0S      = 67.5 GPa
K0S'     = 6.12
rho0     = 6110 kg/m^3
P(CMB)   = 135.75 GPa   [fixiert]
g(ICB)   = 4.4002 m/s^2 [fixiert]
```

Die Vinet-EoS wird hydrostatisch vom ICB zum CMB integriert; `P(ICB)` wird so geschossen, dass der feste CMB-Druck erreicht wird.

Rekonstruktion:

```text
P(ICB)                     = 332.907833984 GPa
rho(CMB)                   = 9991.684133 kg/m^3
Vp(CMB)                    = 8.000056706 km/s
EPOC äußerer-Kern-Laufzeit = 241.157585664 s
```

Die rekonstruierte CMB-Geschwindigkeit stimmt mit dem veröffentlichten EPOC-Wert von `8.00 km/s` überein.

**Wichtige Grenze:** Die EPOC-Autoren fixieren `P(CMB)` und `g(ICB)` und weisen selbst darauf hin, dass der Planet als Ganzes dadurch nicht selbstkonsistent ist. EPOC ist außerdem ein **outer-core model**, kein Modell des zentralen inneren Kerns.

Referenz: Irving, Cottaar & Lekić (2018), DOI `10.1126/sciadv.aar2538`.

## 4. PREM+EPOC-Hybrid als Pfad-Sensitivität

Nur der äußere PREM-Kernabschnitt `1221.5–3480 km` wird gegen EPOC ausgetauscht. Alle übrigen Schichten bleiben PREM.

```text
PREM Zentrum -> Oberfläche          = 606.774333212 s
PREM+EPOC Zentrum -> Oberfläche     = 607.099782248 s
Differenz, ein Weg                  = +0.325449036 s
Differenz, Zentrum-Streuer, 2 Wege = +0.650898072 s
```

Interpretation:

```text
ABSOLUTE CENTER-SCATTER BASELINE: REFERENCE-MODEL SENSITIVE
```

Eine absolute ~20-min-Laufzeit eines hypothetischen zentralen Streuers besitzt damit allein durch diesen outer-core-only Referenztausch eine Systematik von rund `0.65 s` für den idealisierten radialen Zweiwegpfad.

## 5. Korrektur gegenüber einer zu starken EPOC-Interpretation

EPOC darf **nicht** als Ersatzmodell für die lokale H0-Near-Zone verwendet werden.

Die aktuelle Stage-3.94-H0-Proxystörung liegt standardmäßig innerhalb

```text
r_outer = 2 km,
```

während EPOC erst außerhalb des ICB bei

```text
r >= 1221.5 km
```

gilt. Die Bereiche sind disjunkt. Bei einer differentiellen Laufzeitrechnung, in der Referenz und perturbiertes Modell außerhalb der Near-Zone identisch sind, kürzt sich die outer-core-Baseline exakt heraus.

Daher gilt für die aktuelle 0–2-km-Near-Zone:

```text
EPOC-vs-PREM outer-core swap -> keine direkte Änderung des lokalen Δt-Proxys
```

EPOC ist dennoch wertvoll für **absolute Pfadzeiten**, globale Moden/SmKS-Systematik und für die Warnung, dass die Wahl des Hintergrundmodells relevant ist.

## 6. Nächster stärkerer Referenzmodell-Gate: SCEM 2026

Munch et al. (2026) publizierten self-consistent Earth models (SCEM) aus Long-Period-Seismik, Tiden und astronomisch-geodätischen Constraints. Das zugehörige Zenodo-Dataset `10.5281/zenodo.18386410` enthält:

- MAP-Modelle,
- Posterior-Subsets,
- obere/untere Bounds für `Vp`, `Vs` und Dichte,
- für SCEM zusätzlich Druck/Temperatur, wo verfügbar,
- einen Forward Calculator für Normalmoden.

Das ist für einen späteren **whole-Earth reference-model uncertainty gate** geeigneter als ein isolierter EPOC-Hybrid.

Aktueller Status:

```text
SCEM source/dataset identified: YES
SCEM numerical model ingested:  NO
SCEM numerical gate executed:   NO
```

Es werden **keine SCEM-Zahlen erfunden oder aus Plots abgelesen**. Der numerische Gate wird erst ausgeführt, wenn `models.zip` bzw. die relevanten `.bm`-Dateien lokal verfügbar sind.

Referenzen:
- Munch et al. (2026), DOI `10.1029/2024JB030971`
- Dataset DOI `10.5281/zenodo.18386410`

## 7. Gate-Ergebnis

```text
PREM radial implementation:                     PASS
PREM legacy ~606.77 s reproduction:             PASS
EPOC-Vinet reconstruction:                      PASS
EPOC published CMB Vp ~8.00 km/s cross-check:  PASS
Absolute path reference sensitivity:            DETECTED (~0.6509 s two-way)
Current H0 0–2 km local overlap with EPOC:       NONE
SCEM whole-Earth uncertainty ingestion:          DEFERRED / DATA FILE REQUIRED
H0 physical closure:                             OPEN
Experimental BH evidence:                        NONE
```

## 8. Aussagegrenze

Dieser Stage verschärft die Seismikmethodik, bestätigt die Kernhypothese aber nicht. Ein späteres H0-Signal müsste über Referenzmodell-, Quellen-, 3-D-Heterogenitäts-, Rotations-/Anisotropie-, Instrument-/Timing- und vollständige Wellenform-Systematiken robust bleiben.
