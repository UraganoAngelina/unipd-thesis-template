# Graph Report - graphify_kb  (2026-08-04)

## Corpus Check
- cluster-only mode — file stats not available

## Summary
- 150 nodes · 143 edges · 23 communities (18 shown, 5 thin omitted)
- Extraction: 91% EXTRACTED · 9% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `05e5ef61`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- SOAP/WSDL Integration Surface
- RVE-100 Resource Subscription
- Progetto SI.Ter
- Signer Configuration
- Infrastructure Reference Architecture
- Requisiti COT
- CO 116117
- AsyncSign V2.2 WSDL
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
1. `SOAP/WSDL Integration Surface` - 11 edges
2. `Progetto SI.Ter` - 7 edges
3. `Scryba Sign Server` - 7 edges
4. `AsyncSign V2.2 WSDL` - 5 edges
5. `RVE-100 Resource Subscription` - 4 edges
6. `Paymed` - 4 edges
7. `Remote Digital Signature` - 4 edges
8. `Signer Configuration` - 4 edges
9. `SyncSign V3 WSDL` - 4 edges
10. `Utils V2 WSDL` - 4 edges

## Surprising Connections (you probably didn't know these)
- `RVE-54 Patient Query` --semantically_similar_to--> `Anagrafe Zero`  [INFERRED] [semantically similar]
  Specifiche tecniche - Anagrafe Zero v2.6.pdf → analisi_completa.md
- `Digitalizzazione Elementi DM77` --conceptually_related_to--> `Progetto SI.Ter`  [INFERRED]
  SITER_presentazione alla Cabina di Regia_25 marzo 2026.pdf → analisi_completa.md
- `Modello di Governo SI.Ter` --references--> `Progetto SI.Ter`  [EXTRACTED]
  DDR 11922 del 16.03.2026_SITER.pdf → analisi_completa.md
- `Parole Alert` --conceptually_related_to--> `CO 116117`  [INFERRED]
  MANUALE PROTOCOLLO 2_116117.docx 1.pdf → analisi_completa.md
- `IAP Endpoint` --conceptually_related_to--> `Identity And Assertion Provider`  [INFERRED]
  specifiche.txt → Infrastruttura di sicurezza GDL-O Sicurezza v2.14.pdf

## Hyperedges (group relationships)
- **Scryba Sign Integration Scenarios** — scryba_sign_3_x_developer_s_guide_synchronous_workflow, scryba_sign_3_x_developer_s_guide_asynchronous_workflow, scryba_sign_3_x_developer_s_guide_graphometric_workflow [EXTRACTED 1.00]
- **Scryba Sign SOAP Service Surface** — scryba_sign_3_x_developer_s_guide_syncsign_v3, scryba_sign_3_x_developer_s_guide_asyncsign_v2_2, scryba_sign_3_x_developer_s_guide_utils_v2, scryba_sign_3_x_developer_s_guide_notification_v1, scryba_sign_3_x_developer_s_guide_timestamp_v1, scryba_sign_3_x_developer_s_guide_digitalstamp_v1, scryba_sign_3_x_developer_s_guide_signerutils_v1, scryba_sign_3_x_developer_s_guide_applicationutils_v1, scryba_sign_3_x_developer_s_guide_validationsutils_v1 [EXTRACTED 1.00]
- **Stateful Signature Session Chain** — scryba_sign_3_x_developer_s_guide_signer_configuration, scryba_sign_3_x_developer_s_guide_sync_session_chain, scryba_sign_3_x_developer_s_guide_async_session_chain, scryba_sign_3_x_developer_s_guide_document_status_lifecycle [INFERRED 0.85]
- **Sanita Territoriale Operating Model** — dm77_decreto, analisi_co116117, analisi_pua, analisi_cot, analisi_progetto_siter, percorsi_flussi_nsis [INFERRED 0.85]
- **SI.Ter Integration Stack** — analisi_apms, analisi_anagrafe_zero, analisi_fser_xds, rti_rabbitmq, rti_camunda, rti_epersonam, rti_sister [EXTRACTED 1.00]
- **XDS Document Sharing Metadata Pattern** — affinity_xdsb, affinity_xdsdocumententry_metadata, xvalue_xds_transactions, xvalue_xds_repository, xvalue_xds_registry [INFERRED 0.85]
- **Regional Healthcare Authentication Pattern** — subscription_iua_saml, rti_jwt_authentication, context_rve121_get_access_token, security_rve1_assertion [INFERRED 0.85]
- **Latency Aware Distributed Systems** — latency_edge_computing_latency, latency_persistent_connections, network_load_sharing_window, network_beta_quantile_rule, srg_point_to_point_latency [INFERRED 0.75]

## Communities (23 total, 5 thin omitted)

### Community 0 - "SOAP/WSDL Integration Surface"
Cohesion: 0.12
Nodes (19): applicationUtils V1.0 WSDL, SPID/CIE-based Automatic FEA Enrolment, digitalStamp V1.0 WSDL, Scryba Sign 3.x Developer's Guide (V16), HTTPS with Basic Authentication, RetrieveIdentityDocument, Integration Certification Process, DespatchOtp and VerifyOTP (+11 more)

### Community 1 - "RVE-100 Resource Subscription"
Cohesion: 0.13
Nodes (15): RVE-100 Resource Subscription, RVE-55 PatientID Assignment, Specifiche Anagrafe Zero, Specifiche Chiamata di Contesto RVE, JWT Token, RVE-121 GetAccessToken, RVE-130 Chiamata Contesto, SAML 2.0 Assertion (+7 more)

