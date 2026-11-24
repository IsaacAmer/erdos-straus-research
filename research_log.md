# Research log

## 2026-11-22 — Workspace initialized

- Project: Erdős–Straus conjecture.
- Conjecture: for each integer n >= 2, positive integers a,b,c exist with 4/n = 1/a + 1/b + 1/c.
- Important audit note: a previously reported count of 2,384 primes through 100,000 was not accompanied by a reproducible script/output in the conversation; classify it as **unverified** until independently rerun.
- The conditional divisor construction for a chosen (p,h,w) is encoded in `src/erdos_straus.py` and tested on p=73, h=7, w=10.
- Next task: audit the literature and independently verify all reductions before treating any residue-class statement as a starting theorem.

## 2026-11-24 — Phase 14 layer-cake correction and verification

- **Base commit:** `cf602b54b285043a387d27602edc70d55201772a`
- **Working-tree status at verification:** Phase 14 note and program metadata modified but not committed; release-kit files from the prior package also remained untracked.
- **Environment reported by maintainer:** Python 3.15.2, Windows 11 build 26200, repository `.venv` interpreter.

### Mathematical/documentation changes

- Replaced the earlier tie-count argument in Section 8 of `notes/ES-PHASE14-TOTIENT-SUBLEVEL-DENSITY.md` with a layer-cake lower bound and a matching upper bound for the sum of the `P` least costs.
- The corrected variational statement is

  `min_{|S|=P} sum_{(u,a) in S} (phi(4ua)-2) ~ P^2/A_infinity`,

  for distinct admissible pairs with `1 <= u <= 4`. Consequently, under mean cost at most `tau L`, `P <= (tau A_infinity + o(1)) L`.
- Added Section 9 comparing Phase 14's cost-sublevel family with Phase 12's rectangular four-slice family. The comparison is between pair-count coefficients under the same mean-cost budget:

  `S_rect = 361*pi^2/1728 ~= 2.061879160181`,
  `A_infinity ~= 2.151838912194`,
  `A_infinity/S_rect ~= 1.043629982664`.

  This is a 4.363% increase in the pair-count coefficient within the restricted `u <= 4` family-size problem. It is not a 4.363% improvement to the original Erdős–Straus exceptional-set bound. The two example Phase 12/14 exponent constants use different parameter choices and must not be compared directly.
- Corrected `theorem_bound` metadata in `src/phase14_totient_sublevel.py` to describe a Big-O bound instead of a literal inequality with implicit constant 1. The search algorithm and its numerical computation were not changed.

### Verification reported

- Phase 14 suite: 11 tests passed in 0.341 s.
- Full suite: 119 tests passed in 2.575 s.
- Phase 14 program completed with `A_infinity = 2.151838912194`, `kappa = 0.013993650132`, `kappa-limit = 0.014009367918`, and 99.887805% of the limiting coefficient.
- Finite implementation audits used surrogate `L` values 100, 250, 500, and 1000. These are not searches over primes up to corresponding `N` values.
- `git diff --check` returned no whitespace errors. Git emitted only line-ending conversion warnings (LF to CRLF) for the two modified files.

### Scope and limitations

- The 119-test result applies to the tested working tree based on `cf602b5` plus the two uncommitted Phase 14 edits; it is not evidence that commit `cf602b5` alone contains those edits.
- The analytic argument still depends on the hypotheses and conclusions of Dahan's Theorem 4.6. Passing software tests does not prove the Wiener–Ikehara asymptotic or independently verify Dahan's theorem.
- The density estimate controls the restricted exceptional set `E_4(N)` only. It does not prove `E_4(N)` is empty, does not prove the original conjecture, and does not improve the cited bound for the full exceptional set.
- Priority for the specific fixed-`u` application is not established. General totient-value distribution predates this project (Bateman, 1972), and a related Euler-product constant appears in Dahan's earlier preprint in a different context.

### Next action

1. Preserve the Phase 14 machine-readable audit under `results/`.
2. Verify that local-only JSON outputs are ignored by Git.
3. Audit each untracked release-kit file before deciding whether to include it.
4. Complete the release preflight and perform a final test run.
5. Commit only the reviewed files; do not use `git add .`.

The public README and research-log update have now been applied locally and remain uncommitted.


### 2026-11-24 ? Documentation Polish, Arabic Docs Organization, and Release Freeze Prep (`cc02edb`)
- Organized Arabic phase README files under `docs/ar/` with an index (`docs/ar/README.md`) while preserving Git history.
- Standardized LaTeX math delimiters in `README.md` (`$` and `$$`), added the GitHub Actions CI badge, and added a `Quick Start` section.
- Synchronized project verification records to commit `cc02edb` (119 local tests passing in 2.715 s on Windows 11 / Python 3.15.2; 4 GitHub Actions jobs passing).
- Explicitly documented that Phase 13 is not an integrated or tested module in the current repository inventory, and any historical work related to it remains unresolved.
