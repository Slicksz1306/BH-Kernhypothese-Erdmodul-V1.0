import copy
import unittest

from stage3_95e_a35_closure_capability_audit import (
    ALLOWED_CLASSES,
    evaluate_solver_release,
    load_matrix,
    validate_matrix,
)


class TestStage395EA35ClosureCapabilityAudit(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rows = load_matrix()
        cls.by_id = {row["closure_id"]: row for row in cls.rows}

    def test_matrix_shape_and_vocabulary(self):
        self.assertEqual(len(self.rows), 16)
        self.assertEqual(len(self.by_id), 16)
        self.assertTrue(
            {row["current_class"] for row in self.rows}.issubset(ALLOWED_CLASSES)
        )
        validate_matrix(self.rows)

    def test_solver_release_is_blocked(self):
        result = evaluate_solver_release(self.rows)
        self.assertEqual(result["release_ready_interface_count"], 1)
        self.assertEqual(result["blocking_interface_count"], 15)
        self.assertEqual(result["solver_release_gate"], "NOT PASSED")
        self.assertEqual(result["real_q_eq_implementation"], "NO-GO")
        self.assertEqual(result["physical_closure"], "OPEN")
        self.assertEqual(result["experimental_bh_evidence"], "NONE")

    def test_known_hard_blockers_remain_open(self):
        expected = {
            "A35-ION": "CURRENTLY UNAVAILABLE",
            "A35-LST": "CURRENTLY UNAVAILABLE",
            "A35-MQ": "MODEL-DEPENDENT",
            "A35-K": "MODEL-DEPENDENT",
        }
        for closure_id, status in expected.items():
            self.assertEqual(self.by_id[closure_id]["current_class"], status)
            self.assertEqual(self.by_id[closure_id]["blocks_solver_now"], "yes")

    def test_thermodynamics_is_not_promoted_beyond_source_domain(self):
        row = self.by_id["A35-THERMO"]
        self.assertEqual(row["current_class"], "DERIVABLE")
        self.assertEqual(row["domain_status"], "PARTIAL_DOMAIN_ONLY")
        self.assertEqual(row["blocks_solver_now"], "yes")

    def test_poisson_equation_does_not_close_material_response(self):
        self.assertEqual(self.by_id["A35-FIELD"]["current_class"], "THEORY-CLOSED")
        self.assertEqual(self.by_id["A35-FIELD"]["blocks_solver_now"], "no")
        self.assertEqual(self.by_id["A35-RESPONSE"]["blocks_solver_now"], "yes")

    def test_anti_proxy_guard_rejects_false_l_st_promotion(self):
        rows = copy.deepcopy(self.rows)
        for row in rows:
            if row["closure_id"] == "A35-LST":
                row["current_class"] = "DATA-CLOSED"
        with self.assertRaises(ValueError):
            validate_matrix(rows)

    def test_anti_proxy_guard_rejects_false_matching_promotion(self):
        rows = copy.deepcopy(self.rows)
        for row in rows:
            if row["closure_id"] == "A35-MQ":
                row["current_class"] = "THEORY-CLOSED"
        with self.assertRaises(ValueError):
            validate_matrix(rows)


if __name__ == "__main__":
    unittest.main()
