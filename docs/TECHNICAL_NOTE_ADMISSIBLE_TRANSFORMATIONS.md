# Technical Note: Evaluation over Admissible Transformations

## Purpose

This note narrows OMNIA-MINIMAL into one testable threshold object:

structural stability under admissible transformations.

The goal is not to present OMNIA as a total theory.
The goal is to define a measurable evaluation object.

## Problem

Many evaluations observe one form:

M(x)

But if the object is representation-sensitive, a single observed output can be misleading.

A model may appear correct under x and fail under T(x), even when T preserves the task-relevant core.

Therefore:

single-form correctness is not structural stability.

## Definitions

Input:

x

An observed input, task, object, problem, or case.

Model or system:

M

The system being evaluated.

Admissible transformation family:

T = {T_1, T_2, ..., T_n}

Each T_i changes the observable form of x while preserving the relevant task core.

Output family:

O_T(M, x) = { M(T_i(x)) | T_i in T }

Extractor:

Phi

A function that extracts the task-relevant property from each output.

Examples:

- numerical answer;
- classification label;
- ranking;
- decision-relevant constraint;
- safety-relevant property;
- invariant relation.

Structural signal family:

Y_T(M, x) = { Phi(M(T_i(x))) | T_i in T }

Dispersion:

Dispersion(Y_T)

A measure of how much the extracted task-relevant properties diverge across admissible transformations.

Structural stability:

Low dispersion = structural stability.

Structural fragility:

High dispersion = structural fragility.

## Operational formula

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

## Compatibility is not identity

These outputs are compatible:

5
There are 5 balls.
The box contains five balls.

These outputs are not compatible:

5
6
There are four balls.

## Minimal example

Original task:

A box contains 3 red balls and 2 blue balls.
How many balls are in the box?

Admissible variants:

A box contains 2 blue balls and 3 red balls.
How many balls are in the box?

There are 3 red balls and 2 blue balls in a box.
What is the total number of balls?

A box contains 3 red balls and 2 blue balls.
The box is made of wood.
How many balls are in the box?

Expected compatible structure:

5

If a system outputs:

5, 5, 6

then the issue is not only one wrong answer.
It is a fragility under an admissible transformation family.

## Boundary

OMNIA-MINIMAL does not claim semantic truth, model intelligence, moral correctness, final decision authority, or general robustness in all possible conditions.

It measures a narrower property:

compatibility of task-relevant output properties under admissible transformations.

## Reviewer-facing question

Can this formulation be understood as a generalization of prompt sensitivity evaluation, where prompt variants are one class of admissible transformations?

If not, under which existing mathematical or evaluation framework should it be placed?

## Minimal contribution

The contribution is not the claim that prompt sensitivity exists.

The contribution is the broader framing:

single-form evaluation should be replaced, where relevant, by evaluation over admissible transformation families.
