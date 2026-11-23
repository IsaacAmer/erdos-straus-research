import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
src=str(ROOT/'src')
if src not in sys.path: sys.path.insert(0,src)

import unittest
from dataclasses import replace
from phase7_floor_quotient import prime_by_trial_division
from phase8_small_factor import all_witnesses_small_factor
from phase10_jacobi_audit import audit_type_ii_witness, audit_witness_collection, jacobi_symbol

SAMPLE_PRIMES=(193,2521,66529,10009,100057,1000033,10000537,100000081,1000000009)
EXPECTED={193:2,2521:3,66529:1,10009:24,100057:24,1000033:33,10000537:42,100000081:49,1000000009:68}

class JacobiSymbolTests(unittest.TestCase):
    def test_standard_values(self):
        self.assertEqual(jacobi_symbol(1,15),1)
        self.assertEqual(jacobi_symbol(2,73),1)
        self.assertEqual(jacobi_symbol(3,73),1)
        self.assertEqual(jacobi_symbol(5,13),-1)
        self.assertEqual(jacobi_symbol(0,15),0)
        self.assertEqual(jacobi_symbol(-1,73),1)
    def test_quadratic_reciprocity_on_odd_coprime_inputs(self):
        from math import gcd
        for a in range(1,40,2):
            for n in range(3,42,2):
                if gcd(a,n)==1:
                    expected=jacobi_symbol(n,a)*(-1 if a%4==3 and n%4==3 else 1)
                    self.assertEqual(jacobi_symbol(a,n),expected)
    def test_rejects_invalid_denominator(self):
        for n in (0,-3,2,18):
            with self.subTest(n=n):
                with self.assertRaises(ValueError): jacobi_symbol(3,n)

class TypeIIJacobiAuditTests(unittest.TestCase):
    def test_known_p73_witnesses(self):
        ws=all_witnesses_small_factor(73,1)
        self.assertEqual(len(ws),2)
        for w in ws:
            report=audit_type_ii_witness(73,w)
            self.assertTrue(report.identities_ok)
            self.assertTrue(report.jacobi_laws_ok)
            self.assertTrue(report.passed)
    def test_all_246_witnesses_satisfy_published_jacobi_laws(self):
        total=0
        for p in SAMPLE_PRIMES:
            self.assertEqual(p%24,1)
            self.assertTrue(prime_by_trial_division(p))
            subtotal=0
            for u in range(1,5):
                ws=all_witnesses_small_factor(p,u)
                report=audit_witness_collection(p,ws)
                self.assertTrue(report['all_passed'],report)
                subtotal+=len(ws)
            self.assertEqual(subtotal,EXPECTED[p])
            total+=subtotal
        self.assertEqual(total,246)
    def test_rejects_composite_or_wrong_residue_prime(self):
        w=all_witnesses_small_factor(73,1)[0]
        for p in (75,121,193*193,101):
            with self.subTest(p=p):
                with self.assertRaises(ValueError): audit_type_ii_witness(p,w)
    def test_detects_corrupted_witness(self):
        w=all_witnesses_small_factor(73,1)[0]
        bad=replace(w,s=w.s+4)
        report=audit_witness_collection(73,[bad])
        self.assertEqual(report['failed_count'],1)
        self.assertFalse(report['all_passed'])

if __name__=='__main__': unittest.main(verbosity=2)
