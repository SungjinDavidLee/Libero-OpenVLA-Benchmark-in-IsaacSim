# System and repository architecture

## 1. LIBERO × OpenVLA benchmark architecture

~~~mermaid
flowchart TD
    suite["LIBERO-Spatial suite (BDDL, fixed initial states)"] --> env["LIBERO environment (MuJoCo + Franka)"]
    instr["Fixed language instruction"] --> input["OpenVLA input pipeline"]
    env --> obs["RGB observation"]
    obs --> input
    input --> policy["OpenVLA 7B (DINOv2 + SigLIP + Llama-2)"]
    policy --> action["7D action"]
    action --> env
    env --> eval["Success or timeout evaluator"]
    eval --> logs["Summary, log, video, NPZ"]
~~~

### 블록별 의미

1. **LIBERO-Spatial suite**: task description, BDDL, fixed initial state를 제공한다.
2. **LIBERO environment**: action을 적용하고 RGB observation, reward, done/info를 반환한다.
3. **OpenVLA input pipeline**: resolution 256, center crop, fixed instruction을 사용한다.
4. **OpenVLA policy**: official LIBERO-Spatial fine-tuned checkpoint를 사용한다. OpenVLA의 vision path는 DINOv2와 SigLIP을 결합하고 language/action policy로 연결한다.
5. **Action/evaluator**: policy action을 LIBERO convention에 맞게 변환한 뒤 environment에 적용하고, success 또는 220-step timeout을 기록한다.

이번 benchmark에서 observation/state semantics를 바꾸거나 task-specific controller를 삽입하지 않는다. 이것이 공식 baseline과 비교 가능한 최소 구조다.

## 2. Artifact and repository architecture

~~~mermaid
flowchart TD
    root["benchmarks/libero_spatial_openvla"] --> docs["docs/"]
    root --> figures["figures/"]
    root --> results["results/"]
    root --> media["media/task_04/"]
    root --> scripts["scripts/"]
    docs --> report["benchmark_report.md + failure_analysis.md"]
    figures --> plots["PNG charts"]
    results --> data["CSV + JSON + raw logs"]
    media --> evidence["Task 4 MP4 + NPZ"]
    scripts --> generator["make_figures.py"]
~~~

### Git

- Markdown: 사람이 읽는 보고서와 아키텍처
- Mermaid: GitHub에서 바로 렌더링되는 구조도
- PNG: README에서 바로 보이는 그래프와 failure case
- CSV/JSON: 정확한 수치와 실행 메타데이터
- Python/YAML: 그래프 생성 및 benchmark 설정 기록
- 짧은 대표 MP4: Task 4 failure evidence

### Git LFS / Release

- 전체 500 episode MP4
- 전체 trajectory NPZ
- 장기적으로 늘어날 multi-seed 결과
- model weight와 LIBERO 원본 데이터셋
