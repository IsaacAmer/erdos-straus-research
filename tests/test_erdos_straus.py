import unittest
from fractions import Fraction

from src.erdos_straus import build_from_shift_and_divisor, verify_representation


class TestErdosStraus(unittest.TestCase):
    def test_known_construction_p73(self):
        x, b, c = build_from_shift_and_divisor(73, 7, 10)
        self.assertEqual((x, b, c), (20, 210, 30660))
        self.assertEqual(
            Fraction(4, 73),
            Fraction(1, x) + Fraction(1, b) + Fraction(1, c),
        )

    def test_verifier_rejects_wrong_identity(self):
        self.assertFalse(verify_representation(73, 20, 210, 30661))

    def test_verifier_rejects_nonpositive_denominators(self):
        self.assertFalse(verify_representation(73, 20, 210, 0))

    def test_invalid_divisor_is_rejected(self):
        with self.assertRaises(ValueError):
            build_from_shift_and_divisor(73, 7, 11)


if __name__ == "__main__":
    unittest.main()
