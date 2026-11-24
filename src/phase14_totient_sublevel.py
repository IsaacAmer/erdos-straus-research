"""Totient-sublevel Type-II families for u=1,2,3,4.

The analytic proof is given in notes/ES-PHASE14-TOTIENT-SUBLEVEL-DENSITY.md.
The finite audit uses exact integer totients. Standard library only.
"""
from __future__ import annotations

import argparse
import json
import math
from array import array
from fractions import Fraction
from pathlib import Path
from typing import Any

U_VALUES = (1, 2, 3, 4)
DEFAULT_GAMMA = Fraction(999, 1000)
DEFAULT_DELTA0 = Fraction(1, 65536)
# Apery's constant, used only for a decimal presentation. The proof uses zeta(3).
ZETA3_DECIMAL = 1.2020569031595942854


def euler_phi(n: int) -> int:
    """Exact Euler totient."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    result = n
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            result -= result // p
            while x % p == 0:
                x //= p
        p += 1 if p == 2 else 2
    if x > 1:
        result -= result // x
    return result


def phi_sieve(n: int) -> array:
    """Exact uint32 totients for 0..n, with a compact contiguous buffer."""
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    if n >= 2**32:
        raise ValueError("sieve limit too large for uint32 storage")
    phi = array("I", range(n + 1))
    phi[0] = 0
    for p in range(2, n + 1):
        if phi[p] == p:
            for m in range(p, n + 1, p):
                phi[m] -= phi[m] // p
    return phi


def tau_value(delta0: Fraction = DEFAULT_DELTA0) -> Fraction:
    if not isinstance(delta0, Fraction) or not (0 < delta0 < Fraction(1, 8)):
        raise ValueError("delta0 must be a Fraction strictly between 0 and 1/8")
    return Fraction(1, 8) - delta0


def validate_parameters(gamma: Fraction, delta0: Fraction) -> None:
    if not isinstance(gamma, Fraction) or not (0 < gamma < 1):
        raise ValueError("gamma must be a Fraction strictly between 0 and 1")
    tau_value(delta0)


def prime_product_odd() -> float:
    """Pi = prod_{p>2}(1 + 1/(p(p-1))) = 105*zeta(3)/pi^4."""
    return 105.0 * ZETA3_DECIMAL / (math.pi ** 4)


def counting_constants_by_u() -> dict[str, float]:
    """C_u in #{a: (a,u)=1, phi(4ua)<=X} ~ C_u X."""
    pi_prod = prime_product_odd()
    return {
        "1": 0.5 * pi_prod,
        "2": 0.125 * pi_prod,
        "3": (1.0 / 7.0) * pi_prod,
        "4": 0.0625 * pi_prod,
    }


def pair_coefficient_A_infinity() -> float:
    """A_inf = 2*sum C_u = (9765/56)*zeta(3)/pi^4."""
    return (9765.0 / 56.0) * ZETA3_DECIMAL / (math.pi ** 4)


def kappa_limit() -> float:
    """Limit (5/96)*(1/8)*A_inf as gamma->1 and delta0->0."""
    return (5.0 / 768.0) * pair_coefficient_A_infinity()


def kappa_for_parameters(gamma: Fraction, delta0: Fraction) -> float:
    validate_parameters(gamma, delta0)
    return (5.0 / 96.0) * float(gamma * tau_value(delta0)) * pair_coefficient_A_infinity()


def max_a_bound(T: Fraction, u: int) -> int:
    """From phi(n)^2 >= n/2, phi(4ua)<=T implies a<=T^2/(2u)."""
    if not isinstance(T, Fraction) or T <= 0:
        raise ValueError("T must be a positive Fraction")
    if u not in U_VALUES:
        raise ValueError("u must be in {1,2,3,4}")
    return (T.numerator * T.numerator) // (2 * u * T.denominator * T.denominator)


