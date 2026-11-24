# Erdős–Straus Research Lab

- **Project type:** Independent computational and analytic workbench in number theory
- **Repository:** <https://github.com/IsaacAmer/erdos-straus-research>
- **Documentation snapshot:** 24 November 2026
- **Git base:** `cf602b54b285043a387d27602edc70d55201772a`
- **Verification state:** the 119-test run reported below was performed on the working tree based on that commit, after the local Phase 14 documentation/source correction; those local changes had not yet been committed at the time of the run.

## Overview

The Erdős–Straus conjecture asks whether every integer $n\ge2$ can be written as

$$
\frac4n=\frac1x+\frac1y+\frac1z,
\qquad x,y,z\in\mathbb Z_{>0}.
$$

This repository is a reproducible workbench for selected divisor criteria and Type-II witness searches, with particular attention to primes $p\equiv1\pmod{24}$. It contains exact-integer Python implementations, parameter conversions, bounded searches, finite character audits, performance experiments, and analytic notes applying existing sieve results to restricted parameter families.

**The repository does not prove the Erdős–Straus conjecture.** In particular, it does not prove that every prime $p\equiv1\pmod{24}$ has a Type-II witness with $u\le4$, and it does not establish priority for the Phase 14 application.

## Quick Start

### Requirements
- Python 3.11 or 3.13 (validated in GitHub Actions).
- No third-party packages are required for the core tests.

### Clone the repository
```bash
git clone https://github.com
cd erdos-straus-research
```

### Run the complete test suite
```bash
python -m unittest discover -s tests -v
```

### Run the Phase 14 density audit
```bash
python src/phase14_totient_sublevel.py --output results/PHASE14-TOTIENT-SUBLEVEL-DENSITY-LOCAL.json
```

The local JSON output is ignored by Git and is intended for reproducibility checks.

## Research map

- **Foundations and parameter conversions:** exact verification of selected Egyptian-fraction identities and cross-checks among selected Type-I and Type-II parameterizations.
- **Phases 4–8:** restricted Type-II criteria, fixed-parameter and quotient-layer searches, finite witness certificates, and independent search implementations.
- **Phase 9:** a local comparison of two search implementations on selected prime inputs.
- **Phases 10–11:** finite Jacobi-symbol and small-$u$ character/square-class audits.
- **Phase 11 density corollary:** a coarse finite family of Type-II pairs with $u\le4$, used in an application of Dahan's Theorem 4.6.
- **Phase 12:** an optimized *rectangular four-slice* family, with separate cutoffs $a\le A_u$ for each $u\in\{1,2,3,4\}$.
- **Phase 14:** a *totient-sublevel* family selected by the actual cost $w(u,a)=\varphi(4ua)-2$, together with a corrected layer-cake optimality argument.

The current integrated test inventory contains Phase 6–12 and Phase 14 tests. There is no separate `test_phase13_*.py` module in the tested inventory; Phase 13 should not be described as a separately validated component unless its status and files are documented independently.

## Phase 14: restricted Type-II density corollary

For $u\in\{1,2,3,4\}$, the note studies

$$
F_u(X)=\#\{a\ge1:(a,u)=1,\ \varphi(4ua)\le X\}.
$$

The derived fixed-$u$ constants are

$$
\lambda_1=\frac{\Pi}{2},\quad
\lambda_2=\frac{\Pi}{8},\quad
\lambda_3=\frac{\Pi}{7},\quad
\lambda_4=\frac{\Pi}{16},
$$

where

$$
\Pi=\prod_{q>2}\left(1+\frac1{q(q-1)}\right)
=\frac{105\zeta(3)}{\pi^4}.
$$

Thus

$$
A_\infty=2\sum_{u=1}^4\lambda_u
=\frac{31}{28}\frac{\zeta(2)\zeta(3)}{\zeta(6)}
\approx2.151838912194.
$$

Selecting all admissible pairs with $u\le4$ and $\varphi(4ua)\le2\gamma\tau\log\log N$, where $\tau=1/8-\delta_0$ and fixed $0<\gamma<1$, gives the derived restricted exceptional-set estimate

