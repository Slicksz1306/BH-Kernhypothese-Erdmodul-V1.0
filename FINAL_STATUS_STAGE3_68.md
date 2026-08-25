# SL/BH-Kernhypothese Erdmodul V1.4 - Stage 3.68 Abschlussstatus

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Stand:** 25.08.2026  
**Forschungsstand:** Stage 3.68

## 1. Zweck dieses Dokuments

Dieses Dokument konsolidiert die Testserie des Erdmoduls bis Stage 3.68. Es ersetzt widerspruechliche Zwischenformulierungen durch einen konservativen Endstatus.

Die Hypothese ist **nicht experimentell bestaetigt**. Es gibt keine direkte Detektion eines Schwarzen Lochs im Erdzentrum.

## 2. Zwei strikt getrennte Zweige

### H+ - Standard-Hawking

H+ nimmt die uebliche semiklassische Hawking-Strahlung eines Schwarzschild-Schwarzen-Lochs an.

### H0 - kein Hawking

H0 setzt als nichtstandardmaessige Gegenhypothese

```text
P_Hawking = 0.
```

H0 ist damit **kein Standard-GR/QFT-Zweig**. Alle Hawking-basierten Teilchen- und Neutrinogrenzen sind fuer H0 definitionsgemaess nicht anwendbar; dafuer benoetigt H0 eine eigenstaendige fundamentale Begruendung, die dieses Erdmodul nicht liefert.

## 3. Minimaler Erdbranch

Der aktive kleine Erdbranch verwendet eine glatte redistributive Massenbuchhaltung. Eine zentrale kompakte Masse `M_BH` wird nicht zusaetzlich zur gemessenen Erdmasse addiert, sondern durch eine glatte Massenkompensation gegen PREM bilanziert.

```text
rho_new(r) = rho_PREM(r) - M_BH w(r)
Integral 4 pi r^2 w(r) dr = 1.
```

Der historische harte Ersatzkugel-/Kavitaetsbranch ist verworfen. `r_rep`, `r_B` und `r_s` sind unterschiedliche Skalen:

```text
r_s = 2 G M_BH / c^2
r_B = G M_BH / c_eff^2
M_PREM(<r_rep) = M_BH
```

## 4. H+ - entscheidender Hawking/Neutrino-Test

Nach Korrektur der Hawking-Normierung liegt der relevante Standard-Hawking-H+-Bereich des Projekts bei ungefaehr

```text
M_BH = 4.82e11 ... 5.49e11 kg
T_H  = 21.99 ... 19.31 MeV.
```

Mit einem Greybody-Hawking-Primarspektrum und konservativer Zuordnung von einem Sechstel des gesamten primaeren Neutrinoflusses zu `anti-nu_e` ergab der Projekt-Reinterpretationstest im SK-IV-Energieband 25.29-31.29 MeV eine vorhergesagte mittlere differentielle Flussdichte von etwa

```text
0.098 ... 0.122 cm^-2 s^-1 MeV^-1.
```

Der publizierte spektrumsunabhaengige beobachtete 90%-CL-SK-IV-Grenzwert in diesem Band betraegt

```text
0.04 cm^-2 s^-1 MeV^-1.
```

Damit gilt **innerhalb der angegebenen H+-Modellannahmen**:

```text
H+ / Standard-Hawking: FAIL.
```

Praezise Aussagegrenze: Dies ist eine **Projekt-Reinterpretation eines Super-Kamiokande-Limits**, keine offizielle Super-Kamiokande-Analyse eines hypothetischen Erdzentrum-BH.

Referenzen: Super-Kamiokande, arXiv:2305.05135, insbesondere Tabelle 2; BlackHawk, arXiv:1905.04268 und aktuelle BlackHawk-Weiterentwicklungen.

## 5. H0 - Akkretion und Langzeitentwicklung

Als Near-Zone-Supply-Benchmark wurde der relativistische Michel-Solver des Projekts verwendet. Fuer `M=1e16 kg` liefert die getestete phenomenologische Dense-Matter-EOS etwa

```text
Mdot_Michel = 147 ... 1460 kg/s.
```

Unter der fuer diesen Benchmark verwendeten `Mdot proportional M^2`-Skalierung ergibt sich bei `M=1e11 kg` ungefaehr

```text
Mdot = 1.47e-8 ... 1.46e-7 kg/s.
```

Die nachfolgenden H0-Haertetests untersuchten Festigkeit/Yield, plastischen Supply, Rotation, Knudsen-Uebergang, kinetischen Capture, Loss-Cone-Recycling sowie radiative/QED-Rueckkopplung.

