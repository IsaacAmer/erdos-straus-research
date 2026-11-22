import unittest

from src.typeII_u_bound import (
    minimal_u_witness,
    type_ii_witness_for_u,
    rosati_type_ii_decomposition,
)


class TestTypeIIQuotientCriterion(unittest.TestCase):
    def test_three_u1_exceptions_have_exact_higher_u_witnesses(self):
        expected = {
            193: (2, 1, 5, 7, 5, 39),
            2521: (2, 1, 29, 31, 11, 87),
            66529: (4, 11, 1041, 95, 4, 703),
        }
        for p, values in expected.items():
            self.assertIsNone(type_ii_witness_for_u(p, 1))
            w = minimal_u_witness(p, 4)
            self.assertIsNotNone(w)
            self.assertEqual(
                (w["u"], w["a"], w["Q"], w["r"], w["k"], w["s"]),
                values,
            )
            self.assertEqual(p % 24, 1)
            self.assertEqual(w["a"] * p + w["u"], w["Q"] * w["s"])
            self.assertEqual((w["s"] + 1) % (4 * w["u"] * w["a"]), 0)
            decomposition = rosati_type_ii_decomposition(p, w)
            self.assertEqual(decomposition["identity"], __import__("fractions").Fraction(4, p))

    def test_u1_witness_examples(self):
        for p in (73, 97, 241, 313, 337, 409, 433, 457, 577, 601):
            w = type_ii_witness_for_u(p, 1)
            self.assertIsNotNone(w, f"expected a u=1 witness for p={p}")
            self.assertEqual((w["a"] * p + 1) % w["s"], 0)
            self.assertEqual((w["s"] + 1) % (4 * w["a"]), 0)

    def test_invalid_u_rejected(self):
        with self.assertRaises(ValueError):
            type_ii_witness_for_u(73, 0)

    def test_minimal_u_limit(self):
        self.assertIsNone(minimal_u_witness(193, 1))
        self.assertEqual(minimal_u_witness(193, 2)["u"], 2)


if __name__ == "__main__":
    unittest.main()
