# Phase 10 — Independent Jacobi audit of the project's Type-II witnesses

**Erdős–Straus Research Lab · 23 November 2026**  
**Status:** independent implementation and finite audit of a published theorem; no new Jacobi reciprocity law is claimed.

## 1. Published result being checked

Benjamin Dahan's arXiv preprint *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture* (arXiv:2611.08717v1, 5 November 2026), Theorem 2.4, establishes six Jacobi-symbol identities on the Type-II variety. For a prime \(p\equiv1\pmod4\), and a Type-II witness in the normal form used in the proof, the identities are

\[
\left(\frac{\alpha}{s}\right)=1,
\qquad
\left(\frac{ua}{s}\right)=1,
\]

and

\[
\left(\frac{s}{p}\right)=
\left(\frac{p}{s}\right)=-1,
\qquad
\left(\frac{uv}{p}\right)=-1,
\qquad
\left(\frac{\alpha c}{p}\right)=-1.
\]

These are Dahan's identities, not discoveries of this repository. The theorem and its proof appear in Section 2.2 of the cited preprint.

## 2. Exact identification of the project's variables

Phase 8 returns a witness \((u,a,s,v,e,k)\) satisfying the four exact integer identities

\[
ap+u=sv,
\qquad s+1=4uak,
\]

\[
u+v=ae,
\qquad p+e=4ukv.
\]

Dahan's Type-II normal form in the proof of Theorem 2.4 is

\[
ap=4a\alpha uv-u-v,
\qquad s=4ua\alpha-1,
\qquad c=\frac{u+v}{a},
\]

so that \(p+c=4\alpha uv\). From the Phase 8 identities,

\[
ap=sv-u=(4uak-1)v-u=4auk v-u-v,
\]

and \(c=(u+v)/a=e\). Therefore the exact coordinate map is

\[
\boxed{\alpha=k,\qquad c=e,}
\]

with \(u,a,s,v\) unchanged. This establishes the correspondence algebraically, rather than relying on a superficial similarity of notation.

## 3. What the audit code checks

`src/phase10_jacobi_audit.py` implements the Jacobi symbol by the Euclidean reciprocity algorithm using only Python's standard library. For every supplied Phase 8 witness, it first rechecks

\[
ap+u=sv,\quad s+1=4uak,\quad u+v=ae,
\quad p+e=4ukv,
\]

and \(\gcd(u,a)=1\). It then evaluates all six published Jacobi identities under the mapping \(\alpha=k,c=e\).

The checker verifies that \(p\) is prime and \(p\equiv1\pmod{24}\), and that \(s\) is odd before evaluating Jacobi symbols. A corrupted witness is deliberately included in the tests to ensure that the audit rejects it.

## 4. Reproducible finite audit

The audit covers nine primes, each congruent to 1 modulo 24, with all four values \(u=1,2,3,4\). The witness counts are:

| \(p\) | Witnesses across \(u=1,2,3,4\) |
|---:|---:|
| 193 | 2 |
| 2,521 | 3 |
| 66,529 | 1 |
| 10,009 | 24 |
| 100,057 | 24 |
| 1,000,033 | 33 |
| 10,000,537 | 42 |
| 100,000,081 | 49 |
| 1,000,000,009 | 68 |
| **Total** | **246** |

Result: **246/246 witness records passed all six Jacobi identities and the four integer-identity checks; zero failures.** The complete record is saved in `results/PHASE10-JACOBI-AUDIT.json`.

This is a consistency audit of the program's outputs on nine primes. It neither proves that a witness exists for every prime nor proves the project's proposed restriction \(u\le4\).

## 5. Tests and reproduction

The seven tests in `tests/test_phase10_jacobi_audit.py` cover reference Jacobi values, quadratic reciprocity, invalid denominators, two known witnesses for \(p=73\), all 246 sample witnesses, rejection of invalid prime inputs, and detection of a corrupted witness.

From the repository root:

```powershell
python -m unittest discover -s tests -p "test_phase10_jacobi_audit.py" -v
python src/phase10_demo.py
```

## 6. Research status

- **Published by Dahan:** Theorem 2.4 and all six Jacobi identities.
- **Implemented here:** an exact independent Jacobi-symbol routine and an audit of the project's Type-II witness records against those identities.
- **Verified in the finite sample:** all 246 witness records passed.
- **Not established:** a universal witness for every \(p\equiv1\pmod{24}\), or the conjecture that a witness always exists with \(u\le4\).
- **Novelty:** no priority claim is made for the reciprocity laws. The project contribution in this phase is a reproducible software audit.

## Reference

Benjamin Dahan, *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture*, arXiv:2611.08717v1 (5 November 2026), Theorem 2.4, Section 2.2: https://arxiv.org/abs/2611.08717
