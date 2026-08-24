# 저장소 구성

[English version](en/file_map.md)

~~~text
.
├── README.md                         # 한국어 메인 문서
├── README.en.md                      # English README
├── CITATION.cff
├── configs/
│   └── libero_spatial_seed7.yaml
├── docs/
│   ├── architecture.md
│   ├── benchmark_report.md
│   ├── data_format.md
│   ├── failure_analysis.md
│   ├── file_map.md
│   ├── reproducibility.md
│   └── en/                           # English documentation
│       ├── architecture.md
│       ├── benchmark_report.md
│       ├── data_format.md
│       ├── failure_analysis.md
│       ├── file_map.md
│       └── reproducibility.md
├── figures/
│   ├── official_vs_current.png
│   ├── success_rate_by_task.png
│   ├── success_vs_mean_steps.png
│   ├── mean_policy_steps_by_task.png
│   └── task4_failure_case.png
├── media/
│   └── task_04/
│       ├── README.md
│       ├── README.ko.md
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

결과 디렉터리는 태스크 모음, 체크포인트 계열, 랜덤 시드 순서로 구성한다. 로그와 태스크 요약은 그래프와 분리되어 있으며, `media/`에는 전체 500개 에피소드가 아닌 대표적인 Task 4 자료만 포함한다.

저장소 내부 경로는 상대 경로로 작성되어 있다. 모델 가중치, LIBERO 데이터셋, 장비별 설치 경로는 저장소에 포함하지 않는다.
