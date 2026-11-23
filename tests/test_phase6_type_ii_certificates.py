"""Exact checks for 17 Erdos-Straus Type-II witness certificates.

The rows certify witnesses with u <= 3 and a <= 5.
Standard library only; copy into the project's tests/ directory.
"""

from math import gcd, isqrt
import unittest


# Rows are (p, u, a, s, v, e, k).
ROWS = (
    (409, 1, 2, 7, 117, 59, 1),
    (577, 1, 2, 7, 165, 83, 1),
    (5569, 1, 2, 47, 237, 119, 6),
    (9601, 1, 2, 111, 173, 87, 14),
    (23929, 1, 2, 7, 6837, 3419, 1),
    (83449, 3, 2, 791, 211, 107, 33),
    (102001, 3, 4, 47, 8681, 2171, 1),
    (329617, 1, 2, 15, 43949, 21975, 2),
    (712321, 1, 2, 23, 61941, 30971, 3),
    (1134241, 1, 2, 7, 324069, 162035, 1),
    (1724209, 1, 2, 39, 88421, 44211, 5),
    (1726201, 1, 2, 1983, 1741, 871, 248),
    (5212561, 1, 2, 87, 119829, 59915, 11),
    (8813281, 1, 5, 2099, 20994, 4199, 105),
)


# (p, a, s, v, e, k): certificates on the stricter u=1 slice.
U1_ROWS = (
    (409, 2, 7, 117, 59, 1),
    (577, 2, 7, 165, 83, 1),
    (5569, 2, 47, 237, 119, 6),
    (9601, 2, 111, 173, 87, 14),
    (23929, 2, 7, 6837, 3419, 1),
    (83449, 5, 1059, 394, 79, 53),
    (102001, 6, 23, 26609, 4435, 1),
    (329617, 2, 15, 43949, 21975, 2),
    (712321, 2, 23, 61941, 30971, 3),
    (1134241, 2, 7, 324069, 162035, 1),
    (1724209, 2, 39, 88421, 44211, 5),
    (1726201, 2, 1983, 1741, 871, 248),
    (5212561, 2, 87, 119829, 59915, 11),
    (8813281, 5, 2099, 20994, 4199, 105),
)


BOUNDARY_CASES = (
    # (p, least normalized u, a, s, v, e, k).
    (193, 2, 1, 15, 13, 15, 2),
    (2521, 2, 7, 111, 159, 23, 2),
    (66529, 4, 11, 703, 1041, 95, 4),
)


def dual_k_bound(p: int, u: int) -> tuple[int, int]:
    """Return r_u and the exact upper bound for k in the fixed-u search."""
    modulus = 4 * u
    residue = (-p) % modulus
    if residue == 0:
        residue = modulus
    if residue <= u:
        raise ValueError("This residue bound requires r_u > u")
    return residue, (p + residue) // (4 * u * (residue - u))


def all_dual_witnesses(p: int, u: int) -> list[tuple[int, int, int, int, int]]:
    """Exhaust fixed-u search; return all (a,s,v,e,k) witnesses."""
    _, k_max = dual_k_bound(p, u)
    witnesses: list[tuple[int, int, int, int, int]] = []
    for k in range(1, k_max + 1):
        target = p + 4 * k * u * u
        modulus = 4 * u * k
        for s in positive_divisors(target):
            if (s + 1) % modulus:
                continue
            a = (s + 1) // modulus
            if gcd(u, a) != 1:
                continue
            e = target // s
            v = a * e - u
            if v <= 0:
                continue
            # Verify the reconstructed Dahan Type-II witness.
            if a * p + u != s * v:
                continue
            if p + e != 4 * u * v * k:
                continue
            witnesses.append((a, s, v, e, k))
    return witnesses


def find_dual_witness(p: int, u: int) -> tuple[int, int, int, int, int] | None:
    """Return the first witness in increasing k order, if one exists."""
    witnesses = all_dual_witnesses(p, u)
    return witnesses[0] if witnesses else None


def jacobi_symbol(a: int, n: int) -> int:
    """Compute the Jacobi symbol (a/n) for positive odd n."""
    if n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")
    a %= n
    result = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a %= n
    return result if n == 1 else 0


