import unittest
from math import isqrt, gcd
from src.parameter_dictionary import (
    type_i_witness_to_pw, pw_type_i_to_witness,
    type_ii_witness_to_pw, pw_type_ii_to_witness,
    rosati_type_i_to_pw, rosati_type_ii_to_pw,
)


def primes_upto(limit):
    """Small standard-library sieve; avoids any third-party dependency."""
    if limit < 2:
        return []
    flags = [True] * (limit + 1)
    flags[0:2] = [False, False]
    for q in range(2, isqrt(limit) + 1):
        if flags[q]:
            for multiple in range(q * q, limit + 1, q):
                flags[multiple] = False
    return [q for q, flag in enumerate(flags) if flag]


class TestTypeICrosswalk(unittest.TestCase):
    def test_example_p73(self):
        pw = type_i_witness_to_pw(73, 2, 1, 15)
        self.assertEqual((pw["A"], pw["d"], pw["f"]), (1, 11, 15))
        back = pw_type_i_to_witness(73, pw["A"], pw["d"], pw["f"])
        self.assertEqual((back["u"], back["a"], back["s"]), (2, 1, 15))

    def test_rosati_type_i_example(self):
        r = rosati_type_i_to_pw(73, 1, 5, 2, 11)
        self.assertEqual((r["A_PW"], r["d_PW"], r["f_PW"]), (1, 11, 15))

    def test_nontrivial_rosati_gcd_type_i(self):
        # Rosati tuple has gcd(A,C)=3; normalization maps to P&W data (1,63,11).
        result = rosati_type_i_to_pw(241, 3, 66, 3, 7)
        self.assertEqual((result["A_PW"], result["d_PW"], result["f_PW"]),
                         (1, 63, 11))
        self.assertEqual(result["normalizing_gcd"], 3)

    def test_gcd_normalization_on_pw_input(self):
        # Raw P&W data (p,A,d,f)=(241,3,7,11): U=3 and gcd(A,U)=3.
        w = pw_type_i_to_witness(241, 3, 7, 11)
        self.assertEqual((w["u"], w["a"], w["s"], w["alpha"], w["normalizing_gcd"]),
                         (1, 1, 11, 63, 3))

    def test_bounded_generated_witnesses_roundtrip(self):
        count = 0
        for p in primes_upto(800):
            if p % 24 != 1:
                continue
            for u in range(1, min(p, 15)):
                for a in range(1, 16):
                    if gcd(u, a) != 1:
                        continue
                    for alpha in range(1, 15):
                        s = 4 * u * a * alpha - p
                        if s <= 0 or (a * p + u) % s:
                            continue
                        pw = type_i_witness_to_pw(p, u, a, s)
                        back = pw_type_i_to_witness(p, pw["A"], pw["d"], pw["f"])
                        self.assertEqual((back["u"], back["a"], back["s"]), (u, a, s))
                        count += 1
        self.assertGreater(count, 0)


class TestTypeIICrosswalk(unittest.TestCase):
    def test_example_p409(self):
        pw = type_ii_witness_to_pw(409, 1, 2, 7)
        self.assertEqual((pw["A"], pw["B"], pw["e"]), (1, 117, 59))
        back = pw_type_ii_to_witness(409, pw["A"], pw["B"], pw["e"])
        self.assertEqual((back["u"], back["a"], back["s"]), (1, 2, 7))

    def test_rosati_type_ii_example(self):
        r = rosati_type_ii_to_pw(409, 1, 117, 2, 1)
        self.assertEqual((r["A_PW"], r["B_PW"], r["e_PW"]), (1, 117, 59))

    def test_nontrivial_rosati_gcd_type_ii(self):
        # Rosati tuple has gcd(A,C)=2; normalized P&W Type-II data are (2,5,7).
        result = rosati_type_ii_to_pw(313, 4, 10, 2, 2)
        self.assertEqual((result["A_PW"], result["B_PW"], result["e_PW"]),
                         (2, 5, 7))
        self.assertEqual(result["normalizing_gcd"], 2)

    def test_gcd_normalization_roundtrip(self):
        # P&W data (p,A,B,e)=(313,4,10,7): the raw modulator is 2,
        # gcd(A,modulator)=2, and Dahan Lemma 3.10 normalizes it.
        w = pw_type_ii_to_witness(313, 4, 10, 7)
        self.assertEqual((w["u"], w["a"], w["s"], w["alpha"], w["normalizing_gcd"]),
                         (2, 1, 63, 8, 2))
        back = type_ii_witness_to_pw(313, w["u"], w["a"], w["s"])
        self.assertEqual((back["A"], back["B"], back["e"]), (2, 5, 7))

    def test_bounded_generated_witnesses_roundtrip(self):
        count = 0
        for p in primes_upto(800):
            if p % 24 != 1:
                continue
            for u in range(1, 16):
                for a in range(1, 16):
                    if gcd(u, a) != 1:
                        continue
                    for alpha in range(1, 15):
                        s = 4 * u * a * alpha - 1
                        if (a * p + u) % s:
                            continue
                        pw = type_ii_witness_to_pw(p, u, a, s)
                        back = pw_type_ii_to_witness(p, pw["A"], pw["B"], pw["e"])
                        self.assertEqual((back["u"], back["a"], back["s"]), (u, a, s))
                        count += 1
        self.assertGreater(count, 0)


if __name__ == "__main__":
    unittest.main()
