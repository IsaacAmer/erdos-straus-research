# Phase 12 — An optimized finite family for the small-u Type-II density bound

**Erdős–Straus Research Lab**  
**Date:** 23 November 2026  
**Claim ID:** `ES4-DENSITY-OPT-01`  
**Status:** a derived quantitative corollary of Dahan's Theorem 4.6, with a sharper explicit parameter family and an exact mean-totient asymptotic. It is not a proof of the Erdős–Straus conjecture and is not presented as an independent replacement for Dahan's theorem.

## 1. Result in one statement

Let \(\mathcal E_4(N)\) be the set of primes \(p\le N\), \(p\equiv1\pmod{24}\), for which there is no Type-II witness
\[
\gcd(u,a)=1,\qquad s\mid ap+u,\qquad s\equiv-1\pmod{4ua}
\]
for any \(u\in\{1,2,3,4\}\) and any positive integer \(a\).

We derive from Dahan's Theorem 4.6 the explicit bound
\[
\boxed{
|\mathcal E_4(N)|
\ll N\exp\left(-\left(\kappa+o(1)\right)(\log\log N)^2\right),
\qquad
\kappa=\frac{504317\pi^2}{377487360}
\approx0.01318563165.
}
\]

The earlier phase-5 application used the coarse estimate \(\varphi(4ua)-2\le4ua\) and the cutoff \(ua\le0.01\log\log N\). The present choice computes the mean of \(\varphi(4ua)\) sharply for each of the four fixed values of \(u\), then chooses four different modulator cutoffs. The resulting leading exponent coefficient is about **15.85 times** the coefficient obtained from that earlier coarse parameter choice.

This is a sharper application of an existing theorem, not a new proof of the conjecture. The statement depends on Dahan's published-as-preprint Theorem 4.6 and should be cited accordingly.

## 2. The exact mean-totient lemma

For fixed \(u\in\{1,2,3,4\}\), define
\[
d_u=\frac{\varphi(u)}u,
\qquad
c_u=\frac{12u}{\pi^2}\prod_{q\mid 2u}\frac{q}{q+1},
\]
where the product is over the distinct prime divisors of \(2u\).

### Lemma 12.1

