# Project status and claim register

**Evidence cut-off:** 24 November 2026.
**Repository:** `IsaacAmer/erdos-straus-research`
**Git base for the latest verified working tree:** `cf602b54b285043a387d27602edc70d55201772a` (the Phase 14 and documentation revisions were local changes at verification time).
**Important:** This register is based on the user's command logs and the notes previously supplied. It is not an independent line-by-line code audit.

## Executive status

The project is a substantial, reproducible computational research workbench with a provisional analytic corollary. The strongest defensible public description is:

> An independent computational investigation of Type-II divisor witnesses for the Erdős–Straus conjecture, with exact-arithmetic verification, finite character audits, performance comparisons, and a restricted density calculation derived from an existing sieve theorem.

Do not describe it as a proof of the conjecture, as a new theorem of established priority, or as a peer-reviewed publication.

## Claim register

| Component | What the supplied record supports | What it does not support | Public status |
|---|---|---|---|
| Erdős–Straus conjecture | Correct problem statement and known reductions are documented | A proof for all integers or all primes | Open problem; project does not solve it |
| Type-I/Type-II criteria and conversions | Implemented conversions and regression tests for selected examples | Original discovery of the cited criteria | Literature-based implementation/cross-check |
| Phase 6 certificates | Tests report certificates for a fixed set of 14 literature/boundary primes; parameter-box sharpness within that finite set | A theorem for all primes | Finite certificate collection |
| Phase 7 quotient prefilter | Tests compare fast quotient enumeration with a full scan and reproduce selected boundary cases | Universal coverage of all primes | Exact finite algorithmic check |
| Phase 8 small-factor search | Tests report equality of witness sets with Phase 7 on 76 primes through 5000, 14 literature primes, and selected boundary primes | Global algorithmic equivalence or universal speedup | Reproducible finite cross-validation |
| Phase 9 scaling | Recorded benchmark at p=1,000,000,009: Phase 7 about 9.126452 s; Phase 8 about 0.080084 s; reported ratio 113.96×; equal witness sets | 113.96× on all machines, all inputs, or all workloads | One local benchmark; hardware/environment specific |
| Phase 10 Jacobi audit | 246/246 tested witnesses satisfy the cited Jacobi laws in the supplied finite run | New Jacobi laws or a universal proof | Finite verification of literature-derived identities |
| Phase 11 character profile | Finite profile run with `--limit 10000`, local square-class checks, and explicit certificates | A global classification for all primes | Finite classification/audit |
| Phase 12 density optimization | Tests for cutoff order, exact coefficient formula, and comparison with a rectangular family | A globally optimal sieve method | Optimization inside a specified family/budget |
| Phase 13 | No standalone `test_phase13_*.py` appears in the supplied 119-test transcript | That Phase 13 does not exist, or that it is complete | Status unclear; document it as exploratory/superseded unless a separate module and proof are recovered |
| Phase 14 totient sublevel | 11 dedicated tests; reported constants `A_inf≈2.151838912194`, `kappa≈0.013993650132`, limiting value `≈0.014009367918`; derived using Dahan Theorem 4.6 | Emptiness of the restricted exceptional set; proof of the original conjecture; established novelty | Provisional derived density corollary; mathematical review still required |

## Phase 14 precise scope

The restricted set studied is

\[
\mathcal E_4(N)=\{p\le N: p\text{ prime},\ p\equiv1\pmod{24},\
\text{and no Type-II witness exists for any }1\le u\le4\text{ and admissible }a\}.
\]

The reported bound is of the form

\[
|\mathcal E_4(N)|\ll N\exp\left(- (\kappa+o(1))(\log\log N)^2\right).
\]

This bounds a restricted-parameter obstruction. It does not say `E_4(N)` is empty. It must not be presented as a stronger bound for the original Erdős–Straus exceptional set. The parameter family and Dahan theorem are existing-framework ingredients; the fixed-`u` totient constants and selected-family application are the project's candidate derived contribution, with priority unestablished.

## Phase 14 mathematical correction status

The earlier tie-count inference was not justified by `F(x)=cx+o(x)` alone. The corrected layer-cake lower- and upper-bound argument is now integrated into Section 8 of the main Phase 14 note, equations (14.19)-(14.23). The separate erratum is retained as an audit record. Software tests do not prove the analytic asymptotic or Dahan's theorem.

## Reproducibility record

The supplied logs record:

- Phase 14 dedicated tests: 11 passed.
- Full test suite after Phase 14: 119 passed in 2.575 s, on the reported Windows 11 / Python 3.15.2 environment.
- Phase 10 finite audit: 246/246 passed.
- Phase 9 local benchmark includes an input at p=1,000,000,009 with the timings above.

The logs also contain different Python interpreter references (a Phase 14 environment note says Python 3.13.5; an earlier traceback references `C:\Python315`). This may reflect separate environments, but it must be clarified. Each published run should record `python --version`, `sys.executable`, OS, commit hash, command, and output.

## Known maintenance issues from the supplied record

1. Local-only JSON outputs are now covered by the `.gitignore` rule `results/*-LOCAL.json`. Verify that no local output is staged before release.
2. Run both `git diff --check` and `git diff --cached --check` immediately before the final commit.
3. The main README and research log have now been updated locally. The README is the canonical public overview; the older `README-FINAL-DRAFT.md` should not replace it.
4. Phase 13 has no corresponding standalone test in the reported full suite; recover and classify it, or document it as a non-integrated exploratory branch.
5. No `LICENSE` was shown in the repository tree previously supplied. Decide the reuse policy before an archival release.
6. The current `CITATION.cff` uses the public alias `IsaacAmer`. That is a privacy-preserving choice; verify the generated citation after release metadata is finalized.

## Safe claims for public use

- “119 unit tests passed in the recorded local environment at the documented commit.”
- “A finite audit checked 246 generated witnesses against published Jacobi-symbol identities.”
- “A local benchmark reported a 113.96× speed ratio on one specified input and machine.”
- “The Phase 14 note derives a restricted density corollary from an existing sieve theorem; novelty and priority are not established.”

Avoid: “proved Erdős–Straus,” “solved Type II for all primes,” “new theorem” (without qualification), “published paper,” or a claim that the entire codebase has been independently audited.


## Documentation & Verification Snapshot (Commit `cc02edb`)

- **Reference commit:** `cc02edb` on `main`
- **Local verification environment:** Windows 11, Python 3.15.2 (`.venv`)
- **Local test suite:** 119 tests passed in 2.715 s (run on the working tree that became `cc02edb`)
- **CI status (GitHub Actions):** 4 workflow jobs passing on `cc02edb`
- **Phase 13 status:** Phase 13 is not an integrated or tested module in the current release (`v0.1.0`), and the status of any historical work related to it remains unresolved.
