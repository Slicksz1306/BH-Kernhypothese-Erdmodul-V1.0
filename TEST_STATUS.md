# SL/BH-Kernhypothese Erdmodul - Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 26.08.2026  
**Theorie-Textstand:** Erdmodul V1.5  
**Aktueller Forschungsstand:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; Stage 3.69A/3.69A-1 und Stage 3.69A-3 Quantum/Wave-Capture-Teilmodule numerisch bearbeitet; Stage 3.69 Full-Multiphysics und Stage 3.70 nicht durchgefuehrt

## Statusbegriffe

- **PASS/kompatibel** = innerhalb des konkret benannten reduzierten Modells kein Widerspruch gefunden; kein empirischer Nachweis.
- **FAIL** = der konkret benannte Branch/Mechanismus widerspricht dem verwendeten Test oder kann die erforderliche Bedingung nicht erfuellen.
- **CALCULATED** = definierter Benchmark numerisch berechnet, ohne Aussage ueber die noch offene Full-Stack-Closure.
- **OPEN** = mit vorhandenen Gleichungen/Daten nicht abschliessend entschieden.
- **nicht anwendbar** = der Test setzt Physik voraus, die der jeweilige Branch definitionsgemaess nicht besitzt.
- **zurueckgezogen/korrigiert** = fruehere Zwischenaussage durch einen haerteren Test ersetzt.

Kein Status in dieser Datei ist eine direkte Detektion eines Erdzentrum-BH.

## 1. Branch-Definition

```text
H+ = mit Standard-Hawking-Strahlung
H0 = ohne Hawking-Strahlung
```

Beide Branches bleiben parallel dokumentiert. Gemeinsame Materie-/Capture-Tests werden nicht automatisch einem Branch zugerechnet; H+ besitzt zusaetzliche Hawking-Quellterme.

## 2. Strukturbranches

| Test | Status |
|---|---|
| starke Zentralmassenvariante | **FAIL** |
| Hard-Cavity/Hard-Replacement | **FAIL**, mechanisch verworfen |
| kleiner smooth-compensated Branch | mathematisch massenerhaltend; weiter getestet |
| Verwechslung `r_s=r_B=r_rep` | **FAIL**, drei getrennte Skalen |

## 3. H+ - Hawking/Greybody/Neutrinos

Stage 3.28 korrigierte die Hawking-Normierung. Der relevante H+-Bereich verschob sich auf etwa

```text
4.82e11 ... 5.49e11 kg.
```

Stage 3.30 verglich ein konservatives Greybody-Primaer-`anti-nu_e`-Signal mit publizierten spektrumsunabhaengigen SK-IV-Limits.

```text
25.29-31.29 MeV:
Projektfluss ~0.098 ... 0.122 cm^-2 s^-1 MeV^-1
SK-IV observed 90% CL = 0.04 cm^-2 s^-1 MeV^-1
```

```text
H+ Standard-Hawking: FAIL im Projekt-Reinterpretationstest.
```

Aussagegrenze: keine offizielle Super-K-Erdzentrum-BH-Exklusion.

## 4. Akkretion / Langzeit – gemeinsame und H0-relevante Tests

Fuer den zentralen PREM-Supply-Proxy:

```text
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s.
```

| Teiltest | Status |
|---|---|
| statische Festkoerperbarriere | kein robuster Blocker |
| Rotation/Winkelimpuls | kein robuster Blocker |
| radialer Supply | kein zwingender Engpass im getesteten Brueckenmodell |
| One-pass kinetic capture als permanenter Faktor | **zurueckgezogen** |
| Loss Cone / Recycling | eher full-loss-cone; exakte kinetische Loesung OPEN |
| Reservoir/Fokker-Planck-Closure | kein makroskopischer Stau zwingend erforderlich |
| radiativer Eddington-Stopp | kein robuster Stopp im getesteten Massenbereich |
| exakte MeV-Plasma/QED/Nuklearphysik | **OPEN** |
| Quantum/Wave-Capture Regimecheck | **DONE** |
| Schwarzschild-Dirac radial solver | **IMPLEMENTED** |
| Horizon/current self-check | **PASS als numerischer Solver-Selfcheck** |
| Dirac in/out matching | **IMPLEMENTED; Matchingradius-Benchmarks stabil** |
| Low-`alpha` externe Regression | **PASS** |
| Intermediate-`alpha` Doran-Struktur | **PASS qualitativ/numerisch** |
| Earth-speed neutral proton mass scan `1e10...5e11 kg` | **CALCULATED** |
| flux-stabile schwache Partialwellen-Auswertung | **IMPLEMENTED** |
| Charge-Feedback-Kraftskalen | **CALCULATED** |
| stationaerer Equal-T-Plasma-Chargebenchmark | **CALCULATED** |
| charged Dirac capture `sigma_p,e(Q)` | **OPEN** |
| coherent Fe/Ni scalar/composite capture | **OPEN** |
| Dense-Matter-Screening/Transport-Chargeclosure | **OPEN** |
| species-resolved dense-core net `Mdot` | **OPEN** |
| globaler 47-TW-Waerme-Sanity-Check | kein Ausschluss des getesteten kleinen Michel-Benchmarks |
| Erdalter-Masse/Waerme im kleinen Branch | kein Ausschluss in den reduzierten Stressproxies |

