"""Exact coordinate changes for Rosati and published Erdős–Straus criteria.

Type II is connected to Dahan Theorem 3.9 / Lemma 3.10. The normalized
Type-I witness used here is connected to Rosati and Pomerance–Weingartner
Corollary 2.2; it is NOT Dahan Theorem 3.14.

This module is a verification aid, not a proof of Erdős–Straus. It uses only
the Python standard library and exact integer/Fraction arithmetic.
"""
from __future__ import annotations

from fractions import Fraction
from math import gcd, isqrt
from typing import Dict, Tuple


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d <= isqrt(n):
        if n % d == 0:
            return False
        d += 2
    return True


def _positive(**values: int) -> None:
    for name, value in values.items():
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer")


def _prime_p(p: int) -> None:
    if not is_prime(p):
        raise ValueError("p must be prime")
    if p % 4 != 1:
        raise ValueError("this bridge is stated for primes p == 1 (mod 4)")


def _verify_rosati_type_ii(p: int, A: int, B: int, C: int, D: int) -> None:
    _positive(p=p, A=A, B=B, C=C, D=D)
    _prime_p(p)
    if 4 * A * B * C * D != A + B + p * C:
        raise ValueError("Rosati Type-II equation 4ABCD=A+B+pC fails")
    if gcd(A * B * D, p) != 1:
        raise ValueError("Rosati Type-II condition gcd(ABD,p)=1 fails")


def _verify_rosati_type_i(p: int, A: int, B: int, C: int, D: int) -> None:
    _positive(p=p, A=A, B=B, C=C, D=D)
    _prime_p(p)
    if 4 * A * B * C * D != p * (A + B) + C:
        raise ValueError("Rosati Type-I equation 4ABCD=p(A+B)+C fails")
    if gcd(A * B * C * D, p) != 1:
        raise ValueError("Rosati Type-I condition gcd(ABCD,p)=1 fails")


def dahan_type_ii_to_rosati(p: int, u: int, a: int, s: int) -> Dict[str, int]:
    """Dahan Thm. 3.9 witness -> Rosati's Type-II quadruple.

    Input: s | (a*p+u), s == -1 (mod 4*u*a).
    The theorem allows non-coprime (u,a); we normalize using gcd(u,a),
    as in Dahan Lemma 3.10, before producing Rosati parameters.
    """
    _positive(p=p, u=u, a=a, s=s)
    _prime_p(p)
    if (a * p + u) % s:
        raise ValueError("s must divide a*p+u")
    if (s + 1) % (4 * u * a):
        raise ValueError("s must be congruent to -1 modulo 4*u*a")

    g = gcd(u, a)
    u0, a0 = u // g, a // g
    # Dahan Lemma 3.10: the same s remains a divisor after reduction.
    if (a0 * p + u0) % s:
        raise ArithmeticError("gcd normalization did not preserve divisibility")
    if (s + 1) % (4 * u0 * a0):
        raise ArithmeticError("gcd normalization did not preserve congruence")

    B = (a0 * p + u0) // s
    D = (s + 1) // (4 * u0 * a0)
    A, C = u0, a0
    _verify_rosati_type_ii(p, A, B, C, D)
    return {"p": p, "A": A, "B": B, "C": C, "D": D,
            "u": A, "a": C, "s": s, "normalizing_gcd": g}


def rosati_type_ii_to_dahan(p: int, A: int, B: int, C: int, D: int) -> Dict[str, int]:
    """Rosati Type-II quadruple -> normalized Dahan Thm. 3.9 witness."""
    _verify_rosati_type_ii(p, A, B, C, D)
    g = gcd(A, C)
    if B % g:
        raise ArithmeticError("Rosati equation should force gcd(A,C) to divide B")
    u, a, v = A // g, C // g, B // g
    alpha = D * g * g
    s = 4 * u * a * alpha - 1
    if s * v != a * p + u:
        raise ArithmeticError("Rosati-to-Dahan Type-II identity failed")
    if (s + 1) % (4 * u * a):
        raise ArithmeticError("Type-II congruence failed")
    return {"p": p, "u": u, "a": a, "s": s, "v": v,
            "alpha": alpha, "normalizing_gcd": g}


