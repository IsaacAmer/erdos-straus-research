"""Run exact sample crosswalks for the Phase-2 Rosati/Dahan/P&W dictionary."""
try:
    from src.parameter_dictionary import rosati_type_i_to_pw, rosati_type_ii_to_pw
    from src.rosati_dahan_bridge import verify_rosati_decomposition
except ModuleNotFoundError:
    # Also support direct execution as: python src/phase2_demo.py
    from parameter_dictionary import rosati_type_i_to_pw, rosati_type_ii_to_pw
    from rosati_dahan_bridge import verify_rosati_decomposition

EXAMPLES = [
    ("Type II", 409, (1, 117, 2, 1), "II"),
    ("Type I", 73, (1, 5, 2, 11), "I"),
    ("Type II, gcd normalization", 313, (4, 10, 2, 2), "II"),
    ("Type I, gcd normalization", 241, (3, 66, 3, 7), "I"),
]


def main() -> None:
    for label, p, (A, B, C, D), kind in EXAMPLES:
        ok = verify_rosati_decomposition(p, A, B, C, D, kind)
        if kind == "I":
            data = rosati_type_i_to_pw(p, A, B, C, D)
            pw_parameters = (data["A_PW"], data["d_PW"], data["f_PW"])
        else:
            data = rosati_type_ii_to_pw(p, A, B, C, D)
            pw_parameters = (data["A_PW"], data["B_PW"], data["e_PW"])
        print(f"{label}: p={p}, Rosati={(A, B, C, D)}")
        print(f"  P&W parameters={pw_parameters}; exact identity={ok}")
        if kind == "II":
            denoms = (p * B * C * D, p * A * C * D, A * B * D)
        else:
            denoms = (B * C * D, A * C * D, p * A * B * D)
        print(f"  unit-fraction denominators={denoms}")
        if not ok:
            raise SystemExit("Exact fraction verification failed")
    print("All four exact sample decompositions verified.")


if __name__ == "__main__":
    main()
