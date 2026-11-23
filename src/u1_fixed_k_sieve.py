"""Fixed-k divisor sieve for u=1 Type-II witnesses.

For p prime, p == 1 (mod 24), and k >= 1:
    u=1 witness with this k
iff p+4k has a divisor s == -1 (mod 4k).
Then a=(s+1)/(4k), t=(p+4k)/s, and s=4ak-1.

Standard library only.
"""
from __future__ import annotations
from math import isqrt


def factorization(n: int) -> list[tuple[int, int]]:
    if not isinstance(n, int) or isinstance(n, bool) or n < 1:
        raise ValueError("n must be a positive integer")
    out=[]
    e=0
    while n % 2 == 0 and n > 1:
        n//=2
        e+=1
    if e: out.append((2,e))
    q=3
    while q <= isqrt(n):
        e=0
        while n % q == 0:
            n//=q
            e+=1
        if e: out.append((q,e))
        q+=2
    if n>1: out.append((n,1))
    return out


def divisor_residue_representatives(n: int, modulus: int) -> dict[int,int]:
    """Return one actual divisor for every residue attained modulo modulus."""
    if n<1 or modulus<2:
        raise ValueError("require n >= 1 and modulus >= 2")
    states={1 % modulus:1}
    for q,e in factorization(n):
        powers=[q**j for j in range(e+1)]
        new={}
        for residue,divisor in states.items():
            for power in powers:
                r=(residue*(power % modulus)) % modulus
                new.setdefault(r,divisor*power)
        states=new
    return states


def fixed_k_witness(p: int, k: int) -> dict[str,int] | None:
    """Return an exact u=1 witness for this fixed k, or None."""
    if not isinstance(p,int) or isinstance(p,bool) or p<2 or p%24!=1:
        raise ValueError("p must be an integer >=2 with p == 1 (mod 24)")
    if not isinstance(k,int) or isinstance(k,bool) or k<1:
        raise ValueError("k must be a positive integer")
    n=p+4*k
    modulus=4*k
    reps=divisor_residue_representatives(n,modulus)
    s=reps.get(modulus-1)
    if s is None:
        return None
    a,rem=divmod(s+1,modulus)
    t,rem_t=divmod(n,s)
    if rem or rem_t or a<1 or t<1:
        raise ArithmeticError("failed to reconstruct positive integer parameters")
    if s != 4*a*k-1 or n != t*s:
        raise ArithmeticError("factorization identity failed")
    if (a*p+1)%s:
        raise ArithmeticError("original Dahan divisibility condition failed")
    if (s+1)%(4*a):
        raise ArithmeticError("original Dahan congruence failed")
    return {"p":p,"u":1,"a":a,"k":k,"s":s,"t":t}


def k1_witness_from_prime_factor(p: int) -> dict[str,int] | None:
    """k=1 succeeds iff p+4 has a prime factor q == 3 (mod 4)."""
    if not isinstance(p,int) or isinstance(p,bool) or p<2 or p%24!=1:
        raise ValueError("p must satisfy p == 1 (mod 24)")
    for q,e in factorization(p+4):
        if q%4==3:
            s=q
            a=(s+1)//4
            t=(p+4)//s
            if (p+4)!=t*s or (a*p+1)%s:
                raise ArithmeticError("k=1 construction failed")
            return {"p":p,"u":1,"a":a,"k":1,"s":s,"t":t}
    return None


def k2_coordinate_test(p: int) -> dict[str,object]:
    """Exact C2 x C2 product-set criterion for k=2.

    U(8)={1,3,5,7}; use 3^alpha 5^beta with alpha,beta mod 2.
    Target -1=7 corresponds to (1,1).
    """
    if not isinstance(p,int) or isinstance(p,bool) or p<2 or p%24!=1:
        raise ValueError("p must satisfy p == 1 (mod 24)")
    n=p+8
    # Residue vectors: 1:(0,0), 3:(1,0), 5:(0,1), 7:(1,1).
    coordinates={1:(0,0),3:(1,0),5:(0,1),7:(1,1)}
    states={(0,0)}
    data=[]
    for q,e in factorization(n):
        v=coordinates[q%8]
        data.append((q,e,v))
        powers={((j*v[0])%2,(j*v[1])%2) for j in range(e+1)}
        states={((x+a)%2,(y+b)%2) for (x,y) in states for (a,b) in powers}
    target=(1,1)
    generic=fixed_k_witness(p,2)
    return {
        "p":p,"n":n,"factorization":factorization(n),
        "factor_coordinates":data,
        "reachable_coordinates":sorted(states),
        "target_coordinates":target,
        "witness_exists":target in states,
        "witness":generic,
    }


def first_witness_up_to_k(p: int, k_max: int) -> dict[str,int] | None:
    if not isinstance(k_max,int) or isinstance(k_max,bool) or k_max<1:
        raise ValueError("k_max must be positive")
    for k in range(1,k_max+1):
        w=fixed_k_witness(p,k)
        if w is not None:
            return w
    return None


if __name__=="__main__":
    for p in (73,97,193,313,1009,2521,66529):
        print("p=",p)
        print("  k=1:",k1_witness_from_prime_factor(p))
        print("  k=2:",k2_coordinate_test(p))
        print("  first k<=12:",first_witness_up_to_k(p,12))
