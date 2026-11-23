"""Floor-quotient prefilter for the fixed-u Type-II divisor search.

Mathematical setting: p > 1, p == 1 (mod 24), and 1 <= u <= 4.
The module uses Python's standard library only. The caller is responsible
for supplying a prime p in the stated residue class; the validation routine
checks the congruence and parameter range, but deliberately does not run an
expensive primality test on every call.

The prefilter is necessary, not sufficient: every genuine Type-II witness
produces a candidate k, but a candidate k still needs a valid divisor test.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import gcd, isqrt


@dataclass(frozen=True, order=True)
class TypeIIWitness:
    """A normalized Dahan Type-II witness (u, a, s, v, e, k)."""

    u: int
    a: int
    s: int
    v: int
    e: int
    k: int


def _validate_parameters(p: int, u: int) -> None:
    if not isinstance(p, int) or isinstance(p, bool) or p <= 1:
        raise ValueError("p must be an integer greater than 1")
    if p % 24 != 1:
        raise ValueError("p must satisfy p == 1 (mod 24)")
    if not isinstance(u, int) or isinstance(u, bool) or not 1 <= u <= 4:
        raise ValueError("u must be one of 1, 2, 3, 4")


def least_positive_residue_of_minus_p(p: int, u: int) -> int:
    """Return r_u in {1,...,4u} with r_u == -p (mod 4u)."""
    _validate_parameters(p, u)
    modulus = 4 * u
    residue = (-p) % modulus
    return residue if residue else modulus


def coarse_k_bound(p: int, u: int) -> int:
    """Proved upper bound floor((p+r_u)/(4u(r_u-u)))."""
    r_u = least_positive_residue_of_minus_p(p, u)
    if r_u <= u:
        # For p == 1 (mod 24), u <= 4, this branch is unreachable.
        raise ValueError("The required residue inequality r_u > u failed")
    return (p + r_u) // (4 * u * (r_u - u))


def floor_quotient_k_candidates(p: int, u: int) -> tuple[int, ...]:
    """Enumerate all k passing the exact floor-gap necessary condition.

    Let N = p+u and L = 4*u*k. A witness forces
        floor(N/(L-1)) > floor(N/L).
    The loop enumerates all drop positions L of floor(N/i), by walking
    through its distinct quotient blocks. It then retains multiples of 4u.

    The number of loop iterations is at most 2*floor(sqrt(N)).
    """
    _validate_parameters(p, u)
    n_value = p + u
    modulus = 4 * u
    k_max = coarse_k_bound(p, u)
    candidates: list[int] = []

    i = 1
    while i <= n_value:
        quotient = n_value // i

        # Any witness has floor(N/v) = L-1 = 4*u*k-1.  Iterating
        # distinct floor quotients therefore enumerates all possible L.
        if (quotient + 1) % modulus == 0:
            k = (quotient + 1) // modulus
            if 1 <= k <= k_max:
                candidates.append(k)

        # Skip the complete block on which floor(N/i) is constant.
        i = n_value // quotient + 1

    # The quotient-block construction is duplicate-free, but sorting makes
    # the public output stable and convenient for callers.
    return tuple(sorted(set(candidates)))


def slow_floor_gap_candidates(p: int, u: int) -> tuple[int, ...]:
    """Reference implementation: scan all k up to the proved coarse bound.

    Used for tests and small-prime cross-checks, not as the fast algorithm.
    """
    _validate_parameters(p, u)
    n_value = p + u
    k_max = coarse_k_bound(p, u)
    result = []
    for k in range(1, k_max + 1):
        length = 4 * u * k
        if n_value // (length - 1) > n_value // length:
            result.append(k)
    return tuple(result)


def candidate_v_interval(p: int, u: int, k: int) -> tuple[int, int]:
    """Return the necessary integer interval for v for a candidate k.

    A witness must have floor((p+u)/L) < v <= floor((p+u)/(L-1)),
    where L=4*u*k. The function raises if k is not a prefilter candidate.
    """
    _validate_parameters(p, u)
    if not isinstance(k, int) or isinstance(k, bool) or k < 1:
        raise ValueError("k must be a positive integer")
    if k not in floor_quotient_k_candidates(p, u):
        raise ValueError("k does not pass the floor-quotient prefilter")
    n_value = p + u
    length = 4 * u * k
    return n_value // length + 1, n_value // (length - 1)


def positive_divisors(n: int) -> tuple[int, ...]:
    """Return all positive divisors by transparent trial factorization.

    This intentionally simple routine is suitable for the small regression
    examples in the project. For large inputs, use a separately audited
    factorization backend; do not interpret this as a high-performance sieve.
    """
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")

    remaining = n
    factors: list[tuple[int, int]] = []
    divisor = 2
    while divisor * divisor <= remaining:
        if remaining % divisor == 0:
            exponent = 0
            while remaining % divisor == 0:
                remaining //= divisor
                exponent += 1
            factors.append((divisor, exponent))
        divisor = 3 if divisor == 2 else divisor + 2
    if remaining > 1:
        factors.append((remaining, 1))

    values = [1]
    for prime, exponent in factors:
        previous = values[:]
        prime_power = 1
        for _ in range(exponent):
            prime_power *= prime
            values.extend(value * prime_power for value in previous)
    return tuple(sorted(values))


def all_dual_type_ii_witnesses(p: int, u: int) -> tuple[TypeIIWitness, ...]:
    """Exhaust the dual-divisor search for this fixed p and u.

    For each prefiltered k, examine every divisor s of p+4*k*u^2 with
    s == -1 (mod 4*u*k). Reconstruct a,e,v and verify the original Dahan
    criterion exactly. This is complete for this fixed u, with no imposed
    external upper bound on a.

    Trial factorization makes this a verification/reference routine, not an
    optimized large-range search.
    """
    _validate_parameters(p, u)
    witnesses: list[TypeIIWitness] = []

    for k in floor_quotient_k_candidates(p, u):
        modulus = 4 * u * k
        target = p + 4 * k * u * u
        for s in positive_divisors(target):
            if (s + 1) % modulus:
                continue
            a = (s + 1) // modulus
            if gcd(u, a) != 1:
                continue
            e = target // s
            v = a * e - u
            if v <= 0:
                continue
            if a * p + u != s * v:
                continue
            if p + e != 4 * u * v * k:
                continue
            witnesses.append(TypeIIWitness(u, a, s, v, e, k))

    return tuple(sorted(set(witnesses)))


def distinct_quotient_count(n: int) -> int:
    """Count distinct values of floor(n/i), i=1,...,n."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    count = 0
    i = 1
    while i <= n:
        quotient = n // i
        count += 1
        i = n // quotient + 1
    return count


def prime_by_trial_division(n: int) -> bool:
    """Deterministic primality check used only for small regression inputs."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    divisor = 3
    limit = isqrt(n)
    while divisor <= limit:
        if n % divisor == 0:
            return False
        divisor += 2
    return True
