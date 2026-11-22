# ES-PHASE3-AUDIT — bounded-u Type-II experiment

**Date:** 22 November 2026  
**Status:** Exact finite criterion + reproducible finite computation + research conjecture (unproved).

## 1. Results reproduced

The user's Windows run reported:

- 33/33 unit tests passed.
- For primes `p <= 1,000,000`, `p == 1 (mod 24)`: 9,732 primes were tested.
- Minimal normalized Type-II `u` counts: `u=1: 9729`, `u=2: 2`, `u=4: 1`.
- No tested prime failed for all `u <= 4`.
- The three primes without a `u=1` witness were `193`, `2521`, and `66529`.

I independently compiled the package's C++17 implementation and ran it with `N=100,000,000`. It reproduced:

| Minimal `u` | Count |
|---:|---:|
| 1 | 719,778 |
| 2 | 2 |
| 3 | 0 |
| 4 | 1 |
| **Total** | **719,781** |

No prime in that finite interval lacked a Type-II witness with `u <= 4`.

The C++ output also reports witnesses with large `a`; the maximum found was `a=5839` at `p=41,900,329`. Thus this is **not** Dahan's fixed-depth result with both `u,a <= 4`.

## 2. Exact finite quotient criterion

Start from the normalized Dahan Type-II condition for prime `p`:

\[
\gcd(u,a)=1,\qquad s\mid ap+u,\qquad s\equiv -1\pmod{4ua},
\]
with positive integers `u,a,s`.

Write

\[
s=4uak-1,\qquad Q=\frac{ap+u}{s}.
\]

Then `k,Q` are positive integers and

\[
Q(4uak-1)=ap+u,
\]
so

\[
a(4uQk-p)=u+Q.
\]

Therefore

\[
a\mid u+Q,\qquad r:=\frac{u+Q}{a}\in\mathbb Z_{>0},
\]
with

\[
\boxed{p+r=4uQk.}
\]

Since `r <= u+Q` and `k >= 1`,

\[
4uQ\le p+r\le p+u+Q,
\]
which yields

\[
\boxed{1\le Q\le\left\lfloor\frac{p+u}{4u-1}\right\rfloor.}
\]

Conversely, if an integer `Q` in this range and a positive divisor `a | (u+Q)` satisfy

\[
\gcd(a,u)=1,\qquad 4uQ\mid p+\frac{u+Q}{a},
\]
then setting

\[
r=\frac{u+Q}{a},\quad k=\frac{p+r}{4uQ},\quad s=4uak-1
\]
produces a positive integer `s` with

\[
Qs=ap+u,\qquad s\equiv-1\pmod{4ua}.
\]

Thus, for every fixed `(p,u)`, the Type-II witness search is an **exact finite search** over `Q` and the divisors of `u+Q` up to the displayed bound. This criterion is a useful reparameterization, but it is not claimed to be new.

## 3. Relation to existing literature — important novelty correction

Dahan's Theorem 3.9 in *Sieve dimension and search depth for the Erdős–Straus conjecture* (arXiv:2608.24035v2) gives the two-parameter Type-II criterion `s | an+u`, `s == -1 (mod 4ua)` and the corresponding reconstruction. Dahan's later paper *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture* (arXiv:2611.08717), Proposition 8.1, gives the equivalent bilinear identity

\[
n+w=4uv(aw-u).
\]

With `Q=aw-u`, `r=w`, and `k=v` (renaming to avoid collisions), this is exactly `p+r=4uQk`. Thus neither the two-parameter criterion nor this bilinear reparameterization should be presented as a new theorem. The finite upper bound on `Q` is an elementary consequence of positivity and is used here as an exact finite-search parametrization.

The same paper's Theorem 2.1 gives a dual divisor formulation: for some positive `alpha,u`, the integer `p+4 alpha u^2` has a divisor `s == -1 (mod 4 alpha u)`. Our witness satisfies this with `alpha=k` and `s=4uak-1`; its complementary factor is `r`, because

\[
p+4ku^2 = r(4uak-1),\qquad r\equiv-p\pmod{4uk}.
\]

So the observed small-`u` phenomenon can also be viewed as a bounded-`u` question for this dual divisor family.

Dahan's 2026 one-parameter geometric sieve fixes the **original modulator** `a=1` and varies the other parameter; that is not the same as the current experiment, which fixes the original `u<=4` but allows `a` to grow. Dahan's two-parameter depth `J` restricts both `u` and `a` to at most `J`; our observed `a` can be much larger than 4.

Sources:

- Benjamin Dahan, arXiv:2608.24035v2, Theorem 3.9 and the discussion of the `a=1` slice / two-parameter criterion: https://arxiv.org/abs/2608.24035
- Benjamin Dahan, arXiv:2611.08717, Proposition 8.1: https://arxiv.org/abs/2611.08717

## 4. Additional exact cross-check on Dahan's 14 hyperbolic-exception primes

Dahan's Proposition 3.8/3.13 in arXiv:2608.24035 lists 14 primes below `5*10^9` that lie outside the `a=1` hyperbolic family, and gives Type-II witnesses with both parameters at most 5. Using the present exact bounded-`u` search, I found a `u=1` witness for each of these 14 primes. The corresponding `a` values were:

| `p` | `a` with `u=1` |
|---:|---:|
| 409 | 2 |
| 577 | 2 |
| 5,569 | 5 |
| 9,601 | 2 |
| 23,929 | 2 |
| 83,449 | 6 |
| 102,001 | 6 |
| 329,617 | 2 |
| 712,321 | 2 |
| 1,134,241 | 2 |
| 1,742,409 | 2 |
| 1,726,201 | 2 |
| 5,212,561 | 2 |
| 8,813,281 | 94 |

For all 14 rows, the exact Rosati reconstruction was checked with rational arithmetic and yielded `4/p` exactly. This is a new cross-check of the current program against a published finite exceptional list; it is not a theorem about all primes and is not a claim of novelty.

## 5. What the data does and does not say

The finite data suggests the following **research conjecture**:

> Every prime `p == 1 (mod 24)` admits a normalized Type-II witness with `u <= 4`, with no fixed upper bound imposed on `a`.

This is a strong statement. If true, it would give a Type-II decomposition for every prime in the residue class left by the classical reductions, and hence would imply the Erdős–Straus conjecture. That consequence makes the conjecture much stronger than a routine computational pattern.

Current evidence:

- Python finite scan: through `10^6`.
- Compiled C++ finite scan: through `10^8`.
- Cross-check: 14 additional primes from Dahan's published exceptional list, all solved in the `u=1` slice with `a` ranging up to 94.

Not established:

- No proof that `u <= 4` works for every prime.
- No counterexample beyond the tested range.
- No proof that this bound is new relative to the complete literature.
- No proof of the Erdős–Straus conjecture.

## 6. Next research task

Before extending the computation to larger ranges, audit the exact one-coordinate slice `u <= 4`, `a` unrestricted, against all formulations in Dahan arXiv:2608.24035 and arXiv:2611.08717, plus the Type-I/Type-II literature. In particular:

1. Translate the fixed-`u` quotient criterion into Dahan's dual divisor criterion involving divisors of `p+4 alpha u^2`.
2. Determine whether any published result already gives a bound on this one coordinate with the other coordinate unrestricted.
3. Try to derive a rigorous obstruction for fixed `u` or, conversely, a covering argument for `u=1,2,3,4`.
4. Search for the smallest counterexample to `u<=4` using exhaustive exact code, and save a certificate for every tested prime.

Do not treat a larger finite scan as a proof. The main value of the next step must be a proof, an obstruction, or a new theorem-level reduction.
