# Stage 3.68E – Integration externen Fachfeedbacks

**Projekt:** SL/BH-Kernhypothese Erdmodul V1.5  
**Stand:** 26.08.2026  
**Status:** fachliche Rueckmeldungen ausgewertet; keine neue experimentelle Validierung

Diese Notiz dokumentiert technische Konsequenzen aus externem Fachfeedback zu Numerical Relativity/HPC und globaler Seismologie. Private Korrespondenz wird nicht woertlich veroeffentlicht. Die daraus uebernommenen Punkte werden nur als technische Modellkorrekturen dokumentiert.

## 1. Bondi-/Sound-Speed-Parameter explizit festgelegt

Die Bondi-Skala und Bondi-Rate haengen empfindlich von der verwendeten effektiven Schallgeschwindigkeit ab. Fuer den zentralen PREM-Proxy werden die PREM-Werte

```text
rho_c = 13.0885 g/cm^3
V_P   = 11.2622 km/s
V_S   = 3.6678 km/s
```

verwendet. Fuer den fluidartigen Bulk-Sound-Speed-Proxy gilt

```text
c_eff = sqrt(V_P^2 - 4/3 V_S^2)
      = 10.4355 km/s
      ~ 10.44 km/s.
```

Damit ist fuer `M_BH = 1e11 kg`

```text
r_B = G M_BH / c_eff^2 ~ 61 nm.
```

Aussagegrenze: `c_eff` ist ein PREM-basierter aeusserer Supply-Proxy. Er ist keine Aussage ueber die mikroskopische Dispersionsrelation in der tiefen kinetischen/quantum Capture-Zone.

## 2. Quantum-/Wave-Capture als neuer Pflichtblock fuer Stage 3.69

Der Schwarzschildradius eines `1e11 kg`-BH liegt bei ungefaehr

```text
r_s ~ 1.5e-16 m.
```

Damit darf klassisches Bondi-/Michel-Fluidverhalten nicht automatisch bis zum Horizont extrapoliert werden. Wenn Horizontskala und relevante de-Broglie-/Compton-/Streuskalen nicht im geometrisch-optischen Grenzfall liegen, ist die Absorption als Wellen-/Quantenproblem zu behandeln.

Die Stage-3.69-Hierarchie wird deshalb erweitert zu

```text
PREM global
 -> Elastoplastik/Rheologie
 -> Mikro-Hydrodynamik
 -> kinetische GR-Zone
 -> Quantum/Wave-Capture
 -> GR-Horizon-Sink / Capture-Randbedingung.
```

Bondi/Michel bleiben aeussere Supply-/Benchmarkmodelle. Die tatsaechliche Netto-Akkretionsrate darf erst nach Kopplung an die quanten-/wellenmechanische Absorption festgelegt werden.

Relevante Referenz fuer die grundsaetzliche Regimeabhaengigkeit: Doran, Lasenby, Dolan & Hinder (2005), *Fermion absorption cross section of a Schwarzschild black hole*, arXiv:gr-qc/0503019. Dort geht die Absorption im Grenzfall `r_s >> wavelength` gegen den klassischen Grenzfall, waehrend fuer kleine BH relativ zur Wellenlaenge quantenmechanische Absorptionsquerschnitte erforderlich sind.

## 3. Unabhaengiger globaler Waerme-Sanity-Check

Als konservative globale Vergleichsskala wird der gemessene terrestrische Oberflaechen-Waermefluss

```text
P_Earth ~ 47 +/- 2 TW
```

verwendet (Davies & Davies 2010).

Falls ein Anteil `eta` der akkretierbaren Ruheenergie als in der Erde verbleibende Waerme erscheint,

```text
P_heat = eta Mdot c^2,
```

folgt

```text
Mdot_max = P_Earth / (eta c^2).
```

Fuer `eta=1`:

```text
Mdot_max ~ 5.23e-4 kg/s
         ~ 1.65e4 kg/year.
```

Der obere bisherige Michel-Benchmark des kleinen Branches bei `M_BH=5e11 kg` ist

```text
Mdot ~ 3.65e-6 kg/s
     ~ 115 kg/year
P_heat(eta=1) ~ 0.328 TW.
```

Damit liegt selbst dieser extreme `eta=1`-Benchmark um etwa Faktor `143` unter der globalen 47-TW-Vergleichsskala.

```text
47-TW global heat sanity check:
    kein Ausschluss des getesteten kleinen H0-Michel-Benchmarks.
```

Wichtig: Diese Rechnung ist nur ein globaler Energie-Sanity-Check. Lokale Temperaturfelder, Transportwege, Neutrinoverluste, Strahlungs-/Teilchenemission und die tatsaechliche Effizienz `eta` muessen in Stage 3.69 selbstkonsistent berechnet werden. Kleinere `eta` lockern die globale Massenraten-Obergrenze proportional zu `1/eta`.

## 4. Seismik-Kanal fuer Stage 3.70 herabgestuft

Eine physisch stark gestoerte Near Zone auf Nano-/Mikrometerskalen ist nicht direkt raeumlich durch globale Seismologie aufloesbar. Deshalb wird ein 3-D-Full-Wave-Seismiktest nur dann als aussichtsreicher Stage-3.70-Kanal behandelt, wenn Stage 3.69 eine **makroskopisch gekoppelte** Struktur erzeugt, zum Beispiel

```text
Delta rho(r), Delta V_P(r), Delta V_S(r)
```

auf ausreichend grossen Skalen oder eine koharente Normalmoden-/Streusignatur oberhalb der realen Datenempfindlichkeit.

Eine mikroskopische `r_B ~ 60 nm`-Zone allein ist keine direkt seismisch aufloesbare Zielstruktur.

## 5. Konsequenz fuer den Projektstatus

Diese externe Rueckmeldung veraendert den konservativen Endstatus nicht:

```text
H+ Standard-Hawking:
    FAIL im getesteten SK-IV-Projekt-Reinterpretationsmodell.

H0:
    OPEN / nicht nachgewiesen.

Formation:
    stark negativ / unaufgeloest.

Stage 3.69:
    DEFINED / NOT PERFORMED; jetzt inklusive Quantum/Wave-Capture.

Stage 3.70:
    DEFINED / NOT PERFORMED; Seismik nur bei makroskopischer gekoppelter Signatur.
```

Die Rueckmeldungen sind damit Modellhaertung und keine experimentelle Bestaetigung.

## Literatur

- Dziewonski, A. M. & Anderson, D. L. (1981), *Preliminary Reference Earth Model*, Physics of the Earth and Planetary Interiors 25, 297-356.
- Davies, J. H. & Davies, D. R. (2010), *Earth's surface heat flux*, Solid Earth 1, 5-24. Preferred estimate: `47 +/- 2 TW`.
- Doran, C., Lasenby, A., Dolan, S. & Hinder, I. (2005), *Fermion absorption cross section of a Schwarzschild black hole*, arXiv:gr-qc/0503019.
