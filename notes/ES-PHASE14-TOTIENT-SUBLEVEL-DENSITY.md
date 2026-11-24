# Phase 14 — The totient-sublevel family and the optimal Type-II density coefficient for fixed small u

**Erdős–Straus Research Lab**
**Original draft date:** 23 November 2026
**Latest revision:** 24 November 2026
**Claim ID:** `ES4-TOTIENT-SUBLEVEL-01`
**Status:** a derived corollary of Dahan's Theorem 4.6, using a Wiener–Ikehara counting argument. It is not a proof of the Erdős–Straus conjecture and does not prove that the small-u exceptional set is empty.

## 1. Main theorem

For a prime \(p\equiv1\pmod{24}\), a Type-II witness is a coprime pair \((u,a)\) and a positive divisor \(s\) such that
\[
(u,a)=1,\qquad s\mid ap+u,\qquad s\equiv-1\pmod{4ua}.
\]
Let \(\mathcal E_4(N)\) be the set of such primes \(p\le N\) for which no Type-II witness exists with \(1\le u\le4\), allowing every positive \(a\).

We prove the following derived density estimate:
\[
\boxed{
|\mathcal E_4(N)|\ll
N\exp\left(-\left(\kappa+o(1)\right)(\log\log N)^2\right),
}
\tag{14.1}
\]
where, for any fixed \(0<\gamma<1\) and \(0<\delta_0<1/8\),
\[
\kappa=\frac5{96}\gamma\left(\frac18-\delta_0\right)
\frac{31}{28}\frac{\zeta(2)\zeta(3)}{\zeta(6)}.
\tag{14.2}
\]
In particular, with
\[
\gamma=\frac{999}{1000},\qquad \delta_0=\frac1{65536},
\]
we obtain
\[
\boxed{\kappa\approx0.013993650132,}
\]
which is approximately **99.8878%** of the limiting coefficient
\[
\boxed{
\kappa_\infty=\frac{155}{21504}\frac{\zeta(2)\zeta(3)}{\zeta(6)}
\approx0.014009367918.
}
\tag{14.3}
\]
The limiting coefficient is the supremum for applications of Dahan's Theorem 4.6 restricted to families of Type-II pairs with \(u\le4\), under the mean-modulus constraint in that theorem. It is not claimed to be a universal optimum for all possible sieve methods or for the Erdős–Straus problem itself.

## 2. The density sieve being applied

We use Benjamin Dahan, *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture*, arXiv:2611.08717v1 (5 November 2026), Theorem 4.6, equations (27)–(28).

For a finite family \(\mathcal P\subseteq\mathcal P_2(J)\) of \(P=|\mathcal P|\) coprime pairs, where
\[
\mathcal P_2(J)=\{(u,a)\in[1,J]^2:(u,a)=1\},
\]
put
\[
\log z=\frac{\log N}{4P\log\log N},\qquad
B_N=\log\left(\frac{\log z}{\log(J^5)}\right),
\]
and
\[
\overline\varphi(\mathcal P)=\frac1P\sum_{(u,a)\in\mathcal P}(\varphi(4ua)-2).
\]
If \(J\to\infty\), \(\log P\le(1-\eta_0)\log\log N\) for some fixed \(\eta_0>0\), \(\log z>\log(J^5)\), and
\[
\overline\varphi(\mathcal P)\le\left(\frac18-\delta_0\right)B_N,
\]
then Dahan proves
\[
|E_{\mathcal P}(N)|\ll N\exp\left(-\frac5{96}P\frac{B_N^2}{\log\log N}+O(P\log\log J)\right).
\tag{14.4}
\]
Here \(E_{\mathcal P}(N)\) is the set of primes \(p\le N\), \(p\equiv1\pmod{24}\), that fail every pair in \(\mathcal P\).

Our task is to choose \(\mathcal P=\mathcal P_N\) as efficiently as possible subject to \(u\le4\).

## 3. Exact totient parametrization

