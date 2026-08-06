---
type: "query"
date: "2026-07-31T09:29:50.692545+00:00"
question: "Come rifocalizzare titolo, Abstract ed Expected Contributions sulla profilazione end-to-end e sul confronto direct_vs_middleware?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["_direct_vs_middleware_summary()", "E-MIDDLEWARE-001", "FlowOrchestrator", "rve_gateway.py"]
---

# Q: Come rifocalizzare titolo, Abstract ed Expected Contributions sulla profilazione end-to-end e sul confronto direct_vs_middleware?

## Answer

Expanded from the original request via graph vocabulary: [direct, middleware, gateway, client, latency, metric, experiment, scenario, flow, patient, rve, iti]. The graph and current code support an end-to-end profiling framework and a differential client-observed comparison implemented by _direct_vs_middleware_summary(). The defensible quantity is apparent mediation overhead at the client boundary, not a causal decomposition of gateway internals. E-MIDDLEWARE-001 records that the retained live middleware sample follows failure paths, so it does not validate nominal overhead or capacity-planning conclusions.

## Outcome

- Signal: useful

## Source Nodes

- _direct_vs_middleware_summary()
- E-MIDDLEWARE-001
- FlowOrchestrator
- rve_gateway.py