"""Exact finite checks for the Dahan--Bradford divisor criteria.

The code checks the algebraic correspondence for a finite set of primes and
shifts. It is a regression test, not a proof of the universal conjecture.
Only Python's standard library is required.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt
from typing import Iterable


@dataclass(frozen=True)
class Witness:
    u: int
    v: int
    branch: str  # "Type I" (twisted) or "Type II" (untwisted)
    d: int


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    q = 3
    while q * q <= n:
        if n % q == 0:
            return False
        q += 2
    return True


def divisors(n: int) -> list[int]:
    if n < 1:
        raise ValueError("n must be positive")
    low: list[int] = []
    high: list[int] = []
    for q in range(1, isqrt(n) + 1):
        if n % q == 0:
            low.append(q)
            if q * q != n:
                high.append(n // q)
    return low + high[::-1]


def factorization(n: int) -> list[tuple[int, int]]:
    """Return (prime, exponent) pairs using elementary trial division."""
    if n < 1:
        raise ValueError("n must be positive")
    out: list[tuple[int, int]] = []
    q = 2
    while q * q <= n:
        if n % q == 0:
            e = 0
            while n % q == 0:
                n //= q
                e += 1
            out.append((q, e))
        q = 3 if q == 2 else q + 2
    if n > 1:
        out.append((n, 1))
    return out


def admissible_parameters(p: int, c: int) -> int:
    """Validate a Bradford-range prime/shift pair and return K=(p+c)/4.

    p must be prime, p == 1 (mod 4), c == 3 (mod 4), and
    0 < c <= p+2. This is the overlap with Bradford's smallest-denominator
    range x <= ceil(p/2), for p == 1 (mod 4).
    """
    if not is_prime(p) or p % 4 != 1:
        raise ValueError("p must be prime and congruent to 1 modulo 4")
    if c <= 0 or c % 4 != 3 or c > p + 2:
        raise ValueError("c must satisfy 0 < c <= p+2 and c == 3 (mod 4)")
    K, rem = divmod(p + c, 4)
    if rem or K <= 0:
        raise ValueError("(p+c)/4 must be a positive integer")
    if gcd(c, p * K) != 1:
        raise ArithmeticError("expected gcd(c,pK)=1 in this range")
    return K


def dahan_witnesses(p: int, c: int) -> list[tuple[int, int]]:
    """All unordered coprime divisor pairs u,v | pK with c | u+v."""
    K = admissible_parameters(p, c)
    M = p * K
    ds = divisors(M)
    out: list[tuple[int, int]] = []
    for i, u in enumerate(ds):
        for v in ds[i:]:
            if gcd(u, v) == 1 and (u + v) % c == 0:
                out.append((u, v))
    return out


def dahan_pair_to_bradford(p: int, c: int, u: int, v: int) -> Witness:
    """Map one Dahan pair to its Bradford divisor witness."""
    K = admissible_parameters(p, c)
    M = p * K
    if M % u or M % v or gcd(u, v) != 1 or (u + v) % c:
        raise ValueError("(u,v) is not a valid Dahan witness")

    if u % p == 0 or v % p == 0:
        # Exactly one can be divisible by p because gcd(u,v)=1.
        if u % p != 0:
            u, v = v, u
        r, s = u // p, v
        if K * s % r:
            raise ArithmeticError("Type I transfer did not produce an integer")
        d = K * s // r
        branch = "Type I"
    else:
        # Both are divisors of K. Order u <= v for d <= K.
        if u > v:
            u, v = v, u
        if K * u % v:
            raise ArithmeticError("Type II transfer did not produce an integer")
        d = K * u // v
        branch = "Type II"

    if K * K % d:
        raise ArithmeticError("transferred d does not divide K^2")
    if branch == "Type I" and (d + p * K) % c:
        raise ArithmeticError("Type I congruence failed")
    if branch == "Type II" and (d > K or (d + K) % c):
        raise ArithmeticError("Type II conditions failed")
    return Witness(u, v, branch, d)


def bradford_divisors(p: int, c: int) -> tuple[list[int], list[int]]:
    """Return (Type I d's, Type II d's) in Bradford's divisor criterion."""
    K = admissible_parameters(p, c)
    type_i: list[int] = []
    type_ii: list[int] = []
    for d in divisors(K * K):
        if (d + p * K) % c == 0:
            type_i.append(d)
        if d <= K and (d + K) % c == 0:
            type_ii.append(d)
    return type_i, type_ii


