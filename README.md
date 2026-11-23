# Erdős–Straus Research Lab

**Status:** Exploratory computational research  
**Main focus:** Divisor criteria and Type-II witness searches for the Erdős–Straus conjecture

## Overview

The Erdős–Straus conjecture asks whether every integer $n \geq 2$ admits a representation

$$ \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z},
\qquad x,y,z\in\mathbb Z_{>0}. $$

This repository is a reproducible workbench for studying selected divisor formulations associated with the conjecture. Its current computational focus is the Type-II criterion for primes $p\equiv 1\pmod{24}$, especially the restricted case $u=1$. The code explores fixed-parameter and quotient-layer searches, reconstructs candidate witnesses, and checks identities using exact integer arithmetic.

**This repository does not claim a proof of the Erdős–Straus conjecture.** It also makes no claim that the exploratory reformulations or bounds documented here are new. Novelty and priority require independent literature review.

## Current scope

The current code and notes cover:

- Exact integer verification of selected Egyptian-fraction decompositions.
- Parameter conversions and cross-checks among selected Type-I and Type-II formulations.
- The $u=1$ Type-II case, including fixed-$k$ and fixed-quotient formulations.
- Divisor-residue tests for selected quotient layers, including $t=3,7,11,15,19$.
- Finite searches for specified prime inputs, with reconstruction and verification of any reported witness.

A finite search that finds no witness only rules out the searched parameter range or the specified restricted case. It does not show that the prime has no Erdős–Straus representation.

## Repository layout

```text
src/        Python implementations and exact-arithmetic search tools
tests/      Unit tests for implementations and selected identities
notes/      Mathematical derivations, proof drafts, and audit notes
sources/    Bibliographic notes and references
results/    Saved output from selected computational runs
```

Additional project documents include the research log and research protocol.

## Requirements

- Python 3.10 or later is recommended.
- The current test suite is designed to use Python's standard library; no third-party package installation should be required for the commands below.

## Run the tests

### Windows PowerShell

From the repository root:

```powershell
py -3 -m unittest discover -s tests -v
```

If you prefer to use the project's existing virtual environment:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

### Linux / macOS

```bash
python3 -m unittest discover -s tests -v
```

The project maintainer reported 58 passing unit tests in the local development environment on 23 November 2026. Re-run the suite after cloning; test results are environment- and revision-specific. Passing tests validate only the tested code paths and examples. They are not a proof of a universal mathematical statement.

## Run selected programs

From the repository root in Windows PowerShell:

```powershell
python .\src\u1_factor_criterion.py
python .\src\u1_quotient_layers.py
python .\src\u1_t15_t19_layers.py
python .\src\u1_fixed_k_sieve.py
```

If using the existing virtual environment:

```powershell
.\.venv\Scripts\python.exe .\src\u1_factor_criterion.py
.\.venv\Scripts\python.exe .\src\u1_quotient_layers.py
.\.venv\Scripts\python.exe .\src\u1_t15_t19_layers.py
.\.venv\Scripts\python.exe .\src\u1_fixed_k_sieve.py
```

These scripts print selected examples and bounded-search results. Read the corresponding files in `notes/` for the mathematical scope and limitations of each computation.

## Mathematical status and limitations

1. The conjecture remains open; this repository supplies no general proof.
2. The Type-II identities and divisor criteria used as starting points are related to criteria already present in the literature. This repository records experiments and derivations around them; it does not claim priority for those criteria.
3. Bounds and equivalences in the notes must be read under their stated hypotheses. A computational test is not a substitute for a proof.
4. The current $u=1$ search is a restricted case. Failure at $u=1$, or failure in finitely many quotient layers, does not imply failure of Type II or of the original conjecture.
5. No claim is made that the proposed restriction $u\leq 4$ holds for every prime.
6. Computational claims should be accompanied by source code, exact input ranges, and reproducible output.

## Research practice

The project aims to keep the following separate:

- proved algebraic statements;
- finite computations and their exact search ranges;
- conjectures and heuristic observations;
- literature claims that still need source-level verification.

When reporting a computational result, include the input range, algorithm, software environment, output, and the exact mathematical claim the computation does—and does not—support.

## Selected references

- Benjamin Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, $n\equiv1\pmod{24}$*, arXiv:2608.24035: https://arxiv.org/abs/2608.24035
- Benjamin Dahan, *Composite witness sieves, Kneser–Plancherel containers, and the exponent $5/7$ for the Erdős–Straus conjecture*, arXiv:2611.08717: https://arxiv.org/abs/2611.08717
- Eugen J. Ionascu and Andrew Wilson, *On the Erdős–Straus Conjecture* (2011), *Revue Roumaine de Mathématiques Pures et Appliquées*, 56(1), 21–30: https://www.csm.ro/reviste/Revue_Mathematique/pdfs/2011/1/Ionascu.pdf
- Kyle Bradford, *Elemental Patterns from the Erdős–Straus Conjecture*, arXiv:2403.16047: https://arxiv.org/abs/2403.16047

See `sources/` for the project's working bibliography. These references are starting points, not an exhaustive literature review.

## Contributions and feedback

Corrections to code, test cases, citations, or mathematical derivations are welcome. Please identify the exact file and claim, and provide a reproducible example where possible. Distinguish a counterexample to a computational subclaim from a counterexample to the Erdős–Straus conjecture itself.

## License

No license is currently specified. Until a license is added, do not assume that the code or notes may be reused, redistributed, or incorporated into another project merely because this repository is publicly viewable.


