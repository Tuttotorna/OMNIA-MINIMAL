# Reviewer Follow-up Note

## Proposed name

Structural Evaluation over Admissible Transformations

## Definition

Given:

- an input or task x;
- a model or system M;
- a family of admissible transformations T;
- an extractor Phi for task-relevant output properties;

we evaluate:

{ Phi(M(T(x))) | T in T }

rather than only:

Phi(M(x))

## Core metric

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

## Interpretation

Low dispersion -> structural stability under T.
High dispersion -> structural fragility under T.

## Main question

Is this already standard under another name, for example:

- prompt sensitivity;
- stochastic evaluation;
- invariance testing;
- robustness evaluation;
- metamorphic testing;
- representation sensitivity;
- measurement theory?

Or is there room for a broader formal framework that treats these as special cases of evaluation over admissible transformations?

<!-- METAMORPHIC_ALIGNMENT_REVIEWER_START -->

## Metamorphic testing alignment

The closest existing technical family appears to be metamorphic testing.

A reviewer may reasonably say:

This is related to metamorphic testing. The key is to define the metamorphic relation.

OMNIA-MINIMAL accepts this as the most natural technical placement.

The current compact formula is:

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

A more metamorphic-testing-oriented specialization is:

Fragility_{T,R,Phi}(M,x) = ViolationRate_R({ Phi(M(T_i(x))) | T_i in T })

Where:

- T is the family of admissible transformations.
- R is the expected compatibility relation or metamorphic relation.
- Phi extracts the task-relevant output property.
- ViolationRate_R measures how often the expected relation R is violated.

This means that admissible transformations alone are not enough.

A complete evaluation should specify:

1. what transformations are admissible;
2. what property is extracted from the output;
3. what relation should hold across the transformed outputs;
4. how dispersion or violation is measured.

The intended positioning is not:

OMNIA-MINIMAL invented metamorphic testing.

The intended positioning is:

OMNIA-MINIMAL provides a compact structural framing in which metamorphic testing, prompt sensitivity, invariance testing, robustness evaluation, and representation sensitivity can be read as related cases of evaluation over admissible transformations and expected compatibility relations.

<!-- METAMORPHIC_ALIGNMENT_REVIEWER_END -->
