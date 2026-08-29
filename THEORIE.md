# SL/BH-Kernhypothese Erdmodul V1.5

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Stand:** 29.08.2026

**Forschungsstand:** Reduced Stack bis A31, Formation/Delivery bis F8a und Multi-Gate Closure bis Stage 3.94 bearbeitet; High-Fidelity Stage 3.69 und Experimental Stage 3.70 definiert, nicht durchgefuehrt

## 1. Gegenstand und Aussageebenen

Die definierende Hypothese des Erdmoduls lautet:

> Im Erdzentrum wird eine kleine zentrale kompakte Schwarzloch-Masse als theoretische Zusatzkomponente untersucht. Im aktiven Basismodell wird ihre Masse glatt gegen normale PREM-Masse bilanziert, so dass sie nicht zusaetzlich zur gemessenen Erdmasse addiert wird.

Es wird **keine direkte Detektion** eines Schwarzen Lochs im Erdzentrum behauptet.

Dieses Dokument trennt vier Aussageebenen:

| Ebene | Bedeutung im Erdmodul |
|---|---|
| Referenzphysik und externe Daten | Standard-GR, PREM-Referenzwerte und publizierte Messgrenzen werden als externe Grundlagen verwendet; sie werden durch dieses Projekt nicht neu bestaetigt. |
| Modellannahme | Zentralmasse, smooth compensation und insbesondere `P_Hawking=0` im H0-Zweig werden gesetzt und nicht aus den Rechnungen bewiesen. |
| Mathematisches/numerisches Ergebnis | Ein `PASS` gilt nur fuer die angegebene Gleichung, Parameterwahl, Randbedingung und Regression. |
| Spekulation / offene Physik | Physische Existenz, Entstehung, finales `Q_eq`, eindeutige H0-Signatur und experimenteller Nachweis bleiben offen, sofern nicht anders belegt. |

## 2. Abgrenzung der starken Variante

Im verwendeten PREM-/Traegheitsmoment-/Seismikvergleich ist eine Variante mit einem wesentlichen Anteil der Erdmasse im zentralen BH nicht vereinbar.

```text
starke Zentralmassenvariante: im Projektmodell verworfen.
```

Gegenstand der weiteren Tests ist nur ein kleiner zentraler Branch.

## 3. Zwei fundamentale Zweige

### H+

H+ verwendet die standardmaessige semiklassische Hawking-Vorhersage als Modellinput. Das Projekt liefert keinen eigenen experimentellen Nachweis der Hawking-Strahlung.

### H0

H0 setzt

```text
P_Hawking = 0.
```

H0 ist eine bewusst nichtstandardmaessige Modellannahme und kein etablierter GR/QFT-Zweig. Die Theorie dieses Erdmoduls liefert keine fundamentale Ableitung fuer das Ausbleiben der Hawking-Strahlung. Ein offener H0-Branch widerlegt daher weder die Hawking-Vorhersage noch Standard-GR/QFT.

## 4. Smooth-compensated Massenbuchhaltung

Das aktuelle Nullmodell ist PREM. Die BH-Masse wird durch eine glatte Funktion `w(r)` kompensiert:

```text
rho_new(r) = rho_PREM(r) - M_BH w(r)
Integral 4 pi r^2 w(r) dr = 1.
```

Damit bleibt die Gesamtmasse im ideal kugelsymmetrischen Buchhaltungsgrenzfall unveraendert.

Der historische Hard-Cavity-/Hard-Replacement-Branch ist innerhalb der bisherigen Projektpruefungen mechanisch verworfen.

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

Als Minimalrahmen der reduzierten Tests wird Standard-GR ausserhalb des Horizonts plus eine zentrale kompakte Masse und die smooth-compensated Materieverteilung verwendet. Fruehere Skalar-Tensor-Erweiterungen bleiben als Modellvarianten archiviert, sind aber fuer die hier dokumentierten reduzierten Aussagen nicht erforderlich.

## 7. H+ und Hawking-Neutrinos

Nach Korrektur der Hawking-Normierung liegt der relevante H+-Bereich des Projekts bei etwa

```text
M_BH = 4.82e11 ... 5.49e11 kg
T_H  = 21.99 ... 19.31 MeV.
```

Ein projektinterner Greybody-Primaerneutrino-Proxy wurde gegen publizierte spektrumsunabhaengige Super-Kamiokande-`anti-nu_e`-Grenzen verglichen.

Im Energieband 25.29-31.29 MeV:

