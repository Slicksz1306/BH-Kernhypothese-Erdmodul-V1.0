# SL/BH-Kernhypothese Erdmodul V1.5

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Stand:** 26.08.2026  
**Forschungsstand:** Stage 3.68 bearbeitet; Stage 3.68E externes Fachfeedback integriert; Stage 3.69/3.70 definiert, nicht durchgefuehrt

## 1. Gegenstand

Die definierende Hypothese des Erdmoduls lautet:

> Im Erdzentrum wird eine kleine zentrale kompakte Schwarzloch-Masse als theoretische Zusatzkomponente untersucht. Im aktiven Basismodell wird ihre Masse glatt gegen normale PREM-Masse bilanziert, so dass sie nicht zusaetzlich zur gemessenen Erdmasse addiert wird.

Es wird **keine direkte Detektion** eines Schwarzen Lochs im Erdzentrum behauptet.

## 2. Abgrenzung der starken Variante

Eine Variante mit einem wesentlichen Anteil der Erdmasse im zentralen BH ist mit der beobachteten radialen Erdstruktur, dem Traegheitsmoment und der Seismologie nicht vereinbar.

```text
starke Zentralmassenvariante: verworfen.
```

Gegenstand der weiteren Tests ist nur ein kleiner zentraler Branch.

## 3. Zwei fundamentale Zweige

### H+

H+ nimmt Standard-Hawking-Strahlung an.

### H0

H0 setzt

```text
P_Hawking = 0.
```

H0 ist eine bewusst nichtstandardmaessige Gegenhypothese und kein etablierter GR/QFT-Zweig. Die Theorie dieses Erdmoduls liefert keine fundamentale Ableitung fuer das Ausbleiben der Hawking-Strahlung.

## 4. Smooth-compensated Massenbuchhaltung

Das aktuelle Nullmodell ist PREM. Die BH-Masse wird durch eine glatte Funktion `w(r)` kompensiert:

```text
rho_new(r) = rho_PREM(r) - M_BH w(r)
Integral 4 pi r^2 w(r) dr = 1.
```

Damit bleibt die Gesamtmasse im ideal kugelsymmetrischen Buchhaltungsgrenzfall unveraendert.

Der historische Hard-Cavity-/Hard-Replacement-Branch ist mechanisch verworfen.

## 5. Drei verschiedene Radien und expliziter Sound-Speed-Proxy

```text
r_s = 2 G M_BH / c^2
r_B = G M_BH / c_eff^2
M_PREM(<r_rep) = M_BH
```

Es gilt ausdruecklich

```text
r_s != r_B != r_rep.
```

`r_rep` ist nur eine Massenbuchhaltungs-/Groessenskala, keine physische Vakuumgrenze.

Fuer den zentralen PREM-Supply-Proxy werden

```text
rho_c = 13.0885 g/cm^3
V_P   = 11.2622 km/s
V_S   = 3.6678 km/s
```

verwendet. Daraus folgt

```text
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s
      ~ 10.44 km/s.
```

Damit liegt bei `M_BH~1e11 kg` die Bondi-Skala bei Groessenordnung `~61 nm`. Dieser `c_eff`-Wert ist ein aeusserer PREM-/Supply-Proxy, keine mikroskopische Dispersionsrelation der tiefsten Capture-Zone.

## 6. Minimaler Gravitationsrahmen

Fuer die Endtests des kleinen Branches genuegt als Minimalrahmen Standard-GR ausserhalb des Horizonts plus eine zentrale kompakte Masse und die smooth-compensated Materieverteilung. Fruehere Skalar-Tensor-Erweiterungen bleiben als Modellvarianten archiviert, sind aber fuer die zentrale Stage-3.68-Aussage nicht erforderlich.

## 7. H+ und Hawking-Neutrinos

Nach Korrektur der Hawking-Normierung liegt der relevante H+-Bereich des Projekts bei etwa

```text
M_BH = 4.82e11 ... 5.49e11 kg
T_H  = 21.99 ... 19.31 MeV.
```

Ein Greybody-Primaerneutrino-Test wurde gegen publizierte spektrumsunabhaengige Super-Kamiokande-`anti-nu_e`-Grenzen verglichen.

Im Energieband 25.29-31.29 MeV:

```text
Projekt-H+ Primaerfluss: ~0.098 ... 0.122 cm^-2 s^-1 MeV^-1
SK-IV beobachtetes 90%-CL-Limit: 0.04 cm^-2 s^-1 MeV^-1
```

