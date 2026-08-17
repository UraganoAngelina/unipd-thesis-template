---
type: "query"
date: "2026-08-17T08:39:35.071994+00:00"
question: "Refactor Chapter 3 using the knowledge base for Scryba Sign, mutual TLS, the UI bridge, the metric engine, functional tests, and experimental-validity boundaries."
contributor: "graphify"
outcome: "useful"
source_nodes: ["scrybasign_common.py", "resolve_auth_header()", "MtlsContextFactory", "ui_config_bridge.py", "ConfigTab", "RunTab", "DashboardTab", "MetricsCalculator", "WarningDetector"]
---

# Q: Refactor Chapter 3 using the knowledge base for Scryba Sign, mutual TLS, the UI bridge, the metric engine, functional tests, and experimental-validity boundaries.

## Answer

Expanded from graph vocabulary via scrybasign, signing, authentication, header, soap, mtls, ssl, factory, config, bridge, tabs, dashboard, pipeline, metric, warning, calculator, jsonl, tests, placeholder, and fhir. The refactor verifies code before prose: resolve_auth_header implements Basic authentication rather than OTP; SignOneDoc carries a fixed Base64 test document; MtlsContextFactory caches SSLContext instances by named profile; the UI persists configuration but RunTab remains a demonstration worker; MetricsCalculator and WarningDetector derive statistical evidence and configurable warnings; recorded 28-pass evidence belongs to a migration snapshot, while the incomplete live campaign limits performance inference.

## Outcome

- Signal: useful

## Source Nodes

- scrybasign_common.py
- resolve_auth_header()
- MtlsContextFactory
- ui_config_bridge.py
- ConfigTab
- RunTab
- DashboardTab
- MetricsCalculator
- WarningDetector