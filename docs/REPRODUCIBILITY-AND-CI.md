# Reproducibility and continuous integration

## Why this matters

A test count is useful only when a reader can reproduce it against an exact source snapshot and interpreter. The supplied logs report 119 passing tests after Phase 14, but they also contain different interpreter references: Python 3.13.5 in the Phase 14 environment note and `C:\Python315` in an earlier traceback. This may reflect separate runs; do not merge them into one environment claim.

## Canonical local audit (Windows PowerShell)

Run from the repository root. Use the virtual-environment interpreter explicitly rather than relying only on the `(.venv)` prompt:

```powershell
$python = ".\.venv\Scripts\python.exe"

Write-Host "=== interpreter ==="
& $python --version
& $python -c "import sys, platform; print(sys.executable); print(platform.platform())"

Write-Host "=== source snapshot ==="
git rev-parse HEAD
git status --short

Write-Host "=== full test suite ==="
& $python -m unittest discover -s tests -v
```

Save the entire terminal output to a dated file under `results/`, and state the exact command and commit hash. If you intentionally use a different interpreter, record it as a separate run.

## GitHub Actions workflow

The supplied `.github/workflows/tests.yml` runs the unit suite on clean Ubuntu and Windows hosted runners using Python 3.11 and 3.13 (four matrix jobs). Merge it, push it, and wait for the first run to complete. A green CI run is independent evidence that the tests work on those runners; it still does not validate the analytic proof or establish a universal theorem.

## Required metadata for every benchmark

- commit hash;
- Python version and `sys.executable`;
- operating system and machine details;
- exact command-line arguments;
- number of repeats and timing aggregation method;
- input values and primality/residue conditions;
- exact witness-set equality check;
- output file path and checksum.

## Phase 9 wording

The recorded run for `p=1,000,000,009` reports Phase 7 = 9.126452 s and Phase 8 = 0.080084 s, a ratio of 113.96×, with equal witness sets. Present this as one measured local benchmark (three repeats in the supplied command), not as a general speedup claim. Report the machine and timing method from the source output before publishing the figure.