### Community 2 - "Progetto SI.Ter"
Cohesion: 0.14
Nodes (14): RVE-54 Patient Query, Anagrafe Zero, APMS, Dimissione Protetta, ePersonam, FSEr XDS, Progetto SI.Ter, SisTer (+6 more)

### Community 3 - "Signer Configuration"
Cohesion: 0.14
Nodes (14): Asynchronous Signing Workflow, FDR, Smart Card, and FEA Certificate Types, getDocumentStatus GET/DELETE Lifecycle, GetUserInfo4, Large-file SFTP and SHA-256 Transfer Procedure, Notification V1.0 WSDL, Signer Configuration, Signing Power and Signature Profile (+6 more)

### Community 4 - "Infrastructure Reference Architecture"
Cohesion: 0.20
Nodes (10): Cognito User Pool, APMS Specifiche, APMS Integration, Audit Log Management, Microservizi, Infrastructure Reference Architecture, Identity And Assertion Provider, ITI-20 Record Audit Event (+2 more)

### Community 5 - "Requisiti COT"
Cohesion: 0.25
Nodes (9): Requisiti Consultori, Requisiti Cure Domiciliari, Requisiti COT, Capitolato Tecnico SI.Ter, COT, PUA, RTI AlmavivA Offerta Tecnica, ePersonam (+1 more)

### Community 6 - "CO 116117"
Cohesion: 0.33
Nodes (7): CO 116117, Centrale Operativa Territoriale, DM 77/2022, Punto Unico di Accesso, Manuale Protocollo 116117, Parole Alert, Schede Problema

### Community 7 - "AsyncSign V2.2 WSDL"
Cohesion: 0.29
Nodes (7): OpenSignSession, EnqueueDoc, CloseSignSession Chain, AsyncSign V2.2 WSDL, Medas Device Manager, EnqueueOneDoc, FeaFgmEnqueueOneDoc, FeaFgmUtils WSDL, Graphometric Signature Workflow

### Community 8 - "Affinity Domain Italia"
Cohesion: 0.33
Nodes (6): Affinity Domain Italia, Fascicolo Sanitario Elettronico, Infrastruttura Nazionale per l Interoperabilita, IHE XDS.b, XDSDocumentEntry Metadata, XDS.b Transactions

### Community 9 - "COT Standard"
Cohesion: 0.33
Nodes (6): Assistenza Domiciliare, Casa della Comunita, CO 116117 Standard, COT Standard, Decreto Ministeriale 77/2022, Distretto

### Community 10 - "Edge Computing Latency"
Cohesion: 0.33
Nodes (6): Edge Computing Latency, Persistent Connections, When Latency Matters, Beta Quantile Rule, Numerical Evaluation Of Network Latency And Throughput, Load-Sharing Window

### Community 11 - "Paymed"
Cohesion: 0.60
Nodes (5): Advenias, Endpoint GET accessi, Integrazione Advenias Paymed, Paymed, Endpoint POST accessi

### Community 12 - "SI.Ter Dimensionamento Computazionale"
Cohesion: 0.50
Nodes (4): Componenti Accenture DIH, Componenti Almaviva ePersonam, Componenti GPI SisTer, SI.Ter Dimensionamento Computazionale

### Community 13 - "Dimissione Protetta End To End"
Cohesion: 0.50
Nodes (4): Camunda BPMN Rules, Dimissione Protetta End To End, FSEr XDS Layer, RabbitMQ Queues

### Community 14 - "Impact of Latency on Applications Performance"
Cohesion: 0.50
Nodes (4): Impact of Latency on Applications Performance, MPI/Pro, Ping-Pong Tests, Point-to-Point Latency

### Community 15 - "Document Source"
Cohesion: 0.50
Nodes (4): Document Source, Specifiche integrazione XValue, XDS Document Registry, XDS Document Repository

### Community 16 - "Data Reference Architecture"
Cohesion: 0.67
Nodes (3): Data Governance, Data Reference Architecture, Data Virtualization

### Community 17 - "Layer Interoperabilita"
Cohesion: 0.67
Nodes (3): Camunda v7, Layer Interoperabilita, RabbitMQ

## Knowledge Gaps
- **61 isolated node(s):** `ePersonam`, `SisTer`, `Dimissione Protetta`, `FSEr XDS Layer`, `RabbitMQ Queues` (+56 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **5 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `SOAP/WSDL Integration Surface` connect `SOAP/WSDL Integration Surface` to `Signer Configuration`, `AsyncSign V2.2 WSDL`?**
  _High betweenness centrality (0.048) - this node is a cross-community bridge._
- **Why does `Progetto SI.Ter` connect `Progetto SI.Ter` to `CO 116117`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **What connects `ePersonam`, `SisTer`, `Dimissione Protetta` to the rest of the system?**
  _61 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `SOAP/WSDL Integration Surface` be split into smaller, more focused modules?**
  _Cohesion score 0.12280701754385964 - nodes in this community are weakly interconnected._
- **Should `RVE-100 Resource Subscription` be split into smaller, more focused modules?**
  _Cohesion score 0.13333333333333333 - nodes in this community are weakly interconnected._
- **Should `Progetto SI.Ter` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._
- **Should `Signer Configuration` be split into smaller, more focused modules?**
  _Cohesion score 0.14285714285714285 - nodes in this community are weakly interconnected._