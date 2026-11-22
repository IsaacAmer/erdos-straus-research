# ES-PHASE2 — Corrected exact parameter dictionary: Rosati, Dahan, Pomerance–Weingartner

**Date:** 22 November 2026  
**Status:** A proved algebraic translation of known criteria, supported by exact-arithmetic regression tests. It is **not** a proof of the Erdős–Straus conjecture and is not claimed as a new criterion.

## 1. Why this correction matters

The previous bridge draft attributed a Type-I criterion to Dahan Theorem 3.14. That attribution was wrong. In Dahan's v2 paper:

- Theorem 2.6 and Corollary 2.7 give the fixed-shift criterion, with untwisted and twisted branches.
- Theorem 3.9 and Lemma 3.10 give a two-parameter **Type-II** witness criterion.
- Theorem 3.14 proves correctness and gives the operation count for Algorithm 2; it is not a Type-I criterion.

The Type-I half of the current dictionary is instead sourced directly to Rosati's Type-I equation and Pomerance–Weingartner Corollary 2.2. Its normalized witness form is derived below. This exact distinction is preserved in the code and tests.

## 2. Primary-source statements

### 2.1 Rosati, in normalized form as printed by Salez

For prime `p`, the fraction `4/p` is a sum of three positive unit fractions if and only if at least one of these systems has positive integer solutions:

**Rosati Type II**

\[
4ABCD=A+B+pC,\qquad \gcd(ABD,p)=1.
\tag{R-II}
\]

**Rosati Type I**

\[
4ABCD=p(A+B)+C,\qquad \gcd(ABCD,p)=1.
\tag{R-I}
\]

Salez Proposition 1 explicitly attributes these formulae to Rosati and prints both conditions. Rosati's 1954 original separates the two cases according to whether the prime divides exactly two or exactly one of the three denominators.

### 2.2 Dahan, Type II

For prime `p`, Dahan Theorem 3.9 characterizes a Type-II solution by positive integers `u,a` and a divisor `s | ap+u` such that

\[
s\equiv -1\pmod{4ua}.
\tag{D-II}
\]

The explicit reconstruction uses

\[
v=\frac{ap+u}{s},\qquad c=\frac{u+v}{a},\qquad
\alpha=\frac{p+c}{4uv}.
\]

Dahan Lemma 3.10 shows that we may normalize `gcd(u,a)=1` without losing a witness.

### 2.3 Pomerance–Weingartner

For `m=4` and prime `p`, their Corollary 2.2 characterizes Type I by

\[
f\mid 4A^2d+1,\qquad 4Ad\mid p+f.
\tag{PW-I}
\]

Their Corollary 2.4 characterizes Type II by

\[
e\mid A+B,\qquad 4AB\mid p+e.
\tag{PW-II}
\]

These are if-and-only-if criteria, not just sufficient conditions.

## 3. Main dictionary theorem

Let `p` be prime with `p ≡ 1 (mod 4)`. The following parameter systems are exactly interconvertible, with the transformations implemented in `src/parameter_dictionary.py` and `src/rosati_dahan_bridge.py`.

### 3.1 Type II: Rosati ↔ Dahan Theorem 3.9 ↔ P&W Corollary 2.4

Start with a normalized Dahan witness

\[
\gcd(u,a)=1,\qquad s\mid ap+u,\qquad s\equiv-1\pmod{4ua}.
\]

Set

\[
v=\frac{ap+u}{s},\qquad \alpha=\frac{s+1}{4ua}.
\]

Then

\[
4u v a\alpha=v(s+1)=ap+u+v,
\]

so the Rosati Type-II tuple is

\[
(A,B,C,D)=(u,v,a,\alpha).
\]

Now put

\[
e=\frac{u+v}{a}.
\]

Dahan's reconstruction guarantees this is an integer, and

\[
p+e=\frac{ap+u+v}{a}
=\frac{v(s+1)}a=4uv\alpha.
\]

Thus the P&W Type-II data are `(A_PW,B_PW,e)=(u,v,e)`, satisfying (PW-II).

**Reverse from Rosati Type II.** Suppose (R-II) holds. Put `g=gcd(A,C)`. Reducing (R-II) modulo `g` shows `g|B`; since `p∤A`, we also have `p∤g`. Define

\[
u=A/g,\quad a=C/g,\quad v=B/g,\quad \alpha=Dg^2.
\]

Then

\[
4uav\alpha=u+v+pa.
\]

Set `s=4uaα−1`. It follows that

\[
s v=ap+u,\qquad s\equiv-1\pmod{4ua},
\]

which is the normalized Dahan Type-II witness. The P&W Type-II parameters then follow from `e=(u+v)/a`.

**Reverse from P&W Type II.** Suppose (PW-II) holds. Put

\[
a_0=(A+B)/e,\qquad \alpha=(p+e)/(4AB),\qquad s=4Aa_0\alpha-1.
\]

Then

\[
sB=a_0p+A.
\]

Let `g=gcd(A,a0)`, and set `u=A/g`, `a=a0/g`. Since `s≡−1 mod 4Aa0`, `gcd(s,g)=1`; consequently `s` still divides `ap+u` after dividing by `g`, and `s≡−1 mod 4ua`. This is Dahan's normalized witness.

### 3.2 Type I: Rosati ↔ normalized witness ↔ P&W Corollary 2.2

The normalized witness is

