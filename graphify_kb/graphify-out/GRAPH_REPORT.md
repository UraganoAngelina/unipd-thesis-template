# Graph Report - .  (2026-07-17)

## Corpus Check
- Corpus is ~4,859 words - fits in a single context window. You may not need a graph.

## Summary
- 108 nodes · 95 edges · 20 communities (16 shown, 4 thin omitted)
- Extraction: 86% EXTRACTED · 14% INFERRED · 0% AMBIGUOUS · INFERRED: 13 edges (avg confidence: 0.89)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- RVE Anagrafe Subscriptions
- APMS Security Architecture
- SI.Ter Governance
- Capitolato Care Services
- RVE Context Authentication
- COT PUA Operations
- FSE XDS Interoperability
- DM77 Territorial Standards
- Latency Modeling
- Paymed Access Sync
- SI.Ter Sizing
- Protected Discharge Flow
- Network Latency Benchmarks
- XValue Document Sharing
- Data Architecture
- Integration Middleware
- OAuth Token Flow
- eIDAS Signatures
- Qualified Trust Services
- Territorial Health Flows

## God Nodes (most connected - your core abstractions)
1. `Progetto SI.Ter` - 7 edges
2. `RVE-100 Resource Subscription` - 4 edges
3. `Paymed` - 4 edges
4. `DM 77/2022` - 3 edges
5. `CO 116117` - 3 edges
6. `Anagrafe Zero` - 3 edges
7. `Dimissione Protetta End To End` - 3 edges
8. `Edge Computing Latency` - 3 edges
9. `SI.Ter Dimensionamento Computazionale` - 3 edges
10. `Capitolato Tecnico SI.Ter` - 3 edges

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
- **Sanita Territoriale Operating Model** — dm77_decreto, analisi_co116117, analisi_pua, analisi_cot, analisi_progetto_siter, percorsi_flussi_nsis [INFERRED 0.85]
- **SI.Ter Integration Stack** — analisi_apms, analisi_anagrafe_zero, analisi_fser_xds, rti_rabbitmq, rti_camunda, rti_epersonam, rti_sister [EXTRACTED 1.00]
- **XDS Document Sharing Metadata Pattern** — affinity_xdsb, affinity_xdsdocumententry_metadata, xvalue_xds_transactions, xvalue_xds_repository, xvalue_xds_registry [INFERRED 0.85]
- **Regional Healthcare Authentication Pattern** — subscription_iua_saml, rti_jwt_authentication, context_rve121_get_access_token, security_rve1_assertion [INFERRED 0.85]
- **Latency Aware Distributed Systems** — latency_edge_computing_latency, latency_persistent_connections, network_load_sharing_window, network_beta_quantile_rule, srg_point_to_point_latency [INFERRED 0.75]

## Communities (20 total, 4 thin omitted)

### Community 0 - "RVE Anagrafe Subscriptions"
Cohesion: 0.18
Nodes (11): RVE-100 Resource Subscription, RVE-54 Patient Query, RVE-55 PatientID Assignment, Specifiche Anagrafe Zero, Anagrafe Zero, Dimissione Protetta, FSEr XDS, Interoperabilita e Integrazioni (+3 more)

### Community 1 - "APMS Security Architecture"
Cohesion: 0.20
Nodes (10): Cognito User Pool, APMS Specifiche, APMS Integration, Audit Log Management, Microservizi, Infrastructure Reference Architecture, Identity And Assertion Provider, ITI-20 Record Audit Event (+2 more)

### Community 2 - "SI.Ter Governance"
Cohesion: 0.22
Nodes (9): APMS, ePersonam, Progetto SI.Ter, SisTer, Cabina di Regia, Modello di Governo SI.Ter, APMS Token Multitenancy, Presentazione alla Cabina di Regia (+1 more)

### Community 3 - "Capitolato Care Services"
Cohesion: 0.25
Nodes (9): Requisiti Consultori, Requisiti Cure Domiciliari, Requisiti COT, Capitolato Tecnico SI.Ter, COT, PUA, RTI AlmavivA Offerta Tecnica, ePersonam (+1 more)

### Community 4 - "RVE Context Authentication"
Cohesion: 0.22
Nodes (9): Specifiche Chiamata di Contesto RVE, JWT Token, RVE-121 GetAccessToken, RVE-130 Chiamata Contesto, SAML 2.0 Assertion, SITER-DIH API Gateway, Specifiche RTI Anagrafica, JWT Authentication (+1 more)

### Community 5 - "COT PUA Operations"
Cohesion: 0.33
Nodes (7): CO 116117, Centrale Operativa Territoriale, DM 77/2022, Punto Unico di Accesso, Manuale Protocollo 116117, Parole Alert, Schede Problema

### Community 6 - "FSE XDS Interoperability"
Cohesion: 0.33
Nodes (6): Affinity Domain Italia, Fascicolo Sanitario Elettronico, Infrastruttura Nazionale per l Interoperabilita, IHE XDS.b, XDSDocumentEntry Metadata, XDS.b Transactions

### Community 7 - "DM77 Territorial Standards"
Cohesion: 0.33
Nodes (6): Assistenza Domiciliare, Casa della Comunita, CO 116117 Standard, COT Standard, Decreto Ministeriale 77/2022, Distretto

### Community 8 - "Latency Modeling"
Cohesion: 0.33
Nodes (6): Edge Computing Latency, Persistent Connections, When Latency Matters, Beta Quantile Rule, Numerical Evaluation Of Network Latency And Throughput, Load-Sharing Window

### Community 9 - "Paymed Access Sync"
Cohesion: 0.60
Nodes (5): Advenias, Endpoint GET accessi, Integrazione Advenias Paymed, Paymed, Endpoint POST accessi

### Community 10 - "SI.Ter Sizing"
Cohesion: 0.50
Nodes (4): Componenti Accenture DIH, Componenti Almaviva ePersonam, Componenti GPI SisTer, SI.Ter Dimensionamento Computazionale

### Community 11 - "Protected Discharge Flow"
Cohesion: 0.50
Nodes (4): Camunda BPMN Rules, Dimissione Protetta End To End, FSEr XDS Layer, RabbitMQ Queues

### Community 12 - "Network Latency Benchmarks"
Cohesion: 0.50
Nodes (4): Impact of Latency on Applications Performance, MPI/Pro, Ping-Pong Tests, Point-to-Point Latency

### Community 13 - "XValue Document Sharing"
Cohesion: 0.50
Nodes (4): Document Source, Specifiche integrazione XValue, XDS Document Registry, XDS Document Repository

### Community 14 - "Data Architecture"
Cohesion: 0.67
Nodes (3): Data Governance, Data Reference Architecture, Data Virtualization

### Community 15 - "Integration Middleware"
Cohesion: 0.67
Nodes (3): Camunda v7, Layer Interoperabilita, RabbitMQ

## Knowledge Gaps
- **50 isolated node(s):** `ePersonam`, `SisTer`, `Dimissione Protetta`, `FSEr XDS Layer`, `RabbitMQ Queues` (+45 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **4 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Progetto SI.Ter` connect `SI.Ter Governance` to `RVE Anagrafe Subscriptions`, `COT PUA Operations`?**
  _High betweenness centrality (0.067) - this node is a cross-community bridge._
- **Why does `Anagrafe Zero` connect `RVE Anagrafe Subscriptions` to `SI.Ter Governance`?**
  _High betweenness centrality (0.062) - this node is a cross-community bridge._
- **What connects `ePersonam`, `SisTer`, `Dimissione Protetta` to the rest of the system?**
  _50 weakly-connected nodes found - possible documentation gaps or missing edges._