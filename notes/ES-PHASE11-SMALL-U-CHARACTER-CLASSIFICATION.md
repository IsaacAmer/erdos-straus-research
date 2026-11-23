# Phase 11 — A small-u square-class obstruction for Type-II character kernels

**Erdős–Straus Research Lab**  
**Date:** 23 November 2026  
**Status:** a proved four-case lemma and a derived specialization of Dahan's character count; novelty relative to the complete literature remains unverified.  
**Scope:** normalized Type-II parameter pairs
\[
1\le u\le4,\qquad a\ge1,\qquad \gcd(u,a)=1,\qquad a+u\equiv1\pmod2.
\]

## 1. The question and the relevant published theorems

For a fixed pair \((u,a)\), put
\[
m=4ua,\qquad G=(\mathbb Z/m\mathbb Z)^\times,
\qquad r=a+u\pmod m.
\]
Because \(a+u\) is odd and \(\gcd(a,u)=1\), the residue \(r\) is a unit and \(8\mid m\).

Dahan's Theorem 2.8(b) in arXiv:2611.08717 studies real quadratic characters modulo \(4ua\). For 3-smooth \(u\), with \(a+u\) odd and \(u,a>1\), it shows that the value of every such character on \(ap+u\) is independent of the prime \(p\equiv1\pmod{24}\):
\[
ap+u\equiv a+u\pmod{24a}.
\]
If \(\chi(a+u)=-1\), the prime-factor residue set of \(ap+u\) cannot be contained in \(\ker\chi\). The theorem also gives a count of the odd characters \(\chi(-1)=-1\) for which \(\chi(r)=-1\), depending on the square class of \(r\) relative to \(-1\). See Dahan, Theorem 2.8(b), especially the character-count statement and proof.

There are two admissible boundary pairs with \(a=1\), namely \((u,a)=(2,1)\) and \((4,1)\), which are outside the literal \(u,a>1\) hypothesis of Theorem 2.8(b). They are handled separately in Section 6.1; they are not silently included in the theorem's stated scope.

Dahan's Theorem 2.6 gives a separate cofactor-involution restriction when \(u\in\{1,2,3,6\}\). For our range this covers \(u=1,2,3\), but not \(u=4\). Parts (a,b) apply under the normalized and parity hypotheses; the stronger cycle decomposition and maximal-size count in part (c) additionally require \(r\equiv3\) or \(5\pmod8\). Remark 2.7 explicitly warns that its numerical bound concerns admissible subsets of exact size \(|G|/2\); a smaller admissible subset need not extend to one of that size. We preserve this limitation below.

**Attribution:** The character and dihedral theorems are Dahan's. This note derives a small-\(u\) square-class lemma and specializes the published character-count formula. It does not claim a new version of Dahan's theorems.

## 2. Main lemma: \(-r\) is never a square for \(u\le4\)

### Lemma 11.1

Let \(u\in\{1,2,3,4\}\), \(a\ge1\), \(\gcd(u,a)=1\), and \(a+u\) odd. Then
\[
\boxed{-(a+u)\notin\bigl((\mathbb Z/4ua\mathbb Z)^\times\bigr)^2.}
\tag{11.1}
\]

### Proof

Set \(m=4ua\). Since one of \(u,a\) is even, \(8\mid m\). Every odd square is \(1\pmod8\). Thus, if \(-r\) were a square modulo \(m\), then necessarily
\[
r=a+u\equiv7\pmod8.
\tag{11.2}
\]
We show that (11.2), together with the local quadratic-residue conditions at odd prime divisors of \(m\), is impossible in each of the four cases.

**Case \(u=1\).** Here \(a\) is even. From (11.2), \(a\equiv6\pmod8\), so \(a=2b\) with \(b\) odd and \(b\equiv3\pmod4\). For every odd prime \(q\mid a\), the condition that \(-r\) be a square modulo \(q\) becomes
\[
\left(\frac{-r}{q}\right)=\left(\frac{-1}{q}\right)=1,
\]
since \(r=a+1\equiv1\pmod q\). Hence every such \(q\equiv1\pmod4\), forcing \(b\equiv1\pmod4\), a contradiction.