```text
Projekt-H+ Primaerfluss: ~0.098 ... 0.122 cm^-2 s^-1 MeV^-1
SK-IV beobachtetes 90%-CL-Limit: 0.04 cm^-2 s^-1 MeV^-1
```

Daraus folgt innerhalb der verwendeten H+-Annahmen:

```text
getesteter H+-Greybody/Super-K-Parameterbranch: FAIL im Projektvergleich.
```

Dies ist eine Projekt-Reinterpretation und keine offizielle Super-Kamiokande-Suche nach einem Erdzentrum-BH. Das Ergebnis verwirft nur den getesteten H+-Parameterbranch innerhalb der verwendeten Emissions-, Greybody- und Vergleichsannahmen; es widerlegt die Hawking-Strahlung nicht allgemein.

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

Keiner dieser reduzierten Tests liefert derzeit innerhalb seiner Annahmen eine robuste vollstaendige Akkretionssperre. Daraus folgt nicht, dass die reale Akkretion mit einer der berechneten Raten stattfindet. Die exakte nichtstationaere MeV-Mikrophysik bleibt offen.

Seit Stage 3.68E wird zusaetzlich festgehalten, dass Bondi/Michel nicht automatisch bis zur Horizontabsorption extrapoliert werden duerfen. Bei `M~1e11 kg` liegt `r_s~1.5e-16 m`; deshalb ist ein separater **Quantum/Wave-Capture**-Block erforderlich, falls relevante Teilchenwellenlaengen bzw. Streuskalen den geometrisch-optischen Grenzfall nicht rechtfertigen.

```text
Bondi/Michel = aeusserer Supply-Benchmark
Quantum/Wave-Capture = offene innere Absorptionsphysik
finale Netto-Mdot = OPEN bis zur Kopplung in Stage 3.69
```

## 9. H0-Langzeit- und Waermevertraeglichkeit

Fuer den kleinen H0-Zweig fuehren die getesteten Michel-Skalierungen ueber ein Erdalter zu sehr kleinen globalen Massenanteilen. In der verwendeten Parameterisierung bleiben auch konservativ angesetzte Energieproxies klein gegen die globale Erdwaerme-Referenz.

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

Im smooth-compensated Branch ist die aeussere eingeschlossene Masse durch die Modellkonstruktion nahezu PREM-identisch. Bei `M~1e11 kg` ist die Bondi-/Kompressionsskala nur Groessenordnung `~61 nm`, waehrend der Buchhaltungsradius Groessenordnung `~100 m` besitzt.

Daraus folgt, dass starke lokale Materialaenderungen nicht ueber die ganze `~100 m`-Zone angenommen werden duerfen. Fruehere Millisekunden-Proxies, die die gesamte Buchhaltungszone als stark veraendert behandelten, wurden entsprechend abgeschaerft.

Externes Fachfeedback aus globaler Seismologie stuetzt die qualitative Einschaetzung, dass eine reine Nano-/Mikrometer-Near-Zone nicht direkt seismisch raeumlich aufloesbar ist; dies ist keine H0-Detektion oder -Validierung. Seismik wird fuer Stage 3.70 deshalb nur dann als aussichtsreicher Kanal behandelt, wenn Stage 3.69 eine **makroskopisch gekoppelte** `Delta rho`, `Delta V_P`, `Delta V_S`-Struktur oder eine koharente Normalmoden-/Streusignatur oberhalb realer Datenempfindlichkeit erzeugt.

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

Ein bereits extrem kalter und co-moving Zustand kann als spekulative Anfangsbedingung gesetzt werden. Ein hergeleiteter Standardmechanismus, der einen normalen collisionless PBH in diesen engen Phasenraum bringt, wurde im Projekt nicht gefunden.

```text
OPEN als gesetzte Anfangsbedingung; physischer Formationmechanismus nicht hergeleitet.
```

## 12. Stage 3.94 – reduzierte Multi-Gate Closure

Stage 3.94 behandelt drei mathematisch/numerisch getrennte Bloecke. Die Stufenbezeichnung ist ein Projektlabel und bedeutet nicht, dass die High-Fidelity-Stages 3.69 und 3.70 ausgefuehrt wurden.

