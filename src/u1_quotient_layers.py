"""Exact quotient-layer analysis for the u=1 Type-II criterion.

For prime p == 1 (mod 24), a u=1 witness can be written as
    p + 4k = t(4ak - 1),  t == 3 (mod 4).
Equivalently, with M_t=(p+t)/4, we need a divisor d|M_t with
    d == -1 (mod t),
then a=(d+1)/t and k=M_t/d.

All routines use only the Python standard library.
"""
from __future__ import annotations

from math import gcd, isqrt
from typing import Iterator


def factorization(n: int) -> list[tuple[int, int]]:
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    out: list[tuple[int, int]] = []
    e = 0
    while n % 2 == 0 and n > 1:
        n //= 2
        e += 1
    if e:
        out.append((2, e))
    q = 3
    while q <= isqrt(n):
        e = 0
        while n % q == 0:
            n //= q
            e += 1
        if e:
            out.append((q, e))
        q += 2
    if n > 1:
        out.append((n, 1))
    return out


def divisor_residue_representatives(n: int, modulus: int) -> dict[int, int]:
    """Map each residue mod modulus attained by a divisor to one divisor.

    Dynamic programming over the prime-power factorization is exact: every
    divisor is represented by choosing an exponent from 0 through e_q.
    """
    if modulus < 2:
        raise ValueError("modulus must be >= 2")
    reps = {1 % modulus: 1}
    for q, exponent in factorization(n):
        powers = [(q ** j, pow(q, j, modulus)) for j in range(exponent + 1)]
        new: dict[int, int] = {}
        for residue, divisor in reps.items():
            for integer_power, residue_power in powers:
                new_residue = (residue * residue_power) % modulus
                new.setdefault(new_residue, divisor * integer_power)
        reps = new
    return reps


def quotient_layer_witness(p: int, t: int) -> dict[str, int] | None:
    """Find a u=1 witness in the exact quotient layer t, if one exists."""
    if not isinstance(p, int) or isinstance(p, bool) or p < 2:
        raise ValueError("p must be an integer >= 2")
    if p % 24 != 1:
        raise ValueError("p must satisfy p == 1 (mod 24)")
    if not isinstance(t, int) or isinstance(t, bool) or t < 3 or t % 4 != 3:
        raise ValueError("t must be an integer >= 3 with t == 3 (mod 4)")
    if t > (p + 4) // 3:
        return None
    numerator = p + t
    if numerator % 4:
        raise ArithmeticError("p+t should be divisible by 4")
    M = numerator // 4
    reps = divisor_residue_representatives(M, t)
    d = reps.get(t - 1)
    if d is None:
        return None
    a, rem = divmod(d + 1, t)
    k, rem_k = divmod(M, d)
    if rem or rem_k or a < 1 or k < 1:
        raise ArithmeticError("divisor reconstruction did not give positive integers")
    s = 4 * a * k - 1
    if p + 4 * k != t * s:
        raise ArithmeticError("quotient-layer factorization failed")
    if (a * p + 1) % s:
        raise ArithmeticError("reconstructed witness fails s | ap+1")
    if (s + 1) % (4 * a):
        raise ArithmeticError("reconstructed witness fails congruence")
    return {"p": p, "u": 1, "t": t, "M": M, "d": d,
            "a": a, "k": k, "s": s}


def quotient_layer_report(p: int, t: int) -> dict[str, object]:
    """Return factorization and all attainable divisor residues for one layer."""
    if p % 24 != 1 or t < 3 or t % 4 != 3:
        raise ValueError("require p == 1 (mod 24), t >= 3, t == 3 (mod 4)")
    if t > (p + 4) // 3:
        raise ValueError("t exceeds the necessary upper bound")
    M = (p + t) // 4
    reps = divisor_residue_representatives(M, t)
    witness = quotient_layer_witness(p, t)
    return {
        "p": p,
        "t": t,
        "M": M,
        "factorization": factorization(M),
        "attainable_divisor_residues": sorted(reps),
        "target_residue": t - 1,
        "target_attained": (t - 1) in reps,
        "witness": witness,
    }


def t11_discrete_log_test(p: int) -> dict[str, object]:
    """Exact C_10 subset-sum test for the t=11 layer.

    2 is a primitive root mod 11 and -1 == 2^5 mod 11. If
    M_11=prod(q_i^e_i), a divisor congruent to -1 exists iff bounded
    exponents f_i in [0,e_i] can make sum f_i*log_2(q_i) == 5 mod 10.
    Any factor 11 must be selected with exponent zero for a nonzero target.
    """
    report = quotient_layer_report(p, 11)
    M = int(report["M"])
    logs = {1: 0, 2: 1, 4: 2, 8: 3, 5: 4,
            10: 5, 9: 6, 7: 7, 3: 8, 6: 9}
    reachable = {0}
    factor_logs = []
    for q, exponent in factorization(M):
        residue = q % 11
        if residue == 0:
            factor_logs.append((q, exponent, None))
            continue
        ell = logs[residue]
        factor_logs.append((q, exponent, ell))
        powers = {(j * ell) % 10 for j in range(exponent + 1)}
        reachable = {(x + y) % 10 for x in reachable for y in powers}
    return {
        "p": p,
        "M11": M,
        "factorization": factorization(M),
        "prime_factor_logs": factor_logs,
        "reachable_log_residues": sorted(reachable),
        "target_log_residue": 5,
        "witness_exists": 5 in reachable,
    }


def k_equals_one_family_witness(p: int, t: int) -> dict[str, int] | None:
    """Construct the immediate k=1 witness when p == -4 (mod t)."""
    if p % 24 != 1 or t < 3 or t % 4 != 3:
        raise ValueError("require p == 1 (mod 24), t >= 3, t == 3 (mod 4)")
    if gcd(t, 24) != 1 or (p + 4) % t:
        return None
    a, rem = divmod(p + t + 4, 4 * t)
    s, rem_s = divmod(p + 4, t)
    if rem or rem_s or a < 1 or s != 4 * a - 1:
        raise ArithmeticError("k=1 construction failed divisibility")
    if (a * p + 1) % s:
        raise ArithmeticError("k=1 construction failed original divisibility")
    return {"p": p, "u": 1, "t": t, "a": a, "k": 1, "s": s}


if __name__ == "__main__":
    for p in (193, 2521, 66529, 313, 73):
        print(f"p={p}")
        for t in (3, 7, 11):
            if t <= (p + 4) // 3:
                print(" ", quotient_layer_report(p, t))
        print(" t=11 logs:", t11_discrete_log_test(p))
