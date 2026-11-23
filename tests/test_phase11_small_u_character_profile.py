import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=str(ROOT/'src')
if src not in sys.path: sys.path.insert(0,src)

import unittest
from math import gcd
from phase11_small_u_character_profile import (
    character_kernel_profile,
    explicit_square_class_conditions,
    factorization,
    is_square_unit_modulus,
    prime_factor_square_class_span_certificate,
    scan_modulator_box,
)


def brute_is_square(x,m):
    if gcd(x,m)!=1:return False
    target=x%m
    return any((z*z)%m==target for z in range(m) if gcd(z,m)==1)


def character_class_vector(x,m):
    fac=factorization(m)
    bits=[]
    v2=next((e for q,e in fac if q==2),0)
    if v2>=3:
        bits.extend({1:(0,0),3:(1,0),5:(0,1),7:(1,1)}[x%8])
    elif v2==2:
        bits.append(1 if x%4==3 else 0)
    for q,e in fac:
        if q!=2:
            bits.append(1 if pow(x%q,(q-1)//2,q)==q-1 else 0)
    return tuple(bits)


def brute_odd_character_count_with_chi_r_minus_one(u,a):
    m=4*u*a; r=a+u
    vm=character_class_vector(-1,m); vr=character_class_vector(r,m)
    d=len(vm); total_odd=0; count=0
    for mask in range(1<<d):
        dotm=sum(((mask>>i)&1)*vm[i] for i in range(d))%2
        dotr=sum(((mask>>i)&1)*vr[i] for i in range(d))%2
        if dotm==1:
            total_odd+=1
            if dotr==1: count+=1
    return count,total_odd


class SmallUSquareClassTests(unittest.TestCase):
    def test_local_square_test_matches_brute_force(self):
        for u in range(1,5):
            for a in range(1,121):
                if gcd(u,a)!=1 or (a+u)%2==0:continue
                m=4*u*a;r=a+u
                with self.subTest(u=u,a=a):
                    self.assertEqual(is_square_unit_modulus(r,m),brute_is_square(r,m))
                    self.assertEqual(is_square_unit_modulus(-r,m),brute_is_square(-r,m))

    def test_explicit_r_square_table_matches_local_criteria(self):
        for u in range(1,5):
            for a in range(1,2001):
                if gcd(u,a)!=1 or (a+u)%2==0:continue
                m=4*u*a;r=a+u
                expected=explicit_square_class_conditions(u,a)
                with self.subTest(u=u,a=a):
                    self.assertEqual(expected[0],is_square_unit_modulus(r,m))
                    self.assertEqual(expected[1],is_square_unit_modulus(-r,m))

    def test_minus_r_is_never_a_square_for_u_at_most_four(self):
        for u in range(1,5):
            for a in range(1,5001):
                if gcd(u,a)!=1 or (a+u)%2==0:continue
                with self.subTest(u=u,a=a):
                    self.assertFalse(is_square_unit_modulus(-(a+u),4*u*a))

    def test_exact_odd_character_count_by_linear_algebra(self):
        samples=[]
        for u in range(1,5):
            for a in range(2,101):
                if gcd(u,a)==1 and (a+u)%2==1:
                    samples.append((u,a))
        for u,a in samples:
            p=character_kernel_profile(u,a)
            actual,total=brute_odd_character_count_with_chi_r_minus_one(u,a)
            with self.subTest(u=u,a=a):
                self.assertEqual(total,p.odd_character_count)
                self.assertEqual(actual,p.odd_characters_with_chi_r_minus_one)

    def test_dihedral_scope_and_source_scope_flags(self):
        self.assertTrue(character_kernel_profile(1,2).dahan_theorem_2_6_ab_applies)
        self.assertTrue(character_kernel_profile(1,2).dahan_theorem_2_6_c_cycle_bound_applies)
        self.assertTrue(character_kernel_profile(1,6).dahan_theorem_2_6_ab_applies)
        self.assertFalse(character_kernel_profile(1,6).dahan_theorem_2_6_c_cycle_bound_applies)
        self.assertFalse(character_kernel_profile(4,3).dahan_theorem_2_6_ab_applies)
        self.assertFalse(character_kernel_profile(4,3).dahan_theorem_2_6_c_cycle_bound_applies)
        self.assertTrue(character_kernel_profile(2,3).dahan_theorem_2_8b_as_stated_applies)
        self.assertTrue(character_kernel_profile(1,2).elementary_u1_extension_applies)
        self.assertTrue(character_kernel_profile(2,1).dahan_theorem_2_8a_applies)
        self.assertTrue(character_kernel_profile(2,1).exceptional_a1_character_applies)
        self.assertTrue(character_kernel_profile(4,1).exceptional_a1_character_applies)
        self.assertFalse(character_kernel_profile(4,1).dahan_theorem_2_8a_applies)

    def test_a_equals_one_character_obstructions(self):
        # (u,a)=(2,1): chi_4 has chi_4(-1)=chi_4(3)=-1,
        # and p+2 == 3 (mod 4) for p == 1 (mod 24).
        chi4 = lambda n: 1 if n % 4 == 1 else -1
        self.assertEqual(chi4(3), -1)
        self.assertEqual(chi4(193 + 2), -1)
        # (u,a)=(4,1): chi_-8 has chi_-8(-1)=-1, chi_-8(5)=-1;
        # p+4 == 5 (mod 8), so multiplicativity excludes T from its kernel.
        def chi_minus8(n):
            n %= 8
            if n % 2 == 0:
                return 0
            chi_minus1 = -1 if n % 4 == 3 else 1
            chi_2 = -1 if n % 8 in (3, 5) else 1
            return chi_minus1 * chi_2
        self.assertEqual(chi_minus8(5), -1)
        self.assertEqual(chi_minus8(193 + 4), -1)
        # The character-span certificate must remain complete in both cases.
        for p, u, a in ((193, 2, 1), (193, 4, 1)):
            cert = prime_factor_square_class_span_certificate(p, u, a)
            self.assertTrue(cert["quotient_is_square_modulus"])
            self.assertTrue(cert["multiplicativity_obstruction_source"])

    def test_dihedral_maximal_subset_bound_example(self):
        p=character_kernel_profile(1,2)
        self.assertEqual(p.modulus,8)
        self.assertEqual(p.dihedral_order,2)
        self.assertEqual(p.maximum_size_admissible_subset_count_exponent,0)

    def test_prime_factor_square_class_span_certificates(self):
        samples=((73,1,2),(193,1,2),(193,2,3),(2521,4,3),(10009,3,2),(100057,2,3),(193,2,1),(193,4,1))
        for p,u,a in samples:
            with self.subTest(p=p,u=u,a=a):
                cert=prime_factor_square_class_span_certificate(p,u,a)
                self.assertIn(cert["target_square_class"],("-1","r"))
                self.assertTrue(cert["quotient_is_square_modulus"])
                self.assertFalse(cert["minus_r_is_square"])
                self.assertTrue(set(cert["selected_prime_factors"]).issubset(set(cert["distinct_prime_factors"])))
                self.assertGreaterEqual(cert["selected_subproduct"],1)
                self.assertEqual(cert["selected_prime_factor_count"], len(cert["selected_prime_factors"]))
                self.assertLessEqual(cert["selected_prime_factor_count"], cert["square_class_group_dimension"])
                if not cert["r_is_square"]:
                    self.assertTrue(cert["selected_prime_factors"])

    def test_parameter_box_counts_through_10000(self):
        result=scan_modulator_box(10000)
        rows={r['u']:r for r in result['summary_by_u']}
        expected={
          1:(5000,1250,3750,5000,2500,1250,2500,1250),
          2:(4999,466,4533,4999,2499,2034,2499,466),
          3:(3334,229,3105,3334,1668,1437,1668,229),
          4:(4999,1250,3749,0,0,3749,0,1250),
        }
        for u,vals in expected.items():
            r=rows[u]
            got=(r['valid_parameter_pairs'],r['r_square_pairs'],r['character_filter_active_pairs'],
                 r['theorem_2_6_ab_pairs'],r['theorem_2_6_c_cycle_bound_pairs'],
                 r['character_only_relative_to_cycle_bound'],r['both_character_and_cycle_bound'],
                 r['neither_character_nor_cycle_bound'])
            self.assertEqual(got,vals)
            self.assertEqual(r['minus_r_square_pairs'],0)

    def test_rejects_invalid_pair(self):
        for u,a in ((0,1),(5,1),(2,4),(1,3),(3,6)):
            with self.subTest(u=u,a=a):
                with self.assertRaises(ValueError): character_kernel_profile(u,a)

if __name__=='__main__': unittest.main(verbosity=2)
