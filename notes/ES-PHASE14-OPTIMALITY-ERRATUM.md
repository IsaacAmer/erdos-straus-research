# Phase 14 erratum — repairing the minimum-cost argument and clarifying scope

**Date:** 23 November 2026  
**Related note:** `notes/ES-PHASE14-TOTIENT-SUBLEVEL-DENSITY.md`  
**Claim:** `ES4-TOTIENT-SUBLEVEL-01`  
**Purpose:** a correction/clarification to Section 8 of the Phase 14 note. The density derivation in Sections 1–7 is logically separate from the issue identified below.

## 1. The point that needs correction

The Phase 14 note uses

\[
F(x)=\#\{(u,a):1\le u\le4,\ (u,a)=1,\ w(u,a)\le x\}
\sim \frac{A_\infty}{2}x,
\]

and then asserts that the number of pairs tied at the cutoff, `F(x_P)-F(x_P-1)`, is `o(P)`. That last assertion does **not** follow from `F(x)=cx+o(x)` alone: an asymptotic for the cumulative counting function does not, by itself, control increments over intervals of fixed length. The conclusion can be proved without any tie estimate. Replace the tie paragraph in Section 8 by the argument below.

## 2. Correct layer-cake proof

Write

\[
w(u,a)=\varphi(4ua)-2,\qquad c=\frac{A_\infty}{2}.
\]

Let

\[
F(x)=\#\{(u,a):1\le u\le4,\ (u,a)=1,\ w(u,a)\le x\}
\]

and

\[
G(x)=\sum_{w(u,a)\le x}w(u,a).
\]

The Phase 14 Dirichlet-series argument gives `F(x)~cx`. Partial summation then gives

\[
G(x)=xF(x)-\int_0^xF(t)\,dt
\sim \frac{c}{2}x^2.
\tag{E.1}
\]

For any finite set \(S\) of \(P\) distinct admissible pairs, the layer-cake identity is

\[
\sum_{(u,a)\in S}w(u,a)
=\int_0^\infty
\#\{(u,a)\in S:w(u,a)>t\}\,dt.
\]

At every \(t\ge0\), at most \(F(t)\) elements of \(S\) can have cost at most \(t\). Hence

\[
\sum_{(u,a)\in S}w(u,a)
\ge \int_0^\infty (P-F(t))_+\,dt.
\tag{E.2}
\]

Since \(F(t)\sim ct\), squeezing \(F(t)\) between \((c-\epsilon)t\) and \((c+\epsilon)t\) for sufficiently large \(t\) shows

\[
\int_0^\infty(P-F(t))_+\,dt
\sim \frac{P^2}{2c}.
\tag{E.3}
\]

For the matching upper bound, fix \(\epsilon>0\) and set

\[
x_+=\frac{(1+\epsilon)P}{c}.
\]

For sufficiently large \(P\), `F(x_+)≥P`. Thus there are at least \(P\) admissible pairs of cost at most \(x_+\), and the sum of the \(P\) least costs is at most `G(x_+)`. By (E.1),

\[
G(x_+)
\sim \frac{c}{2}\left(\frac{(1+\epsilon)P}{c}\right)^2
=\frac{(1+\epsilon)^2}{2c}P^2.
\]

Letting \(\epsilon\downarrow0\), and combining this with (E.2)–(E.3), proves

\[
\boxed{
\min_{|S|=P}\sum_{(u,a)\in S}w(u,a)
\sim \frac{P^2}{2c}
=\frac{P^2}{A_\infty}.
}
\tag{E.4}
\]

This proves the same asymptotic minimum-cost statement as intended in Phase 14, without making an unjustified claim about ties.

Consequently, if a family of `P→∞` distinct admissible pairs satisfies

\[
\frac1P\sum_{(u,a)\in S}w(u,a)\le \tau L,
\]

then (E.4) implies

\[
\boxed{P\le(\tau A_\infty+o(1))L.}
\]

The totient-sublevel family in Phase 14 has

\[
P_N=(\gamma\tau A_\infty+o(1))L,
\]

so, as fixed \(\gamma\uparrow1\), it approaches this upper bound. The optimality statement is therefore valid **for maximizing the number of pairs under this mean-cost budget, restricted to \(u\le4\)**. It is not a claim of global optimality among all sieve methods, all formulations, or all parameter ranges.

## 3. A necessary comparison with Dahan's other results

The Phase 14 exceptional set is

\[
\mathcal E_4(N)=\{p\le N: p\text{ prime},\ p\equiv1\pmod{24},
\text{ and no Type-II witness exists for any }u\le4\text{ and any }a\}.
\]

