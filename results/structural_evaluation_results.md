# Structural Evaluation Demo Results

Formula:

Fragility_T(M, x) = Dispersion({ Phi(M(T(x))) | T in T })

| Case | Expected Core | Extracted Values | Dispersion | Classification |
|---|---:|---|---:|---|
| stable_ball_count | 5 | ['5', '5', '5'] | 0.000 | STABLE |
| fragile_ball_count | 5 | ['5', '5', '6'] | 0.667 | FRAGILE |
| format_stable_sum | 12 | ['12', '12', '12'] | 0.000 | STABLE |

Interpretation:

- STABLE: admissible transformations preserved the task-relevant structure.
- FRAGILE: at least one admissible transformation produced an incompatible output.
- DIVERGENT: outputs are broadly incompatible across the transformed family.

Boundary:

This demo does not decide truth, intelligence, or final reliability.
It only measures compatibility of extracted task-relevant properties across admissible transformations.
