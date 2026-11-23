import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import unittest
from phase7_floor_quotient import all_dual_type_ii_witnesses, prime_by_trial_division
from phase8_small_factor import all_witnesses_small_factor
from phase9_scaling import DEFAULT_PRIMES, benchmark_one


class Phase9ScalingTests(unittest.TestCase):
    def test_default_benchmark_inputs_are_prime_and_in_residue_class(self):
        for p in DEFAULT_PRIMES:
            with self.subTest(p=p):
                self.assertEqual(p % 24, 1)
                self.assertTrue(prime_by_trial_division(p))

    def test_phase7_and_phase8_return_identical_full_witness_sets(self):
        sample = (73, 193, 2521, 66529, 10009, 100057)
        for p in sample:
            for u in range(1, 5):
                with self.subTest(p=p, u=u):
                    self.assertEqual(
                        all_dual_type_ii_witnesses(p, u),
                        all_witnesses_small_factor(p, u),
                    )

    def test_every_benchmark_witness_has_original_type_ii_identity(self):
        row = benchmark_one(66529, 4, repeats=1)
        self.assertTrue(row["witness_sets_identical"])
        self.assertTrue(row["witness_identities_verified"])
        self.assertEqual(row["witness_count"], 1)

    def test_benchmark_reports_nonnegative_times_and_candidate_counts(self):
        for u in range(1,5):
            row=benchmark_one(193,u,repeats=1)
            self.assertGreaterEqual(row["phase7_median_seconds"],0)
            self.assertGreaterEqual(row["phase8_median_seconds"],0)
            self.assertGreaterEqual(row["k_candidates"],0)
            self.assertGreaterEqual(row["phase8_small_factor_divisibility_tests"],0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
