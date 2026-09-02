# Graph Report - .  (2026-09-01)

## Corpus Check
- 3 files · ~1,328 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 34 nodes · 41 edges · 8 communities (7 shown, 1 thin omitted)
- Extraction: 80% EXTRACTED · 20% INFERRED · 0% AMBIGUOUS · INFERRED: 8 edges (avg confidence: 0.92)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Experimental Dataset Provenance
- Middleware Flow Outcome Semantics
- Corrected Integer Flow Counts
- Response and Application Outcomes
- Runtime Error Taxonomy
- Campaign and Fault Injection
- RVE-121 Gateway Outcomes
- RVE-55 Semantic Validation

## God Nodes (most connected - your core abstractions)
1. `Tassonomia degli errori 20260727T185227` - 6 edges
2. `Esperimento 20260727T185227` - 6 edges
3. `E-FLOW-SUCCESS-001` - 6 edges
4. `Dataset sperimentale sanitizzato 20260727T185227` - 5 edges
5. `E-RVE121-001` - 3 edges
6. `E-RVETOKEN-001` - 3 edges
7. `E-MIDDLEWARE-001` - 3 edges
8. `Separazione tra status code e outcome` - 3 edges
9. `Popolazione pooled di 1.687 flussi completati` - 3 edges
10. `263 flussi riusciti` - 3 edges

## Surprising Connections (you probably didn't know these)
- `E-FAULT-001` --semantically_similar_to--> `Separazione dei fault iniettati dagli errori spontanei`  [INFERRED] [semantically similar]
  20260727T185227/experiment_summary.md → 20260727T185227/error_taxonomy.md
- `Fonte di verità del successo dei flussi middleware` --references--> `E-FLOW-SUCCESS-001`  [EXTRACTED]
  20260727T185227/README.md → 20260727T185227/flow_success_correction.md
- `Separazione tra esiti di richiesta e di flusso` --conceptually_related_to--> `Separazione tra status code e outcome`  [INFERRED]
  20260727T185227/flow_success_correction.md → 20260727T185227/experiment_summary.md
- `Separazione tra esiti di richiesta e di flusso negli scenari middleware` --semantically_similar_to--> `Separazione tra esiti di richiesta e di flusso`  [INFERRED] [semantically similar]
  20260727T185227/experiment_summary.md → 20260727T185227/flow_success_correction.md
- `E-RVETOKEN-001` --conceptually_related_to--> `Output extraction failure`  [INFERRED]
  20260727T185227/experiment_summary.md → 20260727T185227/error_taxonomy.md

## Hyperedges (group relationships)
- **Catena di evidenza RVE-121** — knowledge_base_experiments_20260727t185227_experiment_summary_e_rve121_001, knowledge_base_experiments_20260727t185227_experiment_summary_rve_121_http_200_without_causal_transition, knowledge_base_experiments_20260727t185227_error_taxonomy_gateway_timeout [INFERRED 0.85]
- **Distinzione tra esito HTTP e applicativo** — knowledge_base_experiments_20260727t185227_readme_status_code_zero, knowledge_base_experiments_20260727t185227_error_taxonomy_output_extraction_failure, knowledge_base_experiments_20260727t185227_experiment_summary_separazione_status_code_outcome [INFERRED 0.95]
- **Validità metodologica del campione sperimentale** — knowledge_base_experiments_20260727t185227_readme_protocollo_live_incompleto, knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001, knowledge_base_experiments_20260727t185227_experiment_summary_e_middleware_001 [INFERRED 0.85]

## Communities (8 total, 1 thin omitted)

### Community 0 - "Experimental Dataset Provenance"
Cohesion: 0.29
Nodes (7): E-PROTOCOL-001, Alias stabili per valori sensibili, Dataset sperimentale sanitizzato 20260727T185227, Figure come evidenza visuale, Fonte di verità del successo dei flussi middleware, Protocollo live incompleto, Sanitizzazione con whitelist

### Community 1 - "Middleware Flow Outcome Semantics"
Cohesion: 0.40
Nodes (6): E-MIDDLEWARE-001, Separazione tra esiti di richiesta e di flusso negli scenari middleware, Correzione del successo dei flussi middleware, E-FLOW-SUCCESS-001, Scenario flow_type_comparison_middleware, Separazione tra esiti di richiesta e di flusso

### Community 2 - "Corrected Integer Flow Counts"
Cohesion: 0.40
Nodes (6): 1.424 flussi non riusciti, 263 flussi riusciti, Popolazione pooled di 1.687 flussi completati, Tasso esatto 15,589804386...%, Valore pubblicato 15,59%, Vincolo di integrità del conteggio intero

### Community 3 - "Response and Application Outcomes"
Cohesion: 0.50
Nodes (4): Output extraction failure, E-RVETOKEN-001, Separazione tra status code e outcome, Status code 0 come assenza di risposta HTTP

### Community 4 - "Runtime Error Taxonomy"
Cohesion: 0.67
Nodes (3): Dependency resolution failure, Tassonomia degli errori 20260727T185227, Transport timeout

### Community 5 - "Campaign and Fault Injection"
Cohesion: 0.67
Nodes (3): Separazione dei fault iniettati dagli errori spontanei, E-FAULT-001, Esperimento 20260727T185227

### Community 6 - "RVE-121 Gateway Outcomes"
Cohesion: 0.67
Nodes (3): Gateway timeout, E-RVE121-001, RVE-121 HTTP 200 senza dimostrazione causale della transizione

## Knowledge Gaps
- **8 isolated node(s):** `Transport timeout`, `Dependency resolution failure`, `Alias stabili per valori sensibili`, `Figure come evidenza visuale`, `RVE-121 HTTP 200 senza dimostrazione causale della transizione` (+3 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `E-FLOW-SUCCESS-001` connect `Middleware Flow Outcome Semantics` to `Experimental Dataset Provenance`, `Corrected Integer Flow Counts`?**
  _High betweenness centrality (0.458) - this node is a cross-community bridge._
- **Why does `Esperimento 20260727T185227` connect `Campaign and Fault Injection` to `Experimental Dataset Provenance`, `Middleware Flow Outcome Semantics`, `Response and Application Outcomes`, `RVE-121 Gateway Outcomes`, `RVE-55 Semantic Validation`?**
  _High betweenness centrality (0.430) - this node is a cross-community bridge._
- **Why does `E-MIDDLEWARE-001` connect `Middleware Flow Outcome Semantics` to `Campaign and Fault Injection`?**
  _High betweenness centrality (0.279) - this node is a cross-community bridge._
- **What connects `Transport timeout`, `Dependency resolution failure`, `Alias stabili per valori sensibili` to the rest of the system?**
  _8 weakly-connected nodes found - possible documentation gaps or missing edges._