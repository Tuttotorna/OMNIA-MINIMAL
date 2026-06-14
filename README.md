# OMNIA-MINIMAL


[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20691985.svg)](https://doi.org/10.5281/zenodo.20691985)

[![OMNIA-MINIMAL CI](https://github.com/Tuttotorna/OMNIA-MINIMAL/actions/workflows/minimal-demo.yml/badge.svg)](https://github.com/Tuttotorna/OMNIA-MINIMAL/actions/workflows/minimal-demo.yml)


**Correctness is not structural stability.**

OMNIA-MINIMAL is the minimal reproducible entry point into the OMNIA ecosystem.

It demonstrates one narrow claim:

> An output can pass surface correctness while failing structural stability under independent transformations.

OMNIA does not infer meaning.  
OMNIA does not decide truth.  
OMNIA does not replace human judgment.

OMNIA measures structural behavior after generation.

---


## Foundational Principle

OMNIA-MINIMAL is the minimal public demonstration of the L.O.N. Multi-Form Invariance Principle:

> No single form is sovereign.

In OMNIA-MINIMAL, this becomes:

> No first correctness is sovereign.

A response, result, or claim is not trusted because it appears correct once. It must preserve structural compatibility under simple, independent transformations of form.

OMNIA-MINIMAL exists to expose the smallest reproducible version of this claim:

> correctness once does not imply structural stability.

See:

- https://github.com/Tuttotorna/lon-mirror/tree/main/foundation

## The core problem

Most evaluations ask:

    Is the answer correct?

OMNIA asks a different post-hoc question:

    Does the structure remain stable when the task is transformed?

These are not the same question.

A result may be correct in one surface form and unstable across equivalent or near-equivalent transformations.

That gap is the object of measurement.

---

## Minimal pipeline

    case
    ↓
    independent transformations
    ↓
    surface correctness check
    ↓
    structural comparison
    ↓
    stability signal

The output is not a verdict.

The output is a signal.

---

## What this repository demonstrates

This repo includes a small deterministic demo.

It compares answers across transformed versions of the same underlying task.

It then emits a bounded structural signal:

    STABLE
    FRAGILE
    DIVERGENT

The demo is intentionally simple.

The point is not to prove a universal theory.

The point is to show the smallest reproducible version of the OMNIA claim:

    surface correctness != structural stability
    measurement != inference != decision

---

## Run the demo

    python examples/run_minimal_demo.py

Expected behavior:

    CASE: arithmetic_stable_001
    base_surface_correct: true
    structural_signal: STABLE

    CASE: arithmetic_fragile_001
    base_surface_correct: true
    structural_signal: FRAGILE

    CASE: arithmetic_divergent_001
    base_surface_correct: false
    structural_signal: DIVERGENT

---

## What OMNIA is

OMNIA is a post-hoc structural measurement framework.

It is:

- model-agnostic
- post-hoc
- bounded
- reproducible
- falsifiable
- decision-external

It measures structural behavior after an output has been produced.

---

## What OMNIA is not

OMNIA is not:

- an AI model
- a truth oracle
- a consciousness system
- a semantic judge
- a replacement for human decision
- a universal proof engine

---

## Boundary

A stable structure is not automatically true.

An unstable structure is not automatically false.

Stability is a signal.

Not a verdict.

---

## Ecosystem

OMNIA-MINIMAL is not the full OMNIA ecosystem.

It is the smallest reproducible doorway into it.

See:

    ECOSYSTEM_MAP.md

for the linked repositories.

---

## DOI

OMNIA-MINIMAL is archived on Zenodo.

DOI:

    10.5281/zenodo.20338347

DOI link:

    https://doi.org/10.5281/zenodo.20338347

Zenodo record:

    https://zenodo.org/records/20338347

Recommended citation:

    Brighindi, Massimiliano. OMNIA-MINIMAL: Structural Stability Beyond Surface Correctness. Zenodo. https://doi.org/10.5281/zenodo.20338347


---

## Citation and archiving

OMNIA-MINIMAL is release-ready and citation-ready.

Citation metadata:

- [CITATION.cff](CITATION.cff)

Release notes:

- [RELEASE_NOTES.md](RELEASE_NOTES.md)

Archiving metadata:

- [.zenodo.json](.zenodo.json)

Release checklist:

- [docs/RELEASE_CHECKLIST.md](docs/RELEASE_CHECKLIST.md)

Citation and archiving notes:

- [docs/CITATION_AND_ARCHIVING.md](docs/CITATION_AND_ARCHIVING.md)

Boundary:

    measurement != inference != decision


---

## Clickable ecosystem navigation

OMNIA-MINIMAL now includes a clickable reading path into the wider OMNIA ecosystem.

Start here:

- [docs/WHAT_TO_READ_NEXT.md](docs/WHAT_TO_READ_NEXT.md)
- [docs/ECOSYSTEM_READING_PATH.md](docs/ECOSYSTEM_READING_PATH.md)
- [docs/CLICKABLE_ECOSYSTEM_INDEX.md](docs/CLICKABLE_ECOSYSTEM_INDEX.md)

These files do not only list repositories.

They provide clickable links to the relevant repositories, browsable trees, and verified files when available.


---

## Extended minimal dataset

The repository now includes a slightly stronger minimal dataset.

It covers:

    arithmetic variation
    symbolic reordering
    paraphrase stability
    distractor clauses
    representation change

The goal is not scale.

The goal is to show that the FRAGILE signal is not a single isolated example.

See:

    docs/CASE_CATALOG.md
    docs/EXTENDED_RESULTS.md
    docs/EXTENDED_MINIMAL_DATASET.md

---

## Minimal paper

A paper-style explanation of the repository is available here:

    docs/MINIMAL_PAPER.md

It defines:

    Abstract
    Problem
    Claim
    Method
    Minimal Experiment
    Results
    Boundaries
    Failure Conditions
    Reproducibility

The paper keeps the claim deliberately narrow:

    Correctness is not structural stability.

---

## Continuous validation

This repository includes a GitHub Actions workflow.

Every push runs:

    python examples/run_minimal_demo.py
    pytest -q

The demo is therefore not only documented.

It is automatically checked.

See:

    .github/workflows/minimal-demo.yml

<!-- OMNIA_STRUCTURAL_EVALUATION_THRESHOLD -->

## Technical threshold: Structural Evaluation over Admissible Transformations

OMNIA-MINIMAL is now narrowed to one testable threshold object:

single-form correctness is not structural stability.

Operational formula:

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

Meaning:

A system should not be evaluated only on one observed form.
It should be evaluated across admissible transformations that change the form while preserving the task-relevant core.

Low dispersion means structural stability.
High dispersion means structural fragility.

Key documents:

- docs/STRUCTURAL_EVALUATION_OVER_ADMISSIBLE_TRANSFORMATIONS.md
- docs/TECHNICAL_NOTE_ADMISSIBLE_TRANSFORMATIONS.md
- docs/REVIEWER_FOLLOWUP_NOTE.md
- examples/admissible_transformations_demo.py
- data/admissible_transformation_cases.jsonl
- results/structural_evaluation_results.md

Boundary:

OMNIA-MINIMAL does not decide truth, intelligence, or final reliability.
It measures output compatibility across admissible transformations.

<!-- OMNIA_ZENODO_CITATION_BLOCK_START -->

## Citation and archival

This repository is prepared for GitHub-Zenodo archival.

Repository:
https://github.com/Tuttotorna/OMNIA-MINIMAL

Latest GitHub release: v0.6.2 (https://github.com/Tuttotorna/OMNIA-MINIMAL/releases/tag/v0.6.2)

Detected Zenodo DOI(s):
- https://doi.org/10.5281/zenodo.20338347

Metadata files used for archival/citation:

- .zenodo.json
- CITATION.cff

Zenodo note:

GitHub-Zenodo archiving works after the repository is enabled in Zenodo GitHub settings and a GitHub release is created.

<!-- OMNIA_ZENODO_CITATION_BLOCK_END -->

<!-- ZENODO_REMAINING_REPAIR_BLOCK_START -->

## Zenodo repair / archival metadata

This repository has been updated with clean Zenodo and citation metadata.

Repository:
https://github.com/Tuttotorna/OMNIA-MINIMAL

Repair release tag:
zenodo-repair-remaining-20260613-070535-omnia-minimal

Metadata files:

- .zenodo.json
- CITATION.cff

Purpose:

- provide clean GitHub-Zenodo archival metadata;
- provide a valid citation file;
- trigger a fresh GitHub release for Zenodo processing;
- reduce risk from old failed or incomplete Zenodo release attempts.

Important note:

Old failed Zenodo attempts may remain visible in Zenodo history.
The relevant state is whether the newest repair release becomes Published.

<!-- ZENODO_REMAINING_REPAIR_BLOCK_END -->

<!-- OMNIA_METAMORPHIC_ALIGNMENT_START -->

## Relation to metamorphic testing

The closest existing technical family for OMNIA-MINIMAL appears to be metamorphic testing.

OMNIA-MINIMAL does not claim to replace metamorphic testing.

The current structural formula is:

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

A more metamorphic-testing-oriented specialization is:

Fragility_{T,R,Phi}(M,x) = ViolationRate_R({ Phi(M(T_i(x))) | T_i in T })

Meaning:

- T = admissible transformations;
- Phi = task-relevant output property extractor;
- R = expected compatibility relation or metamorphic relation;
- ViolationRate_R = rate of violation of the expected relation.

This alignment is important because admissible transformations alone are not enough.

A complete evaluation should define:

1. the transformation family;
2. the extracted property;
3. the expected compatibility relation;
4. the dispersion or violation metric.

New alignment document:

- docs/METAMORPHIC_TESTING_ALIGNMENT.md

Safe positioning:

OMNIA-MINIMAL is a structural framing of evaluation over admissible transformations and expected compatibility relations.

Metamorphic testing is the closest existing family.

Prompt sensitivity, invariance testing, robustness evaluation, and representation sensitivity can be read as related cases when they evaluate compatibility across controlled transformations.

<!-- OMNIA_METAMORPHIC_ALIGNMENT_END -->
