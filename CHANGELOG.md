# Changelog

Dieses Changelog dokumentiert die öffentlich sichtbaren Entwicklungsstände des Erdmoduls. Historische Zwischenwerte bleiben als Entwicklungsstand erhalten; spätere härtere Tests ersetzen nur ihre aktuelle Interpretation.

## V1.5 / A13b–A19 / Stage 3.70B — 29.08.2026

Die nach A13 verbliebenen Reduced-/Falsifikationsblöcke wurden nacheinander bearbeitet, ohne offene physische Closures künstlich als PASS zu deklarieren.

### A13b — Grant-2021 experimenteller Liquid-Fe-Fit-Anker

- publizierte Grant-2021 Liquid-Fe-EOS-Fitform bis `400 GPa` implementiert;
- PREM-Randcheck: `B_Grant~1.419 TPa` vs `K_PREM~1.425 TPa`;
- nominaler `1e11 kg` Supply-Scan: `~1.29e-7...3.80e-6 kg/s`;
- konservativer Fit/T/Intermediate-EOS-Corner-Scan: `~8.27e-8...6.13e-6 kg/s`;
- raw Zenodo / direct SESAME-92141 ingestion bleibt OPEN;
- keine Figure-Punkte erfunden oder digitalisiert.

### A14 — Dense-core Electron Screening

- diffuse `+24.18e`-Plasmaskala als bevorzugte Earth-core-Closure zurückgestuft;
- Thomas-Fermi-Dense-Core-Proxy: `E_F~19.4...86.6 eV`, `lambda_TF~2.95e-11...4.29e-11 m`;
- screened response scale grob `O(1...5e)`;
- Proton-Dirac bei `+1.6...+4.9e` bleibt nur order-unity unterdrückt (`~0.925...0.867 classical`);
- großer elektrostatischer Protonenblocker nicht gefunden;
- exakter screened Coulomb-Dirac-Elektronenmatcher bleibt OPEN refinement.

### A15 — Integrated Reduced Net-Throughput

A13b Supply gegen A10 Processing-Capacity:

```text
1e10 kg: Xi~0.832...61.60 -> supply/EOS/backpressure conditional
1e11 kg: Xi~1.59e-3...1.18e-1 -> processing-capable
2e11 kg: Xi~2.42e-4...1.80e-2 -> processing-capable
5e11 kg: Xi~2.00e-5...1.48e-3 -> processing-capable.
```

Single-pass capture wird wegen `chi_capture=p/(p+e_perm)` nicht als stationärer Multiplikationsfaktor missbraucht.

Finale Full-WDM species-resolved `Mdot_BH(t)` bleibt OPEN.

### A16 — Wärme / 4.54-Gyr-Sensitivität

A13b `eta=1` momentane Restmassenleistung:

```text
1e10 kg: max ~0.0055 TW
1e11 kg: max ~0.551 TW
2e11 kg: max ~2.20 TW
5e11 kg: max ~13.76 TW.
```

Gegen die grobe globale `47 +/-2 TW`-Wärmeflussskala ergibt sich kein harter Budget-Ausschluss. Ein vollständiger geothermischer Quellenfit bleibt OPEN.

`dM/dt=kM^2`-Rückwärtslösungen über `4.54 Gyr` bleiben algebraisch positiv; hohe Supply-Aeste erzeugen jedoch kurze heutige Wachstumsskalen und starken Evolutions-/Fine-Tuning-Druck.

### A17 / Stage 3.70A — Observability Gate

- direkte `r_B`-Near-Zone-Seismik als extrem sub-wavelength eingestuft;
- bei `lambda=1 km`: `ka~3.9e-11...1.9e-9`;
- H0-Seismik erfordert daher eine vorhergesagte makroskopische `delta-rho/delta-Vp/delta-Vs`-Struktur oder äquivalente Observable;
- Engpass ist die Modellvorhersage, nicht das Fehlen öffentlicher PREM-/Seismikdaten.

### A18 / Stage 3.70B — Current Real-Data Audit

2026 SK-Gd-Publikation im Band `25.29...31.29 MeV`:

```text
SK-IV observed 90% CL        0.04 cm^-2 s^-1 MeV^-1
SK-VI+VII NN observed        0.13
SK-VI+VII BDT observed       0.16.
```

Projekt-H+ Proxy `0.098...0.122` bleibt damit gegen den stärksten publizierten SK-IV-Binconstraint um Faktor `2.45...3.05` darüber:

```text
H+ = FAIL in project reinterpretation against strongest published bin limit.
```

Die standalone SK-Gd-2026-Limits allein sind in diesem Bin schwächer. Keine offizielle Super-K-Erdzentrum-BH-Exklusion wird behauptet.

Die 2026 gemeldete DSNB-Indikation wird nicht als Earth-BH-Signal interpretiert.

H0:

```text
REAL-DATA LIKELIHOOD NOT YET IDENTIFIABLE.
```

### A19 — Formation / Delivery Recheck

Capture-freundlicher direct-Earth Dynamical-Friction-Proxy bei normalem Halo-Encounter `v_inf=220 km/s`:

```text
DeltaE/E_inf ~1e-18...5e-17.
```

One-crossing capture-friendly Geschwindigkeitsschwelle:

```text
~0.004...0.031 m/s.
```

Damit bleibt normaler Halo-Earth-Capture ein **VERY STRONG FAIL**. Neuere Drei-Körper-PBH-Star-Capture-Arbeiten zeigen reale Mechanismen in anderen Massen-/Hostregimen, liefern aber keinen Earth-delivery Rescue für `1e13...5e14 g`.

Ein primordial bereits cold/co-moving eingebetteter Seed bleibt als Anfangsbedingung OPEN; Ursprung und Wahrscheinlichkeit sind nicht hergeleitet.

### Projektstatus nach A19

```text
H+:
  negative in strongest project Hawking-neutrino comparison.

H0:
  quantitative reduced stack;
  not detected;
  unique real-data likelihood not yet identifiable.

M>=1e11 kg:
  reduced inner processing-capable in tested A13b stack.

1e10 kg:
  supply/EOS/backpressure conditional.

Formation:
  one of the strongest remaining negatives.
```

Neue zentrale Dateien:

- `STAGE3_69I_A13B_GRANT_FIT_ANCHOR.md`
- `stage3_69i_a13b_grant_fit_anchor.py`
- `STAGE3_69J_A14_ELECTRON_SCREENING.md`
- `stage3_69j_a14_electron_screening.py`
- `STAGE3_69K_A15_NET_THROUGHPUT.md`
- `stage3_69k_a15_net_throughput.py`
- `STAGE3_69L_A16_HEAT_AGE.md`
- `stage3_69l_a16_heat_age.py`
- `STAGE3_70A_A17_PRE_FALSIFICATION.md`
- `stage3_70a_a17_prefalsification.py`
- `STAGE3_70B_A18_REALDATA_AUDIT.md`
- `stage3_70b_a18_realdata_audit.py`
- `STAGE3_71_A19_FORMATION_RECHECK.md`
- `stage3_71_a19_formation_recheck.py`

---

## V1.5 / Stage 3.69I/A13 General-EOS Michel Supply — 26.08.2026

- general-EOS relativistischer Michel-Solver implementiert;
- A12c constant-stiffness Regression `~1e-5...1e-4`: PASS;
- controlled variable-EOS surrogate bei `1e11 kg`: `4.64e-8...1.37e-6 kg/s`;
- `>=1e11 kg` processing-capable im getesteten A13-Surrogat;
- `1e10 kg` EOS/supply conditional;
- constant PREM stiffness to horizon nur Stresslimit;
- historischer Michel-Bereich als **LEGACY / EOS-SENSITIVE** klassifiziert.

---

## V1.5 / Stage 3.69H/A12-A12c — 26.08.2026

- A12 Shock-Konvergenz bis N=1024;
- kapazitätslimitierter `1e10 kg` Branch outward-propagating, keine stationäre endliche Innen-`Mdot` etabliert;
- A12b More/TF-`Zbar` sowie eta/k-Sensitivitäten;
- A12c relativistische Supply-Korrektur und EOS-Sensitivität.

---

## V1.5 / Stage 3.69E/A9-A10 — 26.08.2026

- exact repeated-encounter closure `chi_capture=p/(p+e_perm)`;
- permanent Escape vs Recycling getrennt;
- first-principles-informed WDM-Transporthüllen;
- `local Kn~1 != permanent escape`;
- inner Processing-Capacity quantitativ klassifiziert.

---

## V1.5 / Stage 3.69A-A8 — 26.08.2026

- Schwarzschild-Dirac-Prototyp und Regressionen;
- Earth-speed Protonenscan;
- charged-Proton-Sensitivität;
- Fe-56/Ni-58 `0+` Composite-Capture;
- Recycling-/Collision-Regime-Korrekturen;
- Dense-Fe/weak-reaction Timescale Gates.

---

## V1.5 / Stage 3.68E — 26.08.2026

- externer Numerical-Relativity/HPC- und Seismologie-Input integriert;
- `c_eff=10.4355 km/s` und `r_B~61 nm` bei `1e11 kg` dokumentiert;
- Bondi/Michel nicht mehr automatisch als finale Horizon-Rate interpretiert;
- Quantum/Wave-Capture und 47-TW-Wärmecheck als Pflichtblöcke aufgenommen.

---

## V1.5 / Definition Stage 3.69-3.70 — 25.08.2026

- Stage 3.69 als High-Fidelity-/Multiphysics-Closure definiert;
- Stage 3.70 als branch-spezifischer Real-Data-/Falsifikationstest definiert.

---

## V1.4 / Stage 3.68 — 25.08.2026

- H+ und H0 strikt getrennt;
- kleiner smooth-compensated Branch weitergeführt;
- Hard-Cavity und mehrere frühe Akkretions-/Coulomb-Proxies korrigiert oder verworfen;
- Formation unter getesteten Standardwegen stark negativ.

---

## V1.3 / Stage 3.14-3.17 — 25.08.2026

- Bondi-/Michel-Akkretionsaudit;
- smooth-compensated Branch;
- erste Seismik-Härtetests und Hawking/Michel-Massenscans.

---

## V1.0 — 23.08.2026

Erstveröffentlichung des Erdmoduls. Die archivierte V1.0-PDF bleibt unverändert als Prioritäts-/Archivnachweis.