For fixed \(u\in\{1,2,3,4\}\), put
\[
C_u=\prod_{q\mid 2u}\left(1-\frac1q\right),\qquad B_u=4uC_u.
\]
The four values are
\[
B_1=2,\quad B_2=4,\quad B_3=4,\quad B_4=8.
\]
For every \(a\) with \((a,u)=1\), Euler's product gives the exact identity
\[
\boxed{
\varphi(4ua)=B_u\,a\prod_{\substack{q\mid a\\q\nmid2u}}\left(1-\frac1q\right).
}
\tag{14.5}
\]
The factor on the right, apart from the fixed \(B_u\), is multiplicative as a function of \(a\) on integers coprime to \(u\).

## 4. Counting modulators by their exact totient value

For each fixed \(u\), define
\[
F_u(X)=\#\{a\ge1:(a,u)=1,\ \varphi(4ua)\le X\}.
\]
The key point is that this counting function has a linear asymptotic with an explicit Euler-product constant.

### Lemma 14.1 — Dirichlet-series factorization

Let
\[
\Pi=\prod_{q>2\atop q\text{ prime}}\left(1+\frac1{q(q-1)}\right).
\]
Then
\[
F_u(X)=\lambda_u X+o(X),
\tag{14.6}
\]
where
\[
\boxed{
\lambda_1=\frac12\Pi,\quad
\lambda_2=\frac18\Pi,\quad
\lambda_3=\frac17\Pi,\quad
\lambda_4=\frac1{16}\Pi.
}
\tag{14.7}
\]

**Proof.** Write \(m_u(a)=\varphi(4ua)\), and let
\[
b_u(n)=\#\{a\ge1:(a,u)=1,\ m_u(a)=n\}.
\]
The coefficients \(b_u(n)\) are nonnegative. For \(\Re s>1\), (14.5) gives the absolutely convergent Euler product
\[
D_u(s):=\sum_{n\ge1}\frac{b_u(n)}{n^s}
=B_u^{-s}\prod_{q\nmid u}
\left(1+\sum_{k\ge1}h_u(q^k)^{-s}\right),
\]
where \(h_u(q^k)=q^k\) if \(q\mid2u\), and \(h_u(q^k)=q^k(1-1/q)\) if \(q\nmid2u\).
Factoring out the Riemann zeta function yields
\[
D_u(s)=B_u^{-s}\zeta(s)H_u(s),
\tag{14.8}
\]
with
\[
H_u(s)=
\prod_{q\mid u}(1-q^{-s})
\prod_{\substack{q>2\\q\nmid u}}
\left(1-q^{-s}+q^{-s}(1-1/q)^{-s}\right).
\tag{14.9}
\]
For every compact subset of \(\Re s>0\), each factor in the second product is
\[
1+O_K(q^{-1-\Re s}),
\]
so the product converges normally there. Thus \(H_u\) is analytic for \(\Re s>0\), and
\[
\lim_{s\to1}(s-1)D_u(s)=\frac{H_u(1)}{B_u}.
\]
At \(s=1\), the local factors are \(1-1/q\) for \(q\mid u\), and \(1+1/[q(q-1)]\) for odd primes \(q\nmid u\). The Wiener–Ikehara Tauberian theorem therefore gives
\[
F_u(X)\sim\frac{H_u(1)}{B_u}X.
\]
Evaluating the four finite factors at \(u=1,2,3,4\) gives exactly (14.7). \(\square\)

### Lemma 14.2 — Sum of the totient costs

Partial summation applied to (14.6) gives
\[
\boxed{
\sum_{\substack{a\ge1:(a,u)=1\\\varphi(4ua)\le X}}
(\varphi(4ua)-2)
=\frac{\lambda_u}{2}X^2+o(X^2).
}
\tag{14.10}
\]
Indeed, if \(F_u(t)=\lambda_ut+o(t)\), then
\[
\sum_{m_u(a)\le X}m_u(a)
=XF_u(X)-\int_0^XF_u(t)\,dt
=\frac{\lambda_u}{2}X^2+o(X^2),
\]
and subtracting \(2F_u(X)=O(X)\) is lower order.

## 5. The exact small-u counting constant

