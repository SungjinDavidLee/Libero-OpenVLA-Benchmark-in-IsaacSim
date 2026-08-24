# LIBERO-Spatial Benchmark Report

## Overview

OpenVLA was evaluated with the LIBERO-Spatial fine-tuned checkpoint on the ten tasks in the LIBERO-Spatial suite. Each task was evaluated for 50 trials with seed 7.

## Evaluation protocol

- Checkpoint: openvla/openvla-7b-finetuned-libero-spatial
- Task suite: libero_spatial
- Trials: 50 per task, 500 total
- Maximum horizon: 220 policy steps
- Initial state: LIBERO task initial states
- Image resolution: 256
- Center crop: enabled
- Policy input: RGB observation and task instruction

## Aggregate result

![Official and current result](../figures/official_vs_current.png)

The evaluation produced 422 successful episodes out of 500, corresponding to an overall success rate of 84.4%. All 78 failed episodes terminated by timeout. No runtime error was recorded in the task logs.

## Task-wise result

![Task-wise success rate](../figures/success_rate_by_task.png)

![Mean policy steps](../figures/mean_policy_steps_by_task.png)

![Success rate and policy horizon](../figures/success_vs_mean_steps.png)

Task 0 achieved the highest success rate at 98%. Task 4 achieved the lowest success rate at 68% and also had the largest mean policy horizon at 156.04 steps. Task 8 and Task 9 achieved 74% and 76%, respectively.

The task-wise values are stored in [task_results.csv](../results/libero_spatial/openvla_7b_finetuned/seed_7/task_results.csv). The JSON summaries and logs are stored in the same seed directory.

## Comparison with the official result

The official OpenVLA report gives 84.7 ± 0.9% for LIBERO-Spatial, averaged over three random seeds. The present result is 84.4% for seed 7. The difference is 0.3 percentage points and should not be interpreted as a model difference because the current measurement is not a three-seed average.

## Interpretation

Lower task success is associated with longer action horizons in this ten-task comparison. This observation is exploratory because task geometry, object arrangement, and motion constraints vary simultaneously.

Task 4 is the clearest constrained-grasp case. The target bowl is located inside a cabinet drawer, where the drawer boundary and partial occlusion restrict the available approach and lift configurations. The result is not explained by target–distractor distance alone: Task 0 also places the bowl between nearby objects but reaches 98%.

## Limitations

- The result represents one random seed.
- The ten tasks do not isolate individual geometric factors.
- The reported failure analysis uses representative Task 4 trajectories rather than all failed episodes.
- The current release reports native LIBERO performance; transfer results in Isaac Sim or on a real Franka require a separate evaluation protocol.

## References

- [OpenVLA official README](https://github.com/openvla/openvla)
- [OpenVLA LIBERO evaluator](https://github.com/openvla/openvla/blob/main/experiments/robot/libero/run_libero_eval.py)
- [LIBERO repository](https://github.com/Lifelong-Robot-Learning/LIBERO)
