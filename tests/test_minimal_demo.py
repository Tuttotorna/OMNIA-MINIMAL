import json
import subprocess
import sys
from pathlib import Path


def test_minimal_demo_runs():
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
    assert "STABLE" in result.stdout
    assert "FRAGILE" in result.stdout
    assert "DIVERGENT" in result.stdout


def test_results_are_written():
    root = Path(__file__).resolve().parents[1]
    results_path = root / "results" / "minimal_results.jsonl"

    assert results_path.exists()

    rows = [
        json.loads(line)
        for line in results_path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]

    signals = {row["case_group"]: row["structural_signal"] for row in rows}

    assert signals["arithmetic_stable_001"] == "STABLE"
    assert signals["arithmetic_fragile_001"] == "FRAGILE"
    assert signals["arithmetic_divergent_001"] == "DIVERGENT"
