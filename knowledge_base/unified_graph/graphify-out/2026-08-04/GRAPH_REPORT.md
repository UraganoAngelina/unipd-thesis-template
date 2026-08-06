# Graph Report - knowledge_base/unified_graph  (2026-08-04)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 706 nodes · 1204 edges · 38 communities (29 shown, 9 thin omitted)
- Extraction: 95% EXTRACTED · 5% INFERRED · 0% AMBIGUOUS · INFERRED: 58 edges (avg confidence: 0.74)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `05e5ef61`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- traffic_exec_engine.py
- main.py
- _common.py
- DashboardTab
- metric_engine.py
- flow_orchestrator.py
- fhir_patient_generator.py
- collect_logs
- RunTab
- Request Dataset Generator RVE Guide
- FlowOrchestrator
- rve_gateway.py
- MockMiddlewareLogGenerator
- ConfigTab
- live Mode
- __init__.py
- __init__.py
- SOAP/WSDL Integration Surface
- Progetto SI.Ter
- Tassonomia degli errori 20260727T185227
- Infrastructure Reference Architecture
- Requisiti COT
- Affinity Domain Italia
- COT Standard
- Edge Computing Latency
- Paymed
- SI.Ter Dimensionamento Computazionale
- Dimissione Protetta End To End
- Impact of Latency on Applications Performance
- Document Source
- Data Reference Architecture
- Layer Interoperabilita
- Authorization Code Flow
- eIDAS
- Firma Elettronica Qualificata
- Flussi NSIS
- Electronic Seal

## God Nodes (most connected - your core abstractions)
1. `RunTab` - 30 edges
2. `execute_flow()` - 22 edges
3. `FlowOrchestrator` - 21 edges
4. `build_workload()` - 20 edges
5. `ConfigTab` - 20 edges
6. `DashboardTab` - 19 edges
7. `FlowBuildTest` - 18 edges
8. `run()` - 18 edges
9. `collect_logs()` - 17 edges
10. `genera_paziente()` - 15 edges

## Surprising Connections (you probably didn't know these)
- `RVE-54 Patient Query` --semantically_similar_to--> `Anagrafe Zero`  [INFERRED] [semantically similar]
  Specifiche tecniche - Anagrafe Zero v2.6.pdf → analisi_completa.md
- `resolve_auth_header()` --implements--> `HTTPS with Basic Authentication`  [INFERRED]
  rve_transactions/scrybasign_common.py → Scryba Sign 3.x Developer's Guide.pdf
- `E-RVE121-001` --references--> `RVE-121 GetAccessToken`  [INFERRED]
  20260727T185227/experiment_summary.md → Specifiche tecniche chiamata di contesto RVE v1.3_PC.pdf
- `Digitalizzazione Elementi DM77` --conceptually_related_to--> `Progetto SI.Ter`  [INFERRED]
  SITER_presentazione alla Cabina di Regia_25 marzo 2026.pdf → analisi_completa.md
