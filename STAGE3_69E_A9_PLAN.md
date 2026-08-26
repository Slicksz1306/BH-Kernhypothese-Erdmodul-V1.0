# Stage 3.69E / A9 – Residence-Time + Backpressure + Minimal Weak Network

**Status:** NEXT BLOCK / NOT YET CALCULATED

## Ziel

A9 soll die letzte grosse Reduced-Closure zwischen aeusserem Supply und innerem Horizon-Sink quantitativ schliessen:

```text
supply
 -> residence/recycling
 -> backpressure/escape
 -> charge neutrality
 -> Fe/Ni charge/composition network
 -> actual chi_transport
 -> net Mdot_BH
```

## Mindestgleichungen

```text
Mdot_BH = chi_transport * Mdot_supply

dM_res/dt = Mdot_supply - Mdot_BH - Mdot_escape

chi_capture = p/(p+e)
```

plus ein minimales species-/charge network fuer Fe/Ni/e-/p mit Reaktionsraten gegen lokale Residence-Zeiten.

## Acceptance criteria

1. reproduzierbare Massenerhaltung;
2. absorbierender und reflektierender Grenzfall werden korrekt reproduziert;
3. `chi_transport` wird nicht als freier Faktor eingesetzt, sondern aus Residence/Escape/Backpressure abgeleitet;
4. Weak reactions werden nur aktiviert, wenn `tau_reaction <= tau_residence`;
5. Ergebnis ist eine Mdot-Spanne mit klar dokumentierten EOS-/Transportunsicherheiten.

A9 entscheidet nicht automatisch die Existenzhypothese. Es soll die aktuelle groesste Akkretionsunsicherheit quantitativ reduzieren.
