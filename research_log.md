# Research log

## 2026-11-22 — Workspace initialized

- Project: Erdős–Straus conjecture.
- Conjecture: for each integer n >= 2, positive integers a,b,c exist with 4/n = 1/a + 1/b + 1/c.
- Important audit note: a previously reported count of 2,384 primes through 100,000 was not accompanied by a reproducible script/output in the conversation; classify it as **unverified** until independently rerun.
- The conditional divisor construction for a chosen (p,h,w) is encoded in `src/erdos_straus.py` and tested on p=73, h=7, w=10.
- Next task: audit the literature and independently verify all reductions before treating any residue-class statement as a starting theorem.
