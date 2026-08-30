# NSF Source Audit – SL/BH-Kernhypothese Erdmodul

**Datum:** 30.08.2026  
**Scope:** NSF.gov, NSF News, NSF Public Access Repository (NSF-PAR), relevante aktuelle NSF-Programme sowie daraus auffindbare peer-reviewte Quellen.  
**Ziel:** Nur Material übernehmen, das bestehende Projekt-Gates tatsächlich schärft, validiert oder mit belastbaren Referenzdaten versorgt.

## Ergebnis

Der NSF-Sweep liefert **keine direkte vollständige A35-Closure** für ein reales `Q_eq`, aber mehrere wertvolle Validierungs- und Methodenquellen. Der stärkste neue unmittelbar implementierbare Projektpunkt ist ein **EPOC-vs-PREM-Seismik-Sensitivitätsgate** für H0. Für F12 werden die bereits geforderten modellabhängigen Nicht-Gauß-Statistiken klar bestätigt. Für H+ kommen externe Hawking/PBH-Populationsgrenzen hinzu, die ausdrücklich **keine Earth-center-BH-Exklusion** darstellen.

## Gate-Impact

| Gate | Vor NSF-Audit | Nach NSF-Audit | Konsequenz |
|---|---|---|---|
| A35 multikomponentiger Ionen-Transport `L_st` | OPEN | OPEN | Kein direktes Fe-Ni-Light Onsager/Maxwell-Stefan-Dataset gefunden. |
| A35 Elektronen-Transport | OPEN | OPEN, besser validierbar | Fe-Si/Fe-Ni-Si Leitfähigkeitsdaten + WDM Kubo-Greenwood/Workshop als Validierungs-/Methodenanker. |
| A35 Ionisation/charge states | OPEN | OPEN, Unsicherheit stärker belegt | WDM-Literatur zeigt Ionisationsmodell als wesentliche Streuungsquelle. |
| `Q_bullet -> Q_m` / Capture `K_s` | OPEN | OPEN | Interface-Plasmaarbeit rechtfertigt explizites Matching-Modul, liefert aber keine BH/WDM-Closure. |
| H0 Seismik | Sensitivität primär PREM | **neues Robustheitsgate** | EPOC als unabhängiges outer-core Referenzmodell gegen PREM rechnen. |
| F12 PBH-Formation | OPEN | OPEN, Gate besser begründet | Exakte PBH-Abundanz muss bei Nicht-Gaußförmigkeit modellabhängig berechnet werden. |
| H+ Hawking | stark unter Druck | unverändert; externe Kontextgrenzen ergänzt | INTEGRAL/SPI liefert Populationsgrenzen, aber keine Einzelobjekt-Earth-center-Grenze. |
| Experimenteller BH-Nachweis | NONE | NONE | NSF-Material liefert keinen Nachweis. |

## H0: EPOC-vs-PREM als Pflicht-Sensitivität

Irving, Cottaar & Lekić (2018) stellen das **EPOC**-Modell des äußeren Erdkerns vor. Gegenüber PREM sinkt der reduzierte χ²-Misfit der verwendeten Normalmoden von 1.54 auf 1.02; für Moden mit >10% integrierter Sensitivität im äußeren Kern von 2.51 auf 0.74. EPOC besitzt außerdem systematisch andere Geschwindigkeits- und Dichteprofile; die Dichte liegt etwa 0.94–1.25% über PREM.

**Projektregel:** Jede H0-Seismik-Aussage, die nur unter PREM besteht, gilt künftig als **REFERENCE-MODEL-SENSITIVE**. Eine belastbare H0-Seismikgrenze sollte mindestens unter PREM und EPOC erneut berechnet werden.

Das ist kein positives BH-Signal, sondern ein Robustheitstest gegen Unsicherheit des Referenz-Erdmodells.

Quelle: https://par.nsf.gov/servlets/purl/10084418  
DOI: https://doi.org/10.1126/sciadv.aar2538

## A35: Übernehmen

