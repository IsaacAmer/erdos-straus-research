# ES-FOUNDATION-01-DRAFT
## Preliminary mathematical audit: witness criterion and Bradford divisor criterion

**Status:** Working draft — algebraic equivalence under the stated hypotheses; literature attribution remains to be checked.

### 1. Setup

Let \(p\) be prime, with
\[
p\equiv 1\pmod 4,\qquad h\equiv 3\pmod 4,\qquad 0<h\le p,
\]
and define
\[
K=\frac{p+h}{4}.
\]

Then \(K\) is a positive integer. Also,
\[
\gcd(h,p)=1,\qquad \gcd(h,K)=1,\qquad p\nmid K.
\]
Indeed, \(4K=p+h\), \(h\) is odd, and \(p\nmid h\) because \(0<h\le p\) and \(h\not\equiv p\pmod4\). Consequently \(\gcd(h,pK)=1\).

### 2. Binary Egyptian-fraction criterion

For positive coprime integers \(A,M\), the equation
\[
\frac AM=\frac1a+\frac1b
\]
has a positive-integer solution if and only if there exist positive coprime divisors \(r,s\mid M\) such that
\[
r+s\equiv0\pmod A.
\]

**Proof.** If a solution exists, write \(a=gr,\ b=gs\), where \(g=\gcd(a,b)\) and \(\gcd(r,s)=1\). Then
\[
Agrs=M(r+s).
\]
Since \(\gcd(rs,r+s)=1\), it follows that \(rs\mid M\); since \(\gcd(A,M)=1\), it also follows that \(A\mid r+s\).

Conversely, given such \(r,s\), set
\[
g=\frac{M(r+s)}{Ars}.
\]
The divisibility conditions ensure that \(g\) is a positive integer, and then
\[
\frac1{gr}+\frac1{gs}=\frac AM.
\]
This proves the criterion.

### 3. Application to the Erdős–Straus remainder

Since \(4K=p+h\),
\[
\frac4p-\frac1K=\frac{h}{pK}.
\]
The criterion above, applied with \(A=h\) and \(M=pK\), shows that
\[
\frac4p=\frac1K+\frac1A+\frac1B
\]
for positive integers \(A,B\) if and only if there exist coprime positive divisors \(u,v\mid pK\) with
\[
h\mid u+v.
\]

This is an independently stated witness criterion. Do not attribute it to a named author's theorem without checking the exact theorem statement and hypotheses in the original source.

### 4. Conversion to divisor conditions

Consider coprime positive divisors \(u,v\mid pK\) satisfying \(h\mid u+v\).

#### Case I: \(p\nmid u\) and \(p\nmid v\)

Then \(u,v\mid K\). After interchanging them if necessary, assume \(u\le v\), and define
\[
d=\frac{Ku}{v}.
\]
This is an integer, \(d\mid K^2\), and \(d\le K\). Moreover,
\[
d+K=\frac Kv(u+v),
\]
so \(h\mid d+K\), because \(v\mid K\) and \(\gcd(K,h)=1\). Thus
\[
d\mid K^2,\qquad d\le K,\qquad d\equiv-K\pmod h.
\]

#### Case II: \(p\mid u\) or \(p\mid v\)

By coprimality, at most one is divisible by \(p\). After interchanging, write \(u=pr,\ v=s\). Since \(p\nmid K\), we have \(r,s\mid K\) and \(\gcd(r,s)=1\). Define
\[
d=\frac{Ks}{r}.
\]
Then \(d\) is an integer, \(d\mid K^2\), and
\[
d+pK=\frac Kr(s+pr).
\]
Hence
\[
d\equiv-pK\pmod h.
\]
No condition \(d\le K\) is asserted in this case.

### 5. Reverse conversion by prime valuations

Suppose \(d\mid K^2\). Write
\[
K=\prod_q q^{e_q},\qquad d=\prod_q q^{f_q},
\]
where \(0\le f_q\le2e_q\).

For the branch
\[
d\le K,\qquad d\equiv-K\pmod h,
\]
define
\[
u=\prod_q q^{\max(f_q-e_q,0)},\qquad
v=\prod_q q^{\max(e_q-f_q,0)}.
\]
Then \(u,v\mid K\), \(\gcd(u,v)=1\), and \(d=Ku/v\). Thus
\[
d+K=\frac Kv(u+v).
\]
Since \(h\mid d+K\) and \(\gcd(K/v,h)=1\), we get \(h\mid u+v\).

For the branch
\[
d\mid K^2,\qquad d\equiv-pK\pmod h,
\]
define
\[
r=\prod_q q^{\max(e_q-f_q,0)},\qquad
s=\prod_q q^{\max(f_q-e_q,0)}.
\]
Then \(r,s\mid K\), \(\gcd(r,s)=1\), and \(d=Ks/r\). Therefore
\[
d+pK=\frac Kr(s+pr).
\]
Using \(\gcd(K/r,h)=1\), we obtain \(h\mid s+pr\). Taking \(u=pr,\ v=s\) gives coprime divisors of \(pK\) with \(h\mid u+v\).

### 6. Conditional equivalence statement

Under the hypotheses in Section 1, the following are equivalent:

1. There exist coprime positive divisors \(u,v\mid pK\) such that \(h\mid u+v\).
2. There exists a positive divisor \(d\mid K^2\) satisfying at least one of:
   - \(d\equiv-pK\pmod h\);
   - \(d\le K\) and \(d\equiv-K\pmod h\).

The proof is given by the forward and reverse constructions above.

### 7. Verification cautions and open items

- This establishes an algebraic equivalence between the two explicitly stated conditions; it does **not** prove the Erdős–Straus conjecture.
- The attribution of the witness criterion to Dahan must be checked against the exact theorem, notation, and hypotheses in the original paper. Do not infer attribution merely from similarity.
- Bradford's Type I/Type II terminology must be matched to the definitions in the original paper. In the present conversion, the two branches are described by whether \(p\) divides one of the witness divisors; this should not be confused with the original classification unless the source explicitly identifies them.
- No computational test is a substitute for the general proof.
- Before publication or external circulation, independently check every divisibility implication and compare the statements with the original papers.

**Research status:** preliminary proof draft; mathematical derivation recorded; bibliographic attribution and source-level comparison remain open.
