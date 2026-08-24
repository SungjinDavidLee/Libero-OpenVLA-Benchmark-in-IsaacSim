# 재현 방법

[English version](en/reproducibility.md)

## 평가 설정

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

## 평가 명령

아래 명령은 OpenVLA와 LIBERO가 별도의 디렉터리에 설치되어 있다고 가정한다.

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

위 명령은 10개 태스크를 각 50회씩 평가한다. 태스크별 실행기는 OpenVLA 소스 트리에 있으며, 본 저장소에는 실행 결과인 요약 파일, 로그, 그래프, 대표 궤적을 저장한다.

동일한 실행 예시는 `scripts/run_libero_spatial_benchmark.sh`에 포함되어 있다.

## 그래프 재생성

저장소 루트에서 다음 명령을 실행한다.

~~~bash
python scripts/make_figures.py
~~~

스크립트는 태스크별 CSV와 Task 4 NPZ 파일을 읽어 `figures/`의 그래프를 생성한다.

## 재현에 필요한 조건

- OpenVLA 체크포인트와 대응하는 동작 정규화 키
- LIBERO 태스크 모음과 태스크 순서
- 태스크별 50회 평가
- 랜덤 시드와 최대 정책 스텝
- 이미지 해상도와 center crop 설정
- Python, PyTorch, Transformers, flash-attn 버전
- GPU 및 CUDA 버전
