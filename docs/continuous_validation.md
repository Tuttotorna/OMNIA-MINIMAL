# Continuous Validation

OMNIA-MINIMAL includes a GitHub Actions workflow.

The workflow runs automatically on:

- every push to `main`
- every pull request to `main`
- manual workflow dispatch

It executes:

    python examples/run_minimal_demo.py
    pytest -q

This means the minimal demonstration is not only described.

It is continuously checked.

---

## Why this matters

The repository claims:

    Correctness is not structural stability.

The CI does not prove the full OMNIA ecosystem.

It proves that the minimal demonstration remains executable and reproducible.

This is the correct boundary:

    reproducible demo
    not universal proof
