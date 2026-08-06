---
type: "query"
date: "2026-08-02T15:44:59.379944+00:00"
question: "How are RVE-1.b, RVE-54, and RVE-55 ordered in direct RDG flows?"
contributor: "graphify"
outcome: "corrected"
correction: "Represent the implementation as a shared authentication prerequisite branching into two direct-flow variants, not as RVE-1.b to RVE-54 to RVE-55."
source_nodes: ["FlowOrchestrator", "FLOW_PATIENT_QUERY", "rve_1b.py", "rve_54.py", "rve_55.py"]
---

# Q: How are RVE-1.b, RVE-54, and RVE-55 ordered in direct RDG flows?

## Answer

RDG defines two distinct direct-flow variants that share RVE-1.b as the authentication prerequisite: FLOW_PATIENT_QUERY orders RVE-1.b then RVE-54 (Patient Query), while FLOW_PATIENT_CREATE orders RVE-1.b then RVE-55 (PatientID Assignment). RVE-54 and RVE-55 are not sequential steps of one direct flow. The SAML output from RVE-1.b is propagated to the selected downstream transaction, and RDG retains flow identity, ordered steps, outputs, timestamps, and outcomes for traceability.

## Outcome

- Signal: corrected
- Correction: Represent the implementation as a shared authentication prerequisite branching into two direct-flow variants, not as RVE-1.b to RVE-54 to RVE-55.

## Source Nodes

- FlowOrchestrator
- FLOW_PATIENT_QUERY
- rve_1b.py
- rve_54.py
- rve_55.py