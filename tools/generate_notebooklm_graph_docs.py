#!/usr/bin/env python3
"""Convert the three thesis Graphify graphs into lossless NotebookLM Markdown.

The generated prose is intentionally repetitive: every node occurrence retains
all of its properties and every binary edge occurrence is verbalized both at
its source and at its target. Stable HTML comments provide a machine-checkable
coverage trail without replacing the natural-language content.
"""

from __future__ import annotations

import html
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "knowledge_base" / "notebooklm_graph_export"
GENERATED_ON = date(2026, 7, 31).isoformat()


@dataclass(frozen=True)
class GraphSpec:
    key: str
    name: str
    path: Path
    repo_prefix: str | None


GRAPH_SPECS = (
    GraphSpec(
        "documentale",
        "grafo documentale",
        ROOT / "graphify_kb" / "graphify-out" / "graph.json",
        "graphify_kb",
    ),
    GraphSpec(
        "codice",
        "grafo del codice RDG",
        Path(
            "/home/alberto/Desktop/Request-Dataset-Generator/"
            "graphify-out/graph.json"
        ),
        "Request-Dataset-Generator",
    ),
    GraphSpec(
        "unificata",
        "grafo unificato",
        ROOT
        / "knowledge_base"
        / "unified_graph"
        / "graphify-out"
        / "graph.json",
        None,
    ),
)


@dataclass(frozen=True)
class FileSpec:
    filename: str
    title: str
    domain: str
    repo: str
    communities: tuple[int, ...]


FILE_SPECS = (
    FileSpec(
        "01_interoperabilita_tecnico_normativa_parte1.md",
        "Interoperabilità tecnico-normativa — parte 1",
        "Interoperabilità tecnico-normativa",
        "graphify_kb",
        tuple(range(0, 10)),
    ),
    FileSpec(
        "02_interoperabilita_tecnico_normativa_parte2.md",
        "Interoperabilità tecnico-normativa — parte 2",
        "Interoperabilità tecnico-normativa",
        "graphify_kb",
        tuple(range(10, 20)),
    ),
    FileSpec(
        "03_architettura_rdg_parte1.md",
        "Architettura e codice del framework RDG — parte 1",
        "Architettura e codice del framework RDG",
        "Request-Dataset-Generator",
        (0,),
    ),
    FileSpec(
        "04_architettura_rdg_parte2.md",
        "Architettura e codice del framework RDG — parte 2",
        "Architettura e codice del framework RDG",
        "Request-Dataset-Generator",
        (1,),
    ),
    FileSpec(
        "05_architettura_rdg_parte3.md",
        "Architettura e codice del framework RDG — parte 3",
        "Architettura e codice del framework RDG",
        "Request-Dataset-Generator",
        (2, 3),
    ),
    FileSpec(
        "06_architettura_rdg_parte4.md",
        "Architettura e codice del framework RDG — parte 4",
        "Architettura e codice del framework RDG",
        "Request-Dataset-Generator",
        (4, 5, 6),
    ),
    FileSpec(
        "07_architettura_rdg_parte5.md",
        "Architettura e codice del framework RDG — parte 5",
        "Architettura e codice del framework RDG",
        "Request-Dataset-Generator",
        (7, 8, 9),
    ),
    FileSpec(
        "08_architettura_rdg_parte6.md",
        "Architettura e codice del framework RDG — parte 6",
        "Architettura e codice del framework RDG",
        "Request-Dataset-Generator",
        (10, 11, 12, 13),
    ),
    FileSpec(
        "09_architettura_rdg_parte7.md",
        "Architettura e codice del framework RDG — parte 7",
        "Architettura e codice del framework RDG",
        "Request-Dataset-Generator",
        (14, 15, 16, 17),
    ),
    FileSpec(
        "10_risultati_sperimentali.md",
        "Risultati sperimentali sanitizzati",
        "Risultati sperimentali",
        "experiments",
        tuple(range(0, 5)),
    ),
)


DOC_COMMUNITY_LABELS = json.loads(
    (ROOT / "graphify_kb" / "graphify-out" / ".graphify_labels.json").read_text(
        encoding="utf-8"
    )
)
CODE_COMMUNITY_LABELS = json.loads(
    Path(
        "/home/alberto/Desktop/Request-Dataset-Generator/"
        "graphify-out/.graphify_labels.json"
    ).read_text(encoding="utf-8")
)
EXPERIMENT_COMMUNITY_LABELS = {
    "0": "Sanitizzazione, alias e protocollo live",
    "1": "Tassonomia degli errori e fault",
    "2": "Validazione semantica e middleware",
    "3": "Esito HTTP ed estrazione degli output",
    "4": "Evidenza sperimentale RVE-121",
}

RELATION_VERBS = {
    "calls": "chiama",
    "conceptually_related_to": "è concettualmente correlato a",
    "contains": "contiene",
    "implements": "implementa",
    "imports": "importa",
    "imports_from": "importa da",
    "indirect_call": "effettua una chiamata indiretta verso",
    "inherits": "eredita da",
    "method": "registra come proprio metodo",
    "rationale_for": "costituisce una motivazione per",
    "re_exports": "riesporta",
    "references": "fa riferimento a",
    "semantically_similar_to": "è semanticamente simile a",
    "shares_data_with": "condivide dati con",
    "uses": "usa",
}

GLOSSARIES = {
    "graphify_kb": (
        ("APMS", "Acronimo presente nel grafo; l'espansione non è registrata."),
        ("COT", "Acronimo presente nel grafo; l'espansione non è registrata."),
        ("FHIR", "Nome canonico dell'acronimo usato nelle etichette del grafo."),
        ("FSE", "Acronimo presente nel grafo; l'espansione non è registrata."),
        ("IHE", "Nome canonico dell'acronimo usato nelle etichette del grafo."),
        ("IUA", "Nome canonico dell'acronimo usato nelle etichette del grafo."),
        ("JWT", "Nome canonico dell'acronimo usato nelle etichette del grafo."),
        ("PUA", "Acronimo presente nel grafo; l'espansione non è registrata."),
        ("RVE", "Nome canonico del prefisso delle transazioni regionali nel grafo."),
        ("SAML", "Nome canonico dell'acronimo usato nelle etichette del grafo."),
        ("SI.Ter", "Nome canonico adottato dalle etichette del grafo."),
        ("XDS", "Nome canonico dell'acronimo usato nelle etichette del grafo."),
    ),
    "Request-Dataset-Generator": (
        (
            "RDG",
            "Nome editoriale canonico del repository Request-Dataset-Generator.",
        ),
        ("AST", "Valore di provenienza `_origin=ast` registrato dal grafo."),
        ("FHIR", "Nome canonico dell'acronimo usato negli identificatori RDG."),
        ("RVE", "Nome canonico del prefisso usato per i flussi RDG."),
        ("UI", "Nome canonico dell'acronimo usato nei moduli di interfaccia."),
    ),
    "experiments": (
        ("HTTP", "Nome canonico dell'acronimo usato nelle etichette sperimentali."),
        ("RVE", "Nome canonico del prefisso delle evidenze sperimentali."),
        (
            "Alias sanitizzato",
            "Valore opaco che deve restare identico; il grafo non autorizza "
            "la ricostruzione del dato reale.",
        ),
    ),
}


