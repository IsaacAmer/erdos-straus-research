"""Exact Jacobi-symbol audit for Phase 8 Type-II witnesses.

The checked identities are the necessary conditions in Benjamin Dahan,
"Composite witness sieves, Kneser–Plancherel containers, and the exponent
5/7 for the Erdős–Straus conjecture", arXiv:2611.08717, Theorem 2.4.

Mapping from the project's Phase 8 TypeIIWitness(u,a,s,v,e,k):
    Dahan's alpha = k, and Dahan's shift c = e.

This module audits an already reconstructed witness. It does not prove that
any witness exists and does not replace the exact equation checks.
"""
from __future__ import annotations

from dataclasses import asdict, dataclass
from math import gcd
from functools import lru_cache
from typing import Iterable

from phase7_floor_quotient import prime_by_trial_division


@dataclass(frozen=True)
class JacobiAudit:
    p: int
    u: int
    a: int
    s: int
    v: int
    e: int
    alpha: int
    identity_ap_plus_u_equals_sv: bool
    identity_s_plus_1_equals_4u_alpha_a: bool
    identity_u_plus_v_equals_ae: bool
    identity_p_plus_e_equals_4u_alpha_v: bool
    coprime_u_a: bool
    jacobi_alpha_over_s: int
    jacobi_ua_over_s: int
    jacobi_s_over_p: int
    jacobi_p_over_s: int
    jacobi_uv_over_p: int
    jacobi_alpha_e_over_p: int

    @property
    def identities_ok(self) -> bool:
        return all((
            self.identity_ap_plus_u_equals_sv,
            self.identity_s_plus_1_equals_4u_alpha_a,
            self.identity_u_plus_v_equals_ae,
            self.identity_p_plus_e_equals_4u_alpha_v,
            self.coprime_u_a,
        ))

    @property
    def jacobi_laws_ok(self) -> bool:
        return all((
            self.jacobi_alpha_over_s == 1,
            self.jacobi_ua_over_s == 1,
            self.jacobi_s_over_p == -1,
            self.jacobi_p_over_s == -1,
            self.jacobi_uv_over_p == -1,
            self.jacobi_alpha_e_over_p == -1,
        ))

    @property
    def passed(self) -> bool:
        return self.identities_ok and self.jacobi_laws_ok

    def as_dict(self) -> dict[str, object]:
        result = asdict(self)
        result.update({
            "identities_ok": self.identities_ok,
            "jacobi_laws_ok": self.jacobi_laws_ok,
            "passed": self.passed,
        })
        return result


def jacobi_symbol(a: int, n: int) -> int:
    """Return the Jacobi symbol (a/n) for integer a and positive odd n."""
    if not isinstance(a, int) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(n, int) or isinstance(n, bool) or n <= 0 or n % 2 == 0:
        raise ValueError("n must be a positive odd integer")

    a %= n
    sign = 1
    while a:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                sign = -sign
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            sign = -sign
        a %= n
    return sign if n == 1 else 0


@lru_cache(maxsize=256)
def _is_target_prime(p: int) -> bool:
    return prime_by_trial_division(p)


def audit_type_ii_witness(p: int, witness: object) -> JacobiAudit:
    """Verify the Phase 8 equations and Dahan Theorem 2.4 symbol laws.

    `witness` must expose fields u, a, s, v, e, k, as Phase 8's
    TypeIIWitness does. The prime check is deliberate: the denominator in
    the Legendre-symbol laws must be prime.
    """
    if not isinstance(p, int) or isinstance(p, bool) or p <= 1 or p % 24 != 1:
        raise ValueError("p must be an integer prime candidate congruent to 1 mod 24")
    if not _is_target_prime(p):
        raise ValueError("p must be prime")

    try:
        values = (witness.u, witness.a, witness.s, witness.v, witness.e, witness.k)
    except AttributeError as exc:
        raise TypeError("witness must expose integer fields u,a,s,v,e,k") from exc
    if any(not isinstance(value, int) or isinstance(value, bool) for value in values):
        raise TypeError("witness fields u,a,s,v,e,k must be integers")
    u, a, s, v, e, alpha = values

    if min(u, a, s, v, e, alpha) <= 0:
        raise ValueError("witness parameters must all be positive")
    if u not in (1, 2, 3, 4):
        raise ValueError("u must be one of 1, 2, 3, 4")
    if s % 2 == 0:
        raise ValueError("s must be odd for the Jacobi denominator")

    return JacobiAudit(
        p=p,
        u=u,
        a=a,
        s=s,
        v=v,
        e=e,
        alpha=alpha,
        identity_ap_plus_u_equals_sv=(a * p + u == s * v),
        identity_s_plus_1_equals_4u_alpha_a=(s + 1 == 4 * u * alpha * a),
        identity_u_plus_v_equals_ae=(u + v == a * e),
        identity_p_plus_e_equals_4u_alpha_v=(p + e == 4 * u * alpha * v),
        coprime_u_a=(gcd(u, a) == 1),
        jacobi_alpha_over_s=jacobi_symbol(alpha, s),
        jacobi_ua_over_s=jacobi_symbol(u * a, s),
        jacobi_s_over_p=jacobi_symbol(s, p),
        jacobi_p_over_s=jacobi_symbol(p, s),
        jacobi_uv_over_p=jacobi_symbol(u * v, p),
        jacobi_alpha_e_over_p=jacobi_symbol(alpha * e, p),
    )


def audit_witness_collection(p: int, witnesses: Iterable[object]) -> dict[str, object]:
    """Audit a collection, returning counts and detailed failed certificates."""
    audits = [audit_type_ii_witness(p, w) for w in witnesses]
    failed = [a.as_dict() for a in audits if not a.passed]
    return {
        "p": p,
        "witness_count": len(audits),
        "passed_count": len(audits) - len(failed),
        "failed_count": len(failed),
        "all_passed": not failed,
        "failed_certificates": failed,
    }
