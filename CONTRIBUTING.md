# Contributing

This is an educational portfolio project. Contributions should improve correctness, reproducibility, clarity, or responsible use.

## Before changing code
- Read the project README and methodology.
- Do not commit the Jigsaw dataset, raw comment exports, model checkpoints, or private evidence.
- Keep train/test separation intact.
- Do not report metrics without a reproducible run and clear evaluation settings.
- Keep severity categories explicitly described as project-defined heuristics.

## Suggested workflow
1. Create a branch for the change.
2. Make one focused change at a time.
3. Run the relevant unit tests.
4. Run affected notebook cells, then run the full notebook when feasible.
5. Update documentation if behaviour or limitations change.
6. Open a pull request describing the change and its validation.

## Reporting model results
Include the dataset version, split, seed, label threshold, per-label metrics, averaging method, and environment. Explain any missing or failed experiments.
