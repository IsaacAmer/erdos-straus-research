# Phase 5 Addendum — Strong density bound for the small-Type-II-parameter problem

**Project:** Erdős–Straus Research Lab  
**Date:** 23 November 2026  
**Status:** rigorous corollary of Dahan's published-on-arXiv sieve theorems; not a new independent theorem  
**Scope:** primes \(p\equiv1\pmod{24}\), Type-II witnesses with one normalized parameter \(u\le4\)

---

## 1. The exact question studied by the project

Dahan's two-parameter Type-II criterion says that, for a prime \(p\equiv1\pmod{24}\), a Type-II witness exists precisely when there are positive integers \(u,a,s\) satisfying

\[
 s\mid ap+u,\qquad s\equiv-1\pmod{4ua}.
 \tag{1}
\]

By Dahan's normalization lemma, one may assume \(\gcd(u,a)=1\) without changing \(s\) or increasing \(u\).

The project's restricted statement is

\[
(R_4)\qquad
\forall p\equiv1\pmod{24}\text{ prime},\quad
\exists u\in\{1,2,3,4\},\ a,s\ge1\text{ satisfying (1)}.
\]

Let \(\mathcal E_4(N)\) denote the set of primes \(p\le N\), \(p\equiv1\pmod{24}\), for which **no** witness exists for any \(u\le4\) and any positive modulator \(a\).

The question \(R_4\) is pointwise: is \(\mathcal E_4(N)\) empty for every \(N\)? The results below do not prove that.

## 2. Strongest consequence obtained from Dahan's sieve: a stretched-exponential exceptional-set bound

Dahan's Definition 4.1 defines \(E_2(N;J)\) as the primes \(p\le N\), \(p\equiv1\pmod{24}\), for which there is no Type-II witness among **any** coprime parameter pairs

\[
1\le u\le J,\qquad 1\le a\le J.
\]

Dahan's Theorem 4.33 proves that, for every fixed \(\varepsilon>0\) (sufficiently small), one can choose a depth \(J=J(N)\) with

\[
\log J\le (0.692830\ldots+\varepsilon)(\log N)^{1/3}
\]

such that

\[
\boxed{
|E_2(N;J)|\ll_{\varepsilon}
N\exp\!\left(-(0.1093-\varepsilon)(\log N)^{2/3}\right).
}
\tag{2}
\]

The constant \(0.1093\) is the explicit numerical value given in Theorem 4.33(b); the paper obtains it from the exact sieve constant \(\kappa_1^*=9/(2\pi^2)\). This is a theorem about a growing two-parameter search depth, not a result restricted to \(u\le4\).

### Corollary 5A — the project's exceptional set inherits this stronger bound

For all sufficiently large \(N\), the chosen \(J(N)\) is at least 4. If \(p\in\mathcal E_4(N)\), then it has no witness for any \(u\le4\), regardless of \(a\). In particular, it has no witness for any coprime pair with \(u,a\le J(N)\). Thus

\[
\mathcal E_4(N)\subseteq E_2(N;J(N)).
\]

Combining this inclusion with (2) gives

\[
\boxed{
|\mathcal E_4(N)|\ll_{\varepsilon}
N\exp\!\left(-(0.1093-\varepsilon)(\log N)^{2/3}\right).
}
\tag{3}
\]

This is stronger than the fixed-depth consequence \(N/(\log N)^A\) for every fixed \(A>0\): for each fixed \(A\), the stretched-exponential factor in (3) is eventually smaller than \((\log N)^{-A}\).

**Interpretation.** The proportion of primes \(p\equiv1\pmod{24}\) that fail all four families \(u=1,2,3,4\), even with unrestricted \(a\), tends to zero very rapidly in the asymptotic sense of (3).

**Attribution and novelty.** The sieve estimate (2) is Dahan's Theorem 4.33. The implication (3) is the elementary set inclusion above, specialized to the project's restriction. It is a useful project-specific corollary, but it is not claimed as a new independent theorem or as an improvement to Dahan's estimate.

### What (3) does not say

The bound does **not** imply that \(\mathcal E_4(N)\) is empty or finite. Indeed, for every fixed \(c>0\),

\[
N\exp\bigl(-c(\log N)^{2/3}\bigr)\longrightarrow\infty.
\]

It is therefore compatible with infinitely many exceptional primes. It does not establish \(R_4\), and it does not prove the Erdős–Straus conjecture.

## 3. An independent fixed-depth refinement

For a fixed integer \(J\ge1\), define

\[
\mathcal P_{4,J}=
\{(u,a):1\le u\le4,\ 1\le a\le J,\ \gcd(u,a)=1\}.
\]

Its cardinality is

\[
\begin{aligned}
P_4(J)
&=J+\left\lceil\frac J2\right\rceil
 +(J-\left\lfloor\frac J3\right\rfloor)
 +\left\lceil\frac J2\right\rceil\\
&=2J+2\left\lceil\frac J2\right\rceil
 -\left\lfloor\frac J3\right\rfloor.
\end{aligned}
\]

Dahan's Theorem 4.3 gives, for every fixed finite set \(\mathcal P\) of coprime pairs,

\[
|E_{\mathcal P}(N)|\ll_{\mathcal P}
\frac{N}{(\log N)^{1+|\mathcal P|/2}}.
\]

Since \(\mathcal E_4(N)\subseteq E_{\mathcal P_{4,J}}(N)\), for every fixed \(J\),

