# Metamorphic Testing Alignment

## Purpose

This note aligns OMNIA-MINIMAL with the closest existing technical family:

metamorphic testing.

The goal is not to claim that OMNIA-MINIMAL replaces metamorphic testing.

The goal is to clarify that structural evaluation over admissible transformations can be read as a compact framing that connects:

- metamorphic testing;
- prompt sensitivity evaluation;
- invariance testing;
- robustness evaluation;
- representation sensitivity;
- structural stability measurement.

## Closest existing family

Metamorphic testing appears to be the closest existing technical family.

In metamorphic testing, the central idea is not to rely only on one input-output pair.

Instead, one defines related inputs and expected relations between their outputs.

This is especially useful when a traditional oracle is difficult, expensive, incomplete, or unavailable.

OMNIA-MINIMAL uses different wording, but the structural proximity is clear.

## Current OMNIA-MINIMAL formula

The current compact formula is:

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

Where:

- x is the input, task, object, case, or observed system.
- M is the model or system being evaluated.
- T is a family of admissible transformations.
- T(x) is the same task observed through a changed form.
- Phi extracts the task-relevant property from the output.
- Dispersion measures whether extracted properties remain compatible or diverge.

## Metamorphic-testing specialization

When an expected relation is explicit, the formula can be specialized as:

Fragility_{T,R,Phi}(M,x) = ViolationRate_R({ Phi(M(T_i(x))) | T_i in T })

Where:

- T is the family of admissible transformations.
- R is the expected compatibility relation or metamorphic relation.
- Phi extracts the task-relevant output property.
- ViolationRate_R measures how often the expected relation R is violated.

## Interpretation

The original dispersion formula is useful when compatibility is measured as spread, disagreement, or inconsistency.

The metamorphic relation formula is useful when the expected relation is explicit.

So:

Dispersion can be read as a general instability signal.

ViolationRate_R can be read as a metamorphic-testing specialization.

## Why R matters

Admissible transformations alone are not enough.

A complete structural evaluation should specify:

1. the transformation family T;
2. the extracted property Phi;
3. the expected compatibility relation R;
4. the violation or dispersion metric.

Without R, the framework risks being too broad.

With R, it becomes closer to executable metamorphic testing.

## Example

Original task:

A box contains 3 red balls and 2 blue balls. How many balls are in the box?

Admissible transformation:

A box contains 2 blue balls and 3 red balls. How many balls are in the box?

Extracted property:

Phi = numerical answer.

Expected relation:

R = equality of the extracted numerical answer.

Expected result:

Both outputs should preserve the same extracted answer: 5.

If the outputs are 5 and 6, the expected relation is violated.

This is not merely one wrong answer.

It is structural fragility under an admissible transformation.

## Boundary

OMNIA-MINIMAL does not claim that metamorphic testing is new.

OMNIA-MINIMAL does not claim to replace metamorphic testing.

OMNIA-MINIMAL does not claim to decide truth, intelligence, or final reliability.

The narrower proposal is:

single-form evaluation can mistake local correctness for structural stability.

The technical framing is:

evaluate task-relevant properties across admissible transformations and expected compatibility relations.

## Proposed positioning

The safest positioning is:

OMNIA-MINIMAL is a structural framing of evaluation over admissible transformations.

Metamorphic testing is the closest existing technical family.

Prompt sensitivity, invariance testing, robustness evaluation, and representation sensitivity can be treated as related cases when they evaluate compatibility across controlled transformations.

## Reviewer-facing question

Is this formulation already fully captured by metamorphic testing?

Or is it useful as a compact structural language connecting metamorphic testing, prompt sensitivity, invariance, robustness, and representation sensitivity?

## Minimal contribution

The possible contribution is not the discovery of input transformations.

The possible contribution is the compression:

single-form correctness is not structural stability.

and the common grammar:

admissible transformations -> extracted properties -> expected compatibility relations -> dispersion or violation -> fragility signal.
