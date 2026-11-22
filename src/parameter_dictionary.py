"""Exact crosswalks among Rosati, Dahan, and Pomerance--Weingartner criteria.

Scope: odd primes p == 1 (mod 4), with the intended application p == 1 (mod 24).
All checks use exact integer arithmetic. This is a criterion translator, not a
proof of the Erdős--Straus conjecture.
"""
from __future__ import annotations

from math import gcd, isqrt
from typing import Dict


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


def _positive(**kw: int) -> None:
    for k, v in kw.items():
        if not isinstance(v, int) or isinstance(v, bool) or v <= 0:
            raise ValueError(f"{k} must be a positive integer")


def _prime_scope(p: int) -> None:
    _positive(p=p)
    if not is_prime(p) or p % 4 != 1:
        raise ValueError("p must be prime and congruent to 1 modulo 4")


def _check_type_i_witness(p: int, u: int, a: int, s: int) -> None:
    _prime_scope(p)
    _positive(u=u, a=a, s=s)
    if gcd(u, a) != 1:
        raise ValueError("normalized Type-I witness requires gcd(u,a)=1")
    if u >= p:
        raise ValueError("normalized Type-I witness requires u<p")
    if (a * p + u) % s:
        raise ValueError("s must divide a*p+u")
    if (s + p) % (4 * u * a):
        raise ValueError("s must be congruent to -p modulo 4*u*a")


def _check_type_ii_witness(p: int, u: int, a: int, s: int) -> None:
    _prime_scope(p)
    _positive(u=u, a=a, s=s)
    if (a * p + u) % s:
        raise ValueError("s must divide a*p+u")
    if (s + 1) % (4 * u * a):
        raise ValueError("s must be congruent to -1 modulo 4*u*a")


def type_i_witness_to_pw(p: int, u: int, a: int, s: int) -> Dict[str, int]:
    """Normalized Type-I witness -> Pomerance--Weingartner Cor. 2.2 data.

    Dahan-style normalized witness:
        gcd(u,a)=1, u<p, s | ap+u, s == -p (mod 4ua).

    Pomerance--Weingartner Type I (m=4):
        f | 4*A^2*d + 1, 4*A*d | p+f.

    Dictionary: A=a, d=(p+s)/(4ua), f=s.
    """
    _check_type_i_witness(p, u, a, s)
    numerator = p + s
    modulus = 4 * u * a
    alpha, rem = divmod(numerator, modulus)
    if rem:
        raise ArithmeticError("Type-I alpha is not integral")
    if (4 * a * a * alpha + 1) % s:
        raise ArithmeticError("Pomerance--Weingartner Type-I divisor condition failed")
    if numerator % (4 * a * alpha):
        raise ArithmeticError("Pomerance--Weingartner Type-I modulus condition failed")
    return {"p": p, "A": a, "d": alpha, "f": s,
            "u": u, "alpha": alpha}


def pw_type_i_to_witness(p: int, A: int, d: int, f: int) -> Dict[str, int]:
    """Pomerance--Weingartner Cor. 2.2 data -> normalized Type-I witness.

    Given f | 4*A^2*d+1 and 4*A*d | p+f, put U=(p+f)/(4Ad).
    Divide A,U by g=gcd(A,U), and replace d by d*g^2. This is the
    normalized witness (u,a,s)=(U/g,A/g,f).
    """
    _prime_scope(p)
    _positive(A=A, d=d, f=f)
    if (4 * A * A * d + 1) % f:
        raise ValueError("P&W Type-I condition f | 4*A^2*d+1 failed")
    denominator = 4 * A * d
    if (p + f) % denominator:
        raise ValueError("P&W Type-I condition 4*A*d | p+f failed")

    U = (p + f) // denominator
    g = gcd(A, U)
    a, u = A // g, U // g
    alpha = d * g * g
    s = f

    # Verify the normalized witness from first principles.
    _check_type_i_witness(p, u, a, s)
    if alpha != (s + p) // (4 * u * a) or (s + p) % (4 * u * a):
        raise ArithmeticError("normalized Type-I alpha identity failed")
    if (4 * a * a * alpha + 1) % s:
        raise ArithmeticError("normalized P&W divisor identity failed")
    return {"p": p, "u": u, "a": a, "s": s,
            "alpha": alpha, "normalizing_gcd": g,
            "raw_A": A, "raw_U": U, "raw_d": d}


