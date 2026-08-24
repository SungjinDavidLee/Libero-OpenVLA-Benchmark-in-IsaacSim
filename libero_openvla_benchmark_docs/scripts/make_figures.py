#!/usr/bin/env python3
"""Create GitHub-friendly benchmark figures from the checked-in CSV/NPZ data."""

from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.gridspec import GridSpec


PALETTE = [
    "#8f83e8",
    "#f3bb28",
    "#4fb7a4",
    "#ee858c",
    "#5e9ed8",
    "#ef9c72",
    "#67bcae",
    "#aa8fe7",
    "#f0b832",
    "#5d9bd3",
]
RED = "#ba153f"
GRID = "#e5e7eb"
TEXT = "#384152"


def style_axis(ax, y_grid=True):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#c8ccd4")
    ax.spines["bottom"].set_color("#c8ccd4")
    ax.tick_params(colors=TEXT, labelsize=9)
    if y_grid:
        ax.grid(axis="y", color=GRID, linewidth=0.8)
        ax.set_axisbelow(True)


def read_results(root: Path):
    path = root / "results" / "task_results.csv"
    with path.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for row in rows:
        row["task_id"] = int(row["task_id"])
        row["success_rate"] = float(row["success_rate"])
        row["mean_policy_steps"] = float(row["mean_policy_steps"])
        row["successes"] = int(row["successes"])
        row["failures"] = int(row["failures"])
    return rows


def save(fig, path: Path):
    path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(path, dpi=220, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def make_success_rate(rows, out):
    tasks = [r["task_id"] for r in rows]
    values = [100 * r["success_rate"] for r in rows]
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    bars = ax.bar(tasks, values, color=PALETTE, width=0.68, edgecolor="white", linewidth=1.2)
    ax.set_title("LIBERO-Spatial success rate by task", fontsize=18, color="#367eb5", pad=18)
    ax.set_xlabel("Task", color=TEXT)
    ax.set_ylabel("Success rate (%)", color=TEXT)
    ax.set_ylim(0, 108)
    ax.set_xticks(tasks, [f"Task {x}" for x in tasks])
    style_axis(ax)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 2.0, f"{value:.0f}%",
                ha="center", va="bottom", fontsize=10, color=TEXT)
    ax.text(0.0, -0.19, "50 trials per task | seed 7 | checkpoint: OpenVLA LIBERO-Spatial",
            transform=ax.transAxes, fontsize=9, color="#6b7280")
    save(fig, out / "success_rate_by_task.png")


def make_mean_steps(rows, out):
    tasks = np.array([r["task_id"] for r in rows])
    values = np.array([r["mean_policy_steps"] for r in rows])
    fig, ax = plt.subplots(figsize=(10.5, 5.5))
    ax.plot(tasks, values, color=RED, linewidth=3.0, marker="o", markersize=7,
            markerfacecolor="white", markeredgewidth=2.0, markeredgecolor=RED)
    ax.fill_between(tasks, values, 0, color="#f6d8df", alpha=0.45)
    ax.set_title("Mean policy steps by task", fontsize=18, color="#367eb5", pad=18)
    ax.set_xlabel("Task", color=TEXT)
    ax.set_ylabel("Mean policy steps", color=TEXT)
    ax.set_ylim(0, 220)
    ax.set_xticks(tasks, [f"Task {x}" for x in tasks])
    style_axis(ax)
    for task, value in zip(tasks, values):
        if task in (4, 8, 9):
            ax.annotate(f"{value:.2f}", (task, value), xytext=(0, 12),
                        textcoords="offset points", ha="center", fontsize=9, color=RED)
    ax.text(0.0, -0.19, "Higher values indicate longer action horizons before success or timeout",
            transform=ax.transAxes, fontsize=9, color="#6b7280")
    save(fig, out / "mean_policy_steps_by_task.png")


def make_official_comparison(root, out):
    with (root / "results" / "overall_summary.json").open(encoding="utf-8") as f:
        summary = json.load(f)
    labels = ["Official\nOpenVLA", "Current\nseed 7"]
    values = [100 * summary["official_openvla_reported_success_rate"],
              100 * summary["overall_success_rate"]]
    colors = ["#8f83e8", "#4fb7a4"]
    fig, ax = plt.subplots(figsize=(7.0, 5.2))
    bars = ax.bar(labels, values, color=colors, width=0.5, edgecolor="white", linewidth=1.3)
    ax.set_title("LIBERO-Spatial: official vs current", fontsize=17, color="#367eb5", pad=18)
    ax.set_ylabel("Success rate (%)", color=TEXT)
    ax.set_ylim(0, 100)
    style_axis(ax)
    for bar, value in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, value + 2, f"{value:.1f}%",
                ha="center", fontsize=11, color=TEXT)
    ax.text(0.0, -0.20, "Official: 3-seed average | Current: one seed (7)", transform=ax.transAxes,
            fontsize=9, color="#6b7280")
    save(fig, out / "official_vs_current.png")


def make_success_vs_steps(rows, out):
    x = np.array([r["mean_policy_steps"] for r in rows])
    y = np.array([100 * r["success_rate"] for r in rows])
    tasks = np.array([r["task_id"] for r in rows])
    corr = np.corrcoef(x, y)[0, 1]
    fig, ax = plt.subplots(figsize=(8.5, 5.8))
    ax.scatter(x, y, s=120, c=[PALETTE[t] for t in tasks], edgecolors="white", linewidths=1.2)
    for task, xx, yy in zip(tasks, x, y):
        ax.annotate(f"T{task}", (xx, yy), xytext=(6, 5), textcoords="offset points",
                    fontsize=9, color=TEXT)
    ax.set_title("Success rate vs mean policy steps", fontsize=17, color="#367eb5", pad=18)
    ax.set_xlabel("Mean policy steps", color=TEXT)
    ax.set_ylabel("Success rate (%)", color=TEXT)
    ax.set_xlim(75, 170)
    ax.set_ylim(60, 102)
    style_axis(ax)
    ax.text(0.02, 0.05, f"Exploratory Pearson r = {corr:.2f} (n=10 tasks)",
            transform=ax.transAxes, fontsize=9, color="#6b7280")
    save(fig, out / "success_vs_mean_steps.png")