**Case \(u=2\).** Here \(a\) is odd and (11.2) gives \(a\equiv5\pmod8\). For every prime \(q\mid a\), square-residuosity of \(-r\) modulo \(q\) gives
\[
\left(\frac{-2}{q}\right)=1,
\]
so \(q\equiv1\) or \(3\pmod8\). Every power of a residue in \(\{1,3\}\pmod8\), and every product of such powers, is again in \(\{1,3\}\pmod8\). Therefore \(a\equiv1\) or \(3\pmod8\), contradicting \(a\equiv5\pmod8\).

**Case \(u=3\).** Here \(a\) is even and \(3\nmid a\). Equation (11.2) gives \(a\equiv4\pmod8\), so \(v_2(a)=2\). Square-residuosity of \(-r\) modulo \(3\) requires
\[
-a\equiv1\pmod3,
\quad\text{hence}\quad a\equiv2\pmod3.
\]
For every odd prime \(q\mid a\), square-residuosity modulo \(q\) gives
\[
\left(\frac{-3}{q}\right)=1,
\]
which is equivalent to \(q\equiv1\pmod3\). Thus the odd part of \(a\) is \(1\pmod3\); because \(a=4b\) with \(b\equiv1\pmod3\), we obtain \(a\equiv1\pmod3\), a contradiction.

**Case \(u=4\).** Here \(a\) is odd and (11.2) gives \(a\equiv3\pmod8\). For every prime \(q\mid a\), square-residuosity of \(-r\) modulo \(q\) gives
\[
\left(\frac{-4}{q}\right)=\left(\frac{-1}{q}\right)=1,
\]
so every \(q\equiv1\pmod4\). Their product with multiplicity forces \(a\equiv1\pmod4\), contradicting \(a\equiv3\pmod4\).

All cases are impossible, proving (11.1). \(\square\)

## 3. Consequence for Dahan's odd-character count

Let
\[
X=\operatorname{Hom}(G,\{\pm1\}),
\qquad X^- = \{\chi\in X:\chi(-1)=-1\}.
\]
Since \(8\mid m\), the class of \(-1\) in \(G/G^2\) is nontrivial, and therefore
\[
|X^-|=\frac{|X|}{2}.
\]
The quotient \(G/G^2\) is an \(\mathbb F_2\)-vector space. A quadratic character is a linear functional on this vector space. Requiring \(\chi(-1)=-1\) and \(\chi(r)=-1\) imposes two affine linear conditions:

- If \(r\in G^2\), then \(\chi(r)=+1\) for every character, so there are **zero** odd characters with \(\chi(r)=-1\).
- If the classes of \(r\) and \(-1\) are linearly independent, exactly \(|X|/4\) characters satisfy both conditions. This is exactly half of \(X^-\).
- The remaining possibility in Dahan's three-case count is \([r]=[-1]\), equivalently \(-r\in G^2\). Lemma 11.1 rules this case out for every \(u\le4\).

Consequently, for all normalized small-\(u\) pairs,
\[
\boxed{
\#\{\chi\in X^-:\chi(r)=-1\}
=
\begin{cases}
0,&r\text{ is a square in }G,\\[2mm]
|X|/4,&r\text{ is not a square in }G.
\end{cases}}
\tag{11.3}
\]
If \(\omega(m_{\rm odd})\) denotes the number of distinct odd prime divisors of \(m=4ua\), then
\[
|X|=2^{2+\omega(m_{\rm odd})}.
\]
Thus, in the nonsquare case, exactly
\[
\boxed{2^{\omega(m_{\rm odd})}}
\]
odd characters trigger Dahan's multiplicativity obstruction. In particular, the third branch of the general character count—where every odd character has \(\chi(r)=-1\)—never occurs for the project's four small values of \(u\).