## 5. Stage 3.69A-1 – isolierter Schwarzschild-Dirac-Capture

Fuer `alpha=0.2`:

```text
E/m=1.5:
  x_match=500   -> sigma/M^2=123.2562
  x_match=1000  -> sigma/M^2=123.2594
  x_match=2000  -> sigma/M^2=123.2587

E/m=2.0:
  x_match=500   -> sigma/M^2=103.9639
  x_match=1000  -> sigma/M^2=103.9655
  x_match=2000  -> sigma/M^2=103.9650
```

Weitere Benchmarkstruktur:

```text
E/m=1.5: Dirac ~123.259, klassisch ~128.680
E/m=2.0: Dirac ~103.965, klassisch ~103.380
E/m=5.0: Dirac ~89.682, klassisch ~87.174
high-energy target: 27*pi ~84.823
```

Der Solver reproduziert die qualitative Doran-Struktur. Ein vollstaendiger punktweiser Kurvenregressionstest bleibt offen.

## 6. Stage 3.69A-3 – Earth-speed Proton Capture

Referenz:

```text
M_BH variable
v = 10.4355 km/s
u = 3.4809081e-5.
```

### 6.1 Flux-stabile Absorption

Fuer sehr schwache Partialwellen wird nicht nur

```text
P_abs = 1-|S|^2
```

verwendet, sondern aus dem konservierten Strom direkt

```text
P_abs = (-W_H)/(2 q |A_in|^2),
q=p/(E+m), W_H=-1.
```

Damit wird Catastrophic Cancellation bei `|S|~1` vermieden.

### 6.2 Protonen-Massenscan

| `M_BH` | `alpha_p` | `kmax` | `x_match` | `sigma_D/sigma_classical` | `sigma_D` [m^2] |
|---:|---:|---:|---:|---:|---:|
| `1e10 kg` | `0.0353107` | 3 | `5e6` | `0.0326735` | `7.47496e-26` |
| `1e11 kg` | `0.353107` | 3 | `5e6` | `0.950295` | `2.17406e-22` |
| `2e11 kg` | `0.706215` | 5 | `2e6` | `1.008071` | `9.22496e-22` |
| `5e11 kg` | `1.76554` | 9 | `1e6` | `0.996621` | `5.70011e-21` |

Partialwellenschnitt beim oberen Punkt:

```text
kmax=5 -> 0.6015 classical
kmax=6 -> 0.8420
kmax=7 -> 0.99630
kmax=8 -> 0.99662110
kmax=9 -> 0.99662113.
```

Matchingradius-Spotcheck `M=1e11 kg, kmax=3`:

```text
x_match=1e6 -> 0.95024543 classical
x_match=5e6 -> 0.95029487 classical
x_match=1e7 -> 0.95035969 classical.
```

### 6.3 Korrektur des frueheren Protonenbenchmarks

Die Unruh-Low-Energy-Naeherung lieferte bei `M=1e11 kg`

```text
sigma_Unruh,p ~6.3447e-23 m^2.
```

Der volle Dirac-Matcher liefert

```text
sigma_Dirac,p ~2.1741e-22 m^2
             ~0.9503 sigma_classical.
```

Damit ist die fruehere Unruh-Protonenextrapolation fuer `alpha_p~0.353` als finaler Earth-speed-Wert **ersetzt**, nicht der Unruh-Benchmark als solcher verworfen.

## 7. Stage 3.69A-3 – Charge Feedback

Bei `M_BH=1e11 kg` und einer Elementarladung:

```text
|F_C/F_G| proton   = 0.0206661
|F_C/F_G| electron = 37.9461.
```

Klassische Kraftgrenzen:

```text
Q_max,p   = +48.3884 e = 7.75268e-18 C
|Q_max,e| =   0.026353 e = 4.22224e-21 C.
```

Equal-T stationaerer Plasma-Benchmark nach Zajacek et al.:

```text
Q_eq ~ +24.1810 e = 3.87423e-18 C.
```

RN-Extremalladungsskala:

```text
Q_extremal ~8.6175 C
Q_eq/Q_extremal ~4.50e-19.
```

Interpretation:

- Die Metrik bleibt auf diesen Ladungsskalen praktisch Schwarzschild.
- Die Dynamik geladener Teilchen kann trotzdem stark veraendert werden.
- Die stationaere Zajacek-Formel ist **kein** Erdkerngleichgewicht; dichte Fe/Ni-Materie, Screening, Kollisionen und Transport fehlen.

## 8. Erdstruktur / Seismik

| Test | kleiner smooth Branch |
|---|---|
| Gesamtmasse / `GM` | kompatibel durch redistributive Buchhaltung |
| Traegheitsmoment / Rotation | Effekt im kleinen Branch extrem klein |
| reduzierte Hydrostatik | kein Ausschluss |
| starke gesamte `r_rep`-Zone | frueherer Proxy **korrigiert**; physische starke Zone liegt viel tiefer |
| Body-wave Timing Proxy | kein messbarer robuster Ausschluss |
| Normalmodenproxy | kein messbarer robuster Ausschluss |
| direkte Nano-/Mikrometer-Seismik | keine realistische raeumliche Aufloesung |
| echte 3-D-Full-Wave-Likelihood | **nicht durchgefuehrt; nur sinnvoll bei makroskopisch gekoppelter Signatur** |

## 9. Formation

| Mechanismus | Status |
|---|---|
| In-situ-Kollaps normaler Fe/Ni-Erdmaterie | **FAIL** |
| spaeter direkter Earth-Capture | **FAIL** |
| Proto-Earth-Capture | **FAIL** unter getesteten Bedingungen |
| Planetesimal-Capture | **FAIL** unter getesteten Bedingungen |
| protoplanetarer Gasdrag fuer PBH | **FAIL** als ausreichender Bremsmechanismus |
| Halo -> Protosternwolke -> kalte Scheibe -> SI/Pebble | **FAIL** unter Standardbedingungen |
| bereits cold/co-moving Anfangsbedingung | mathematisch moeglich, Herkunft **OPEN / stark unmotiviert** |

## 10. Endmatrix

| Bereich | H+ | H0 |
|---|---|---|
| starke Erd-SL-Variante | FAIL | FAIL |
| kleiner smooth PREM-Branch | kein eigener Erdstruktur-Ausschluss | kein eigener Erdstruktur-Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL im getesteten Projektmodell** | nicht anwendbar |
| neutraler Earth-speed Proton Dirac Capture | **CALCULATED**, gemeinsamer Materieblock | **CALCULATED**, gemeinsamer Materieblock |
| Charge-Feedback-Kraftskalen | **CALCULATED** | **CALCULATED** |
| charged Dirac `sigma_p,e(Q)` | OPEN | OPEN |
| Dense Fe/Ni-Netto-Akkretion | OPEN | OPEN |
| Seismik/Normalmoden reduziert | kein positiver Nachweis | kein positiver Nachweis |
| spaeter Earth-Capture | FAIL | FAIL |
| Standard-Formation/Delivery | stark negativ | stark negativ |
| direkte experimentelle Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## 11. Verbleibende Endstufen

- **Stage 3.69A-4:** charged Dirac capture + selbstkonsistentes `Q(t)`.
- **Stage 3.69 Full-Multiphysics:** Dense-Matter-Komposition, Screening, coherent Fe/Ni scalar/composite capture bzw. Dissociation, Transport/Reaktionen und species-resolved Netto-`Mdot`.
- **Stage 3.70:** dedizierte branch-spezifische Real-Data-/Experiment-Likelihood einer aus Stage 3.69 abgeleiteten Signatur.

## 12. Konservativer Schluss

```text
H+ Standard-Hawking: FAIL im getesteten Projekt-Reinterpretationsmodell; Branch bleibt separat erhalten.
H0 heutige Existenzhypothese: OPEN / durch bisherige reduzierte Erdtests nicht ausgeschlossen.
Neutraler Earth-speed Proton Dirac Capture: CALCULATED.
Bei M=1e11 kg liegt sigma_p bei ~0.9503 sigma_classical; keine starke Protonen-Wellenunterdrueckung.
Charge-feedback force/equilibrium scales: CALCULATED as benchmarks.
Charged capture + dense Fe/Ni charge/screening closure: OPEN.
Finale species-resolved Netto-Akkretionsrate: OPEN.
Formation: stark negativ / kein Standardweg gefunden.
Empirischer Nachweis: keiner.
```

Details:

- [`STAGE3_69A1_DIRAC_PROTOTYPE.md`](STAGE3_69A1_DIRAC_PROTOTYPE.md)
- [`STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md`](STAGE3_69A3_EARTH_PROTON_CHARGE_FEEDBACK.md)
- [`stage3_69a3_earth_proton_charge.py`](stage3_69a3_earth_proton_charge.py)
- [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md)