Ergebnis:

- keine robuste statische Festkoerperbarriere gefunden;
- Rotation liefert im untersuchten Regime keinen robusten Michel-Blocker;
- eine naive einmalige Loss-Cone-Unterdrueckung ist nicht als Langzeitfaktor zulaessig, wenn Partikel kollisional recycelt werden;
- ein reduzierter Reservoir-/Fokker-Planck-Closure-Test erfordert nur lokale Dichteverstaerkung, nicht automatisch einen makroskopischen dauerhaften Stau;
- radiativer Eddington-Feedback liegt fuer die untersuchten kleinen Massen selbst bei extrem konservativer Energieobergrenze unter der fuer Fe-artiges Plasma relevanten Skala;
- die exakte MeV-Mikrophysik bleibt offen.

Eine 2026 veroeffentlichte Arbeit ueber sphaerische PBH-Akkretion in Sterninneren findet fuer kleine PBHs ein Hot-Bondi-Regime, in dem Bremsstrahlung die Akkretion nicht stoppt, sowie bei hoeheren Massen Kuehlungs- bzw. Photon-Trapping-Regime. Diese Arbeit ist wegen anderer Umgebung nicht quantitativ auf den Erdkern uebertragbar, spricht aber gegen eine generische radiative Akkretionssperre. Referenz: arXiv:2606.02726.

**H0-Akkretionsstatus:** exakte Rate OPEN; in den reduzierten Langzeit-/Waerme-Stresstests kein Ausschluss des kleinen H0-Zweigs.

## 6. Erdstruktur, Hydrostatik und Seismik

PREM bleibt das Nullmodell. Die starke Variante, bei der ein wesentlicher Anteil der Erdmasse zentralisiert wird, ist nicht mit beobachteter Erdstruktur vereinbar und gehoert nicht zum aktiven Zweig.

Fuer den kleinen smooth-compensated H0-Zweig gilt:

- ausserhalb der Kompensationszone ist die eingeschlossene Masse im idealen kugelsymmetrischen Grenzfall nahezu PREM-identisch;
- Oberflaechengravitation und `GM_Earth` liefern deshalb keinen brauchbaren positiven Nachweis;
- die relevante physische Kompressions-/Bondiskala bei `M~1e11 kg` liegt nur bei Groessenordnung `~60 nm`, waehrend der PREM-Buchhaltungsradius Groessenordnung `~100 m` besitzt;
- starke Materialaenderungen sind daher auf eine extrem kleine Near Zone konzentriert;
- vereinfachte Laufzeit- und Normalmoden-Proxies liefern keine derzeit messbare eindeutige Signatur.

**Status:** Der kleine smooth H0-Zweig ist durch die bisher ausgefuehrten reduzierten PREM-/Seismiktests nicht ausgeschlossen. Ein echter 3-D-Full-Wave-/Real-Data-Likelihood-Test wurde nicht durchgefuehrt.

PREM-Referenz: Dziewonski & Anderson (1981), Preliminary Reference Earth Model.

## 7. Formation

Formation wurde absichtlich getrennt von der Frage getestet, ob ein bereits vorhandenes kleines H0-BH heute mit der Erde kompatibel waere.

### In-situ-Kollaps

Normale Fe/Ni-Erdmaterie kann unter Standard-GR nicht spontan auf den Schwarzschildradius eines `~1e10-1e11 kg`-BH kollabieren.

```text
Status: FAIL.
```

### Spaeter direkter Earth-Capture

Dynamische Reibung waehrend eines einzelnen Erddurchflugs ist fuer den aktiven Massenbereich viel zu schwach. In einem PREM-/Chandrasekhar-basierten reduzierten Capture-Proxy muss ein `~1e11 kg`-PBH bereits eine hyperbolische Ueberschussgeschwindigkeit im ungefaehren mm/s- bis cm/s-Bereich besitzen, damit selbst ein optimaler Durchflug gebunden werden kann. Normale astrophysikalische Populationen liegen dagegen im km/s- bis 100-km/s-Bereich.

Gravitationswellenverluste sind fuer Earth-Capture in diesem Massenbereich vernachlaessigbar.

```text
Status: spaeter Earth-Capture FAIL.
```

### Proto-Earth / Planetesimal / Gasdrag