This is a **parameter-pair structural statement**. It is not a statement that a Type-II witness exists for a given prime: Dahan's theorem says that a prime-factor residue set cannot lie inside any of the corresponding obstructed kernels.

## 4. A finite square-class span certificate from the prime factors of \(ap+u\)

The character obstruction has a direct linear-algebra interpretation that can be checked on the actual prime factors.

Let \(p\equiv1\pmod{24}\) be prime, let \((u,a)\) satisfy Section 1, and put
\[
M=ap+u.
\]
Let \(T\subseteq G\) be the set of residue classes modulo \(m=4ua\) of the **distinct prime divisors** of \(M\), and let
\[
W=\operatorname{span}_{\mathbb F_2}\{[q]:q\mid M,\ q\text{ prime}\}\subseteq G/G^2.
\]
All these prime divisors are units modulo \(m\), because \(\gcd(ap+u,4ua)=1\) under the stated hypotheses.

### Corollary 11.2 (prime-factor square-class span)

If \(r=a+u\) is not a square modulo \(m\), then
\[
\boxed{[r]\in W\quad\text{or}\quad[-1]\in W.}
\tag{11.4}
\]
Equivalently, there is a nonempty subset \(S\) of the distinct prime divisors of \(ap+u\) such that the product
\[
D_S=\prod_{q\in S}q
\]
satisfies one of
\[
\boxed{D_S/r\text{ is a square unit modulo }4ua,\qquad
D_S/(-1)\text{ is a square unit modulo }4ua.}
\tag{11.5}
\]
Here division means multiplication by the modular inverse.

**Proof.** Since \(r\) is not a square and Lemma 11.1 says \(-r\) is not a square, the classes \([r]\) and \([-1]\) are nonzero and distinct in \(V=G/G^2\). Suppose neither belongs to \(W\). Their images in \(V/W\) are then both nonzero. In an \(\mathbb F_2\)-vector space, any two nonzero vectors admit a linear functional taking value \(1\) on both: if they coincide, assign value \(1\) to that vector; if they are independent, assign value \(1\) to each and extend a basis.

Pulling this functional back to \(V\) gives a quadratic character \(\chi\) with
\[
\chi(-1)=\chi(r)=-1,
\qquad \chi(q)=+1\quad(q\mid M).
\]
Thus \(T\subseteq\ker\chi\). This contradicts Dahan's Theorem 2.8(b) when \(u>1,a>1\), the separate conductor argument in Section 6 when \(u=1\), or the explicit unique-character arguments for \((u,a)=(2,1),(4,1)\) in Section 6.1. Hence at least one of \([r],[-1]\) lies in \(W\). Unpacking the definition of the span gives a subset of prime divisors whose product has the required square class. Since \([r]\ne0\) and \([-1]\ne0\), the subset is nonempty. The square-class group has dimension
\[
\dim_{\mathbb F_2}(G/G^2)=2+\omega(m_{\rm odd}),
\]
where \(\omega(m_{\rm odd})\) counts the distinct odd prime divisors of \(m=4ua\). A basis representation therefore yields
\[
\boxed{1\le |S|\le 2+\omega((4ua)_{\rm odd}).}
\]
This bounds the number of distinct prime factors selected in the certificate, not the total number of prime factors of \(ap+u\) or the modulator \(a\). \square

This corollary does **not** produce a Type-II divisor \(s\equiv-1\pmod{4ua}\). It gives a necessary multiplicative pattern among prime factors of \(ap+u\), modulo squares. It is a finite certificate that can be extracted by linear algebra over \(\mathbb F_2\), after factoring \(ap+u\).

The module `prime_factor_square_class_span_certificate` constructs such a certificate: it factors \(ap+u\), encodes each prime factor's class in \(G/G^2\), solves the span problem, and verifies the resulting quotient is a square modulo \(4ua\). It is intended as an audit tool for moderate inputs, not as a replacement for the faster Phase 8 witness search.