Daraus folgt innerhalb der verwendeten H+-Annahmen:

```text
H+ Standard-Hawking: FAIL.
```

Dies ist eine Projekt-Reinterpretation und keine offizielle Super-Kamiokande-Suche nach einem Erdzentrum-BH.

## 8. H0-Akkretion

Der relativistische Michel-Solver liefert im historischen `1e16 kg`-Benchmark fuer die getestete Dense-Matter-EOS

```text
Mdot_Michel ~147 ... 1460 kg/s.
```

Mit der verwendeten `M^2`-Skalierung entspricht dies bei `1e11 kg` ungefaehr

```text
Mdot ~1.47e-8 ... 1.46e-7 kg/s.
```

Die folgenden moeglichen Blockaden wurden als reduzierte Grenz-/Sensitivity-Tests untersucht:

- hcp-Fe-/Festkoerperfestigkeit,
- Yield und plastischer Flow,
- radialer Material-Supply,
- Rotation und Winkelimpulstransport,
- Kontinuum-/Knudsen-Uebergang,
- kinetische Capture-Cone,
- Loss-Cone-Recycling,
- reduzierter Reservoir-/Fokker-Planck-Closure,
- Bremsstrahlung, Strahlungsdruck und Pair-/QED-Sensitivitaet.

Keiner dieser reduzierten Tests liefert derzeit eine robuste vollstaendige Akkretionssperre. Die exakte nichtstationaere MeV-Mikrophysik bleibt jedoch offen.

Seit Stage 3.68E wird zusaetzlich festgehalten, dass Bondi/Michel nicht automatisch bis zur Horizontabsorption extrapoliert werden duerfen. Bei `M~1e11 kg` liegt `r_s~1.5e-16 m`; deshalb ist ein separater **Quantum/Wave-Capture**-Block erforderlich, falls relevante Teilchenwellenlaengen bzw. Streuskalen den geometrisch-optischen Grenzfall nicht rechtfertigen.

```text
Bondi/Michel = aeusserer Supply-Benchmark
Quantum/Wave-Capture = offene innere Absorptionsphysik
finale Netto-Mdot = OPEN bis zur Kopplung in Stage 3.69
```

## 9. H0-Langzeit- und Waermevertraeglichkeit

Fuer den kleinen H0-Zweig fuehren die getesteten Michel-Skalierungen ueber ein Erdalter zu sehr kleinen globalen Massenanteilen. Selbst sehr konservative lokale Energieobergrenzen bleiben gegen die gesamte Erdwaerme klein.

Ein zusaetzlicher globaler Sanity-Check verwendet `P_Earth ~47 +/- 2 TW`. Fuer

```text
P_heat = eta Mdot c^2
```

folgt bei `eta=1` eine maximale globale Vergleichsrate von ungefaehr

```text
Mdot_max ~1.65e4 kg/year.
```

Der obere bisherige Michel-Benchmark des kleinen Branches bei `5e11 kg` liegt bei ungefaehr `115 kg/year` bzw. `0.328 TW` fuer `eta=1`, also rund Faktor `143` unter dieser Vergleichsskala.

Daraus folgt nur:

```text
kein Ausschluss durch die getesteten globalen Massen-/Waermeproxies.
```

Es folgt nicht, dass die exakte Akkretionsrate gemessen oder bewiesen waere. Lokale Energiepartition und reale Effizienz `eta` bleiben Stage-3.69-Outputs.

## 10. Erdstruktur und Seismik

Im smooth-compensated Branch ist die aeussere eingeschlossene Masse nahezu PREM-identisch. Bei `M~1e11 kg` ist die Bondi-/Kompressionsskala nur Groessenordnung `~61 nm`, waehrend der Buchhaltungsradius Groessenordnung `~100 m` besitzt.

Daraus folgt, dass starke lokale Materialaenderungen nicht ueber die ganze `~100 m`-Zone angenommen werden duerfen. Fruehere Millisekunden-Proxies, die die gesamte Buchhaltungszone als stark veraendert behandelten, wurden entsprechend abgeschaerft.