- `RVE Flows` --semantically_similar_to--> `RVE Flows`  [INFERRED] [semantically similar]
  README.md → usage.txt

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **Scryba Sign Integration Scenarios** — graphify_kb::scryba_sign_3_x_developer_s_guide_synchronous_workflow, graphify_kb::scryba_sign_3_x_developer_s_guide_asynchronous_workflow, graphify_kb::scryba_sign_3_x_developer_s_guide_graphometric_workflow [EXTRACTED 1.00]
- **Scryba Sign SOAP Service Surface** — graphify_kb::scryba_sign_3_x_developer_s_guide_syncsign_v3, graphify_kb::scryba_sign_3_x_developer_s_guide_asyncsign_v2_2, graphify_kb::scryba_sign_3_x_developer_s_guide_utils_v2, graphify_kb::scryba_sign_3_x_developer_s_guide_notification_v1, graphify_kb::scryba_sign_3_x_developer_s_guide_timestamp_v1, graphify_kb::scryba_sign_3_x_developer_s_guide_digitalstamp_v1, graphify_kb::scryba_sign_3_x_developer_s_guide_signerutils_v1, graphify_kb::scryba_sign_3_x_developer_s_guide_applicationutils_v1, graphify_kb::scryba_sign_3_x_developer_s_guide_validationsutils_v1 [EXTRACTED 1.00]
- **Stateful Signature Session Chain** — graphify_kb::scryba_sign_3_x_developer_s_guide_signer_configuration, graphify_kb::scryba_sign_3_x_developer_s_guide_sync_session_chain, graphify_kb::scryba_sign_3_x_developer_s_guide_async_session_chain, graphify_kb::scryba_sign_3_x_developer_s_guide_document_status_lifecycle [INFERRED 0.85]
- **Sanita Territoriale Operating Model** — graphify_kb::dm77_decreto, graphify_kb::analisi_co116117, graphify_kb::analisi_pua, graphify_kb::analisi_cot, graphify_kb::analisi_progetto_siter, graphify_kb::percorsi_flussi_nsis [INFERRED 0.85]
- **SI.Ter Integration Stack** — graphify_kb::analisi_apms, graphify_kb::analisi_anagrafe_zero, graphify_kb::analisi_fser_xds, graphify_kb::rti_rabbitmq, graphify_kb::rti_camunda, graphify_kb::rti_epersonam, graphify_kb::rti_sister [EXTRACTED 1.00]
- **XDS Document Sharing Metadata Pattern** — graphify_kb::affinity_xdsb, graphify_kb::affinity_xdsdocumententry_metadata, graphify_kb::xvalue_xds_transactions, graphify_kb::xvalue_xds_repository, graphify_kb::xvalue_xds_registry [INFERRED 0.85]
- **Regional Healthcare Authentication Pattern** — graphify_kb::subscription_iua_saml, graphify_kb::rti_jwt_authentication, graphify_kb::context_rve121_get_access_token, graphify_kb::security_rve1_assertion [INFERRED 0.85]
- **Latency Aware Distributed Systems** — graphify_kb::latency_edge_computing_latency, graphify_kb::latency_persistent_connections, graphify_kb::network_load_sharing_window, graphify_kb::network_beta_quantile_rule, graphify_kb::srg_point_to_point_latency [INFERRED 0.75]
- **Catena di evidenza RVE-121** — experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_rve121_001, experiments::knowledge_base_experiments_20260727t185227_experiment_summary_rve_121_http_200_without_causal_transition, experiments::knowledge_base_experiments_20260727t185227_error_taxonomy_gateway_timeout [INFERRED 0.85]
- **Distinzione tra esito HTTP e applicativo** — experiments::knowledge_base_experiments_20260727t185227_readme_status_code_zero, experiments::knowledge_base_experiments_20260727t185227_error_taxonomy_output_extraction_failure, experiments::knowledge_base_experiments_20260727t185227_experiment_summary_separazione_status_code_outcome [INFERRED 0.95]
- **Validità metodologica del campione sperimentale** — experiments::knowledge_base_experiments_20260727t185227_readme_protocollo_live_incompleto, experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001, experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_middleware_001 [INFERRED 0.85]

## Communities (38 total, 9 thin omitted)

### Community 0 - "traffic_exec_engine.py"
Cohesion: 0.05
Nodes (53): RuntimeError, Semaphore, SSLContext, ExtractionTest, PlaceholderTest, _build_parser(), ConcurrencyTracker, _correlation_headers() (+45 more)

### Community 1 - "main.py"
Cohesion: 0.08
Nodes (49): to_json(), to_xml(), _annotate_dataset_flows(), _append_json(), _build_namespace(), _cfg_section(), cmd_collect(), cmd_execute() (+41 more)

### Community 2 - "_common.py"
Cohesion: 0.08
Nodes (43): b64_decode(), b64_encode(), b64url_encode(), build_mock_jwt(), extract_patient_cf(), extract_patient_mpi(), linearize_xml(), msg_id_to_saml_id() (+35 more)

### Community 3 - "DashboardTab"
Cohesion: 0.09
Nodes (20): main(), Entry point CustomTkinter per Request-Dataset-Generator., Shell principale con titlebar simulata e tabview., RDGApp, Costanti visuali per la UI CustomTkinter di RDG., Tab di configurazione esperimento RDG., DashboardTab, Any (+12 more)

### Community 4 - "metric_engine.py"
Cohesion: 0.07
Nodes (27): _build_parser(), _direct_vs_middleware_summary(), GraphGenerator, _load_config(), main(), MetricsCalculator, ArgumentParser, Genera grafici PNG direttamente dal dataset/metrics gia in memoria. (+19 more)