- Fe-Si / Fe-Ni-Si Hochdruck-Leitfähigkeit als **Subdomain-Validierung**.
- Charged-particle transport workshop als **Inter-Code-/Unsicherheitsmethodik**.
- Dense-hydrogen review als **Kubo-Greenwood- und Ionisationsunsicherheitsreferenz**.
- Pump-probe-WDM und interfacial thermal resistance als **Experiment-/Interface-Methodenreferenzen**.

### Nicht hochstufen

- `sigma` oder `kappa` -> freies `D_e`: **VERBOTEN**.
- Selbst-/binäre Diffusion -> vollständige multikomponentige `L_st`: **VERBOTEN**.
- Fe-Si -> Fe-Ni-Light vollständige Closure: **VERBOTEN**.
- Plasma-Interfacewärmewiderstand -> `Q_bullet -> Q_m` oder `K_s`: **VERBOTEN**.

### A35-Blocker nach NSF-Sweep

1. Vollständige species-resolved Fe-Ni-Light Ionen-Transportmatrix: **nicht geschlossen**.
2. Vollständiger WDM-Elektronenflussoperator im Zielzustand: **nicht geschlossen**.
3. Fe-Ni-Light Thermodynamik/Hesse-Matrix über Ziel-P-T-X: **nicht geschlossen**.
4. Diskrete Ladungszustands-/Ionisationsclosure: **nicht geschlossen**.
5. Inneres BH/WDM-Matching `Q_bullet -> Q_m`: **nicht geschlossen**.
6. Capture/Sink `B_s`, `K_s`/`Ktilde_s`: **nicht geschlossen**.

**Wichtig:** „In diesem NSF-Sweep nicht gefunden“ ist keine Behauptung, dass solche Daten weltweit nicht existieren. Es bedeutet nur: kein direkt verwertbarer NSF-Treffer wurde in dieser Recherche identifiziert.

### A35-Schlüsselquellen

1. **Earth’s core composition and core formation** — Fe-Ni plus ca. 10% leichtere Elemente; Identitäten/Anteile bleiben unsicher.  
   https://par.nsf.gov/servlets/purl/10658234  
   DOI: https://doi.org/10.1016/B978-0-323-99762-1.00116-9

2. **Thermal conductivity of Fe-Si alloys and thermal stratification in Earth’s core** — Experimente plus FPMD/DMFT; liquid Fe-9Si nahe Top-Outer-Core ca. 100–110 W m^-1 K^-1. Nur Subdomain-Validierung.  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC8740763/  
   DOI: https://doi.org/10.1073/pnas.2119001119

3. **Transport properties of Fe-Ni-Si alloys at Earth's core conditions** — Resistivität Fe-10wt%Ni und Fe-1.8wt%Si bis ca. 142 GPa / 3400 K; modellierte nominale Leitfähigkeit ca. 50 W m^-1 K^-1 für Fe-5Ni-8Si. Kein multikomponentiger Massentransportoperator.  
   DOI: https://doi.org/10.1016/j.epsl.2020.116614

4. **Review of the second charged-particle transport coefficient code comparison workshop** — Methoden-/Benchmarkanker für WDM-Transport.  
   https://par.nsf.gov/servlets/purl/10570457  
   DOI: https://doi.org/10.1063/5.0198155

5. **Towards first principles-based simulations of dense hydrogen** — Kubo-Greenwood als Standardroute für DFT-Transport; Codevergleiche zeigen typische Streuung von ca. 20% im best-case weak-coupling, Faktor ~2 im WDM-Bereich und bis Faktor 10+ bei niedrigen Temperaturen; Ionisationszustand als wichtige Streuungsquelle. Methodisch wertvoll, numerisch nicht auf Fe-Ni-Light übertragbar.  
   https://par.nsf.gov/servlets/purl/10632133

6. **Ultrafast pump-probe WDM diagnostics** — Methodenreferenz für zukünftige WDM-Messungen, keine Fe-Ni-Light-Closure.  
   https://www.nsf.gov/news/researchers-track-plasma-creation-using-novel-ultra-fast

