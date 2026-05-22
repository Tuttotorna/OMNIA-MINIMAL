# Failure Conditions

This document defines when the OMNIA-MINIMAL claim would weaken or fail.

The repository is intentionally falsifiable.

It does not claim universal truth.

It demonstrates one bounded distinction:

    correctness is not structural stability

---

## 1. Collapse condition

The claim would weaken if surface correctness and structural stability always collapsed into the same measurement.

If every correct answer were always structurally stable, and every incorrect answer were always structurally unstable, then the OMNIA-MINIMAL distinction would add no information.

The fragile case exists to test exactly this gap.

---

## 2. Invalid transformation condition

The claim would weaken if the transformed variants did not preserve the same underlying task.

A transformation must not secretly change the task.

Acceptable transformations include:

    reordering equivalent quantities
    rephrasing the same relation
    changing surface form without changing expected structure

Invalid transformations include:

    changing the expected answer
    adding new hidden constraints
    removing required information
    changing the task type

---

## 3. Hidden semantic judgment condition

The claim would weaken if the result depended on hidden semantic interpretation.

OMNIA-MINIMAL avoids this by using explicit fields:

    task
    expected_answer
    model_answer

The minimal runner does not infer meaning.

It compares declared expected answers against declared observed answers.

---

## 4. Non-reproducibility condition

The claim would weaken if the demo could not be reproduced.

For that reason, the repository includes:

    deterministic data
    deterministic runner
    pytest tests
    GitHub Actions CI

The expected local commands are:

    python examples/run_minimal_demo.py
    pytest -q

---

## 5. Overclaim condition

The claim would weaken if the repository claimed more than it demonstrates.

OMNIA-MINIMAL does not claim:

    universal truth
    semantic understanding
    artificial consciousness
    final correctness
    model intelligence
    decision authority

It claims only:

    surface correctness and structural stability can diverge

---

## 6. Correct interpretation

A stable signal does not mean true.

A fragile signal does not mean false.

A divergent signal does not automatically assign blame.

The signal says only that structural behavior changed under the defined measurement.

That is the boundary:

    measurement != inference != decision
