# ES4-U1 Addendum — sharper bounds and an exact divisor formulation

**Purpose:** continue Problem ES4-U1 from the Phase-4 report. This note proves stronger finite bounds for the `u=1` slice and gives a divisor-residue formulation that is exact for each fixed prime.

**Scope:** throughout, `p` is prime and `p ≡ 1 (mod 24)`. A normalized Type-II witness at `u=1` means positive integers `a,s` satisfying

\[
s\mid ap+1,\qquad s\equiv-1\pmod{4a}.
\]

## 1. A useful factorization identity

Write

\[
s=4ak-1,\qquad k\ge1.
\]

The divisibility `s | ap+1` implies `s | p+4k`, because

\[
4k(ap+1)=(s+1)p+4k=sp+(p+4k).
\]

Conversely, if `s | p+4k` and `s ≡ -1 (mod 4k)`, set `a=(s+1)/(4k)`. Then

\[
4k(ap+1)=(s+1)p+4k=sp+(p+4k),
\]

so `s | 4k(ap+1)`. Since `gcd(s,4k)=1`, it follows that `s | ap+1`.

Thus the `u=1` criterion is exactly:

\[
\boxed{\exists k\ge1,\ \exists s\mid p+4k:\ s\equiv-1\pmod{4k}.}
\tag{U1-Div}
\]

For such a pair, `a=(s+1)/(4k)` and `t=(p+4k)/s` are positive integers, and

\[
\boxed{p+4k=t(4ak-1).}
\tag{U1-Fact}
\]

Since the left side is `1 (mod 4)` and `4ak-1` is `3 (mod 4)`,

\[
t\equiv3\pmod4.
\]

Therefore `t=3` or `t≥7`.

## 2. Sharper bounds than those in the Phase-4 report

The Phase-4 report obtained the valid but weaker bounds

\[
a\le\left\lfloor\frac{p+4}{9}\right\rfloor,
\qquad
k\le\left\lfloor\frac{p+3}{8}\right\rfloor.
\]

The factorization `p+4k=t(4ak−1)` allows both to be improved.

### Lemma U1-SB

Every `u=1` witness for `p ≡ 1 (mod 24)` satisfies

\[
\boxed{a\le\left\lfloor\frac{p+11}{28}\right\rfloor,
\qquad
k\le\left\lfloor\frac{p+3}{20}\right\rfloor.}
\]

**Proof.** Split according to the only two possibilities for `t`.

**Case 1: `t=3`.** From (U1-Fact),

\[
p+3=4k(3a-1),\qquad
M:=\frac{p+3}{4}=(3a-1)k.
\]
Because `p ≡ 1 (mod 24)`, `M ≡ 1 (mod 6)`; in particular `M` is odd and `M ≡1 (mod 3)`. Hence both factors `3a−1` and `k` are odd. Thus `a` is even and `a≥2`, so `3a−1≥5` and

\[
k\le\frac M5=\frac{p+3}{20}.
\]

Reducing `M=(3a−1)k` modulo 3 gives `1 ≡ 2k (mod 3)`, so `k ≡2 (mod 3)`. Together with oddness, `k ≡5 (mod 6)`; this is an additional restriction on the `t=3` branch. Also

\[
a\le\frac{M/5+1}{3}=\frac{p+23}{60}
\le\frac{p+11}{28}.
\]
The last inequality holds for every positive `p`.

**Case 2: `t≥7`.** Since `a,k≥1`,

\[
p+4k=t(4ak-1)\ge7(4ak-1),
\]
whence

\[
p+7\ge(28a-4)k.
\]
As `k≥1`, this gives `a≤(p+11)/28`. Also, using `a≥1`,

\[
p+4k\ge7(4k-1),
\]
so `p+7≥24k` and `k≤(p+7)/24`. Since `p≥73`,

\[
\frac{p+7}{24}\le\frac{p+3}{20}.
\]
This proves both bounds. ∎

