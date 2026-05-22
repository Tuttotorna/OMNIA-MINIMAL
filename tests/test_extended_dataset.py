import json
import subprocess
import sys
from pathlib import Path


def load_jsonl(path):
    return [
        json.loads(line)
        for line in Path(path).read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def test_extended_case_groups_present():
    root = Path(__file__).resolve().parents[1]
    rows = load_jsonl(root / "data" / "minimal_cases.jsonl")
    groups = {row["case_group"] for row in rows}

    expected_groups = {
        "arithmetic_stable_001",
        "arithmetic_fragile_001",
        "arithmetic_divergent_001",
        "symbolic_fragile_001",
        "paraphrase_stable_001",
        "distractor_fragile_001",
        "representation_fragile_001",
    }

    missing = expected_groups - groups
    assert not missing, f"Missing expected case groups: {sorted(missing)}"


def test_extended_results_include_multiple_fragile_families():
    root = Path(__file__).resolve().parents[1]
    script = root / "examples" / "run_minimal_demo.py"

    result = subprocess.run(
        [sys.executable, str(script)],
        cwd=str(root),
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    assert result.returncode == 0, result.stderr

    results_path = root / "results" / "minimal_results.jsonl"
    rows = load_jsonl(results_path)

    signals = {row["case_group"]: row["structural_signal"] for row in rows}

    assert signals["symbolic_fragile_001"] == "FRAGILE"
    assert signals["distractor_fragile_001"] == "FRAGILE"
    assert signals["representation_fragile_001"] == "FRAGILE"
    assert signals["paraphrase_stable_001"] == "STABLE"

    fragile_count = sum(1 for signal in signals.values() if signal == "FRAGILE")
    assert fragile_count >= 4
