#!/usr/bin/env python3
"""Merge one Graphify document fragment and refresh its unified namespace.

The unified graph is a composition of independently generated graphs.  This
utility replaces only the ``graphify_kb`` namespace, retaining code and
experimental nodes as well as valid cross-namespace bridge edges.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from graphify.build import build_merge
from graphify.cluster import cluster
from graphify.detect import save_manifest
from graphify.export import to_json
from graphify.validate import assert_valid


DOC_NAMESPACE = "graphify_kb"
DOC_PREFIX = f"{DOC_NAMESPACE}::"
BRIDGE_SOURCE = "knowledge_base/unified_graph/README.md"
SCRYBA_BRIDGES = [
    (
        "Request-Dataset-Generator::rve_transactions_scrybasign_get_user_info",
        f"{DOC_PREFIX}scryba_sign_3_x_developer_s_guide_getuserinfo4",
        "implements",
    ),
    (
        "Request-Dataset-Generator::rve_transactions_scrybasign_sign_one_doc",
        f"{DOC_PREFIX}scryba_sign_3_x_developer_s_guide_signonedoc",
        "implements",
    ),
    (
        "Request-Dataset-Generator::rve_transactions_scrybasign_common",
        f"{DOC_PREFIX}scryba_sign_3_x_developer_s_guide_soap_wsdl_integration",
        "implements",
    ),
    (
        "Request-Dataset-Generator::rve_transactions_scrybasign_common_resolve_auth_header",
        f"{DOC_PREFIX}scryba_sign_3_x_developer_s_guide_https_basic_authentication",
        "implements",
    ),
]


def _read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _write_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


def _prefix_node(node: dict) -> dict:
    prefixed = dict(node)
    local_id = node["id"]
    prefixed.pop("community", None)
    prefixed.pop("community_name", None)
    prefixed["repo"] = DOC_NAMESPACE
    prefixed["local_id"] = local_id
    prefixed["id"] = f"{DOC_PREFIX}{local_id}"
    return prefixed


def _prefix_edge(edge: dict) -> dict:
    prefixed = dict(edge)
    prefixed["source"] = f"{DOC_PREFIX}{edge['source']}"
    prefixed["target"] = f"{DOC_PREFIX}{edge['target']}"
    return prefixed


def _prefix_hyperedge(hyperedge: dict) -> dict:
    prefixed = dict(hyperedge)
    prefixed["id"] = f"{DOC_PREFIX}{hyperedge['id']}"
    prefixed["nodes"] = [f"{DOC_PREFIX}{node_id}" for node_id in hyperedge.get("nodes", [])]
    prefixed["repo"] = DOC_NAMESPACE
    return prefixed


def _prefix_source_hyperedge(hyperedge: dict, namespace: str) -> dict:
    prefixed = dict(hyperedge)
    prefix = f"{namespace}::"
    prefixed["id"] = f"{prefix}{hyperedge['id']}"
    prefixed["nodes"] = [f"{prefix}{node_id}" for node_id in hyperedge.get("nodes", [])]
    prefixed["repo"] = namespace
    return prefixed


def _bridge_edge(source: str, target: str, relation: str) -> dict:
    return {
        "source": source,
        "target": target,
        "relation": relation,
        "confidence": "INFERRED",
        "confidence_score": 0.95,
        "source_file": BRIDGE_SOURCE,
        "source_location": None,
        "weight": 1.0,
        "_origin": "unified_bridge",
    }


def update_document_graph(fragment_path: Path, document_root: Path, document_graph: Path) -> dict:
    fragment = _read_json(fragment_path)
    assert_valid(fragment)

    graph = build_merge(
        [fragment],
        graph_path=document_graph,
        directed=False,
        # Synchronous and asynchronous workflows are distinct concepts even
        # though their labels are lexically similar; fuzzy LLM-style deduplication
        # would incorrectly collapse them.
        dedup=False,
        root=document_root,
    )
    communities = cluster(graph)
    to_json(graph, communities, str(document_graph), force=True)

    source_pdf = document_root / "Scryba Sign 3.x Developer's Guide.pdf"
    save_manifest(
        {"paper": [str(source_pdf)]},
        manifest_path=str(document_graph.parent / "manifest.json"),
        kind="both",
        root=document_root,
    )
    return _read_json(document_graph)


def update_unified_graph(
    document_data: dict,
    unified_graph: Path,
    experiment_graph: Path | None = None,
) -> tuple[int, int]:
    unified = _read_json(unified_graph)
    old_nodes = unified.get("nodes", [])
    old_links = unified.get("links", unified.get("edges", []))

    preserved_nodes = [node for node in old_nodes if not node["id"].startswith(DOC_PREFIX)]
    document_nodes = [_prefix_node(node) for node in document_data.get("nodes", [])]
    valid_ids = {node["id"] for node in preserved_nodes + document_nodes}

    preserved_links = []
    for edge in old_links:
        source_is_doc = edge["source"].startswith(DOC_PREFIX)
        target_is_doc = edge["target"].startswith(DOC_PREFIX)
        if source_is_doc and target_is_doc:
            continue
        if edge["source"] in valid_ids and edge["target"] in valid_ids:
            preserved_links.append(edge)
    document_links = [_prefix_edge(edge) for edge in document_data.get("links", [])]
    bridge_links = [
        _bridge_edge(source, target, relation)
        for source, target, relation in SCRYBA_BRIDGES
        if source in valid_ids and target in valid_ids
    ]
    merged_links = preserved_links + document_links + bridge_links
    deduplicated_links = []
    seen_link_keys = set()
    for edge in merged_links:
        key = (edge["source"], edge["target"], edge.get("relation"))
        if key in seen_link_keys:
            continue
        seen_link_keys.add(key)
        deduplicated_links.append(edge)

    old_hyperedges = unified.get("hyperedges", unified.get("graph", {}).get("hyperedges", []))
    preserved_hyperedges = [
        hyperedge
        for hyperedge in old_hyperedges
        if not hyperedge.get("id", "").startswith(DOC_PREFIX)
        and not any(node_id.startswith(DOC_PREFIX) for node_id in hyperedge.get("nodes", []))
    ]
    document_hyperedges = [
        _prefix_hyperedge(hyperedge)
        for hyperedge in document_data.get(
            "hyperedges", document_data.get("graph", {}).get("hyperedges", [])
        )
    ]
    experiment_hyperedges = []
    if experiment_graph is not None:
        experiment_data = _read_json(experiment_graph)
        experiment_prefix = "experiments::"
        preserved_hyperedges = [
            hyperedge
            for hyperedge in preserved_hyperedges
            if not hyperedge.get("id", "").startswith(experiment_prefix)
            and not any(
                node_id.startswith(experiment_prefix)
                for node_id in hyperedge.get("nodes", [])
            )
        ]
        experiment_hyperedges = [
            _prefix_source_hyperedge(hyperedge, "experiments")
            for hyperedge in experiment_data.get(
                "hyperedges", experiment_data.get("graph", {}).get("hyperedges", [])
            )
        ]

    unified["nodes"] = preserved_nodes + document_nodes
    unified["links"] = deduplicated_links
    unified.pop("edges", None)
    all_hyperedges = preserved_hyperedges + document_hyperedges + experiment_hyperedges
    unified["hyperedges"] = all_hyperedges
    unified.setdefault("graph", {})["hyperedges"] = all_hyperedges

    _write_json(unified_graph, unified)
    return len(document_nodes), len(document_links)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("fragment", type=Path)
    parser.add_argument("document_root", type=Path)
    parser.add_argument("unified_graph", type=Path)
    parser.add_argument("--experiment-graph", type=Path)
    args = parser.parse_args()

    document_root = args.document_root.resolve()
    document_graph = document_root / "graphify-out" / "graph.json"
    document_data = update_document_graph(args.fragment.resolve(), document_root, document_graph)
    experiment_graph = args.experiment_graph.resolve() if args.experiment_graph else None
    node_count, edge_count = update_unified_graph(
        document_data,
        args.unified_graph.resolve(),
        experiment_graph,
    )
    print(
        f"Document graph: {len(document_data.get('nodes', []))} nodes, "
        f"{len(document_data.get('links', []))} edges; "
        f"unified document namespace: {node_count} nodes, {edge_count} edges."
    )


if __name__ == "__main__":
    main()
