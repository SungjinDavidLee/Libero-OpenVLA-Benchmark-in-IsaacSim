# File map: source files to GitHub locations

## 1. 현재 업로드된 원본 위치

이 작업 공간에서 분석에 사용한 원본은 다음 위치에 있다.

~~~text
/workspace/scratch/956958c344ce/upload/
├── task-0.log ... task-9.log
├── task_summary-0.json ... task_summary-9.json
├── episode_000.mp4
├── episode_001.mp4
├── episode_004.mp4
├── episode_000.npz
├── episode_001.npz
└── episode_004.npz
~~~

이는 현재 대화에 업로드된 staging 위치다. 실제 사용자 머신의 benchmark 원본은 로그에 기록된 다음 경로를 따른다.

~~~text
/home/user/LIBERO/experiments/libero_spatial_benchmark/
└── openvla-7b-finetuned-libero-spatial/seed_7/task_04/
    ├── videos/episode_XXX.mp4
    └── trajectories/episode_XXX.npz
~~~

## 2. 이 문서 묶음 안의 위치

~~~text
libero_openvla_benchmark_docs/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── benchmark_report.md
│   ├── data_format.md
│   ├── failure_analysis.md
│   ├── file_map.md
│   └── reproducibility.md
├── configs/libero_spatial_openvla_seed7.yaml
├── figures/
│   ├── success_rate_by_task.png
│   ├── mean_policy_steps_by_task.png
│   ├── official_vs_current.png
│   ├── success_vs_mean_steps.png
│   └── task4_failure_case.png
├── results/native_libero_spatial/openvla_7b_finetuned/seed_7/
│   ├── task_summary-0.json ... task_summary-9.json
│   └── logs/task-0.log ... task-9.log
├── results/overall_summary.json
├── results/task_results.csv
├── media/task_04/
│   ├── episode_000.mp4
│   ├── episode_001.mp4
│   ├── episode_004.mp4
│   ├── episode_000.npz
│   ├── episode_001.npz
│   └── episode_004.npz
└── scripts/make_figures.py
~~~

## 3. OpenVLA 저장소에 복사할 위치

현재 실행 환경에서는 사용자의 /home/user/openvla 저장소에 직접 쓸 수 없으므로, 아래처럼 benchmark 전용 디렉터리로 복사한다.

~~~bash
export OPENVLA_ROOT=/home/user/openvla
export BENCH_REPO="$OPENVLA_ROOT/benchmarks/libero_spatial_openvla"

mkdir -p "$BENCH_REPO"
cp -a /path/to/libero_openvla_benchmark_docs/. "$BENCH_REPO/"
~~~

압축 파일로 전달받았다면 다음처럼 풀면 된다.

~~~bash
TMP_DOCS_DIR=$(mktemp -d)
unzip -q libero_openvla_benchmark_docs.zip -d "$TMP_DOCS_DIR"
mkdir -p "$OPENVLA_ROOT/benchmarks/libero_spatial_openvla"
cp -a "$TMP_DOCS_DIR/libero_openvla_benchmark_docs/." \
  "$OPENVLA_ROOT/benchmarks/libero_spatial_openvla/"
~~~

최종 README 링크는 다음이 된다.

~~~text
/home/user/openvla/benchmarks/libero_spatial_openvla/README.md
~~~

## 4. 추가 원본을 넣을 때의 규칙

- 전체 Task 로그: results/native_libero_spatial/openvla_7b_finetuned/seed_7/logs/
- 전체 Task summary: 같은 seed 디렉터리
- Task별 영상: media/task_XX/videos/
- Task별 trajectory: media/task_XX/trajectories/
- 여러 seed: results/native_libero_spatial/openvla_7b_finetuned/seed_8/처럼 형제 디렉터리
- 절대 경로: 공개 전 relative path로 치환
- model weight와 LIBERO dataset: 이 저장소에 복사하지 않음
