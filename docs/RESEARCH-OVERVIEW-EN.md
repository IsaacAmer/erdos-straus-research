# Erdős–Straus Research Lab — Portfolio Overview

**Project:** Independent computational mathematics research
**Public handle:** IsaacAmer
**Repository:** https://github.com/IsaacAmer/erdos-straus-research
**Evidence snapshot:** 24 November 2026 (verified working tree based on commit `cf602b5`, with subsequent local revisions).

## Abstract

The Erdős–Straus conjecture asks whether every integer \(n\ge2\) can be represented as a sum of three unit fractions, \(4/n=1/x+1/y+1/z\), with positive integer denominators. This project is a reproducible computational workbench for investigating selected divisor criteria and Type-II witnesses for primes in the residue class \(p\equiv1\pmod{24}\).

The work combines exact-integer Python implementations, conversions between selected parameterizations, bounded quotient and divisor searches, finite audits of Jacobi-symbol identities, square-class computations, and a local performance comparison of two search procedures. The supplied records report 119 passing unit tests after Phase 14, a finite Phase 10 audit of 246 witnesses against published Jacobi-symbol laws, and a Phase 9 local benchmark in which two procedures returned equal witness sets for \(p=1,000,000,009\), with a recorded timing ratio of approximately 113.96×.

The most recent analytic component selects admissible parameter pairs using a threshold on Euler's totient function \(\varphi(4ua)\), with \(1\le u\le4\), and applies an existing sieve theorem to estimate the size of a restricted exceptional set. The reported exponent constant for the chosen parameters is approximately 0.013993650132. This is a derived restricted-slice corollary, not a proof that the restricted exceptional set is empty and not a proof of the original conjecture. Its novelty and priority have not been established.

The project emphasizes reproducibility and research integrity: published results are attributed, finite computations are not presented as universal proofs, mathematical claims are separated from software tests, and AI-assisted development is disclosed. The repository is best understood as an independently maintained computational research project and a record of mathematical investigation, not as a peer-reviewed paper.

## Keywords

Erdős–Straus conjecture; Egyptian fractions; Type-II divisor witnesses; exact arithmetic; computational number theory; Euler totient; Jacobi symbols; reproducibility.


## Documentation & Verification Snapshot (Commit `cc02edb`)

- **Reference commit:** `cc02edb` on `main`
- **Local verification environment:** Windows 11, Python 3.15.2 (`.venv`)
- **Local test suite:** 119 tests passed in 2.715 s (run on the working tree that became `cc02edb`)
- **CI status (GitHub Actions):** 4 workflow jobs passing on `cc02edb`
- **Phase 13 status:** Phase 13 is not an integrated or tested module in the current release (`v0.1.0`), and the status of any historical work related to it remains unresolved.
