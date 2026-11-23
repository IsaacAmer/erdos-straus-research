"""Exact divisor-residue tests for the u=1 quotient layers t=15 and t=19.

Only the Python standard library is required.
For p == 1 (mod 24), a u=1 witness in layer t is equivalent to a
divisor d | (p+t)/4 with d == -1 (mod t).
"""
from __future__ import annotations

from math import isqrt
from typing import Dict, List, Optional, Tuple


def factorint(n: int) -> List[Tuple[int, int]]:
    """Trial-division factorization, intended for moderate research examples."""
    if n < 1:
        raise ValueError("n must be positive")
    out: List[Tuple[int, int]] = []
    e = 0
    while n % 2 == 0:
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


def divisor_residue_representatives(n: int, modulus: int) -> Dict[int, int]:
    """Map each attainable divisor residue to one actual positive divisor."""
    if n < 1 or modulus < 2:
        raise ValueError("require n >= 1 and modulus >= 2")
    states: Dict[int, int] = {1 % modulus: 1}
    for q, e in factorint(n):
        powers = [pow(q, j, modulus) for j in range(e + 1)]
        actual_powers = [q ** j for j in range(e + 1)]
        updated: Dict[int, int] = {}
        for residue, divisor in states.items():
            for j, power_residue in enumerate(powers):
                new_residue = residue * power_residue % modulus
                updated.setdefault(new_residue, divisor * actual_powers[j])
        states = updated
    return states


def layer_result(p: int, t: int) -> dict:
    """Exact u=1 quotient-layer result, including a reconstructed witness."""
    if p <= 0 or (p - 1) % 24:
        raise ValueError("p must be a positive integer congruent to 1 mod 24")
    if t < 3 or t % 4 != 3:
        raise ValueError("t must be >= 3 and congruent to 3 mod 4")
    if (p + t) % 4:
        raise ValueError("(p+t)/4 must be an integer")
    M = (p + t) // 4
    reps = divisor_residue_representatives(M, t)
    target = (-1) % t
    d = reps.get(target)
    witness = None
    if d is not None:
        a = (d + 1) // t
        k = M // d
        s = 4 * a * k - 1
        # Independent reconstruction checks.
        assert d % t == target
        assert d * k == M
        assert p + 4 * k == t * s
        assert s == 4 * a * k - 1
        witness = {"p": p, "u": 1, "t": t, "M": M,
                   "d": d, "a": a, "k": k, "s": s}
    return {
        "p": p, "t": t, "M": M, "factorization": factorint(M),
        "attainable_divisor_residues": sorted(reps),
        "target_residue": target, "target_attained": d is not None,
        "witness": witness,
    }


def t15_coordinates(q: int) -> Tuple[int, int]:
    """Return (alpha mod 4, beta mod 2) with q == 2^alpha*7^beta mod 15.

    q must be a unit modulo 15.
    """
    r = q % 15
    if r in (0, 3, 5, 6, 9, 10, 12):
        raise ValueError("q must be coprime to 15")
    table = {
        1: (0, 0), 2: (1, 0), 4: (2, 0), 8: (3, 0),
        7: (0, 1), 14: (1, 1), 13: (2, 1), 11: (3, 1),
    }
    return table[r]


def t15_coordinate_test(p: int) -> dict:
    """The C4 x C2 bounded-sum criterion for t=15."""
    if p <= 0 or (p - 1) % 24:
        raise ValueError("p must be a positive integer congruent to 1 mod 24")
    t = 15
    M = (p + t) // 4
    fac = factorint(M)
    states = {(0, 0)}
    factor_data = []
    for q, e in fac:
        if q % 3 == 0 or q % 5 == 0:
            factor_data.append((q, e, None))
            continue  # Such a prime power cannot appear in d == 14 (mod 15).
        alpha, beta = t15_coordinates(q)
        factor_data.append((q, e, (alpha, beta)))
        powers = [((j * alpha) % 4, (j * beta) % 2) for j in range(e + 1)]
        states = {
            ((x + da) % 4, (y + db) % 2)
            for (x, y) in states for (da, db) in powers
        }
    target = (1, 1)  # 14 == 2^1 * 7^1 (mod 15)
    return {
        "p": p, "t": 15, "M": M, "factorization": fac,
        "prime_factor_coordinates": factor_data,
        "reachable_coordinates": sorted(states),
        "target_coordinates": target,
        "witness_exists": target in states,
        "general_residue_test": layer_result(p, 15),
    }


def t19_discrete_log_test(p: int) -> dict:
    """Discrete-log criterion for t=19, where 2 is a primitive root."""
    if p <= 0 or (p - 1) % 24:
        raise ValueError("p must be a positive integer congruent to 1 mod 24")
    t = 19
    M = (p + t) // 4
    logs = {pow(2, j, t): j for j in range(t - 1)}
    assert len(logs) == t - 1 and pow(2, 9, t) == t - 1
    fac = factorint(M)
    reachable = {0}
    factor_data = []
    for q, e in fac:
        if q % t == 0:
            factor_data.append((q, e, None))
            continue
        ell = logs[q % t]
        factor_data.append((q, e, ell))
        reachable = {
            (r + j * ell) % (t - 1)
            for r in reachable for j in range(e + 1)
        }
    target = 9
    return {
        "p": p, "t": 19, "M": M, "factorization": fac,
        "prime_factor_logs": factor_data,
        "reachable_log_residues": sorted(reachable),
        "target_log_residue": target,
        "witness_exists": target in reachable,
        "general_residue_test": layer_result(p, 19),
    }


if __name__ == "__main__":
    for p in (193, 2521, 66529, 313, 73):
        print(f"p={p}")
        print("  t=15:", t15_coordinate_test(p))
        print("  t=19:", t19_discrete_log_test(p))
