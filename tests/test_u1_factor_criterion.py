import unittest

from src.u1_factor_criterion import (
    certify_u1_failure,
    find_u1_witness,
    sharp_u1_bounds,
    t3_witness,
    witness_at_k,
)


class TestSharpU1Bounds(unittest.TestCase):
    def test_bounds_are_exact_integer_floors(self):
        self.assertEqual(sharp_u1_bounds(73), (3, 3))
        self.assertEqual(sharp_u1_bounds(97), (3, 5))

    def test_rejects_wrong_residue_class(self):
        with self.assertRaises(ValueError):
            sharp_u1_bounds(101)


class TestU1DivisorCriterion(unittest.TestCase):
    def test_known_witnesses(self):
        expected = {
            73: (2, 1, 7, 11),
            97: (1, 2, 7, 15),
            313: (3, 4, 47, 7),
        }
        for p, row in expected.items():
            w = find_u1_witness(p)
            self.assertIsNotNone(w)
            self.assertEqual((w["a"], w["k"], w["s"], w["t"]), row)
            self.assertEqual((w["s"] + 1) % (4 * w["a"] * w["k"]), 0)
            self.assertEqual((w["a"] * p + 1) % w["s"], 0)

    def test_three_u1_exceptions(self):
        for p, bounds in ((193, (7, 9)), (2521, (90, 126)), (66529, (2376, 3326))):
            result = certify_u1_failure(p)
            self.assertEqual((result["a_max"], result["k_max"]), bounds)
            self.assertIsNone(result["u1_witness"])
            self.assertEqual(result["k_values_checked"], bounds[1])

    def test_fixed_k_divisor_search(self):
        self.assertIsNotNone(witness_at_k(313, 4))
        self.assertIsNone(witness_at_k(193, 1))

    def test_t3_factor_criterion(self):
        w = t3_witness(1009)
        self.assertIsNotNone(w)
        self.assertEqual((w["q"], w["a"], w["k"], w["t"]), (11, 4, 23, 3))
        self.assertIsNone(t3_witness(193))


if __name__ == "__main__":
    unittest.main()