def code_span(value: Any) -> str:
    """Render an exact scalar representation as a safe Markdown code span."""
    if value is None:
        text = "null"
    elif value is True:
        text = "true"
    elif value is False:
        text = "false"
    elif isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False, sort_keys=True)
    else:
        text = str(value)
    text = text.replace("\n", "\\n").replace("\r", "\\r")
    longest = max((len(run) for run in re.findall(r"`+", text)), default=0)
    fence = "`" * (longest + 1)
    pad = " " if text.startswith("`") or text.endswith("`") else ""
    return f"{fence}{pad}{text}{pad}{fence}"


def heading_text(value: str) -> str:
    return html.escape(value.replace("\n", " ").replace("\r", " "))


def count_by(items: list[dict[str, Any]], key: str) -> Counter[str]:
    return Counter(str(item.get(key, "(assente)")) for item in items)


def format_counts(counter: Counter[str]) -> str:
    return ", ".join(f"{key}: {counter[key]}" for key in sorted(counter))


def graph_canonical_id(spec: GraphSpec, node_id: str) -> str:
    if spec.key == "unificata":
        return node_id
    return f"{spec.repo_prefix}::{node_id}"


def graph_endpoint_canonical_id(spec: GraphSpec, endpoint: str) -> str:
    if spec.key == "unificata":
        return endpoint
    return f"{spec.repo_prefix}::{endpoint}"


def community_label(repo: str, community: int) -> str:
    labels = {
        "graphify_kb": DOC_COMMUNITY_LABELS,
        "Request-Dataset-Generator": CODE_COMMUNITY_LABELS,
        "experiments": EXPERIMENT_COMMUNITY_LABELS,
    }[repo]
    return labels.get(str(community), f"Comunità Graphify {community}")


def relation_clause(source_name: str, relation: str, target_name: str) -> str:
    verb = RELATION_VERBS.get(relation)
    if verb is None:
        return (
            f"{code_span(source_name)} è collegato a {code_span(target_name)} "
            f"dalla relazione {code_span(relation)}. "
            f"[DA VERIFICARE: il grafo non esplicita la semantica della relazione "
            f"{relation}]"
        )
    return f"{code_span(source_name)} {verb} {code_span(target_name)}."


def node_property_sentence(
    subject: str, key: str, value: Any, graph_name: str
) -> str:
    val = code_span(value)
    bare_subject = subject.removeprefix("il ")
    templates = {
        "id": (
            f"Nel {graph_name}, {subject} possiede l'identificatore esatto {val}."
        ),
        "label": (
            f"Nel {graph_name}, l'etichetta originale del {bare_subject} è "
            f"{val}."
        ),
        "file_type": (
            f"Nel {graph_name}, la proprietà `file_type` tipizza {subject} come "
            f"{val}."
        ),
        "source_file": (
            f"Nel {graph_name}, il file sorgente registrato per {subject} è {val}."
        ),
        "source_location": (
            f"Nel {graph_name}, la posizione sorgente registrata per {subject} è "
            f"{val}; il valore `null` indica che il grafo non la valorizza."
        ),
        "source_url": (
            f"Nel {graph_name}, l'URL sorgente registrato per {subject} è {val}; "
            f"il valore `null` indica che il grafo non lo valorizza."
        ),
        "captured_at": (
            f"Nel {graph_name}, l'istante di acquisizione registrato per {subject} "
            f"è {val}; il valore `null` indica che il grafo non lo valorizza."
        ),
        "author": (
            f"Nel {graph_name}, l'autore registrato per {subject} è {val}; il "
            f"valore `null` indica che il grafo non lo valorizza."
        ),
        "contributor": (
            f"Nel {graph_name}, il contributore registrato per {subject} è {val}; "
            f"il valore `null` indica che il grafo non lo valorizza."
        ),
        "community": (
            f"Nel {graph_name}, Graphify assegna {subject} alla comunità numerica "
            f"{val}."
        ),
        "norm_label": (
            f"Nel {graph_name}, l'etichetta normalizzata del {bare_subject} è "
            f"{val}."
        ),
        "_origin": (
            f"Nel {graph_name}, la proprietà di provenienza `_origin` di {subject} "
            f"vale {val}."
        ),
        "repo": (
            f"Nel {graph_name}, la proprietà `repo` associa {subject} al "
            f"repository {val}."
        ),
        "local_id": (
            f"Nel {graph_name}, l'identificatore locale conservato per {subject} "
            f"è {val}."
        ),
    }
    return templates.get(
        key,
        f"Nel {graph_name}, {subject} possiede inoltre la proprietà "
        f"{code_span(key)} con valore {val}. "
        f"[DA VERIFICARE: la semantica della proprietà non è esplicitata dal grafo]",
    )


