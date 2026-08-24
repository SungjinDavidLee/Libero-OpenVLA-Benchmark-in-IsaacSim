# 시스템 아키텍처

[English version](en/architecture.md)

## LIBERO 및 OpenVLA 평가 흐름

~~~mermaid
flowchart TD
    suite["LIBERO-Spatial 태스크 모음"] --> environment["LIBERO 환경"]
    instruction["태스크 지시문"] --> input["OpenVLA 입력"]
    environment --> observation["RGB 관측"]
    observation --> input
    input --> policy["OpenVLA 정책"]
    policy --> action["7D 로봇 동작"]
    action --> environment
    environment --> evaluator["성공 및 타임아웃 평가기"]
    evaluator --> artifacts["로그, 요약, 영상, 궤적"]
~~~

태스크 모음은 BDDL 태스크 정의, 지시문, 초기 상태를 제공한다. LIBERO 환경은 RGB 관측을 반환하고 정책이 예측한 동작을 적용한다. OpenVLA 정책은 LIBERO-Spatial 미세조정 체크포인트를 사용하며, 평가기는 성공 여부, 종료 원인, 정책 스텝, 궤적 자료를 기록한다.

## OpenVLA 정책 경로

~~~mermaid
flowchart LR
    image["RGB 이미지"] --> vision["DINOv2 및 SigLIP"]
    instruction["언어 지시문"] --> fusion["멀티모달 정책"]
    vision --> fusion
    fusion --> action["7D 로봇 동작"]
~~~

평가에는 OpenVLA LIBERO-Spatial 체크포인트와 LIBERO의 표준 동작 인터페이스를 사용한다. 동작 후처리는 LIBERO 평가기의 규약에 따른다.

## 저장소 구성

~~~mermaid
flowchart TD
    repository["Libero-OpenVLA-Benchmark-in-IsaacSim"] --> docs["docs"]
    repository --> results["results/libero_spatial"]
    repository --> figures["figures"]
    repository --> media["media/task_04"]
    repository --> scripts["scripts"]
    results --> seed["openvla_7b_finetuned/seed_7"]
    seed --> data["요약, 로그, CSV, JSON"]
    scripts --> generator["make_figures.py"]
~~~

저장소는 보고서, 원자료, 생성된 그래프, 대표 미디어, 유틸리티 스크립트를 분리한다. Isaac Sim 전이 실험은 네이티브 LIBERO 기준선과 구분되는 별도의 결과 그룹으로 추가할 수 있다.
