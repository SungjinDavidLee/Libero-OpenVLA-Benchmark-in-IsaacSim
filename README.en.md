# LIBERO-Spatial OpenVLA Benchmark

[한국어](README.md) | English

Native LIBERO-Spatial evaluation of the OpenVLA LIBERO-Spatial fine-tuned checkpoint.

The repository contains the benchmark configuration, task-wise results, analysis figures, representative Task 4 trajectories, and the evaluation architecture. The current release is a LIBERO baseline; Isaac Sim and real-Franka transfer results are maintained as separate experiment conditions.

## Results

![Task-wise success rate](figures/success_rate_by_task.png)

![Mean policy steps](figures/mean_policy_steps_by_task.png)

- Overall success rate: **84.4%** (422/500)
- Lowest task success rate: **Task 4, 68%**
- Highest task success rate: **Task 0, 98%**
- Failure termination: **78 timeouts at 220 policy steps**
- Evaluation seed: **7**

![Official and current result](figures/official_vs_current.png)

The official OpenVLA LIBERO-Spatial result is 84.7 ± 0.9%, reported over three random seeds. The result in this repository is a single-seed measurement and is therefore reported separately.

## Repository contents

- [Benchmark report](docs/en/benchmark_report.md)
- [Task 4 failure analysis](docs/en/failure_analysis.md)
- [System architecture](docs/en/architecture.md)
- [Reproducibility](docs/en/reproducibility.md)
- [Repository layout](docs/en/file_map.md)
- [Data format](docs/en/data_format.md)
- [Task-wise results](results/libero_spatial/openvla_7b_finetuned/seed_7/task_results.csv)
- [Figure generation script](scripts/make_figures.py)

## Evaluation configuration

~~~yaml
checkpoint: openvla/openvla-7b-finetuned-libero-spatial
task_suite: libero_spatial
tasks: 0-9
trials_per_task: 50
total_trials: 500
seed: 7
max_policy_steps: 220
image_resolution: 256
center_crop: true
~~~

## References

- [OpenVLA](https://github.com/openvla/openvla)
- [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
