# NSF Audit Addendum – EPOC Scope Correction + 2026 SCEM Cross-Check

**Datum:** 30.08.2026

## Korrektur

Im ersten NSF-Sweep wurde EPOC zu breit als unmittelbares `EPOC-vs-PREM`-H0-Near-Zone-Robustheitsgate formuliert. Das wird hier präzisiert:

- EPOC ist ein Modell **des äußeren Kerns**.
- In der EPOC-Inversion werden Änderungen auf den outer-core Bereich beschränkt; außerhalb wird PREM verwendet.
- Die Autoren fixieren `P(CMB)=135.75 GPa` und `g(ICB)=4.4002 m/s²` und sagen ausdrücklich, dass das resultierende Planetmodell als Ganzes nicht selbstkonsistent ist.
- Die Stage-3.94-H0-Near-Zone liegt standardmäßig bei `r <= 2 km`, also weit innerhalb des inneren Kerns.

**Folge:** EPOC ist ein valider **outer-core/path-background validation source**, aber kein direkter Ersatz für das zentrale H0-Near-Zone-Modell. Für eine lokale differentielle 0–2-km-Anomalie kürzt sich ein ausschließlich äußerer-Kern-Referenztausch aus dem Δt heraus. Für absolute Zentrum-Streuer-Laufzeiten bleibt die Referenzmodellwahl relevant.

## Post-NSF Cross-Check: moderneres whole-Earth Modell

Munch et al. (2026), *Self-Consistent Models of Earth's Mantle and Core From Long-Period Seismic and Tidal Constraints*, ist der stärkere nächste Referenzmodellpfad. Die Arbeit invertiert Long-Period-Normalmoden zusammen mit astronomisch-geodätischen Daten und Tidal Response und stellt sowohl physikalisch selbstkonsistente SCEM- als auch polynomial parametrisierte P-PEM-Modelle bereit.

Das aktuelle Dataset auf Zenodo (`10.5281/zenodo.18386410`, Version v4) enthält `models.zip` mit MAP-Modellen, posterior-repräsentativen Modellen und Bounds von `Vp`, `Vs` und Dichte. Für SCEM werden zusätzlich Druck und Temperatur bereitgestellt, wo verfügbar.

**Projektklassifikation:**

```text
EPOC 2018: OUTER_CORE_REFERENCE / PATH_VALIDATION
SCEM 2026: WHOLE_EARTH_REFERENCE / UNCERTAINTY_ROUTE
```

SCEM wird erst numerisch übernommen, wenn die tatsächlichen `.bm`-Modelldateien vorliegen. Repository-Metadaten oder Abbildungen werden nicht als numerische Ersatzdaten verwendet.

## Quellen

- Irving, Cottaar & Lekić (2018), DOI `10.1126/sciadv.aar2538`
- PREM / IRIS EMC, DOI `10.17611/DP/10131390`
- Munch et al. (2026), DOI `10.1029/2024JB030971`
- SCEM/P-PEM dataset v4, DOI `10.5281/zenodo.18386410`