\[
\boxed{
|\mathcal E_4(N)|\ll_J
\frac{N}{(\log N)^{1+P_4(J)/2}}.
}
\tag{4}
\]

For example, \(J=1\) gives four parameter pairs and exponent 3; \(J=2\) gives six pairs and exponent 4; \(J=3\) gives nine pairs and exponent \(5.5\). The implied constant depends on fixed \(J\). One must not let \(J\) grow with \(N\) in (4) without a separate uniform estimate; Theorem 4.33 is the appropriate result for a growing depth.

## 4. Exact algebraic normal form used by the project's search

Starting from (1), write

\[
s=4uak-1,\qquad v=\frac{ap+u}{s}.
\]

Dahan's Type-II reconstruction gives \(a\mid u+v\). Set

\[
t=\frac{u+v}{a},\qquad v=at-u.
\]

Then

\[
\boxed{p+t=4u(at-u)k.}
\tag{5}
\]

Conversely, if positive integers \(a,k,t\) satisfy (5), and \(\gcd(u,a)=1\), setting \(s=4uak-1\) gives

\[
 ap+u=(at-u)(4uak-1),
\]
so (1) follows. If an initially constructed pair \((u,a)\) is not coprime, Dahan's normalization lemma divides both parameters by their gcd and preserves the same divisor \(s\); the normalized first parameter can only decrease.

For \(p\equiv1\pmod{24}\) and \(u=1,2,3,4\), the least positive residues \(r_u\equiv-p\pmod{4u}\) are

\[
r_1=3,\quad r_2=7,\quad r_3=11,
\]

and

\[
r_4=\begin{cases}15,&p\equiv1\pmod{16},\\7,&p\equiv9\pmod{16}.\end{cases}
\]

Each satisfies \(r_u>u\). Put \(d=at-u\). Then (5) becomes

\[
p+t=4udk,\qquad d\ge t-u.
\]

It follows that each fixed prime has a finite exact search range:

\[
\boxed{t\le\left\lfloor\frac{p+4u^2}{4u-1}\right\rfloor,}
\]

\[
\boxed{k\le\left\lfloor\frac{p+r_u}{4u(r_u-u)}\right\rfloor,}
\]

and

\[
\boxed{
a\le\left\lfloor\min\left\{
\frac{p+4u^2}{r_u(4u-1)},
\frac{p+r_u+4u^2}{4ur_u}
\right\}\right\rfloor.}
\]

These bounds depend on \(p\); they are not absolute constants. For the fixed normalized value \(u\), retain the condition \(\gcd(u,a)=1\). If this fails, normalization changes the first parameter to a smaller divisor of \(u\), which is relevant when testing the union \(u\le4\).

## 5. Pomerance–Weingartner coordinates

Pomerance–Weingartner's Type-II criterion for a prime denominator \(p\) is the existence of positive integers \(A,B,E\) with

\[
E\mid A+B,\qquad 4AB\mid p+E.
\tag{PW-II}
\]

Dahan's Type-II parameters and these parameters encode the same existence statement. From a Dahan witness, put

\[
B=\frac{ap+u}{s},\quad
k=\frac{s+1}{4ua},\quad
E=\frac{u+B}{a},\quad A=u.
\]

Then \(E\mid A+B\) and \(p+E=4uBk\). Conversely, from (PW-II), put

\[
a=\frac{A+B}{E},\quad k=\frac{p+E}{4AB},\quad s=4Aak-1.
\]

A direct calculation gives \(sB=ap+A\) and \(s\equiv-1\pmod{4Aa}\); Dahan's gcd normalization handles a non-coprime pair. Thus the project's restriction \(u\le4\) is equivalently

\[
\boxed{\exists A,B,E\ge1:\quad E\mid A+B,\quad4AB\mid p+E,
\quad\min(A,B)\le4.}
\]

This is a convenient way to state the open subproblem. The parameter conversion is a crosswalk between published criteria, not a new criterion.

## 6. Reproducibility and claim labels

The repository's reported computation through \(10^8\) is finite evidence only. The Phase 3 audit reports 719,781 primes \(p\le10^8\), \(p\equiv1\pmod{24}\), with minimal normalized \(u\)-counts 719,778 at \(u=1\), two at \(u=2\), none at \(u=3\), and one at \(u=4\). The reported maximum modulator is 5,839, at \(p=41,900,329\). This does not prove (R4).

Before calling this computation independently reproducible, the repository should retain together: the exact C++ source, exact compile command and compiler version, exact run command and flags, raw output, and a small independent Python regression check for the exceptional cases and sample witnesses.

## 7. References

- Benjamin Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, \(n\equiv1\pmod{24}\)*, arXiv:2608.24035v2 (5 November 2026), Definition 4.1, Theorems 3.9, 4.3 and 4.33, and Lemma 3.10: https://arxiv.org/abs/2608.24035
- Carl Pomerance and Andreas Weingartner, *Exceptions to the Erdős–Straus–Schinzel conjecture*, *Ramanujan Journal* 69 (2026), Article 31, especially Corollary 2.4: https://arxiv.org/abs/2511.16817
- Kyle Bradford, *Elemental Patterns from the Erdős–Straus Conjecture*, *Integers* 25 (2025), A54; arXiv:2403.16047: https://arxiv.org/abs/2403.16047
- Elsholtz and Tao (2013), the framework acknowledged by Pomerance–Weingartner for the Type-I/Type-II parametrizations: https://arxiv.org/abs/1303.3025
