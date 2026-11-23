"""Run the Phase 10 Dahan Theorem 2.4 audit on a reproducible prime set."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

from phase8_small_factor import all_witnesses_small_factor
from phase10_jacobi_audit import audit_type_ii_witness

DEFAULT_PRIMES = (
    193, 2521, 66529, 10009, 100057, 1000033,
    10000537, 100000081, 1000000009,
)


def run(primes: tuple[int, ...]) -> dict[str, object]:
    records = []
    witness_total = 0
    passed_total = 0
    for p in primes:
        u_records = []
        for u in range(1, 5):
            witnesses = all_witnesses_small_factor(p, u)
            audits = [audit_type_ii_witness(p, w) for w in witnesses]
            passed = sum(a.passed for a in audits)
            u_records.append({
                "u": u,
                "witness_count": len(witnesses),
                "passed_count": passed,
                "failed_count": len(audits) - passed,
                "certificates": [a.as_dict() for a in audits],
            })
            witness_total += len(witnesses)
            passed_total += passed
        records.append({
            "p": p,
            "p_mod_24": p % 24,
            "u_slices": u_records,
            "witness_total": sum(x["witness_count"] for x in u_records),
        })
    return {
        "study": "Phase 10: Jacobi-symbol audit of Type-II witnesses",
        "source": "Benjamin Dahan, arXiv:2611.08717, Theorem 2.4",
        "parameter_mapping": "Phase8 alpha=k and shift c=e",
        "primes": list(primes),
        "prime_count": len(primes),
        "u_values": [1, 2, 3, 4],
        "witness_count": witness_total,
        "passed_count": passed_total,
        "failed_count": witness_total - passed_total,
        "all_passed": witness_total == passed_total,
        "records": records,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--primes", type=int, nargs="*", default=list(DEFAULT_PRIMES))
    parser.add_argument("--output", type=Path, default=Path("results/PHASE10-JACOBI-AUDIT.json"))
    args = parser.parse_args()
    report = run(tuple(args.primes))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    for record in report["records"]:
        print(f"p={record['p']}: witnesses={record['witness_total']}")
    print(
        f"TOTAL: {report['passed_count']}/{report['witness_count']} witness audits passed; "
        f"failures={report['failed_count']}"
    )
    print(f"Saved: {args.output}")
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
