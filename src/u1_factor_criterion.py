"""Exact finite search for the u=1 slice of Dahan's Type-II criterion.

Standard library only. The search uses a sharpened bound proved in
notes/ES4-U1-SHARP-BOUNDS.md:
    1 <= k <= floor((p+3)/20),
    1 <= a <= floor((p+11)/28).
It searches by divisors s | (p+4k), s == -1 (mod 4k).
This is an exact decision procedure for a fixed p, not a proof that u=1
works for every prime in the target residue class.
"""
from __future__ import annotations

from math import isqrt
from typing import Iterator


def factorization(n: int) -> list[tuple[int, int]]:
    """Return the prime factorization as (prime, exponent) pairs."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    out: list[tuple[int, int]] = []
    e = 0
    while n % 2 == 0 and n > 1:
        n //= 2
        e += 1
    if e:
        out.append((2, e))
    d = 3
    while d <= isqrt(n):
        e = 0
        while n % d == 0:
            n //= d
            e += 1
        if e:
            out.append((d, e))
        d += 2
    if n > 1:
        out.append((n, 1))
    return out


def positive_divisors(n: int) -> Iterator[int]:
    """Yield all positive divisors of n in increasing order."""
    fac = factorization(n)
    values = [1]
    for prime, exponent in fac:
        powers = [prime ** j for j in range(exponent + 1)]
        values = [x * y for x in values for y in powers]
    yield from sorted(values)


def sharp_u1_bounds(p: int) -> tuple[int, int]:
    """Return (a_max, k_max) for every u=1 witness when p == 1 mod 24."""
    if not isinstance(p, int) or isinstance(p, bool) or p < 2:
        raise ValueError("p must be an integer >= 2")
    if p % 24 != 1:
        raise ValueError("this sharpened bound is stated for p == 1 (mod 24)")
    return (p + 11) // 28, (p + 3) // 20


def witness_at_k(p: int, k: int) -> dict[str, int] | None:
    """Find a u=1 witness with this k, if one exists."""
    if p < 2 or k < 1:
        raise ValueError("p >= 2 and k >= 1 are required")
    modulus = 4 * k
    for s in positive_divisors(p + modulus):
        if (s + 1) % modulus:
            continue
        a = (s + 1) // modulus
        if a < 1:
            continue
        if (a * p + 1) % s:
            raise ArithmeticError("divisor criterion failed to reconstruct ap+1")
        t, rem = divmod(p + modulus, s)
        if rem or t * s != p + modulus:
            raise ArithmeticError("quotient reconstruction failed")
        if p + modulus != t * s or s != 4 * a * k - 1:
            raise ArithmeticError("factor identity failed")
        return {"p": p, "u": 1, "a": a, "k": k, "s": s, "t": t}
    return None


def find_u1_witness(p: int) -> dict[str, int] | None:
    """Decide the u=1 criterion for p == 1 (mod 24) using the sharp k bound."""
    _, k_max = sharp_u1_bounds(p)
    for k in range(1, k_max + 1):
        witness = witness_at_k(p, k)
        if witness is not None:
            a_max, _ = sharp_u1_bounds(p)
            if witness["a"] > a_max:
                raise ArithmeticError("witness violates the proved sharp a bound")
            return witness
    return None


def t3_witness(p: int) -> dict[str, int] | None:
    """Construct a t=3 witness iff (p+3)/4 has a prime factor == 2 (mod 3)."""
    if p < 2 or p % 24 != 1:
        raise ValueError("p must satisfy p == 1 (mod 24)")
    m = (p + 3) // 4
    for q, _ in factorization(m):
        if q % 3 == 2:
            a = (q + 1) // 3
            k = m // q
            s = 4 * a * k - 1
            if p + 4 * k != 3 * s or (a * p + 1) % s:
                raise ArithmeticError("t=3 construction failed exact verification")
            return {"p": p, "u": 1, "a": a, "k": k, "s": s, "t": 3, "q": q}
    return None


def certify_u1_failure(p: int) -> dict[str, object]:
    """Return a reproducible finite-scan summary; None witness means failure."""
    a_max, k_max = sharp_u1_bounds(p)
    witness = find_u1_witness(p)
    return {
        "p": p,
        "a_max": a_max,
        "k_max": k_max,
        "k_values_checked": k_max,
        "u1_witness": witness,
        "status": "witness found" if witness else "no u=1 witness in the complete bounded search",
    }


if __name__ == "__main__":
    for p in (73, 97, 193, 313, 2521, 66529, 1009):
        print(certify_u1_failure(p))
