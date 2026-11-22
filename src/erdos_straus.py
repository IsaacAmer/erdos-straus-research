"""Exact arithmetic tools for the Erdős–Straus conjecture.

No floating-point arithmetic is used. The conditional construction below
checks whether a *chosen* (p, h, w) yields a valid representation. It does
not assert that such parameters exist for every prime p.
"""

from __future__ import annotations

from fractions import Fraction
from math import gcd


def verify_representation(n: int, a: int, b: int, c: int) -> bool:
    """Return True iff n>=2, a,b,c are positive and 4/n=1/a+1/b+1/c."""
    if n < 2 or min(a, b, c) <= 0:
        return False
    return Fraction(4, n) == Fraction(1, a) + Fraction(1, b) + Fraction(1, c)


def build_from_shift_and_divisor(p: int, h: int, w: int) -> tuple[int, int, int]:
    """Construct (x,b,c) from a sufficient divisor criterion.

    Let x=(p+h)/4 and D=p*x. If h is positive, h == 3 (mod 4),
    gcd(D,h)=1, w|D^2, and w == -D (mod h), then v=D^2/w also
    satisfies v == -D (mod h). Consequently

        4/p = 1/x + 1/b + 1/c,
        b=(D+w)/h, c=(D+v)/h.

    The function checks all conditions and verifies the final identity
    exactly. It raises ValueError if the supplied parameters do not qualify.
    It does not check primality of p: primality is not needed for the algebra.
    """
    if p < 2:
        raise ValueError("p must be at least 2")
    if h <= 0 or h % 4 != 3:
        raise ValueError("h must be positive and congruent to 3 modulo 4")
    if (p + h) % 4 != 0:
        raise ValueError("(p+h) must be divisible by 4")

    x = (p + h) // 4
    if x <= 0:
        raise ValueError("x must be positive")

    d = p * x
    if gcd(d, h) != 1:
        raise ValueError("gcd(p*x,h) must equal 1")
    if w <= 0 or (d * d) % w != 0:
        raise ValueError("w must be a positive divisor of (p*x)^2")
    if (w + d) % h != 0:
        raise ValueError("w must be congruent to -p*x modulo h")

    v = (d * d) // w
    if (v + d) % h != 0:
        raise ValueError("derived v is not congruent to -p*x modulo h")

    b_num = d + w
    c_num = d + v
    if b_num % h != 0 or c_num % h != 0:
        raise ArithmeticError("internal divisibility check failed")

    b = b_num // h
    c = c_num // h
    if min(x, b, c) <= 0:
        raise ValueError("constructed denominators must be positive")
    if not verify_representation(p, x, b, c):
        raise ArithmeticError("exact verification of the final identity failed")

    return x, b, c


if __name__ == "__main__":
    # Reproducible demonstration only; this is not a proof of the conjecture.
    p, h, w = 73, 7, 10
    x, b, c = build_from_shift_and_divisor(p, h, w)
    print(f"p={p}, h={h}, w={w} -> (x,b,c)=({x},{b},{c})")
    print("exact identity verified:", verify_representation(p, x, b, c))
