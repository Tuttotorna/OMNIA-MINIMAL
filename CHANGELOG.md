# Changelog


## v0.3.0

Added paper-style research framing.

### Added

- `docs/MINIMAL_PAPER.md`
- `docs/FAILURE_CONDITIONS.md`
- `docs/REPRODUCIBILITY.md`
- `docs/ABSTRACT.md`
- README link to the minimal paper.

### Purpose

This version makes OMNIA-MINIMAL readable as a minimal falsifiable research object.

The claim remains narrow:

    Correctness is not structural stability.

The boundary remains unchanged:

    measurement != inference != decision


## v0.2.0

Added automated reproducibility layer.

### Added

- GitHub Actions CI workflow.
- Automatic execution of `examples/run_minimal_demo.py`.
- Automatic pytest validation.
- README CI badge.
- Explicit version history.

### Purpose

The repository is no longer only a static explanation.

It now contains an automatically executed minimal validation loop:

    data
    demo runner
    result generation
    tests
    CI verification

This strengthens the central claim:

    Correctness is not structural stability.

## v0.1.0

Initial OMNIA-MINIMAL release.

### Added

- Minimal deterministic demo.
- Stable / fragile / divergent cases.
- Structural measurement boundary.
- Ecosystem map.
- Validation protocol.
- Reproducible test suite.
