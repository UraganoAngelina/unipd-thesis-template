#!/usr/bin/env python3
"""Replace the experimental namespace in the unified Graphify graph."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from graphify.validate import assert_valid


NAMESPACE = "experiments"
PREFIX = f"{NAMESPACE}::"


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def prefix_node(node: dict) -> dict:
    result = dict(node)
    local_id = node["id"]
    result.pop("community", None)
    result.pop("community_name", None)
    result["repo"] = NAMESPACE
    result["local_id"] = local_id
    result["id"] = f"{PREFIX}{local_id}"
    return result


def prefix_edge(edge: dict) -> dict:
    result = dict(edge)
    result["source"] = f"{PREFIX}{edge['source']}"
    result["target"] = f"{PREFIX}{edge['target']}"
    return result


def prefix_hyperedge(hyperedge: dict) -> dict:
    result = dict(hyperedge)
    result["id"] = f"{PREFIX}{hyperedge['id']}"
    result["nodes"] = [f"{PREFIX}{node_id}" for node_id in hyperedge.get("nodes", [])]
    result["repo"] = NAMESPACE
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("experiment_graph", type=Path)
    parser.add_argument("unified_graph", type=Path)
    args = parser.parse_args()

    experiment = read_json(args.experiment_graph)
    unified = read_json(args.unified_graph)
    assert_valid(experiment)
    assert_valid(unified)

    retained_nodes = [node for node in unified.get("nodes", []) if not node["id"].startswith(PREFIX)]
    experiment_nodes = [prefix_node(node) for node in experiment.get("nodes", [])]
    nodes = retained_nodes + experiment_nodes
    valid_ids = {node["id"] for node in nodes}

    retained_links = []
    for edge in unified.get("links", unified.get("edges", [])):
        source_is_experiment = edge["source"].startswith(PREFIX)
        target_is_experiment = edge["target"].startswith(PREFIX)
        if source_is_experiment and target_is_experiment:
            continue
        if edge["source"] in valid_ids and edge["target"] in valid_ids:
            retained_links.append(edge)
    experiment_links = [prefix_edge(edge) for edge in experiment.get("links", experiment.get("edges", []))]

    retained_hyperedges = [
        hyperedge
        for hyperedge in unified.get("hyperedges", unified.get("graph", {}).get("hyperedges", []))
        if not hyperedge.get("id", "").startswith(PREFIX)
        and not any(node_id.startswith(PREFIX) for node_id in hyperedge.get("nodes", []))
    ]
    experiment_hyperedges = [
        prefix_hyperedge(hyperedge)
        for hyperedge in experiment.get("hyperedges", experiment.get("graph", {}).get("hyperedges", []))
    ]

    unified["nodes"] = nodes
    unified["links"] = retained_links + experiment_links
    unified.pop("edges", None)
    unified["hyperedges"] = retained_hyperedges + experiment_hyperedges
    unified.setdefault("graph", {})["hyperedges"] = unified["hyperedges"]
    args.unified_graph.write_text(
        json.dumps(unified, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(
        f"Synced {len(experiment_nodes)} experimental nodes and "
        f"{len(experiment_links)} experimental edges into the unified graph."
    )


if __name__ == "__main__":
    main()
