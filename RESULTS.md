# Minimal Results

This file summarizes the expected result of the minimal demo.

The generated machine-readable output is stored in:

    results/minimal_results.jsonl

---

## Expected cases

arithmetic_stable_001:

Surface correctness passes.

Transformed variants remain compatible.

Expected signal:

    STABLE

---

arithmetic_fragile_001:

The base output is surface-correct.

At least one transformed variant becomes inconsistent.

Expected signal:

    FRAGILE

---

arithmetic_divergent_001:

The group contains direct correctness failure and incompatible answers.

Expected signal:

    DIVERGENT

---

## Interpretation

The important case is:

    FRAGILE

because it demonstrates the central claim:

    a case can pass surface correctness while failing structural stability
