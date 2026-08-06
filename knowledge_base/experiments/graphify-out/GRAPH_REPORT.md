# Graph Report - /home/alberto/unipd-thesis-template/knowledge_base/experiments  (2026-07-29)

## Corpus Check
- Large corpus: 582 files · ~965,404 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 23 nodes · 26 edges · 5 communities
- Extraction: 77% EXTRACTED · 23% INFERRED · 0% AMBIGUOUS · INFERRED: 6 edges (avg confidence: 0.93)
- Token cost: 3,834 input · 4,780 output

## Community Hubs (Navigation)
- Dataset e validità sperimentale
- Fault e dipendenze runtime
- Errori applicativi middleware
- Esito HTTP e applicativo
- Risultati RVE-121

## God Nodes (most connected - your core abstractions)
1. `Tassonomia degli errori 20260727T185227` - 6 edges
2. `Esperimento 20260727T185227` - 6 edges
3. `Dataset sperimentale sanitizzato 20260727T185227` - 4 edges
4. `E-RVE121-001` - 3 edges
5. `E-RVETOKEN-001` - 3 edges
6. `Sanitizzazione con whitelist` - 2 edges
7. `Protocollo live incompleto` - 2 edges
8. `Status code 0 come assenza di risposta HTTP` - 2 edges
9. `Output extraction failure` - 2 edges
10. `Semantic validation failure` - 2 edges

## Surprising Connections (you probably didn't know these)
- `E-FAULT-001` --semantically_similar_to--> `Separazione dei fault iniettati dagli errori spontanei`  [INFERRED] [semantically similar]
  20260727T185227/experiment_summary.md → 20260727T185227/error_taxonomy.md
- `E-PROTOCOL-001` --conceptually_related_to--> `Protocollo live incompleto`  [INFERRED]
  20260727T185227/experiment_summary.md → 20260727T185227/README.md
- `Status code 0 come assenza di risposta HTTP` --conceptually_related_to--> `Separazione tra status code e outcome`  [INFERRED]
  20260727T185227/README.md → 20260727T185227/experiment_summary.md
- `E-RVETOKEN-001` --conceptually_related_to--> `Output extraction failure`  [INFERRED]
  20260727T185227/experiment_summary.md → 20260727T185227/error_taxonomy.md
- `E-RVE55-001` --conceptually_related_to--> `Semantic validation failure`  [INFERRED]
  20260727T185227/experiment_summary.md → 20260727T185227/error_taxonomy.md

## Hyperedges (group relationships)
- **Catena di evidenza RVE-121** — knowledge_base_experiments_20260727t185227_experiment_summary_e_rve121_001, knowledge_base_experiments_20260727t185227_experiment_summary_rve_121_http_200_without_causal_transition, knowledge_base_experiments_20260727t185227_error_taxonomy_gateway_timeout [INFERRED 0.85]
- **Distinzione tra esito HTTP e applicativo** — knowledge_base_experiments_20260727t185227_readme_status_code_zero, knowledge_base_experiments_20260727t185227_error_taxonomy_output_extraction_failure, knowledge_base_experiments_20260727t185227_experiment_summary_separazione_status_code_outcome [INFERRED 0.95]
- **Validità metodologica del campione sperimentale** — knowledge_base_experiments_20260727t185227_readme_protocollo_live_incompleto, knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001, knowledge_base_experiments_20260727t185227_experiment_summary_e_middleware_001 [INFERRED 0.85]

## Communities (5 total, 0 thin omitted)

### Community 0 - "Dataset e validità sperimentale"
Cohesion: 0.33
Nodes (6): E-PROTOCOL-001, Alias stabili per valori sensibili, Dataset sperimentale sanitizzato 20260727T185227, Figure come evidenza visuale, Protocollo live incompleto, Sanitizzazione con whitelist

### Community 1 - "Fault e dipendenze runtime"
Cohesion: 0.40
Nodes (5): Dependency resolution failure, Separazione dei fault iniettati dagli errori spontanei, Tassonomia degli errori 20260727T185227, Transport timeout, E-FAULT-001

### Community 2 - "Errori applicativi middleware"
Cohesion: 0.40
Nodes (5): Semantic validation failure, E-MIDDLEWARE-001, E-RVE55-001, Esperimento 20260727T185227, Failure path degli scenari middleware

### Community 3 - "Esito HTTP e applicativo"
Cohesion: 0.50
Nodes (4): Output extraction failure, E-RVETOKEN-001, Separazione tra status code e outcome, Status code 0 come assenza di risposta HTTP

### Community 4 - "Risultati RVE-121"
Cohesion: 0.67
Nodes (3): Gateway timeout, E-RVE121-001, RVE-121 HTTP 200 senza dimostrazione causale della transizione

## Knowledge Gaps
- **6 isolated node(s):** `Alias stabili per valori sensibili`, `Figure come evidenza visuale`, `Transport timeout`, `Dependency resolution failure`, `RVE-121 HTTP 200 senza dimostrazione causale della transizione` (+1 more)
  These have ≤1 connection - possible missing edges or undocumented components.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Esperimento 20260727T185227` connect `Errori applicativi middleware` to `Dataset e validità sperimentale`, `Fault e dipendenze runtime`, `Esito HTTP e applicativo`, `Risultati RVE-121`?**
  _High betweenness centrality (0.522) - this node is a cross-community bridge._
- **Why does `Dataset sperimentale sanitizzato 20260727T185227` connect `Dataset e validità sperimentale` to `Esito HTTP e applicativo`?**
  _High betweenness centrality (0.268) - this node is a cross-community bridge._
- **Why does `Tassonomia degli errori 20260727T185227` connect `Fault e dipendenze runtime` to `Errori applicativi middleware`, `Esito HTTP e applicativo`, `Risultati RVE-121`?**
  _High betweenness centrality (0.249) - this node is a cross-community bridge._
- **What connects `Alias stabili per valori sensibili`, `Figure come evidenza visuale`, `Transport timeout` to the rest of the system?**
  _6 weakly-connected nodes found - possible documentation gaps or missing edges._