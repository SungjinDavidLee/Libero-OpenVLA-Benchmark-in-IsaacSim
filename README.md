# LIBERO-Spatial OpenVLA 벤치마크

[English](README.en.md) | 한국어

LIBERO-Spatial 태스크 모음에서 LIBERO-Spatial 미세조정 체크포인트를 사용한 OpenVLA의 성능을 평가한 결과를 정리한 저장소입니다.

본 릴리스는 네이티브 LIBERO 환경을 대상으로 한 기준선 평가입니다. Isaac Sim 및 실제 Franka로의 전이 결과는 별도의 실험 조건으로 관리합니다.

## 결과

![태스크별 성공률](figures/success_rate_by_task.png)

![평균 정책 스텝](figures/mean_policy_steps_by_task.png)

- 전체 성공률: **84.4%** (422/500)
- 가장 낮은 성공률: **Task 4, 68%**
- 가장 높은 성공률: **Task 0, 98%**
- 실패 종료 원인: **220 정책 스텝 제한에 의한 타임아웃 78회 (log의 최종 종료 상태 기준, 실제 원인은 오브젝트 충돌,겹칩/동작 정체 등)**
- 평가 시드: **7**

![공식 결과와 본 평가 결과](figures/official_vs_current.png)

OpenVLA에서 보고한 LIBERO-Spatial 공식 결과는 세 개의 랜덤 시드에 대한 평균 **84.7 ± 0.9%**입니다. 본 저장소의 결과는 시드 7에서 측정한 단일 시드 결과이므로 공식 평균과 구분하여 해석해야 합니다.

## 문서

- [벤치마크 보고서](docs/benchmark_report.md)
- [Task 4 실패 분석](docs/failure_analysis.md)
- [시스템 아키텍처](docs/architecture.md)
- [재현 방법](docs/reproducibility.md)
- [저장소 구성](docs/file_map.md)
- [데이터 형식](docs/data_format.md)
- [태스크별 결과](results/libero_spatial/openvla_7b_finetuned/seed_7/task_results.csv)
- [그래프 생성 스크립트](scripts/make_figures.py)

## 평가 설정

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

## 참고 자료

- [OpenVLA](https://github.com/openvla/openvla)
- [LIBERO](https://github.com/Lifelong-Robot-Learning/LIBERO)
