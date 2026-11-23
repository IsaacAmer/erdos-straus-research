"""Exact quadratic-character profile for the four small-u Type-II branches.

Research basis:
- Dahan, arXiv:2611.08717, Theorems 2.6 and 2.8.
- This module explicitly specializes the square classes of r=a+u modulo 4ua
  for u=1,2,3,4, and proves -r is never a square when gcd(u,a)=1 and a+u is odd.

No factorization of ap+u is performed. The module studies the finite unit group
G=(Z/(4ua)Z)^x attached to a parameter pair (u,a).
"""
from __future__ import annotations

import argparse
import json
from dataclasses import asdict, dataclass
from math import gcd
from pathlib import Path
from typing import Iterable


def factorization(n: int) -> tuple[tuple[int, int], ...]:
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    rem = n
    out: list[tuple[int, int]] = []
    d = 2
    while d * d <= rem:
        if rem % d == 0:
            e = 0
            while rem % d == 0:
                rem //= d
                e += 1
            out.append((d, e))
        d = 3 if d == 2 else d + 2
    if rem > 1:
        out.append((rem, 1))
    return tuple(out)


def is_square_unit_modulus(x: int, modulus: int) -> bool:
    """Whether x is a square in (Z/modulus Z)^x, using local criteria.

    For odd q^e, a unit is a square iff it is a quadratic residue mod q.
    For 2^e, the criteria are: any odd unit for e=1; x=1 mod 4 for e=2;
    x=1 mod 8 for e>=3.
    """
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("x must be an integer")
    if not isinstance(modulus, int) or isinstance(modulus, bool) or modulus < 1:
        raise ValueError("modulus must be a positive integer")
    if gcd(x, modulus) != 1:
        return False
    for q, exponent in factorization(modulus):
        if q == 2:
            if exponent == 1:
                continue
            if exponent == 2 and x % 4 != 1:
                return False
            if exponent >= 3 and x % 8 != 1:
                return False
        else:
            if pow(x % q, (q - 1) // 2, q) != 1:
                return False
    return True


def explicit_square_class_conditions(u: int, a: int) -> tuple[bool, bool]:
    """Return (r_is_square, -r_is_square) from the explicit u<=4 table.

    Preconditions are checked by _validate_pair. The second component is
    identically False for all four small-u branches; keeping it in the return
    value makes the theorem's three character cases directly auditable.
    """
    _validate_pair(u, a)
    odd_prime_factors = [q for q, _ in factorization(a) if q != 2]

    if u == 1:
        r_square = (a % 8 == 0)
        minus_r_square = (a % 8 == 6 and all(q % 4 == 1 for q in odd_prime_factors))
    elif u == 2:
        r_square = (a % 8 == 7 and all(q % 8 in (1, 7) for q in odd_prime_factors))
        minus_r_square = (a % 8 == 5 and all(q % 8 in (1, 3) for q in odd_prime_factors))
    elif u == 3:
        r_square = (
            a % 8 == 6 and a % 3 == 1
            and all(q % 12 in (1, 11) for q in odd_prime_factors)
        )
        minus_r_square = (
            a % 8 == 4 and a % 3 == 2
            and all(q % 3 == 1 for q in odd_prime_factors)
        )
    else:  # u == 4
        r_square = (a % 8 == 5)
        minus_r_square = (a % 8 == 3 and all(q % 4 == 1 for q in odd_prime_factors))
    return r_square, minus_r_square


def _validate_pair(u: int, a: int) -> None:
    if not isinstance(u, int) or isinstance(u, bool) or u not in (1, 2, 3, 4):
        raise ValueError("u must be one of 1, 2, 3, 4")
    if not isinstance(a, int) or isinstance(a, bool) or a < 1:
        raise ValueError("a must be a positive integer")
    if gcd(u, a) != 1:
        raise ValueError("gcd(u,a) must equal 1")
    if (a + u) % 2 == 0:
        raise ValueError("this classification requires a+u odd")


def euler_phi(n: int) -> int:
    result = n
    for q, _ in factorization(n):
        result = result // q * (q - 1)
    return result


def multiplicative_order(base: int, modulus: int) -> int:
    if modulus < 2 or gcd(base, modulus) != 1:
        raise ValueError("base must be a unit modulo modulus >= 2")
    residue = 1
    for order in range(1, euler_phi(modulus) + 1):
        residue = (residue * base) % modulus
        if residue == 1:
            return order
    raise ArithmeticError("order was not found within Euler's phi bound")


@dataclass(frozen=True)
class CharacterKernelProfile:
    u: int
    a: int
    modulus: int
    r: int
    r_mod_8: int
    odd_prime_factor_count_of_modulus: int
    real_character_group_order: int
    odd_character_count: int
    r_is_square: bool
    minus_r_is_square: bool
    odd_characters_with_chi_r_minus_one: int
    odd_character_kernels_not_excluded_by_this_filter: int
    character_filter_active: bool
    dahan_theorem_2_8b_as_stated_applies: bool
    elementary_u1_extension_applies: bool
    exceptional_a1_character_applies: bool
    prime_factor_multiplicativity_obstruction_applies: bool
    dahan_theorem_2_8a_applies: bool
    dahan_theorem_2_6_ab_applies: bool
    dahan_theorem_2_6_c_cycle_bound_applies: bool
    dihedral_order: int | None
    maximum_size_admissible_subset_count_exponent: int | None

    def as_dict(self) -> dict[str, object]:
        return asdict(self)


def character_kernel_profile(u: int, a: int) -> CharacterKernelProfile:
    _validate_pair(u, a)
    modulus = 4 * u * a
    r = a + u
    fac = factorization(modulus)
    odd_omega = sum(1 for q, _ in fac if q != 2)
    # Since a+u is odd and gcd(a,u)=1, exactly one of a,u is even; hence 8|4ua.
    if modulus % 8:
        raise ArithmeticError("the parity hypotheses should force 8 | 4ua")
    real_characters = 4 * (2 ** odd_omega)
    odd_characters = real_characters // 2  # -1 is not a square modulo 8.

    r_square_generic = is_square_unit_modulus(r, modulus)
    minus_r_square_generic = is_square_unit_modulus(-r, modulus)
    r_square_explicit, minus_r_square_explicit = explicit_square_class_conditions(u, a)
    if (r_square_generic, minus_r_square_generic) != (r_square_explicit, minus_r_square_explicit):
        raise ArithmeticError("explicit small-u square-class table disagrees with local square test")
    if minus_r_square_generic:
        raise ArithmeticError("proved small-u obstruction: -(a+u) cannot be a square modulo 4ua")

    # Dahan's character count: if r is a square, no odd character has chi(r)=-1;
    # if neither r nor -r is square, exactly |X|/4 odd characters have chi(r)=-1.
    obstructed_odd = 0 if r_square_generic else real_characters // 4

    theorem28_as_stated = (u > 1 and a > 1)  # u=2,3,4 are 3-smooth
    u1_extension = (u == 1 and a > 1)  # conductor argument proved separately
    # The only admissible a=1 pairs are (u,a)=(2,1),(4,1).
    # They are handled by explicit odd quadratic characters: chi_4 and chi_-8.
    exceptional_a1_character = (a == 1 and u in (2, 4))
    obstruction_applies = theorem28_as_stated or u1_extension or exceptional_a1_character
    theorem28a = (r % 4 == 3)
    # Dahan Theorem 2.6(a,b) applies to u in {1,2,3} for all admissible
    # pairs. Its stronger cycle decomposition / N_max bound in part (c)
    # additionally requires r == 3 or 5 (mod 8).
    theorem26_ab = u in (1, 2, 3)
    theorem26_c = theorem26_ab and r % 8 in (3, 5)
    if theorem26_c:
        order = multiplicative_order(r, modulus)
        phi = euler_phi(modulus)
        if phi % (2 * order):
            raise ArithmeticError("dihedral cycle count should be integral under Theorem 2.6 hypotheses")
        exponent = phi // (2 * order) - 1
    else:
        order = None
        exponent = None

    return CharacterKernelProfile(
        u=u, a=a, modulus=modulus, r=r, r_mod_8=r % 8,
        odd_prime_factor_count_of_modulus=odd_omega,
        real_character_group_order=real_characters,
        odd_character_count=odd_characters,
        r_is_square=r_square_generic,
        minus_r_is_square=minus_r_square_generic,
        odd_characters_with_chi_r_minus_one=obstructed_odd,
        odd_character_kernels_not_excluded_by_this_filter=odd_characters - obstructed_odd,
        character_filter_active=(obstructed_odd > 0),
        dahan_theorem_2_8b_as_stated_applies=theorem28_as_stated,
        elementary_u1_extension_applies=u1_extension,
        exceptional_a1_character_applies=exceptional_a1_character,
        prime_factor_multiplicativity_obstruction_applies=obstruction_applies,
        dahan_theorem_2_8a_applies=theorem28a,
        dahan_theorem_2_6_ab_applies=theorem26_ab,
        dahan_theorem_2_6_c_cycle_bound_applies=theorem26_c,
        dihedral_order=order,
        maximum_size_admissible_subset_count_exponent=exponent,
    )



def square_class_bit_vector(x: int, modulus: int) -> int:
    """Encode a unit square class in (Z/modulus Z)^x / squares as an F2 bitset.

    The first two bits encode the unit modulo 8; subsequent bits encode the
    Legendre signs at the distinct odd prime divisors of the modulus.
    The caller's modulus must be divisible by 8.
    """
    if not isinstance(x, int) or isinstance(x, bool):
        raise TypeError("x must be an integer")
    if not isinstance(modulus, int) or isinstance(modulus, bool) or modulus < 8 or modulus % 8:
        raise ValueError("modulus must be a positive multiple of 8")
    if gcd(x, modulus) != 1:
        raise ValueError("x must be a unit modulo modulus")
    bits = {1: 0b00, 3: 0b01, 5: 0b10, 7: 0b11}[x % 8]
    bit_index = 2
    for q, _ in factorization(modulus):
        if q == 2:
            continue
        if pow(x % q, (q - 1) // 2, q) == q - 1:
            bits |= 1 << bit_index
        bit_index += 1
    return bits


def _span_representation(vectors: list[int], target: int) -> int | None:
    """Return a bit mask of generators whose XOR equals target, if any."""
    basis: dict[int, tuple[int, int]] = {}
    for index, vector in enumerate(vectors):
        value = vector
        combination = 1 << index
        while value:
            pivot = value.bit_length() - 1
            if pivot in basis:
                row, row_combination = basis[pivot]
                value ^= row
                combination ^= row_combination
            else:
                basis[pivot] = (value, combination)
                break
    value = target
    combination = 0
    while value:
        pivot = value.bit_length() - 1
        if pivot not in basis:
            return None
        row, row_combination = basis[pivot]
        value ^= row
        combination ^= row_combination
    return combination


def prime_factor_square_class_span_certificate(p: int, u: int, a: int) -> dict[str, object]:
    """Find a prime-factor subproduct square-equivalent to r or -1.

    This is the F2-linear-algebra consequence of Dahan Theorem 2.8(b): for
    every odd character with chi(-1)=chi(r)=-1, not all prime factors of
    ap+u can lie in ker(chi). Hence the classes of -1 or r lie in the span
    of the prime-factor classes. For u=1 the note proves the conductor
    argument separately.

    Factorization is by exact trial division; intended as an audit/certificate
    generator for moderate inputs, not as the fast Phase 8 witness search.
    """
    if not isinstance(p, int) or isinstance(p, bool) or p <= 1 or p % 24 != 1:
        raise ValueError("p must be an integer congruent to 1 mod 24")
    # Deterministic elementary primality validation for reproducible audit data.
    if p % 2 == 0:
        raise ValueError("p must be prime")
    d = 3
    while d * d <= p:
        if p % d == 0:
            raise ValueError("p must be prime")
        d += 2
    _validate_pair(u, a)
    if p <= u:
        raise ValueError("p must exceed u")
    profile = character_kernel_profile(u, a)
    if not profile.prime_factor_multiplicativity_obstruction_applies:
        raise ValueError("no proved multiplicativity obstruction is registered for this pair")
    modulus = 4 * u * a
    M = a * p + u
    if gcd(M, modulus) != 1:
        raise ArithmeticError("ap+u should be a unit modulo 4ua under the hypotheses")
    factors = factorization(M)
    primes = [q for q, _ in factors]
    vectors = [square_class_bit_vector(q, modulus) for q in primes]
    target_minus_one = square_class_bit_vector(-1, modulus)
    target_r = square_class_bit_vector(a + u, modulus)
    rep_minus_one = _span_representation(vectors, target_minus_one)
    rep_r = _span_representation(vectors, target_r)
    candidates = []
    if rep_minus_one is not None:
        candidates.append((rep_minus_one.bit_count(), "-1", rep_minus_one, -1))
    if rep_r is not None:
        candidates.append((rep_r.bit_count(), "r", rep_r, a + u))
    if not candidates:
        raise ArithmeticError("Dahan's multiplicativity obstruction predicts a span certificate")
    _, target_name, mask, target_integer = min(candidates, key=lambda x: (x[0], x[1]))
    selected = [q for i, q in enumerate(primes) if (mask >> i) & 1]
    product = 1
    for q in selected:
        product *= q
    target_residue = target_integer % modulus
    ratio = (product % modulus) * pow(target_residue, -1, modulus) % modulus
    ratio_square = is_square_unit_modulus(ratio, modulus)
    if not ratio_square:
        raise ArithmeticError("internal certificate check failed: quotient is not a square")
    if u == 1:
        obstruction_source = "project-derived conductor extension for u=1"
    elif u > 1 and a > 1:
        obstruction_source = "Dahan Theorem 2.8(b)"
    elif u == 2 and a == 1:
        obstruction_source = "Dahan Theorem 2.8(a), chi_4"
    else:
        obstruction_source = "elementary chi_-8 character for (u,a)=(4,1)"
    square_class_dimension = 2 + sum(1 for q, _ in factorization(modulus) if q != 2)
    if not 1 <= len(selected) <= square_class_dimension:
        raise ArithmeticError("selected subset size exceeded the square-class dimension bound")
    return {
        "p": p, "u": u, "a": a, "modulus": modulus, "M_ap_plus_u": M,
        "multiplicativity_obstruction_source": obstruction_source,
        "square_class_group_dimension": square_class_dimension,
        "selected_prime_factor_count": len(selected),
        "distinct_prime_factors": primes, "target_square_class": target_name,
        "selected_prime_factors": selected,
        "selected_subproduct": product,
        "target_residue_modulus": target_residue,
        "subproduct_times_target_inverse_modulus": ratio,
        "quotient_is_square_modulus": ratio_square,
        "r_is_square": target_r == 0,
        "minus_r_is_square": square_class_bit_vector(-(a + u), modulus) == 0,
    }

def scan_modulator_box(limit: int = 10_000) -> dict[str, object]:
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 2:
        raise ValueError("limit must be an integer >= 2")
    summary = []
    for u in range(1, 5):
        counts = {
            "valid_parameter_pairs": 0,
            "r_square_pairs": 0,
            "character_filter_active_pairs": 0,
            "theorem_2_6_ab_pairs": 0,
            "theorem_2_6_c_cycle_bound_pairs": 0,
            "theorem_2_8a_pairs": 0,
            "theorem_2_8b_or_u1_extension_pairs": 0,
            "both_character_and_cycle_bound": 0,
            "character_only_relative_to_cycle_bound": 0,
            "neither_character_nor_cycle_bound": 0,
            "minus_r_square_pairs": 0,
        }
        for a in range(2, limit + 1):
            if gcd(u, a) != 1 or (a + u) % 2 == 0:
                continue
            p = character_kernel_profile(u, a)
            counts["valid_parameter_pairs"] += 1
            counts["r_square_pairs"] += int(p.r_is_square)
            counts["character_filter_active_pairs"] += int(p.character_filter_active)
            counts["theorem_2_6_ab_pairs"] += int(p.dahan_theorem_2_6_ab_applies)
            counts["theorem_2_6_c_cycle_bound_pairs"] += int(p.dahan_theorem_2_6_c_cycle_bound_applies)
            counts["theorem_2_8a_pairs"] += int(p.dahan_theorem_2_8a_applies)
            counts["theorem_2_8b_or_u1_extension_pairs"] += int(
                p.dahan_theorem_2_8b_as_stated_applies or p.elementary_u1_extension_applies
            )
            counts["both_character_and_cycle_bound"] += int(
                p.character_filter_active and p.dahan_theorem_2_6_c_cycle_bound_applies
            )
            counts["character_only_relative_to_cycle_bound"] += int(
                p.character_filter_active and not p.dahan_theorem_2_6_c_cycle_bound_applies
            )
            counts["neither_character_nor_cycle_bound"] += int(
                not p.character_filter_active and not p.dahan_theorem_2_6_c_cycle_bound_applies
            )
            counts["minus_r_square_pairs"] += int(p.minus_r_is_square)
        summary.append({"u": u, "a_range": [2, limit], **counts})
    return {
        "study": "Explicit quadratic-character classes for small Type-II parameters",
        "limit": limit,
        "conditions": "1<=u<=4, 2<=a<=limit, gcd(u,a)=1, a+u odd",
        "claims": {
            "minus_r_square_impossible": True,
            "character_obstruction_count": "0 if r is a square; otherwise |X|/4 odd characters",
            "theorem_2_6_scope": "parts (a,b) apply for u in {1,2,3}; part (c) cycle bound additionally requires r mod 8 in {3,5}",
            "theorem_2_8a_scope": "applies when r == 3 (mod 4)",
            "theorem_2_8b_scope": "as stated for u=2,3,4 and a>1; u=1 has a separate conductor proof; the admissible a=1 pairs (2,1),(4,1) have explicit odd-character proofs",
        },
        "summary_by_u": summary,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--limit", type=int, default=10_000)
    parser.add_argument("--output", type=Path, default=Path("results/PHASE11-CHARACTER-CLASSIFICATION.json"))
    args = parser.parse_args()
    result = scan_modulator_box(args.limit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2), encoding="utf-8")
    for row in result["summary_by_u"]:
        print(
            f"u={row['u']}: valid={row['valid_parameter_pairs']}, "
            f"character-filter={row['character_filter_active_pairs']}, "
            f"T2.6(b)={row['theorem_2_6_ab_pairs']}, "
            f"T2.6(c)={row['theorem_2_6_c_cycle_bound_pairs']}, "
            f"T2.8(a)={row['theorem_2_8a_pairs']}, "
            f"char-filter={row['character_filter_active_pairs']}, "
            f"both(char+cycle)={row['both_character_and_cycle_bound']}, "
            f"char-only={row['character_only_relative_to_cycle_bound']}, "
            f"neither={row['neither_character_nor_cycle_bound']}, "
            f"minus-r-square={row['minus_r_square_pairs']}"
        )
    print(f"Saved: {args.output}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
