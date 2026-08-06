---
type: "query"
date: "2026-07-31T10:01:00.584428+00:00"
question: "Come riallineare il Capitolo 1 alla Surrogate Observability Strategy e alle 74 run?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["FlowOrchestrator", "_direct_vs_middleware_summary()", "fhir_patient_generator.py", "SITER-DIH API Gateway", "APMS Specifiche"]
---

# Q: Come riallineare il Capitolo 1 alla Surrogate Observability Strategy e alle 74 run?

## Answer

Expanded from original query via vocab: [siter, integration, gateway, middleware, direct, latency, fhir, patient, rve, security, observability, metric]. The evidence supports an empirical end-to-end profiling methodology implemented by RDG: synthetic FHIR R4 patients, asyncio-based concurrent execution, direct RVE-54/RVE-55 paths, and a direct_vs_middleware summary that reports mean and percentile deltas. Because internal gateway telemetry is unavailable, those deltas characterize apparent path-level mediation overhead and must not be presented as a causal decomposition of gateway internals. The SI.Ter sources establish a multilayer integration context spanning APIs, authentication, regional patient services, orchestration, transformations, document exchange, and operational boundaries. The experimental corpus comprises 74 completed runs, appropriately framed as proof of concept of pipeline sensitivity without claims about sample-space adequacy.

## Outcome

- Signal: useful

## Source Nodes

- FlowOrchestrator
- _direct_vs_middleware_summary()
- fhir_patient_generator.py
- SITER-DIH API Gateway
- APMS Specifiche