$$
|\mathcal E_4(N)|\ll
N\exp\!\left(-\left(\kappa+o(1)\right)(\log\log N)^2\right),
\qquad
\kappa=\frac5{96}\gamma\tau A_\infty.
$$

For the documented choices $\gamma=999/1000$ and $\delta_0=1/65536$, the program reports

$$
\kappa\approx0.013993650132,
\qquad \kappa_{\rm limit}\approx0.014009367918.
$$

This is a **derived corollary for the restricted set** of primes that fail every Type-II pair with $u\le4$. It does not prove that this restricted exceptional set is empty or finite, and it is not an improvement to the known bound on the full Erdős–Straus exceptional set.

### Phase 14 optimality statement

The corrected layer-cake argument proves

$$
\min_{|S|=P}\sum_{(u,a)\in S}\bigl(\varphi(4ua)-2\bigr)
\sim\frac{P^2}{A_\infty},
$$

where the minimum ranges over sets of $P$ distinct admissible pairs with $u\le4$ and $(u,a)=1$. Therefore, under the mean-cost budget $\frac1P\sum_S(\varphi(4ua)-2)\le\tau L$, one has

$$
P\le(\tau A_\infty+o(1))L.
$$

This is optimality **only for the pair-count/mean-cost variational problem with $u\le4$**. It is not global optimality among all sieve methods or all possible parameter families. The corrected proof does not rely on an unsupported estimate for the number of pairs tied at a cutoff.

### Comparison with Phase 12

Phase 12 optimizes only within rectangular four-slice families and has pair-count coefficient

$$
S_{\rm rect}=\sum_{u=1}^4\frac{d_u}{c_u}
=\frac{361\pi^2}{1728}
\approx2.061879160181.
$$

Phase 14's cost-sublevel selection has coefficient $A_\infty\approx2.151838912194$. Consequently,

$$
\frac{A_\infty}{S_{\rm rect}}\approx1.043629982664,
$$

an improvement of approximately **4.363% in the asymptotic pair-count coefficient** under the same mean-cost budget and the same $u\le4$ restriction. This is not a 4.363% improvement to the full conjecture's exceptional-set bound. The particular numerical $\kappa$ values previously printed for Phases 12 and 14 use different $\gamma$ and $\delta_0$, so those two printed exponents should not be directly compared as a controlled benchmark.

## Reported computational evidence

The following are finite, environment-specific software checks, not universal mathematical proofs:

- **Phase 6:** tests reconstruct Type-II certificates for a fixed set of 14 selected literature/boundary primes, including checks of the stated finite parameter box.
- **Phases 7–8:** exact witness-set comparisons between two search approaches on the finite regression inputs, including 76 primes through 5000, 14 selected literature primes, and selected boundary cases.
- **Phase 9:** one recorded local benchmark at $p=1{,}000{,}000{,}009$ reported about 9.126452 s for Phase 7 and 0.080084 s for Phase 8 (about 113.96× in that run). This is one machine/input measurement, not a general speedup guarantee.
- **Phase 10:** a finite audit checked 246 generated witnesses against the cited Jacobi-symbol identities; the relevant tests also check standard Jacobi-symbol behavior and rejection of corrupted inputs.
- **Phase 11:** finite character and square-class computations, including parameter-box checks through 10,000 and explicit local/global consistency tests.
- **Phase 12:** exact finite totient sums and mean-cost audits for the rectangular family.
- **Phase 14:** exact finite totient-sublevel audits, including family cardinality, total cost, observed versus predicted ratios, and the coordinate bound.

### Latest local test run

On 24 November 2026, the maintainer reported the following run on Windows 11, Python 3.15.2, using the repository's `.venv` interpreter:

- Phase 14-specific suite: **11 tests passed** in 0.341 s.
- Full discovered suite: **119 tests passed in 2.575 s**.
- `python src/phase14_totient_sublevel.py` completed and reported the constants above, with finite audit values $L\in\{100,250,500,1000\}$.
- `git diff --check` returned no whitespace errors.

