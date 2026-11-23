"""Factorization-free exact search for fixed-u Type-II witnesses.

For each floor-quotient candidate k, set L = 4*u*k and M = p + L*u.
A dual Type-II witness is a factorization M = s*e such that
    s == -1 (mod L), and gcd(u, (s+1)//L) == 1.
Every such factorization also forces e == -p (mod L).
At least one of s,e is <= sqrt(M). The algorithm enumerates the smaller
factor in its necessary residue class and tests divisibility directly.

This is an exact finite search for a fixed prime p == 1 (mod 24) and fixed
u in {1,2,3,4}; it does not impose an external upper bound on the modulator a.
It uses the Phase 7 quotient prefilter and only the Python standard library.
"""
from __future__ import annotations

from math import gcd, isqrt

from phase7_floor_quotient import (
    TypeIIWitness,
    _validate_parameters,
    floor_quotient_k_candidates,
)


def _least_positive_residue(residue: int, modulus: int) -> int:
    """Least positive representative of a residue class modulo modulus."""
    value = residue % modulus
    return value if value else modulus


def all_witnesses_small_factor(p: int, u: int) -> tuple[TypeIIWitness, ...]:
    """Return every normalized Type-II witness for fixed (p,u), exactly.

    For each Phase 7 candidate k, let L=4*u*k and M=p+4*k*u*u.
    A valid witness corresponds to M=s*e with s == -1 (mod L),
    a=(s+1)//L, gcd(a,u)=1, and the reconstructed quantities
        v = a*e-u
    satisfying v>0 and the original Type-II identity.

    We avoid integer factorization by splitting into two complete cases:
      1. s <= sqrt(M): enumerate s=L*a-1 directly;
      2. e <= sqrt(M): enumerate e == -p (mod L), then recover s=M/e.

    Every factor pair has at least one factor <= sqrt(M), so the search is
    complete. The return value is deduplicated and sorted.
    """
    _validate_parameters(p, u)
    found: set[TypeIIWitness] = set()

    for k in floor_quotient_k_candidates(p, u):
        modulus = 4 * u * k
        target = p + 4 * k * u * u
        root = isqrt(target)

        # Case 1: s is the smaller factor. Write s = modulus*a - 1.
        a_max = (root + 1) // modulus
        for a in range(1, a_max + 1):
            if gcd(a, u) != 1:
                continue
            s = modulus * a - 1
            if target % s:
                continue
            e = target // s
            v = a * e - u
            if e <= u or v <= 0:
                continue
            if a * p + u != s * v:
                continue
            if p + e != modulus * v:
                continue
            found.add(TypeIIWitness(u, a, s, v, e, k))

        # Case 2: e is the smaller factor. Since M == p (mod modulus)
        # and s == -1 (mod modulus), e must be == -p (mod modulus).
        e0 = _least_positive_residue(-p, modulus)
        if e0 <= root:
            e_count = (root - e0) // modulus + 1
            for j in range(e_count):
                e = e0 + j * modulus
                if target % e:
                    continue
                s = target // e
                if (s + 1) % modulus:
                    continue
                a = (s + 1) // modulus
                if gcd(a, u) != 1:
                    continue
                v = a * e - u
                if e <= u or v <= 0:
                    continue
                if a * p + u != s * v:
                    continue
                if p + e != modulus * v:
                    continue
                found.add(TypeIIWitness(u, a, s, v, e, k))

    return tuple(sorted(found))


def count_small_factor_divisibility_tests(p: int, u: int) -> int:
    """Count candidate divisibility tests performed by the two small-factor scans.

    This count measures the algorithm's arithmetic trial candidates, not wall
    time. Each candidate tests a single exact remainder M % d.
    """
    _validate_parameters(p, u)
    total = 0
    for k in floor_quotient_k_candidates(p, u):
        modulus = 4 * u * k
        root = isqrt(p + 4 * k * u * u)

        # Number of s=modulus*a-1 in [1, root].
        s_count = (root + 1) // modulus

        # Number of positive e == -p (mod modulus) in [1, root].
        e0 = _least_positive_residue(-p, modulus)
        e_count = 0 if e0 > root else (root - e0) // modulus + 1
        total += s_count + e_count
    return total
