import math
import sys
import unittest
from fractions import Fraction
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from phase14_totient_sublevel import (
    DEFAULT_DELTA0,
    DEFAULT_GAMMA,
    U_VALUES,
    euler_phi,
    finite_audit,
    kappa_for_parameters,
    kappa_limit,
    max_a_bound,
    pair_coefficient_A_infinity,
    tau_value,
)


class TotientSublevelTests(unittest.TestCase):
    def test_euler_phi_reference_values(self):
        expected = {1: 1, 2: 1, 4: 2, 8: 4, 12: 4, 24: 8, 36: 12, 60: 16, 84: 24}
        for n, value in expected.items():
            with self.subTest(n=n):
                self.assertEqual(euler_phi(n), value)


    def test_exact_totient_parametrization_for_all_four_u(self):
        B = {1: 2, 2: 4, 3: 4, 4: 8}
        for u in U_VALUES:
            for a in range(1, 201):
                if math.gcd(a, u) != 1:
                    continue
                radical_factor = Fraction(1, 1)
                x = a
                q = 2
                while q * q <= x:
                    if x % q == 0:
                        if q > 2 and (2 * u) % q != 0:
                            radical_factor *= Fraction(q - 1, q)
                        while x % q == 0:
                            x //= q
                    q += 1 if q == 2 else 2
                if x > 1 and x > 2 and (2 * u) % x != 0:
                    radical_factor *= Fraction(x - 1, x)
                rhs = B[u] * a * radical_factor
                with self.subTest(u=u, a=a):
                    self.assertEqual(Fraction(euler_phi(4 * u * a), 1), rhs)

    def test_constants_sum_to_pattern_limit(self):
        # The four counting constants are (1/2, 1/8, 1/7, 1/16)*Pi.
        pi_product = 105 * 1.2020569031595942854 / (math.pi**4)
        expected_sum = (93 / 112) * pi_product
        self.assertAlmostEqual(0.5*pi_product + 0.125*pi_product + (1/7)*pi_product + 0.0625*pi_product,
                               expected_sum, places=14)
        self.assertAlmostEqual(pair_coefficient_A_infinity(), 2*expected_sum, places=14)

    def test_kappa_is_close_to_the_limit(self):
        k = kappa_for_parameters(DEFAULT_GAMMA, DEFAULT_DELTA0)
        self.assertGreater(k, 0.01397)
        self.assertLess(k, kappa_limit())
        self.assertGreater(k / kappa_limit(), 0.997)

    def test_phi_square_root_bound(self):
        for n in range(1, 5000):
            with self.subTest(n=n):
                self.assertGreaterEqual(euler_phi(n) ** 2, n / 2)

    def test_totient_square_root_inequality_and_coordinate_bound(self):
        for n in range(1, 5000):
            with self.subTest(n=n):
                self.assertGreaterEqual(euler_phi(n) ** 2, n / 2)
        T = Fraction(249, 1)
        for u in U_VALUES:
            bound = max_a_bound(T, u)
            for a in range(1, min(bound + 100, 2000) + 1):
                if math.gcd(a, u) == 1 and euler_phi(4 * u * a) <= T:
                    self.assertLessEqual(a, bound)

    def test_finite_totient_sublevel_families(self):
        rows = [finite_audit(L) for L in (250, 500, 1000)]
        for L, row in zip((250, 500, 1000), rows):
            with self.subTest(L=L):
                self.assertGreater(row["pair_count_exact"], 0)
                self.assertGreater(row["J_actual_max_coordinate"], 4)
                self.assertLessEqual(row["J_actual_max_coordinate"], row["J_upper_bound_from_phi_square_inequality"])
        mean_target = rows[0]["predicted_mean_over_L"]
        count_target = rows[0]["predicted_pair_count_coefficient"]
        mean_errors = [abs(row["mean_over_L"] - mean_target) for row in rows]
        count_errors = [abs(row["pair_count_over_L_exact"] - count_target) for row in rows]
        self.assertLess(mean_errors[-1], mean_errors[-2])
        self.assertLess(mean_errors[-2], mean_errors[-3])
        self.assertLess(count_errors[-1], count_errors[-2])
        self.assertLess(count_errors[-2], count_errors[-3])

    def test_observed_pair_count_tracks_asymptotic_prediction(self):
        row = finite_audit(1000)
        predicted = row["predicted_pair_count_coefficient"]
        observed = row["observed_pair_count_coefficient"]
        self.assertLess(abs(observed - predicted), 0.01)

    def test_tau_parameter_is_exact(self):
        self.assertEqual(tau_value(), Fraction(8191, 65536))

    def test_rejects_invalid_parameters(self):
        for gamma, delta in ((Fraction(0), DEFAULT_DELTA0),
                             (Fraction(1), DEFAULT_DELTA0),
                             (DEFAULT_GAMMA, Fraction(0)),
                             (DEFAULT_GAMMA, Fraction(1, 8))):
            with self.subTest(gamma=gamma, delta=delta):
                with self.assertRaises(ValueError):
                    kappa_for_parameters(gamma, delta)

    def test_rejects_invalid_finite_audit(self):
        for L in (0, 19, True, 1.5):
            with self.subTest(L=L):
                with self.assertRaises(ValueError):
                    finite_audit(L)


if __name__ == "__main__":
    unittest.main()
