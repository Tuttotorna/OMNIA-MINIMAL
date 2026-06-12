# Structural Evaluation over Admissible Transformations

## One-line claim

Single-form evaluation can mistake local correctness for structural stability.

## Core formula

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

Where:

- x is the input, task, object, case, or observed system.
- M is the model or system being evaluated.
- T is a family of admissible transformations.
- T(x) is the same task observed through a changed form.
- Phi extracts the task-relevant property from the output.
- Dispersion measures whether extracted properties remain compatible or diverge.

## Human version

A single form is not enough.

Change the form.
Keep what remains compatible.
That is the structure.

## Why this matters

A system can be correct in one observed form and still be fragile under controlled transformations.

A single answer is a point.
A family of transformed answers is a stability field.

## Admissible transformation

A transformation is admissible when it changes the observable form while preserving the relevant task core.

Example:

Original:
A box contains 3 red balls and 2 blue balls.
How many balls are in the box?

Admissible transformation:
A box contains 2 blue balls and 3 red balls.
How many balls are in the box?

The order changes.
The task core does not change.
The answer must remain compatible: 5.

Non-admissible transformation:

A box contains 3 red balls and 4 blue balls.
How many balls are in the box?

This changes the task core.
It is not a transformation of form.
It is a different task.

## Boundary

This does not claim truth.
This does not replace human judgment.
This does not decide.
This does not certify intelligence.

It only measures whether a task-relevant structure remains compatible when the form changes.

## Relation to existing work

In AI evaluation, this connects naturally to:

- prompt sensitivity;
- meaning-preserving perturbations;
- stochastic evaluation;
- robustness testing;
- invariance testing;
- reliability under distributional variation.

The broader proposal is that prompt variants are one class of admissible transformations.

## Reviewer question

Is evaluation over admissible transformations already fully captured under an existing framework?

Or is there room for a broader structural-evaluation formulation connecting prompt sensitivity, invariance, robustness, and stability?

## Compact definition

Structural evaluation is the measurement of output compatibility across admissible transformations of the same task.
