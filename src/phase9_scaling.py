"""Reproducible Phase 7 vs Phase 8 scaling benchmark.

The benchmark compares complete witness sets, not only successful examples.
It records wall-clock time for each fixed (p,u), verifies exact tuple equality,
and stores machine-readable CSV/JSON results.

Run from the repository root:
    python src/phase9_scaling.py --repeats 5

This requires the existing project modules phase7_floor_quotient.py and
phase8_small_factor.py in the same src directory.
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import statistics
import sys
import time
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable

from phase7_floor_quotient import (
    TypeIIWitness,
    all_dual_type_ii_witnesses,
    floor_quotient_k_candidates,
    prime_by_trial_division,
)
from phase8_small_factor import (
    all_witnesses_small_factor,
    count_small_factor_divisibility_tests,
)

# All entries are primes congruent to 1 mod 24. They deliberately mix the
# project's three boundary cases with geometric scale steps from 10^4 to 10^8.
DEFAULT_PRIMES = (
    193,
    2_521,
    66_529,
    10_009,
    100_057,
    1_000_033,
    10_000_537,
    100_000_081,
)


def _median_seconds(fn: Callable[[], tuple[TypeIIWitness, ...]], repeats: int) -> tuple[float, tuple[TypeIIWitness, ...]]:
    samples: list[float] = []
    output: tuple[TypeIIWitness, ...] | None = None
    for _ in range(repeats):
        start = time.perf_counter()
        current = fn()
        elapsed = time.perf_counter() - start
        if output is None:
            output = current
        elif current != output:
            raise RuntimeError("A deterministic search returned different witness sets")
        samples.append(elapsed)
    assert output is not None
    return statistics.median(samples), output


def _verify_witness_set(p: int, u: int, witnesses: tuple[TypeIIWitness, ...]) -> None:
    for w in witnesses:
        if w.u != u:
            raise AssertionError(f"wrong u in witness: {w}")
        if w.a * p + u != w.s * w.v:
            raise AssertionError(f"ap+u=sv failed: p={p}, witness={w}")
        if w.s + 1 != 4 * u * w.a * w.k:
            raise AssertionError(f"s+1=4uak failed: p={p}, witness={w}")
        if u + w.v != w.a * w.e:
            raise AssertionError(f"u+v=ae failed: p={p}, witness={w}")
        if p + w.e != 4 * u * w.v * w.k:
            raise AssertionError(f"p+e=4uvk failed: p={p}, witness={w}")


def benchmark_one(p: int, u: int, repeats: int = 5) -> dict[str, object]:
    if not prime_by_trial_division(p):
        raise ValueError(f"benchmark input is not prime: {p}")
    if p % 24 != 1:
        raise ValueError(f"benchmark input is not 1 modulo 24: {p}")
    if not 1 <= u <= 4:
        raise ValueError("u must be in {1,2,3,4}")
    if repeats < 1:
        raise ValueError("repeats must be positive")

    phase7 = lambda: all_dual_type_ii_witnesses(p, u)
    phase8 = lambda: all_witnesses_small_factor(p, u)

    # Warm-up both paths, then require exact equality before timing.
    warm7 = phase7()
    warm8 = phase8()
    if warm7 != warm8:
        raise AssertionError(
            f"Phase 7/8 witness-set mismatch at p={p}, u={u}: "
            f"Phase7={warm7}, Phase8={warm8}"
        )
    _verify_witness_set(p, u, warm7)

    # Alternate execution order to reduce systematic order bias.
    t7: list[float] = []
    t8: list[float] = []
    for rep in range(repeats):
        order = (phase7, phase8) if rep % 2 == 0 else (phase8, phase7)
        elapsed: list[float] = []
        outputs: list[tuple[TypeIIWitness, ...]] = []
        for fn in order:
            start = time.perf_counter()
            out = fn()
            elapsed.append(time.perf_counter() - start)
            outputs.append(out)
        if outputs[0] != outputs[1] or outputs[0] != warm7:
            raise AssertionError(f"Witness sets changed during benchmark p={p}, u={u}")
        if rep % 2 == 0:
            t7.append(elapsed[0]); t8.append(elapsed[1])
        else:
            t8.append(elapsed[0]); t7.append(elapsed[1])

    med7 = statistics.median(t7)
    med8 = statistics.median(t8)
    k_count = len(floor_quotient_k_candidates(p, u))
    residue_tests = count_small_factor_divisibility_tests(p, u)
    return {
        "p": p,
        "u": u,
        "k_candidates": k_count,
        "witness_count": len(warm7),
        "phase7_median_seconds": med7,
        "phase8_median_seconds": med8,
        "speedup_phase7_over_phase8": (med7 / med8) if med8 else None,
        "phase8_small_factor_divisibility_tests": residue_tests,
        "repeats": repeats,
        "witness_sets_identical": True,
        "witness_identities_verified": True,
    }


def run_benchmark(primes: tuple[int, ...] = DEFAULT_PRIMES, repeats: int = 5) -> dict[str, object]:
    rows: list[dict[str, object]] = []
    for p in primes:
        for u in range(1, 5):
            rows.append(benchmark_one(p, u, repeats=repeats))

    by_prime: list[dict[str, object]] = []
    for p in primes:
        subset = [r for r in rows if r["p"] == p]
        t7 = sum(float(r["phase7_median_seconds"]) for r in subset)
        t8 = sum(float(r["phase8_median_seconds"]) for r in subset)
        by_prime.append({
            "p": p,
            "u_values": 4,
            "witnesses_total": sum(int(r["witness_count"]) for r in subset),
            "phase7_sum_of_u_medians_seconds": t7,
            "phase8_sum_of_u_medians_seconds": t8,
            "speedup": (t7 / t8) if t8 else None,
            "all_witness_sets_identical": all(bool(r["witness_sets_identical"]) for r in subset),
        })

    return {
        "benchmark_name": "Erdos-Straus Phase 7 vs Phase 8 exact Type-II search",
        "timestamp_utc": datetime.now(timezone.utc).isoformat(),
        "environment": {
            "python_version": sys.version,
            "implementation": platform.python_implementation(),
            "platform": platform.platform(),
            "processor": platform.processor(),
            "logical_cpu_count": os.cpu_count(),
        },
        "methodology": {
            "timing": "median of repeated full witness-set searches; perf_counter; warm-up excluded",
            "repeats": repeats,
            "comparison": "exact equality of sorted TypeIIWitness tuples for each (p,u)",
            "verification": "all original Type-II identities rechecked for every returned witness",
            "scope": "fixed p and fixed u in {1,2,3,4}; input p deterministically checked prime and p == 1 mod 24",
            "caution": "timings are environment-specific; no general asymptotic speedup is inferred from this finite sample",
        },
        "rows": rows,
        "by_prime": by_prime,
    }


def save_results(result: dict[str, object], output_dir: Path) -> tuple[Path, Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    json_path = output_dir / "PHASE9-SCALING-RESULTS.json"
    csv_path = output_dir / "PHASE9-SCALING-RESULTS.csv"
    txt_path = output_dir / "PHASE9-SCALING-RESULTS.txt"
    json_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    rows = result["rows"]
    assert isinstance(rows, list)
    if rows:
        with csv_path.open("w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
            writer.writeheader()
            writer.writerows(rows)

    lines = [
        str(result["benchmark_name"]),
        f"UTC: {result['timestamp_utc']}",
        f"Python: {result['environment']['python_version']}",
        f"Platform: {result['environment']['platform']}",
        "",
        "Per-prime aggregate (sum of medians over u=1..4):",
        "p | Phase7 seconds | Phase8 seconds | speedup | all witnesses equal",
    ]
    for row in result["by_prime"]:
        lines.append(
            f"{row['p']} | {row['phase7_sum_of_u_medians_seconds']:.9f} | "
            f"{row['phase8_sum_of_u_medians_seconds']:.9f} | "
            f"{row['speedup']:.2f}x | {row['all_witness_sets_identical']}"
        )
    txt_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return json_path, csv_path, txt_path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repeats", type=int, default=5)
    parser.add_argument("--output-dir", type=Path, default=Path("results"))
    parser.add_argument("--primes", type=int, nargs="*", default=list(DEFAULT_PRIMES))
    args = parser.parse_args()
    result = run_benchmark(tuple(args.primes), repeats=args.repeats)
    paths = save_results(result, args.output_dir)
    for row in result["by_prime"]:
        print(
            f"p={row['p']}: Phase7={row['phase7_sum_of_u_medians_seconds']:.6f}s, "
            f"Phase8={row['phase8_sum_of_u_medians_seconds']:.6f}s, "
            f"speedup={row['speedup']:.2f}x, "
            f"equal={row['all_witness_sets_identical']}"
        )
    print("Saved:", *(str(p) for p in paths))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