This is **not** the same set as Dahan's \(E_2(N;Y)\), which consists of primes failing all pairs in the full hyperbolic family

\[
\mathcal P_{\rm hyp}(Y)=\{(u,a): (u,a)=1,\ ua\le Y\},
\]

where `u` is not restricted to four values and `a` is not unrestricted. The two exceptional sets need not contain one another. Therefore the bounds for them must not be compared as though they were bounds on the same set.

Dahan's Theorem 4.8, with \(Y=\lfloor(1/16)\log\log N\rfloor\), gives

\[
|E_2(N;Y)|\ll N\exp\bigl(-(c_0-o(1))(\log\log N)^2
\log\log\log N\bigr),
\quad c_0=\frac{15}{8192\pi^2},
\]

for that different hyperbolic exceptional set. Dahan's Theorem 7.12 also gives a stronger bound on the **reduced Erdős–Straus exceptional set** \(E(N)\), under the paper's standing convention that \(n\) is a prime with \(n\equiv1\pmod{24}\):

\[
|E(N)|\ll N\exp\left(-c'\frac{(\log N)^{5/7}}
{(\log\log N)^{2/7}}\right).
\]

On that reduced prime domain, a genuine Erdős–Straus exception cannot possess any Type-II witness, so it is contained in \(\mathcal E_4(N)\) and in Dahan's \(E_2(N;Y)\). This inclusion is one-way: a prime in \(\mathcal E_4(N)\) may still have a Type-II witness with \(u>4\), or a Type-I representation, and therefore need not be an Erdős–Straus exception. Thus Dahan's stronger global bound controls the original exceptional set, **not the larger restricted set** \(\mathcal E_4(N)\). Phase 14 studies a complementary restricted-parameter obstruction.

## 4. Prior work on the totient sublevel count and novelty limits

The general asymptotic
\[
\#\{m\ge1:\varphi(m)\le X\}
=\left(\frac{\zeta(2)\zeta(3)}{\zeta(6)}+o(1)\right)X
\]
is classical, not new to this project. Paul T. Bateman, *The distribution of values of the Euler function*, Acta Arithmetica 21 (1972), 329–345, states this counting problem explicitly, gives the same constant, and explains a Wiener–Ikehara proof. The Phase 14 fixed-\(u\) counts are restricted Euler-product variants of this classical result; their derivation is useful for the chosen application, but should not be described as a new general theorem about the distribution of \(\varphi\).

A closely related Erdős–Straus antecedent is Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, \(n\equiv1\pmod{24}\)*, arXiv:2608.24035v2 (9 November 2026), Lemma 4.22. It already contains the constant
\[
\frac12\prod_{q>2}\left(1+\frac1{q(q-1)}\right)
=\frac{\zeta(2)\zeta(3)}{3\zeta(6)},
\]
which is exactly the Phase 14 coefficient \(\lambda_1=\Pi/2\), although it occurs there in a different sum, namely \(\sum_{u\le J}1/\varphi(4u)\).

The potentially project-specific part is the calculation of the four restricted constants for \(\varphi(4ua)\) with fixed \(u=1,2,3,4\), and their use to build a near-optimal family for Dahan's Theorem 4.6 under its mean-cost constraint. This is a **candidate derived corollary/application**, not established priority. The layer-cake optimality proof is an elementary rearrangement principle once the counting asymptotic is known. A specialist literature review is required before claiming novelty or submitting it as an original theorem.

## 5. Recommended wording for the project

Use this description in the README, abstracts, and messages to researchers:

> We derive a totient-sublevel family for the restricted Type-II slice `u≤4`. A Wiener–Ikehara argument gives explicit Euler-product counting constants, and a layer-cake variational argument shows that this family is asymptotically optimal for maximizing the number of selected pairs under the mean-modulus budget in Dahan's Theorem 4.6. This is a derived restricted-slice density corollary; it does not prove that the restricted exceptional set is empty and does not improve the known bound on the full Erdős–Straus exceptional set.

## 6. Attribution

The Type-II criterion and the sieve theorem used here are due to Benjamin Dahan, arXiv:2611.08717v1, Theorem 4.6. The hyperbolic comparison is Dahan's Theorem 4.8, and the global exceptional-set bound is Theorem 7.12. The Phase 14 contribution is the particular fixed-`u` totient distribution calculation, its explicit constants, and the restricted mean-cost optimization derived from those results. Novelty/priority remains subject to a specialist literature review.
