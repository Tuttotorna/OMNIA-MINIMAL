# Extended Minimal Dataset

This document explains why v0.4 adds more cases.

The original repository had three groups:

    STABLE
    FRAGILE
    DIVERGENT

That was enough to demonstrate the core distinction.

However, a single fragile case can look accidental.

v0.4 adds more fragile cases across different transformation families.

The goal is not size.

The goal is signal diversity.

---

## Added families

### Symbolic reordering

A symbolic relation is preserved while variable order changes.

### Distractor clause

Irrelevant information is added without changing the expected answer.

### Representation change

The surface representation changes while the underlying quantity remains fixed.

### Stable paraphrase

A stable paraphrase case is included to avoid claiming that all transformations are fragile.

---

## Correct interpretation

The extended dataset shows:

    fragile behavior can appear across multiple transformation families

It does not show:

    OMNIA is universally validated

The boundary remains:

    measurement != inference != decision
