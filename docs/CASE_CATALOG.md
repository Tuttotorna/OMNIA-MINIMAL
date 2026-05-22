# Case Catalog

OMNIA-MINIMAL now contains a slightly stronger minimal dataset.

The goal is not scale.

The goal is to show that the fragile signal is not limited to a single toy example.

The dataset remains small, deterministic, readable, and falsifiable.

---

## Signals

The runner emits three bounded signals:

    STABLE
    FRAGILE
    DIVERGENT

The central signal is:

    FRAGILE

because it shows the gap between surface correctness and structural stability.

---

## Current case groups

### arithmetic_stable_001

Type:

    arithmetic

Expected signal:

    STABLE

Purpose:

    Demonstrates a fully compatible transformed group.

---

### arithmetic_fragile_001

Type:

    arithmetic order variation

Expected signal:

    FRAGILE

Purpose:

    Demonstrates that the base answer can be correct while a transformed variant fails.

---

### arithmetic_divergent_001

Type:

    arithmetic direct failure

Expected signal:

    DIVERGENT

Purpose:

    Demonstrates direct incompatibility when the base case already fails.

---

### symbolic_fragile_001

Type:

    symbolic variable reordering

Expected signal:

    FRAGILE

Purpose:

    Tests whether symbolic reordering preserves structural compatibility.

---

### paraphrase_stable_001

Type:

    paraphrase stability

Expected signal:

    STABLE

Purpose:

    Demonstrates that not every transformation is fragile.

---

### distractor_fragile_001

Type:

    distractor clause

Expected signal:

    FRAGILE

Purpose:

    Tests whether irrelevant information perturbs the output.

---

### representation_fragile_001

Type:

    representation change

Expected signal:

    FRAGILE

Purpose:

    Tests whether a change in representational surface causes structural instability.

---

## Boundary

These cases are not a universal benchmark.

They are minimal demonstration cases.

The correct interpretation is:

    structural fragility can appear even when the base answer is correct

The incorrect interpretation is:

    OMNIA proves semantic truth

OMNIA-MINIMAL does not prove truth.

It measures a bounded post-hoc structural signal.
