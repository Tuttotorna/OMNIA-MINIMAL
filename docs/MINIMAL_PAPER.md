# Structural Stability Beyond Surface Correctness

## A Minimal Reproducible Demonstration of OMNIA

**Repository:** OMNIA-MINIMAL  
**Author:** Massimiliano Brighindi  
**Ecosystem:** MB-X.01 / L.O.N. / OMNIA  

---

## Abstract

Most evaluation pipelines ask whether an output is correct.

OMNIA-MINIMAL demonstrates a narrower but important distinction:

    correctness is not structural stability

An output may pass a surface correctness check in one form while becoming unstable under independent transformations of the same underlying task.

This repository provides a minimal deterministic demonstration of that gap.

The demonstration is intentionally small.

It does not claim universal validity.

It does not claim semantic truth.

It does not replace human judgment.

It shows that a post-hoc measurement layer can detect structural fragility that a single correctness check may miss.

---

## 1. Problem

A standard evaluation usually asks:

    Is the answer correct?

This is useful but incomplete.

A result may be correct in one surface form but unstable across transformed forms of the same underlying structure.

For example, a model may answer a base arithmetic question correctly, then fail when the quantities are reordered, rephrased, or represented through an equivalent surface form.

That failure is not merely a wrong answer.

It is evidence of structural fragility.

The problem is therefore:

    surface correctness does not necessarily imply structural stability

---

## 2. Central Claim

OMNIA-MINIMAL demonstrates one falsifiable claim:

    correctness is not structural stability

The claim is deliberately narrow.

It does not say:

    stability equals truth

It does not say:

    instability equals falsehood

It says:

    the two measurements can diverge

This divergence can be observed, measured, reproduced, and tested.

---

## 3. Boundary

OMNIA-MINIMAL follows the OMNIA boundary:

    measurement != inference != decision

The repository does not infer meaning.

It does not decide truth.

It does not decide whether an output should be trusted.

It measures structural behavior after an output has already been produced.

The output of the demo is a signal.

It is not a verdict.

---

## 4. Method

The minimal method is:

    case
    independent transformations
    surface correctness check
    structural comparison
    stability signal

Each case group contains:

    one base task
    one or more transformed variants
    expected answers
    observed model answers

The runner compares the answers across variants and emits one of three bounded signals:

    STABLE
    FRAGILE
    DIVERGENT

---

## 5. Minimal Experiment

The experiment contains three deterministic case groups.

### 5.1 Stable case

The base answer is correct.

All transformed variants are also correct.

All observed answers remain compatible.

Expected signal:

    STABLE

### 5.2 Fragile case

The base answer is correct.

At least one transformed variant becomes incorrect or incompatible.

Expected signal:

    FRAGILE

This is the most important case because it demonstrates the core claim:

    surface correctness can pass while structural stability fails

### 5.3 Divergent case

The base answer is already incorrect or the group shows direct incompatibility.

Expected signal:

    DIVERGENT

---

## 6. Minimal Metrics

The demo computes a small pedagogical metric set.

These are not the full OMNIA engine.

They are minimal signals designed to make the central distinction visible.

### base_surface_correct

Whether the base variant answer matches the expected answer.

### all_surface_correct

Whether every variant answer matches its expected answer.

### omega

The fraction of variants compatible with the expected answer.

For this minimal demo:

    omega = correct_variants / total_variants

### delta_omega

The loss from perfect compatibility.

For this minimal demo:

    delta_omega = 1 - omega

### answer_variance

The number of distinct answer forms beyond a single stable answer.

For this minimal demo:

    answer_variance = distinct_answers - 1

### structural_signal

The bounded output signal:

    STABLE
    FRAGILE
    DIVERGENT

---

## 7. Results

The current deterministic demo produces:

    arithmetic_stable_001
    base_surface_correct: true
    all_surface_correct: true
    omega: 1.0
    delta_omega: 0.0
    structural_signal: STABLE

    arithmetic_fragile_001
    base_surface_correct: true
    all_surface_correct: false
    omega: 0.666667
    delta_omega: 0.333333
    structural_signal: FRAGILE

    arithmetic_divergent_001
    base_surface_correct: false
    all_surface_correct: false
    omega: 0.333333
    delta_omega: 0.666667
    structural_signal: DIVERGENT

The key result is:

    arithmetic_fragile_001

because the base case passes surface correctness while the transformed group fails structural stability.

---

## 8. Interpretation

The fragile case shows that there is a measurable gap between:

    getting one answer right

and:

    remaining compatible across transformed versions of the same task

That gap is the minimal OMNIA object of measurement.

The result should not be overstated.

It does not prove a universal theory.

It does not prove that OMNIA captures all forms of robustness.

It proves only that the distinction is operationally demonstrable.

---

## 9. Failure Conditions

The claim would weaken or fail under the following conditions:

1. If surface correctness and structural stability always collapsed into the same measurement.
2. If transformed variants were not genuinely related to the same underlying task.
3. If the signal depended on hidden semantic interpretation rather than explicit comparison.
4. If the demo could not be reproduced.
5. If every failure were manually explained away instead of being included in the result set.

OMNIA-MINIMAL is designed to avoid these problems by using explicit expected answers, explicit observed answers, deterministic scripts, and public CI execution.

---

## 10. Reproducibility

The repository can be reproduced locally with:

    python examples/run_minimal_demo.py
    pytest -q

It is also continuously checked through GitHub Actions.

The CI workflow runs on:

    push to main
    pull request to main
    manual workflow dispatch

This makes the repository more than a static explanation.

It is an executable minimal validation loop.

---

## 11. Ecosystem Position

OMNIA-MINIMAL is not the full OMNIA ecosystem.

It is the smallest reproducible doorway into it.

The larger ecosystem includes:

    lon-mirror
    OMNIABASE
    OMNIA
    omnia-limit
    OMNIA-RADAR
    OMNIA-SECURITY
    OMNIA-CRYPTO
    OMNIAMIND
    OMNIA-THREE-BODY
    OMNIA-INVARIANCE
    OMNIA-CONSTANT
    OMNIA-VALIDATION

OMNIA-MINIMAL does not replace these repositories.

It gives a new reader the shortest possible path to the central idea.

---

## 12. Conclusion

The minimal conclusion is:

    correctness is not structural stability

OMNIA-MINIMAL demonstrates that this distinction can be made operational, measured post-hoc, tested locally, and verified automatically through CI.

The output is a signal.

Not a verdict.

The boundary remains:

    measurement != inference != decision
