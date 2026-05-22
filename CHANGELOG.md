# Changelog


## v0.5.0

Added clickable ecosystem navigation.

### Added

- `docs/ECOSYSTEM_READING_PATH.md`
- `docs/CLICKABLE_ECOSYSTEM_INDEX.md`
- `docs/WHAT_TO_READ_NEXT.md`

### Purpose

This version turns OMNIA-MINIMAL into a real navigation layer.

It does not only list the other repositories.

It provides clickable paths to:

    local OMNIA-MINIMAL files
    linked ecosystem repositories
    browsable GitHub trees
    verified files when available

The claim remains narrow:

    Correctness is not structural stability.

The boundary remains unchanged:

    measurement != inference != decision



## v0.4.0

Added extended minimal dataset.

### Added

- Additional fragile cases across multiple transformation families.
- `symbolic_fragile_001`
- `paraphrase_stable_001`
- `distractor_fragile_001`
- `representation_fragile_001`
- `docs/CASE_CATALOG.md`
- `docs/EXTENDED_RESULTS.md`
- `docs/EXTENDED_MINIMAL_DATASET.md`
- `tests/test_extended_dataset.py`

### Purpose

This version strengthens the minimal demonstration without turning the repository into a large benchmark.

The aim is to show that the FRAGILE signal is not a single isolated case.

The claim remains narrow:

    Correctness is not structural stability.

The boundary remains unchanged:

    measurement != inference != decision



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
