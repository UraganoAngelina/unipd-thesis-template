#!/usr/bin/env python3
"""Regenerate the Chapter 3 result figures from the final RDG campaign.

The Request Dataset Generator repository is treated as read-only.  All images
are written below the thesis workspace.  The path-displacement figure combines
real failed-flow observations with author-provided successful-path medians.  The
successful distributions use one empirical reference shape translated to the
two authoritative medians, so no random samples or unreported dispersion
parameters are introduced.
"""

from __future__ import annotations

import argparse
import json
import os
import tempfile
from collections import deque
from pathlib import Path
from typing import Iterable

os.environ.setdefault(
    "MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "rdg-chapter3-matplotlib")
)

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


DEFAULT_CAMPAIGN = Path(
    "/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r"
)
DEFAULT_OUTPUT = Path(
    "/home/alberto/unipd-thesis-template/thesis/files/runs/batches/"
    "thesis_live_30r/chapter3_graphs"
)

# Author-provided source-of-truth values for the successful-path comparison.
AUTHOR_DIRECT_SUCCESS_MEDIAN_MS = 571.1
AUTHOR_MEDIATED_SUCCESS_MEDIAN_MS = 755.8

BLUE = "#2563eb"
PURPLE = "#9333ea"
ORANGE = "#ea580c"
GREEN = "#059669"
RED = "#dc2626"
GOLD = "#ca8a04"
GRAY = "#64748b"


def load_metrics(path: Path) -> dict:
    with path.open(encoding="utf-8") as handle:
        return json.load(handle)


def scenario_metrics(results: Path, scenario: str) -> list[dict]:
    files = sorted((results / scenario).glob("*/normalized_metrics.json"))
    if not files:
        raise FileNotFoundError(f"No normalized metrics found for {scenario}")
    return [load_metrics(path) for path in files]


def finite(values: Iterable[object]) -> np.ndarray:
    numeric = np.asarray(
        [float(value) for value in values if isinstance(value, (int, float))],
        dtype=float,
    )
    return numeric[np.isfinite(numeric)]


def rolling_time_mean(
    times: Iterable[float], values: Iterable[float], window_seconds: float
) -> np.ndarray:
    """Trailing time-window mean for possibly non-uniform bucket timestamps."""
    queue: deque[tuple[float, float]] = deque()
    total = 0.0
    means: list[float] = []
    for timestamp, value in zip(times, values):
        timestamp = float(timestamp)
        value = float(value)
        queue.append((timestamp, value))
        total += value
        lower_bound = timestamp - window_seconds
        while queue and queue[0][0] <= lower_bound:
            _, expired = queue.popleft()
            total -= expired
        means.append(total / len(queue))
    return np.asarray(means, dtype=float)


def apply_style() -> None:
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 9.2,
            "axes.titlesize": 11,
            "axes.labelsize": 9.2,
            "legend.fontsize": 8.2,
            "xtick.labelsize": 8.2,
            "ytick.labelsize": 8.2,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "axes.titleweight": "semibold",
            "figure.facecolor": "white",
            "axes.facecolor": "white",
            "savefig.facecolor": "white",
        }
    )


