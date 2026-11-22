# ES-PHASE3 — A finite quotient parametrization for Type-II witnesses

**Status:** Exact lemma + computational observation. Not a proof of Erdős–Straus and not a novelty claim.

## 1. Starting criterion

Use the normalized Type-II criterion in Dahan, Theorem 3.9:

\[
\gcd(u,a)=1,\qquad s\mid ap+u,\qquad s\equiv -1\pmod{4ua},
\]

with positive integers \(u,a,s\), and prime \(p\equiv1\pmod{24}\).

Since \(s>0\) and \(s\equiv-1\pmod{4ua}\), write

\[
s=4uak-1,\qquad k\in\mathbb Z_{>0}.
\]

Define the positive integer quotient

\[
Q=\frac{ap+u}{s}.
\]

Then

\[
Q(4uak-1)=ap+u,
\]

so

\[
a(4uQk-p)=u+Q.
\]

Consequently \(a\mid u+Q\). Put

\[
r=\frac{u+Q}{a}.
\]

The same identity becomes

\[
\boxed{p+r=4uQk.}
\]

Therefore \(4uQ\mid p+r\), and because \(r\le u+Q\),

\[
4uQ\le p+r\le p+u+Q,
\]

which yields the explicit finite bound

\[
\boxed{1\le Q\le \left\lfloor\frac{p+u}{4u-1}\right\rfloor.}
\]

## 2. Converse and exact finite criterion

Conversely, fix \(p,u>0\). A normalized Type-II witness with this \(u\) exists if and only if there are positive integers \(Q,a\) such that

\[
1\le Q\le\left\lfloor\frac{p+u}{4u-1}\right\rfloor,
\]

\[
 a\mid u+Q,\qquad \gcd(a,u)=1,
\]

and

\[
\boxed{4uQ\mid p+\frac{u+Q}{a}.}
\]

For the reverse direction, put

\[
r=(u+Q)/a,\quad k=(p+r)/(4uQ),\quad s=4uak-1.
\]

Then \(k\ge1\), \(s>0\), \(s\equiv-1\pmod{4ua}\), and direct calculation gives

\[
Qs=4uakQ-Q=ap+u.
\]

Thus \(s\mid ap+u\), as required.

This is an exact bounded search over \(Q\) and divisors \(a\mid u+Q\) for each fixed \(u\). It is an algebraic reparametrization of the known Type-II criterion, not a new theorem about all primes.

## 3. Reproducible finite computation

The accompanying Python implementation uses only the standard library. It enumerates all primes \(p\le N\) with \(p\equiv1\pmod{24}\), then for each \(u=1,2,3,4\) searches every admissible \(Q\) up to the proved bound and every divisor \(a\mid u+Q\). The witness is checked against the original equations.

### Python run

An independent Python 3 implementation gave:

- \(N=10^6\): 9,732 primes; minimal \(u=1\) for 9,729, \(u=2\) for 2, \(u=4\) for 1; none required \(u>4\).
- \(N=10^7\): 82,887 primes; minimal \(u=1\) for 82,884, \(u=2\) for 2, \(u=4\) for 1; none required \(u>4\).

The only primes in these ranges for which no \(u=1\) witness was found are

\[
193,\quad2521,\quad66529.
\]

### Independent C++ run

A separate C++17 implementation of the same exact finite criterion was compiled with `g++ -O3 -march=native -std=c++17` and run up to \(10^8\). It reported:

| Minimum \(u\) found | Number of primes |
|---:|---:|
| 1 | 719,778 |
| 2 | 2 |
| 3 | 0 |
| 4 | 1 |
| **Total** | **719,781** |

No prime in the tested range lacked a Type-II witness with \(u\le4\).

The three exceptions to \(u=1\) were witnessed as follows:

| \(p\) | \(u\) | \(a\) | \(Q\) | \(r\) | \(k\) | \(s=4uak-1\) |
|---:|---:|---:|---:|---:|---:|---:|
| 193 | 2 | 1 | 5 | 7 | 5 | 39 |
| 2,521 | 2 | 1 | 29 | 31 | 11 | 87 |
| 66,529 | 4 | 11 | 1,041 | 95 | 4 | 703 |

Each row satisfies \(r=(u+Q)/a\), \(p+r=4uQk\), and \(s\mid ap+u\).

The Python run through \(10^7\) and the C++ run through \(10^8\) are independent implementations, but the \(10^8\) output should still be treated as a computational certificate summary, not a formal proof.

## 4. Exact representations for the three u=1 exceptions

Using the Rosati Type-II reconstruction already present in the project, the three witnesses above yield:

\[
\frac4{193}=\frac1{4825}+\frac1{1930}+\frac1{50},
\]

\[
\frac4{2521}=\frac1{804199}+\frac1{55462}+\frac1{638},
\]

\[
\frac4{66529}=\frac1{3047294316}+\frac1{11709104}+\frac1{16656}.
\]

These examples show that failure of the restricted \(u=1\) family does not mean failure of the conjecture; here the Type-II witness with \(u=2\) or \(u=4\) succeeds.

## 5. Relation to Dahan's fixed-depth result

Dahan's abstract defines depth \(J\) using **both** coprime parameters \(u,a\le J\). The present computation bounds only \(u\le4\); it does not bound \(a\), which can grow with \(p\). Therefore this is not a verification of Dahan's fixed-depth statement with \(J=4\), nor does it contradict the exceptional-set theorem.

Reference: Benjamin Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, \(n\equiv1\pmod{24}\)*, arXiv:2608.24035v2 (5 November 2026), especially Theorem 3.9 and the abstract's definition of \(E_2(N;J)\).

## 6. What is and is not established

**Established exactly:** the quotient parametrization and the finite upper bound on \(Q\), for every fixed \(p,u\), by direct algebra.

**Established computationally:** up to \(10^7\) using Python and up to \(10^8\) using a separate C++ implementation, every prime \(p\equiv1\pmod{24}\) tested has a normalized Type-II witness with \(u\le4\).

**Not established:** that every such prime has a witness with \(u\le4\); that \(a\) is bounded; that the observation is new in the literature; or that the Erdős–Straus conjecture is solved.

## 7. Next research question

Investigate whether there is a theoretical reason for the observed one-coordinate bound \(u\le4\), while allowing \(a\) to grow. First compare this exact condition with all parameter-reduction lemmas and search-depth statements in Dahan v2 and the prior literature. Then attempt either:

1. prove a uniform bound on \(u\), or
2. construct an infinite family of primes for which the least possible normalized Type-II \(u\) exceeds 4.

A finite search cannot decide between these alternatives.