**Sharpness checks.** At `p=73`, the witness `(a,k,s,t)=(3,1,11,7)` attains `a=(p+11)/28=3`. At `p=97`, the witness `(a,k,s,t)=(2,5,39,3)` attains `k=(p+3)/20=5`. Thus neither uniform constant in Lemma U1-SB can be decreased in general.

## 3. Exact bounded search over `k`

Combining (U1-Div) with Lemma U1-SB gives a complete finite decision procedure for the `u=1` case of any fixed `p ≡1 (mod 24)`:

\[
\boxed{
\text{U1 succeeds}\iff
\exists 1\le k\le\left\lfloor\frac{p+3}{20}\right\rfloor,
\ \exists s\mid p+4k:
\ s\equiv-1\pmod{4k}.
}
\]

When such `s` is found, `a=(s+1)/(4k)` automatically satisfies the witness equations. Conversely every witness must occur in this `k`-range.

The bound on `a` is also available as an independent consistency check:

\[
1\le a\le\left\lfloor\frac{p+11}{28}\right\rfloor.
\]

This is materially smaller than the Phase-4 bound `a≤(p+4)/9` and the earlier `k≤(p+3)/8`.

## 4. The first quotient layer `t=3` is completely characterized

For `t=3`, the equation becomes

\[
M=\frac{p+3}{4}=(3a-1)k.
\]
A positive divisor of `M` congruent to `2 (mod 3)` exists if and only if `M` has a prime factor `q ≡2 (mod 3)`: if a product is `2 (mod 3)`, at least one of its prime factors is `2 (mod 3)`; conversely such a prime factor itself is a suitable divisor.

Consequently:

\[
\boxed{
\text{There is a `u=1` witness with quotient }t=3
\iff
\frac{p+3}{4}\text{ has a prime factor }q\equiv2\pmod3.
}
\]

An explicit witness is

\[
a=\frac{q+1}{3},\qquad k=\frac{p+3}{4q},
\qquad s=4ak-1.
\]
Because `(p+3)/4 ≡1 (mod 6)`, the prime `q` is necessarily `5 (mod 6)`, and the resulting `k` is `5 (mod 6)`.

This is only the `t=3` layer, not a characterization of all `u=1` witnesses. For example, `p=313` has no such `t=3` witness because `(p+3)/4=79` is prime and `79≡1 (mod 3)`, but it does have a `u=1` witness at `t=7`:

\[
313+16=7(4\cdot3\cdot4-1)=7\cdot47.
\]

## 5. Two other immediate sufficient conditions

The complete divisor criterion also gives two simple edge cases:

1. **`a=1` succeeds** if and only if `(p+1)/2` has a prime factor `q≡3 (mod 4)`. This is the Phase-4 report's `ES4-U1-02`.
2. **`k=1` succeeds** if and only if `p+4` has a prime factor `q≡3 (mod 4)`. Indeed, when `k=1`, the divisor `s` is `3 (mod 4)`; it has a prime factor `3 (mod 4)`. Conversely any such prime factor can be chosen as `s`, with `a=(s+1)/4`.

Therefore a prime for which `u=1` fails must satisfy all three necessary factorization restrictions:

- every odd prime factor of `p+1` is `1 (mod 4)`;
- every prime factor of `p+4` is `1 (mod 4)`;
- every prime factor of `(p+3)/4` is `1 (mod 3)`.

These are necessary, not sufficient, for `u=1` failure.

## 6. The next quotient layer `t=7` and a residue-product test

For `t=7`, define

\[
M_7=\frac{p+7}{4}.
\]
A witness with quotient `t=7` exists if and only if `M_7` has a positive divisor `d` such that

\[
d\equiv6\pmod7.
\]
Indeed, take `d=7a−1`; conversely, from such a divisor set `a=(d+1)/7` and `k=M_7/d`. This gives `p+4k=7(4ak−1)`.

Since the nonzero residue group modulo 7 is cyclic of order 6, and 3 is a primitive root with `−1 ≡ 3^3 (mod 7)`, the condition can be expressed directly from the prime factorization

