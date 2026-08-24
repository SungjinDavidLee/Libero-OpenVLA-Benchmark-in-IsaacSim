# Data format

## task_results.csv

한 행이 한 Task다. 그래프는 이 파일에서 생성한다.

- task_id: 0–9
- instruction: 고정 instruction
- num_trials: 요청한 trial 수
- successes: 성공 episode 수
- failures: 실패 episode 수
- success_rate: 0–1
- mean_policy_steps: 완료 episode를 포함한 task 평균 policy step
- failure_reasons: JSON 문자열. 현재 모든 failure가 timeout

## task_summary JSON

실행 script가 Task별로 저장한 원본에 가까운 summary다. benchmark 설정과 결과를 한 파일에서 확인할 수 있다.

주요 필드:

~~~text
task_suite_name
task_id
instruction
pretrained_checkpoint
unnorm_key
seed
num_trials_requested
num_trials_completed
num_successes
num_failures
success_rate
mean_policy_steps
failure_reasons
max_steps
num_steps_wait
resolution
center_crop
~~~

## Task 4 NPZ evidence

대표 NPZ에는 다음 배열이 들어 있다.

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

task4_failure_case.png는 rgb, eef_pos, action_env, success, termination_reason을 사용해 다시 만들 수 있다.
