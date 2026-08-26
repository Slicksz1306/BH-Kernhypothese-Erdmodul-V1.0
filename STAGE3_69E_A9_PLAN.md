# Stage 3.69E / A9 – Residence-Time + Backpressure + Minimal Weak Network

**Status:** REDUCED CLOSURE CALCULATED / FULL WDM-HYDRO STILL OPEN

Der urspruenglich in dieser Datei definierte A9-Plan wurde am 26.08.2026 als reproduzierbare Reduced-Closure bearbeitet.

## Ziel

A9 verbindet

```text
supply
 -> residence/recycling
 -> backpressure/escape
 -> charge neutrality
 -> Fe/Ni weak-timescale gate
 -> chi_transport
 -> net Mdot_BH.
```

## Mindestgleichungen

```text
Mdot_BH = chi_transport * Mdot_supply

dM_res/dt = Mdot_supply - Mdot_BH - Mdot_escape

chi_capture = p/(p+e)
```

## Acceptance-Status

1. **Massenerhaltung / Reservoir-Bilanz:** in der Reduced Capacity-Closure umgesetzt.
2. **Absorbierender/reflektierender Grenzfall:** A7-PDE vorhanden; A9 ergaenzt die repeated-encounter/escape Closure.
3. **`chi_transport` nicht frei eingesetzt:** `p/(p+e)` plus collisional escape optical-depth bracket verwendet.
4. **Weak reactions nur bei ausreichender Residence-Zeit:** ueber `lambda_required=1/t_res` getestet.
5. **Mdot-/Transportstatus mit Unsicherheiten:** fuer den Strong-Coupling-Branch und den `1e10...5e11 kg` Massenscan dokumentiert.

## Hauptergebnis

```text
M >= ~1e11 kg:
    current strong-coupling/recycling reduced branch is supply-processing capable
    for tested r_t = 3e-11 ... 2e-10 m.

M = 1e10 kg:
    transition-scale/backpressure sensitive; OPEN.

Full first-principles WDM transport / final Stage 3.69 Mdot:
    OPEN.
```

Details und Zahlen:

- `STAGE3_69E_A9_RESIDENCE_BACKPRESSURE_NETWORK.md`
- `stage3_69e_a9_residence_backpressure_network.py`

Naechster Pflichtblock:

```text
Stage 3.69F / A-10:
first-principles-informed WDM transport
+ time-dependent hydro/kinetic sink coupling
-> replace geometric mean-free-path proxy
-> final reduced species-resolved Mdot band.
```
