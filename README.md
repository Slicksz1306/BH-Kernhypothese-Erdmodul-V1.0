# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.4  
**Aktueller Forschungsstand:** Stage 3.68  
**Stand:** 25.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Archivhinweis:** `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs- und Prioritätsnachweis erhalten. Die aktuelle Forschungsfassung wird in den Markdown-Dateien dokumentiert.

## Wissenschaftlicher Status in einem Satz

Die SL/BH-Kernhypothese Erdmodul ist ein **theoretischer Forschungsentwurf, kein experimenteller Nachweis**. Der Standard-Hawking-Zweig H+ faellt im aktuellen Projekt-Reinterpretationstest gegen ein publiziertes Super-Kamiokande-`anti-nu_e`-Limit; der nichtstandardmaessige H0-Zweig ohne Hawking-Strahlung wird durch die bisherigen reduzierten Erdtests nicht ausgeschlossen, besitzt aber weder eine positive Detektion noch einen hergeleiteten Standard-Formationweg.

## Zwei getrennte Hypothesen

### H+ - mit Standard-Hawking

H+ verwendet die uebliche semiklassische Hawking-Strahlung.

Nach der Greybody-/Neutrino-Haertung liegt der relevante Projektbereich bei ungefaehr

```text
M_BH = 4.82e11 ... 5.49e11 kg
T_H  = 21.99 ... 19.31 MeV.
```

Der konservative Projektfluss im SK-IV-Band 25.29-31.29 MeV liegt ueber dem publizierten spektrumsunabhaengigen beobachteten 90%-CL-Grenzwert von `0.04 cm^-2 s^-1 MeV^-1`.

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
```

Dies ist eine **Reinterpretation** eines Super-Kamiokande-Limits, keine offizielle Super-Kamiokande-Erdzentrum-BH-Analyse.

### H0 - ohne Hawking

H0 setzt als nichtstandardmaessige Gegenhypothese

```text
P_Hawking = 0.
```

H0 ist damit kein Standard-GR/QFT-Zweig. Hawking-basierte Neutrino-/Gamma-Grenzen sind fuer H0 definitionsgemaess nicht anwendbar; die fundamentale Begruendung fuer `P_Hawking=0` bleibt offen.

## Aktiver Erdbranch

Die starke Variante mit einem wesentlichen Anteil der Erdmasse im zentralen BH ist verworfen. Der aktive kleine Branch ist **smooth compensated**:

```text
rho_new(r) = rho_PREM(r) - M_BH w(r)
Integral 4 pi r^2 w(r) dr = 1.
```

Eine harte leere Ersatzkugel ist mechanisch verworfen. Drei verschiedene Skalen duerfen nicht verwechselt werden:

```text
r_s = 2 G M_BH / c^2
r_B = G M_BH / c_eff^2
M_PREM(<r_rep) = M_BH.
```

## Stand der Erdtests

Fuer den kleinen smooth H0-Zweig liefern die bisher ausgefuehrten reduzierten Tests keinen robusten Ausschluss durch

- Gesamtmasse / `GM`,
- Traegheitsmoment und Rotation,
- smooth PREM-Massenbuchhaltung,
- reduzierte Hydrostatik,
- vereinfachte Seismik/Normalmoden,
- Langzeitwaerme,
- den gestuften Akkretionsaudit aus Festigkeit, Yield, plastischem Supply, Rotation, Knudsen-Uebergang, Loss Cone und radiativem Feedback.

Das bedeutet **Kompatibilitaet innerhalb der getesteten Modelle**, nicht Evidenz fuer ein BH im Erdzentrum.

## Formation

Formation wurde separat getestet.

```text
In-situ-Kollaps normaler Erdmaterie: FAIL
spaeter direkter Earth-Capture: FAIL
Proto-Earth-/Planetesimal-Standardcapture: FAIL
normaler Halo -> kalte protoplanetare Scheibe: FAIL unter den getesteten Bedingungen
cold/co-moving Anfangsbedingung: mathematisch moeglich, Herkunftsmechanismus nicht hergeleitet
```

Formation ist damit der groesste negative Punkt des H0-Gesamtmodells.

## Endstatus Stage 3.68

| Bereich | H+ Standard-Hawking | H0 ohne Hawking |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleiner smooth Erdbranch | kein eigener Erdstruktur-Ausschluss | kein eigener Erdstruktur-Ausschluss |
| Super-K / Hawking-Neutrinos | **FAIL im Projekt-Reinterpretationstest** | nicht anwendbar |
| Akkretion / Waerme | gekoppelte H+-Probleme | exakte Rate OPEN; kein robuster Ausschluss im kleinen Branch |
| spaetere Earth-Capture-Formation | FAIL | FAIL |
| Standard-Formation/Delivery | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| positive eindeutige Signatur | keine | keine |

**Konservatives Fazit:**

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 als heutige versteckte Zentralmasse: OPEN / durch bisherige Erdtests nicht ausgeschlossen.
H0 fundamentale Begruendung fuer kein Hawking: OPEN.
H0 Formation: stark negativ / kein Standardweg gefunden.
Empirischer Nachweis: keiner.
```

## Was real noch fehlt

Zwei Endstufen liegen ausserhalb der abgeschlossenen Desk-Study-Testserie:

1. High-Fidelity-Multiphysik/HPC fuer die Near Zone plus 3-D-Full-Wave-Seismik.
2. Dedizierter experimenteller bzw. Real-Data-Test auf eine eindeutige H0-Signatur.

## Dateien

- [`FINAL_STATUS_STAGE3_68.md`](FINAL_STATUS_STAGE3_68.md) - vollstaendige Endmatrix und Schlussfolgerung.
- [`PUBLIC_UPDATE_V1_4.md`](PUBLIC_UPDATE_V1_4.md) - kurze oeffentliche Zusammenfassung.
- [`THEORIE.md`](THEORIE.md) - aktueller Theorierahmen.
- [`TEST_STATUS.md`](TEST_STATUS.md) - Test- und Falsifikationsmatrix.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) - numerischer Status und Aussagegrenzen.
- [`AKKRETION_STATUS.md`](AKKRETION_STATUS.md) - Akkretions-/Langzeitstatus.
- [`MASSENSCAN_STAGE3_15.md`](MASSENSCAN_STAGE3_15.md) - historischer Stage-3.15-Massenscan.
- [`SEISMIK_STAGE3_16_17.md`](SEISMIK_STAGE3_16_17.md) - historischer Seismik-Haertetest.
- [`CHANGELOG.md`](CHANGELOG.md) - Korrektur- und Versionshistorie.
- [`CITATION.cff`](CITATION.cff) - Zitiermetadaten.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` - unveraenderte Erstveroeffentlichung.

## Literatur-Kernreferenzen

- Dziewonski, A. M. & Anderson, D. L. (1981), *Preliminary Reference Earth Model*.
- Super-Kamiokande Collaboration, arXiv:2305.05135, Tabelle 2.
- Arbey & Auffinger, BlackHawk, arXiv:1905.04268; BlackHawk v3.0, arXiv:2606.06355.
- Cantiello et al. (2026), *Accretion of Primordial Black Holes in Stellar Interiors*, arXiv:2606.02726.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.4*, theoretischer Forschungsentwurf, Abschlussstand Stage 3.68, Rheinland-Pfalz, Deutschland.