The reproducible examples are:

| \(p\) | \(u\) | \(a\) | \(ap+u\) factorization | target class | selected prime factors |
|---:|---:|---:|---|---|---|
| 73 | 1 | 2 | \(3\cdot7^2\) | \(-1\) | \(7\) |
| 193 | 1 | 2 | \(3^2\cdot43\) | \(r\) | \(3\) |
| 193 | 2 | 3 | \(7\cdot83\) | \(r\) | \(7,83\) |
| 2521 | 4 | 3 | \(7\cdot23\cdot47\) | \(-1\) | \(23\) |
| 10009 | 3 | 2 | \(20021\) | \(r\) | \(20021\) |
| 100057 | 2 | 3 | \(23\cdot31\cdot421\) | \(-1\) | \(23\) |
| 193 | 2 | 1 | \(3\cdot5\cdot13\) | \(r\) | \(3\) |
| 193 | 4 | 1 | \(197\) | \(r\) | \(197\) |

For each row, the program separately verifies that the chosen subproduct divided by the indicated target is a square unit modulo \(4ua\). The complete JSON certificates are saved in `results/PHASE11-SQUARE-CLASS-SPAN-EXAMPLES.json`.

## 5. Explicit square-class classification for \(r=a+u\)

Local square criteria modulo prime powers give the following exact table under the hypotheses of Section 1. In the table, \(q\) ranges over odd prime divisors of \(a\).

| \(u\) | Necessary and sufficient condition for \(r=a+u\) to be a square modulo \(4ua\) |
|---:|---|
| 1 | \(a\equiv0\pmod8\) |
| 2 | \(a\equiv7\pmod8\), and every \(q\mid a\) satisfies \(q\equiv\pm1\pmod8\) |
| 3 | \(a\equiv6\pmod8\), \(a\equiv1\pmod3\), and every \(q\mid a\) satisfies \(q\equiv\pm1\pmod{12}\) |
| 4 | \(a\equiv5\pmod8\) |

The proof is local: for \(2^e\) with \(e\ge3\), an odd unit is a square exactly when it is \(1\pmod8\); for each odd prime \(q\mid 4ua\), the unit must be a quadratic residue modulo \(q\). The Chinese remainder theorem combines these local conditions. The \(u=1,4\) rows have no additional odd-prime restriction because the corresponding residues are automatically squares modulo every odd \(q\mid a\).

Together with Lemma 11.1, this table completely identifies when the character filter in (11.3) is inactive (the square rows) and when exactly half of the odd characters are obstructed (all other admissible pairs).

## 6. The \(u=1\) extension of the multiplicativity argument

Dahan states Theorem 2.8(b) for \(u,a>1\). The project's \(u=1\) branch is not literally covered by that hypothesis. However, the same conductor argument extends to it as follows.

For \(u=1\), the hypotheses force \(a\) even. A real Dirichlet character modulo \(4a\) has primitive conductor whose 2-part divides \(8\) and whose odd part is squarefree and supported on the odd primes dividing \(a\). Hence its conductor divides
\[
8\operatorname{rad}(a_{\rm odd})\mid24a.
\]
For every prime \(p\equiv1\pmod{24}\),
\[
ap+1\equiv a+1\pmod{24a}.
\]
Therefore every such character satisfies
\[
\chi(ap+1)=\chi(a+1).
\]
If \(\chi(a+1)=-1\), the prime factors of \(ap+1\) cannot all lie in \(\ker\chi\), because complete multiplicativity would then give \(\chi(ap+1)=+1\). This gives the same kernel obstruction for \(u=1\), derived here rather than attributed to the literal hypotheses of Dahan's Theorem 2.8(b).

### 6.1 The two admissible boundary pairs with a=1

