---
type: "query"
date: "2026-07-29T10:33:56.609516+00:00"
question: "Which documented requirements, transaction chains, workload mechanisms, KPI categories, and sanitised evidence support Chapter 2 of the thesis?"
contributor: "graphify"
outcome: "useful"
source_nodes: ["FlowOrchestrator", "build_workload", "build_timeline", "ConcurrencyTracker", "MetricsCalculator", "WarningDetector"]
---

# Q: Which documented requirements, transaction chains, workload mechanisms, KPI categories, and sanitised evidence support Chapter 2 of the thesis?

## Answer

The graph supports a source-bounded Chapter 2 through this expansion: FlowOrchestrator -> supported RVE/ITI/ScrybaSign flow composition and ordered dependencies; build_workload -> configurable weighted flow mix; build_timeline -> constant, step, daily-profile, and injected-burst schedules; ConcurrencyTracker -> active-work observations; MetricsCalculator -> request, flow, outcome, throughput, concurrency, and time-series populations; WarningDetector -> implementation warnings that must not be treated as ex ante domain thresholds. The sanitised empirical dataset entity transaction_outcomes.csv#all-transactions supports observed live outcome coverage across 74 complete runs for the listed transaction families, but not profile conformance, mock coverage, or domain acceptance. M08-M10 and M12 therefore remain unresolved, while M11 is only partially resolved.

## Outcome

- Signal: useful

## Source Nodes

- FlowOrchestrator
- build_workload
- build_timeline
- ConcurrencyTracker
- MetricsCalculator
- WarningDetector