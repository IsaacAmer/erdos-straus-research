# Phase 14 correction: minimum-cost selection without a tie assumption

**Status (24 November 2026):** The corrected layer-cake argument is now integrated into Section 8 of the main Phase 14 note, equations (14.19)-(14.23). The main note is the canonical version; this document is retained as a historical audit record.

**Purpose:** document the original tie-count issue and its correction.

Let

\[
w(u,a)=\varphi(4ua)-2\ge0,
\]

for admissible pairs `1≤u≤4`, `gcd(u,a)=1`. Define

\[
F(x)=\#\{(u,a):w(u,a)\le x\},
\qquad
G(x)=\sum_{w(u,a)\le x}w(u,a).
\]

Assume the Phase 14 counting asymptotic

\[
F(x)\sim cx,
\qquad c=\frac{A_\infty}{2}.
\]

Partial summation gives

\[
G(x)=xF(x)-\int_0^xF(t)\,dt
\sim\frac c2x^2.
\tag{1}
\]

## Lower bound for any set of P distinct pairs

Let `S` be any set of `P` admissible pairs. The layer-cake identity states

\[
\sum_{(u,a)\in S}w(u,a)
=\int_0^\infty\#\{(u,a)\in S:w(u,a)>t\}\,dt.
\]

At most `F(t)` elements of `S` can have cost at most `t`; therefore

\[
\#\{(u,a)\in S:w(u,a)>t\}\ge(P-F(t))_+.
\]

Consequently

\[
\sum_{(u,a)\in S}w(u,a)
\ge\int_0^\infty(P-F(t))_+\,dt.
\tag{2}
\]

Since `F(t)~ct`, the integral in (2) is asymptotic to

\[
\int_0^{P/c}(P-ct)\,dt
=\frac{P^2}{2c}.
\tag{3}
\]

This lower-bound argument does not assume anything about the number of pairs tied at a cutoff.

## Matching upper bound

Fix `epsilon>0` and set

\[
x_+=\frac{(1+\epsilon)P}{c}.
\]

For sufficiently large `P`, `F(x_+)≥P`, so there are at least `P` pairs of cost at most `x_+`. The sum of the `P` least costs is therefore at most `G(x_+)`. By (1),

\[
G(x_+)\sim\frac c2\left(\frac{(1+\epsilon)P}{c}\right)^2
=\frac{(1+\epsilon)^2P^2}{2c}.
\]

Letting `epsilon` tend to zero and combining with (2)–(3) yields

\[
\boxed{\min_{|S|=P}\sum_{(u,a)\in S}w(u,a)
\sim\frac{P^2}{2c}=\frac{P^2}{A_\infty}.}
\]

Hence any family of `P→∞` distinct admissible pairs satisfying

\[
\frac1P\sum_{(u,a)\in S}w(u,a)\le\tau L
\]

must satisfy

\[
\boxed{P\le(\tau A_\infty+o(1))L.}
\]

The totient-sublevel family in Phase 14 has

\[
P_N=(\gamma\tau A_\infty+o(1))L,
\]

so it approaches this upper bound as the fixed parameter `gamma` approaches 1. This is optimality **only for maximizing the number of selected pairs under the stated mean-cost budget and restricted range `u≤4`**. It is not a claim of optimality among all sieve methods or all possible parameter families.

## Integration checklist

- [ ] Replace the original tie-count paragraph with the proof above.
- [ ] Check the definition of `F` and `G` against the actual Phase 14 note.
- [ ] Verify that all costs are nonnegative (`phi(4ua)≥2`).
- [ ] Check that the counting asymptotic `F(x)~(A_inf/2)x` is independently established with the required hypotheses.
- [ ] Re-read Dahan Theorem 4.6 and verify every parameter condition separately.
- [ ] Keep “optimal within this fixed-u mean-cost model” distinct from “globally optimal sieve.”
- [ ] Rerun the full software tests, and record that this only validates implementation, not the asymptotic proof.
