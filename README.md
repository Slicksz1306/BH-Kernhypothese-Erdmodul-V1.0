# SL/BH-Kernhypothese Erdmodul

## Veröffentlichungsangaben

**Autor:** Daniel Marcel Schlicksupp  
**Geburtsdatum:** 13.06.1988  
**Region:** Rheinland-Pfalz  
**Land:** Deutschland  
**Aktueller Theorie-Textstand:** Erdmodul V1.2  
**Numerischer Entwicklungsstand:** SL-TOV / Earth Matching 1.3C  
**Stand:** 25.08.2026  
**Erstveröffentlichung des Erdmoduls V1.0:** 23.08.2026

Copyright 2026 Daniel Marcel Schlicksupp. Alle Rechte vorbehalten.

> **Versionshinweis:** Der Repository-Name enthält aus historischen Gründen weiterhin `V1.0`. Die Datei `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` ist die unveränderte Veröffentlichungsfassung vom 23.08.2026 und bleibt als Archiv-/Prioritätsnachweis erhalten. `THEORIE.md` dokumentiert den aktuellen Erdmodul-Stand. Der vorhandene SHA-256-Hash bezieht sich weiterhin auf die unveränderte V1.0-PDF.

## Wissenschaftlicher Status

Die SL/BH-Kernhypothese ist ein **theoretisches Forschungsmodell**. `SL` steht in diesem Projekt für **Schwarzes Loch**. Für die Erde wird als Modellannahme geprüft, ob ein kleines zentrales Schwarzes Loch mit einer entsprechend redistributiven Materieverteilung vereinbar sein kann.

Es wird **keine direkte Detektion eines Schwarzen Lochs im Erdzentrum behauptet**. Begriffe wie „bestanden“ oder „validiert“ beziehen sich ausschließlich auf klar benannte interne Konsistenz- beziehungsweise numerische Solvertests, nicht auf einen experimentellen Nachweis.

## Aktuelles Erdmodell V1.2

Das finale Erdmodell ist **nicht** die frühere starke Grenzvariante `M_SL ~ M_Earth`. Diese Variante bleibt unter PREM/Standard-GR mit der beobachteten radialen Massenverteilung, Seismologie und dem Trägheitsmoment unvereinbar und ist nicht Bestandteil des aktuellen Erdmodells.

Der aktuelle kleine, redistributive Zweig verwendet stattdessen die Massenbuchhaltung

```text
M_PREM(<r_rep) = M_SL
```

Das zentrale Objekt wird also **nicht zusätzlich** zur gemessenen Erdmasse addiert. Es ersetzt im Basismodell dieselbe PREM-Masse im Zentrum. Im ideal kugelsymmetrischen redistributiven Grenzfall bleibt außerhalb der Ersatzregion die eingeschlossene Gesamtmasse gleich:

```text
M'(<r) = M_PREM(<r),  r >= r_rep
```

Damit bleibt dort auch das monopole äußere Gravitationsfeld unverändert. Das ist eine Massenbuchhaltungsbedingung und für sich allein noch keine vollständige selbstkonsistente Innenraumlösung.

## Drei getrennte Skalen

```text
Schwarzschildradius:        r_s   = 2 G M_SL / c^2
Bondi-/Referenzskala:       r_B   = G M_SL / c_eff^2
Struktureller Ersatzradius: M_PREM(<r_rep) = M_SL
```

`r_s`, `r_B` und `r_rep` dürfen nicht gleichgesetzt werden. Insbesondere ist `c_eff` im Erdmodul nur eine modellabhängige Referenzgröße. Die seismische P-Wellen-Geschwindigkeit eines festen/mehrphasigen Kerns ist nicht automatisch der thermodynamische Schallparameter eines idealen Bondi-Fluids.

## Ergebnis des V1.2-Konsistenzmoduls

Für den kleinen redistributiven Erd-BH-Zweig wurde innerhalb der verwendeten Modellannahmen kein ausschließender Widerspruch in den bislang implementierten Prüfungen gefunden. Untersucht wurden insbesondere:

- Gesamtmassen-Buchhaltung und äußere Gravitation,
- Größenordnung des Trägheitsmoments,
- seismologische Einordnung,
- Trennung von Horizont-, Einfluss- und Strukturgrößen,
- Akkretions- und Kontinuumsregime,
- Wärme- und Langzeitbedingungen.

Das bedeutet **interne Modellkompatibilität innerhalb der geprüften Randbedingungen**, nicht empirische Bestätigung.

## Numerische Erweiterung: SL-TOV / Earth Matching

Der aktuelle Simulationsstack geht über die rein redistributive V1.2-Buchhaltung hinaus. Implementiert ist eine sphärische Jordan-Frame-Minimalfassung mit

```text
F(chi) = F0 + xi chi^2
V(chi) = 1/2 m_chi^2 chi^2 + 1/4 lambda chi^4
```