These checks were run on the working tree based on commit `cf602b5`, **after** the local Phase 14 note and program-metadata edits, but **before** those edits were committed. They therefore document that tested working tree, not the unmodified commit alone. The finite $L$-values are surrogate implementation audits, not a search over primes up to a corresponding value of $N$.

To reproduce the tests from the repository root in Windows PowerShell:

```powershell
python -m unittest discover -s tests -p "test_phase14_totient_sublevel.py" -v
python -m unittest discover -s tests -v
python .\src\phase14_totient_sublevel.py --output .\results\PHASE14-TOTIENT-SUBLEVEL-DENSITY-LOCAL.json
```

For a traceable run, also record:

```powershell
python --version
python -c "import sys, platform; print(sys.executable); print(platform.platform())"
git rev-parse HEAD
git status --short
```

A passing test suite validates only the code paths and examples it exercises. It does not establish the analytic asymptotics or Dahan's theorem.

## Repository layout

```text
src/        Python implementations and exact-arithmetic search tools
tests/      Unit tests for implementations and selected identities
notes/      Mathematical derivations, proof drafts, and audit notes
sources/    Bibliographic notes and references
results/    Saved output from selected computational runs
docs/       Project documentation, reviews, and presentation material
```

## Research integrity and open limitations

- The Type-II criterion and the sieve estimates applied in Phases 11, 12, and 14 are attributed to the cited literature; the project records specific derived applications and finite implementations.
- Bateman's classical work already studies the distribution of values of Euler's $\varphi$-function. The general totient-distribution method is not claimed as new.
- A related Euler-product constant appears in Dahan's earlier preprint in a different sum. The fixed-$u$ counting constants and their use in this restricted family are treated as a project derivation whose novelty/priority has not been established.
- The density estimate for $\mathcal E_4(N)$ does not prove $\mathcal E_4(N)=\varnothing$.
- Dahan's stronger bound for the original exceptional set concerns a different set. It must not be compared as though it were a bound on $\mathcal E_4(N)$.
- Phase 13 is not represented as a separately tested integrated module in the current test inventory.
- No license is currently specified. Public visibility on GitHub does not itself grant permission to reuse or redistribute the code or notes.

## Selected references

- P. T. Bateman, “The distribution of values of the Euler function,” *Acta Arithmetica* 21 (1972), 329–345. DOI: <https://doi.org/10.4064/aa-21-1-329-345>. Publisher PDF: <https://matwbn.icm.edu.pl/ksiazki/aa/aa21/aa2115.pdf>.
- B. Dahan, “Sieve dimension and search depth for the Erdős–Straus conjecture, $n\equiv1\pmod{24}$,” arXiv:2608.24035v2 (last revised 5 November 2026): <https://arxiv.org/abs/2608.24035v2>.
- B. Dahan, “Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture,” arXiv:2611.08717v1 (submitted 5 November 2026): <https://arxiv.org/abs/2611.08717v1>.
- J. Korevaar, “Ikehara-Type Theorem Involving Boundedness,” arXiv:0807.0537: <https://arxiv.org/abs/0807.0537>.
- E. J. Ionascu and A. Wilson, “On the Erdős–Straus Conjecture,” *Revue Roumaine de Mathématiques Pures et Appliquées* 56 (2011), 21–30: <https://www.csm.ro/reviste/Revue_Mathematique/pdfs/2011/1/Ionascu.pdf>.
- K. Bradford, “Elemental Patterns from the Erdős–Straus Conjecture,” arXiv:2403.16047: <https://arxiv.org/abs/2403.16047>.

The bibliography in `sources/` is the working source list. The references above are not an exhaustive literature review.

## Citation, release, and licensing

`CITATION.cff` is included for software citation. Before making a formal release, verify its author/alias fields, decide on a license only after checking the provenance and rights for every included file, and ensure the release tag points to the exact tested commit. A Zenodo DOI or Software Heritage identifier should only be claimed after the archive has actually been created.

## Contributions and feedback

Corrections to code, test cases, citations, or mathematical derivations are welcome. Please identify the exact file and claim, provide a reproducible example where possible, and distinguish a counterexample to a restricted computational claim from a counterexample to the Erdős–Straus conjecture itself.
