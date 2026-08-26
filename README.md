# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; Stage 3.69A/3.69A-1 und Stage 3.69A-3 Quantum/Wave-Capture-Teilmodule numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 offen  
**Stand:** 26.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Archivhinweis:** `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs- und Prioritätsnachweis erhalten. Der aktuelle Forschungsstand wird in den Markdown-Dateien und reproduzierbaren Python-Skripten dokumentiert.

## Wissenschaftlicher Status

Die SL/BH-Kernhypothese Erdmodul ist ein **theoretischer Forschungsentwurf, kein experimenteller Nachweis**. Untersucht wird, ob ein kleiner zentraler BH-Branch mit bekannten Erdbeobachtungen und etablierter GR/Teilchen-/Materiephysik konsistent modelliert werden kann.

Der aktuelle Stand trennt zwei Branches strikt:

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben parallel erhalten. Gemeinsame Capture-/Materietests werden fuer beide verwendet; Hawking-spezifische Emissionstests gelten nur fuer H+.

## H+ – Standard-Hawking

Nach korrigierter Hawking-Normierung und Greybody-/Neutrino-Haertung liegt der relevante Projektbereich im getesteten Modell bei ungefaehr

```text
M_BH = 4.82e11 ... 5.49e11 kg
T_H  = 21.99 ... 19.31 MeV.
```

Der konservative Projektfluss im SK-IV-Band `25.29-31.29 MeV` liegt ueber dem verwendeten publizierten spektrumsunabhaengigen beobachteten 90%-CL-Grenzwert.

```text
H+ Standard-Hawking: FAIL im getesteten Projekt-Reinterpretationsmodell.
```

Dies ist eine Projekt-Reinterpretation eines Super-Kamiokande-Limits, keine offizielle Super-K-Erdzentrum-BH-Analyse.

## H0 – ohne Hawking

H0 setzt als nichtstandardmaessige Gegenhypothese

```text
P_Hawking = 0.
```

Hawking-basierte Neutrino-/Gamma-Grenzen sind fuer H0 definitionsgemaess nicht anwendbar. H0 bleibt jedoch voll an Akkretion, Ladungsfeedback, Dense-Matter-Transport, Langzeitstabilitaet, Formation und direkte Beobachtungen gebunden.

```text
H0: OPEN / nicht nachgewiesen.
```

## Aktiver Erdbranch

Die starke Variante mit einem wesentlichen Anteil der Erdmasse im zentralen BH ist verworfen. Der aktive kleine Branch ist `smooth compensated`:

```text
rho_new(r) = rho_PREM(r) - M_BH w(r)
Integral 4 pi r^2 w(r) dr = 1.
```

Eine harte leere Ersatzkugel ist mechanisch verworfen. Drei Skalen werden getrennt behandelt:

```text
r_s = 2 G M_BH / c^2
r_B = G M_BH / c_eff^2
M_PREM(<r_rep) = M_BH.
```

Fuer den zentralen PREM-Supply-Proxy:

```text
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s.
```

Bei `M_BH~1e11 kg` folgt `r_B~61 nm`.

## Bisherige Erdtests

Der kleine smooth Branch liefert in den bisher ausgefuehrten reduzierten Modellen keinen robusten Ausschluss durch

- Gesamtmasse / `GM`,
- Traegheitsmoment und Rotation,
- smooth PREM-Massenbuchhaltung,
- reduzierte Hydrostatik,
- vereinfachte Seismik/Normalmoden,
- globale Langzeitwaerme-Proxies,
- Yield/plastischen Supply,
- Knudsen-/kinetische Uebergaenge,
- Loss-Cone-/Recycling-Proxies.

Das bedeutet **Kompatibilitaet innerhalb der getesteten Modelle**, nicht Evidenz fuer ein BH im Erdzentrum.

## Stage 3.69A-1 – Schwarzschild-Dirac-Capture

Implementiert sind

```text
massive Schwarzschild-Dirac radial equation
regular horizon branch
conserved-current/Wronskian diagnostics
asymptotic in/out partial-wave matching
```

Der Solver reproduziert externe Low-`alpha`-Benchmarks und die qualitative Doran-Struktur aus Wellenoszillationen um den klassischen Capture-Wert.

Beispiel `alpha=0.2`:

```text
E/m=1.5: sigma/M^2 ~123.259  (classical ~128.680)
E/m=2.0: sigma/M^2 ~103.965  (classical ~103.380)
E/m=5.0: sigma/M^2 ~89.682   (classical ~87.174)
```

Details: [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md).

## Stage 3.69A-3 – Earth-speed Proton Dirac Capture

Der entscheidende neue Protonentest verwendet direkt

```text
v = 10.4355 km/s
u = 3.4809081e-5
```

und den vollen Dirac-Matcher statt einer Extrapolation der analytischen Unruh-Low-Energy-Naeherung.

Zur Stabilisierung sehr schwacher Partialwellen wird die Absorption zusaetzlich direkt aus dem konservierten eingehenden/Horizon-Fluss bestimmt:

```text
P_abs = (-W_H)/(2 q |A_in|^2),
q = p/(E+m), W_H=-1.
```

### Protonen-Massenscan

| `M_BH` | `alpha_p` | `kmax` | `sigma_Dirac/sigma_classical` | `sigma_Dirac` [m^2] |
|---:|---:|---:|---:|---:|
| `1e10 kg` | `0.0353107` | 3 | `0.0326735` | `7.47496e-26` |
| `1e11 kg` | `0.353107` | 3 | `0.950295` | `2.17406e-22` |
| `2e11 kg` | `0.706215` | 5 | `1.008071` | `9.22496e-22` |
| `5e11 kg` | `1.76554` | 9 | `0.996621` | `5.70011e-21` |

Am wichtigen `1e11 kg`-Referenzpunkt ergibt der volle Dirac-Lauf damit

```text
sigma_p ~2.1741e-22 m^2
        ~0.9503 sigma_classical.
