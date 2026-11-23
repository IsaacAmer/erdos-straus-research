# ES4-U1-T11 — divisor residues at the next quotient layer

**Research continuation:** Phase 4, after the exact `u=1` criterion and sharpened bounds.

## 1. General quotient-layer identity

For `u=1`, write a witness as

\[
p+4k=t(4ak-1),\qquad t\equiv3\pmod4.
\]
Set

\[
M_t=\frac{p+t}{4}.
\]
Then

\[
M_t=(at-1)k.
\]
Consequently, a witness in the fixed quotient layer `t` exists if and only if `M_t` has a positive divisor `d` satisfying

\[
d\equiv-1\pmod t.
\]
The reconstruction is exact:

\[
a=\frac{d+1}{t},\qquad k=\frac{M_t}{d},\qquad s=4ak-1.
\]

The converse follows by substitution. The allowed quotient range is

\[
3\le t\le\left\lfloor\frac{p+4}{3}\right\rfloor,
\qquad t\equiv3\pmod4.
\]

## 2. The `t=11` layer

Set

\[
M_{11}=\frac{p+11}{4}.
\]
The exact criterion is

\[
\boxed{\exists d\mid M_{11}: d\equiv10\pmod{11}.}
\]

The multiplicative group `(Z/11Z)^×` is cyclic of order 10, and 2 is a primitive root. Since `−1 ≡ 10 ≡ 2^5 (mod 11)`, factor

\[
M_{11}=\prod_i q_i^{e_i}.
\]
For each prime factor `q_i != 11`, let `ell_i` be the discrete logarithm satisfying `q_i ≡ 2^{ell_i} (mod 11)`. A divisor `d=prod q_i^{f_i}` has residue `−1` if and only if

\[
\boxed{\sum_i f_i\ell_i\equiv5\pmod{10},
\qquad 0\le f_i\le e_i.}
\]

If `11 | M_11`, its exponent in `d` must be zero, because a divisor divisible by 11 cannot be congruent to 10 modulo 11.

This is an exact bounded subset-sum problem in the cyclic group `C_10`. It is an equivalent finite test of the divisor condition, not a proof that the layer always succeeds.

## 3. The three observed `u=1` failures also fail at `t=11`

| `p` | `M_11` | factorization | residues of all divisors modulo 11 |
|---:|---:|---|---|
| 193 | 51 | `3·17` | `{1,3,6,7}` |
| 2,521 | 633 | `3·211` | `{1,2,3,6}` |
| 66,529 | 16,635 | `3·5·1109` | `{1,3,4,5,9}` |

In each case, residue 10 is absent, so no witness exists in the `t=11` layer. This is a local obstruction at one layer only; full failure of `u=1` requires all admissible `t` to fail. The previous finite `u=1` program checked the complete bounded range for these three specific primes.

For comparison, `p=313` fails at `t=3` and `t=11`, but succeeds at `t=7`:

\[
M_7=80,\quad20\mid80,\quad20\equiv-1\pmod7.
\]
This illustrates why checking a few initial layers is not a classification.

## 4. A simple infinite family at any eligible fixed layer

There is an immediate `k=1` construction. Let `t>=3`, `t≡3 (mod 4)`, `gcd(t,24)=1`, and let `p` be prime satisfying

\[
p\equiv1\pmod{24},\qquad p\equiv-4\pmod t.
\]
Then set

\[
a=\frac{p+t+4}{4t},\qquad s=\frac{p+4}{t},\qquad k=1.
\]
Both are positive integers, `s=4a−1`, and

\[
p+4=ts.
\]
The `u=1` divisor equivalence then gives `s | ap+1`. Thus this entire arithmetic progression of primes has a `u=1` witness.

Because `gcd(t,24)=1`, the Chinese remainder theorem gives one residue class modulo `24t` satisfying the two congruences. Its residue is coprime to `24t` (as `t` is odd and coprime to 24), so Dirichlet's theorem implies infinitely many primes in this class.

Examples:

- `t=7`: `p≡73 (mod 168)`; for every prime in this class the formulas give `a=(p+11)/28`, `s=(p+4)/7`, `k=1`.
- `t=11`: `p≡73 (mod 264)`; for every prime in this class the formulas give `a=(p+15)/44`, `s=(p+4)/11`, `k=1`.

This is an elementary sufficient family, not a solution to the full `u=1` problem. The two progressions overlap at primes satisfying both conditions, and there is no claim that their union covers all primes `1 mod 24`.

## 5. What this layer analysis adds

- It translates the `t=11` layer into a bounded residue subset-sum in `C_10`.
- It explains explicitly why the three current `u=1` exceptions fail at `t=11` as well as at `t=3,7`.
- It supplies explicit infinite arithmetic progressions of primes with `u=1` witnesses, via `k=1`.

The derivations are elementary. Their novelty relative to all prior literature has not been established. The main open problem remains to prove that some layer `t` succeeds for every prime `p≡1 (mod 24)`, or to characterize the primes for which every layer fails.
