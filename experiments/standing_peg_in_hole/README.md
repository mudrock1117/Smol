# Standing Peg-in-Hole — SmolVLA reproduction

This experiment is isolated on branch `experiments/standing-peg-in-hole`; the original `main` branch remains unchanged.

## Objective

Reproduce the published Standing Peg-in-Hole baseline (simulation / dataset / fixed evaluation episodes) using the existing LeRobot and SmolVLA implementation, **before** introducing geometry awareness or recovery-guided changes.

## Reproduction gates

1. **Provenance and baseline:** obtain the original paper/reproduction archive, record exact versions, file checksums, observation and action definitions, train/validation/test split, checkpoints, metrics and evaluation seeds.
2. **Data audit:** inspect the demonstration dataset and verify mapping into `LeRobotDataset` without silently changing camera views, coordinate frames, units, action semantics, or episode boundaries.
3. **Offline baseline:** load original SmolVLA checkpoint with the appropriate policy processor, verify feature shapes / normalization and measure held-out data metrics.
4. **Simulation:** run the original environment and fixed-episode evaluation, confirm exact success conditions; compare with reported original baseline.
5. **Extensions (only after baseline):** stage-aware diagnostics, geometry-aware correction, failure recovery data, and OOD tests; conduct controlled ablations.

## Existing LeRobot entry points

- Model: `src/lerobot/policies/smolvla/`
- Dataset: `src/lerobot/datasets/lerobot_dataset.py`
- Training: `src/lerobot/scripts/lerobot_train.py`
- Evaluation: `src/lerobot/scripts/lerobot_eval.py`
- Environment plugins: `src/lerobot/envs/`

**No assumption is made that the external simulation can run in this repository unchanged.** Check the original simulator requirements separately before adding an environment adapter.

## Storage and reproducibility

Keep datasets, model checkpoints and simulation caches outside Git, on the designated data volume; never commit pretrained weights, large recordings or private files. Log each run's Git commit, dependency versions, seed, checkpoint hash, dataset identifier and evaluation protocol. Keep all initial implementation in this experiment directory rather than editing the SmolVLA backbone.
