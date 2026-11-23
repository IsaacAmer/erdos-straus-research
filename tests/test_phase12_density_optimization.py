import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from phase12_density_optimization import (
    C_U,
    D_U,
    GAMMA,
    TAU,
    asymptotic_exponent_coefficient,
    asymptotic_pair_coefficient,
    rectangular_optimal_pair_coefficient,
    cutoff_coefficients,
    euler_phi,
    finite_profile,
)


class Phase12OptimizedDensityTests(unittest.TestCase):
    def test_euler_phi_reference_values(self):
        values = {1: 1, 4: 2, 8: 4, 12: 4, 24: 8, 36: 12, 60: 16, 84: 24}
        for n, expected in values.items():
            with self.subTest(n=n):
                self.assertEqual(euler_phi(n), expected)

    def test_small_u_totient_coefficients(self):
        expected = {
            1: 8 / math.pi**2,
            2: 16 / math.pi**2,
            3: 18 / math.pi**2,
            4: 32 / math.pi**2,
        }
        self.assertEqual(set(C_U), {1, 2, 3, 4})
        for u, value in expected.items():
            self.assertAlmostEqual(C_U[u], value, places=14)

    def test_pair_density_coefficient_exact_formula(self):
        expected = GAMMA * TAU * (361 * math.pi**2 / 1728)
        self.assertAlmostEqual(asymptotic_pair_coefficient(), expected, places=14)
        self.assertAlmostEqual(sum(D_U[u] / C_U[u] for u in D_U), 361 * math.pi**2 / 1728, places=14)

    def test_family_attains_99_percent_of_rectangular_optimum(self):
        self.assertAlmostEqual(
            asymptotic_pair_coefficient() / rectangular_optimal_pair_coefficient(),
            GAMMA,
            places=14,
        )
        for u, x_u in cutoff_coefficients().items():
            self.assertAlmostEqual(C_U[u] * x_u, GAMMA * TAU, places=14)

    def test_exponent_constant_exact_formula(self):
        expected = (5 / 96) * GAMMA * TAU * (361 * math.pi**2 / 1728)
        self.assertAlmostEqual(asymptotic_exponent_coefficient(), expected, places=14)
        self.assertGreater(asymptotic_exponent_coefficient(), 0.0131)

    def test_cutoff_order(self):
        x = cutoff_coefficients()
        self.assertGreater(x[1], x[2])
        self.assertGreater(x[2], x[3])
        self.assertGreater(x[3], x[4])
        self.assertTrue(all(v > 0 for v in x.values()))

    def test_finite_mean_condition_at_audit_values(self):
        for L in (100, 200, 500, 1000, 5000, 10000):
            with self.subTest(L=L):
                row = finite_profile(L)
                self.assertTrue(row["finite_mean_condition_passes"])
                self.assertGreater(row["pair_count_P"], 0)
                self.assertGreater(row["B_log_logz_over_logJ5"], 0)
                self.assertEqual(row["A_u_cutoffs"]["1"], row["J"])
                self.assertLessEqual(row["mean_phi_4ua_minus_2_exact"], row["theorem_4_6_mean_threshold"])

    def test_finite_mean_tracks_asymptotic_value(self):
        row = finite_profile(10000)
        target = GAMMA * TAU
        self.assertLess(abs(row["mean_over_L"] - target), 0.002)
        self.assertLess(abs(row["pair_count_over_L"] - asymptotic_pair_coefficient()), 0.002)

    def test_rejects_invalid_L(self):
        for value in (0, -1, 49, float("nan"), float("inf"), True):
            with self.subTest(value=value):
                with self.assertRaises(ValueError):
                    finite_profile(value)


if __name__ == "__main__":
    unittest.main()