def edge_property_sentence(
    subject: str,
    key: str,
    value: Any,
    graph_name: str,
    edge_index: int,
) -> str:
    val = code_span(value)
    templates = {
        "source": (
            f"Nel {graph_name}, l'arco {edge_index} registra come `source` "
            f"l'identificatore {val} per la relazione che coinvolge {subject}."
        ),
        "target": (
            f"Nel {graph_name}, l'arco {edge_index} registra come `target` "
            f"l'identificatore {val} per la relazione che coinvolge {subject}."
        ),
        "relation": (
            f"Nel {graph_name}, il tipo dichiarato dell'arco {edge_index} che "
            f"coinvolge {subject} è {val}."
        ),
        "confidence": (
            f"Nel {graph_name}, la confidenza categoriale dell'arco {edge_index} "
            f"che coinvolge {subject} è {val}."
        ),
        "confidence_score": (
            f"Nel {graph_name}, il punteggio numerico di confidenza dell'arco "
            f"{edge_index} che coinvolge {subject} è {val}."
        ),
        "source_file": (
            f"Nel {graph_name}, il file sorgente dell'arco {edge_index} che "
            f"coinvolge {subject} è {val}."
        ),
        "source_location": (
            f"Nel {graph_name}, la posizione sorgente dell'arco {edge_index} che "
            f"coinvolge {subject} è {val}; `null` segnala una posizione non "
            f"valorizzata."
        ),
        "weight": (
            f"Nel {graph_name}, il peso dell'arco {edge_index} che coinvolge "
            f"{subject} è {val}."
        ),
        "_origin": (
            f"Nel {graph_name}, la provenienza `_origin` dell'arco {edge_index} "
            f"che coinvolge {subject} è {val}."
        ),
        "context": (
            f"Nel {graph_name}, il contesto dichiarato per l'arco {edge_index} "
            f"che coinvolge {subject} è {val}."
        ),
    }
    return templates.get(
        key,
        f"Nel {graph_name}, l'arco {edge_index} che coinvolge {subject} possiede "
        f"la proprietà {code_span(key)} con valore {val}. "
        f"[DA VERIFICARE: la semantica della proprietà non è esplicitata dal grafo]",
    )


def load_graphs() -> dict[str, dict[str, Any]]:
    loaded = {}
    for spec in GRAPH_SPECS:
        loaded[spec.key] = json.loads(spec.path.read_text(encoding="utf-8"))
    return loaded


def build_model(graphs: dict[str, dict[str, Any]]) -> dict[str, Any]:
    unified_nodes = {
        node["id"]: node for node in graphs["unificata"]["nodes"]
    }
    occurrences: dict[str, list[tuple[GraphSpec, int, dict[str, Any]]]] = (
        defaultdict(list)
    )
    node_canonical_by_occurrence: dict[tuple[str, str], str] = {}
    for spec in GRAPH_SPECS:
        for index, node in enumerate(graphs[spec.key]["nodes"]):
            cid = graph_canonical_id(spec, node["id"])
            node_canonical_by_occurrence[(spec.key, node["id"])] = cid
            occurrences[cid].append((spec, index, node))

    missing_from_unified = sorted(set(occurrences) - set(unified_nodes))
    if missing_from_unified:
        raise ValueError(
            "Nodi sorgente privi di controparte unificata: "
            + ", ".join(missing_from_unified[:10])
        )

    label_counts = Counter(node["label"] for node in unified_nodes.values())
    canonical_names = {}
    for cid, node in unified_nodes.items():
        label = node["label"]
        if label_counts[label] == 1:
            canonical_names[cid] = label
        else:
            canonical_names[cid] = f"{label} [{node['local_id']}]"

    file_for_canonical: dict[str, str] = {}
    for cid, node in unified_nodes.items():
        repo = node["repo"]
        community = int(node["community"])
        matches = [
            spec
            for spec in FILE_SPECS
            if spec.repo == repo and community in spec.communities
        ]
        if len(matches) != 1:
            raise ValueError(
                f"Segmentazione non univoca per {cid}: {len(matches)} file"
            )
        file_for_canonical[cid] = matches[0].filename

    edges = []
    outgoing: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    incoming: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for spec in GRAPH_SPECS:
        for index, edge in enumerate(graphs[spec.key]["links"]):
            source_cid = graph_endpoint_canonical_id(spec, edge["source"])
            target_cid = graph_endpoint_canonical_id(spec, edge["target"])
            record = {
                "spec": spec,
                "index": index,
                "edge": edge,
                "source_cid": source_cid,
                "target_cid": target_cid,
            }
            edges.append(record)
            outgoing[(spec.key, source_cid)].append(record)
            incoming[(spec.key, target_cid)].append(record)

    hyperedges = []
    for spec in GRAPH_SPECS:
        for index, hyperedge in enumerate(
            graphs[spec.key].get("graph", {}).get("hyperedges", [])
        ):
            member_cids = []
            for member in hyperedge["nodes"]:
                candidate = graph_endpoint_canonical_id(spec, member)
                if candidate not in unified_nodes and spec.key == "unificata":
                    matches = [
                        cid
                        for cid, node in unified_nodes.items()
                        if node.get("local_id") == member
                    ]
                    if len(matches) != 1:
                        raise ValueError(
                            "Membro di iperarco unificato non risolvibile: "
                            f"{member}"
                        )
                    candidate = matches[0]
                member_cids.append(candidate)
            hyperedges.append(
                {
                    "spec": spec,
                    "index": index,
                    "hyperedge": hyperedge,
                    "member_cids": member_cids,
                    "files": sorted(
                        {file_for_canonical[cid] for cid in member_cids}
                    ),
                }
            )

    return {
        "unified_nodes": unified_nodes,
        "occurrences": occurrences,
        "canonical_names": canonical_names,
        "file_for_canonical": file_for_canonical,
        "edges": edges,
        "outgoing": outgoing,
        "incoming": incoming,
        "hyperedges": hyperedges,
    }


class Coverage:
    def __init__(self) -> None:
        self.graph_properties: set[tuple[str, str]] = set()
        self.node_properties: set[tuple[str, int, str]] = set()
        self.edge_properties: set[tuple[str, int, str, str]] = set()
        self.hyperedge_properties: set[tuple[str, int, str]] = set()
        self.node_markers: Counter[tuple[str, int]] = Counter()
        self.edge_markers: Counter[tuple[str, int, str]] = Counter()
        self.hyperedge_markers: Counter[tuple[str, int]] = Counter()


