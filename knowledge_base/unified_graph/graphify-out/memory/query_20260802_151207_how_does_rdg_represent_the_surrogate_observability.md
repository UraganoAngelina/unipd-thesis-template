---
type: "architecture"
date: "2026-08-02T15:12:07.408713+00:00"
question: "How does RDG represent the Surrogate Observability Pattern and estimate gateway overhead without middleware logs?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["_direct_vs_middleware_summary", "MiddlewareLogParser", "metric_engine.py", "log_collector.py"]
---

# Q: How does RDG represent the Surrogate Observability Pattern and estimate gateway overhead without middleware logs?

## Answer

Expanded via graph vocabulary: [direct, gateway, middleware, latency, metric, flow, client, log]. RDG compares client-observed end-to-end duration distributions for direct patient flows and FLOW_PATIENT_QUERY_MIDDLEWARE. metric_engine.py computes apparent_overhead_ms as mediated statistics minus direct statistics for mean, p50, p95, and p99. When middleware logs are absent, gateway_latency_ms and upstream_latency_ms remain unavailable, so Delta L estimates aggregate path-level mediation overhead under comparable workloads; it does not isolate gateway-internal processing time, because routing, network, security processing, transformations, and retries may contribute.

## Outcome

- Signal: useful

## Source Nodes

- _direct_vs_middleware_summary
- MiddlewareLogParser
- metric_engine.py
- log_collector.py