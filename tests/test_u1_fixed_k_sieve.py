import unittest
from src.u1_fixed_k_sieve import (
    divisor_residue_representatives,
    fixed_k_witness,
    k1_witness_from_prime_factor,
    k2_coordinate_test,
    first_witness_up_to_k,
)


class TestFixedKSieve(unittest.TestCase):
    def test_divisor_residue_dp_against_brute_force(self):
        for n in range(1,60):
            for m in (4,8,12,16,20,24):
                got=set(divisor_residue_representatives(n,m))
                expected={d%m for d in range(1,n+1) if n%d==0}
                self.assertEqual(got,expected)

    def test_k1_prime_factor_criterion(self):
        w=k1_witness_from_prime_factor(73)
        self.assertIsNotNone(w)
        self.assertEqual((w["a"],w["s"],w["t"]),(2,7,11))
        self.assertIsNone(k1_witness_from_prime_factor(193))

    def test_k2_coordinate_criterion(self):
        for p in (97,337,433,457,577):
            result=k2_coordinate_test(p)
            self.assertTrue(result["witness_exists"])
            self.assertIsNotNone(result["witness"])
        self.assertEqual((k2_coordinate_test(97)["witness"]["a"],
                          k2_coordinate_test(97)["witness"]["s"]), (1,7))

    def test_k2_fails_for_selected_examples(self):
        for p in (73,193,2521,313,66529):
            result=k2_coordinate_test(p)
            self.assertFalse(result["witness_exists"])
            self.assertIsNone(result["witness"])

    def test_p313_first_witness_at_k4(self):
        self.assertIsNone(fixed_k_witness(313,1))
        self.assertIsNone(fixed_k_witness(313,2))
        self.assertIsNone(fixed_k_witness(313,3))
        w=fixed_k_witness(313,4)
        self.assertEqual((w["a"],w["s"],w["t"]),(3,47,7))

    def test_three_full_u1_failures_have_no_small_k_witness(self):
        for p in (193,2521,66529):
            self.assertIsNone(first_witness_up_to_k(p,12))

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            fixed_k_witness(100,1)
        with self.assertRaises(ValueError):
            fixed_k_witness(73,0)


if __name__=="__main__":
    unittest.main()
