# ES-FOUNDATION-01 — Source verification and corrected attribution

Date: 22 November 2026
Status: literature cross-check completed for the statements listed below.

## 1. Bradford (2024 preprint; later published in Integers 25 (2025))

The original arXiv HTML for Kyle Bradford, *Elemental Patterns from the Erdős Straus Conjecture*, states the divisor criterion in its abstract and proves the two directions in Propositions 1–4:

- Type I: `d | x^2` and `d ≡ -p x (mod 4x-p)`.
- Type II: `d | x^2`, `d ≤ x`, and `d ≡ -x (mod 4x-p)`.
- Type I is defined by `p ∤ y`; Type II by `p | y`, with `x ≤ y ≤ z`.

Original source: https://arxiv.org/html/2403.16047

## 2. Dahan (arXiv:2608.24035v2, 5 November 2026)

The original arXiv HTML contains the exact witness criterion previously discussed:

**Lemma 2.2 (binary criterion).** If `gcd(A,M)=1`, then `A/M = 1/y + 1/z` has a positive-integer solution iff there are coprime divisors `u,v | M` with `u+v ≡ 0 (mod A)`.

**Theorem 2.6.** For prime `n`, shift `c ≡ 3 (mod 4)`, `0<c≤2n`, and `K=(n+c)/4`, a decomposition with first denominator `K` exists iff there are coprime divisors `u,v | nK` with `u+v ≡ 0 (mod c)`. The theorem gives the explicit remainder factor `d=(u+v)nK/(uvc)` and decomposition `4/n=1/K+1/(du)+1/(dv)`.

**Corollary 2.7.** It splits the criterion into:

- Untwisted: `d1,d2 | K`, `gcd(d1,d2)=1`, and `d1+d2 ≡ 0 (mod c)`.
- Twisted: `d1,d2 | K`, `gcd(n d1,d2)=1`, and `n d1+d2 ≡ 0 (mod c)`.

The paper defines Type I/II in Definition 2.8 by the number of denominators divisible by `n` (one or two respectively). The two-parameter criterion `s | an+u`, `s ≡ -1 (mod 4ua)` is a different later result, Theorem 3.9; it should not be confused with Theorem 2.6.

Original source: https://arxiv.org/abs/2608.24035

## 3. What is now settled

The witness condition used in `ES-FOUNDATION-01-DRAFT.md` is not an unsupported attribution: it is exactly Dahan's Theorem 2.6, with the shift renamed from `c` to `h`, and denominator `K=(p+h)/4`.

Bradford's divisor-of-a-square criterion is the separate formulation in his paper. The algebraic maps in the proof draft relate the witness pairs to Bradford's Type I/Type II divisors on the restricted overlap `0<h≤p` (which is inside both papers' admissible ranges). This is a restricted overlap, not a claim that the full parameter ranges of the two papers are identical.

## 4. Important scope warnings

- Dahan Theorem 2.6 allows `0<c≤2p`; Bradford's smallest-denominator formulation uses `ceil(p/4)≤x≤ceil(p/2)`, corresponding to `3≤c=4x-p≤p+2` when `p≡1 (mod 4)`.
- The draft's algebraic equivalence was stated only for `0<h≤p`. Do not silently expand that proof's range without checking all hypotheses in the expanded range.
- A finite Python audit can test the conversion but cannot prove existence of a witness for every prime.
- Dahan's Theorem 3.9 is a distinct two-parameter criterion and may be a more promising later research direction; it is not the same as Theorem 2.6.

## 5. Primary references

- Bradford, *Elemental Patterns from the Erdős Straus Conjecture*, arXiv:2403.16047: https://arxiv.org/html/2403.16047
- Dahan, *Sieve dimension and search depth for the Erdős-Straus conjecture, n ≡ 1 (mod 24)*, arXiv:2608.24035v2: https://arxiv.org/abs/2608.24035