Externes Fachfeedback aus globaler Seismologie bestaerkt die bereits interne Einschaetzung, dass eine reine Nano-/Mikrometer-Near-Zone nicht direkt seismisch raeumlich aufloesbar ist. Seismik wird fuer Stage 3.70 deshalb nur dann als aussichtsreicher Kanal behandelt, wenn Stage 3.69 eine **makroskopisch gekoppelte** `Delta rho`, `Delta V_P`, `Delta V_S`-Struktur oder eine koharente Normalmoden-/Streusignatur oberhalb realer Datenempfindlichkeit erzeugt.

Die bisher ausgefuehrten reduzierten Laufzeit-, Streu- und Normalmodenproxies liefern keinen robusten Ausschluss des kleinen smooth H0-Zweigs und auch keine positive Detektion.

## 11. Formation

### 11.1 In-situ-Kollaps

Normale Erdmaterie kollabiert unter Standard-GR nicht spontan zu einem `~1e10-1e11 kg`-BH.

```text
FAIL.
```

### 11.2 Spaeter Earth-Capture

Ein collisionless PBH verliert bei einem normalen Erddurchflug fuer den aktiven Massenbereich zu wenig Energie durch dynamische Reibung. Ein reduzierter PREM-/Chandrasekhar-Capture-Test verlangt fuer `~1e11 kg` hyperbolische Ueberschussgeschwindigkeiten im ungefaehren mm/s- bis cm/s-Bereich, waehrend normale astrophysikalische Populationen viele Groessenordnungen schneller sind.

```text
FAIL.
```

### 11.3 Proto-Earth / Planetesimal / Gas

Die getesteten Standardpfade liefern ebenfalls keine ausreichende Dissipation.

```text
FAIL unter den getesteten Standardbedingungen.
```

### 11.4 Cold/co-moving

Ein bereits extrem kalter und co-moving Zustand kann als Anfangsbedingung gesetzt werden. Ein Standardmechanismus, der einen normalen collisionless PBH in diesen engen Phasenraum bringt, wurde nicht gefunden.

```text
OPEN als gesetzte Anfangsbedingung; Formationmechanismus stark unmotiviert.
```

## 12. Endstatus

```text
H+ Standard-Hawking:
    FAIL im getesteten Greybody/Super-K-Reinterpretationsmodell.

H0 heutige versteckte Zentralmasse:
    OPEN / durch die bisherigen reduzierten Erdtests nicht ausgeschlossen.

H0 fundamentale Grundlage fuer P_Hawking=0:
    OPEN / nicht geliefert.

H0 Formation:
    stark negativ; kein getesteter Standard-Delivery-Pfad erfolgreich.

Empirischer Nachweis:
    keiner.
```

## 13. Aussagegrenze

Die korrekte wissenschaftliche Aussage lautet nicht „die Theorie ist bewiesen“ und nicht „alle Tests bestanden“.

Die korrekte Aussage lautet:

> Der Standard-Hawking-Zweig H+ faellt innerhalb des aktuellen Projektmodells. Ein nichtstandardmaessiger kleiner H0-Zweig kann in den bisherigen reduzierten heutigen Erdtests verborgen bleiben, besitzt aber keine positive Detektion, keine fundamentale Ableitung fuer das Ausbleiben der Hawking-Strahlung und keinen hergeleiteten Standard-Formationweg. Die finale H0-Akkretionsrate bleibt zudem offen, bis Supply, Kinetik und Quantum/Wave-Capture in Stage 3.69 gekoppelt wurden.

## 14. Verbleibende Endstufen – formal definiert

**Stage 3.69 – High-Fidelity Multiphysics: DEFINED / NOT PERFORMED.** Verschachtelte PREM/Elastoplastik/Mikro-Hydro/kinetische-GR/Quantum-Wave-Capture/GR-Horizon-Sink-Architektur mit expliziten Transport-, QED-/Pair-/Nuklear-Zeitskalen.

**Stage 3.70 – Experimental H0 Falsification: DEFINED / NOT PERFORMED.** Dedizierter Real-Data-/Likelihood-Test einer quantitativen H0-Signatur, die erst aus Stage 3.69 stammen darf. Seismik ist nur bei einer makroskopisch gekoppelten Signatur ein aussichtsreicher Kanal.

Der letzte tatsaechlich bearbeitete interne Teststand bleibt Stage 3.68. Stage 3.68E dokumentiert die Integration externen Fachfeedbacks und ist keine neue experimentelle Validierung.

Details: [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md), [`EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`](EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md) und [`FINAL_STATUS_STAGE3_68.md`](FINAL_STATUS_STAGE3_68.md).
