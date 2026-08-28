# Stage 3.71 / A19 — Formation / Delivery Recheck

## Status

**STANDARD EARTH-CAPTURE REMAINS FAIL / RECENT THREE-BODY STAR-CAPTURE RESULTS DO NOT RESCUE PROJECT MASS RANGE / COLD CO-MOVING ORIGIN STILL OPEN BUT UNDERIVED**

Formation is intentionally kept separate from the internal Earth-core accretion calculation. A model can be internally long-lived after insertion and still fail to explain how the object arrived at the center.

## 1. Literature update

Oncins et al. (2022) calculate PBH capture by stars through dynamical friction after a PBH has been placed on a bound, star-crossing orbit. Their fluid dynamical-friction form has the characteristic scaling

```text
a_df ~ 4 pi G^2 rho M_PBH I / v^2.
```

They emphasize that capture is favored in high-density, low-velocity environments.

A recent 2026 preprint by Gottlieb et al., *The Life and Death of Stars That Capture Primordial Black Holes* (arXiv:2606.02700), finds that direct single-pass capture by stellar dynamical friction is negligibly rare over its asteroid-mass range and that initial binding is instead dominated by three-body interactions with planetary/stellar companions. For a solar-type host with a Jupiter analog, inspiral within a main-sequence lifetime requires roughly

```text
M_BH,crit >= 1e22 g.
```

The Earth-core project range is only

```text
1e10 ... 5e11 kg
= 1e13 ... 5e14 g,
```

so it is roughly `2e7...1e9` times lighter than that Jupiter-analog inspiral threshold. This newer channel therefore does not provide a standard delivery mechanism into the Earth for the project mass range.

This comparison is qualitative across different host systems; the 2026 work studies stellar capture, not direct Earth capture.

## 2. Deliberately optimistic direct-Earth capture estimate

To test standard halo delivery, A19 uses a capture-friendly one-crossing drag estimate:

```text
F_df = 4 pi G^2 M^2 rho I / v^2
Delta E = F_df * 2 R_E.
```

Inputs:

```text
rho = 5514 kg/m3       [uniform mean Earth density]
R_E = 6371 km
v_esc = 11.2 km/s
I = 30                 [deliberately generous friction/Coulomb factor]
v_inf = 220 km/s       [standard halo-speed benchmark].
```

The in-Earth speed is approximated by

```text
v^2 = v_inf^2 + v_esc^2.
```

The energy that must be removed for capture is

```text
E_inf = 1/2 M v_inf^2.
```

### Results at halo speed

| M_BH | DeltaE crossing [J] | E_inf [J] | DeltaE/E_inf |
|---:|---:|---:|---:|
| `1e10 kg` | `2.43e2` | `2.42e20` | `1.00e-18` |
| `1e11 kg` | `2.43e4` | `2.42e21` | `1.00e-17` |
| `2e11 kg` | `9.73e4` | `4.84e21` | `2.01e-17` |
| `5e11 kg` | `6.08e5` | `1.21e22` | `5.02e-17` |

Thus even this intentionally favorable drag estimate misses one-pass halo capture by about

```text
16 ... 18 orders of magnitude in energy.
```

A smaller/more realistic friction factor only worsens this result.

## 3. How co-moving would it have to be?

Solving the same optimistic estimate for the maximum asymptotic speed that could be captured in one crossing gives

```text
DeltaE(v_inf) = 1/2 M v_inf^2.
```

Results:

| M_BH | capture threshold v_inf |
|---:|---:|
| `1e10 kg` | `0.0043 m/s` |
| `1e11 kg` | `0.0137 m/s` |
| `2e11 kg` | `0.0194 m/s` |
| `5e11 kg` | `0.0307 m/s` |

This is **millimeter-to-centimeter per second** relative motion at infinity, not a normal Galactic-halo encounter.

Therefore the old project statement becomes sharper:

```text
normal halo -> direct Earth capture:
FAIL very strongly.

cold/co-moving object already embedded in the forming system:
mathematically possible as an initial condition,
but its origin and probability are not derived.
```

The exact low-speed drag law changes near Mach~1/subsonic regimes, but A19 already chose `I=30` as a deliberately capture-friendly upper proxy. The conclusion is controlled by the enormous energy gap, not percent-level drag details.

## 4. Proto-Earth / planetesimal route

A smaller early body does not automatically solve the problem. A primordial object arriving with ordinary halo velocity still carries a specific positive orbital energy `~v_inf^2/2` that must be dissipated. Lower-density/smaller bodies offer less column density and therefore generally less drag per passage.

A route in which the PBH was **already nearly co-moving with the protoplanetary material** is qualitatively different. It is not standard capture from the Galactic halo; it is an initial phase-space correlation that needs a cosmological/protoplanetary origin model.

No such origin has yet been derived in the project.

## 5. Current formation matrix

| Mechanism | Updated status |
|---|---|
| in-situ collapse of normal Earth matter | **FAIL** |
| later direct Earth capture from normal halo speeds | **VERY STRONG FAIL** |
| Proto-Earth/planetesimal capture from normal halo speeds | **FAIL under tested standard conditions** |
| stellar single-pass dynamical-friction capture | **inefficient in modern literature** |
| three-body stellar/planetary companion capture | **real mechanism in literature, but does not rescue 1e13...5e14 g Earth-delivery range** |
| normal halo -> cold protoplanetary disk | **strongly negative / no demonstrated dissipation path** |
| primordial cold/co-moving seed already embedded in solar-system material | **OPEN initial condition; origin/probability not derived** |

## 6. Overall implication

A19 does **not** falsify the internal statement "if an object were placed at the center, could the reduced Earth model process matter around it?".

It does strongly constrain the larger physical hypothesis:

```text
A credible Earth-core model still requires a formation/delivery mechanism.
```

At present, formation remains one of the strongest negatives in the entire project.

## Reproducibility

- `stage3_71_a19_formation_recheck.py`

## Claims boundary

A19 uses an intentionally simplified optimistic drag calculation to demonstrate the energy-scale problem. It is not a cosmological PBH-abundance calculation and not a complete N-body model of solar-system formation.