Under \(\gcd(u,a)=1\) and \(a+u\) odd, the only pairs with \(a=1\) and \(u\in\{1,2,3,4\}\) are \((u,a)=(2,1)\) and \((4,1)\).

- For \((u,a)=(2,1)\), we have \(r=3\pmod8\) and \(M=p+2\equiv3\pmod4\). The odd quadratic character \(\chi_4(n)=(-1)^{(n-1)/2}\) satisfies \(\chi_4(-1)=-1\), \(\chi_4(r)=-1\), and \(\chi_4(M)=-1\). Complete multiplicativity therefore forces at least one prime factor of \(M\) outside \(\ker\chi_4\). This is also the special obstruction in Dahan's Theorem 2.8(a).
- For \((u,a)=(4,1)\), we have \(r=5\pmod{16}\) and \(M=p+4\equiv5\pmod8\). The primitive odd character \(\chi_{-8}(n)=\left(\frac{-8}{n}\right)\) modulo 8 satisfies \(\chi_{-8}(-1)=-1\), \(\chi_{-8}(r)=-1\), and \(\chi_{-8}(M)=-1\). Thus the prime factors of \(M\) cannot all lie in its kernel.

For each of these two moduli, \(G/G^2\) has dimension 2, and the classes of \(r\) and \(-1\) are independent (also guaranteed by Lemma 11.1). Hence exactly one odd character has \(\chi(r)=-1\); it is the character just exhibited. Consequently the linear-algebra argument in Corollary 11.2 applies to both boundary pairs as well.

The code records these as explicit boundary-character arguments, not as applications of Theorem 2.8(b).

## 7. How the result combines with Dahan's cofactor dihedral rigidity

For \(u=1,2,3\), Dahan's Theorem 2.6(a,b) applies to every admissible pair \((u,a)\): if no divisor \(s\equiv-1\pmod{4ua}\) exists, the prime-factor residue set \(T_{u,a}(p)\) avoids \(-1\) and \(-r\), and meets each relevant involution orbit at most once.

The stronger cycle decomposition in Theorem 2.6(c) additionally requires
\[
r=a+u\equiv3\text{ or }5\pmod8.
\]
For those pairs, the group splits into even cycles of length \(2L\), where \(L=\operatorname{ord}_{4ua}(r)\), and Dahan obtains
\[
N_{\max}(u,a)\le2^{\frac{\varphi(4ua)}{2L}-1}.
\]
This counts only admissible subsets of exact cardinality \(|G|/2\). As Dahan's Remark 2.7 emphasizes, it does not bound all smaller admissible subsets. We do not use it as a count of every possible failure set.

The new small-\(u\) lemma adds a separate fact: in all four branches, the quadratic-character case \([r]=[-1]\) is absent. Thus:

- for \(u=1,2,3\), the character obstruction can be combined with Theorem 2.6(a,b), and with its cycle bound when \(r\equiv3,5\pmod8\);
- for \(u=4\), Dahan's Theorem 2.6 does not apply, but the character classification and Theorem 2.8(a,b) still do;
- none of these structural restrictions alone proves the existence of a witness.

## 8. Finite parameter-box audit through \(a=10{,}000\)

The program enumerated every pair
\[
2\le a\le10{,}000,\quad 1\le u\le4,
\quad\gcd(u,a)=1,\quad a+u\text{ odd}.
\]
These are counts of **parameter pairs**, not counts of primes, witnesses, or counterexamples.

| \(u\) | Valid pairs | \(r\) square | Character obstruction active | Theorem 2.6(a,b) scope | Theorem 2.6(c) cycle-bound scope | Both character + cycle | Neither of those two filters |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5,000 | 1,250 | 3,750 | 5,000 | 2,500 | 2,500 | 1,250 |
| 2 | 4,999 | 466 | 4,533 | 4,999 | 2,499 | 2,499 | 466 |
| 3 | 3,334 | 229 | 3,105 | 3,334 | 1,668 | 1,668 | 229 |
| 4 | 4,999 | 1,250 | 3,749 | 0 | 0 | 0 | 1,250 |

