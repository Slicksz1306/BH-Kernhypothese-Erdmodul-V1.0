# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Region:** Rheinland-Pfalz, Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.3  
**Aktueller Forschungsstand:** Stage 3.17  
**Stand:** 25.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Archivhinweis:** `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` bleibt unverändert als Erstveröffentlichungs- und Prioritätsnachweis erhalten. Die aktuelle Weiterentwicklung wird in den Markdown-Dateien dokumentiert.

## Wissenschaftlicher Status

Die **SL/BH-Kernhypothese Erdmodul** ist ein theoretisches Forschungsmodell. `SL` bezeichnet ein **Schwarzes Loch**.

Es wird **keine direkte Detektion eines Schwarzen Lochs im Erdzentrum behauptet**. Numerisch bestandene Solver-, Matching-, Forward- oder Cross-Solver-Tests sind keine empirischen Nachweise.

Die starke Variante, in der ein zentrales Schwarzes Loch einen wesentlichen Anteil der Erdmasse oder Erdgravitation trägt, ist mit der beobachteten Erdstruktur nicht vereinbar. Ein wesentlich kleinerer zentraler SL-Zweig wird weiter getestet.

## Redistributive Massenbuchhaltung – aktuelle Korrektur

Frühere Fassungen verwendeten die Buchhaltung

```text
M_PREM(<r_rep) = M_SL.
```

Stage 3.16 zeigt jedoch, dass `r_rep` **nicht** als physische leere Ersatzkugel interpretiert werden darf. Eine harte zentrale Kavität wäre unter dem Erdkern-Druck mechanisch nicht haltbar.

Der aktuelle Kandidatenzweig ist daher **smooth compensated**:

```text
rho_new(r) = rho_PREM(r) - M_SL w(r)
```

mit

```text
integral 4 pi r^2 w(r) dr = 1.
```

Damit wird die SL-Masse weiterhin nicht doppelt gezählt, aber gewöhnliche Materie bleibt bis in die Near Zone vorhanden. `r_rep` ist nur noch eine Buchhaltungs-/Größenskala.

## Feldtheoretischer Minimalrahmen

Der sphärische Jordan-Frame-Minimalstack verwendet

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4.
```

Der GR-Grenzfall muss für `xi -> 0`, `chi -> 0`, `dchi/dr -> 0` auf die gewöhnliche TOV-Struktur zurückfallen. Ein reales zentrales Schwarzes Loch wird über eine Horizon-/Matching-Randbedingung und nicht als reguläres TOV-Zentrum behandelt.

## Earth-Matching

Für den historischen Referenzzweig

```text
M_SL   = 1e16 kg
q(r_a) = 1e-14
```

wurden `r_c=500 km` und `r_c=300 km` mit der gehärteten Layered-PREM-Closure voll gekoppelt numerisch validiert; der 300-km-Punkt ist cross-solver-validiert.

**Wichtige Stage-3.16-Korrektur:** Diese älteren Hard-/Vacuum-Near-Zone-Matching-Ergebnisse dürfen nicht automatisch als Validierung des neuen `R_smooth`-Branches gelten. Das Earth Matching muss für die materiereiche glatte Near Zone neu gerechnet werden.

## Akkretionsblock

Die klassische Bondi-Algebra wurde reproduziert; kein mathematischer Fehler in der Formel wurde gefunden. Die entscheidende Frage ist ihre physikalische Anwendbarkeit auf kondensierte, plastische und degenerierte Erdmaterie.

Der relativistische Michel-Test ergibt für `M_SL=1e16 kg` in der getesteten phenomenologischen condensed-to-degenerate EOS ungefähr

```text
Mdot_Michel ~ 147 ... 1460 kg/s.
```

Damit bleibt der alte `1e16 kg`-Referenzzweig durch Langzeitakkretion stark belastet.

## Stage 3.15 – Hawking/Michel-Massenscan

Die gleichzeitige reduzierte Massenentwicklung

```text
dM/dt = k_Michel M^2 - A_H/M^2
```

besitzt ein instabiles Hawking/Michel-Gleichgewicht bei ungefähr

```text
M_eq ~ 1.28e11 ... 2.28e11 kg.
```

Die lineare e-Faltungszeit liegt ungefähr bei `4.2e9 ... 2.4e10 Jahren`. Ein kleines Anfangsmassenband kann im reduzierten ODE über 4.54 Gyr weniger als 1% Netto-Massenänderung zeigen.

Das ist **kein Attraktor und kein Nachweis**. Die Materialtransportphysik liegt bei diesem niedrigen Massenband außerhalb der Stage-3.14-MD-Kalibrierung, und das Earth Matching ist dort noch nicht validiert.

Details: [`MASSENSCAN_STAGE3_15.md`](MASSENSCAN_STAGE3_15.md).

## Stage 3.16 – externe Geophysik-Härtetests

Ein externer Einwand gegen eine wörtliche zentrale Ersatzkugel wurde quantitativ geprüft.

### Hard cavity

Bei `P_c~364 GPa` ergibt sich für eine nahezu leere Kugelkavität eine charakteristische von-Mises-Skala von ungefähr

```text
sigma_VM ~546 GPa.
```

Die Druckkollaps-Zeitskala beträgt grob

```text
~1.08 s        für M_SL=1e16 kg,
~0.025–0.030 s für das Stage-3.15-Massenband.
```

Der `R_hard`-Zweig wird daher als statischer Erdbranch verworfen.

### Zentralstreu-Geometrie

Der PREM-basierte radiale P-Wellenweg Zentrum→Oberfläche beträgt ungefähr

```text
606.77 s.
```

Ein **realer** zentraler Streuer würde für flache Erdbeben daher ungefähr bei

```text
1210–1214 s  (~20.2 min)
```

ankommen und im kugelsymmetrischen 1-D-Modell nahezu unabhängig von der Epizentraldistanz sein.

Die Zeitgeometrie ist korrekt; entscheidend ist aber, ob der physische Branch überhaupt einen starken zentralen Streuer enthält.

## Stage 3.17 – Seismik des glatten Branches

Seismometer koppeln nicht direkt an den Ereignishorizont, sondern an Dichte, Druck und elastische Eigenschaften des umgebenden Materials.

Mit einer glatten Massenkompensation und dem bisherigen fixed-elastic-moduli-Forward-Proxy ergeben sich für das Stage-3.15-Massenband:

```text
PKIKP 180° Laufzeitänderung:
R_mix=100 km:      ~21–86 ns
R_mix=500 km:      ~0.8–3.5 ns
R_mix=1221.5 km:   ~0.14–0.58 ns.
```

Selbst eine absichtlich scharfe fractional-PREM-Grenze bei `R_mix=100 km` hätte nur eine Normalinzidenz-Reflexionsamplitude in der Größenordnung

```text
~6e-10 ... 1e-9.
```

Ein glatter Taper besitzt diesen führenden Sprung gar nicht.

Damit ist die starke ~1212-s-Hard-Cavity-Reflexion **keine automatische Vorhersage** des `R_smooth`-Branches.

Die noch ungelöste Near-Zone besitzt im Stage-3.15-Band nur eine Größenskala von ungefähr `133–161 m`. Hypothetische lokale Vp-Erhöhungen über diese gesamte Zone liefern im einfachen PKIKP-180°-Timing-Proxy ungefähr:

```text
+1% Vp:     ~0.23–0.28 ms
+10% Vp:    ~2.1–2.6 ms
+50% Vp:    ~7.9–9.5 ms
+100% Vp:   ~11.8–14.3 ms.
```

Das ist noch kein voller elastischer Full-Wave-Test; antipodale Fokussierung, Modenkonversion, Dämpfung und reale Near-Zone-Mineralphysik fehlen.

Details: [`SEISMIK_STAGE3_16_17.md`](SEISMIK_STAGE3_16_17.md).

## Aktueller konservativer Status

```text
M_SL ~ 1e16 kg:
    stark durch relativistische Langzeitakkretion belastet

