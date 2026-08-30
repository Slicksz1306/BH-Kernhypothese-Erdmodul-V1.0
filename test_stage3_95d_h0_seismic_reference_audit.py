import unittest

from stage3_95d_h0_seismic_reference_audit import (
    R_ICB_M,
    absolute_center_scatter_baseline_shift_s,
    audit_summary,
    hybrid_prem_epoc_center_surface_time_s,
    outer_core_swap_overlaps_local_h0,
    prem_radial_time_s,
    solve_epoc_profile,
)


class TestStage395DSeismicReferenceAudit(unittest.TestCase):
    def test_prem_center_surface_reference(self):
        self.assertAlmostEqual(prem_radial_time_s(), 606.7743332118, places=6)

    def test_prem_outer_core_reference(self):
        self.assertAlmostEqual(
            prem_radial_time_s(R_ICB_M, 3_480_000.0),
            240.8321366279,
            places=6,
        )

    def test_epoc_reconstruction_matches_paper_cmb_velocity(self):
        epoc = solve_epoc_profile()
        self.assertAlmostEqual(epoc.vp_cmb_m_s / 1000.0, 8.00, places=2)
        self.assertAlmostEqual(epoc.p_cmb_pa / 1e9, 135.75, places=6)
        self.assertAlmostEqual(epoc.p_icb_pa / 1e9, 332.907834, places=5)

    def test_epoc_outer_core_time(self):
        self.assertAlmostEqual(
            solve_epoc_profile().outer_core_time_s,
            241.1575856638,
            places=6,
        )

    def test_hybrid_absolute_path_shift(self):
        self.assertAlmostEqual(
            hybrid_prem_epoc_center_surface_time_s(),
            607.0997822478,
            places=6,
        )
        self.assertAlmostEqual(
            absolute_center_scatter_baseline_shift_s(),
            0.6508980719,
            places=6,
        )

    def test_outer_core_swap_is_disjoint_from_current_h0_near_zone(self):
        for radius in (2_000.0, 100_000.0, 500_000.0, R_ICB_M):
            self.assertFalse(outer_core_swap_overlaps_local_h0(radius))
        self.assertTrue(outer_core_swap_overlaps_local_h0(R_ICB_M + 1.0))

    def test_claim_boundary(self):
        summary = audit_summary()
        self.assertEqual(summary["interpretation"], "PATH_BACKGROUND_SENSITIVITY_ONLY")
        self.assertEqual(summary["experimental_bh_evidence"], "NONE")
        self.assertFalse(summary["stage394_2km_overlap"])


if __name__ == "__main__":
    unittest.main()
