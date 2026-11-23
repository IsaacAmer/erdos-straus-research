import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from u1_t15_t19_layers import (
    divisor_residue_representatives,
    layer_result,
    t15_coordinate_test,
    t19_discrete_log_test,
)


class TestT15T19Layers(unittest.TestCase):
    def test_t15_coordinates_match_general_divisor_dp(self):
        for p in (73, 193, 313, 2521, 66529):
            result = t15_coordinate_test(p)
            self.assertEqual(
                result["witness_exists"],
                result["general_residue_test"]["target_attained"],
            )

    def test_t19_logs_match_general_divisor_dp(self):
        for p in (73, 193, 313, 2521, 66529):
            result = t19_discrete_log_test(p)
            self.assertEqual(
                result["witness_exists"],
                result["general_residue_test"]["target_attained"],
            )

    def test_known_t15_and_t19_failures(self):
        for p in (73, 193, 313, 2521, 66529):
            self.assertFalse(t15_coordinate_test(p)["witness_exists"])
            self.assertFalse(t19_discrete_log_test(p)["witness_exists"])

    def test_t7_and_t11_known_successes_remain(self):
        self.assertTrue(layer_result(73, 7)["target_attained"])
        self.assertTrue(layer_result(73, 11)["target_attained"])
        self.assertTrue(layer_result(313, 7)["target_attained"])

    def test_divisor_residue_dp_matches_direct_divisors(self):
        for n in range(1, 100):
            for m in (7, 11, 15, 19):
                expected = {d % m for d in range(1, n + 1) if n % d == 0}
                got = set(divisor_residue_representatives(n, m))
                self.assertEqual(got, expected)

    def test_reconstructed_witness_identity(self):
        result = layer_result(73, 7)
        w = result["witness"]
        self.assertIsNotNone(w)
        self.assertEqual(73 + 4 * w["k"], w["t"] * w["s"])
        self.assertEqual(w["s"], 4 * w["a"] * w["k"] - 1)


if __name__ == "__main__":
    unittest.main()
