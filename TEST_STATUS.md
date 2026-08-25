# SL/BH-Kernhypothese Erdmodul – Test- und Validierungsstand

**Autor:** Daniel Marcel Schlicksupp  
**Stand:** 25.08.2026  
**Theorie-Textstand:** Erdmodul V1.3  
**Aktueller Forschungsstand:** Stage 3.17

## Statusbegriffe

- **validiert** = der konkret benannte numerische Solver-/Konvergenztest erfüllt die festgelegten Kriterien.
- **Kandidat** = numerisch plausibel, aber nicht vollständig cross-solver-/mesh-bestätigt.
- **Sensitivität** = Parameter- oder Modellvergleich; keine empirische Grenze.
- **offen** = mit den vorhandenen Gleichungen/Daten noch nicht belastbar entschieden.
- **korrigiert/zurückgezogen** = ein früheres Zwischenresultat wurde durch einen härteren Test ersetzt.
- **empirisch bestätigt** = unabhängige Messdaten erforderlich; derzeit nicht erreicht.

Keiner der hier dokumentierten Tests ist eine direkte Detektion eines Schwarzen Lochs im Erdzentrum.

## 1. Erdstruktur / Earth Matching

Historischer Referenzzweig:

```text
M_SL=1e16 kg, q(r_a)=1e-14.
```

- Layered-PREM-GR-Baseline: `Delta R/R~4.17e-9`, `Delta M/M~4.44e-8`.
- `r_c=500 km`: voll gekoppelt validiert.
- `r_c=300 km`: cross-solver-validiert.
- `250 km`: Kandidat.
- `200 km`: offen.

**Stage-3.16-Korrektur:** Diese alten Ergebnisse gehören zu einer materiearmen/harten inneren Matching-Interpretation und dürfen nicht automatisch als Validierung des neuen `R_smooth`-Branches verwendet werden.

## 2. Seismologie / Strukturproxies Stages 1.7–1.9

- 1D P-/PKP-/PKIKP-Raytracing implementiert.
- q-basierte Referenzzweige zeigen Millisekunden-Laufzeitverschiebungen.
- Toroidale Normalmoden nur als vereinfachter SNREI-artiger Prototyp.
- Bisherige `0.041 s`-Skala hochwertiger Kernphasen-Differentialmessungen wird nur als Vergleichsmaß verwendet, nicht als formale Ausschlussgrenze.

## 3. Akkretion / Langzeit Stages 2–3.14

- Klassische Bondi-Algebra reproduziert; kein mathematischer Fehler gefunden.
- Unmodifizierte kanonische Bondi-Rate für `1e16 kg` ist geologisch viel zu schnell.
- Festkörperdiffusion/Creep/Wärme/Melt-Front wurden als Grenzregime getestet.
- „Lokale Wärme schmilzt zwangsläufig alles und startet automatisch Bondi“ ist zu stark.
- Konstante `Gamma~4`-Capture-Grenze um `~54 r_s`: zurückgezogen.
- `8 GPa`-Mikrorettung aus hcp-Fe: für Coulombmaterie zurückgezogen.
- Voll relativistischer Michel-Solver besteht analytischen `Gamma=2`-Selfcheck mit relativer Mdot-Abweichung ~`2e-14`.
- Für `M_SL=1e16 kg` liefert die phenomenologische condensed-to-degenerate EOS ungefähr `147–1460 kg/s` und belastet diesen Referenzzweig stark.
- Aktuelle Coulomb-Plastizität zeigt keinen nachgewiesenen einfachen `1e5–1e6`-Blockademechanismus für den `1e16 kg`-Zweig.

## 4. Stage 3.15 – vollständiger Massenscan

Gekoppelte reduzierte Massenentwicklung:

```text
dM/dt = k_Michel M^2 - A_H/M^2.
```

Wichtige Korrektur gegenüber Stage 3.12: Hawking und Michel dürfen nicht nur als getrennte Ausschlussgrenzen geschnitten werden.

Im reduzierten Modell existiert ein instabiles Gleichgewicht

```text
M_eq ~1.28e11 ... 2.28e11 kg.
```

- e-Faltungszeit: `~4.2e9 ... 2.4e10 yr`.
- Anfangsmassenband für `<1%` Nettoänderung über 4.54 Gyr: ungefähr `-0.5/+0.5%` bis `-4.4/+5.1%` um `M_eq`.
- PREM-Buchhaltungsradius: `~133–161 m`.
- Kein Attraktor; kein empirischer Nachweis.
- Materialtransport liegt dort außerhalb der Stage-3.14-MD-Ratenkalibrierung.