```

Der fruehere Unruh-Low-Energy-Protonenwert

```text
~6.3447e-23 m^2
```

bleibt als asymptotischer Benchmark dokumentiert, wird bei `alpha_p~0.353` aber nicht mehr als finaler Earth-speed Protonenwert verwendet.

Details: [`STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md`](STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md).

## Stage 3.69A-3 – Charge Feedback

Bei `M_BH=1e11 kg` erzeugt bereits eine Elementarladung folgende Kraftverhaeltnisse:

```text
|F_C/F_G| proton   = 0.0206661
|F_C/F_G| electron = 37.9461.
```

Klassische Kraftgrenzen:

```text
Q_max,p   = +48.3884 e
|Q_max,e| =   0.026353 e.
```

Stationaerer Equal-T-Plasma-Benchmark nach Zajacek et al.:

```text
Q_eq ~ +24.1810 e
     ~ 3.87423e-18 C.
```

Zum Vergleich:

```text
Q_extremal,RN ~8.6175 C
Q_eq/Q_extremal ~4.50e-19.
```

Damit kann Ladungsfeedback die Teilchendynamik stark veraendern, waehrend die Raumzeit auf diesen Skalen praktisch Schwarzschild bleibt.

Diese Charge-Werte sind **keine** selbstkonsistente Erdkerngleichgewichtsloesung. Dense Fe/Ni-Screening, Kollisionen, Degeneration, Ionisation und Transport bleiben offen.

## Was Stage 3.69A-3 veraendert

```text
Earth-speed neutral proton Dirac capture: CALCULATED
Proton mass scan 1e10...5e11 kg: CALCULATED
flux-stable weak partial-wave extraction: IMPLEMENTED
Unruh proton extrapolation at alpha~0.35: REPLACED by full Dirac result
charge force scales: CALCULATED
stationary equal-T plasma charge benchmark: CALCULATED
charged Dirac sigma_p,e(Q): OPEN
Dense Fe/Ni charge/screening closure: OPEN
species-resolved net Mdot: OPEN
```

Insbesondere zeigt der `1e11 kg`-Punkt **keine starke Protonen-Wellenunterdrueckung**; die entscheidende Akkretionsunsicherheit verschiebt sich damit auf Ladungsfeedback, Screening, Fe/Ni-Zustand, Transport und Reaktionsclosure.

## Formation

Die bisher getesteten Standardwege sind stark negativ:

```text
In-situ-Kollaps normaler Erdmaterie: FAIL
spaeter direkter Earth-Capture: FAIL
Proto-Earth-/Planetesimal-Standardcapture: FAIL
normaler Halo -> kalte protoplanetare Scheibe: FAIL unter getesteten Bedingungen
cold/co-moving Anfangsbedingung: mathematisch moeglich, Herkunft nicht hergeleitet
```

Formation bleibt einer der groessten negativen Punkte des Gesamtmodells.

## Aktuelle Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleiner smooth Erdbranch | kein eigener Erdstruktur-Ausschluss | kein eigener Erdstruktur-Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL im getesteten Projektmodell** | nicht anwendbar |
| neutraler Earth-speed Proton Dirac Capture | CALCULATED | CALCULATED |
| Charge-Feedback-Kraftskalen | CALCULATED | CALCULATED |
| charged Dirac `sigma_p,e(Q)` | OPEN | OPEN |
| Dense Fe/Ni-Netto-Akkretion | OPEN | OPEN |
| Seismik | kein positiver Nachweis | kein positiver Nachweis |
| Standard-Formation/Delivery | stark negativ | stark negativ |
| direkte Detektion | keine | keine |
| positive eindeutige Signatur | keine | keine |

## Naechste Schritte

```text
Stage 3.69A-4:
charged Dirac capture + self-consistent Q(t)
```

anschliessend

```text
Dense Fe/Ni state + screening + transport
 -> coherent/composite or dissociated capture
 -> charge/nuclear feedback
 -> species-resolved net Mdot_BH
