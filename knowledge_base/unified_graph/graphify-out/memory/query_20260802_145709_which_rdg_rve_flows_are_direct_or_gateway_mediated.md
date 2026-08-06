---
type: "architecture"
date: "2026-08-02T14:57:09.025976+00:00"
question: "Which RDG RVE flows are Direct or Gateway-Mediated for the thesis workflow visual?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["FlowOrchestrator", "MetricEngine", "rve_gateway", "rve_token"]
---

# Q: Which RDG RVE flows are Direct or Gateway-Mediated for the thesis workflow visual?

## Answer

Current flow metadata defines FLOW_PATIENT_QUERY as RVE-1.b to RVE-54, FLOW_PATIENT_CREATE as RVE-1.b to RVE-55, and FLOW_CONTEXT_CALL as RVE-1.b to RVE-121 to RVE-130. The implemented differential comparison groups the patient query/create flows as direct and contrasts them with FLOW_PATIENT_QUERY_MIDDLEWARE, whose excerpt begins Middleware Token to Gateway RVE-54 to Gateway RVE-55. No gateway-mediated counterpart is defined for FLOW_CONTEXT_CALL.

## Outcome

- Signal: useful

## Source Nodes

- FlowOrchestrator
- MetricEngine
- rve_gateway
- rve_token