### Community 5 - "flow_orchestrator.py"
Cohesion: 0.07
Nodes (30): Protocol, _new_uuid(), _payload_size(), Flow Orchestrator  Definisce i workflow RVE come catene ordinate di transazioni, Calcola la dimensione in byte del body della richiesta., Costruisce un flusso completo come lista di step pre-compilati.          In moda, Protocollo che ogni modulo rve_Xb.py deve soddisfare.      Un modulo Python è un, RveTransactionModule (+22 more)

### Community 6 - "fhir_patient_generator.py"
Cohesion: 0.09
Nodes (30): _cf_consonanti(), _cf_vocali(), dict_to_xml_element(), genera_bundle_rve55(), genera_codice_fiscale(), genera_paziente(), _new_uuid(), datetime (+22 more)

### Community 7 - "collect_logs"
Cohesion: 0.10
Nodes (23): _build_parser(), collect_logs(), _first_present(), _framework_event_key(), FrameworkLogParser, _load_config(), LogJoiner, main() (+15 more)

### Community 8 - "RunTab"
Cohesion: 0.15
Nodes (3): Accoda l'aggiornamento progress nel main thread Tk., Controllo pipeline con progress bar e log thread-safe., RunTab

### Community 9 - "Request Dataset Generator RVE Guide"
Cohesion: 0.08
Nodes (27): FHIR Synthetic Patients, FLOW_CONTEXT_CALL, FLOW_PATIENT_CREATE, FLOW_PATIENT_QUERY, mTLS with IAP, Pipeline, Request Dataset Generator RVE, RVE Flows (+19 more)

### Community 10 - "FlowOrchestrator"
Cohesion: 0.09
Nodes (7): FlowOrchestrator, Compone i flussi RVE come sequenze di step pre-compilati.      Uso::          or, Args:             config: configurazione globale (endpoints, auth, ecc.), rve_transactions — Moduli di composizione request RVE (Regione Veneto)  Espone l, ConfigJsonTest, FlowBuildTest, MainDispatchTest

### Community 11 - "rve_gateway.py"
Cohesion: 0.18
Nodes (22): _address_locality(), _address_postal_code(), _address_text(), _birth_date_millis(), _build_mock_bundle(), build_request(), build_step(), _family_name() (+14 more)

### Community 12 - "MockMiddlewareLogGenerator"
Cohesion: 0.13
Nodes (13): _build_parser(), main(), MockMiddlewareLogGenerator, ArgumentParser, Simula transizioni del circuit breaker., Scompone la latenza client in gateway_latency + upstream_latency.          Il ga, Inietta anomalie (spike, errori, timeout) con probabilità configurate., Genera una riga di log middleware da un evento response_received. (+5 more)

### Community 18 - "SOAP/WSDL Integration Surface"
Cohesion: 0.06
Nodes (40): applicationUtils V1.0 WSDL, OpenSignSession, EnqueueDoc, CloseSignSession Chain, Asynchronous Signing Workflow, AsyncSign V2.2 WSDL, SPID/CIE-based Automatic FEA Enrolment, FDR, Smart Card, and FEA Certificate Types, Medas Device Manager, digitalStamp V1.0 WSDL (+32 more)

### Community 19 - "Progetto SI.Ter"
Cohesion: 0.06
Nodes (36): RVE-100 Resource Subscription, RVE-54 Patient Query, RVE-55 PatientID Assignment, Specifiche Anagrafe Zero, Anagrafe Zero, APMS, CO 116117, Centrale Operativa Territoriale (+28 more)

### Community 20 - "Tassonomia degli errori 20260727T185227"
Cohesion: 0.10
Nodes (23): Dependency resolution failure, Separazione dei fault iniettati dagli errori spontanei, Gateway timeout, Output extraction failure, Semantic validation failure, Tassonomia degli errori 20260727T185227, Transport timeout, E-FAULT-001 (+15 more)

### Community 21 - "Infrastructure Reference Architecture"
Cohesion: 0.20
Nodes (10): Cognito User Pool, APMS Specifiche, APMS Integration, Audit Log Management, Microservizi, Infrastructure Reference Architecture, Identity And Assertion Provider, ITI-20 Record Audit Event (+2 more)

