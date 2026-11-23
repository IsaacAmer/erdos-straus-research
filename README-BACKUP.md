# Erdos-Straus Research Lab — starter repository

This is a reproducible workspace for investigating the Erdős–Straus conjecture:

    For every integer n >= 2, find positive integers a,b,c such that
    4/n = 1/a + 1/b + 1/c.

## Research integrity rules

- A finite computation is evidence about the tested range, not a proof for all n.
- Never report a computational result without the exact code, parameters, runtime environment, and saved output.
- Distinguish theorem, lemma, conjecture, heuristic, computation, and unverified claim.
- Use exact integer/rational arithmetic. Do not use floating-point equality to verify identities.
- Before calling an idea new, search the literature and compare the exact statement, not just the wording.
- Preserve failed approaches and counterexamples.

## Initial setup (Windows PowerShell)

From this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m unittest discover -s tests -v
```

The initial checker uses only Python's standard library. Do not install NumPy, Numba, or a large symbolic stack just for this first phase.

Optional later additions, only when needed:

- `sympy` for symbolic algebra and factorization experiments.
- JupyterLab for exploratory notebooks.
- Lean 4 + Mathlib for formalizing stable lemmas after we know precisely what to prove.

## Repository layout

- `src/erdos_straus.py`: exact arithmetic helpers and a conditional construction.
- `tests/`: reproducible tests.
- `research_log.md`: dated session checkpoints.
- `RESEARCH_PROTOCOL.md`: research and verification standards.
- `PROJECT_INSTRUCTIONS_AR.md`: instructions to paste into the ChatGPT Project.
- `sources/`: bibliography records and source PDFs/notes.
- `results/`: machine outputs; every result must include the command and code version.
- `notes/`: derivations, counterexamples, and rejected approaches.

## Important status of the included construction

The function in `src/erdos_straus.py` checks a *sufficient conditional construction* for a chosen prime p, shift h, and divisor w. It does not prove that suitable h and w exist for every prime. The example p=73 is a test case, not evidence of a general theorem.