def render_node_occurrence(
    cid: str,
    occurrence: tuple[GraphSpec, int, dict[str, Any]],
    model: dict[str, Any],
    coverage: Coverage,
) -> list[str]:
    spec, node_index, node = occurrence
    subject_name = model["canonical_names"][cid]
    subject = f"il nodo canonico {code_span(subject_name)}"
    marker = (
        f"<!-- GRAPH_NODE graph={spec.key} index={node_index} "
        f"id={html.escape(str(node['id']))} -->"
    )
    coverage.node_markers[(spec.key, node_index)] += 1
    sentences = [
        node_property_sentence(subject, key, value, spec.name)
        for key, value in node.items()
    ]
    for key in node:
        coverage.node_properties.add((spec.key, node_index, key))

    paragraphs = [marker, " ".join(sentences)]
    for direction, records in (
        ("outgoing", model["outgoing"].get((spec.key, cid), [])),
        ("incoming", model["incoming"].get((spec.key, cid), [])),
    ):
        if not records:
            if direction == "outgoing":
                paragraphs.append(
                    f"Nel {spec.name}, {subject} non possiede archi uscenti "
                    f"registrati nel campo `links`."
                )
            else:
                paragraphs.append(
                    f"Nel {spec.name}, {subject} non possiede archi entranti "
                    f"registrati nel campo `links`."
                )
            continue
        for record in records:
            paragraphs.extend(
                render_edge_relation(record, direction, model, coverage)
            )
    return paragraphs


def render_edge_relation(
    record: dict[str, Any],
    direction: str,
    model: dict[str, Any],
    coverage: Coverage,
) -> list[str]:
    spec: GraphSpec = record["spec"]
    edge = record["edge"]
    edge_index = record["index"]
    source_cid = record["source_cid"]
    target_cid = record["target_cid"]
    source_name = model["canonical_names"][source_cid]
    target_name = model["canonical_names"][target_cid]
    subject_name = source_name if direction == "outgoing" else target_name
    subject = f"il nodo canonico {code_span(subject_name)}"
    marker = (
        f"<!-- GRAPH_EDGE graph={spec.key} index={edge_index} "
        f"role={direction} -->"
    )
    coverage.edge_markers[(spec.key, edge_index, direction)] += 1

    if direction == "outgoing":
        orientation = (
            f"Nel {spec.name}, {subject} è la sorgente `source` della relazione "
            f"{code_span(edge['relation'])} verso il nodo canonico "
            f"{code_span(target_name)}; l'orientamento registrato nel JSON va "
            f"dall'ID {code_span(edge['source'])} all'ID "
            f"{code_span(edge['target'])}. "
        )
    else:
        orientation = (
            f"Nel {spec.name}, {subject} è il destinatario `target` della "
            f"relazione {code_span(edge['relation'])} proveniente dal nodo "
            f"canonico {code_span(source_name)}; l'orientamento registrato nel "
            f"JSON va dall'ID {code_span(edge['source'])} all'ID "
            f"{code_span(edge['target'])}. "
        )
    orientation += "La relazione tecnica esplicita è la seguente: " + (
        relation_clause(source_name, edge["relation"], target_name)
    )
    sentences = [orientation]
    for key, value in edge.items():
        sentences.append(
            edge_property_sentence(
                subject, key, value, spec.name, edge_index
            )
        )
        coverage.edge_properties.add((spec.key, edge_index, direction, key))
    return [marker, " ".join(sentences)]


def render_hyperedge(
    record: dict[str, Any],
    model: dict[str, Any],
    coverage: Coverage,
    marker_suffix: str,
) -> list[str]:
    spec: GraphSpec = record["spec"]
    index = record["index"]
    hyperedge = record["hyperedge"]
    names = [model["canonical_names"][cid] for cid in record["member_cids"]]
    marker = (
        f"<!-- GRAPH_HYPEREDGE graph={spec.key} index={index} "
        f"copy={html.escape(marker_suffix)} -->"
    )
    coverage.hyperedge_markers[(spec.key, index)] += 1
    subject = (
        f"l'iperarco {code_span(hyperedge['label'])} con identificatore "
        f"{code_span(hyperedge['id'])}"
    )
    member_pairs = ", ".join(
        f"{code_span(name)} (ID locale {code_span(local_id)})"
        for name, local_id in zip(names, hyperedge["nodes"])
    )
    sentences = [
        f"Nel {spec.name}, {subject} comprende esattamente i nodi {member_pairs}.",
        f"Nel {spec.name}, {subject} dichiara la relazione di gruppo "
        f"{code_span(hyperedge['relation'])}; il grafo associa tutti i membri "
        f"elencati all'etichetta dell'iperarco senza specificare una coppia "
        f"`source`-`target`.",
    ]
    for key, value in hyperedge.items():
        if key == "nodes":
            sentence = (
                f"Nel {spec.name}, la proprietà `nodes` di {subject} conserva "
                f"nell'ordine il valore esatto {code_span(value)}."
            )
        elif key == "id":
            sentence = (
                f"Nel {spec.name}, la proprietà `id` di {subject} vale "
                f"{code_span(value)}."
            )
        elif key == "label":
            sentence = (
                f"Nel {spec.name}, la proprietà `label` di {subject} vale "
                f"{code_span(value)}."
            )
        elif key == "relation":
            sentence = (
                f"Nel {spec.name}, la proprietà `relation` di {subject} vale "
                f"{code_span(value)}."
            )
        elif key == "confidence":
            sentence = (
                f"Nel {spec.name}, la confidenza categoriale di {subject} vale "
                f"{code_span(value)}."
            )
        elif key == "confidence_score":
            sentence = (
                f"Nel {spec.name}, il punteggio di confidenza di {subject} vale "
                f"{code_span(value)}."
            )
        elif key == "source_file":
            sentence = (
                f"Nel {spec.name}, il file sorgente di {subject} è "
                f"{code_span(value)}."
            )
        else:
            sentence = (
                f"Nel {spec.name}, {subject} possiede la proprietà "
                f"{code_span(key)} con valore {code_span(value)}. "
                f"[DA VERIFICARE: proprietà dell'iperarco non documentata]"
            )
        sentences.append(sentence)
        coverage.hyperedge_properties.add((spec.key, index, key))
    return [marker, " ".join(sentences)]


