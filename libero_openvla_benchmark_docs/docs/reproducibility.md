# Reproducibility

## Benchmark configuration

~~~yaml
checkpoint: openvla/openvla-7b-finetuned-libero-spatial
task_suite_name: libero_spatial
task_ids: 0-9
num_trials_per_task: 50
total_trials: 500
seed: 7
max_steps: 220
num_steps_wait: 10
resolution: 256
center_crop: true
~~~

실행은 pretrained checkpoint와 그 checkpoint에 맞는 unnorm_key=libero_spatial을 사용한다. seed, package version, GPU, CUDA, evaluator commit을 함께 저장해야 공식 수치와 의미 있는 비교가 된다.

## User-machine command

~~~bash
cd /home/user/openvla

export OPENVLA_ROOT=/home/user/openvla
export LIBERO_ROOT=/home/user/LIBERO
export BENCH_ROOT="$LIBERO_ROOT/experiments/libero_spatial_benchmark"

python experiments/robot/libero/run_libero_spatial_taskwise_benchmark.py \
  --task-id all \
  --num-trials 50 \
  --seed 7 \
  --output-root "$BENCH_ROOT" \
  2>&1 | tee "$BENCH_ROOT/benchmark_seed_7.log"
~~~

이 명령은 Task 0–9를 각각 50회씩 실행한다. 총 episode 수는 500회다.

## Expected output layout

~~~text
/home/user/LIBERO/experiments/libero_spatial_benchmark/
└── openvla-7b-finetuned-libero-spatial/
    └── seed_7/
        ├── task_00/
        │   ├── task_summary.json
        │   ├── episodes.csv
        │   ├── videos/
        │   └── trajectories/
        ├── task_01/
        ├── ...
        └── task_09/
~~~

현재 묶음은 각 원본 summary/log를 results/native_libero_spatial/openvla_7b_finetuned/seed_7/ 아래에 보존한다. 원본 machine path는 로그에 남아 있으므로 GitHub 공개 전에 사용자명과 절대 경로가 노출되지 않도록 relative path로 정리한다.

## Fair comparison checklist

- 동일 checkpoint와 unnorm_key
- 동일 task suite와 task ordering
- 동일 trial 수와 max step
- 동일 seed protocol
- 동일 Python/PyTorch/Transformers/flash-attn 버전
- 동일 GPU 또는 hardware note
- center crop, image resolution, action/gripper convention 기록
- 공식 결과가 multi-seed 평균인지 단일 seed인지 명시

## Official comparison

OpenVLA 공식 README는 LIBERO-Spatial fine-tuned model에 대해 84.7 ± 0.9%를 보고하고, 공식 evaluator는 task당 50 trial을 기본값으로 사용한다. 이번 결과 84.4%는 seed 7 단일 실행이다. 수치 차이는 작지만, 단일 seed 결과이므로 error bar를 붙이거나 공식 평균과 동일한 통계 절차로 해석하지 않는다.
