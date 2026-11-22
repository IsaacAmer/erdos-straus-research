"""Exact bounded-u search for normalized Dahan Type-II witnesses.

This module uses only the Python standard library. It investigates primes
p == 1 (mod 24) and normalized Type-II witnesses (u,a,s) satisfying

    gcd(u,a) = 1,
    s | a*p + u,
    s == -1 (mod 4*u*a).

The search is exhaustive for each fixed u because it enumerates a finite
quotient Q with a proved upper bound. It does not prove that u <= 4 works
for every prime, and it does not prove the Erdős--Straus conjecture.
"""
from __future__ import annotations

import argparse
from collections import Counter
from math import gcd, isqrt
from typing import Iterator


def positive_divisors(n: int) -> Iterator[int]:
    """Yield every positive divisor of n in increasing order."""
    if n < 1:
        raise ValueError("n must be positive")
    low: list[int] = []
    high: list[int] = []
    for d in range(1, isqrt(n) + 1):
        if n % d == 0:
            low.append(d)
            other = n // d
            if other != d:
                high.append(other)
    yield from low
    yield from reversed(high)


def primes_up_to(limit: int) -> Iterator[int]:
    """Sieve of Eratosthenes; yield all primes <= limit."""
    if limit < 2:
        return
    sieve = bytearray(b"\x01") * (limit + 1)
    sieve[0:2] = b"\x00\x00"
    for p in range(2, isqrt(limit) + 1):
        if sieve[p]:
            start = p * p
            count = (limit - start) // p + 1
            sieve[start : limit + 1 : p] = b"\x00" * count
    for n in range(2, limit + 1):
        if sieve[n]:
            yield n


def type_ii_witness_for_u(p: int, u: int) -> dict[str, int] | None:
    """Find a normalized Dahan Type-II witness for fixed p and u.

    Returns {p,u,a,Q,r,k,s}, or None if no such witness exists.
    The finite search is complete for this fixed u.
    """
    if not isinstance(p, int) or isinstance(p, bool) or p <= 0:
        raise ValueError("p must be a positive integer")
    if not isinstance(u, int) or isinstance(u, bool) or u <= 0:
        raise ValueError("u must be a positive integer")

    # If Q=(a*p+u)/s and s=4*u*a*k-1, then
    # p + (u+Q)/a = 4*u*Q*k. In particular a | (u+Q), and
    # 1 <= Q <= floor((p+u)/(4*u-1)).
    q_max = (p + u) // (4 * u - 1)
    for Q in range(1, q_max + 1):
        m = u + Q
        modulus = 4 * u * Q
        for a in positive_divisors(m):
            if gcd(u, a) != 1:
                continue
            r = m // a
            numerator = p + r
            if numerator % modulus:
                continue
            k = numerator // modulus
            if k < 1:
                continue
            s = 4 * u * a * k - 1
            # Exact independent checks of the original witness conditions.
            if (a * p + u) != Q * s:
                raise ArithmeticError("quotient reconstruction identity failed")
            if (a * p + u) % s or (s + 1) % (4 * u * a):
                raise ArithmeticError("reconstructed Type-II witness failed")
            return {"p": p, "u": u, "a": a, "Q": Q,
                    "r": r, "k": k, "s": s, "Q_max": q_max}
    return None


def minimal_u_witness(p: int, u_max: int = 4) -> dict[str, int] | None:
    """Return the first witness found for u=1,...,u_max."""
    if u_max < 1:
        raise ValueError("u_max must be positive")
    for u in range(1, u_max + 1):
        witness = type_ii_witness_for_u(p, u)
        if witness is not None:
            return witness
    return None



def rosati_type_ii_decomposition(p: int, witness: dict[str, int]) -> dict[str, object]:
    """Reconstruct and exactly verify the Rosati Type-II unit-fraction triple."""
    from fractions import Fraction

    u, a, s = witness["u"], witness["a"], witness["s"]
    g = gcd(u, a)
    un, an = u // g, a // g
    numerator = an * p + un
    if numerator % s:
        raise ArithmeticError("witness divisibility failed during Rosati reconstruction")
    if (s + 1) % (4 * un * an):
        raise ArithmeticError("witness congruence failed during Rosati reconstruction")
    B = numerator // s
    D = (s + 1) // (4 * un * an)
    A, C = un, an
    if 4 * A * B * C * D != A + B + p * C:
        raise ArithmeticError("Rosati Type-II Diophantine identity failed")
    if gcd(A * B * D, p) != 1:
        raise ArithmeticError("Rosati Type-II coprimality condition failed")
    denominators = (p * B * C * D, p * A * C * D, A * B * D)
    total = sum((Fraction(1, d) for d in denominators), Fraction(0, 1))
    if total != Fraction(4, p):
        raise ArithmeticError("exact Egyptian-fraction identity failed")
    return {"p": p, "A": A, "B": B, "C": C, "D": D,
            "denominators": denominators, "identity": total}

def run_scan(limit: int = 1_000_000, u_max: int = 4) -> dict[str, object]:
    """Exhaustively scan primes p <= limit with p == 1 (mod 24)."""
    counts: Counter[int] = Counter()
    failures: list[int] = []
    u1_failures: list[int] = []
    sample_witnesses: dict[int, dict[str, int]] = {}
    total = 0
    for p in primes_up_to(limit):
        if p % 24 != 1:
            continue
        total += 1
        first = type_ii_witness_for_u(p, 1)
        if first is None:
            u1_failures.append(p)
        witness = first
        if witness is None:
            for u in range(2, u_max + 1):
                witness = type_ii_witness_for_u(p, u)
                if witness is not None:
                    break
        if witness is None:
            failures.append(p)
        else:
            counts[witness["u"]] += 1
            if p in (193, 2521, 66529):
                sample_witnesses[p] = witness
    return {
        "limit": limit,
        "u_max": u_max,
        "prime_count": total,
        "minimal_u_counts": dict(sorted(counts.items())),
        "u1_failures": u1_failures,
        "no_witness_failures": failures,
        "special_witnesses": sample_witnesses,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=1_000_000)
    parser.add_argument("--u-max", type=int, default=4)
    args = parser.parse_args()
    report = run_scan(args.limit, args.u_max)
    print(f"limit: {report['limit']}")
    print(f"primes p <= limit with p == 1 (mod 24): {report['prime_count']}")
    print(f"minimal-u witness counts: {report['minimal_u_counts']}")
    print(f"u=1 failures: {report['u1_failures']}")
    print(f"no witness with u <= {args.u_max}: {report['no_witness_failures']}")
    for p, witness in report["special_witnesses"].items():
        print(f"special witness p={p}: {witness}")


if __name__ == "__main__":
    main()