The program also found zero cases with \(-r\) square, as required by Lemma 11.1. This is an implementation check over a finite box; the proof of Lemma 11.1 is the universal argument.

The exact data are saved in `results/PHASE11-CHARACTER-CLASSIFICATION-10000.json`.

## 9. Tests and reproducibility

The Phase 11 tests check:

1. Local square tests against brute-force squares for all admissible pairs with \(a\le120\).
2. The explicit square-class table against local criteria for all admissible pairs with \(a\le2000\).
3. The impossibility of \(-r\) being a square for all admissible pairs with \(a\le5000\).
4. The odd-character count against an independent \(\mathbb F_2\)-linear-algebra enumeration for every admissible pair with \(a\le100\).
5. The correct scope of Dahan Theorems 2.6 and 2.8 and the separate \(u=1\) extension.
6. The exact parameter-box counts through \(a=10{,}000\).
7. Rejection of invalid parameter pairs.
8. Exact square-class span certificates on eight concrete (p,u,a) inputs, including direct verification that the selected subproduct divided by the target class is a square modulo \(4ua\).

The combined Phase 10 + Phase 11 suite contains 17 tests (7 in Phase 10 and 10 in Phase 11). Phase 10 independently audits the six Jacobi laws from Dahan's Theorem 2.4 on the 246 witnesses produced for nine sample primes; Phase 11 verifies the small-\(u\) square-class classification above.

From the repository root, after adding the package:

```powershell
python -m unittest discover -s tests -p "test_phase10_jacobi_audit.py" -v
python -m unittest discover -s tests -p "test_phase11_small_u_character_profile.py" -v
python -m unittest discover -s tests -v
python src/phase10_demo.py
python src/phase11_demo.py --limit 10000
python src/phase11_span_demo.py
```

## 10. Research status and limitations

**Proved in this note:**

- Lemma 11.1: \(-r\) is never a square modulo \(4ua\) for normalized, odd-parity pairs with \(u\le4\).
- Corollary 11.2: when \(r\) is not a square, the square classes of \(r\) or \(-1\) occur in the \(\mathbb F_2\)-span of the distinct prime-factor classes of \(ap+u\).
- The explicit square-class table for \(r=a+u\).
- The derived reduction of Dahan's three-way odd-character count to two cases (zero or exactly half of odd characters) for the four small-\(u\) branches.
- The elementary extension of the multiplicativity-conductor argument to the \(u=1\) branch.

**Known from Dahan, not newly proved here:**

- Theorem 2.4 global Jacobi reciprocity.
- Theorem 2.6 cofactor dihedral restrictions.
- Theorem 2.8 quadratic-kernel multiplicativity obstruction and general character-count framework.

**Not proved:**

- that every prime \(p\equiv1\pmod{24}\) has a Type-II witness with \(u\le4\);
- that the character and dihedral constraints force one of the four branches to succeed;
- that all possible failure residue sets have been classified;
- that Lemma 11.1 or the derived corollary is absent from every prior source. The statement is a project-specific four-case specialization of the published general character framework; a full novelty/priority audit is still required before publication claims.

## 11. References

1. Benjamin Dahan, *Composite witness sieves, Kneser–Plancherel containers, and the exponent 5/7 for the Erdős–Straus conjecture*, arXiv:2611.08717 (2026), Theorem 2.4 (global Jacobi reciprocity), Theorem 2.6 (cofactor dihedral rigidity), Theorem 2.8 (quadratic-kernel multiplicativity obstruction), and Remark 2.7 (scope of the maximal dihedral count): https://arxiv.org/abs/2611.08717
2. Benjamin Dahan, *Sieve dimension and search depth for the Erdős–Straus conjecture, \(n\equiv1\pmod{24}\)*, arXiv:2608.24035 (2026): https://arxiv.org/abs/2608.24035