R_hard / leere zentrale Ersatzkugel:
    mechanisch verworfen

M_SL ~ 1e11 kg, R_smooth:
    Hawking/Michel-Kandidatenband im reduzierten ODE,
    verteilte smooth-Kompensation im Seismikproxy extrem klein,
    Near-Zone-Transport und neues Earth Matching weiterhin offen
```

Damit ist weder ein Erd-SL nachgewiesen noch die gesamte kleine Erd-SL-Hypothese ausgeschlossen.

## Nächste harte Tests

1. voll gekoppeltes Earth Matching des `R_smooth`-Branches im `~1e11 kg`-Band,
2. selbstkonsistentes Near-Zone-Profil `rho(r), Vp(r), Vs(r)`,
3. elastischer Full-Wave-/Antipodal-Array-Synthetic,
4. Near-Zone-Transport außerhalb der Stage-3.14-MD-Kalibrierung,
5. Hawking-Greybody-/Teilchenspezies-, Spin- und Ladungssensitivität,
6. Formation Rule für das niedrige Massenband.

## Dateien

- [`THEORIE.md`](THEORIE.md) – Theorierahmen.
- [`TEST_STATUS.md`](TEST_STATUS.md) – Test- und Validierungsmatrix.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) – numerischer Entwicklungsstand.
- [`AKKRETION_STATUS.md`](AKKRETION_STATUS.md) – Akkretions-/Langzeitstatus.
- [`MASSENSCAN_STAGE3_15.md`](MASSENSCAN_STAGE3_15.md) – Hawking/Michel-Massenscan.
- [`SEISMIK_STAGE3_16_17.md`](SEISMIK_STAGE3_16_17.md) – externe Geophysik-Einwände und Smooth-Branch-Seismik.
- [`CHANGELOG.md`](CHANGELOG.md) – Versions- und Korrekturhistorie.
- [`CITATION.cff`](CITATION.cff) – Zitiermetadaten.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` – unveränderte Erstveröffentlichung.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.3*, theoretischer Forschungsentwurf, aktueller Entwicklungsstand Stage 3.17, Rheinland-Pfalz, Deutschland.
