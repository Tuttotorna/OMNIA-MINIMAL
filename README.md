# OMNIA-MINIMAL

**Correctness is not structural stability.**

OMNIA-MINIMAL is the minimal reproducible entry point into the OMNIA ecosystem.

It demonstrates one narrow claim:

> An output can pass surface correctness while failing structural stability under independent transformations.

OMNIA does not infer meaning.  
OMNIA does not decide truth.  
OMNIA does not replace human judgment.

OMNIA measures structural behavior after generation.

---

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
