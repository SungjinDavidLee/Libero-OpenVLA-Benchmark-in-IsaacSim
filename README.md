# LIBERO-Spatial × OpenVLA Benchmark

OpenVLA 공식 LIBERO-Spatial fine-tuned checkpoint를 사용해 Task 0–9를 각 50회씩 평가한 결과를 정리한 문서이다.

## 핵심 결과

![Task별 성공률](figures/success_rate_by_task.png)

![Task별 평균 policy step](figures/mean_policy_steps_by_task.png)

- 전체 성공률: **422 / 500 = 84.4%**
- 가장 높은 Task: **Task 0, 98%**
- 가장 낮은 Task: **Task 4, 68%**
- 모든 실패 episode의 종료 원인: **timeout at 220 policy steps**
- 공식 OpenVLA README의 LIBERO-Spatial 보고값: **84.7 ± 0.9%**. 이번 결과는 seed 7 단일 실행이므로 수치가 매우 가깝다는 점까지 비교할 수 있지만, 동일한 하드웨어·패키지·3개 seed 조건을 재현했다는 의미는 아니다.

![공식 결과와 이번 실행](figures/official_vs_current.png)

## 중요 문서

1. [docs/benchmark_report.md](docs/benchmark_report.md) — 그래프 중심 최종 요약
2. [docs/failure_analysis.md](docs/failure_analysis.md) — Task 4를 포함한 실패 원인 분석
3. [docs/architecture.md](docs/architecture.md) — LIBERO와 OpenVLA의 아키텍처
4. [docs/reproducibility.md](docs/reproducibility.md) — 평가 조건과 재실행 명령
5. [docs/file_map.md](docs/file_map.md) — 사용자 머신의 원본 위치와 GitHub 저장 위치
6. [results/task_results.csv](results/task_results.csv) — 그래프의 원본 수치
7. [results/overall_summary.json](results/overall_summary.json) — 집계 메타데이터

정확한 수치를 확인할 때는 그래프에서 값을 읽지 말고 CSV/JSON을 사용한다. 그래프는 사람이 빠르게 경향을 확인하기 위한 산출물이다.


## 원본 및 제3자 프로젝트

- [OpenVLA](https://github.com/openvla/openvla)
- [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
