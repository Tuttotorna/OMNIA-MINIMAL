#!/usr/bin/env python3
"""
OMNIA-MINIMAL demo runner.

This is not the full OMNIA engine.

It is a minimal deterministic demonstration of the core distinction:

    surface correctness != structural stability
    measurement != inference != decision

The runner reads transformed case groups, compares expected answers and
model answers, and emits a bounded structural signal.
"""

import json
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "minimal_cases.jsonl"
RESULTS_PATH = ROOT / "results" / "minimal_results.jsonl"


def normalize(value):
    return str(value).strip().lower()


def read_jsonl(path):
    rows = []
    with path.open("r", encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                raise ValueError(f"Invalid JSONL at line {line_number}: {exc}") from exc
    return rows


def group_rows(rows):
    groups = defaultdict(list)
    for row in rows:
        required = [
            "case_group",
            "variant_id",
            "variant_type",
            "task",
            "expected_answer",
            "model_answer",
        ]
        missing = [key for key in required if key not in row]
        if missing:
            raise ValueError(f"Missing keys {missing} in row: {row}")
        groups[row["case_group"]].append(row)
    return dict(groups)


def measure_group(case_group, rows):
    base_rows = [r for r in rows if r["variant_type"] == "base"]
    if len(base_rows) != 1:
        raise ValueError(f"{case_group} must contain exactly one base variant.")

    base = base_rows[0]
    correctness = []
    answers = []
    expected_values = []

    for row in rows:
        expected = normalize(row["expected_answer"])
        answer = normalize(row["model_answer"])
        expected_values.append(expected)
        answers.append(answer)
        correctness.append(answer == expected)

    base_surface_correct = normalize(base["model_answer"]) == normalize(base["expected_answer"])
    all_surface_correct = all(correctness)
    unique_answers = sorted(set(answers))
    unique_expected = sorted(set(expected_values))

    omega = sum(correctness) / len(correctness)
    answer_variance = max(0, len(unique_answers) - 1)
    delta_omega = 1.0 - omega

    if all_surface_correct and answer_variance == 0:
        signal = "STABLE"
    elif base_surface_correct and (not all_surface_correct or answer_variance > 0):
        signal = "FRAGILE"
    else:
        signal = "DIVERGENT"

    return {
        "case_group": case_group,
        "variant_count": len(rows),
        "base_surface_correct": base_surface_correct,
        "all_surface_correct": all_surface_correct,
        "unique_expected_answers": unique_expected,
        "unique_model_answers": unique_answers,
        "omega": round(omega, 6),
        "delta_omega": round(delta_omega, 6),
        "answer_variance": answer_variance,
        "structural_signal": signal,
        "boundary": "measurement != inference != decision",
    }


def main():
    rows = read_jsonl(DATA_PATH)
    groups = group_rows(rows)
    results = []

    print("=" * 80)
    print("OMNIA-MINIMAL")
    print("=" * 80)
    print("Correctness is not structural stability.")
    print("Measurement is not inference. Measurement is not decision.")
    print("=" * 80)

    for case_group, group in sorted(groups.items()):
        result = measure_group(case_group, group)
        results.append(result)

        print()
        print(f"CASE: {result['case_group']}")
        print(f"variant_count: {result['variant_count']}")
        print(f"base_surface_correct: {str(result['base_surface_correct']).lower()}")
        print(f"all_surface_correct: {str(result['all_surface_correct']).lower()}")
        print(f"unique_model_answers: {result['unique_model_answers']}")
        print(f"omega: {result['omega']}")
        print(f"delta_omega: {result['delta_omega']}")
        print(f"answer_variance: {result['answer_variance']}")
        print(f"structural_signal: {result['structural_signal']}")

    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)
    with RESULTS_PATH.open("w", encoding="utf-8") as f:
        for result in results:
            f.write(json.dumps(result, ensure_ascii=False) + "\n")

    print()
    print("=" * 80)
    print(f"Wrote results to: {RESULTS_PATH.relative_to(ROOT)}")
    print("=" * 80)


if __name__ == "__main__":
    main()
