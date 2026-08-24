#!/usr/bin/env bash
set -eo pipefail

if [ -z "$OPENVLA_ROOT" ]; then
  echo "Set OPENVLA_ROOT to the OpenVLA repository." >&2
  exit 1
fi

if [ -z "$OUTPUT_ROOT" ]; then
  echo "Set OUTPUT_ROOT to the benchmark output directory." >&2
  exit 1
fi

python "$OPENVLA_ROOT/experiments/robot/libero/run_libero_spatial_taskwise_benchmark.py" \
  --task-id all \
  --num-trials 50 \
  --seed 7 \
  --output-root "$OUTPUT_ROOT" \
  2>&1 | tee "$OUTPUT_ROOT/benchmark_seed_7.log"
