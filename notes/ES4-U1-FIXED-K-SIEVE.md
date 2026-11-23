# Fixed-k sieve for the u=1 slice

## 1. Exact criterion

For a normalized Type-II witness at `u=1`, write

\[
s=4ak-1.
\]

Then

\[
s\mid ap+1
\iff
s\mid p+4k.
\]

Indeed,

\[
4k(ap+1)=sp+(p+4k),
\]

and \(\gcd(s,4k)=1\). Therefore for each fixed positive integer \(k\),

\[
\boxed{\text{a u=1 witness with this }k
\iff
\exists s\mid p+4k,\ s\equiv-1\pmod{4k}.}
\]

The reconstruction is

\[
a=\frac{s+1}{4k},\qquad t=\frac{p+4k}{s}.
\]

This is exact for every fixed \(k\), not merely sufficient.

## 2. The first two k-layers

### k=1

The condition becomes a divisor \(s\mid p+4\) with \(s\equiv3\pmod4\). Such a divisor exists iff \(p+4\) has a prime factor \(q\equiv3\pmod4\). Choose \(s=q\), \(a=(q+1)/4\), and \(t=(p+4)/q\).

Thus:

\[
\boxed{k=1\text{ succeeds}\iff p+4\text{ has a prime factor }3\pmod4.}
\]

### k=2

The condition becomes a divisor \(s\mid p+8\) with \(s\equiv7\pmod8\). Since

\[
(\mathbb Z/8\mathbb Z)^\times\cong C_2\times C_2,
\]

write each odd prime residue as \(3^\alpha5^\beta\), with \(\alpha,\beta\in\{0,1\}\):
- 1 ↔ (0,0)
- 3 ↔ (1,0)
- 5 ↔ (0,1)
- 7 ↔ (1,1)

If \(p+8=\prod q_i^{e_i}\), k=2 succeeds iff exponents \(0\le f_i\le e_i\) can be chosen so that

\[
\sum_i f_i\alpha_i\equiv1\pmod2,\qquad
\sum_i f_i\beta_i\equiv1\pmod2.
\]

This is an exact bounded subset-product criterion.

## 3. Examples

| p | p+4 | k=1 | p+8 | k=2 | first known u=1 witness |
|---:|---:|:---:|---:|:---:|---:|
| 73 | 77=7·11 | succeeds | 81=3⁴ | fails | k=1 |
| 97 | 101 | fails | 105=3·5·7 | succeeds | k=2 |
| 193 | 197 | fails | 201=3·67 | fails | no u=1 witness |
| 313 | 317 | fails | 321=3·107 | fails | k=4 |
| 1009 | 1013 | fails | 1017=3²·113 | fails | k=11 |
| 2521 | 2525=5²·101 | fails | 2529=3²·281 | fails | no u=1 witness |
| 66529 | 66533 | fails | 66537=3²·7393 | fails | no u=1 witness |

For p=313, the k=4 witness is

\[
313+16=7(4\cdot3\cdot4-1)=7\cdot47.
\]

The three displayed full u=1 failures (193, 2521, 66529) were separately checked over the complete k-range from the proved bound in the previous addendum; their failure through k=12 alone would not prove full failure.

## 4. Interpretation

The fixed-k view is dual to the quotient-t view:
- quotient-t: find \(d\mid(p+t)/4\) with \(d\equiv-1\pmod t\);
- fixed-k: find \(s\mid p+4k\) with \(s\equiv-1\pmod{4k}\).

Both are equivalent parameterizations of the same u=1 witness, not independent criteria.

The first two layers provide simple arithmetic sieves. Their union does not cover all primes \(p\equiv1\pmod{24}\), as p=193 is already a counterexample to that restricted two-layer coverage. This does not refute u=1 overall or the four-u conjecture.

The supplied program implements exact divisor-residue DP and reconstructs witnesses for each fixed k. Its results are finite checks, not a proof that a fixed number of k-layers covers all primes.
