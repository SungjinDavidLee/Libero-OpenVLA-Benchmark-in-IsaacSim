# Reproducibility

## Evaluation configuration

~~~yaml
checkpoint: openvla/openvla-7b-finetuned-libero-spatial
task_suite: libero_spatial
task_ids: 0-9
trials_per_task: 50
total_trials: 500
seed: 7
max_policy_steps: 220
num_steps_wait: 10
image_resolution: 256
center_crop: true
~~~

## Evaluation command

The command below assumes that the OpenVLA and LIBERO repositories are installed separately.

~~~bash
export OPENVLA_ROOT=/path/to/openvla
export OUTPUT_ROOT=/path/to/libero_spatial_results

python "$OPENVLA_ROOT/experiments/robot/libero/run_libero_spatial_taskwise_benchmark.py" \
  --task-id all \
  --num-trials 50 \
  --seed 7 \
  --output-root "$OUTPUT_ROOT" \
  2>&1 | tee "$OUTPUT_ROOT/benchmark_seed_7.log"
~~~

The command evaluates ten tasks with 50 trials per task. The taskwise runner is maintained in the OpenVLA source tree; this repository contains the resulting summaries, logs, figures, and representative trajectories.

The same command is available as scripts/run_libero_spatial_benchmark.sh.

## Figure regeneration

From the repository root:

~~~bash
python scripts/make_figures.py
~~~

The script reads the task-wise CSV and the Task 4 NPZ files and regenerates all figures in figures/.

## Reproducibility requirements

- OpenVLA checkpoint and matching action normalization key
- LIBERO task suite and task order
- 50 trials per task
- Seed and maximum policy horizon
- Image resolution and center-crop setting
- Python, PyTorch, Transformers, and flash-attn versions
- GPU and CUDA version
