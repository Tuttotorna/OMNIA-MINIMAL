# Release Notes

## v0.6.0

### Title

OMNIA-MINIMAL: Structural Stability Beyond Surface Correctness

---

## Summary

This release turns OMNIA-MINIMAL into a citable, release-ready, Zenodo-ready minimal research object.

The repository demonstrates one narrow claim:

    correctness is not structural stability

An output can pass surface correctness while failing structural stability under independent transformations.

---

## What is included

This release includes:

    minimal deterministic demo
    extended minimal dataset
    STABLE / FRAGILE / DIVERGENT signals
    pytest regression tests
    GitHub Actions CI
    paper-style documentation
    failure conditions
    reproducibility notes
    clickable ecosystem navigation
    citation metadata
    Zenodo metadata

---

## Current verified signals

The demo currently emits:

    STABLE
    FRAGILE
    DIVERGENT

The key cases are the FRAGILE cases, where the base answer is correct but transformed variants reveal instability.

---

## Reproducibility

Run locally:

    python examples/run_minimal_demo.py
    pytest -q

Expected test result:

    4 passed

The GitHub Actions workflow also runs the demo and tests automatically.

---

## Boundary

This release does not claim universal validity.

It does not claim semantic truth.

It does not claim that stability equals truth.

It does not claim that instability equals falsehood.

The boundary remains:

    measurement != inference != decision

The output is a signal.

Not a verdict.

---

## Recommended citation

Use the repository citation metadata:

    CITATION.cff

For archival platforms such as Zenodo, use:

    .zenodo.json

---

## Repository

https://github.com/Tuttotorna/OMNIA-MINIMAL