def type_ii_witness_to_pw(p: int, u: int, a: int, s: int) -> Dict[str, int]:
    """Dahan Thm. 3.9 witness -> P&W Cor. 2.4 Type-II data.

    Normalize gcd(u,a) using Dahan Lemma 3.10, put
    v=(a*p+u)/s and e=(u+v)/a. Then e | u+v and 4uv | p+e.
    """
    _check_type_ii_witness(p, u, a, s)
    g = gcd(u, a)
    un, an = u // g, a // g
    # Lemma 3.10: s is coprime to g and divides the normalized numerator.
    if gcd(s, g) != 1 or (an * p + un) % s:
        raise ArithmeticError("Dahan gcd normalization failed")
    if (s + 1) % (4 * un * an):
        raise ArithmeticError("Dahan congruence did not survive normalization")
    v = (an * p + un) // s
    e, r = divmod(un + v, an)
    if r:
        raise ArithmeticError("Dahan reconstruction did not make e integral")
    alpha, rem = divmod(p + e, 4 * un * v)
    if rem:
        raise ArithmeticError("P&W Type-II condition 4uv | p+e failed")
    if (un + v) % e:
        raise ArithmeticError("P&W Type-II condition e | u+v failed")
    return {"p": p, "A": un, "B": v, "e": e,
            "u": un, "a": an, "s": s,
            "alpha": alpha, "normalizing_gcd": g}


def pw_type_ii_to_witness(p: int, A: int, B: int, e: int) -> Dict[str, int]:
    """P&W Cor. 2.4 Type-II data -> normalized Dahan Thm. 3.9 witness.

    Given e | A+B and 4AB | p+e, put a0=(A+B)/e and
    alpha=(p+e)/(4AB), s=4*A*a0*alpha-1. Normalize gcd(A,a0).
    """
    _prime_scope(p)
    _positive(A=A, B=B, e=e)
    if (A + B) % e:
        raise ValueError("P&W Type-II condition e | A+B failed")
    if (p + e) % (4 * A * B):
        raise ValueError("P&W Type-II condition 4AB | p+e failed")
    a0 = (A + B) // e
    alpha = (p + e) // (4 * A * B)
    s = 4 * A * a0 * alpha - 1
    g = gcd(A, a0)
    u, a = A // g, a0 // g
    alpha_n = alpha * g * g
    if (a * p + u) % s:
        raise ArithmeticError("P&W to Dahan Type-II divisibility failed")
    if (s + 1) != 4 * u * a * alpha_n:
        raise ArithmeticError("P&W to Dahan Type-II congruence failed")
    _check_type_ii_witness(p, u, a, s)
    return {"p": p, "u": u, "a": a, "s": s,
            "v": B, "alpha": alpha_n,
            "normalizing_gcd": g}


def rosati_type_i_to_pw(p: int, A: int, B: int, C: int, D: int) -> Dict[str, int]:
    """Rosati Type-I quadruple -> P&W Type-I triple.

    Rosati: 4ABCD=p(A+B)+C, gcd(ABCD,p)=1.
    Normalize g=gcd(A,C), which divides B; then
    (a,u,v,alpha)=(A/g,C/g,B/g,D*g^2). P&W data are (a,alpha,s),
    where s=4*a*u*alpha-p.
    """
    _prime_scope(p)
    _positive(A=A, B=B, C=C, D=D)
    if 4 * A * B * C * D != p * (A + B) + C:
        raise ValueError("Rosati Type-I equation failed")
    if gcd(A * B * C * D, p) != 1:
        raise ValueError("Rosati Type-I coprimality condition failed")
    g = gcd(A, C)
    if B % g:
        raise ArithmeticError("gcd(A,C) must divide B by the Rosati equation")
    a, u, v = A // g, C // g, B // g
    alpha = D * g * g
    s = 4 * a * u * alpha - p
    # The parameter relation forces s*v = a*p+u.
    if s <= 0 or s * v != a * p + u:
        raise ArithmeticError("Rosati Type-I parameter identity failed")
    witness = type_i_witness_to_pw(p, u, a, s)
    if witness["d"] != alpha:
        raise ArithmeticError("Rosati/P&W Type-I alpha mismatch")
    return {"p": p, "A_PW": a, "d_PW": alpha, "f_PW": s,
            "u_Dahan": u, "a_Dahan": a, "s_Dahan": s,
            "B_over_g": v, "normalizing_gcd": g}


def rosati_type_ii_to_pw(p: int, A: int, B: int, C: int, D: int) -> Dict[str, int]:
    """Rosati Type-II quadruple -> P&W Type-II triple.

    Rosati: 4ABCD=A+B+pC, gcd(ABD,p)=1.
    """
    _prime_scope(p)
    _positive(A=A, B=B, C=C, D=D)
    if 4 * A * B * C * D != A + B + p * C:
        raise ValueError("Rosati Type-II equation failed")
    if gcd(A * B * D, p) != 1:
        raise ValueError("Rosati Type-II coprimality condition failed")
    g = gcd(A, C)
    if B % g:
        raise ArithmeticError("gcd(A,C) must divide B by the Rosati equation")
    u, a, v = A // g, C // g, B // g
    alpha = D * g * g
    s = 4 * u * a * alpha - 1
    if s * v != a * p + u:
        raise ArithmeticError("Rosati Type-II parameter identity failed")
    q = type_ii_witness_to_pw(p, u, a, s)
    return {"p": p, "A_PW": q["A"], "B_PW": q["B"], "e_PW": q["e"],
            "u_Dahan": u, "a_Dahan": a, "s_Dahan": s,
            "normalizing_gcd": g}
