import math
import unittest
import stage3_80_f8_substructure_scan as f8

class F8Tests(unittest.TestCase):
    def test_plummer_density_scales_with_mass(self):
        a=f8.AU
        r1=f8.plummer_density(0.0,1e20,a)
        r4=f8.plummer_density(0.0,4e20,a)
        self.assertAlmostEqual(r4/r1,4.0,places=12)
    def test_virial_sigma_squared_scales_with_mass(self):
        a=f8.AU
        s1=f8.plummer_sigma_1d(0.0,1e20,a)
        s4=f8.plummer_sigma_1d(0.0,4e20,a)
        self.assertAlmostEqual((s4/s1)**2,4.0,places=12)
    def test_virial_q_decreases_as_m_minus_half(self):
        a=f8.AU
        q1=f8.plummer_density(0.0,1e20,a)/f8.plummer_sigma_1d(0.0,1e20,a)**3
        q4=f8.plummer_density(0.0,4e20,a)/f8.plummer_sigma_1d(0.0,4e20,a)**3
        self.assertAlmostEqual(q4/q1,0.5,places=12)
    def test_f6_q_requirement_regression_1e11(self):
        q=f8.q_si_to_msun_pc3_per_kms3(f8.q_required(1e11))
        self.assertAlmostEqual(q,1.46794,places=5)
    def test_bulk_velocity_suppresses_q(self):
        q0=f8.shifted_low_velocity_q(1.0,100.0,0.0)
        q3=f8.shifted_low_velocity_q(1.0,100.0,300.0)
        self.assertAlmostEqual(q3/q0,math.exp(-4.5),places=12)
    def test_stream_expands_and_dilutes(self):
        M=1e20; a=100*f8.AU; sig=10.0
        rho0=f8.gaussian_density(0.0,M,a)
        at,off,rho,q=f8.stream_phase_space_at_collapse(M,a,sig,0.0,0.06)
        self.assertGreater(at,a); self.assertEqual(off,0.0); self.assertLess(rho,rho0); self.assertGreater(q,0.0)
    def test_required_mu_roundtrip(self):
        for m in f8.SEED_MASSES:
            self.assertAlmostEqual(f8.mu_from_density(f8.rho_required_for_mu(m),m),f8.F6_MU_REQ,places=12)

if __name__=='__main__': unittest.main()