Die untersuchten Standardpfade ueber Proto-Earth-Capture, Planetesimal-Capture und protoplanetaren Gasdrag liefern keine ausreichende Dissipation fuer ein collisionless PBH im aktiven Massenbereich.

```text
Status: FAIL unter den getesteten Standardbedingungen.
```

### Cold/co-moving Anfangsbedingung

Ein PBH, das bereits aussergewoehnlich kalt, co-planar, co-rotierend und am richtigen Ort im terrestrischen Ausgangsmaterial liegt, kann als Anfangsbedingung gesetzt werden. Im Projekt wurde jedoch kein Standardmechanismus gefunden, der einen normalen collisionless Halo-PBH in diesen extrem kleinen Phasenraum bringt.

```text
Status: mathematisch moegliche Anfangsbedingung, physikalischer Herkunftsmechanismus OPEN / stark unmotiviert.
```

**Gesamt Formation:** Der getestete Standard-Formation-/Delivery-Stack ist der staerkste negative Punkt des H0-Gesamtmodells.

## 8. Endmatrix Stage 3.68

| Testblock | H+ Standard-Hawking | H0 ohne Hawking |
|---|---|---|
| starke Zentralmassenvariante | FAIL | FAIL |
| kleine smooth PREM-Massenbuchhaltung | kompatibel | kompatibel |
| Gravimetrie / `GM` / Rotation | kein positiver Nachweis | kein positiver Nachweis |
| reduzierte Hydrostatik / Near-Zone | kein eigener Ausschluss | kein eigener Ausschluss |
| vereinfachte Seismik / Normalmoden | kein eigener Ausschluss | kein eigener Ausschluss |
| Standard-Hawking-Neutrinos | **FAIL im Projekt-SK-IV-Reinterpretationstest** | nicht anwendbar |
| Langzeitakkretion / Waerme | H+-spezifische gekoppelte Entwicklung | kleiner H0-Zweig nicht ausgeschlossen; exakte Rate OPEN |
| QED/Pair/radiatives Feedback | keine Rettung des H+-Neutrinoproblems | kein robuster Akkretionsstopp gefunden |
| spaeter Earth-Capture | FAIL als Formation | FAIL als Formation |
| Proto-Earth/Planetesimal-Standardcapture | FAIL | FAIL |
| cold/co-moving Formation | kein Standardmechanismus gefunden | kein Standardmechanismus gefunden |
| direkte experimentelle Detektion | keine | keine |
| eindeutige positive Signatur | keine | keine |

## 9. Wissenschaftliches Endfazit

### H+

```text
Standard-Hawking H+: FAIL innerhalb des getesteten H+-Modells,
primaer wegen des SK-IV anti-nu_e-Reinterpretationstests.
```

### H0 als heutige Existenzhypothese

```text
Ein bereits vorhandenes kleines smooth-compensated H0-BH im Erdzentrum
ist durch die bisher ausgefuehrten reduzierten Erdstruktur-, Seismik-,
Waerme- und Akkretionsstresstests nicht ausgeschlossen.
```

Das ist **Kompatibilitaet, kein Nachweis**.

### H0 als vollstaendige Theorie

H0 benoetigt erstens nichtstandardmaessige fundamentale Physik zur Abschaltung der Hawking-Strahlung und zweitens einen glaubwuerdigen Formation-/Delivery-Mechanismus. Beide Punkte sind nicht geloest.

Daher lautet der konservative Gesamtstatus:

```text
H+ Standard-Hawking: FAIL im getesteten Modell.
H0 heutige versteckte Zentralmasse: OPEN / nicht durch die bisherigen Erdtests ausgeschlossen.
H0 fundamentale Begruendung: OPEN.
H0 Formation: stark negativ / kein Standardweg gefunden.
Empirischer Nachweis: keiner.
```

## 10. Zwei Tests ausserhalb des abgeschlossenen Desk-Study-Stacks

Zwei entscheidende Endstufen bleiben ausserhalb dessen, was diese Arbeit abschliessend leisten kann:

1. **High-Fidelity-Multiphysik:** gekoppelte relativistische Elastoplastik + Dense-Plasma/QED/Nuklearreaktionen + kinetischer Transport + Horizon-Capture, danach 3-D-Full-Wave-Seismik.
2. **Dedizierter experimenteller/Real-Data-Test:** eine speziell auf die verbleibende H0-Signatur optimierte Analyse realer Daten bzw. ein entsprechendes Experiment.

Bis dahin darf die Hypothese weder als bestaetigte Theorie noch als experimentell nachgewiesenes Erd-BH dargestellt werden.
