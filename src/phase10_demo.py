from __future__ import annotations
import argparse,json
from pathlib import Path
from phase8_small_factor import all_witnesses_small_factor
from phase10_jacobi_audit import audit_type_ii_witness
DEFAULT_PRIMES=(193,2521,66529,10009,100057,1000033,10000537,100000081,1000000009)
def run(primes=DEFAULT_PRIMES):
    records=[]; total=passed=0
    for p in primes:
        ur=[]
        for u in range(1,5):
            ws=all_witnesses_small_factor(p,u)
            audits=[audit_type_ii_witness(p,w) for w in ws]
            pc=sum(x.passed for x in audits)
            total+=len(ws); passed+=pc
            ur.append({"u":u,"witness_count":len(ws),"passed_count":pc,
                       "failed_count":len(ws)-pc,"certificates":[x.as_dict() for x in audits]})
        records.append({"p":p,"p_mod_24":p%24,"u_slices":ur,
                        "witness_total":sum(x["witness_count"] for x in ur)})
    return {"study":"Phase 10 Jacobi audit","source":"Dahan arXiv:2611.08717 Theorem 2.4",
            "mapping":"Phase8 alpha=k, c=e","primes":list(primes),"witness_count":total,
            "passed_count":passed,"failed_count":total-passed,"all_passed":total==passed,
            "records":records}
def main():
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,default=Path("results/PHASE10-JACOBI-AUDIT.json"));ap.add_argument("--primes",type=int,nargs="*",default=list(DEFAULT_PRIMES));args=ap.parse_args()
    r=run(tuple(args.primes));args.output.parent.mkdir(parents=True,exist_ok=True);args.output.write_text(json.dumps(r,indent=2),encoding="utf-8")
    for x in r["records"]:print(f"p={x['p']}: witnesses={x['witness_total']}")
    print(f"TOTAL: {r['passed_count']}/{r['witness_count']} passed; failures={r['failed_count']}")
    print(f"Saved: {args.output}");return 0 if r["all_passed"] else 1
if __name__=="__main__":raise SystemExit(main())