From (14.7),
\[
\sum_{u=1}^4\lambda_u
=\left(\frac12+\frac18+\frac17+\frac1{16}\right)\Pi
=\frac{93}{112}\Pi.
\]
For each odd prime \(q\),
\[
\left(1+\frac1{q(q-1)}\right)(1-q^{-2})=1+q^{-3}.
\]
Therefore
\[
\begin{aligned}
\Pi
&=\prod_{q>2}\frac{1+q^{-3}}{1-q^{-2}}\\
&=\frac{\pi^2}{9}\frac{\zeta(3)}{\zeta(6)}
=\frac{105\zeta(3)}{\pi^4}.
\end{aligned}
\]
Consequently
\[
\boxed{
A_\infty:=2\sum_{u=1}^4\lambda_u
=\frac{93}{56}\Pi
=\frac{31}{28}\frac{\zeta(2)\zeta(3)}{\zeta(6)}
\approx2.15183891219.
}
\tag{14.11}
\]

## 6. The totient-sublevel family

Set
\[
L=\log\log N,\qquad \tau=\frac18-\delta_0,
\qquad T_N=2\gamma\tau L,
\]
where \(0<\gamma<1\) and \(0<\delta_0<1/8\) are fixed. Choose the finite family
\[
\boxed{
\mathcal P_N=
\{(u,a):1\le u\le4,\ (a,u)=1,
\varphi(4ua)\le T_N\}.
}
\tag{14.12}
\]
It is finite. In fact, the elementary inequality
\[
\boxed{\varphi(n)^2\ge\frac n2}
\tag{14.13}
\]
holds for every positive integer \(n\). To see this, if \(n=\prod q^e\), then
\[
\frac{\varphi(n)^2}{n}
=\prod_{q^e\parallel n}q^{e-2}(q-1)^2\ge\frac12,
\]
because the only local factor that can be below 1 is \(q=2,e=1\), where it equals \(1/2\). Thus every pair in (14.12) satisfies
\[
a\le\frac{T_N^2}{2u}\le\frac{T_N^2}{2}.
\]
We may take
\[
J_N=\max\left(4,\left\lceil\frac{T_N^2}{2}\right\rceil\right)=O(L^2).
\tag{14.14}
\]
Also \(J_N\to\infty\), since \(|\mathcal P_N|\to\infty\).

Summing (14.6) and (14.10) over the four values of \(u\), with \(T_N=2\gamma\tau L\), gives
\[
\boxed{
P_N:=|\mathcal P_N|
=(\gamma\tau A_\infty+o(1))L,
}
\tag{14.15}
\]
and
\[
\boxed{
\sum_{(u,a)\in\mathcal P_N}(\varphi(4ua)-2)
=(\gamma^2\tau^2 A_\infty+o(1))L^2.
}
\tag{14.16}
\]
Hence
\[
\boxed{
\overline\varphi(\mathcal P_N)
=(\gamma\tau+o(1))L.
}
\tag{14.17}
\]

## 7. Verification of Dahan's hypotheses

From (14.15), \(P_N\asymp L\), and therefore
\[
\log P_N=O(\log L)=o(L).
\]
Thus the size condition in Theorem 4.6 holds, for example with any fixed \(\eta_0<1\). By (14.14), \(J_N=O(L^2)\), so \(\log J_N=O(\log L)\). With
\[
\log z=\frac{\log N}{4P_NL},
\]
we have
\[
B_N=\log\left(\frac{\log z}{\log(J_N^5)}\right)
=L-O(\log L)\sim L.
\]
Since \(\gamma<1\) is fixed, (14.17) implies
\[
\overline\varphi(\mathcal P_N)
=(\gamma\tau+o(1))L
\le\tau B_N
\]
for all sufficiently large \(N\). Also \(\log z>\log(J_N^5)\) eventually. Thus every hypothesis of Dahan's Theorem 4.6 is satisfied.

Every prime in \(\mathcal E_4(N)\) fails every pair in \(\mathcal P_N\), so
\[
\mathcal E_4(N)\subseteq E_{\mathcal P_N}(N).
\]
Using (14.4), (14.15)–(14.17), and
\[
P_N\log\log J_N=O(L\log\log L)=o(L^2),
\]
we obtain
\[
\boxed{
|\mathcal E_4(N)|\ll
N\exp\left(-\left(\frac5{96}\gamma\tau A_\infty+o(1)\right)L^2\right).
}
\tag{14.18}
\]
This proves (14.1)–(14.3).

## 8. Optimality for the mean-modulus constraint: corrected layer-cake proof

