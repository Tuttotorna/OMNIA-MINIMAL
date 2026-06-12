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