| Gate | Modellannahme | Rechnungsergebnis | Offene Physik |
|---|---|---|---|
| F12 | Poisson-Seedzahl und definierte Amplifikations-Proxies | Proxy-Arithmetik und Sweep **PASS** | keine hergeleitete Abbildung auf ein physikalisches `P_zeta(k)` oder echtes `f_NL` |
| A34 | stationaere Ein-Spezies-Drift-Diffusion mit vorgegebenem `D`, `T`, `c_inf` und Randwerten | Profil, ODE-Residuum und radiale Flusserhaltung **PASS** | reales Speziesgemisch, Ladungsrueckkopplung und finales `Q_eq` **OPEN** |
| H0 | frei angesetztes, massenkompensiertes Dichteprofil | Massenkompensation und Laufzeit-Sensitivitaetsproxy **PASS** | eindeutige `Delta rho`, `Delta V_P`, `Delta V_S`-Vorhersage und direkte Detektion **OPEN** |

Insbesondere gilt:

```text
F12 PASS != physikalische Primordial-Closure
A34 PASS != finale Akkretionsrate oder elektrisches Q_eq
H0  PASS != eindeutige Seismikvorhersage oder Detektion
```

Keines dieser drei reduzierten Ergebnisse ist experimentelle Evidenz fuer ein Schwarzes Loch im Erdzentrum.

## 13. Endstatus

```text
H+ Greybody/Super-K-Projektbranch:
    FAIL im getesteten projektinternen Reinterpretationsmodell;
    keine allgemeine Widerlegung der Hawking-Strahlung.

H0 heutige versteckte Zentralmasse:
    OPEN / in den bisherigen reduzierten Erdtests weder nachgewiesen
    noch durch einen eindeutigen H0-Test ausgeschlossen.

H0 fundamentale Grundlage fuer P_Hawking=0:
    OPEN / nicht geliefert.

H0 Formation:
    OPEN; alle bisher getesteten Standard-Delivery-Pfade im Projektmodell FAIL.

F12 physikalische Primordial-Closure:
    OPEN; bisher nur Proxy-Arithmetik.

A34 reduzierte Ein-Spezies-Mathematik:
    PASS fuer ODE, Randbedingungen und Flusserhaltung.

A34 finales multikomponentiges Q_eq:
    OPEN.

H0 eindeutige seismische Vorhersage:
    OPEN; bisher nur kompensierter Sensitivitaetsproxy.

Empirischer Nachweis:
    keiner.
```

## 14. Aussagegrenze

Die korrekte wissenschaftliche Aussage lautet nicht „die Theorie ist bewiesen“ und nicht „alle Tests bestanden“.

Die korrekte Aussage lautet:

> Der getestete H+-Parameterbranch scheitert in der projektinternen Greybody/Super-K-Reinterpretation; dies ist keine allgemeine Widerlegung der Hawking-Strahlung. Fuer den nichtstandardmaessigen H0-Zweig liefern die bisherigen reduzierten Erdtests weder einen eindeutigen Ausschluss noch eine positive Detektion. H0 besitzt keine fundamentale Ableitung fuer `P_Hawking=0` und keinen hergeleiteten Standard-Formationweg. F12 bleibt Proxy-Arithmetik, A34 bleibt trotz mathematischer Ein-Spezies-Closure ohne finales `Q_eq`, und H0 besitzt noch keine eindeutige seismische Vorhersage. Eine experimentelle BH-Evidenz folgt aus keinem dieser Resultate.

## 15. Verbleibende Endstufen – formal definiert

**Stage 3.69 – High-Fidelity Multiphysics: DEFINED / NOT PERFORMED.** Verschachtelte PREM/Elastoplastik/Mikro-Hydro/kinetische-GR/Quantum-Wave-Capture/GR-Horizon-Sink-Architektur mit expliziten Transport-, QED-/Pair-/Nuklear-Zeitskalen.

**Stage 3.70 – Experimental H0 Falsification: DEFINED / NOT PERFORMED.** Dedizierter Real-Data-/Likelihood-Test einer quantitativen H0-Signatur, die erst aus Stage 3.69 stammen darf. Seismik ist nur bei einer makroskopisch gekoppelten Signatur ein aussichtsreicher Kanal.

Stage 3.94 ist der letzte bearbeitete numerische Reduktionsstand. Die dortigen F12-, A34- und H0-Ergebnisse sind Solver-/Proxyresultate und keine neue experimentelle Validierung. Stage 3.69 und 3.70 bleiben fuer die High-Fidelity-Kopplung bzw. einen Real-Data-Likelihood-Test offen.

Details: [`VALIDATION_PROTOCOL_STAGE3_69_70.md`](VALIDATION_PROTOCOL_STAGE3_69_70.md), [`EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md`](EXTERNAL_FEEDBACK_INTEGRATION_STAGE3_68E.md) und [`FINAL_STATUS_STAGE3_68.md`](FINAL_STATUS_STAGE3_68.md).
