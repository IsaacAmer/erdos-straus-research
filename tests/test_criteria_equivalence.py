import unittest

from src.criteria_equivalence import (
    admissible_parameters,
    bradford_divisors,
    bradford_to_dahan,
    dahan_pair_to_bradford,
    dahan_witnesses,
    run_small_audit,
    verify_prime_shift,
)


class TestDahanBradfordEquivalence(unittest.TestCase):
    def test_known_parameters(self):
        self.assertEqual(admissible_parameters(73, 7), 20)

    def test_rejects_invalid_parameters(self):
        with self.assertRaises(ValueError):
            admissible_parameters(73, 8)
        with self.assertRaises(ValueError):
            admissible_parameters(75, 7)

    def test_all_directions_for_sample(self):
        result = verify_prime_shift(73, 7)
        self.assertTrue(result["equivalence_checked"])

    def test_each_witness_maps_both_ways(self):
        p, c = 73, 7
        known_pairs = dahan_witnesses(p, c)
        for u, v in known_pairs:
            w = dahan_pair_to_bradford(p, c, u, v)
            pair = bradford_to_dahan(p, c, w.d, w.branch)
            self.assertIn(tuple(sorted(pair)), known_pairs)
            self.assertGreater(pair[0], 0)
            self.assertGreater(pair[1], 0)

    def test_finite_regression_range(self):
        records = run_small_audit(150)
        self.assertGreater(len(records), 0)
        self.assertTrue(all(r["equivalence_checked"] for r in records))


if __name__ == "__main__":
    unittest.main()