### Community 22 - "Requisiti COT"
Cohesion: 0.25
Nodes (9): Requisiti Consultori, Requisiti Cure Domiciliari, Requisiti COT, Capitolato Tecnico SI.Ter, COT, PUA, RTI AlmavivA Offerta Tecnica, ePersonam (+1 more)

### Community 23 - "Affinity Domain Italia"
Cohesion: 0.33
Nodes (6): Affinity Domain Italia, Fascicolo Sanitario Elettronico, Infrastruttura Nazionale per l Interoperabilita, IHE XDS.b, XDSDocumentEntry Metadata, XDS.b Transactions

### Community 24 - "COT Standard"
Cohesion: 0.33
Nodes (6): Assistenza Domiciliare, Casa della Comunita, CO 116117 Standard, COT Standard, Decreto Ministeriale 77/2022, Distretto

### Community 25 - "Edge Computing Latency"
Cohesion: 0.33
Nodes (6): Edge Computing Latency, Persistent Connections, When Latency Matters, Beta Quantile Rule, Numerical Evaluation Of Network Latency And Throughput, Load-Sharing Window

### Community 26 - "Paymed"
Cohesion: 0.60
Nodes (5): Advenias, Endpoint GET accessi, Integrazione Advenias Paymed, Paymed, Endpoint POST accessi

### Community 27 - "SI.Ter Dimensionamento Computazionale"
Cohesion: 0.50
Nodes (4): Componenti Accenture DIH, Componenti Almaviva ePersonam, Componenti GPI SisTer, SI.Ter Dimensionamento Computazionale

### Community 28 - "Dimissione Protetta End To End"
Cohesion: 0.50
Nodes (4): Camunda BPMN Rules, Dimissione Protetta End To End, FSEr XDS Layer, RabbitMQ Queues

### Community 29 - "Impact of Latency on Applications Performance"
Cohesion: 0.50
Nodes (4): Impact of Latency on Applications Performance, MPI/Pro, Ping-Pong Tests, Point-to-Point Latency

### Community 30 - "Document Source"
Cohesion: 0.50
Nodes (4): Document Source, Specifiche integrazione XValue, XDS Document Registry, XDS Document Repository

### Community 31 - "Data Reference Architecture"
Cohesion: 0.67
Nodes (3): Data Governance, Data Reference Architecture, Data Virtualization

### Community 32 - "Layer Interoperabilita"
Cohesion: 0.67
Nodes (3): Camunda v7, Layer Interoperabilita, RabbitMQ

## Knowledge Gaps
- **76 isolated node(s):** `FHIR Synthetic Patients`, `live Mode`, `Pipeline`, `saml_assertion_b64 Propagation`, `aiohttp` (+71 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **9 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Work-memory lessons

**Preferred sources** — corroborated by past sessions; start here.
- `FlowOrchestrator` (4× useful, score=3.806909033) _(code changed — re-verify)_
- `IHE XDS.b` (2× useful, score=1.99820313) _(code changed — re-verify)_
- `JWT Token` (2× useful, score=1.99820313) _(code changed — re-verify)_
- `SAML 2.0 Assertion` (2× useful, score=1.99820313) _(code changed — re-verify)_
- `fhir_patient_generator.py` (2× useful, score=1.94959107) _(code changed — re-verify)_
- `_direct_vs_middleware_summary()` (2× useful, score=1.899593339) _(code changed — re-verify)_

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `RVE-121 GetAccessToken` connect `Progetto SI.Ter` to `_common.py`, `Tassonomia degli errori 20260727T185227`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Are the 7 inferred relationships involving `FlowOrchestrator` (e.g. with `ConfigJsonTest` and `EngineSmokeTest`) actually correct?**
  _`FlowOrchestrator` has 7 INFERRED edges - model-reasoned connections that need verification._
- **What connects `FHIR Synthetic Patients`, `live Mode`, `Pipeline` to the rest of the system?**
  _76 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `traffic_exec_engine.py` be split into smaller, more focused modules?**
  _Cohesion score 0.052614052614052616 - nodes in this community are weakly interconnected._
- **Should `main.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08408953418027829 - nodes in this community are weakly interconnected._
- **Should `_common.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08233117483811286 - nodes in this community are weakly interconnected._
- **Should `DashboardTab` be split into smaller, more focused modules?**
  _Cohesion score 0.08562367864693446 - nodes in this community are weakly interconnected._