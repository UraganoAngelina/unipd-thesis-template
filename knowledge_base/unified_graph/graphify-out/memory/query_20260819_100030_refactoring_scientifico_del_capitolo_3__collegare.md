---
type: "query"
date: "2026-08-19T10:00:30.034176+00:00"
question: "Refactoring scientifico del Capitolo 3: collegare quantili, Load-Sharing Window, Transfer in Vain e osservabilita client-side"
contributor: "graphify"
outcome: "useful"
source_nodes: ["Load-Sharing Window", "Beta Quantile Rule", "Numerical Evaluation Of Network Latency And Throughput", ".percentile()", ".calc_observability()"]
---

# Q: Refactoring scientifico del Capitolo 3: collegare quantili, Load-Sharing Window, Transfer in Vain e osservabilita client-side

## Answer

Expanded from the thesis request via graph vocabulary: [latency, quantile, percentile, load, sharing, window, transfer, observability]. The graph establishes that the Load-Sharing Window references the Akram latency-throughput paper and motivates the Beta Quantile Rule; client-side percentile and observability calculations connect the theoretical model to the framework evidence. Verified live logs give stress_extreme successful-flow P50 572.346 ms, P95 2026.912 ms, and P99 21505.878 ms, versus baseline_constant P99 18271.775 ms. The thesis therefore treats tail amplification plus lower useful completion as empirical client-boundary evidence of a closing Load-Sharing Window and Transfer in Vain risk, while retaining these concepts as explanatory abstractions. The 184.7 ms value remains an apparent Path-level Overhead at the authorised client boundary under surrogate observability invariants.

## Outcome

- Signal: useful

## Source Nodes

- Load-Sharing Window
- Beta Quantile Rule
- Numerical Evaluation Of Network Latency And Throughput
- .percentile()
- .calc_observability()