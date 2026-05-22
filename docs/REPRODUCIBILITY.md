# Reproducibility

OMNIA-MINIMAL is designed to be executable and verifiable.

It is not only a conceptual README.

It contains:

    data
    runner
    results
    tests
    CI workflow

---

## Local reproduction

Clone the repository:

    git clone https://github.com/Tuttotorna/OMNIA-MINIMAL.git
    cd OMNIA-MINIMAL

Run the demo:

    python examples/run_minimal_demo.py

Run the tests:

    pytest -q

Expected test result:

    2 passed

---

## Expected demo signals

The demo should emit three case groups:

    arithmetic_stable_001
    arithmetic_fragile_001
    arithmetic_divergent_001

Expected signals:

    STABLE
    FRAGILE
    DIVERGENT

The most important signal is:

    FRAGILE

because it shows the central distinction:

    base_surface_correct: true
    all_surface_correct: false

This means that the base case passed, but the transformed group did not remain structurally stable.

---

## Continuous validation

The repository includes GitHub Actions.

The workflow file is:

    .github/workflows/minimal-demo.yml

It runs:

    python examples/run_minimal_demo.py
    pytest -q

The workflow verifies that the minimal demonstration remains executable.

---

## Boundary

Reproducibility does not prove universal validity.

It proves that the minimal demonstration can be executed and checked.

That is the correct scientific boundary.

    reproducible demo
    not universal proof