\[
M_7=\prod_i q_i^{e_i}:
\]
there must exist exponents `0≤f_i≤e_i` with

\[
\sum_i f_i\,\operatorname{ind}_3(q_i)\equiv3\pmod6,
\]
where `ind_3(q_i)` is the discrete logarithm of `q_i` to base 3 modulo 7. This is a bounded subset-sum in the cyclic group `C_6`; it is exact, not just a sufficient condition.

The example `p=313` shows why the `t=3` slice is insufficient: `(p+3)/4=79` has no prime factor `2 (mod 3)`, but

\[
M_7=80,\qquad d=20\mid80,\qquad20\equiv6\pmod7.
\]
Thus `a=3`, `k=4`, `s=47` gives

\[
313+16=7(47).
\]
For the three observed `u=1` failures, the `t=7` divisor test also fails:

| `p` | `M_7=(p+7)/4` | prime factorization | residues of its divisors mod 7 |
|---:|---:|---|---|
| 193 | 50 | `2·5²` | `{1,2,3,4,5}` |
| 2,521 | 632 | `2³·79` | `{1,2,4}` |
| 66,529 | 16,634 | `2·8,317` | `{1,2}` |

This only checks the `t=7` layer. Full `u=1` failure requires all admissible `t=3,7,11,15,...` to fail.

## 6. Exact general characterization of `u=1` failure

For every integer `t ≡3 (mod 4)`, define

\[
M_t=\frac{p+t}{4}.
\]
The identity (U1-Fact) is equivalent to

\[
M_t=(at-1)k.
\]
Therefore a witness with this particular quotient `t` exists exactly when `M_t` has a positive divisor `d` satisfying

\[
d\equiv-1\pmod t.
\]
In that case set `a=(d+1)/t` and `k=M_t/d`.

Also, since `at−1≥t−1` and `k≥1`,

\[
p+t=4(at-1)k\ge4(t-1),
\]
so

\[
3\le t\le\left\lfloor\frac{p+4}{3}\right\rfloor.
\]

Thus `u=1` fails if and only if, for every `t` in this finite arithmetic progression, the divisor-residue set of `M_t` omits `−1 mod t`. This is an exact characterization, but it is not yet a simple closed-form classification of the exceptional primes.

## 8. Exact finite checks for the three observed `u=1` exceptions

Using the sharper `k` bound, the complete ranges are:

| `p` | `a_max = floor((p+11)/28)` | `k_max = floor((p+3)/20)` | Outcome |
|---:|---:|---:|---|
| 193 | 7 | 9 | no `u=1` witness |
| 2,521 | 90 | 126 | no `u=1` witness |
| 66,529 | 2,376 | 3,326 | no `u=1` witness |

The included Python program enumerates every divisor of each `p+4k` in the full proved `k`-range, checks the residue `s≡−1 (mod 4k)`, and verifies any reconstructed witness in the original `s|ap+1` condition. Its tests reproduce these three finite nonexistence checks and positive examples.

A finite certificate for these particular primes is not a classification of all `u=1` failures.

## 9. What this adds to Phase 4 and what remains open

**Newly derived in this addendum:**

- Exact `u=1` divisor criterion using divisors of `p+4k`.
- Sharper universal bounds `a≤(p+11)/28` and `k≤(p+3)/20`.
- The stronger congruence `k≡5 (mod 6)` and `a` even on the `t=3` branch.
- An exact prime-factor characterization of the `t=3` branch.
- The `k=1` sufficient/necessary edge criterion using prime factors of `p+4`.

**Still open:**

- A closed-form characterization of all primes for which `u=1` fails.
- A proof that one of `u=1,2,3,4` always succeeds.
- A counterexample to that four-value conjecture.

These elementary bounds and divisor reformulations are rigorous consequences of the criterion. Their novelty relative to the full literature has not been established and should not be claimed without a full source-by-source comparison.