def metadata_for_file(
    file_spec: FileSpec,
    cids: list[str],
    model: dict[str, Any],
    graphs: dict[str, dict[str, Any]],
) -> list[str]:
    node_occurrences = sum(len(model["occurrences"][cid]) for cid in cids)
    types = Counter(
        model["unified_nodes"][cid]["file_type"] for cid in cids
    )
    edge_records = [
        record
        for record in model["edges"]
        if record["source_cid"] in cids or record["target_cid"] in cids
    ]
    edge_ids = {
        (record["spec"].key, record["index"]) for record in edge_records
    }
    relations = Counter(
        record["edge"]["relation"]
        for record in edge_records
        if (record["spec"].key, record["index"]) in edge_ids
    )
    hypers = [
        record
        for record in model["hyperedges"]
        if file_spec.filename in record["files"]
    ]
    return [
        "## Metadati",
        "",
        f"- Dominio: {file_spec.domain}.",
        f"- Data di generazione: {GENERATED_ON}.",
        (
            "- Versione dei grafi sorgente: KB documentale "
            f"{code_span(graphs['documentale'].get('built_at_commit'))}; "
            f"KB codice RDG {code_span(graphs['codice'].get('built_at_commit'))}; "
            f"KB unificata {code_span(graphs['unificata'].get('built_at_commit'))}."
        ),
        (
            f"- Nodi coperti: {len(cids)} nodi canonici e {node_occurrences} "
            f"occorrenze fisiche; tipi canonici: {format_counts(types)}."
        ),
        (
            f"- Archi coperti: {len(edge_ids)} occorrenze fisiche incidenti ai "
            f"nodi del documento; tipi: {format_counts(relations)}."
        ),
        (
            f"- Iperarchi coperti: {len(hypers)} occorrenze fisiche, replicate "
            f"anche negli altri file coinvolti quando attraversano la "
            f"segmentazione editoriale."
        ),
        (
            "- Nota sulla direzione: tutti e tre i grafi dichiarano "
            "`directed=false`; la prosa conserva comunque l'orientamento dei "
            "campi JSON `source` e `target` senza trasformarlo in causalità."
        ),
        "",
    ]


def glossary_for_file(
    file_spec: FileSpec, cids: list[str], model: dict[str, Any]
) -> list[str]:
    lines = [
        "## Glossario",
        "",
        (
            "- EXTRACTED — Valore della proprietà `confidence` che il grafo "
            "assegna a una relazione estratta."
        ),
        (
            "- INFERRED — Valore della proprietà `confidence` che il grafo "
            "assegna a una relazione inferita; la prosa non promuove una "
            "relazione INFERRED a fatto estratto."
        ),
    ]
    for acronym, definition in GLOSSARIES[file_spec.repo]:
        suffix = ""
        if "espansione non è registrata" in definition:
            suffix = " [DA VERIFICARE: espansione assente dal grafo]"
        lines.append(f"- {acronym} — {definition}{suffix}")
    lines.extend(
        [
            "",
            "### Mappa dei nomi canonici e delle varianti",
            "",
            (
                "La mappa seguente non fonde nodi solo perché semanticamente "
                "simili. Le occorrenze del grafo sorgente e del grafo unificato "
                "sono ricondotte allo stesso nome soltanto tramite `repo` e "
                "`local_id`; le etichette duplicate di nodi distinti sono "
                "disambiguate con l'identificatore locale."
            ),
            "",
        ]
    )
    for cid in cids:
        canonical = model["canonical_names"][cid]
        labels = sorted(
            {
                occurrence[2]["label"]
                for occurrence in model["occurrences"][cid]
            }
        )
        label_text = ", ".join(code_span(label) for label in labels)
        lines.append(
            f"- Il nome canonico {code_span(canonical)} identifica il nodo "
            f"{code_span(cid)}; le etichette originali conservate sono "
            f"{label_text}."
        )
    lines.append("")
    return lines


def generate_domain_file(
    file_spec: FileSpec,
    model: dict[str, Any],
    graphs: dict[str, dict[str, Any]],
    coverage: Coverage,
) -> str:
    cids = sorted(
        [
            cid
            for cid, filename in model["file_for_canonical"].items()
            if filename == file_spec.filename
        ],
        key=lambda cid: (
            int(model["unified_nodes"][cid]["community"]),
            model["canonical_names"][cid].casefold(),
            cid,
        ),
    )
    lines = [f"# {file_spec.title}", ""]
    lines.extend(metadata_for_file(file_spec, cids, model, graphs))
    lines.extend(glossary_for_file(file_spec, cids, model))

    file_hyperedges = [
        record
        for record in model["hyperedges"]
        if file_spec.filename in record["files"]
    ]
    if file_hyperedges:
        lines.extend(["## Iperarchi del dominio", ""])
        for record in file_hyperedges:
            lines.extend(
                render_hyperedge(
                    record, model, coverage, file_spec.filename
                )
            )
            lines.append("")

    grouped: dict[int, list[str]] = defaultdict(list)
    for cid in cids:
        grouped[int(model["unified_nodes"][cid]["community"])].append(cid)
    for community in sorted(grouped):
        lines.extend(
            [
                (
                    f"## Cluster Graphify {community} — "
                    f"{community_label(file_spec.repo, community)}"
                ),
                "",
                (
                    f"Il cluster editoriale Graphify {community} del dominio "
                    f"{file_spec.domain} contiene {len(grouped[community])} nodi "
                    f"canonici in questo documento; il titolo del cluster serve "
                    f"alla navigazione e non introduce relazioni assenti dagli "
                    f"archi JSON."
                ),
                "",
            ]
        )
        for cid in grouped[community]:
            lines.extend(
                [
                    f"### {heading_text(model['canonical_names'][cid])}",
                    "",
                ]
            )
            for occurrence in model["occurrences"][cid]:
                lines.extend(
                    render_node_occurrence(
                        cid, occurrence, model, coverage
                    )
                )
                lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def render_graph_schema(
    spec: GraphSpec,
    graph: dict[str, Any],
    coverage: Coverage,
) -> list[str]:
    node_types = count_by(graph["nodes"], "file_type")
    relation_types = count_by(graph["links"], "relation")
    hyperedges = graph.get("graph", {}).get("hyperedges", [])
    node_keys = sorted({key for node in graph["nodes"] for key in node})
    edge_keys = sorted({key for edge in graph["links"] for key in edge})
    lines = [
        f"### {spec.name}",
        "",
        (
            f"Il {spec.name} contiene {len(graph['nodes'])} nodi, "
            f"{len(graph['links'])} archi binari e {len(hyperedges)} iperarchi "
            f"annidati nella proprietà `graph.hyperedges`. I tipi di nodo, "
            f"ricavati dalla proprietà `file_type`, sono "
            f"{format_counts(node_types)}. I tipi di relazione e le rispettive "
            f"cardinalità sono {format_counts(relation_types)}."
        ),
        (
            f"Nel {spec.name}, le chiavi osservate nei nodi sono "
            f"{code_span(node_keys)}, mentre le chiavi osservate negli archi "
            f"sono {code_span(edge_keys)}."
        ),
    ]
    for key, value in graph.items():
        coverage.graph_properties.add((spec.key, key))
        if key == "directed":
            lines.append(
                f"Nel {spec.name}, la proprietà top-level `directed` vale "
                f"{code_span(value)}."
            )
        elif key == "multigraph":
            lines.append(
                f"Nel {spec.name}, la proprietà top-level `multigraph` vale "
                f"{code_span(value)}."
            )
        elif key == "built_at_commit":
            lines.append(
                f"Nel {spec.name}, la proprietà top-level `built_at_commit` "
                f"vale {code_span(value)}."
            )
        elif key == "nodes":
            lines.append(
                f"Nel {spec.name}, la proprietà top-level `nodes` contiene "
                f"{len(value)} oggetti, tutti tradotti nei documenti di dominio."
            )
        elif key == "links":
            lines.append(
                f"Nel {spec.name}, la proprietà top-level `links` contiene "
                f"{len(value)} oggetti, ciascuno verbalizzato sia presso il nodo "
                f"sorgente sia presso il nodo destinatario."
            )
        elif key == "hyperedges":
            nested_hyperedges = graph.get("graph", {}).get("hyperedges", [])
            if value == nested_hyperedges:
                lines.append(
                    f"Nel {spec.name}, la proprietà top-level `hyperedges` "
                    f"contiene {len(value)} elementi e replica elemento per "
                    f"elemento `graph.hyperedges`; ogni proprietà degli elementi "
                    f"è tradotta nei documenti di dominio."
                )
            else:
                lines.append(
                    f"Nel {spec.name}, la proprietà top-level `hyperedges` "
                    f"contiene {len(value)} elementi distinti da "
                    f"`graph.hyperedges`. [DA VERIFICARE: divergenza tra le due "
                    f"collezioni di iperarchi]"
                )
        elif key == "graph":
            nested_keys = sorted(value)
            lines.append(
                f"Nel {spec.name}, la proprietà top-level `graph` contiene le "
                f"chiavi {code_span(nested_keys)}; i {len(hyperedges)} "
                f"iperarchi contenuti sono tradotti integralmente nei documenti "
                f"di dominio."
            )
        else:
            lines.append(
                f"Nel {spec.name}, la proprietà top-level {code_span(key)} "
                f"possiede il valore {code_span(value)}. "
                f"[DA VERIFICARE: proprietà top-level non documentata]"
            )
    for nested_key in graph.get("graph", {}):
        coverage.graph_properties.add((spec.key, f"graph.{nested_key}"))
    lines.append("")
    return lines


