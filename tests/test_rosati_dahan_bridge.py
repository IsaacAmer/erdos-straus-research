import unittest
from src.rosati_dahan_bridge import (
    dahan_type_ii_to_rosati, rosati_type_ii_to_dahan,
    normalized_type_i_witness_to_rosati, rosati_to_normalized_type_i_witness,
    verify_rosati_decomposition, verify_witness_decomposition,
)


class TestRosatiDahanBridge(unittest.TestCase):
    def test_type_ii_dahan_to_rosati(self):
        q = dahan_type_ii_to_rosati(409, 1, 2, 7)
        self.assertEqual((q["A"], q["B"], q["C"], q["D"]), (1, 117, 2, 1))
        self.assertTrue(verify_rosati_decomposition(409, 1, 117, 2, 1, "II"))

    def test_type_ii_rosati_to_dahan(self):
        q = rosati_type_ii_to_dahan(409, 1, 117, 2, 1)
        self.assertEqual((q["u"], q["a"], q["s"]), (1, 2, 7))
        self.assertTrue(verify_witness_decomposition(409, 1, 2, 7, "II"))

    def test_type_i_normalized_witness_to_rosati(self):
        q = normalized_type_i_witness_to_rosati(73, 2, 1, 15)
        self.assertEqual((q["A"], q["B"], q["C"], q["D"]), (1, 5, 2, 11))
        self.assertTrue(verify_rosati_decomposition(73, 1, 5, 2, 11, "I"))

    def test_type_i_rosati_to_normalized_witness(self):
        q = rosati_to_normalized_type_i_witness(73, 1, 5, 2, 11)
        self.assertEqual((q["u"], q["a"], q["s"]), (2, 1, 15))
        self.assertTrue(verify_witness_decomposition(73, 2, 1, 15, "I"))

    def test_type_ii_gcd_normalization(self):
        # Non-primitive Rosati variables reduce by g=2 to the Dahan witness
        # (u,a,s)=(2,1,63), with alpha multiplied by g^2.
        q = rosati_type_ii_to_dahan(313, 4, 10, 2, 2)
        self.assertEqual((q["u"], q["a"], q["s"], q["v"], q["alpha"]),
                         (2, 1, 63, 5, 8))

    def test_type_i_gcd_normalization(self):
        # Non-primitive Rosati variables reduce by g=2 to (u,a,s)=(2,1,7).
        q = rosati_to_normalized_type_i_witness(313, 2, 90, 4, 10)
        self.assertEqual((q["u"], q["a"], q["s"], q["v"], q["alpha"]),
                         (2, 1, 7, 45, 40))


    def test_finite_regression_witnesses(self):
        # Independent bounded sweep over p <= 2000, p == 1 (mod 24),
        # and coprime 1 <= u,a <= 7. Every discovered witness is mapped
        # Dahan -> Rosati -> Dahan and checked exactly.
        def primes_upto(limit):
            flags = [True] * (limit + 1)
            flags[0:2] = [False, False]
            for q in range(2, int(limit ** 0.5) + 1):
                if flags[q]:
                    for m in range(q*q, limit + 1, q):
                        flags[m] = False
            return [q for q, flag in enumerate(flags) if flag]

        def divisors(n):
            small, large = [], []
            q = 1
            while q*q <= n:
                if n % q == 0:
                    small.append(q)
                    if q*q != n:
                        large.append(n//q)
                q += 1
            return small + large[::-1]

        counts = {"I": 0, "II": 0}
        for p in primes_upto(2000):
            if p % 24 != 1:
                continue
            for a in range(1, 8):
                for u in range(1, 8):
                    import math
                    if math.gcd(u, a) != 1:
                        continue
                    modulus = 4*u*a
                    for s in divisors(a*p + u):
                        if (s + 1) % modulus == 0:
                            rosati = dahan_type_ii_to_rosati(p, u, a, s)
                            back = rosati_type_ii_to_dahan(
                                p, rosati["A"], rosati["B"], rosati["C"], rosati["D"])
                            self.assertEqual((back["u"], back["a"], back["s"]), (u, a, s))
                            counts["II"] += 1
                        if (s + p) % modulus == 0:
                            rosati = normalized_type_i_witness_to_rosati(p, u, a, s)
                            back = rosati_to_normalized_type_i_witness(
                                p, rosati["A"], rosati["B"], rosati["C"], rosati["D"])
                            self.assertEqual((back["u"], back["a"], back["s"]), (u, a, s))
                            counts["I"] += 1
        self.assertGreater(counts["II"], 0)
        self.assertGreater(counts["I"], 0)

    def test_reject_bad_type_ii_congruence(self):
        with self.assertRaises(ValueError):
            dahan_type_ii_to_rosati(409, 1, 2, 8)

    def test_reject_bad_type_i_congruence(self):
        with self.assertRaises(ValueError):
            normalized_type_i_witness_to_rosati(73, 2, 1, 14)

    def test_reject_wrong_rosati_type(self):
        with self.assertRaises(ValueError):
            rosati_type_ii_to_dahan(409, 1, 117, 2, 2)


if __name__ == "__main__":
    unittest.main()