und den Zustandsgrößen

```text
y = [m, nu, p, chi, psi]
psi = dchi/dr
```

Die hydrostatische Integration startet erst an einem Matching-Radius `r_a > r_h`; die unbekannte unmittelbare BH-Nahzone wird nicht künstlich als gewöhnliche TOV-Flüssigkeit fortgesetzt. Der GR-Grenzfall `xi -> 0`, `chi -> 0` ist als harter Solvercheck implementiert.

### Konservativ validierter numerischer Stand 1.3C

Für den konkret fortgesetzten Zweig

```text
M_SL = 1e16 kg
q0   = 1e-14
```

ist die voll gekoppelte Lösung unter den festgelegten numerischen Kriterien für folgende Kopplungs-/Reichweitenskalen validiert:

```text
r_c = 1000 km
r_c =  750 km
r_c =  500 km
```

Bei `r_c = 300 km` wird das aktuelle Single-Shooting numerisch schlecht konditioniert; darunter wird es stark instabil. Ein 100-km-Collocation-Lauf erreicht kleine Gleichungsresiduen, ist wegen fehlender Mesh-Konvergenz aber **nur Kandidat und nicht validiert**.

Die derzeitige Grenze `r_c >= 500 km` ist daher eine **numerische Frontier dieses speziellen Fortsetzungszweigs**, keine physikalische Ausschlussgrenze für kürzere Reichweiten.

Siehe [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) für die genaue Trennung zwischen validierten, Kandidaten- und offenen Bereichen.

## Offene Physik

Noch nicht geschlossen sind insbesondere:

1. Formation Rule / Entstehungsmechanismus des zentralen SL,
2. sub-kontinuierliche beziehungsweise mikroskopische Capture-/Akkretionsphysik,
3. thermischer Energie- und Transportabschluss der BH-Nahzone,
4. fundamentale Hochdruck-Fe/Ni-EOS statt reiner PREM-Barotrop-Closure,
5. vollständiger PREM-/Normalmoden-/Laufzeit-Likelihood-Fit,
6. robuste Short-Range-BVP-Lösung mit Mesh- und Richtungs-Konvergenz,
7. unabhängige, vorab festgelegte Detektionssignaturen.

## Falsifikationsprinzip

Eine konkrete Parameterwahl muss mit **demselben Parametersatz** gleichzeitig gegen alle relevanten Beobachtungsklassen bestehen. Parameter dürfen nicht für jeden Test separat nachjustiert werden.

Mindestens zu prüfen sind:

- Erdmasse und Radius,
- normiertes Trägheitsmoment,
- Seismologie und Normalmoden,
- Wärmehaushalt,
- geologisches Alter und Langzeitstabilität,
- konsistente Formation und Akkretion,
- numerische Stabilität und Konvergenz der vollständigen Randwertlösung.

## Wissenschaftlicher Review

Technische Kritik, Reproduktionsversuche und Falsifikationsanalysen sind ausdrücklich erwünscht. Für belastbare Reviews bitte [`CONTRIBUTING.md`](CONTRIBUTING.md) beachten. Das Repository enthält außerdem ein strukturiertes GitHub-Issue-Template für konzeptionelle, mathematische, numerische und empirische Einwände.

## Dateien

- [`THEORIE.md`](THEORIE.md) – aktueller Erdmodul-Theoriestand V1.2 mit numerischer Erweiterung.
- [`NUMERIK_STATUS.md`](NUMERIK_STATUS.md) – reproduzierbarer Status und Validierungsgrenzen des aktuellen SL-TOV/Earth-Matching-Stacks.
- [`CHANGELOG.md`](CHANGELOG.md) – nachvollziehbare Entwicklung der öffentlichen Theorie- und Numerikstände.
- [`CONTRIBUTING.md`](CONTRIBUTING.md) – Anforderungen für Reproduktion, Review und technische Einwände.
- [`LICENSE`](LICENSE) – Rechte- und Nutzungshinweis für die öffentliche Veröffentlichung.
- `BH_Kernhypothese_Erdmodul_V1_0_Publication.pdf` – archivierte Erstveröffentlichung V1.0 vom 23.08.2026.
- `SHA256SUMS.txt` – Prüfsumme der archivierten V1.0-PDF.
- `CITATION.cff` – Zitiermetadaten des aktuellen Repository-Textstands.

## Primärreferenz

A. M. Dziewonski & D. L. Anderson (1981), *Preliminary Reference Earth Model*, Physics of the Earth and Planetary Interiors 25, 297–356. DOI: 10.1016/0031-9201(81)90046-7.

## Zitierform

Daniel Marcel Schlicksupp (2026), *SL/BH-Kernhypothese Erdmodul V1.2*, Theorie- und Forschungsentwurf, numerischer Entwicklungsstand Earth Matching 1.3C, Rheinland-Pfalz, Deutschland.
