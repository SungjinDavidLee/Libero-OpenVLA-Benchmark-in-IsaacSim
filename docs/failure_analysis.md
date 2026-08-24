# Task 4 Failure Analysis

## Task

Pick up the black bowl in the top drawer of the wooden cabinet and place it on the plate.

Task 4 result:

- Success: 34/50
- Failure: 16/50
- Success rate: 68%
- Mean policy steps: 156.04
- Failure termination: timeout at 220 steps

## Representative trajectories

![Task 4 success and failure](../figures/task4_failure_case.png)

The figure compares two representative episodes:

- Episode 000: success at 127 policy steps
- Episode 001: timeout at 220 policy steps
- Episode 004: success at 134 policy steps

The corresponding videos and NPZ trajectories are stored in [media/task_04](../media/task_04/).

## Observed behavior

In the successful trajectories, the gripper closes near the target and the end-effector rises before transporting the bowl toward the plate. In the representative failed trajectory, the end-effector rises by approximately 0.003 m during the 30 steps following the first close command. The gripper command subsequently changes repeatedly and the episode reaches the step limit without satisfying the task condition.

## Interpretation

The drawer introduces three constraints that are not present in an open tabletop grasp:

1. The cabinet and drawer lip restrict the approach direction.
2. The bowl is partially occluded by the surrounding structure.
3. A stable grasp must be followed by a collision-free lift and transport path.

These constraints reduce the set of feasible grasp configurations. Target proximity alone is insufficient as an explanation. Task 0 places the bowl between a plate and a ramekin but achieves 98%, while Task 4 places the bowl inside a drawer and achieves 68%.

Task 8 provides a second constrained case: the bowl is adjacent to the destination plate and achieves 74%. In this case the target and destination are both close, reducing the available placement clearance.

## Scope of the analysis

The analysis is based on task summaries, logs, videos, and NPZ trajectories. It describes observed failure patterns; intervention effects are not measured in this release.
