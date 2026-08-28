# Stage 3.70B / A18 — Current Real-Data Audit

## Status

**H+ CURRENT DATA RECHECK CALCULATED / H0 FULL LIKELIHOOD NOT IDENTIFIABLE YET**

A18 ist der erste Stage-3.70-Block, der nach dem A13b/A17-Update ausdrücklich die aktuelleren veröffentlichten Beobachtungsdaten erneut gegen den Projektstatus hält.

## 1. Aktueller Super-Kamiokande-Kontext

Die Super-Kamiokande Collaboration veröffentlichte 2026 eine SK-Gd-Suche mit `956.2` Tagen SK-VI+VII-Daten:

- K. Abe et al., *Search for Diffuse Supernova Neutrino Background with 956.2 days of Super-Kamiokande Gadolinium Dataset*, Astrophysical Journal 1005, 101 (2026), arXiv:2511.02222.

Im spectrum-independent Teil werden 90%-CL-Obergrenzen auf den astrophysikalischen `anti-nu_e`-Fluss pro Energiebin angegeben.

Für

```text
25.29 ... 31.29 MeV
```

listet die Publikation:

```text
SK-IV observed 90% CL       = 0.04 cm^-2 s^-1 MeV^-1
SK-VI+VII NN observed       = 0.13 cm^-2 s^-1 MeV^-1
SK-VI+VII BDT observed      = 0.16 cm^-2 s^-1 MeV^-1.
```

Die 2026-Publikation zeigt damit ausdrücklich, dass der ältere SK-IV-Datensatz in diesem hohen Energieband weiterhin die stärkere publizierte Obergrenze besitzt.

## 2. Projekt-H+ Vergleich

Der bisherige konservative Projekt-Greybody-/Flavor-Proxy für H+ in demselben Band liegt bei

```text
Phi_H+,project ~0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Verhältnis zum stärksten SK-IV-Binlimit:

```text
0.098/0.04 = 2.45
0.122/0.04 = 3.05.
```

Dagegen liegt der Projektfluss unter den standalone SK-Gd-2026-Limits:

```text
vs 0.13 -> 0.75 ... 0.94 of limit
vs 0.16 -> 0.61 ... 0.76 of limit.
```

Damit lautet der aktualisierte, präzise Status:

```text
H+ Standard-Hawking:
FAIL in the project's bin-by-bin reinterpretation against the strongest
published SK-IV 25.29--31.29 MeV constraint.

The standalone 2026 SK-Gd-only sample by itself does not exclude the
project proxy in that bin.
```

Dies ist weiterhin **keine offizielle Super-K-Erdzentrum-BH-Exklusion**. Der Projektfluss ist ein eigener Hawking/Greybody-/Flavor-Proxy; eine offizielle detector-response Analyse für eine Earth-centered Hawking source wurde nicht von Super-K publiziert.

## 3. 2026 DSNB indication

Im Juni 2026 berichtete die Super-K Collaboration außerdem auf Neutrino 2026 über eine kombinierte Wasser+Gd-Analyse von ungefähr `5000` Tagen mit einer `2.6 sigma`-Indikation eines DSNB-Signals und einem best-fit Gesamtfluss von ungefähr

```text
3.6 +/- 1.6 cm^-2 s^-1
```

im analysierten breiten Energiebereich.

Dieser Befund darf **nicht** als Unterstützung des H+-Erd-BH-Branches interpretiert werden:

- DSNB ist ein astrophysikalisch erwarteter diffuser Supernova-Hintergrund;
- der Befund ist breitbandig und modellabhängig;
- der stärkere publizierte SK-IV-Hochenergie-Binconstraint bleibt in der 2026 SK-Gd-Publikation dokumentiert;
- es gibt keine identifizierte Earth-centered BH-Signatur.

## 4. H0 real-data identifiability

A17 zeigte:

```text
direct r_B-scale seismology -> not useful
heat hard total budget -> no exclusion
surface monopole under exact spherical compensation -> degenerate
matter-process neutrinos -> no final spectrum
macroscopic seismic perturbation -> amplitude/profile not yet predicted.
```

Öffentliche Daten existieren:

- PREM und seine maschinenlesbaren Tabellen,
- Normalmoden-/Travel-Time-Referenzen,
- globale Wärmeflussdaten,
- Neutrinodaten.

Aber ein H0-Likelihood-Test benötigt eine Vorhersage `y_H0(theta)` für dieselben Observablen. Für die derzeit stärksten H0-Kanäle fehlen noch insbesondere

```text
delta rho(r)
delta Vp(r)
delta Vs(r)
mode-frequency shifts
central-scattering waveform amplitude
matter-process anti-nu_e / nu spectra
thermal deposition profile.
```

Ohne diese Größen wäre eine numerische Likelihood künstlich: freie, nicht aus dem Modell berechnete Signal-Amplituden könnten beliebig an die Daten angepasst werden.

## 5. Stage-3.70 Ergebnis nach A18

| Branch/Kanal | Status |
|---|---|
| H+ strongest published SK-IV high-energy bin | **FAIL in project reinterpretation** |
| H+ standalone SK-Gd 2026 high-energy bins | project proxy **below those limits** |
| 2026 broad DSNB indication | **not an Earth-BH signature** |
| H0 direct microscopic seismology | **not observable/useful** |
| H0 heat absolute 47-TW budget | **no exclusion** |
| H0 full seismic likelihood | **NOT IDENTIFIABLE YET** |
| H0 matter-neutrino likelihood | **NOT IDENTIFIABLE YET** |
| H0 direct detection | **none** |
| unique positive H0 signature | **none** |

## Schlussfolgerung

Stage 3.70 kann derzeit für H+ einen real-data-basierten negativen Projektvergleich aufrechterhalten. Für H0 ist die wissenschaftlich korrekte Ausgabe dagegen

```text
OPEN / REAL-DATA LIKELIHOOD NOT YET IDENTIFIABLE
```

und nicht `PASS`.

Der fehlende Schritt ist eine Full-Multiphysics-Vorhersage einer **eindeutigen makroskopischen Observable**. Erst dann kann PREM/Seismik/Heat/Neutrino gegen H0 statistisch getestet werden.

## Reproducibility

- `stage3_70b_a18_realdata_audit.py`

## Claims boundary

A18 behauptet keine offizielle experimentelle Exklusion eines Erdzentrum-BH durch Super-K und keine Detektion. Es dokumentiert ausschließlich die projektinterne Reinterpretation veröffentlichter Flussgrenzen und die Identifizierbarkeit der H0-Kanäle.