def bradford_to_dahan(p: int, c: int, d: int, branch: str) -> tuple[int, int]:
    """Map a Bradford divisor witness back to a Dahan coprime divisor pair."""
    K = admissible_parameters(p, c)
    if d <= 0 or K * K % d:
        raise ValueError("d must be a positive divisor of K^2")

    exponents = factorization(K)
    f_by_q = {q: 0 for q, _ in exponents}
    for q, _ in factorization(d):
        if q not in f_by_q:
            raise ValueError("d contains a prime not dividing K")
    for q, e in exponents:
        f = 0
        temp = d
        while temp % q == 0:
            temp //= q
            f += 1
        if f > 2 * e:
            raise ValueError("d does not divide K^2")
        f_by_q[q] = f

    if branch == "Type II":
        if d > K or (d + K) % c:
            raise ValueError("d does not satisfy Bradford Type II")
        u = v = 1
        for q, e in exponents:
            f = f_by_q[q]
            u *= q ** max(f - e, 0)
            v *= q ** max(e - f, 0)
    elif branch == "Type I":
        if (d + p * K) % c:
            raise ValueError("d does not satisfy Bradford Type I")
        r = s = 1
        for q, e in exponents:
            f = f_by_q[q]
            r *= q ** max(e - f, 0)
            s *= q ** max(f - e, 0)
        u, v = p * r, s
    else:
        raise ValueError("branch must be 'Type I' or 'Type II'")

    if (p * K) % u or (p * K) % v or gcd(u, v) != 1 or (u + v) % c:
        raise ArithmeticError("reverse transfer did not produce a Dahan witness")
    return u, v


def verify_prime_shift(p: int, c: int) -> dict[str, int | bool]:
    """Check both directions for every witness at one (p,c)."""
    K = admissible_parameters(p, c)
    pairs = dahan_witnesses(p, c)
    type_i, type_ii = bradford_divisors(p, c)

    mapped_i: set[int] = set()
    mapped_ii: set[int] = set()
    for u, v in pairs:
        witness = dahan_pair_to_bradford(p, c, u, v)
        if witness.branch == "Type I":
            mapped_i.add(witness.d)
        else:
            mapped_ii.add(witness.d)

    for d in type_i:
        bradford_to_dahan(p, c, d, "Type I")
    for d in type_ii:
        bradford_to_dahan(p, c, d, "Type II")

    # Every Dahan witness must map to a divisor found by the Bradford scan;
    # and every Bradford witness must map back to a Dahan pair.
    if not mapped_i.issubset(set(type_i)) or not mapped_ii.issubset(set(type_ii)):
        raise AssertionError(f"forward mismatch at p={p}, c={c}")
    if bool(pairs) != bool(type_i or type_ii):
        raise AssertionError(f"existence mismatch at p={p}, c={c}")

    return {
        "p": p,
        "c": c,
        "K": K,
        "dahan_pairs": len(pairs),
        "type_i_divisors": len(type_i),
        "type_ii_divisors": len(type_ii),
        "equivalence_checked": True,
    }


def run_small_audit(prime_limit: int = 300) -> list[dict[str, int | bool]]:
    """Run a complete finite comparison over admissible p and c <= p+2."""
    if prime_limit < 5:
        raise ValueError("prime_limit must be at least 5")
    records: list[dict[str, int | bool]] = []
    for p in range(5, prime_limit + 1):
        if not is_prime(p) or p % 4 != 1:
            continue
        for c in range(3, p + 3, 4):
            records.append(verify_prime_shift(p, c))
    return records


if __name__ == "__main__":
    records = run_small_audit(300)
    print(f"checked prime-shift pairs: {len(records)}")
    print(f"prime values checked: {len({r['p'] for r in records})}")
    print(f"all equivalence checks passed: {all(r['equivalence_checked'] for r in records)}")
    sample = verify_prime_shift(73, 7)
    print("sample p=73, c=7:", sample)
