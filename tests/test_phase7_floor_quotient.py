"""Tests for the exact floor-quotient Type-II prefilter."""

import unittest
from math import isqrt

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))

from phase7_floor_quotient import (
    all_dual_type_ii_witnesses,
    candidate_v_interval,
    coarse_k_bound,
    distinct_quotient_count,
    floor_quotient_k_candidates,
    least_positive_residue_of_minus_p,
    positive_divisors,
    prime_by_trial_division,
    slow_floor_gap_candidates,
)


BOUNDARY_PRIMES = (193, 2521, 66529)
FOURTEEN_PRIMES = (
    409, 577, 5569, 9601, 23929, 83449, 102001,
    329617, 712321, 1134241, 1724209, 1726201,
    5212561, 8813281,
)


class FloorQuotientPrefilterTests(unittest.TestCase):
    def test_least_residues_for_all_four_u_values(self):
        self.assertEqual(
            [least_positive_residue_of_minus_p(193, u) for u in range(1, 5)],
            [3, 7, 11, 15],
        )
        self.assertEqual(
            [least_positive_residue_of_minus_p(2521, u) for u in range(1, 5)],
            [3, 7, 11, 7],
        )
        for p in (193, 2521, 66529):
            for u in range(1, 5):
                self.assertGreater(least_positive_residue_of_minus_p(p, u), u)

    def test_fast_quotient_enumeration_matches_full_k_scan(self):
        primes = [p for p in range(73, 5001) if p % 24 == 1 and prime_by_trial_division(p)]
        for p in primes:
            for u in range(1, 5):
                with self.subTest(p=p, u=u):
                    self.assertEqual(
                        floor_quotient_k_candidates(p, u),
                        slow_floor_gap_candidates(p, u),
                    )

    def test_candidate_count_bound(self):
        for p in BOUNDARY_PRIMES:
            for u in range(1, 5):
                candidates = floor_quotient_k_candidates(p, u)
                self.assertLessEqual(len(candidates), 2 * isqrt(p + u))
                self.assertLessEqual(distinct_quotient_count(p + u), 2 * isqrt(p + u))

    def test_exact_candidate_and_coarse_bound_counts(self):
        expected = {
            193: ((24, 5), (5, 3), (2, 1), (1, 1)),
            2521: ((315, 15), (63, 8), (26, 4), (52, 4)),
            66529: ((8316, 126), (1663, 64), (693, 38), (378, 32)),
        }
        for p, rows in expected.items():
            for u, (expected_bound, expected_candidates) in enumerate(rows, start=1):
                with self.subTest(p=p, u=u):
                    self.assertEqual(coarse_k_bound(p, u), expected_bound)
                    self.assertEqual(len(floor_quotient_k_candidates(p, u)), expected_candidates)

    def test_candidate_intervals_are_nonempty_and_exact(self):
        for p in BOUNDARY_PRIMES:
            for u in range(1, 5):
                for k in floor_quotient_k_candidates(p, u):
                    lower, upper = candidate_v_interval(p, u, k)
                    self.assertLessEqual(lower, upper)
                    n_value = p + u
                    length = 4 * u * k
                    self.assertEqual(lower, n_value // length + 1)
                    self.assertEqual(upper, n_value // (length - 1))

    def test_dual_search_reproduces_three_boundary_primes_completely(self):
        expected = {
            193: {1: 0, 2: 2, 3: 0, 4: 0},
            2521: {1: 0, 2: 2, 3: 0, 4: 1},
            66529: {1: 0, 2: 0, 3: 0, 4: 1},
        }
        for p, counts in expected.items():
            self.assertTrue(prime_by_trial_division(p))
            for u in range(1, 5):
                with self.subTest(p=p, u=u):
                    witnesses = all_dual_type_ii_witnesses(p, u)
                    self.assertEqual(len(witnesses), counts[u])
                    for witness in witnesses:
                        self.assertEqual(witness.u, u)
                        self.assertEqual(witness.a * p + u, witness.s * witness.v)
                        self.assertEqual(witness.s + 1, 4 * u * witness.a * witness.k)
                        self.assertEqual(u + witness.v, witness.a * witness.e)
                        self.assertEqual(p + witness.e, 4 * u * witness.v * witness.k)

    def test_all_fourteen_published_primes_have_a_prefiltered_u1_or_u3_witness(self):
        expected_witnesses = {
            409: (1, 2, 7, 117, 59, 1),
            577: (1, 2, 7, 165, 83, 1),
            5569: (1, 2, 47, 237, 119, 6),
            9601: (1, 2, 111, 173, 87, 14),
            23929: (1, 2, 7, 6837, 3419, 1),
            83449: (3, 2, 791, 211, 107, 33),
            102001: (3, 4, 47, 8681, 2171, 1),
            329617: (1, 2, 15, 43949, 21975, 2),
            712321: (1, 2, 23, 61941, 30971, 3),
            1134241: (1, 2, 7, 324069, 162035, 1),
            1724209: (1, 2, 39, 88421, 44211, 5),
            1726201: (1, 2, 1983, 1741, 871, 248),
            5212561: (1, 2, 87, 119829, 59915, 11),
            8813281: (1, 5, 2099, 20994, 4199, 105),
        }
        self.assertEqual(set(expected_witnesses), set(FOURTEEN_PRIMES))
        for p, expected_row in expected_witnesses.items():
            u, a, s, v, e, k = expected_row
            with self.subTest(p=p):
                self.assertTrue(prime_by_trial_division(p))
                self.assertIn(k, floor_quotient_k_candidates(p, u))
                self.assertEqual(a * p + u, s * v)
                self.assertEqual(s + 1, 4 * u * a * k)
                self.assertEqual(u + v, a * e)
                self.assertEqual(p + e, 4 * u * v * k)
                recovered = all_dual_type_ii_witnesses(p, u)
                self.assertIn(
                    next(w for w in recovered if w.k == k and w.a == a and w.s == s),
                    recovered,
                )

    def test_positive_divisors(self):
        self.assertEqual(positive_divisors(1), (1,))
        self.assertEqual(positive_divisors(12), (1, 2, 3, 4, 6, 12))
        self.assertEqual(positive_divisors(225), (1, 3, 5, 9, 15, 25, 45, 75, 225))

    def test_rejects_invalid_inputs(self):
        for p, u in ((0, 1), (73, 0), (73, 5), (75, 1), (True, 1)):
            with self.subTest(p=p, u=u):
                with self.assertRaises(ValueError):
                    floor_quotient_k_candidates(p, u)


if __name__ == "__main__":
    unittest.main(verbosity=2)
