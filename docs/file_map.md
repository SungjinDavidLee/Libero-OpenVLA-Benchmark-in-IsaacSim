# Repository Layout

~~~text
.
├── README.md
├── CITATION.cff
├── configs/
│   └── libero_spatial_seed7.yaml
├── docs/
│   ├── architecture.md
│   ├── benchmark_report.md
│   ├── data_format.md
│   ├── file_map.md
│   ├── failure_analysis.md
│   └── reproducibility.md
├── figures/
│   ├── official_vs_current.png
│   ├── success_rate_by_task.png
│   ├── success_vs_mean_steps.png
│   ├── mean_policy_steps_by_task.png
│   └── task4_failure_case.png
├── media/
│   └── task_04/
│       ├── episode_000.mp4
│       ├── episode_000.npz
│       ├── episode_001.mp4
│       ├── episode_001.npz
│       ├── episode_004.mp4
│       └── episode_004.npz
├── results/
│   └── libero_spatial/
│       └── openvla_7b_finetuned/
│           └── seed_7/
│               ├── overall_summary.json
│               ├── task_results.csv
│               ├── logs/
│               └── task_summaries/
├── scripts/
│   ├── make_figures.py
│   └── run_libero_spatial_benchmark.sh
└── requirements-figures.txt
~~~

The results directory is organized by task suite, checkpoint family, and random seed. Logs and task summaries are kept separate from generated figures. The media directory contains representative Task 4 evidence rather than the complete 500-episode video set.

The repository contains relative paths only. Model weights, the LIBERO dataset, and machine-specific installation directories are not included.
