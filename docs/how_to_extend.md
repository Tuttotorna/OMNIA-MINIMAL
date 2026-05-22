# How To Extend

To extend OMNIA-MINIMAL, add more case groups to:

    data/minimal_cases.jsonl

Each group should include:

    base
    transform_1
    transform_2
    ...

Keep the expected answer explicit.

Keep the model answer explicit.

Do not hide failures.

Failures are part of the validation.

---

## Recommended extensions

1. Arithmetic perturbations
2. Symbolic reasoning perturbations
3. Paraphrase transformations
4. Representation changes
5. Multi-step reasoning variants
6. Adversarial but semantically equivalent variants

---

## Rule

Do not expand the theory before strengthening the validation.

The next step is not more language.

The next step is more falsifiable cases.