As \(X\to\infty\),
\[
\boxed{
\sum_{\substack{a\le X\\(a,u)=1}}
\left(\varphi(4ua)-2\right)
=d_uc_uX^2+O_u(X\log X).
}
\tag{12.1}
\]
Consequently,
\[
\frac{1}{\#\{a\le X:(a,u)=1\}}
\sum_{\substack{a\le X\\(a,u)=1}}
\left(\varphi(4ua)-2\right)
=c_uX+O_u(\log X).
\tag{12.2}
\]

**Proof.** Put
\[
C(u)=\prod_{q\mid2u}\left(1-\frac1q\right).
\]
For \((a,u)=1\), the totient identity gives
\[
\varphi(4ua)
=4ua\,C(u)
\sum_{\substack{d\mid a\\(d,2u)=1}}\frac{\mu(d)}d.
\]
Summing over \(a\le X\), writing \(a=db\), and using \((d,2u)=1\), we obtain
\[
\sum_{\substack{a\le X\\(a,u)=1}}\varphi(4ua)
=4uC(u)
\sum_{\substack{d\le X\\(d,2u)=1}}\mu(d)
\sum_{\substack{b\le X/d\\(b,u)=1}}b.
\]
For fixed \(u\), the elementary progression estimate is
\[
\sum_{\substack{b\le T\\(b,u)=1}}b
=\frac{\varphi(u)}{2u}T^2+O_u(T).
\]
Therefore the main term is
\[
2\varphi(u)C(u)X^2
\sum_{\substack{d\ge1\\(d,2u)=1}}\frac{\mu(d)}{d^2}
+O_u(X\log X).
\]
The Euler product equals
\[
\sum_{\substack{d\ge1\\(d,2u)=1}}\frac{\mu(d)}{d^2}
=\frac1{\zeta(2)}
\prod_{q\mid2u}\left(1-\frac1{q^2}\right)^{-1}.
\]
Since
\[
\frac{1-1/q}{1-1/q^2}=\frac q{q+1},
\qquad \zeta(2)=\frac{\pi^2}{6},
\]
the leading coefficient becomes
\[
\frac{12\varphi(u)}{\pi^2}
\prod_{q\mid2u}\frac q{q+1}
=d_uc_u.
\]
Subtracting \(2\#\{a\le X:(a,u)=1\}=O_u(X)\) does not change the error term. This proves (12.1), and (12.2) follows from
\(\#\{a\le X:(a,u)=1\}=d_uX+O_u(1)\). \(\square\)

For the four values of \(u\), the constants are:

| \(u\) | \(d_u=\varphi(u)/u\) | \(c_u\) |
|---:|---:|---:|
| 1 | \(1\) | \(8/\pi^2\) |
| 2 | \(1/2\) | \(16/\pi^2\) |
| 3 | \(2/3\) | \(18/\pi^2\) |
| 4 | \(1/2\) | \(32/\pi^2\) |

## 3. The optimized family

Write
\[
L=\log\log N,
\qquad
\delta_0=\frac1{1024},
\qquad
\tau=\frac18-\delta_0=\frac{127}{1024},
\qquad
\gamma=\frac{99}{100}.
\]
For \(u=1,2,3,4\), set
\[
 x_u=\frac{\gamma\tau}{c_u},
 \qquad A_u=\lfloor x_uL\rfloor,
\]
and choose the finite family
\[
\boxed{
\mathcal F_N=
\{(u,a):1\le u\le4,\ 1\le a\le A_u,\ \gcd(u,a)=1\}.
}
\tag{12.3}
\]
The numerical cutoff coefficients are:

| \(u\) | \(x_u\) | cutoff \(A_u\) |
|---:|---:|---:|
| 1 | 0.1514777052… | \(\lfloor0.1514777052\,L\rfloor\) |
| 2 | 0.0757388526… | \(\lfloor0.0757388526\,L\rfloor\) |
| 3 | 0.0673234246… | \(\lfloor0.0673234246\,L\rfloor\) |
| 4 | 0.0378694263… | \(\lfloor0.0378694263\,L\rfloor\) |

Let \(P_N=|\mathcal F_N|\). From the coprime counting estimate and Lemma 12.1,
\[
P_N=\sum_{u=1}^4d_uA_u+O(1)
=\gamma\tau L\sum_{u=1}^4\frac{d_u}{c_u}+O(1).
\]
A direct calculation gives
\[
\begin{aligned}
\sum_{u=1}^4\frac{d_u}{c_u}
&=\pi^2\left(\frac18+\frac1{32}+\frac1{27}+\frac1{64}\right)\\
&=\frac{361\pi^2}{1728}.
\end{aligned}
\]
Hence
\[
\boxed{P_N=(S+o(1))L,
\qquad S=\gamma\tau\frac{361\pi^2}{1728}
=\frac{504317\pi^2}{19660800}.}
\tag{12.4}
\]

### 3.1 Optimality within the rectangular four-slice ansatz

More generally, take cutoffs \(A_u=\lfloor y_uL\rfloor\) with fixed \(y_u>0\). The preceding lemma gives
\[
\frac{P_N}{L}=\sum_{u=1}^4d_uy_u+o(1),
\qquad
\frac{\overline\varphi(\mathcal P_N)}{L}
=\frac{\sum_{u=1}^4d_uc_uy_u^2}
{\sum_{u=1}^4d_uy_u}+o(1).
\]
Thus the asymptotic mean constraint is
\[
\sum_{u=1}^4d_uc_uy_u^2
\le \tau\sum_{u=1}^4d_uy_u.
\]
By Cauchy–Schwarz,
\[
\left(\sum_{u=1}^4d_uy_u\right)^2
\le
\left(\sum_{u=1}^4d_uc_uy_u^2\right)
\left(\sum_{u=1}^4\frac{d_u}{c_u}\right),
\]
so every such rectangular family satisfies
\[
\boxed{\limsup_{N\to\infty}\frac{P_N}{L}
\le \tau\frac{361\pi^2}{1728}.}
\]
Equality in the continuous optimization occurs when \(y_u=\tau/c_u\). Our choice \(y_u=\gamma\tau/c_u\) with \(\gamma=0.99\) therefore attains **99% of the maximum asymptotic pair count** allowed by the mean constraint within this four-slice rectangular ansatz, while retaining a fixed margin for lower-order terms and for \(B_N/L<1\).

The mean modulus appearing in Dahan's theorem is
\[
\overline\varphi(\mathcal F_N)
=\frac1{P_N}\sum_{(u,a)\in\mathcal F_N}
(\varphi(4ua)-2).
\]
Applying Lemma 12.1 separately to the four slices gives
\[
\begin{aligned}
\sum_{(u,a)\in\mathcal F_N}(\varphi(4ua)-2)
&=\sum_{u=1}^4d_uc_uA_u^2+O(L\log L)\\
&=\gamma^2\tau^2L^2\sum_{u=1}^4\frac{d_u}{c_u}+O(L\log L).
\end{aligned}
\]
Dividing by (12.4),
\[
\boxed{\overline\varphi(\mathcal F_N)
=\gamma\tau L+O(\log L).}
\tag{12.5}
\]

## 4. Verification of every hypothesis of Dahan Theorem 4.6

Take
\[
J=\lceil x_1L\rceil.
\]
Since \(x_1>x_2>x_3>x_4>0\), and \(u\le4\), for all sufficiently large \(N\) we have
\[
\mathcal F_N\subseteq\mathcal P_2(J).
\]
Also \(J\to\infty\) and
\[
\log P_N=O(\log L)=o(L),
\]
so the theorem's size condition \(\log P_N\le(1-\eta_0)L\) holds, for example with any fixed \(\eta_0<1\), once \(N\) is sufficiently large.

Dahan defines
\[
\log z=\frac{\log N}{4P_N\log\log N}
=\frac{e^L}{4P_NL}.
\]
Since \(P_N\asymp L\) and \(J\asymp L\),
\[
B_N:=\log\left(\frac{\log z}{\log J^5}\right)
=L-O(\log L)\sim L,
\]
so \(\log z>\log J^5\) eventually.

The mean condition (27) in Dahan's Theorem 4.6 is
\[
\overline\varphi(\mathcal F_N)
\le\left(\frac18-\delta_0\right)B_N
=\tau B_N.
\]
By (12.5), its left side is \(\gamma\tau L+O(\log L)\), while its right side is \(\tau L+O(\log L)\). Since \(\gamma=0.99<1\), the fixed linear margin
\((1-\gamma)\tau L\) dominates all \(O(\log L)\) terms. Thus the mean condition holds for all sufficiently large \(N\).

All hypotheses of Theorem 4.6 are therefore satisfied by \(\mathcal F_N\).

## 5. Density conclusion for the full small-u exceptional set

Let \(E_{\mathcal F_N}(N)\) be Dahan's exceptional set for the finite family \(\mathcal F_N\). Every prime in \(\mathcal E_4(N)\) fails every pair with \(u\le4\), and hence fails every pair in \(\mathcal F_N\). Therefore
\[
\boxed{\mathcal E_4(N)\subseteq E_{\mathcal F_N}(N).}
\tag{12.6}
\]
Theorem 4.6 gives
\[
|E_{\mathcal F_N}(N)|
\ll N\exp\left(
-\frac5{96}P_NB_N^2\frac1L
+O(P_N\log\log J)
\right).
\]
Now
\[
P_N=(S+o(1))L,\quad B_N=(1+o(1))L,
\quad P_N\log\log J=O(L\log\log L)=o(L^2).
\]
Consequently,
\[
|E_{\mathcal F_N}(N)|
\ll N\exp\left(-\left(\frac5{96}S+o(1)\right)L^2\right).
\]
Combining this with (12.6) proves
\[
\boxed{
|\mathcal E_4(N)|
\ll N\exp\left(-\left(\kappa+o(1)\right)(\log\log N)^2\right),
\quad
\kappa=\frac5{96}S
=\frac{504317\pi^2}{377487360}
\approx0.01318563165.
}
\tag{12.7}
\]

This result says that, outside an exceptional set of the displayed size, every prime \(p\equiv1\pmod{24}\) has a Type-II witness with one of the four values \(u=1,2,3,4\), and its corresponding modulator satisfies the explicit scale bound
\[
a\le A_u=\lfloor x_u\log\log N\rfloor.
\]
It still does **not** show that \(\mathcal E_4(N)\) is empty, and therefore does not prove the universal small-u claim or the Erd\u0001s\u0001–Straus conjecture.

## 6. Comparison with the earlier coarse application

The earlier phase-5 family used \(ua\le Y\), \(u\le4\), \(Y=0.01L\), and the crude pointwise bound \(\varphi(4ua)-2\le4ua\). Its resulting leading exponent coefficient was
\[
\kappa_{\rm old}=\frac5{96}\cdot\frac{115}{72}\cdot0.01
\approx0.00083188657.
\]
The optimized four-slice family above yields
\[
\frac{\kappa}{\kappa_{\rm old}}\approx15.8503.
\]
This comparison is about the explicit constants in these two applications of Theorem 4.6, not about a change in the underlying theorem or a proof of a stronger universal statement.

## 7. Finite audit and reproducibility

`src/phase12_density_optimization.py` computes exact finite values of
\[
P_N,\qquad \sum_{(u,a)\in\mathcal F_N}(\varphi(4ua)-2),
\]
using integer totient arithmetic. It then checks the numerical mean condition for selected test values of \(L\). This is an implementation audit only; the proof of (12.1)–(12.7) is analytic.

From the repository root:

```powershell
python -m unittest discover -s tests -p "test_phase12_density_optimization.py" -v
python -m unittest discover -s tests -v
python src/phase12_density_optimization.py --output results/PHASE12-OPTIMIZED-U4-DENSITY.json
```

The finite audit uses \(L\in\{100,200,500,1000,5000,10000\}\). These values test the formulas and cutoff implementation; they are not claims about a computed range of primes.

## 8. Attribution and research status

- **Source theorem:** Benjamin Dahan, *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture*, arXiv:2611.08717v1 (5 November 2026), Theorem 4.6, especially equations (27)–(28): https://arxiv.org/abs/2611.08717
- **Derived here:** the fixed-u summatory totient constants for \(u=1,2,3,4\), the optimized four-slice parameter family, and the resulting explicit corollary constant \(\kappa\).
- **Not claimed:** an original proof of Dahan's sieve theorem, a proof that every prime has a small-u witness, or a proof of the Erdős–Straus conjecture.
- **Novelty assessment:** the application is an explicit optimization of a published theorem. The exact mean asymptotics are elementary consequences of the totient identity and standard summation. A priority claim for the particular optimized constants would require a separate literature audit.
