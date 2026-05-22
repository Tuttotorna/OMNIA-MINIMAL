# Validation Protocol

## Purpose

This protocol defines the minimal reproducible OMNIA demonstration.

The goal is not to validate the entire ecosystem.

The goal is to demonstrate one falsifiable claim:

    surface correctness != structural stability

---

## Input

The input is a JSONL file:

    data/minimal_cases.jsonl

Each row contains:

    case_group
    variant_id
    variant_type
    task
    expected_answer
    model_answer

A case_group contains one base task and one or more transformed variants.

---

## Measurement

For each case group, the runner computes:

    base_surface_correct
    all_surface_correct
    answer_variance
    omega
    delta_omega
    structural_signal

These are minimal demonstration metrics.

They are not the full OMNIA engine.

They are a small pedagogical measurement layer.

---

## Signals

STABLE:

The transformed outputs remain compatible.

FRAGILE:

The base answer may be correct, but transformed variants become inconsistent.

DIVERGENT:

The group shows direct correctness failure or strong incompatibility.

---

## Falsifiability

The claim fails if surface correctness and structural stability always collapse into the same measurement.

The claim is supported when cases exist where surface correctness passes while structural stability fails.