The same counting asymptotic gives an exact variational statement, without any assumption about how many pairs are tied at a cutoff. Put
\[
w(u,a)=\varphi(4ua)-2\ge0,
\]
and define
\[
F(x)=\#\{(u,a):1\le u\le4,\ (u,a)=1,\ w(u,a)\le x\},
\qquad
G(x)=\sum_{w(u,a)\le x}w(u,a).
\]
By Lemma 14.1 and the definition of \(A_\infty\),
\[
F(x)=\left(\frac{A_\infty}{2}+o(1)\right)x=: (c+o(1))x,
\qquad c=\frac{A_\infty}{2}.
\]
Partial summation gives
\[
G(x)=xF(x)-\int_0^xF(t)\,dt
=\left(\frac{c}{2}+o(1)\right)x^2.
\tag{14.19}
\]

For any finite set \(S\) of \(P\) distinct admissible pairs, the layer-cake identity is
\[
\sum_{(u,a)\in S}w(u,a)
=\int_0^\infty\#\{(u,a)\in S:w(u,a)>t\}\,dt.
\]
At most \(F(t)\) elements of \(S\) can have cost at most \(t\). Hence
\[
\sum_{(u,a)\in S}w(u,a)
\ge \int_0^\infty(P-F(t))_+\,dt.
\tag{14.20}
\]

We now evaluate this integral without estimating any fixed-width jump of \(F\). Fix \(0<\varepsilon<c\). There is \(T_\varepsilon\) such that, for all \(t\ge T_\varepsilon\),
\[
(c-\varepsilon)t\le F(t)\le(c+\varepsilon)t.
\]
It follows that
\[
\begin{aligned}
\int_0^\infty(P-F(t))_+\,dt
&\ge \int_{T_\varepsilon}^{P/(c+\varepsilon)}
       (P-(c+\varepsilon)t)\,dt,\\
\int_0^\infty(P-F(t))_+\,dt
&\le PT_\varepsilon+
   \int_{T_\varepsilon}^{P/(c-\varepsilon)}
       (P-(c-\varepsilon)t)\,dt.
\end{aligned}
\]
After division by \(P^2\) and passage to \(P\to\infty\), the lower and upper limits are squeezed between \(1/(2(c+\varepsilon))\) and \(1/(2(c-\varepsilon))\). Letting \(\varepsilon\downarrow0\),
\[
\int_0^\infty(P-F(t))_+\,dt
\sim\frac{P^2}{2c}.
\tag{14.21}
\]

For the matching upper bound on the minimum, fix \(\varepsilon>0\) and put
\[
x_+=\frac{(1+\varepsilon)P}{c}.
\]
Since \(F(x_+)/P\to1+\varepsilon\), for all sufficiently large \(P\) there are at least \(P\) admissible pairs of cost at most \(x_+\). The sum of the \(P\) least costs is therefore at most \(G(x_+)\), and (14.19) gives
\[
G(x_+)=\left(\frac{(1+\varepsilon)^2}{2c}+o(1)\right)P^2.
\]
Combining this with (14.20)–(14.21), then letting \(\varepsilon\downarrow0\), proves
\[
\boxed{
\min_{|S|=P}\sum_{(u,a)\in S}w(u,a)
\sim\frac{P^2}{2c}=\frac{P^2}{A_\infty}.
}
\tag{14.22}
\]
Consequently, every family of \(P\to\infty\) distinct admissible pairs satisfying
\[
\frac1P\sum_{(u,a)\in\mathcal P}w(u,a)\le\tau L
\]
must obey
\[
\boxed{P\le(\tau A_\infty+o(1))L.}
\tag{14.23}
\]
Our totient-sublevel family has
\[
P_N=(\gamma\tau A_\infty+o(1))L,
\]
so for any fixed \(\gamma<1\) it approaches the optimal coefficient to within the factor \(\gamma\); fixed values of \(\gamma\) can be chosen arbitrarily close to 1. This is optimality **only for maximizing the number of selected pairs under the stated mean-cost budget and the restriction \(u\le4\)**. It is not a claim of optimality among all sieve methods, all formulations, or all parameter ranges.

The earlier tie-count argument should not be used: \(F(x)=cx+o(x)\) alone does not imply that the number of pairs tied at a cutoff is \(o(P)\). The layer-cake proof above avoids that unsupported inference entirely.

