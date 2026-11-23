import unittest

from src.u1_quotient_layers import (
    divisor_residue_representatives,
    k_equals_one_family_witness,
    quotient_layer_report,
    quotient_layer_witness,
    t11_discrete_log_test,
)


class TestDivisorResidues(unittest.TestCase):
    def test_divisor_residue_dp_matches_direct_divisors(self):
        reps = divisor_residue_representatives(80, 7)
        self.assertEqual(set(reps), {1, 2, 3, 4, 5, 6})
        self.assertTrue(all(80 % d == 0 for d in reps.values()))

    def test_t7_layer_for_313(self):
        w = quotient_layer_witness(313, 7)
        self.assertIsNotNone(w)
        self.assertEqual((w["M"], w["d"], w["a"], w["k"], w["s"]), (80, 20, 3, 4, 47))
        self.assertEqual(313 + 4 * w["k"], 7 * w["s"])

    def test_t11_layer_fails_for_three_u1_exceptions(self):
        for p, factors, residues in (
            (193, [(3, 1), (17, 1)], [1, 3, 6, 7]),
            (2521, [(3, 1), (211, 1)], [1, 2, 3, 6]),
            (66529, [(3, 1), (5, 1), (1109, 1)], [1, 3, 4, 5, 9]),
        ):
            report = quotient_layer_report(p, 11)
            self.assertEqual(report["factorization"], factors)
            self.assertEqual(report["attainable_divisor_residues"], residues)
            self.assertFalse(report["target_attained"])

    def test_t11_discrete_log_test_matches_divisor_residue_test(self):
        for p in (193, 2521, 66529, 313, 73, 97, 1009):
            log_report = t11_discrete_log_test(p)
            div_report = quotient_layer_report(p, 11)
            self.assertEqual(log_report["witness_exists"], div_report["target_attained"])


class TestKEqualsOneFamily(unittest.TestCase):
    def test_t7_and_t11_constructions_for_73(self):
        w7 = k_equals_one_family_witness(73, 7)
        w11 = k_equals_one_family_witness(73, 11)
        self.assertEqual((w7["a"], w7["s"], w7["k"]), (3, 11, 1))
        self.assertEqual((w11["a"], w11["s"], w11["k"]), (2, 7, 1))

    def test_no_t7_k1_witness_for_313(self):
        self.assertIsNone(k_equals_one_family_witness(313, 7))


if __name__ == "__main__":
    unittest.main()