def normalized_type_i_witness_to_rosati(p: int, u: int, a: int, s: int) -> Dict[str, int]:
    """Normalized Type-I witness -> Rosati Type-I quadruple.

    This normalized witness is equivalent to Pomerance–Weingartner
    Corollary 2.2 for m=4. It is not a criterion from Dahan Theorem 3.14.
    Input: gcd(u,a)=1, u<p, s | (a*p+u), s == -p (mod 4*u*a).
    """
    _positive(p=p, u=u, a=a, s=s)
    _prime_p(p)
    if gcd(u, a) != 1:
        raise ValueError("normalized Type-I witness requires gcd(u,a)=1")
    if u >= p:
        raise ValueError("normalized Type-I witness requires u<p")
    if (a * p + u) % s:
        raise ValueError("s must divide a*p+u")
    if (s + p) % (4 * u * a):
        raise ValueError("s must be congruent to -p modulo 4*u*a")

    B = (a * p + u) // s
    D = (s + p) // (4 * u * a)
    A, C = a, u
    _verify_rosati_type_i(p, A, B, C, D)
    return {"p": p, "A": A, "B": B, "C": C, "D": D,
            "u": u, "a": a, "s": s, "v": B, "alpha": D}


def rosati_to_normalized_type_i_witness(p: int, A: int, B: int, C: int, D: int) -> Dict[str, int]:
    """Rosati Type-I quadruple -> normalized witness equivalent to P&W Cor. 2.2.

    Do not cite this transformation as Dahan Theorem 3.14.
    """
    _verify_rosati_type_i(p, A, B, C, D)
    g = gcd(A, C)
    if B % g:
        raise ArithmeticError("Rosati equation should force gcd(A,C) to divide B")
    a, u, v = A // g, C // g, B // g
    alpha = D * g * g
    s = 4 * u * a * alpha - p
    if s * v != a * p + u:
        raise ArithmeticError("Rosati-to-normalized-Type-I identity failed")
    if gcd(u, a) != 1 or (s + p) % (4 * u * a):
        raise ArithmeticError("normalized Type-I witness conditions failed")
    if (a * p + u) % s:
        raise ArithmeticError("Type-I divisibility failed")
    if u >= p:
        raise ArithmeticError("normalized witness contradicts u<p")
    return {"p": p, "u": u, "a": a, "s": s, "v": v,
            "alpha": alpha, "normalizing_gcd": g}



def verify_rosati_decomposition(p: int, A: int, B: int, C: int, D: int, kind: str) -> bool:
    """Check the exact three-unit-fraction representation encoded by Rosati."""
    if kind == "II":
        _verify_rosati_type_ii(p, A, B, C, D)
        denoms = (p * B * C * D, p * A * C * D, A * B * D)
    elif kind == "I":
        _verify_rosati_type_i(p, A, B, C, D)
        denoms = (B * C * D, A * C * D, p * A * B * D)
    else:
        raise ValueError("kind must be 'I' or 'II'")
    return sum((Fraction(1, x) for x in denoms), Fraction(0, 1)) == Fraction(4, p)


def verify_witness_decomposition(p: int, u: int, a: int, s: int, kind: str) -> bool:
    """Check exact Rosati reconstruction of a Type-II or normalized Type-I witness."""
    if kind == "II":
        q = dahan_type_ii_to_rosati(p, u, a, s)
        A, B, C, D = q["A"], q["B"], q["C"], q["D"]
        return verify_rosati_decomposition(p, A, B, C, D, "II")
    if kind == "I":
        q = normalized_type_i_witness_to_rosati(p, u, a, s)
        A, B, C, D = q["A"], q["B"], q["C"], q["D"]
        return verify_rosati_decomposition(p, A, B, C, D, "I")
    raise ValueError("kind must be 'I' or 'II'")


# Backward-compatible aliases from the preliminary Phase-2 draft.
# The Type-I witness is normalized and sourced to Rosati/P&W Corollary 2.2,
# not to Dahan Theorem 3.14.
dahan_type_i_to_rosati = normalized_type_i_witness_to_rosati
rosati_type_i_to_dahan = rosati_to_normalized_type_i_witness
verify_dahan_decomposition = verify_witness_decomposition


if __name__ == "__main__":
    # Dahan Theorem 3.9 / Rosati Type II: p=409, (u,a,s)=(1,2,7).
    ii = dahan_type_ii_to_rosati(409, 1, 2, 7)
    print("Type II witness:", ii)
    print("Type II exact fraction check:", verify_rosati_decomposition(
        409, ii["A"], ii["B"], ii["C"], ii["D"], "II"))

    # Normalized Type-I witness / Rosati / P&W Corollary 2.2: p=73, (u,a,s)=(2,1,15).
    i = normalized_type_i_witness_to_rosati(73, 2, 1, 15)
    print("Normalized Type-I witness:", i)
    print("Type I exact fraction check:", verify_rosati_decomposition(
        73, i["A"], i["B"], i["C"], i["D"], "I"))