def finite_audit(L: int, gamma: Fraction = DEFAULT_GAMMA,
                 delta0: Fraction = DEFAULT_DELTA0) -> dict[str, Any]:
    """Enumerate the exact totient-sublevel family for a surrogate L=loglog N.

    This checks finite arithmetic and the numerical form of Dahan's mean
    condition. It is not a computation over primes up to exp(exp(L)).
    """
    validate_parameters(gamma, delta0)
    if not isinstance(L, int) or isinstance(L, bool) or L < 20:
        raise ValueError("L must be an integer >= 20")

    tau = tau_value(delta0)
    T = 2 * gamma * tau * L
    a_bounds = {u: max_a_bound(T, u) for u in U_VALUES}
    max_modulus = max(4 * u * a_bounds[u] for u in U_VALUES)
    phi = phi_sieve(max_modulus)
    threshold_num, threshold_den = T.numerator, T.denominator

    P = 0
    cost_sum = 0
    J = 4
    by_u: dict[str, dict[str, int]] = {
        str(u): {"count": 0, "cost_sum": 0} for u in U_VALUES
    }
    for u in U_VALUES:
        for a in range(1, a_bounds[u] + 1):
            if math.gcd(a, u) != 1:
                continue
            value = int(phi[4 * u * a])
            if value * threshold_den > threshold_num:
                continue
            cost = value - 2
            P += 1
            cost_sum += cost
            J = max(J, a, u)
            by_u[str(u)]["count"] += 1
            by_u[str(u)]["cost_sum"] += cost

    if P == 0:
        raise ArithmeticError("totient-sublevel family is unexpectedly empty")

    Lf = float(L)
    # A uniform analytic upper bound for the coordinate box. The actual J
    # used by the theorem may be taken as J_actual; this bound proves J=O(L^2).
    T2 = T * T
    J_bound = max(4, (T2.numerator + 2 * T2.denominator - 1) // (2 * T2.denominator))
    mean = cost_sum / P
    Ainf = pair_coefficient_A_infinity()
    kappa = kappa_for_parameters(gamma, delta0)
    return {
        "L_loglogN_surrogate": L,
        "gamma": float(gamma),
        "delta0": float(delta0),
        "tau": float(tau),
        "totient_cutoff_T": float(T),
        "a_coordinate_bounds_from_phi_lower_bound": {str(u): a_bounds[u] for u in U_VALUES},
        "J_actual_max_coordinate": J,
        "J_upper_bound_from_phi_square_inequality": J_bound,
        "max_modulus_sieved": max_modulus,
        "pair_count_exact": P,
        "pair_count_over_L_exact": P / Lf,
        "cost_sum_exact": cost_sum,
        "mean_phi_4ua_minus_2_exact": mean,
        "mean_over_L": mean / Lf,
        "predicted_mean_over_L": float(gamma * tau),
        "A_infinity": Ainf,
        "predicted_pair_count_coefficient": float(gamma * tau) * Ainf,
        "observed_pair_count_coefficient": P / Lf,
        "kappa_asymptotic": kappa,
        "observed_by_u": by_u,
    }


def build_report(gamma: Fraction, delta0: Fraction,
                 L_values: tuple[int, ...]) -> dict[str, Any]:
    validate_parameters(gamma, delta0)
    tau = tau_value(delta0)
    Ainf = pair_coefficient_A_infinity()
    constants = counting_constants_by_u()
    return {
        "title": "Totient-sublevel Type-II density family for u=1,2,3,4",
        "source_theorem": "Dahan, arXiv:2611.08717v1, Theorem 4.6",
        "status": "derived corollary; no universal Type-II witness and no ES proof claimed",
        "gamma": float(gamma),
        "delta0": float(delta0),
        "tau": float(tau),
        "T_over_loglogN": float(2 * gamma * tau),
        "counting_constants_C_u": constants,
        "sum_C_u": sum(constants.values()),
        "A_infinity_equals_2_sum_C_u": Ainf,
        "A_infinity_formula": "(31/28)*zeta(2)*zeta(3)/zeta(6) = (9765/56)*zeta(3)/pi^4",
        "kappa_exponent_coefficient": kappa_for_parameters(gamma, delta0),
        "kappa_limit_gamma_to_1_delta_to_0": kappa_limit(),
        "fraction_of_limiting_kappa": kappa_for_parameters(gamma, delta0) / kappa_limit(),
        "family_definition": "P_N={(u,a):1<=u<=4, gcd(u,a)=1, phi(4*u*a)<=2*gamma*(1/8-delta0)*loglog(N)}",
        "theorem_bound": "Big-O bound: |E_4(N)| = O(N*exp(-(kappa+o(1))*(log log N)^2))",
        "finite_audits": [finite_audit(L, gamma, delta0) for L in L_values],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--gamma", default="999/1000")
    parser.add_argument("--delta0", default="1/65536")
    parser.add_argument("--L-values", nargs="+", type=int, default=[100, 250, 500, 1000])
    parser.add_argument("--output", default="results/PHASE14-TOTIENT-SUBLEVEL-DENSITY.json")
    args = parser.parse_args()
    gamma = Fraction(args.gamma)
    delta0 = Fraction(args.delta0)
    report = build_report(gamma, delta0, tuple(args.L_values))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"gamma={gamma}; delta0={delta0}; tau={report['tau']:.12f}")
    print("u | counting constant C_u")
    for u, value in report["counting_constants_C_u"].items():
        print(f"{u} | {value:.12f}")
    print(f"A_inf = {report['A_infinity_equals_2_sum_C_u']:.12f}")
    print(f"kappa = {report['kappa_exponent_coefficient']:.12f}")
    print(f"kappa-limit = {report['kappa_limit_gamma_to_1_delta_to_0']:.12f}")
    print(f"fraction of limit = {report['fraction_of_limiting_kappa']:.6%}")
    print("L | P/L exact | P/L predicted | mean/L exact | mean/L predicted | J actual | J bound")
    for row in report["finite_audits"]:
        print(
            f"{row['L_loglogN_surrogate']:>5} | {row['pair_count_over_L_exact']:.6f} | "
            f"{row['predicted_pair_count_coefficient']:.6f} | {row['mean_over_L']:.6f} | "
            f"{row['predicted_mean_over_L']:.6f} | {row['J_actual_max_coordinate']} | "
            f"{row['J_upper_bound_from_phi_square_inequality']}"
        )
    print(f"Saved: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
