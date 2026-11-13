# Baseline validation checklist

## Source artifact provenance
- [ ] Original project's archive URL and immutable version ID
- [ ] Paper/manuscript URL, if independently accessible
- [ ] Simulator, robotics framework and Python versions
- [ ] Training dataset metadata, checksums, episode splits
- [ ] Checkpoint source, architecture, processor/normalization metadata
- [ ] Baseline evaluation command, number of episodes, seeds, success definition
- [ ] Reproduction license/attribution

## Compatibility checks
- [ ] Camera names, order, resolution and RGB/depth representation
- [ ] Joint or EEF state dimension, order, units, reference frame
- [ ] Action dimension, order, absolute vs delta, control frequency
- [ ] Text instruction and tokenizer preprocessing
- [ ] Action chunk length and real-time control loop
- [ ] Training and evaluation metadata and dependency versions

## Evaluation outcomes
- [ ] Sim import and single rollout without model
- [ ] Original pretrained policy loads
- [ ] Fixed evaluation set baseline reproduced with per-stage success breakdown
- [ ] OOD conditions and recovery criteria defined before extensions
