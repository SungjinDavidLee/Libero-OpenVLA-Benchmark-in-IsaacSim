# 데이터 형식

[English version](en/data_format.md)

## 태스크별 CSV

경로: `results/libero_spatial/openvla_7b_finetuned/seed_7/task_results.csv`

각 행은 하나의 태스크를 나타낸다. 주요 열은 다음과 같다.

- `task_id`
- `instruction`
- `num_trials`
- `successes`
- `failures`
- `success_rate`
- `mean_policy_steps`
- `failure_reasons`

## 태스크 요약 JSON

경로: `results/libero_spatial/openvla_7b_finetuned/seed_7/task_summaries/`

각 JSON 파일에는 태스크 지시문, 체크포인트, 시드, 평가 횟수, 성공 횟수, 실패 원인, 이미지 설정, 정책 스텝 제한이 기록되어 있다.

## 태스크 로그

경로: `results/libero_spatial/openvla_7b_finetuned/seed_7/logs/`

각 로그에는 에피소드 시작 정보, 영상 경로, 종료 원인, 성공 여부, 정책 스텝 정보가 포함된다.

## NPZ 궤적

대표적인 Task 4 궤적에는 다음 배열과 메타데이터가 포함된다.

~~~text
rgb
eef_pos
eef_quat
eef_axisangle
gripper_qpos
action_raw
action_env
reward
done
policy_step
sim_step
success
task_id
episode_idx
instruction
termination_reason
last_info_json
error
initial_state
~~~