\[
\gcd(u,a)=1,\quad 0<u<p,\quad s\mid ap+u,
\quad s\equiv-p\pmod{4ua}.
\tag{W-I}
\]

**From the witness to P&W Type I.** Set

\[
\alpha=\frac{s+p}{4ua},\qquad v=\frac{ap+u}{s}.
\]

The P&W Type-I variables are `(A,d,f)=(a,α,s)`. The congruence gives `4aα | p+s`. Also

\[
u(4a^2\alpha+1)=a(p+s)+u\equiv ap+u\equiv0\pmod{s}.
\]

Since `gcd(s,u)=1` (because `s≡−p mod u` and `0<u<p`), we obtain `s | 4a²α+1`. Thus (PW-I) holds.

The Rosati Type-I tuple is

\[
(A,B,C,D)=(a,v,u,\alpha).
\]

Indeed,

\[
4au\alpha v=v(s+p)=ap+u+pv=p(a+v)+u.
\]

The coprimality condition in (R-I) follows from the witness conditions and `p` prime.

**From Rosati Type I to the normalized witness.** Suppose (R-I) holds. Let `g=gcd(A,C)`. Reducing the equation modulo `g` shows `g|B`; since `p∤A`, `p∤g`. Define

\[
a=A/g,\quad u=C/g,\quad v=B/g,\quad \alpha=Dg^2.
\]

Then

\[
4au\alpha v=p(a+v)+u.
\]

With `s=4auα−p`, this becomes

\[
s v=ap+u,
\quad s\equiv-p\pmod{4ua}.
\]

The original coprimality gives `gcd(a,u)=1`, and `u<p`: if `u≥p`, then

\[
s-(ap+u)=4au\alpha-p-ap-u
\ge u(4a-1)-p(a+1)
\ge p(3a-2)>0,
\]

contradicting `s|ap+u` with positive `s`. Thus (W-I) holds.

**P&W Type I ↔ normalized witness.** Given (PW-I), set

\[
U=\frac{p+f}{4Ad},\quad g=\gcd(A,U),\quad
 a=A/g,\quad u=U/g,\quad \alpha=dg^2,\quad s=f.
\]

Then `s+p=4uaα`. From `f | 4A²d+1` and

\[
U(4A^2d+1)=A(p+f)+U,
\]

we get `f | Ap+U`. Also `gcd(f,g)=1`, because any common prime divisor of `f,g` would divide both `A` and `4A²d+1`, an impossibility. Dividing by `g` gives `s|ap+u`. The same comparison as above gives `u<p`. Conversely, the witness-to-P&W calculation already proved (PW-I).

## 4. Exact status of the relationship to Dahan's fixed-shift Type I

Dahan Theorem 2.6 / Corollary 2.7 gives a fixed-shift criterion. Its untwisted branch corresponds to Type II, while its twisted branch corresponds to Type I. The normalized Type-I witness above is directly sourced through Rosati and P&W Corollary 2.2. It must not be relabeled as Dahan Theorem 3.14.

Dahan Proposition 2.5 gives, for a **smallest denominator** `x` in an ordered solution, `p/4 < x ≤ 3p/4`; hence a shift `c=4x−p` satisfies `0<c≤2p`. If we specifically select the smaller non-p-divisible denominator in the Type-I Rosati arrangement, we still need to check the ordering and this shift bound before identifying it with a particular fixed-shift parameter. The code does not claim a global identity for arbitrary nonminimal denominators.

## 5. Four exact examples

| Type | Prime | Rosati `(A,B,C,D)` | Verified representation |
|---|---:|---|---|
| II | 409 | `(1,117,2,1)` | `4/409 = 1/95706 + 1/818 + 1/117` |
| I | 73 | `(1,5,2,11)` | `4/73 = 1/110 + 1/22 + 1/4015` |
| II | 313 | `(4,10,2,2)` | `4/313 = 1/12520 + 1/5008 + 1/80` |
| I | 241 | `(3,66,3,7)` | `4/241 = 1/1386 + 1/63 + 1/334026` |

These examples include nontrivial normalizing gcds (`2` and `3`), not only the coprime/easiest cases. Every equality is checked with Python's exact `Fraction` arithmetic.

## 6. Verification performed

- 20 unit tests pass within this phase pack.
- Tests include fixed examples, invalid-input rejection, both conversion directions, nontrivial gcd normalization, and bounded generated-witness round trips.
- No third-party Python package is required; tests use only the standard library.
- These are finite implementation checks, not proof of universal existence of any witness.

## 7. What is not proved

This dictionary does not show that either Type I or Type II witnesses exist for every prime `p≡1 (mod 24)`. That universal existence statement remains equivalent to the unresolved part of Erdős–Straus. No new infinite family of primes or universal bound on witness parameters is claimed here.

## 8. Research value / next problem

The useful output of this phase is a source-correct, executable coordinate dictionary. It prevents the previous Type-I citation error and lets later work translate a candidate witness among three equivalent representations without re-deriving normalizations each time.

The next genuine research question is not “can the known criteria be translated?”—that has now been done. It is whether one can prove a new uniform restriction or construction for the parameters (for example, a bounded family of Type-II modulators or a nontrivial Type-I family) on the remaining prime class `p≡1 mod 24`. Any proposed restriction must first be checked against Dahan's depth/density results and Pomerance–Weingartner's exceptional-prime estimates.
