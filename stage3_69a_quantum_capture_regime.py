#!/usr/bin/env python3
"""Stage 3.69A quantum/wave-capture regime diagnostic.

This script does NOT compute the final black-hole absorption rate. It only
reproduces the scale and coupling diagnostics used in
STAGE3_69A_QUANTUM_WAVE_CAPTURE.md.
"""

from math import pi

G = 6.67430e-11
C = 299_792_458.0
H = 6.62607015e-34
HBAR = H / (2.0 * pi)
U = 1.66053906660e-27

M_BH = 1.0e11
V = 10.4355e3
PROJECT_MASSES = (1.0e10, 1.0e11, 2.0e11, 5.0e11)

M_E = 9.1093837139e-31
M_P = 1.67262192595e-27
M_FE56 = 55.93493633 * U

PARTICLES = [
    ("electron", M_E),
    ("proton", M_P),
    ("Fe-56 nucleus", M_FE56),
]


def alpha_g(bh_mass, particle_mass):
    return G * bh_mass * particle_mass / (HBAR * C)


def transition_mass(particle_mass):
    """BH mass for alpha_g = 1."""
    return HBAR * C / (G * particle_mass)


r_s = 2.0 * G * M_BH / C**2
r_B = G * M_BH / V**2
u = V / C
r_g = G * M_BH / C**2

# Classical Schwarzschild point-particle capture cross section as quoted by
# Doran et al. (their Eq. 3, natural-unit mass parameter M = GM/c^2).
# Direct evaluation suffers cancellation at very small u, so for this very
# nonrelativistic reference point we use the leading low-u limit:
# sigma_classical -> 16*pi*(GM/c^2)^2/u^2.
sigma_classical_low_u = 16.0 * pi * r_g**2 / u**2

print(f"M_BH = {M_BH:.6e} kg")
print(f"v = {V:.6e} m/s")
print(f"u=v/c = {u:.9e}")
print(f"r_s = {r_s:.9e} m")
print(f"r_B = {r_B:.9e} m")
print(f"sigma_classical(low-u) = {sigma_classical_low_u:.9e} m^2")
print()

header = (
    f"{'particle':<15} {'lambda_dB[m]':>16} {'lambda/r_s':>16} "
    f"{'alpha_g':>14} {'M(alpha=1)[kg]':>18}"
)
print(header)
print('-' * len(header))

for name, mass in PARTICLES:
    lambda_db = H / (mass * V)
    coupling = alpha_g(M_BH, mass)
    m_transition = transition_mass(mass)
    print(
        f"{name:<15} {lambda_db:16.9e} {lambda_db/r_s:16.9e} "
        f"{coupling:14.9e} {m_transition:18.9e}"
    )

print()
print("alpha_g over selected project masses")
print(f"{'M_BH[kg]':>14} {'electron':>14} {'proton':>14} {'Fe-56':>14}")
print('-' * 60)
for bh_mass in PROJECT_MASSES:
    values = [alpha_g(bh_mass, mass) for _, mass in PARTICLES]
    print(
        f"{bh_mass:14.6e} {values[0]:14.6e} "
        f"{values[1]:14.6e} {values[2]:14.6e}"
    )

print()
print("Interpretation:")
print("- Schroedinger is an outer wave/regime proxy only.")
print("- Final horizon absorption requires a relativistic, horizon-regular")
print("  Klein-Gordon/Dirac treatment with ingoing boundary conditions.")
print("- The proton alpha_g~1 transition lies inside the project mass range.")
print("- Bondi/Michel supply must not be equated directly with Mdot_BH until")
print("  the kinetic-to-wave capture closure is solved.")