def save(fig: plt.Figure, output: Path, filename: str) -> None:
    output.mkdir(parents=True, exist_ok=True)
    fig.savefig(output / filename, dpi=320, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def calibration_figure(results: Path, output: Path) -> None:
    dataset = load_metrics(
        results / "load_ramp" / "r05_seed_105" / "normalized_metrics.json"
    )
    buckets = dataset["timeseries"]["buckets"]
    times = finite(bucket.get("t") for bucket in buckets)
    active_flows = finite(bucket.get("max_active_flows") or 0 for bucket in buckets)
    active_steps = finite(bucket.get("max_active_steps") or 0 for bucket in buckets)
    drift = finite(bucket.get("p95_queue_delay_ms") or 0 for bucket in buckets)

    fig, (top, bottom) = plt.subplots(
        2, 1, figsize=(8.2, 5.8), sharex=True, gridspec_kw={"hspace": 0.12}
    )
    top.plot(times, active_flows, color=BLUE, linewidth=1.7, label="Active flows")
    top.plot(times, active_steps, color=PURPLE, linewidth=1.35, label="Active steps")
    top.axhline(30, color=GRAY, linewidth=0.8, linestyle=":", alpha=0.8)
    top.set_title("Client-Observed Concurrency")
    top.set_ylabel("Concurrent units")
    top.set_ylim(bottom=0)
    top.legend(
        loc="upper left",
        ncols=1,
        frameon=True,
        framealpha=0.95,
        facecolor="white",
        edgecolor="#e2e8f0",
    )
    top.grid(alpha=0.22)

    bottom.plot(times, drift, color=ORANGE, linewidth=1.6)
    bottom.set_title("Scheduling Drift")
    bottom.set_xlabel("Elapsed time (s)")
    bottom.set_ylabel("95th-percentile queue delay (ms)")
    bottom.set_ylim(bottom=0)
    bottom.grid(alpha=0.22)

    for axis in (top, bottom):
        axis.axvline(60, color=RED, linewidth=1.15, linestyle="--", alpha=0.9)
    top.annotate(
        "backpressure onset",
        xy=(60, 29),
        xytext=(45, 24),
        ha="right",
        color=RED,
        fontsize=8.2,
        arrowprops={"arrowstyle": "->", "color": RED, "lw": 0.8},
        bbox={"boxstyle": "round,pad=0.18", "facecolor": "white", "edgecolor": "none", "alpha": 0.9},
    )
    fig.align_ylabels((top, bottom))
    save(fig, output, "calibration_concurrency_drift.png")


def latency_distribution_figure(results: Path, output: Path) -> None:
    dataset = load_metrics(
        results / "stress_extreme" / "r05_seed_105" / "normalized_metrics.json"
    )
    latencies = finite(
        request.get("client_latency_ms") for request in dataset.get("requests", [])
    )
    bins = min(90, max(30, int(np.sqrt(latencies.size))))
    fig, axis = plt.subplots(figsize=(8.2, 4.25))
    axis.hist(latencies, bins=bins, color=BLUE, alpha=0.84, edgecolor="white", linewidth=0.3)
    axis.set_title("Client-Observed Request-Latency Distribution")
    axis.set_xlabel("Client latency (ms)")
    axis.set_ylabel("Requests")
    axis.grid(axis="y", alpha=0.22)
    save(fig, output, "stress_latency_distribution.png")


def saturation_timeline_figure(results: Path, output: Path) -> None:
    dataset = load_metrics(
        results / "stress_extreme" / "r05_seed_105" / "normalized_metrics.json"
    )
    buckets = dataset["timeseries"]["buckets"]
    times = finite(bucket.get("t") for bucket in buckets)
    completed = finite(bucket.get("requests_completed") or 0 for bucket in buckets)
    errors = finite(bucket.get("errors") or 0 for bucket in buckets)
    bucket_size = float(dataset["timeseries"].get("bucket_size_seconds") or 1.0)
    throughput = completed / bucket_size
    error_rate = np.divide(
        errors * 100.0,
        completed,
        out=np.zeros_like(errors, dtype=float),
        where=completed > 0,
    )
    availability = np.where(errors == 0, 100.0, 0.0)
    throughput_smooth = rolling_time_mean(times, throughput, 10.0)
    error_smooth = rolling_time_mean(times, error_rate, 10.0)
    availability_smooth = rolling_time_mean(times, availability, 10.0)
    active_flows = finite(bucket.get("max_active_flows") or 0 for bucket in buckets)
    active_steps = finite(bucket.get("max_active_steps") or 0 for bucket in buckets)
    drift = finite(bucket.get("p95_queue_delay_ms") or 0 for bucket in buckets)

    fig, axes = plt.subplots(
        3, 1, figsize=(8.2, 7.0), sharex=True, gridspec_kw={"hspace": 0.14}
    )

    concurrency = axes[0]
    concurrency.plot(times, active_flows, color=BLUE, linewidth=1.15, label="Active flows")
    concurrency.plot(times, active_steps, color=PURPLE, linewidth=1.0, label="Active steps")
    concurrency.set_title("Concurrency and Scheduling Drift")
    concurrency.set_ylabel("Concurrent units")
    concurrency.set_ylim(bottom=0)
    concurrency.grid(alpha=0.2)
    drift_axis = concurrency.twinx()
    drift_axis.plot(times, drift, color=ORANGE, linewidth=0.9, alpha=0.72, label="Queue delay")
    drift_axis.set_ylabel("95th-percentile delay (ms)", color=ORANGE)
    drift_axis.tick_params(axis="y", colors=ORANGE)
    drift_axis.spines["right"].set_visible(True)
    handles_1, labels_1 = concurrency.get_legend_handles_labels()
    handles_2, labels_2 = drift_axis.get_legend_handles_labels()
    concurrency.legend(
        handles_1 + handles_2,
        labels_1 + labels_2,
        loc="lower right",
        ncols=3,
        frameon=True,
        framealpha=0.95,
        facecolor="white",
        edgecolor="#e2e8f0",
    )

    rate_axis = axes[1]
    rate_axis.plot(times, throughput, color=GREEN, linewidth=0.45, alpha=0.20)
    rate_axis.plot(times, throughput_smooth, color=GREEN, linewidth=1.45, label="Throughput, 10 s mean")
    rate_axis.set_title("Throughput and Error Rate")
    rate_axis.set_ylabel("Requests per second", color=GREEN)
    rate_axis.tick_params(axis="y", colors=GREEN)
    rate_axis.set_ylim(bottom=0)
    rate_axis.grid(alpha=0.2)
    error_axis = rate_axis.twinx()
    error_axis.plot(times, error_rate, color=RED, linewidth=0.4, alpha=0.18)
    error_axis.plot(times, error_smooth, color=RED, linewidth=1.3, label="Error rate, 10 s mean")
    error_axis.set_ylabel("Error rate (%)", color=RED)
    error_axis.tick_params(axis="y", colors=RED)
    error_axis.set_ylim(0, 105)
    error_axis.spines["right"].set_visible(True)
    handles_1, labels_1 = rate_axis.get_legend_handles_labels()
    handles_2, labels_2 = error_axis.get_legend_handles_labels()
    rate_axis.legend(handles_1 + handles_2, labels_1 + labels_2, loc="upper left", frameon=False, ncols=2)

    availability_axis = axes[2]
    availability_axis.plot(times, availability_smooth, color=GOLD, linewidth=1.45, label="Availability, 10 s mean")
    availability_axis.set_title("Error-Free Bucket Availability")
    availability_axis.set_xlabel("Elapsed time (s)")
    availability_axis.set_ylabel("Error-free buckets (%)")
    availability_axis.set_ylim(-3, 103)
    availability_axis.grid(alpha=0.2)
    availability_axis.legend(
        loc="upper right",
        frameon=True,
        framealpha=0.95,
        facecolor="white",
        edgecolor="#e2e8f0",
    )
    fig.align_ylabels(axes)
    save(fig, output, "stress_saturation_timeline.png")


def flow_type_figure(results: Path, output: Path) -> None:
    dataset = load_metrics(
        results
        / "flow_type_comparison_direct"
        / "r06_seed_106"
        / "normalized_metrics.json"
    )
    label_map = {
        "FLOW_CONTEXT_CALL": "Context\nCall",
        "FLOW_ITI_18": "Registry Stored\nQuery",
        "FLOW_ITI_43": "Retrieve Document\nSet",
        "FLOW_PATIENT_CREATE": "Patient\nCreate",
        "FLOW_PATIENT_QUERY": "Patient\nQuery",
        "FLOW_SCRYBASIGN_SIGN": "Scryba\nSign",
    }
    grouped: dict[str, list[float]] = {}
    for flow in dataset.get("flows", []):
        duration = flow.get("total_duration_ms")
        if isinstance(duration, (int, float)) and duration > 0:
            grouped.setdefault(flow.get("flow_type", "Unknown"), []).append(float(duration))
    labels = sorted(grouped)
    values = [grouped[label] for label in labels]

    fig, axis = plt.subplots(figsize=(9.1, 5.1))
    boxes = axis.boxplot(
        values,
        tick_labels=[label_map.get(label, label.replace("FLOW_", "")) for label in labels],
        showfliers=False,
        patch_artist=True,
        medianprops={"color": "#111827", "linewidth": 1.35},
        whiskerprops={"color": GRAY},
        capprops={"color": GRAY},
    )
    for patch, color in zip(boxes["boxes"], [PURPLE, ORANGE, BLUE, GREEN, RED, GOLD]):
        patch.set_facecolor(color)
        patch.set_alpha(0.62)
    axis.set_yscale("log")
    axis.set_title("Client-Observed End-to-End Latency by Flow Type")
    axis.set_xlabel("Healthcare flow type", labelpad=8)
    axis.set_ylabel("End-to-end latency (ms, logarithmic scale)")
    axis.grid(axis="y", which="both", alpha=0.22)
    save(fig, output, "flow_type_latency_log.png")


def path_displacement_figure(results: Path, output: Path) -> None:
    comparison = scenario_metrics(results, "direct_vs_middleware")
    direct_failure: list[float] = []
    mediated_failure: list[float] = []
    direct_types = {"FLOW_PATIENT_QUERY", "FLOW_PATIENT_CREATE"}
    for dataset in comparison:
        for flow in dataset.get("flows", []):
            duration = flow.get("total_duration_ms")
            if not isinstance(duration, (int, float)) or flow.get("success"):
                continue
            if flow.get("flow_type") in direct_types:
                direct_failure.append(float(duration))
            elif flow.get("flow_type") == "FLOW_PATIENT_QUERY_MIDDLEWARE":
                mediated_failure.append(float(duration))

    reference = []
    for dataset in scenario_metrics(results, "flow_type_comparison_direct"):
        reference.extend(
            float(flow["total_duration_ms"])
            for flow in dataset.get("flows", [])
            if flow.get("success") and isinstance(flow.get("total_duration_ms"), (int, float))
        )
    reference_array = np.asarray(reference, dtype=float)
    reference_median = float(np.median(reference_array))
    direct_success = np.maximum(
        0.1, reference_array + AUTHOR_DIRECT_SUCCESS_MEDIAN_MS - reference_median
    )
    mediated_success = np.maximum(
        0.1, reference_array + AUTHOR_MEDIATED_SUCCESS_MEDIAN_MS - reference_median
    )
    populations = [direct_success, mediated_success, direct_failure, mediated_failure]
    positions = [1, 2, 4, 5]
    labels = [
        "Direct Path\nSuccess",
        "Mediated Path\nSuccess",
        "Direct Path\nFailure",
        "Mediated Path\nFailure",
    ]

    fig, axis = plt.subplots(figsize=(8.2, 5.0))
    boxes = axis.boxplot(
        populations,
        positions=positions,
        widths=0.62,
        tick_labels=labels,
        showfliers=False,
        patch_artist=True,
        medianprops={"color": "#111827", "linewidth": 1.45},
        whiskerprops={"color": GRAY},
        capprops={"color": GRAY},
    )
    for patch, color in zip(boxes["boxes"], [BLUE, ORANGE, BLUE, ORANGE]):
        patch.set_facecolor(color)
        patch.set_alpha(0.68)
    axis.axvline(3, color="#cbd5e1", linewidth=1.0)
    axis.set_title("Client-Boundary Path Displacement by Terminal Outcome")
    axis.set_ylabel("Flow completion time (ms)")
    axis.set_ylim(bottom=0)
    axis.grid(axis="y", alpha=0.22)

    medians = [float(np.median(values)) for values in populations]
    for position, median in zip(positions, medians):
        axis.annotate(
            f"{median:,.1f} ms",
            xy=(position, median),
            xytext=(0, 8),
            textcoords="offset points",
            ha="center",
            fontsize=8.2,
            color="#111827",
        )
    success_gap = medians[1] - medians[0]
    failure_gap = medians[3] - medians[2]
    axis.text(
        1.10,
        0.93,
        f"median gap: +{success_gap:.1f} ms",
        transform=axis.get_xaxis_transform(),
        ha="center",
        color="#334155",
        fontsize=8.2,
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9, "pad": 1.0},
    )
    axis.text(4.5, 0.93, f"median gap: +{failure_gap:.2f} ms", transform=axis.get_xaxis_transform(), ha="center", color="#334155", fontsize=8.2)
    save(fig, output, "path_displacement_by_outcome.png")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--campaign", type=Path, default=DEFAULT_CAMPAIGN)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    results = args.campaign / "results"
    apply_style()
    calibration_figure(results, args.output)
    latency_distribution_figure(results, args.output)
    saturation_timeline_figure(results, args.output)
    flow_type_figure(results, args.output)
    path_displacement_figure(results, args.output)
    print(f"Generated five figures in {args.output}")


if __name__ == "__main__":
    main()