## 9. Comparison with Phase 12: rectangular versus cost-sublevel selection

Phase 12 optimized the family only within a **rectangular four-slice ansatz**: for each fixed \(u\in\{1,2,3,4\}\), it selected coprime modulators up to a cutoff \(a\le A_u\). Under the same asymptotic mean-cost budget \(\tau L\), its maximal pair-count coefficient within that ansatz is
\[
S_{\rm rect}=\sum_{u=1}^4\frac{d_u}{c_u}
=\frac{361\pi^2}{1728}
\approx2.061879160181,
\]
where \(d_u=\varphi(u)/u\) and \(c_u\) are the constants in Lemma 12.1 of the Phase 12 note. Thus Phase 12 gives the upper coefficient \(\tau S_{\rm rect}\) for rectangular families.

Phase 14 instead ranks **all admissible pairs** with \(u\le4\) by their actual cost \(w(u,a)=\varphi(4ua)-2\). The layer-cake argument proves that the corresponding unrestricted family-size coefficient under the same mean-cost budget is \(\tau A_\infty\), where
\[
A_\infty=\frac{31}{28}\frac{\zeta(2)\zeta(3)}{\zeta(6)}
\approx2.151838912194.
\]
The ratio of these budget-normalized pair-count coefficients is
\[
\frac{A_\infty}{S_{\rm rect}}\approx1.043629982664,
\]
so the cost-sublevel selection improves the **pair-count coefficient by approximately 4.3630%** over the best rectangular four-slice selection, when compared at the same \(\tau\) and \(\gamma\).

This percentage compares the asymptotic pair-count coefficients, not the two particular numerical density exponents printed in Phase 12 and Phase 14: those examples use different choices of \(\gamma\) and \(\delta_0\). Nor does the comparison imply a 4.3630% improvement to the original Erdős–Straus exceptional-set bound. It is a sharper selection rule inside Dahan's Theorem 4.6 and the restricted range \(u\le4\).

## 10. Finite arithmetic audit

`src/phase14_totient_sublevel.py` constructs the family (14.12) for selected surrogate values of \(L\). It uses exact integer totients and the proven upper bound \(a\le T_N^2/(2u)\) to make the search finite. The audit checks:

- exact family cardinality;
- exact sum of \(\varphi(4ua)-2\);
- the observed pair-count and mean-cost ratios against their asymptotic coefficients;
- the actual largest \(a\) against the analytic \(O(L^2)\) coordinate bound.

These finite checks are implementation checks only. They do not establish the Wiener–Ikehara asymptotic or the density theorem; those are proved analytically above. In particular, the asymptotic Dahan mean condition is verified by the fixed margin \(1-\gamma>0\), not by requiring every small numerical surrogate \(L\) to satisfy its eventual inequality.

Reproduce from the repository root:

```powershell
python -m unittest discover -s tests -p "test_phase14_totient_sublevel.py" -v
python -m unittest discover -s tests -v
python src/phase14_totient_sublevel.py --output results/PHASE14-TOTIENT-SUBLEVEL-DENSITY-LOCAL.json
```

## 11. Attribution and scope

- The Type-II divisor criterion and Dahan's Theorem 4.6 are from Benjamin Dahan, arXiv:2611.08717v1 (2026-11-05), Theorem 4.6, equations (27)–(28).
- The Wiener–Ikehara Tauberian theorem is standard. A statement with exactly the nonnegative-coefficient and analytic-continuation hypotheses used here is reproduced in Jacob Korevaar, *Ikehara-Type Theorem Involving Boundedness*, arXiv:0807.0537, Theorem 1.1; see also *Tauberian Theory: A Century of Developments*, Springer (2004). Links: https://arxiv.org/abs/0807.0537 and https://doi.org/10.1007/978-3-662-10225-1.
- Derived here: the four Euler products for the totient-sublevel counting functions, the constants \(\lambda_u\), the aggregate constant \(A_\infty\), the totient-sublevel family, and the optimality statements (14.22)-(14.23) for Dahan's mean-modulus family-size constraint.
- Not claimed: a witness for every prime, the vanishing of \(\mathcal E_4(N)\), a proof of the Erdős–Straus conjecture, or optimality among all analytic/combinatorial approaches.