## 5. Stage 3.16 – externer Geophysik-Härtetest

### Hard cavity / harte Ersatzkugel

Wörtliche Exzision gewöhnlicher Materie innerhalb `r_rep` ergibt eine mechanisch instabile Kavität:

```text
P_c ~364 GPa
sigma_VM ~546 GPa.
```

Druckkollaps-Zeitskalen:

```text
~1.08 s für 1e16 kg
~0.025–0.030 s für das Stage-3.15-Band.
```

**Status:** `R_hard` verworfen.

### Zentralstreu-Geometrie

PREM-basierter radialer P-Weg:

```text
Zentrum -> Oberfläche ~606.77 s.
```

Ein realer zentraler Streuer würde für flache Beben ungefähr bei

```text
~1210–1214 s (~20.2 min)
```

ankommen und im kugelsymmetrischen 1-D-Modell nahezu stationsdistanzunabhängig sein.

**Status:** Zeitgeometrie bestätigt; Beobachtungs-Nichtnachweis nicht formal geprüft.

## 6. Stage 3.17 – Smooth-Branch-Seismik

Aktueller redistributiver Kandidat:

```text
rho_new(r)=rho_PREM(r)-M_SL w(r),
integral 4 pi r^2 w(r)dr=1.
```

`r_rep` ist nur Buchhaltungs-/Größenskala, keine Vakuumgrenze.

Für das Stage-3.15-Massenband ergibt der fixed-elastic-moduli-Forward-Test:

```text
PKIKP 180° delta t:
R_mix=100 km:     ~21–86 ns
R_mix=500 km:     ~0.8–3.5 ns
R_mix=1221.5 km:  ~0.14–0.58 ns.
```

Selbst eine absichtlich scharfe fractional-PREM-Grenze bei `100 km` hätte nur eine Reflexionsamplitude von Größenordnung `~1e-9`; ein glatter Taper besitzt diesen führenden Sprung nicht.

Unbekannte Near-Zone `~133–161 m`:

```text
+1% Vp:     ~0.23–0.28 ms
+10% Vp:    ~2.1–2.6 ms
+50% Vp:    ~7.9–9.5 ms
+100% Vp:   ~11.8–14.3 ms.
```

**Status:** `R_smooth` wird durch diesen vereinfachten Seismik-Forward-Test nicht ausgeschlossen. Die Near Zone benötigt eine selbstkonsistente Material-/Full-Wave-Lösung.

## 7. Aktuelle Statusmatrix

| Bereich | Status |
|---|---|
| starke Erd-SL-Variante | mit Erdstruktur unvereinbar |
| alter `1e16 kg`-Referenzzweig | stark durch relativistische Langzeitakkretion belastet |
| Hard-Cavity/Hard-Replacement | mechanisch verworfen |
| Stage-3.15 `~1e11 kg` Hawking/Michel-Band | Kandidat im reduzierten ODE |
| Smooth mass compensation | mathematisch massenerhaltend; neuer Strukturbranch |
| verteilte Smooth-Seismiksignatur | im Fixed-Moduli-Proxy extrem klein |
| zentrale `~100 m` Near Zone | offen |
| voll gekoppeltes `R_smooth` Earth Matching | noch nicht validiert |
| Formation | offen; gewöhnlicher heutiger Capture stark unplausibel |
| empirische Detektion | keine |

## 8. Nächste harte Tests

1. voll gekoppeltes `R_smooth` Earth Matching für `M~1e11 kg`,
2. selbstkonsistentes `rho(r), Vp(r), Vs(r)` der Near Zone,
3. elastischer Full-Wave-/Antipodal-Array-Synthetic,
4. Near-Zone-Transport bei den hohen dimensionslosen Raten des niedrigen Massenbands,
5. Hawking-Greybody/Teilchenspezies/Spin/Ladung,
6. Formation Rule.

## Aussagegrenze

Der aktuelle Stand ist ein weit ausgearbeiteter und mehrfach korrigierter theoretischer Forschungsrahmen. Er erlaubt **nicht** die Aussage, dass ein Schwarzes Loch im Erdzentrum experimentell nachgewiesen oder die Hypothese als etablierte physikalische Theorie bestätigt wurde.