```

Erst danach kann Stage 3.69 Full-Multiphysics eine belastbare Endvorhersage fuer Stage 3.70 liefern.

## Zentrale Dateien

- [`STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md`](STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md) - aktueller Earth-speed Proton-/Charge-Block.
- [`stage3_69a3_earth_proton_charge.py`](stage3_69a3_earth_proton_charge.py) - reproduzierbarer Stage-3.69A-3-Scan.
- [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md) - Schwarzschild-Dirac-Solver und Benchmarks.
- [`stage3_69a1_dirac_prototype.py`](stage3_69a1_dirac_prototype.py) - Basis-Solver.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) - aktueller numerischer Status.
- [`TEST_STATUS.md`](TEST_STATUS.md) - Test- und Falsifikationsmatrix.
- [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md) - verbleibende Full-Stack-/Experimentprotokolle.
- [`THEORIE.md`](THEORIE.md) - Theorierahmen.
- [`CHANGELOG.md`](CHANGELOG.md) - Versionshistorie.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` - unveraenderte Erstveroeffentlichung.

## Literatur-Kernreferenzen

- Dziewonski, A. M. & Anderson, D. L. (1981), *Preliminary Reference Earth Model*.
- Doran, C., Lasenby, A., Dolan, S. & Hinder, I. (2005), *Fermion absorption cross section of a Schwarzschild black hole*, arXiv:gr-qc/0503019.
- Dolan, S., Doran, C. & Lasenby, A. (2006), *Fermion scattering by a Schwarzschild black hole*, arXiv:gr-qc/0605031.
- Unruh, W. G. (1976), *Absorption cross section of small black holes*.
- Zajaček, M. et al. (2018), *On the charge of the Galactic centre black hole*, MNRAS 480, 4408-4423.
- Nakao, K. et al. (2024), *Electrification of a non-rotating black hole*, arXiv:2409.17639.
- Super-Kamiokande Collaboration, arXiv:2305.05135, Tabelle 2.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.5*, theoretischer Forschungsentwurf; aktueller numerischer Stand bis Stage 3.69A-3, Stage 3.69 Full-Multiphysics und Stage 3.70 offen, Rheinland-Pfalz, Deutschland.