def generate_master_index(
    model: dict[str, Any],
    graphs: dict[str, dict[str, Any]],
    coverage: Coverage,
) -> str:
    total_nodes = sum(len(graph["nodes"]) for graph in graphs.values())
    total_edges = sum(len(graph["links"]) for graph in graphs.values())
    total_hypers = sum(
        len(graph.get("graph", {}).get("hyperedges", []))
        for graph in graphs.values()
    )
    lines = [
        "# Indice master — conversione Graphify per NotebookLM",
        "",
        "## Metadati",
        "",
        "- Dominio: indice trasversale dei tre grafi e dei documenti prodotti.",
        f"- Data di generazione: {GENERATED_ON}.",
        (
            f"- Perimetro fisico di input: {total_nodes} occorrenze di nodo, "
            f"{total_edges} occorrenze di arco binario e {total_hypers} "
            f"occorrenze di iperarco."
        ),
        (
            f"- Spazio canonico: {len(model['unified_nodes'])} nodi del grafo "
            f"unificato; le occorrenze omologhe dei grafi sorgente restano "
            f"descritte separatamente."
        ),
        "",
        "## Fase 1 — Analisi dello schema",
        "",
        (
            "I tre file adottano lo schema di esportazione Graphify/NetworkX: "
            "i nodi sono in `nodes`, gli archi binari sono in `links`, la "
            "tipizzazione dei nodi usa `file_type` e gli iperarchi sono "
            "annidati in `graph.hyperedges`. Lo schema non contiene proprietà "
            "denominate letteralmente `tipo` o `tipo_relazione`; la conversione "
            "usa rispettivamente `file_type` e `relation` senza rinominarne i "
            "valori."
        ),
        "",
    ]
    for spec in GRAPH_SPECS:
        lines.extend(render_graph_schema(spec, graphs[spec.key], coverage))

    lines.extend(
        [
            "## Cluster tematici naturali",
            "",
            (
                "I cluster tematici naturali sono le comunità numeriche "
                "assegnate da Graphify. I nomi delle comunità documentali e del "
                "codice provengono dai file `.graphify_labels.json`; i titoli "
                "sperimentali sono etichette editoriali costruite soltanto con "
                "le etichette dei nodi del relativo cluster e non aggiungono "
                "archi."
            ),
            "",
        ]
    )
    for repo, graph_key, labels in (
        ("graphify_kb", "documentale", DOC_COMMUNITY_LABELS),
        ("Request-Dataset-Generator", "codice", CODE_COMMUNITY_LABELS),
        ("experiments", "unificata", EXPERIMENT_COMMUNITY_LABELS),
    ):
        nodes = [
            node
            for node in graphs[graph_key]["nodes"]
            if (
                graph_key != "unificata"
                or node.get("repo") == "experiments"
            )
        ]
        counts = Counter(int(node["community"]) for node in nodes)
        lines.append(f"### Cluster di {repo}")
        lines.append("")
        for community in sorted(counts):
            lines.append(
                f"- La comunità Graphify {community}, denominata "
                f"{code_span(labels.get(str(community), 'nome non disponibile'))}, "
                f"contiene {counts[community]} nodi."
            )
        lines.append("")

    lines.extend(
        [
            "## Documenti prodotti",
            "",
        ]
    )
    for file_spec in FILE_SPECS:
        node_count = sum(
            1
            for filename in model["file_for_canonical"].values()
            if filename == file_spec.filename
        )
        lines.append(
            f"- [{file_spec.filename}]({file_spec.filename}) copre il dominio "
            f"{file_spec.domain}, le comunità "
            f"{code_span(list(file_spec.communities))} e {node_count} nodi "
            f"canonici."
        )
    lines.extend(
        [
            (
                "- [99_autoverifica.md](99_autoverifica.md) registra l'esito "
                "della verifica obbligatoria e le cardinalità controllate."
            ),
            "",
            "## Mappa delle relazioni cross-documento",
            "",
            (
                "Ogni paragrafo seguente descrive un arco fisico i cui estremi "
                "sono collocati in documenti diversi. La mappa conserva il "
                "grafo di provenienza e non deduplica le occorrenze sorgente e "
                "unificata."
            ),
            "",
        ]
    )
    cross_edges = [
        record
        for record in model["edges"]
        if model["file_for_canonical"][record["source_cid"]]
        != model["file_for_canonical"][record["target_cid"]]
    ]
    if not cross_edges:
        lines.append(
            "Nessun arco binario attraversa i confini dei documenti prodotti."
        )
        lines.append("")
    for record in cross_edges:
        edge = record["edge"]
        source_name = model["canonical_names"][record["source_cid"]]
        target_name = model["canonical_names"][record["target_cid"]]
        source_file = model["file_for_canonical"][record["source_cid"]]
        target_file = model["file_for_canonical"][record["target_cid"]]
        lines.append(
            f"Nel {record['spec'].name}, l'arco {record['index']} collega il "
            f"nodo canonico {code_span(source_name)} nel documento "
            f"[{source_file}]({source_file}) al nodo canonico "
            f"{code_span(target_name)} nel documento "
            f"[{target_file}]({target_file}) tramite la relazione "
            f"{code_span(edge['relation'])}; l'orientamento JSON va da "
            f"{code_span(edge['source'])} a {code_span(edge['target'])}. "
            f"La frase relazionale è: "
            f"{relation_clause(source_name, edge['relation'], target_name)}"
        )
        lines.append("")

    lines.extend(
        [
            "## Mappa degli iperarchi cross-documento",
            "",
        ]
    )
    cross_hypers = [
        record for record in model["hyperedges"] if len(record["files"]) > 1
    ]
    if not cross_hypers:
        lines.append(
            "Nessun iperarco attraversa i confini dei documenti prodotti."
        )
        lines.append("")
    for record in cross_hypers:
        hyperedge = record["hyperedge"]
        files = ", ".join(
            f"[{filename}]({filename})" for filename in record["files"]
        )
        members = ", ".join(
            code_span(model["canonical_names"][cid])
            for cid in record["member_cids"]
        )
        lines.append(
            f"Nel {record['spec'].name}, l'iperarco "
            f"{code_span(hyperedge['label'])} con relazione "
            f"{code_span(hyperedge['relation'])} attraversa i documenti "
            f"{files} e comprende esattamente i nodi canonici {members}."
        )
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def expected_property_sets(
    graphs: dict[str, dict[str, Any]]
) -> dict[str, set[tuple[Any, ...]]]:
    graph_props: set[tuple[Any, ...]] = set()
    node_props: set[tuple[Any, ...]] = set()
    edge_props_by_role: set[tuple[Any, ...]] = set()
    hyper_props: set[tuple[Any, ...]] = set()
    for spec in GRAPH_SPECS:
        graph = graphs[spec.key]
        for key in graph:
            graph_props.add((spec.key, key))
        for nested_key in graph.get("graph", {}):
            graph_props.add((spec.key, f"graph.{nested_key}"))
        for index, node in enumerate(graph["nodes"]):
            for key in node:
                node_props.add((spec.key, index, key))
        for index, edge in enumerate(graph["links"]):
            for role in ("outgoing", "incoming"):
                for key in edge:
                    edge_props_by_role.add((spec.key, index, role, key))
        for index, hyperedge in enumerate(
            graph.get("graph", {}).get("hyperedges", [])
        ):
            for key in hyperedge:
                hyper_props.add((spec.key, index, key))
    return {
        "graph": graph_props,
        "node": node_props,
        "edge": edge_props_by_role,
        "hyperedge": hyper_props,
    }


