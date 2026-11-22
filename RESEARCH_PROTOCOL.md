# Research protocol

## Phase 0 — Audit the starting point

1. State the conjecture and all quantifiers exactly.
2. Build a bibliography from original papers and reliable mathematical references.
3. Verify every claimed reduction (prime reduction, congruence classes, divisor criteria) independently.
4. Recreate any prior computational claim from source code. If no code/output exists, mark it unverified.

## Phase 1 — Reproducible baseline

1. Implement an exact verifier for a proposed triple (n,a,b,c).
2. Implement a transparent search routine for a finite interval.
3. Save every witness and every unresolved case, not only aggregate counts.
4. Cross-check a sample with a second implementation (for example, Mathematica/Wolfram).

## Phase 2 — Mathematical reduction

1. List each known identity with exact domain and positivity conditions.
2. For each residue class, prove coverage or record the unresolved subcase.
3. Translate any divisor criterion into a precise iff/implication statement.
4. Test the boundary of every lemma with exact computation, then prove it symbolically.

## Phase 3 — Novel work

For each proposed new lemma:

1. Write the statement before trying to prove it.
2. Search literature for equivalent or stronger results.
3. Attack it with small cases and structured counterexample search.
4. Prove it on paper.
5. Independently reconstruct the proof without relying on the original derivation.
6. Formalize the stable statement in Lean if useful.

## Phase 4 — Deliverables

A result counts as a research deliverable only if it has:

- an exact theorem statement;
- a complete proof or clearly scoped computational certificate;
- a list of dependencies;
- an independent check;
- a statement of what remains unresolved;
- files and commands sufficient for reproduction.

## Stop/go rule

Do not increase computation simply because the previous run succeeded. First ask whether the next run can distinguish between competing mathematical hypotheses or discover a counterexample to a proposed lemma.
