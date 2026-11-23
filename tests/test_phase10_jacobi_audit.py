import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC = PROJECT_ROOT / "src"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))

import unittest

from phase7_floor_quotient import prime_by_trial_division
from phase8_small_factor import all_witnesses_small_factor
from phase10_jacobi_audit import (
    audit_type_ii_witness,
    audit_witness_collection,
    jacobi_symbol,
)

SAMPLE_PRIMES = (
    193, 2521, 66529, 10009, 100057, 1000033,
    10000537, 100000081, 1000000009,
)
EXPECTED_WITNESSES_BY_PRIME = {
    193: 2,
    2521: 3,
    66529: 1,
    10009: 24,
    100057: 24,
    1000033: 33,
    10000537: 42,
    100000081: 49,
    1000000009: 68,
}


class JacobiSymbolTests(unittest.TestCase):
    def test_standard_values(self):
        self.assertEqual(jacobi_symbol(1, 15), 1)
        self.assertEqual(jacobi_symbol(2, 73), 1)
        self.assertEqual(jacobi_symbol(3, 73), 1)
        self.assertEqual(jacobi_symbol(5, 13), -1)
        self.assertEqual(jacobi_symbol(0, 15), 0)
        self.assertEqual(jacobi_symbol(-1, 73), 1)

    def test_quadratic_reciprocity_for_odd_coprime_inputs(self):
        for a in range(1, 40, 2):
            for n in range(3, 42, 2):
                import math
                if math.gcd(a, n) == 1:
                    expected = jacobi_symbol(n, a) * (-1 if (a % 4 == 3 and n % 4 == 3) else 1)
                    self.assertEqual(jacobi_symbol(a, n), expected)

    def test_rejects_even_or_nonpositive_denominators(self):
        for n in (0, -3, 2, 18):
            with self.subTest(n=n):
                with self.assertRaises(ValueError):
                    jacobi_symbol(3, n)


class TypeIIJacobiAuditTests(unittest.TestCase):
    def test_known_p73_witnesses_satisfy_all_six_laws(self):
        witnesses = all_witnesses_small_factor(73, 1)
        self.assertEqual(len(witnesses), 2)
        for w in witnesses:
            audit = audit_type_ii_witness(73, w)
            self.assertTrue(audit.identities_ok)
            self.assertTrue(audit.jacobi_laws_ok)
            self.assertTrue(audit.passed)

    def test_all_witnesses_for_nine_primes_satisfy_theorem_2_4(self):
        grand_total = 0
        for p in SAMPLE_PRIMES:
            self.assertEqual(p % 24, 1)
            self.assertTrue(prime_by_trial_division(p))
            p_total = 0
            for u in range(1, 5):
                with self.subTest(p=p, u=u):
                    witnesses = all_witnesses_small_factor(p, u)
                    report = audit_witness_collection(p, witnesses)
                    self.assertTrue(report["all_passed"], report)
                    self.assertEqual(report["failed_count"], 0)
                    p_total += len(witnesses)
            self.assertEqual(p_total, EXPECTED_WITNESSES_BY_PRIME[p])
            grand_total += p_total
        self.assertEqual(grand_total, 246)

    def test_audit_rejects_composite_or_wrong_residue_prime(self):
        witness = all_witnesses_small_factor(73, 1)[0]
        for p in (75, 121, 193 * 193):
            with self.subTest(p=p):
                with self.assertRaises(ValueError):
                    audit_type_ii_witness(p, witness)

    def test_collection_reports_failure_for_corrupted_witness(self):
        from dataclasses import replace
        witness = all_witnesses_small_factor(73, 1)[0]
        corrupted = replace(witness, s=witness.s + 4)
        report = audit_witness_collection(73, [corrupted])
        self.assertEqual(report["witness_count"], 1)
        self.assertEqual(report["failed_count"], 1)
        self.assertFalse(report["all_passed"])


if __name__ == "__main__":
    unittest.main(verbosity=2)
