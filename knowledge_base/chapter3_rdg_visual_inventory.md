# Chapter 3 Request Dataset Generator visual inventory

Inventory date: 2026-08-21

The source campaign is `runs/batches/thesis_live_30r`: 145 runs start, 74 runs
contain a complete `execution_log.jsonl`, and those complete runs produce 578
PNG files. Selection uses the most recent complete run in each relevant
scenario according to the graph-file timestamp. The copies under
`thesis/files/runs/` are byte-identical to the source PNG files.

| Scenario | Selected complete run | Target plot | Source status and absolute path |
|---|---|---|---|
| `direct_vs_middleware` | `r14_seed_114` | `direct_vs_middleware_comparison.png` | Found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/direct_vs_middleware/r14_seed_114/graphs/direct_vs_middleware_comparison.png` |
| `load_ramp` | `r05_seed_105` | `scheduling_drift_over_time.png` | Found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/load_ramp/r05_seed_105/graphs/scheduling_drift_over_time.png` |
| `load_ramp` | `r05_seed_105` | `concurrency_over_time.png` | Found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/load_ramp/r05_seed_105/graphs/concurrency_over_time.png` |
| `baseline` | `r05_seed_105` | `e2e_latency_by_flow_type.png` | Candidate found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/baseline/r05_seed_105/graphs/e2e_latency_by_flow_type.png` |
| `baseline_constant` | `r05_seed_105` | `e2e_latency_by_flow_type.png` | Candidate found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/baseline_constant/r05_seed_105/graphs/e2e_latency_by_flow_type.png` |
| `burst` | `r05_seed_105` | `e2e_latency_by_flow_type.png` | Candidate found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/burst/r05_seed_105/graphs/e2e_latency_by_flow_type.png` |
| `error_injection` | `r06_seed_106` | `e2e_latency_by_flow_type.png` | Candidate found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/error_injection/r06_seed_106/graphs/e2e_latency_by_flow_type.png` |
| `flow_type_comparison_direct` | `r06_seed_106` | `e2e_latency_by_flow_type.png` | Found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/flow_type_comparison_direct/r06_seed_106/graphs/e2e_latency_by_flow_type.png` |
| `flow_type_comparison_middleware` | `r15_seed_115` | `e2e_latency_by_flow_type.png` | Candidate found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/flow_type_comparison_middleware/r15_seed_115/graphs/e2e_latency_by_flow_type.png` |
| `stress_extreme` | `r05_seed_105` | `latency_distribution.png` | Found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/stress_extreme/r05_seed_105/graphs/latency_distribution.png` |
| `stress_extreme` | `r05_seed_105` | `error_rate_over_time.png` | Found: `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/stress_extreme/r05_seed_105/graphs/error_rate_over_time.png` |
| `stress_extreme` | `r05_seed_105` | `avaiability_over_time.png` | Requested spelling missing; corrected source found as `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/stress_extreme/r05_seed_105/graphs/availability_over_time.png` |
| `stress_extreme` | `r05_seed_105` | `throughtput_over_time.png` | Requested spelling missing; corrected source found as `/home/alberto/Desktop/Request-Dataset-Generator/runs/batches/thesis_live_30r/results/stress_extreme/r05_seed_105/graphs/throughput_over_time.png` |

The integrated semantic-heterogeneity figure uses
`flow_type_comparison_direct/r06_seed_106` because this scenario isolates the
direct flow families and is the most recent complete direct comparison run. The
other rows remain explicit candidates rather than being silently discarded.

## Visual consistency notes

- In `load_ramp/r05_seed_105`, active flows and active steps reach the configured
  limit of 30 at about 60 seconds. The ninety-fifth-percentile queue delay begins
  its sustained increase at about 65 seconds and reaches approximately 67,000
  milliseconds. The isolated downward discontinuities coincide with temporarily
  empty time buckets; they do not invalidate the long rising envelope.
- In `stress_extreme/r05_seed_105`, the request-latency histogram has a dominant
  low-latency mode and a separate mode near 45,000 milliseconds. The resolved
  configuration declares `execution.step_timeout_seconds = 45` and a 0.05
  injected-timeout rate. The PNG therefore does not support a 30,000-millisecond
  peak or a unique attribution to gateway saturation.
- In `flow_type_comparison_direct/r06_seed_106`, the completion-time boxplots are
  visibly heterogeneous. The Cross-Enterprise Document Sharing Registry Stored
  Query flow is centred near 19,000 milliseconds, while the other displayed
  flow families remain predominantly below roughly 1,500 milliseconds.
- In `direct_vs_middleware/r14_seed_114`, the displayed medians differ by only a
  few milliseconds and the mediated population is more dispersed. This
  single-run, outcome-unstratified plot cannot visually confirm the independent
  pooled successful-path value of 184.7 milliseconds, nor the fine pooled
  failure differences of 12.88 and 284.30 milliseconds.
- The stress error-rate, availability, and throughput plots use the same
  one-second buckets. Availability is a binary bucket indicator (100 when the
  bucket has no errors and 0 otherwise), so it must not be read as a continuous
  provider availability estimate. The panels support temporal co-occurrence,
  not a causal or correlation-coefficient estimate.
