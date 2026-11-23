"""Independent regression tests for the Phase 8 small-factor search."""

import sys
from pathlib import Path

# The source files live in src/ in the repository layout.
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import unittest

from phase7_floor_quotient import (
    all_dual_type_ii_witnesses,
    prime_by_trial_division,
)
from phase8_small_factor import (
    all_witnesses_small_factor,
    count_small_factor_divisibility_tests,
)

BOUNDARY_PRIMES = (193, 2521, 66529)
FOURTEEN_PRIMES = (
    409, 577, 5569, 9601, 23929, 83449, 102001,
    329617, 712321, 1134241, 1724209, 1726201,
    5212561, 8813281,
)


def trial_factorization_division_count(n: int) -> int:
    """Count trial candidates used by Phase 7's elementary factorizer."""
    remaining = n
    divisor = 2
    count = 0
    while divisor * divisor <= remaining:
        count += 1
        if remaining % divisor == 0:
            while remaining % divisor == 0:
                remaining //= divisor
        divisor = 3 if divisor == 2 else divisor + 2
    return count


def phase7_factorization_test_count(p: int, u: int) -> int:
    from phase7_floor_quotient import floor_quotient_k_candidates
    return sum(
        trial_factorization_division_count(p + 4 * k * u * u)
        for k in floor_quotient_k_candidates(p, u)
    )


class SmallFactorSearchTests(unittest.TestCase):
    def test_exact_witness_sets_match_phase7_divisor_search_on_boundary_primes(self):
        for p in BOUNDARY_PRIMES:
            for u in range(1, 5):
                with self.subTest(p=p, u=u):
                    self.assertEqual(
                        all_witnesses_small_factor(p, u),
                        all_dual_type_ii_witnesses(p, u),
                    )

    def test_exact_witness_sets_match_on_fourteen_literature_primes(self):
        for p in FOURTEEN_PRIMES:
            self.assertTrue(prime_by_trial_division(p))
            for u in range(1, 5):
                with self.subTest(p=p, u=u):
                    self.assertEqual(
                        all_witnesses_small_factor(p, u),
                        all_dual_type_ii_witnesses(p, u),
                    )

    def test_exact_witness_sets_match_for_76_primes_through_5000(self):
        primes = [
            p for p in range(73, 5001)
            if p % 24 == 1 and prime_by_trial_division(p)
        ]
        self.assertEqual(len(primes), 76)
        comparisons = 0
        for p in primes:
            for u in range(1, 5):
                with self.subTest(p=p, u=u):
                    self.assertEqual(
                        all_witnesses_small_factor(p, u),
                        all_dual_type_ii_witnesses(p, u),
                    )
                    comparisons += 1
        self.assertEqual(comparisons, 304)

    def test_every_returned_witness_satisfies_original_type_ii_equations(self):
        for p in (73, 193, 2521, 66529):
            for u in range(1, 5):
                for w in all_witnesses_small_factor(p, u):
                    with self.subTest(p=p, witness=w):
                        self.assertEqual(w.a * p + u, w.s * w.v)
                        self.assertEqual(w.s + 1, 4 * u * w.a * w.k)
                        self.assertEqual(w.u + w.v, w.a * w.e)
                        self.assertEqual(p + w.e, 4 * u * w.v * w.k)

    def test_divisibility_trial_counts_match_recorded_benchmarks(self):
        expected = {
            193: (12, 5, 2, 2),
            2521: (74, 31, 16, 12),
            66529: (639, 275, 160, 118),
        }
        for p, counts in expected.items():
            for u, expected_count in enumerate(counts, start=1):
                with self.subTest(p=p, u=u):
                    self.assertEqual(
                        count_small_factor_divisibility_tests(p, u),
                        expected_count,
                    )

    def test_trial_division_counts_against_phase7_factorization(self):
        expected = {
            193: ((25, 12), (13, 5), (8, 2), (8, 2)),
            2521: ((192, 74), (115, 31), (65, 16), (73, 12)),
            66529: ((6710, 639), (2728, 275), (2172, 160), (1678, 118)),
        }
        for p, pairs in expected.items():
            for u, (old_count, new_count) in enumerate(pairs, start=1):
                with self.subTest(p=p, u=u):
                    self.assertEqual(phase7_factorization_test_count(p, u), old_count)
                    self.assertEqual(
                        count_small_factor_divisibility_tests(p, u),
                        new_count,
                    )

    def test_invalid_inputs_are_rejected(self):
        for p, u in ((193, 0), (193, 5), (75, 1), (True, 1)):
            with self.subTest(p=p, u=u):
                with self.assertRaises(ValueError):
                    all_witnesses_small_factor(p, u)


if __name__ == "__main__":
    unittest.main(verbosity=2)
