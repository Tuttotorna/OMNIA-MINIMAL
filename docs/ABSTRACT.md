# Abstract

OMNIA-MINIMAL demonstrates a narrow distinction:

    correctness is not structural stability

A generated output may pass a surface correctness check in one version of a task while failing across transformed versions of the same underlying task.

The repository provides a deterministic post-hoc measurement demo that emits three bounded signals:

    STABLE
    FRAGILE
    DIVERGENT

The central case is FRAGILE: the base answer is correct, but transformed variants reveal instability.

OMNIA-MINIMAL does not infer meaning.

It does not decide truth.

It does not replace human judgment.

It measures structural behavior after generation.

Boundary:

    measurement != inference != decision