def is_prime_by_trial_division(n: int) -> bool:
    """Deterministic primality check, sufficient for the values in ROWS."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    limit = isqrt(n)
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2
    return True


def positive_divisors(n: int) -> list[int]:
    """Return every positive divisor using elementary trial factorization."""
    if n < 1:
        raise ValueError("n must be positive")

    factors: list[tuple[int, int]] = []
    remaining = n
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))

    result = [1]
    for prime, exponent in factors:
        old_divisors = result[:]
        prime_power = 1
        for _ in range(exponent):
            prime_power *= prime
            result.extend(d * prime_power for d in old_divisors)
    return sorted(result)


def has_type_ii_witness(p: int, max_u: int, max_a: int) -> bool:
    """Exhaustively test the complete bounded (u,a,s) search box."""
    for u in range(1, max_u + 1):
        for a in range(1, max_a + 1):
            if gcd(u, a) != 1:
                continue
            numerator = a * p + u
            for s in positive_divisors(numerator):
                if (s + 1) % (4 * u * a) == 0:
                    return True
    return False


class DahanHyperbolicExceptionCertificatesTest(unittest.TestCase):
    def test_all_fourteen_type_ii_certificates(self) -> None:
        self.assertEqual(len(ROWS), 14)
        self.assertLessEqual(max(row[1] for row in ROWS), 3)
        self.assertLessEqual(max(row[2] for row in ROWS), 5)

        for p, u, a, s, v, e, k in ROWS:
            with self.subTest(p=p, u=u, a=a):
                # Prime and congruence conditions for the published list.
                self.assertTrue(is_prime_by_trial_division(p))
                self.assertEqual(p % 24, 1)

                # Normalized Type-II divisor criterion.
                self.assertGreater(u, 0)
                self.assertGreater(a, 0)
                self.assertEqual(gcd(u, a), 1)
                self.assertGreater(s, 0)
                self.assertGreater(v, 0)
                self.assertGreater(e, 0)
                self.assertGreater(k, 0)
                self.assertEqual((a * p + u) % s, 0)
                self.assertEqual((s + 1) % (4 * u * a), 0)

                # Exact quotient and congruence reconstructions.
                self.assertEqual(a * p + u, s * v)
                self.assertEqual(s + 1, 4 * u * a * k)
                self.assertEqual(u + v, a * e)

                # Equivalent Type-II equation and Egyptian-fraction identity.
                self.assertEqual(p + e, 4 * u * v * k)
                self.assertEqual(4 * a * u * v * k, a * p + u + v)

    def test_all_fourteen_have_u1_witness_with_a_at_most6(self) -> None:
        self.assertEqual(len(U1_ROWS), 14)
        for p, a, s, v, e, k in U1_ROWS:
            with self.subTest(p=p):
                self.assertTrue(is_prime_by_trial_division(p))
                self.assertEqual(p % 24, 1)
                self.assertLessEqual(a, 6)
                self.assertEqual(a * p + 1, s * v)
                self.assertEqual(s + 1, 4 * a * k)
                self.assertEqual(1 + v, a * e)
                self.assertEqual(p + e, 4 * v * k)

        # The cap a <= 5 is insufficient on the u=1 slice exactly here.
        self.assertFalse(has_type_ii_witness(102001, max_u=1, max_a=5))

    def test_parameter_box_is_pareto_sharp_for_this_fourteen_prime_set(self) -> None:
        # With u <= 2 and a <= 5, p=102001 has no divisor witness.
        self.assertFalse(has_type_ii_witness(102001, max_u=2, max_a=5))
        # With u <= 3 and a <= 4, p=8813281 has no divisor witness.
        self.assertFalse(has_type_ii_witness(8813281, max_u=3, max_a=4))

        # Every other member of the 14-prime set does have a witness
        # in each of those respective boxes.
        for p, *_ in ROWS:
            if p != 102001:
                self.assertTrue(has_type_ii_witness(p, max_u=2, max_a=5), p)
            if p != 8813281:
                self.assertTrue(has_type_ii_witness(p, max_u=3, max_a=4), p)


    def test_three_project_boundary_primes_have_exact_minimal_u(self) -> None:
        expected_k_bounds = {
            193: {1: 24, 2: 5, 3: 2, 4: 1},
            2521: {1: 315, 2: 63, 3: 26, 4: 52},
            66529: {1: 8316, 2: 1663, 3: 693, 4: 378},
        }
        expected_counts = {
            193: {1: 0, 2: 2, 3: 0, 4: 0},
            2521: {1: 0, 2: 2, 3: 0, 4: 1},
            66529: {1: 0, 2: 0, 3: 0, 4: 1},
        }

        for p, min_u, a, s, v, e, k in BOUNDARY_CASES:
            with self.subTest(p=p):
                self.assertTrue(is_prime_by_trial_division(p))
                self.assertEqual(p % 24, 1)

                # Exhaust every allowed k and every divisor s for all u <= 4.
                # The proven k-bound means this also covers unrestricted a.
                for u in range(1, 5):
                    _, k_max = dual_k_bound(p, u)
                    self.assertEqual(k_max, expected_k_bounds[p][u])
                    witnesses = all_dual_witnesses(p, u)
                    self.assertEqual(len(witnesses), expected_counts[p][u])

                # The displayed certificate has the least possible u.
                self.assertEqual(len(all_dual_witnesses(p, min_u)), expected_counts[p][min_u])
                self.assertIn((a, s, v, e, k), all_dual_witnesses(p, min_u))
                self.assertEqual(gcd(min_u, a), 1)
                self.assertEqual(a * p + min_u, s * v)
                self.assertEqual(s + 1, 4 * min_u * a * k)
                self.assertEqual(min_u + v, a * e)
                self.assertEqual(p + e, 4 * min_u * v * k)
                self.assertEqual(s * e, p + 4 * k * min_u * min_u)

                # Dahan's global Jacobi reciprocity checks for this Type-II witness.
                self.assertEqual(jacobi_symbol(s, p), -1)
                self.assertEqual(jacobi_symbol(p, s), -1)
                self.assertEqual(jacobi_symbol(min_u * v, p), -1)
                self.assertEqual(jacobi_symbol(k * e, p), -1)



if __name__ == "__main__":
    unittest.main(verbosity=2)
