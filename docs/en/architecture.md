# System Architecture

[한국어](../architecture.md) | English

## LIBERO and OpenVLA evaluation

~~~mermaid
flowchart TD
    suite["LIBERO-Spatial task suite"] --> environment["LIBERO environment"]
    instruction["Task instruction"] --> input["OpenVLA input"]
    environment --> observation["RGB observation"]
    observation --> input
    input --> policy["OpenVLA policy"]
    policy --> action["7D action"]
    action --> environment
    environment --> evaluator["Success and timeout evaluator"]
    evaluator --> artifacts["Logs, summaries, videos, trajectories"]
~~~

The task suite provides the BDDL task definition, instruction, and initial state. The environment returns RGB observations and applies the predicted action. The OpenVLA policy uses the LIBERO-Spatial fine-tuned checkpoint. The evaluator records task success, termination reason, policy steps, and trajectory artifacts.

## OpenVLA policy path

~~~mermaid
flowchart LR
    image["RGB image"] --> vision["DINOv2 and SigLIP"]
    instruction["Language instruction"] --> fusion["Multimodal policy"]
    vision --> fusion
    fusion --> action["7D robot action"]
~~~

The evaluation uses the OpenVLA LIBERO-Spatial checkpoint and the standard LIBERO action interface. Action post-processing follows the LIBERO evaluator convention.

## Repository architecture

~~~mermaid
flowchart TD
    repository["Libero-OpenVLA-Benchmark-in-IsaacSim"] --> docs["docs"]
    repository --> results["results/libero_spatial"]
    repository --> figures["figures"]
    repository --> media["media/task_04"]
    repository --> scripts["scripts"]
    results --> seed["openvla_7b_finetuned/seed_7"]
    seed --> data["Summaries, logs, CSV, JSON"]
    scripts --> generator["make_figures.py"]
~~~

The repository separates interpretation, raw benchmark metadata, generated figures, representative media, and utility scripts. Isaac Sim transfer experiments can be added as a separate result group without changing the native LIBERO baseline.
