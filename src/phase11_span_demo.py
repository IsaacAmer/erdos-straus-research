"""Produce small exact square-class span certificates for sample Type-II moduli."""
from __future__ import annotations
import json
from pathlib import Path
from phase11_small_u_character_profile import prime_factor_square_class_span_certificate

SAMPLES = (
    (73, 1, 2),
    (193, 1, 2),
    (193, 2, 3),
    (2521, 4, 3),
    (10009, 3, 2),
    (100057, 2, 3),
    (193, 2, 1),
    (193, 4, 1),
)

def main() -> int:
    records = [prime_factor_square_class_span_certificate(*x) for x in SAMPLES]
    out = {
        "study": "Square-class span certificates derived from Dahan Theorem 2.8 and Phase 11 Lemma 11.1",
        "scope": "six exact sample pairs (p,u,a), all with p prime and p == 1 mod 24",
        "records": records,
        "all_quotients_verified_squares": all(r["quotient_is_square_modulus"] for r in records),
    }
    path = Path("results/PHASE11-SQUARE-CLASS-SPAN-EXAMPLES.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(out, indent=2), encoding="utf-8")
    for r in records:
        print(
            f"p={r['p']}, u={r['u']}, a={r['a']}: "
            f"target={r['target_square_class']}, subset={r['selected_prime_factors']}, "
            f"product={r['selected_subproduct']}, square quotient={r['quotient_is_square_modulus']}"
        )
    print(f"All square-class certificates verified: {out['all_quotients_verified_squares']}")
    print(f"Saved: {path}")
    return 0 if out["all_quotients_verified_squares"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
