import json, re, pathlib
from itertools import combinations

ROOT = pathlib.Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "admissible_transformation_cases.jsonl"
RESULTS = ROOT / "results"
RESULTS.mkdir(parents=True, exist_ok=True)

WORDS = {
    "zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
    "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
    "ten": "10", "eleven": "11", "twelve": "12"
}

def extract_numeric_core(output):
    text = output.lower().strip()
    m = re.search(r"\b\d+\b", text)
    if m:
        return m.group(0)
    for word, value in WORDS.items():
        if re.search(rf"\b{re.escape(word)}\b", text):
            return value
    return None

def dispersion(values):
    pairs = list(combinations(values, 2))
    if not pairs:
        return 0.0
    bad = sum(1 for a, b in pairs if a is None or b is None or a != b)
    return bad / len(pairs)

def classify(d):
    if d == 0:
        return "STABLE"
    if d < 1:
        return "FRAGILE"
    return "DIVERGENT"

def evaluate(case):
    variants = []
    for v in case["variants"]:
        core = extract_numeric_core(v["output"])
        variants.append({
            "transformation": v["transformation"],
            "input": v["input"],
            "output": v["output"],
            "extracted_core": core,
            "expected_core": case["expected_core"],
            "matches_expected": core == case["expected_core"]
        })
    values = [v["extracted_core"] for v in variants]
    d = dispersion(values)
    return {
        "case_id": case["case_id"],
        "description": case["description"],
        "expected_core": case["expected_core"],
        "extracted_values": values,
        "dispersion": d,
        "classification": classify(d),
        "variants": variants
    }

cases = [json.loads(line) for line in DATA.read_text(encoding="utf-8").splitlines() if line.strip()]
results = [evaluate(c) for c in cases]

(RESULTS / "structural_evaluation_results.json").write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

lines = [
    "# Structural Evaluation Demo Results",
    "",
    "Formula:",
    "",
    "Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })",
    "",
    "| Case | Expected Core | Extracted Values | Dispersion | Classification |",
    "|---|---:|---|---:|---|"
]

for r in results:
    lines.append(f"| {r['case_id']} | {r['expected_core']} | {r['extracted_values']} | {r['dispersion']:.3f} | {r['classification']} |")

lines += [
    "",
    "Interpretation:",
    "",
    "- STABLE: admissible transformations preserved the task-relevant structure.",
    "- FRAGILE: at least one admissible transformation produced an incompatible output.",
    "- DIVERGENT: outputs are broadly incompatible across the transformed family.",
    "",
    "Boundary:",
    "",
    "This demo does not decide truth, intelligence, or final reliability.",
    "It only measures compatibility of extracted task-relevant properties across admissible transformations."
]

(RESULTS / "structural_evaluation_results.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

print("Structural Evaluation over Admissible Transformations")
print("=" * 72)
for r in results:
    print(f"{r['case_id']}: classification={r['classification']}, dispersion={r['dispersion']:.3f}, values={r['extracted_values']}")
print(f"\nWrote: {RESULTS / 'structural_evaluation_results.json'}")
print(f"Wrote: {RESULTS / 'structural_evaluation_results.md'}")
