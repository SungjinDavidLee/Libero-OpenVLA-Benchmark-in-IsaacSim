# LIBERO-Spatial benchmark report

## 1. 실행 요약

이번 실행은 OpenVLA의 LIBERO-Spatial fine-tuned checkpoint로 Task 0–9를 각각 50회 평가한 단일 seed benchmark다.

![Task별 성공률](../figures/success_rate_by_task.png)

![Task별 평균 policy step](../figures/mean_policy_steps_by_task.png)

### 결과 한눈에 보기

- **Total:** 422 successes / 500 trials
- **Success rate:** 84.4%
- **Failure count:** 78
- **Failure termination:** 78회 모두 timeout
- **Per-task range:** 68%–98%
- **Slowest mean task:** Task 4, 156.04 policy steps
- **Fastest mean task:** Task 0, 85.72 policy steps

Task별 정확한 수치는 results/task_results.csv와 results/overall_summary.json에 둔다. 아래 그래프의 막대 높이와 선의 위치는 그 파일에서 생성했다.

## 2. 공식 OpenVLA 결과와 비교

![Official vs current](../figures/official_vs_current.png)

비교 조건은 다음과 같다.

- Checkpoint: openvla/openvla-7b-finetuned-libero-spatial, 동일
- Suite: libero_spatial, 동일
- Trials: 10 tasks × 50 = 500, 동일
- Reported success: 공식 84.7 ± 0.9%, 이번 실행 84.4%
- Seed protocol: 공식 3 random seeds 평균, 이번 실행 seed 7 단일 실행
- Max policy steps: 220, 동일
- Image preprocessing: resolution 256, center crop, 동일하게 기록됨

차이는 **−0.3 percentage point**다. 그러나 공식 값은 3개 random seed 평균이고 이번 값은 seed 7 하나이므로, 이 차이를 성능 저하나 개선으로 해석하지 않는다. 다음 단계에서 공식과 같은 seed 수, Python/PyTorch/Transformers/flash-attn 버전, GPU 조건을 고정하면 더 공정한 비교가 된다.

공식 evaluator는 LIBERO-Spatial에서 task당 기본 50 trial, 최대 220 policy step을 사용하고, LIBERO의 고정 initial state를 episode별로 적용한다. 이 benchmark도 그 조건을 기록하고 있다.

## 3. Task별 경향

![Success versus mean steps](../figures/success_vs_mean_steps.png)

관찰되는 경향은 다음과 같다.

- Task 0은 target이 plate와 ramekin 사이에 있지만 98%다. 따라서 “주변 물체가 가까움”만으로 낮은 성공률을 설명할 수 없다.
- Task 1, 5, 6은 다른 물체와의 관계를 해석해야 하지만 88–90%를 보인다.
- Task 4는 top drawer 안의 bowl을 집어야 하며 68%로 가장 낮다.
- Task 8은 target이 plate 옆에 있어 grasp와 placement가 동시에 좁아지고 74%다.
- Task 7과 Task 9는 stove/cabinet 위에서 plate로 이동하는 긴 경로와 높이 차이의 영향을 함께 받을 가능성이 있으며 각각 82%, 76%다.

10개 Task만 비교한 탐색적 상관은 성공률과 평균 policy step 사이에 강한 음의 관계를 보인다. 다만 task geometry가 동시에 바뀌므로 인과관계로 보고하지 않는다.

## 4. 결론

이번 결과는 OpenVLA 공식 LIBERO-Spatial baseline과 aggregate 수준에서 매우 가깝다. benchmark 관점에서 우선 보고할 결론은 다음 세 가지다.

1. 현재 평가 파이프라인은 runtime error 없이 500 episode를 완료했다.
2. 실패는 모두 timeout이며, 특정 Task의 grasp/이동 과정에서 220 step 안에 success condition을 충족하지 못했다.
3. Task 4의 낮은 성능은 단순한 target–distractor 거리보다 drawer 내부의 제한된 접근 공간, occlusion, grasp clearance, lift 후 이동 경로의 누적 난이도로 해석하는 것이 더 타당하다.

## 5. 재현 정보

실행 설정은 reproducibility.md에, 원본 로그와 summary를 넣을 위치는 file_map.md에 정리했다.

공식 참고:

- [OpenVLA official README](https://github.com/openvla/openvla)
- [OpenVLA official LIBERO evaluator](https://github.com/openvla/openvla/blob/main/experiments/robot/libero/run_libero_eval.py)
- [LIBERO official repository](https://github.com/Lifelong-Robot-Learning/LIBERO)
