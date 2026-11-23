"""Exact finite audit and asymptotic constants for the optimized u<=4 family.

The mathematical proof is in notes/ES-PHASE12-OPTIMIZED-U4-DENSITY.md.
Only Python's standard library is used.
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path
from typing import Any

U_VALUES = (1, 2, 3, 4)
DELTA = 1 / 1024
GAMMA = 99 / 100
TAU = 1 / 8 - DELTA

# c_u is the coefficient in the mean asymptotic
# mean_{a<=X, (a,u)=1} (phi(4ua)-2) = c_u X + O_u(log X).
C_U = {
    1: 8 / math.pi**2,
    2: 16 / math.pi**2,
    3: 18 / math.pi**2,
    4: 32 / math.pi**2,
}
D_U = {
    1: 1.0,
    2: 1 / 2,
    3: 2 / 3,
    4: 1 / 2,
}


def euler_phi(n: int) -> int:
    """Return Euler's totient using exact integer arithmetic."""
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


def cutoff_coefficients() -> dict[int, float]:
    """Return x_u where A_u=floor(x_u*L)."""
    return {u: GAMMA * TAU / C_U[u] for u in U_VALUES}


def asymptotic_pair_coefficient() -> float:
    """S such that |F_N| = (S+o(1))*loglog(N)."""
    return GAMMA * TAU * sum(D_U[u] / C_U[u] for u in U_VALUES)


def rectangular_optimal_pair_coefficient() -> float:
    """Supremal P/L under the asymptotic mean constraint in this ansatz."""
    return TAU * sum(D_U[u] / C_U[u] for u in U_VALUES)


def asymptotic_exponent_coefficient() -> float:
    """kappa=(5/96)S in the exponent exp(-(kappa+o(1))(loglog N)^2)."""
    return (5 / 96) * asymptotic_pair_coefficient()


def finite_profile(L: float) -> dict[str, Any]:
    """Compute exact finite parameter counts and totient mean for a chosen L.

    L represents log(log(N)); the script does not construct N itself.
    The reported finite condition is a numerical audit of the asymptotic
    hypotheses, not a proof for finite N.
    """
    if not isinstance(L, (int, float)) or isinstance(L, bool) or not math.isfinite(L) or L < 50:
        raise ValueError("L must be a finite real number >= 50")

    x = cutoff_coefficients()
    A = {u: math.floor(x[u] * L) for u in U_VALUES}
    if min(A.values()) < 1:
        raise ArithmeticError("cutoffs must be positive")

    pairs: list[tuple[int, int]] = []
    totient_sum = 0
    for u in U_VALUES:
        for a in range(1, A[u] + 1):
            if math.gcd(a, u) == 1:
                pairs.append((u, a))
                totient_sum += euler_phi(4 * u * a) - 2

    P = len(pairs)
    if P == 0:
        raise ArithmeticError("empty family")

    J = max(4, max(A.values()))
    # Here log_z means log(z)=log(N)/(4*P*L).  Thus
    # log(log(z)/log(J^5)) = L-log(4PL)-log(5log(J)).
    B = L - math.log(4 * P * L) - math.log(5 * math.log(J))
    mean_totient = totient_sum / P
    threshold = TAU * B

    return {
        "L_loglogN": L,
        "A_u_cutoffs": {str(u): A[u] for u in U_VALUES},
        "x_u_coefficients": {str(u): x[u] for u in U_VALUES},
        "J": J,
        "pair_count_P": P,
        "mean_phi_4ua_minus_2_exact": mean_totient,
        "B_log_logz_over_logJ5": B,
        "theorem_4_6_mean_threshold": threshold,
        "finite_mean_condition_passes": mean_totient <= threshold,
        "pair_count_over_L": P / L,
        "mean_over_L": mean_totient / L,
        "predicted_asymptotic_pair_count_over_L": asymptotic_pair_coefficient(),
        "predicted_asymptotic_mean_over_L": GAMMA * TAU,
    }


def build_report(L_values: tuple[float, ...]) -> dict[str, Any]:
    return {
        "title": "Optimized Type-II density corollary for u in {1,2,3,4}",
        "source_theorem": "Dahan, arXiv:2611.08717v1, Theorem 4.6 (2026-11-05)",
        "status": "derived corollary; not a new proof of Erdos-Straus",
        "delta_0": DELTA,
        "gamma": GAMMA,
        "tau_1_over_8_minus_delta": TAU,
        "c_u": {str(u): C_U[u] for u in U_VALUES},
        "d_u_phi_over_u": {str(u): D_U[u] for u in U_VALUES},
        "x_u_cutoff_coefficients": {str(u): cutoff_coefficients()[u] for u in U_VALUES},
        "S_pair_count_coefficient": asymptotic_pair_coefficient(),
        "rectangular_optimal_pair_count_coefficient": rectangular_optimal_pair_coefficient(),
        "fraction_of_rectangular_optimum": asymptotic_pair_coefficient() / rectangular_optimal_pair_coefficient(),
        "kappa_exponent_coefficient": asymptotic_exponent_coefficient(),
        "finite_audits": [finite_profile(L) for L in L_values],
        "theorem_bound": "|E_4(N)| <= N*exp(-(kappa+o(1))*(log log N)^2), with kappa=5*S/96",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--L-values", nargs="+", type=float, default=[100, 200, 500, 1000, 5000, 10000])
    parser.add_argument("--output", default="results/PHASE12-OPTIMIZED-U4-DENSITY.json")
    args = parser.parse_args()

    report = build_report(tuple(args.L_values))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2), encoding="utf-8")

    print(f"S (pair-count coefficient) = {report['S_pair_count_coefficient']:.12f}")
    print(f"rectangular optimum = {report['rectangular_optimal_pair_count_coefficient']:.12f}")
    print(f"fraction of rectangular optimum = {report['fraction_of_rectangular_optimum']:.6%}")
    print(f"kappa = {report['kappa_exponent_coefficient']:.12f}")
    print("u | x_u | A_u when L=10000")
    for u in U_VALUES:
        print(f"{u} | {cutoff_coefficients()[u]:.12f} | {math.floor(cutoff_coefficients()[u]*10000)}")
    print("L | P/L | exact mean/L | theorem threshold/L | condition")
    for row in report["finite_audits"]:
        print(
            f"{row['L_loglogN']:g} | {row['pair_count_over_L']:.6f} | "
            f"{row['mean_over_L']:.6f} | "
            f"{row['theorem_4_6_mean_threshold']/row['L_loglogN']:.6f} | "
            f"{row['finite_mean_condition_passes']}"
        )
    print(f"Saved: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
