# Data Format

## Task-wise CSV

Path: results/libero_spatial/openvla_7b_finetuned/seed_7/task_results.csv

Each row represents one task. The columns are:

- task_id
- instruction
- num_trials
- successes
- failures
- success_rate
- mean_policy_steps
- failure_reasons

## Task summary JSON

Path: results/libero_spatial/openvla_7b_finetuned/seed_7/task_summaries/

Each summary records the task instruction, checkpoint, seed, trial count, success count, failure reasons, image configuration, and policy horizon.

## Task log

Path: results/libero_spatial/openvla_7b_finetuned/seed_7/logs/

Each log contains episode start, video path, termination reason, success flag, and policy-step information.

## NPZ trajectory

The representative Task 4 trajectories contain:

~~~text
rgb
eef_pos
eef_quat
eef_axisangle
gripper_qpos
action_raw
action_env
reward
done
policy_step
sim_step
success
task_id
episode_idx
instruction
termination_reason
last_info_json
error
initial_state
~~~
