"""Exact Jacobi-symbol audit of Phase 8 Type-II witnesses.

The checked symbol laws are Dahan, arXiv:2611.08717, Theorem 2.4.
Mapping: Phase8.k = Dahan alpha; Phase8.e = Dahan c.
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from functools import lru_cache
from math import gcd
from phase7_floor_quotient import prime_by_trial_division

@dataclass(frozen=True)
class JacobiAudit:
    p:int; u:int; a:int; s:int; v:int; e:int; alpha:int
    identity_ap_plus_u_equals_sv:bool
    identity_s_plus_1_equals_4u_alpha_a:bool
    identity_u_plus_v_equals_ae:bool
    identity_p_plus_e_equals_4u_alpha_v:bool
    coprime_u_a:bool
    jacobi_alpha_over_s:int
    jacobi_ua_over_s:int
    jacobi_s_over_p:int
    jacobi_p_over_s:int
    jacobi_uv_over_p:int
    jacobi_alpha_e_over_p:int
    @property
    def identities_ok(self):
        return all((self.identity_ap_plus_u_equals_sv,
                    self.identity_s_plus_1_equals_4u_alpha_a,
                    self.identity_u_plus_v_equals_ae,
                    self.identity_p_plus_e_equals_4u_alpha_v,
                    self.coprime_u_a))
    @property
    def jacobi_laws_ok(self):
        return (self.jacobi_alpha_over_s==1 and self.jacobi_ua_over_s==1 and
                self.jacobi_s_over_p==-1 and self.jacobi_p_over_s==-1 and
                self.jacobi_uv_over_p==-1 and self.jacobi_alpha_e_over_p==-1)
    @property
    def passed(self): return self.identities_ok and self.jacobi_laws_ok
    def as_dict(self):
        d=asdict(self); d.update(identities_ok=self.identities_ok,
                                jacobi_laws_ok=self.jacobi_laws_ok,
                                passed=self.passed)
        return d

def jacobi_symbol(a:int,n:int)->int:
    if not isinstance(a,int) or isinstance(a,bool): raise TypeError("a must be integer")
    if not isinstance(n,int) or isinstance(n,bool) or n<=0 or n%2==0:
        raise ValueError("n must be positive odd")
    a%=n; sign=1
    while a:
        while a%2==0:
            a//=2
            if n%8 in (3,5): sign=-sign
        a,n=n,a
        if a%4==3 and n%4==3: sign=-sign
        a%=n
    return sign if n==1 else 0

@lru_cache(maxsize=256)
def _is_prime(p): return prime_by_trial_division(p)

def audit_type_ii_witness(p,witness):
    if not isinstance(p,int) or isinstance(p,bool) or p<=1 or p%24!=1:
        raise ValueError("p must be 1 mod 24")
    if not _is_prime(p): raise ValueError("p must be prime")
    try: vals=(witness.u,witness.a,witness.s,witness.v,witness.e,witness.k)
    except AttributeError as exc: raise TypeError("witness must expose u,a,s,v,e,k") from exc
    if any(not isinstance(x,int) or isinstance(x,bool) for x in vals):
        raise TypeError("witness fields must be integers")
    u,a,s,v,e,alpha=vals
    if min(vals)<=0 or u not in (1,2,3,4): raise ValueError("invalid witness parameters")
    if s%2==0: raise ValueError("s must be odd")
    return JacobiAudit(
        p,u,a,s,v,e,alpha,
        a*p+u==s*v,
        s+1==4*u*alpha*a,
        u+v==a*e,
        p+e==4*u*alpha*v,
        gcd(u,a)==1,
        jacobi_symbol(alpha,s),jacobi_symbol(u*a,s),
        jacobi_symbol(s,p),jacobi_symbol(p,s),
        jacobi_symbol(u*v,p),jacobi_symbol(alpha*e,p))

def audit_witness_collection(p,witnesses):
    audits=[audit_type_ii_witness(p,w) for w in witnesses]
    failed=[x.as_dict() for x in audits if not x.passed]
    return {"p":p,"witness_count":len(audits),"passed_count":len(audits)-len(failed),
            "failed_count":len(failed),"all_passed":not failed,"failed_certificates":failed}