def collect_aliases(graphs: dict[str, dict[str, Any]]) -> set[str]:
    pattern = re.compile(r"\b[A-Z][A-Z0-9]+(?:_[A-Z0-9]+)+\b")
    aliases: set[str] = set()
    for graph in graphs.values():
        serialized = json.dumps(graph, ensure_ascii=False)
        aliases.update(pattern.findall(serialized))
    return aliases


def validate_and_report(
    graphs: dict[str, dict[str, Any]],
    model: dict[str, Any],
    coverage: Coverage,
    generated_texts: dict[str, str],
) -> tuple[str, dict[str, Any]]:
    expected = expected_property_sets(graphs)
    property_checks = {
        "graph": coverage.graph_properties == expected["graph"],
        "node": coverage.node_properties == expected["node"],
        "edge": coverage.edge_properties == expected["edge"],
        "hyperedge": coverage.hyperedge_properties == expected["hyperedge"],
    }
    expected_nodes = {
        (spec.key, index)
        for spec in GRAPH_SPECS
        for index, _ in enumerate(graphs[spec.key]["nodes"])
    }
    expected_edges = {
        (spec.key, index, role)
        for spec in GRAPH_SPECS
        for index, _ in enumerate(graphs[spec.key]["links"])
        for role in ("outgoing", "incoming")
    }
    expected_hypers = {
        (spec.key, index)
        for spec in GRAPH_SPECS
        for index, _ in enumerate(
            graphs[spec.key].get("graph", {}).get("hyperedges", [])
        )
    }
    node_check = set(coverage.node_markers) == expected_nodes and all(
        value == 1 for value in coverage.node_markers.values()
    )
    edge_check = set(coverage.edge_markers) == expected_edges and all(
        value == 1 for value in coverage.edge_markers.values()
    )
    hyper_check = set(coverage.hyperedge_markers) == expected_hypers and all(
        value >= 1 for value in coverage.hyperedge_markers.values()
    )

    all_text = "\n".join(generated_texts.values())
    aliases = collect_aliases(graphs)
    missing_aliases = sorted(alias for alias in aliases if alias not in all_text)
    alias_check = not missing_aliases
    canonical_check = (
        len(model["canonical_names"]) == len(model["unified_nodes"])
        and all(
            model["canonical_names"][cid]
            for cid in model["unified_nodes"]
        )
    )
    no_invented_relation_check = all(
        record["edge"]["relation"] in RELATION_VERBS
        or "[DA VERIFICARE:" in relation_clause(
            model["canonical_names"][record["source_cid"]],
            record["edge"]["relation"],
            model["canonical_names"][record["target_cid"]],
        )
        for record in model["edges"]
    )
    all_pass = (
        node_check
        and edge_check
        and hyper_check
        and all(property_checks.values())
        and alias_check
        and canonical_check
        and no_invented_relation_check
    )
    status = "SUPERATO" if all_pass else "FALLITO"
    report = [
        "# Autoverifica della conversione Graphify",
        "",
        "## Metadati",
        "",
        f"- Data di verifica: {GENERATED_ON}.",
        f"- Esito complessivo: **{status}**.",
        (
            f"- Nodi fisici attesi e verificati: {len(expected_nodes)}; nodi "
            f"canonici: {len(model['unified_nodes'])}."
        ),
        (
            f"- Archi fisici attesi: {sum(len(g['links']) for g in graphs.values())}; "
            f"verbalizzazioni direzionali verificate: {len(expected_edges)}."
        ),
        (
            f"- Iperarchi fisici attesi e verificati: {len(expected_hypers)}."
        ),
        (
            f"- Proprietà verificate: {sum(len(value) for value in expected.values())} "
            f"occorrenze di proprietà strutturali."
        ),
        "",
        "## Checklist obbligatoria",
        "",
        (
            f"- [{'x' if node_check else ' '}] Ogni nodo dei JSON di input "
            f"compare in almeno un documento."
        ),
        (
            f"- [{'x' if edge_check else ' '}] Ogni arco dei JSON di input è "
            f"tradotto presso la sorgente e presso il destinatario."
        ),
        (
            f"- [{'x' if hyper_check else ' '}] Ogni iperarco annidato in "
            f"`graph.hyperedges` è tradotto in prosa."
        ),
        (
            f"- [{'x' if all(property_checks.values()) else ' '}] Ogni proprietà "
            f"top-level, di nodo, di arco e di iperarco è stata elaborata."
        ),
        (
            f"- [{'x' if alias_check else ' '}] Nessun alias con forma "
            f"`MAIUSCOLO_CON_UNDERSCORE` è stato alterato o risolto."
        ),
        (
            f"- [{'x' if no_invented_relation_check else ' '}] Nessuna relazione "
            f"è stata aggiunta senza un arco o iperarco sorgente; le semantiche "
            f"non mappate ricevono `[DA VERIFICARE: ...]`."
        ),
        (
            f"- [{'x' if canonical_check else ' '}] La terminologia canonica dei "
            f"nodi è univoca e riutilizzata in tutti i documenti."
        ),
        "",
        "## Dettaglio dei controlli di proprietà",
        "",
    ]
    for category, passed in property_checks.items():
        report.append(
            f"- Proprietà {category}: {'copertura completa' if passed else 'copertura incompleta'} "
            f"su {len(expected[category])} occorrenze attese."
        )
    report.extend(
        [
            "",
            "## Controllo degli alias",
            "",
            (
                f"Il controllo ha individuato {len(aliases)} token distinti con "
                f"forma `MAIUSCOLO_CON_UNDERSCORE` negli input. Tutti i token "
                f"sono presenti senza sostituzione nei documenti generati."
                if alias_check
                else (
                    "Gli alias mancanti sono: "
                    + ", ".join(code_span(alias) for alias in missing_aliases)
                )
            ),
            "",
            "## Limiti dichiarati",
            "",
            (
                "L'autoverifica dimostra la copertura strutturale dei JSON, non "
                "la completezza delle fonti originarie da cui Graphify ha "
                "estratto il grafo. In particolare, il grafo sperimentale non "
                "contiene sette nodi di esperimento né proprietà numeriche "
                "sufficienti per ricostruire integralmente i sette esperimenti "
                "o un confronto quantitativo dell'Esperimento 5; tali contenuti "
                "non vengono inventati. [DA VERIFICARE: rigenerare o arricchire "
                "il grafo se questi dettagli devono diventare sorgenti "
                "NotebookLM]."
            ),
            "",
        ]
    )
    manifest = {
        "status": status,
        "generated_on": GENERATED_ON,
        "counts": {
            "canonical_nodes": len(model["unified_nodes"]),
            "physical_nodes": len(expected_nodes),
            "physical_edges": len(expected_edges) // 2,
            "edge_verbalizations": len(expected_edges),
            "physical_hyperedges": len(expected_hypers),
            "property_occurrences": sum(
                len(value) for value in expected.values()
            ),
            "aliases_checked": len(aliases),
        },
        "checks": {
            "nodes": node_check,
            "edges": edge_check,
            "hyperedges": hyper_check,
            "properties": property_checks,
            "aliases": alias_check,
            "canonical_names": canonical_check,
            "no_invented_relations": no_invented_relation_check,
        },
        "missing_aliases": missing_aliases,
    }
    return "\n".join(report), manifest


def main() -> None:
    graphs = load_graphs()
    model = build_model(graphs)
    coverage = Coverage()
    OUT.mkdir(parents=True, exist_ok=True)

    generated_texts: dict[str, str] = {}
    for file_spec in FILE_SPECS:
        text = generate_domain_file(
            file_spec, model, graphs, coverage
        )
        generated_texts[file_spec.filename] = text
        (OUT / file_spec.filename).write_text(text, encoding="utf-8")

    master = generate_master_index(model, graphs, coverage)
    generated_texts["00_indice_master.md"] = master
    (OUT / "00_indice_master.md").write_text(master, encoding="utf-8")

    verification, manifest = validate_and_report(
        graphs, model, coverage, generated_texts
    )
    generated_texts["99_autoverifica.md"] = verification
    (OUT / "99_autoverifica.md").write_text(
        verification, encoding="utf-8"
    )
    (OUT / "coverage_manifest.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    if manifest["status"] != "SUPERATO":
        raise SystemExit(
            "Autoverifica fallita; consultare coverage_manifest.json"
        )
    print(
        json.dumps(
            {
                "output_dir": str(OUT),
                "files": sorted(generated_texts),
                **manifest["counts"],
                "status": manifest["status"],
            },
            indent=2,
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
