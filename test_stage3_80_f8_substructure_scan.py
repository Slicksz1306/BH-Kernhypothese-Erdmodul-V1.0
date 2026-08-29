import math
import tempfile
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

    def test_f6_embryo_hill_volume_not_finished_earth(self):
        vh_earth=4*math.pi/3*(f8.AU*(f8.M_EARTH/(3*f8.M_SUN))**(1/3))**3
        self.assertAlmostEqual(vh_earth/f8.F6_VH,1/0.03,places=10)

    def test_torus_thin_limit(self):
        frac=f8.torus_hill_spatial_fraction(1e-5*f8.AU)
        expected=f8.F6_RH/(math.pi*f8.AU)
        self.assertAlmostEqual(frac/expected,1.0,places=3)

    def test_torus_bulk_velocity_reduces_eligible_fraction(self):
        f0=f8.velocity_eligible_fraction(100.0,0.0,1000.0)
        f1=f8.velocity_eligible_fraction(100.0,1000.0,1000.0)
        self.assertLess(f1,f0)

    def test_epicycle_requirement(self):
        r=f8.torus_requirement(0.1,0.0)
        self.assertAlmostEqual(r['width_AU'],0.0033574,places=6)
        self.assertTrue(3e4 < r['Nseed_required'] < 4e4)

    def test_compatibility_grid_shape(self):
        gp={'Mmin':1e-16,'Mmax':1e-15,'M_N':2,'sigmamin':0.1,'sigmamax':0.2,'sigma_N':2,
            'rminAU':0.001,'rmaxAU':0.01,'r_N':2,'vrelmin':0.0,'vrelmax':0.5,'vrel_N':2}
        with tempfile.TemporaryDirectory() as d:
            df=f8.rungrid(d+'/x.csv',gp,[1e10])
        self.assertEqual(len(df),16)
        self.assertIn('mu_H',df.columns)
        self.assertIn('epicycleConsistent',df.columns)


if __name__=='__main__':
    unittest.main()
