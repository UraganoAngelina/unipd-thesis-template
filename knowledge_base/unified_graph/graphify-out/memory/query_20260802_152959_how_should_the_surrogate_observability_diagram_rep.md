---
type: "architecture"
date: "2026-08-02T15:29:59.127785+00:00"
question: "How should the surrogate observability diagram represent direct_vs_middleware, APMS, and the authorised observation boundary?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["APMS", "_direct_vs_middleware_summary", "MiddlewareLogParser", "FlowOrchestrator"]
---

# Q: How should the surrogate observability diagram represent direct_vs_middleware, APMS, and the authorised observation boundary?

## Answer

Expanded via graph vocabulary: [apms, gateway, middleware, direct, latency, metric, client, service, flow, experiment]. The current RDG metric engine compares client-observed end-to-end distributions for direct patient flows and FLOW_PATIENT_QUERY_MIDDLEWARE, computing apparent_overhead_ms as mediated minus direct for mean, p50, p95, and p99. APMS is the Application Profile Management System for authentication and profiling, while APMS/gateway internal telemetry is outside the thesis authorised evidence boundary. The diagram therefore shows Path A RDG to downstream service, Path B RDG to Gateway (APMS) to downstream service, and Delta L as a surrogate estimate of aggregate mediated-path overhead rather than APMS internal processing time.

## Outcome

- Signal: useful

## Source Nodes

- APMS
- _direct_vs_middleware_summary
- MiddlewareLogParser
- FlowOrchestrator