7. **Interfacial thermal resistance in HED plasma** — stützt die explizite Interface-/Matching-Architektur; liefert keine BH/WDM-Matching-Closure.  
   https://www.nsf.gov/news/extreme-conditions-heat-does-not-flow-between-materials-it

## F12

NSF-PAR-Quellen stützen die Projektregel, dass PBH-Abundanz nicht allein aus einer Peak-Amplitude abgeleitet werden darf, wenn Nicht-Gaußförmigkeit relevant ist. Eine Arbeit zu unvollständigen inflationären Phasenübergängen sagt ausdrücklich, dass eine auf Gaussianität beruhende PBH-Grenze nur eine grobe Schätzung ist und für den exakten Bound eine modell-spezifische nicht-gaußsche Statistik benötigt wird.

**Projektfolge:** F12 bleibt OPEN, aber die formale Closure-Anforderung wird als harter Gate geführt:

`P_zeta(k)` + definierte Non-Gaussianity/PDF + Collapse/threshold convention + Formation mapping + aktuelle PBH constraint matrix.

Quellen:
- https://par.nsf.gov/servlets/purl/10105471
- https://par.nsf.gov/servlets/purl/10516781
- DOI: https://doi.org/10.1103/PhysRevD.108.115016

## H+

INTEGRAL/SPI fand in einer 16-Jahres-Analyse keinen NFW-förmigen PBH-Beitrag und setzt 95%-CL-Grenzen für PBHs als galaktische DM-Population. Das ist ein externes Hawking/PBH-Observationsresultat.

**Aber:** Es darf nicht als Ausschluss eines einzelnen hypothetischen Schwarzen Lochs im Erdzentrum verwendet werden. Die Analyse setzt eine galaktische PBH-Population und NFW-Geometrie voraus.

Quelle: https://par.nsf.gov/servlets/purl/10437779  
DOI: https://doi.org/10.1103/PhysRevD.106.023030

Die Super-K-IV-Publikation wird nur als Detektor-/Performance-Referenz übernommen: Standard-Fiducial-Volumen 22.5 kt, 2970 SK-IV-Livetage, 3.49-MeV-Threshold der Solarneutrinoanalyse. Sie ist **keine offizielle Suche nach einem Hawking-emittierenden Earth-center-BH**.

Quelle: https://par.nsf.gov/servlets/purl/10543031  
DOI: https://doi.org/10.1103/PhysRevD.109.092001

## NSF als zukünftige Datenroute

- **GEO Core / SPSE:** Erdinneres, Kernstruktur/-physik, Labor/Theorie/Computation.  
  https://www.nsf.gov/funding/opportunities/geo-core-geosciences-core-research-atmospheric-geospace-earth-ocean/nsf26-516/solicitation
- **Plasma Physics (NSF 26-523):** high-energy-density und strongly coupled plasmas.  
  https://www.nsf.gov/funding/opportunities/plasma-physics
- **MATRIX-MIP:** Infrastruktur für Materialien in extremen Umgebungen.  
  https://www.nsf.gov/news/nsf-stands-2-materials-innovation-platforms-50m-investment
- **NSF-PAR + Award Search:** fortlaufende Quellen-/Award-/Dataset-Metadaten-Suche.  
  https://www.nsf.gov/public-access  
  https://www.nsf.gov/funding/award-search

Diese Programme sind **Forschungswege**, keine Evidenz.

## Status nach Audit

```text
Stage 3.95C Architecture Definition Gate: PASS AS SPECIFICATION
Physical Closure Completeness:             OPEN
Solver Release Gate:                       NOT PASSED
Real Q_eq Implementation:                  NO-GO
Experimental BH Evidence:                  NONE
```

Der NSF-Sweep verbessert Referenzmodelle, Validierung, Unsicherheitsbehandlung und zukünftige Datenwege. Er entfernt **keinen** der entscheidenden physischen A35-Blocker.