def load_episode(path: Path):
    data = np.load(path, allow_pickle=True)
    rgb = np.asarray(data["rgb"])
    eef_z = np.asarray(data["eef_pos"])[:, 2]
    gripper = np.asarray(data["action_env"])[:, -1]
    transitions = np.where(np.diff(gripper) != 0)[0] + 1
    close_candidates = transitions[transitions >= 10]
    close_idx = int(close_candidates[0]) if len(close_candidates) else min(50, len(rgb) - 1)
    success = bool(np.asarray(data["success"]).reshape(-1)[0])
    return rgb, eef_z, gripper, close_idx, success


def draw_episode_strip(fig, gs_row, rgb, title, indices):
    for col, idx in enumerate(indices):
        ax = fig.add_subplot(gs_row[col])
        image = np.asarray(rgb[min(idx, len(rgb) - 1)])
        ax.imshow(image)
        ax.set_title(f"step {min(idx, len(rgb) - 1)}", fontsize=9, color=TEXT)
        ax.axis("off")
    fig.text(0.5, gs_row[0].get_position(fig).y1 + 0.028, title,
             fontsize=11, color=TEXT, weight="bold", ha="center")


def make_task4_case(root, out):
    media = root / "media" / "task_04"
    success_rgb, success_z, success_grip, success_close, _ = load_episode(media / "episode_000.npz")
    failure_rgb, failure_z, failure_grip, failure_close, _ = load_episode(media / "episode_001.npz")
    success_indices = [0, success_close, min(success_close + 30, len(success_rgb) - 1), len(success_rgb) - 1]
    failure_indices = [0, failure_close, min(failure_close + 30, len(failure_rgb) - 1), len(failure_rgb) - 1]

    fig = plt.figure(figsize=(14, 9.4), facecolor="white")
    gs = GridSpec(4, 4, figure=fig, height_ratios=[0.13, 1.0, 1.0, 1.35],
                  hspace=0.38, wspace=0.08)
    fig.text(0.5, 0.992, "Task 4: successful lift vs timeout failure",
             fontsize=20, color="#367eb5", ha="center", va="top")
    fig.text(0.02, 0.948, "Target: black bowl inside the top drawer of the wooden cabinet",
             fontsize=10, color="#6b7280")

    draw_episode_strip(fig, [gs[1, col] for col in range(4)], success_rgb,
                       f"SUCCESS  episode_000  |  {len(success_rgb)} steps  |  close@{success_close}",
                       success_indices)
    draw_episode_strip(fig, [gs[2, col] for col in range(4)], failure_rgb,
                       f"FAILURE  episode_001  |  timeout@{len(failure_rgb)}  |  close@{failure_close}",
                       failure_indices)

    ax = fig.add_subplot(gs[3, :])
    success_rel_z = success_z - success_z[success_close]
    failure_rel_z = failure_z - failure_z[failure_close]
    ax.plot(np.arange(len(success_rel_z)), success_rel_z, color="#4fb7a4", linewidth=2.7,
            label=f"success delta_z30 = {success_rel_z[min(success_close + 30, len(success_rel_z)-1)]:+.3f} m")
    ax.plot(np.arange(len(failure_rel_z)), failure_rel_z, color=RED, linewidth=2.7,
            label=f"failure delta_z30 = {failure_rel_z[min(failure_close + 30, len(failure_rel_z)-1)]:+.3f} m")
    ax.axvline(success_close, color="#4fb7a4", linestyle="--", alpha=0.65)
    ax.axvline(failure_close, color=RED, linestyle="--", alpha=0.65)
    ax.set_xlabel("Policy step", color=TEXT)
    ax.set_ylabel("EEF z relative to first close (m)", color=TEXT)
    ax.set_ylim(min(failure_rel_z.min(), success_rel_z.min()) - 0.02,
                max(failure_rel_z.max(), success_rel_z.max()) + 0.03)
    style_axis(ax)
    ax.legend(loc="upper left", frameon=False, fontsize=9)
    grip_ax = ax.twinx()
    grip_ax.step(np.arange(len(failure_grip)), failure_grip, where="post",
                 color=RED, alpha=0.18, linewidth=1.2)
    grip_ax.set_ylim(-1.2, 1.2)
    grip_ax.set_yticks([-1, 1], ["open", "close"])
    grip_ax.tick_params(axis="y", colors="#9ca3af", labelsize=8)
    grip_ax.spines["top"].set_visible(False)
    grip_ax.spines["left"].set_visible(False)
    grip_ax.spines["right"].set_color("#e5e7eb")
    fig.text(0.02, 0.015,
             "Interpretation: success lifts after closing; the representative failure barely lifts and repeatedly toggles the gripper.",
             fontsize=9, color="#6b7280")
    save(fig, out / "task4_failure_case.png")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    out = root / "figures"
    rows = read_results(root)
    make_success_rate(rows, out)
    make_mean_steps(rows, out)
    make_official_comparison(root, out)
    make_success_vs_steps(rows, out)
    make_task4_case(root, out)
    print(f"Wrote figures to {out}")


if __name__ == "__main__":
    main()
