# Migration matrix — old structure to definitive index

## Decision rules

This matrix maps all 91 units in `migration_inventory.md`. A destination marked
`Primary` is the unique home of the migrated prose. `Secondary fragment` is used
only when the source unit contains editorially separable material and the action is
`SPLIT`; it does not authorise duplication. `Cross-reference only` means that the
other section may refer to the primary discussion without copying it.

Implementation-specific sentences found in old Chapters 1–3 are marked `DEFER`
when they would belong to new Chapter 3. They are not counted as existing coverage
of that chapter and may be reused only in a later implementation phase after
verification against the current RDG codebase.

Risk levels:

- **L** — direct move or local title/transition adaptation;
- **M** — overlap, split, outdated structural reference, or terminology check;
- **H** — missing evidence, confidentiality, implementation verification, or
  potential unsupported claim.

## Old Chapter 1

| Source ID | Old placement | New placement | Action | Rationale | Citations/apparatus to preserve | Risk | Expected residual marker |
|---|---|---|---|---|---|---|---|
| C1-001 | Ch. 1 opening, lines 1–30 | Primary: new Chapter 1 opening; commented examples: no thesis destination | SPLIT | Preserve the active chapter anchor while explicitly excluding commented template residue from prose migration. | `chap:introduction`; commented keys/labels remain documented but need not migrate. | M | None; template comments recorded as deferred residue. |
| C1-002 | `Reference Scenario` intro | Primary: 1.1.1; cross-reference only to 1.6 | ADAPT | Its general framing directly opens information continuity; the old chapter roadmap must be removed. | — | L | None. |
| C1-003 | `Thesis Context` intro | Primary: 1.3.1 | MERGE | Merge with the concrete internship/project blocks to avoid repeating the industrial origin. | — | L | None. |
| C1-004 | Internship | Primary: 1.3.1 | ADAPT | Retain documented context and cautious wording; personal details remain evidence-gated. | — | H | `[DATA MISSING: precise internship dates, formal role title, team name, internal deliverables produced, and activities validated by company tutor.]` |
| C1-005 | System integrator role | Primary fragment: 1.3.1; secondary fragment: 1.3.2; cross-reference only to 2.1.2 | SPLIT | Separate professional role from technical ecosystem; theoretical architecture receives only a forward reference. | — | M | None. |
| C1-006 | RTI involvement | Primary: 1.3.1 | ADAPT | Keep only documented case-study involvement and the explicit confidentiality/evidence boundary. | — | H | `[DATA MISSING: documented description of the student's activities in the RTI team, validated by tutor or company documentation.]` |
| C1-007 | Regional-context intro | Primary: 1.2.1 | MERGE | Merge with the fuller institutional material in C1-008/C1-009 and old Chapter 2. | — | L | None. |
| C1-008 | Veneto healthcare system | Primary fragment: 1.2.1; secondary fragment: 1.3.2 | SPLIT | Organisational actors belong to territorial context; technical infrastructures belong to the ecosystem map. | — | M | None. |
| C1-009 | DM 77/PNRR | Primary fragment: 1.2.1; secondary fragment: 1.2.2 | SPLIT | Separate institutional model from the constraints it imposes on admissible solutions. | — | H | `[DATA MISSING: BibLaTeX entry and exact institutional source for PNRR investment-line figures or milestone tables, if retained.]` |
| C1-010 | Information fragmentation | Primary: 1.1.1 | MERGE | Combine with C2-008/C2-012 as the general problem, retaining the three fragmentation levels. | — | M | None. |
| C1-011 | SI.Ter intro | Primary: 1.3.1 | MERGE | Use as the project-context opening and absorb detail from the following units. | — | L | None. |
| C1-012 | SI.Ter overview | Primary fragment: 1.3.1; secondary fragment: 1.3.2 | SPLIT | Separate project/governance framing from the component inventory. | — | H | `[DATA MISSING: BibLaTeX entry and exact page reference for DDR 11922/2026 before a more precise governance formulation.]` |
| C1-013 | SI.Ter functional architecture | Primary: 1.3.1; short validated component-name fragment to 1.3.2 | SPLIT | Functional pathways explain project scope; only the stable component taxonomy belongs in the ecosystem map. | — | H | `[DATA MISSING: final validation of the exact SI.Ter module names.]` |
| C1-014 | SI.Ter technological architecture | Primary fragment: 1.3.2; secondary limitation fragment: 1.4.4 | SPLIT | Keep component responsibilities separate from the cross-layer observability exclusion. | — | H | `[DATA MISSING: final disclosure confirmation for any more detailed description of SI.Ter technological components.]` |
| C1-015 | SI.Ter objectives/milestones | Primary: 1.3.1 | ADAPT | Retain objectives as background; omit dates unless validated because project management is not evaluated. | — | H | `[DATA MISSING: official milestone table and dates, if a SI.Ter timeline is included.]` |
| C1-016 | Research-problem intro | Primary: 1.1.2 | RETAIN | It already states the thesis-specific gap with suitable caution. | — | L | None. |
| C1-017 | Heterogeneous interoperability | Primary: 1.1.2 | MERGE | Merge with C2-009 while retaining the problem focus; theory remains in Chapter 2. | — | M | None. |
| C1-018 | Multi-actor/multi-protocol flows | Primary: 1.1.2 | ADAPT | Preserve dependency/concurrency distinction without turning the problem statement into implementation description. | — | M | None. |
| C1-019 | Missing controlled environment | Primary: 1.1.2; scope fragment to 1.4.1 | SPLIT | The absence of a controlled environment is part of the problem; supported capabilities delimit the investigation. | — | H | `[IMPLEMENTATION CHECK: verify the concise capability list against the current RDG code before migration.]` |
| C1-020 | Framework/middleware correlation limits | Primary fragment: 1.1.2; secondary fragment: 1.4.4 | SPLIT | State the architectural problem once, then formalise the exclusion in scope. | — | M | None. |
| C1-021 | Objectives overview | Primary: 1.5.1 | MERGE | Use as the organising paragraph for the four objective dimensions. | — | L | None. |
| C1-022 | Standards objective | Primary: 1.5.1 | MERGE | Retain as one verifiable objective; defer theoretical exposition to 2.1.3. | — | L | None. |
| C1-023 | Use-case objective | Primary: 1.5.1 | MERGE | Retain as the formalisation objective without claiming completed case-study detail. | — | M | None. |
| C1-024 | Framework objective | Primary fragment: 1.5.1; secondary artefact fragment: 1.5.2 | SPLIT | Separate what the thesis aims to do from the concrete software artefact expected. | — | H | `[IMPLEMENTATION CHECK: verify pipeline and supported-flow claims against current code.]` |
| C1-025 | Measurement objective | Primary: 1.5.1 | MERGE | Retain metric levels and provenance as the fourth objective. | — | L | None. |
| C1-026 | Contributions overview | Primary: 1.5.3 | MERGE | Use as contribution taxonomy; keep expected/demonstrated distinction explicit. | — | M | None. |
| C1-027 | Analytical contribution | Primary: 1.5.3 | MERGE | Integrate with the overview without duplicating objective wording. | — | L | None. |
| C1-028 | Technical contribution | Primary fragment: 1.5.2; secondary fragment: 1.5.3 | SPLIT | The flow/pipeline inventory defines the artefact; its originality claim belongs to contributions. | Six-item `itemize`; flow identifiers. | H | `[IMPLEMENTATION CHECK: verify the current flow map before retaining the list.]` |
| C1-029 | Grey-box contribution | Primary fragment: 1.5.3; cross-reference only to 1.4.4 | ADAPT | Keep the methodological contribution in one place and refer back to the scope exclusion. | — | M | None. |
| C1-030 | Experimental contribution | Primary fragment: 1.5.2 for expected outputs; primary contribution wording: 1.5.3 | SPLIT | Separate expected artefacts from the explicitly data-gated empirical contribution. | — | H | `[DATA MISSING: final executed scenarios, dataset sizes, configuration versions, logs, metric reports, and validated interpretations.]` |
| C1-031 | Dissertation structure | Primary: 1.6 | ADAPT | Rewrite the roadmap for the definitive four-chapter structure; retain only the narrative sequence. | Terminal `\newpage` only if still needed. | H | `[TO EXPAND: replace the obsolete chapter roadmap with the definitive four-chapter structure.]` |

## Old Chapter 2

| Source ID | Old placement | New placement | Action | Rationale | Citations/apparatus to preserve | Risk | Expected residual marker |
|---|---|---|---|---|---|---|---|
| C2-001 | Ch. 2 opening, lines 1–52 | Primary: anchor at the migrated domain-context block in new Chapter 1; comments: no thesis destination | SPLIT | Preserve `chap:domain` as an internal anchor if references require it; template examples are explicit residue. | `chap:domain`; commented figure/listing labels recorded only. | M | None; comments deferred. |
| C2-002 | Domain chapter intro | Primary fragment: 1.1.1; secondary fragment: 1.2.1 | SPLIT | General continuity framing and institutional introduction serve different target functions. | — | M | None. |
| C2-003 | Territorial care/continuity | Primary fragment: 1.1.1; secondary fragment: 1.2.1 | SPLIT | The definition supports the general problem; concrete territorial transitions support context. | — | M | None. |
| C2-004 | Territorial structures/models | Primary fragment: 1.2.1; secondary constraint fragment: 1.2.2 | SPLIT | Separate organisational description from regulatory/technological obligations. | — | H | `[DATA MISSING: BibLaTeX entry and exact page references for DM 77/2022 passages.]` |
| C2-005 | COT role | Primary: 1.2.1 | RETAIN | Directly satisfies the target’s institutional COT content. | — | L | None. |
| C2-006 | Other actors/roles | Primary: 1.2.1; cross-reference only to 2.4.3 | ADAPT | Keep MMG/ULSS/hospital/ADI roles in territorial context and avoid duplicating the future stakeholder inventory. | — | M | None. |
| C2-007 | Digitalisation impact/workflow patterns | Primary fragment: 1.2.1; secondary protected-discharge fragment: 2.4.1; process-dependency fragment: 2.4.4 | SPLIT | The conceptual impact belongs to context, while the two explicitly described workflow patterns are the only pre-existing case material. | — | H | `[DATA MISSING: final disclosure validation for detailed SI.Ter workflow variants, operational names, and organisation-specific examples.]` |
| C2-008 | Fragmentation/interoperability intro | Primary: 1.1.1 | MERGE | Merge with C1-010 to avoid repeating the general problem. | — | M | None. |
| C2-009 | Application heterogeneity | Primary fragment: 1.1.1; secondary ecosystem examples: 1.3.2 | SPLIT | Separate the general problem from the component map. | — | M | None. |
| C2-010 | Layer separation | Primary fragment: 1.1.1; secondary limitation fragment: 1.4.4 | SPLIT | Architecture explains fragmentation; observation-boundary caution formalises scope. | — | M | None. |
| C2-011 | Orchestration/routing/decoupling | Primary: 1.1.1; cross-reference only to 2.1.2 | ADAPT | Target 1.1.1 explicitly requires orchestration and decoupling as enabling mechanisms; deeper theory remains in C3-004/C3-006. | — | M | None. |
| C2-012 | Interoperability added value | Primary: 1.1.1 | MERGE | Use as the conclusion of the general-problem sequence. | — | L | None. |
| C2-013 | Ecosystem intro | Primary: 1.3.2 | MERGE | Opens the actor/component map and absorbs the following concise entries. | — | L | None. |
| C2-014 | Corporate/regional systems | Primary: 1.3.2 | MERGE | Direct component/responsibility mapping. | — | L | None. |
| C2-015 | API gateway/middleware | Primary: 1.3.2 | ADAPT | Keep high-level roles; omit product-level detail not needed in Chapter 1. | — | M | None. |
| C2-016 | Identity providers/authentication | Primary fragment: 1.3.2; secondary constraint fragment: 1.2.2 | SPLIT | Ecosystem actors and confidentiality/authorization constraints require distinct treatment. | — | H | None; sensitive values remain excluded. |
| C2-017 | Anagrafe Zero | Primary: 1.3.2; cross-reference only to 2.5.3 | ADAPT | Keep the registry as an ecosystem component; concrete transaction detail is supplied by C3-008. | — | H | `[IMPLEMENTATION CHECK: verify current RVE-54/55/57/100 coverage before retaining framework claims.]` |
| C2-018 | FSE/document infrastructure | Primary: 1.3.2; cross-reference only to 2.5.5 | ADAPT | Keep the component map here; concrete ITI semantics have a separate primary source. | — | H | `[IMPLEMENTATION CHECK: verify ITI-18/43 coverage and preserve the non-implementation of ITI-41.]` |
| C2-019 | ePersonam/context services | Primary: 1.3.2; cross-reference only to 2.5.4 | ADAPT | Keep ePersonam and context services in the ecosystem; C3-013 owns transaction semantics. | — | H | `[IMPLEMENTATION CHECK: verify FLOW_CONTEXT_CALL and repair source punctuation during migration.]` |
| C2-020 | Prescription services | Primary: 1.3.2 | RETAIN | It is a component in scope context but explicitly outside the central implemented flows. | — | L | None. |
| C2-021 | Constraints intro | Primary: 1.2.2 | MERGE | Provides the organising paragraph for normative and organisational constraints. | — | L | None. |
| C2-022 | National/regional constraints | Primary: 1.2.2 | ADAPT | Retain the source hierarchy and cautious legal scope. | — | H | `[DATA MISSING: final list of national and regional legal references.]` |
| C2-023 | Identity/authorization constraints | Primary: 1.2.2 | ADAPT | Retain architectural constraints without exposing attributes, matrices or credentials. | — | H | `[DATA MISSING: final description of disclosable identity attributes and authorization rules.]` |
| C2-024 | Document-management constraints | Primary: 1.2.2 | ADAPT | Retain synthetic-data and document-governance rationale at architectural level. | — | H | `[DATA MISSING: final citation for data-protection and clinical-document governance rules.]` |
| C2-025 | Traceability/audit constraints | Primary: 1.2.2 | ADAPT | Preserve the distinction between production audit and experimental observability. | — | H | `[DATA MISSING: confirmation of disclosable production audit and ATNA details.]` |
| C2-026 | Empty tail/`\newpage` | Destination file boundary only, if required | DEFER | It has no semantic content; the layout command is retained only after pagination is known. | `\newpage`. | L | None. |

## Old Chapter 3

| Source ID | Old placement | New placement | Action | Rationale | Citations/apparatus to preserve | Risk | Expected residual marker |
|---|---|---|---|---|---|---|---|
| C3-001 | State-of-art opening | Primary: new Chapter 2 opening | ADAPT | Retain the joint architecture/performance rationale and align it with the solution-space function. | `chap:stateofart`. | M | None. |
| C3-002 | Integration-architecture intro | Primary: 2.1.2 | MERGE | Use as the opening of the software-architecture block. | `sec:integration-architectures`. | L | None. |
| C3-003 | SOA/ROA | Primary: 2.1.2 | RETAIN | Substantive theory already matches the target and preserves qualified regional examples. | All six keys listed in inventory; `subsec:soa-roa`. | L | None. |
| C3-004 | Gateways/middleware/orchestration | Primary: 2.1.2 | ADAPT | Retain responsibilities and trade-offs; defer code-verification comments and implementation detail. | `subsec:gateway-middleware-orchestration`. | M | None. |
| C3-005 | Synchronous/stateless multi-step flows | Primary: 2.1.2 | ADAPT | Keep architecture semantics and regional evidence; defer source-code implementation sentences. | `arsenal-context-rve-v13`, `arsenal-anagrafe-zero-v26`, `ihe-xdsb`; label. | M | None. |
| C3-006 | Decoupling | Primary: 2.1.2 | RETAIN | Directly satisfies architecture alternatives and evaluation trade-offs. | `subsec:decoupling`. | L | None. |
| C3-007 | Standards intro | Primary: 2.1.3 | MERGE | Opens the standards/protocol section and sets the correct hierarchy of specifications. | `sec:healthcare-standards`. | L | None. |
| C3-008 | FHIR R4 | Primary fragment: 2.1.3; regional fragment: 2.5.3; implementation fragment: DEFER to 3.2.1/3.2.4 | SPLIT | Generic FHIR theory, concrete RVE registry semantics and code evidence have different narrative functions. | `hl7-fhir-r4`, `hl7-fhir-r4-bundle`, `arsenal-anagrafe-zero-v26`; `subsec:fhir-r4`. | H | `[IMPLEMENTATION CHECK: revalidate Patient/Bundle generation before any Chapter 3 reuse.]` |
| C3-009 | IHE IUA | Primary: 2.1.3; cross-reference only to 2.5.2/2.5.4 | ADAPT | Keep IUA generic and explicitly distinct from concrete regional RVE flows. | `ihe-iua`, `arsenal-security-v214`, `arsenal-context-rve-v13`; label. | M | None. |
| C3-010 | IHE XDS.b | Primary: 2.1.3 | RETAIN | Supplies the generic profile, actors and metadata model; concrete transactions follow elsewhere. | `ihe-xdsb`, `affinity-domain-italia-v263`, `ulss3-xvalue-v29`; label. | L | None. |
| C3-011 | ITI transactions | Primary: 2.5.5; cross-reference only from 2.1.3 | ADAPT | Concrete publication/query/retrieval semantics belong in the architecture/transaction section, avoiding duplication of the XDS overview. | `ihe-xdsb`, `ulss3-xvalue-v29`; `subsec:iti-document-transactions`. | H | `[IMPLEMENTATION CHECK: ITI-41 remains analytically relevant but unimplemented.]` |
| C3-012 | SOAP/REST/XML/JSON | Primary: 2.1.3 | RETAIN | Directly matches the target protocol/format comparison and its performance cautions. | Five keys listed in inventory; label. | L | None. |
| C3-013 | SAML/JWT/RVE context security | Primary generic fragment: 2.1.3; RVE-1b fragment: 2.5.2; RVE-121/130 fragment: 2.5.4 | SPLIT | The KB-supported classification separates APMS/IUA theory from regional authentication and context-call transactions. | `arsenal-security-v214`, `arsenal-context-rve-v13`, `apms-auth-v141`; `subsec:saml-jwt`. | M | None; no secret/token content may migrate. |
| C3-014 | Performance intro | Primary: 2.2.1 | MERGE | Opens distributed-system evaluation theory. | `sec:distributed-performance`. | L | None. |
| C3-015 | Latency levels/FCT | Primary: 2.2.1 | RETAIN | Directly supplies the target latency-boundary distinctions. | `iorio-when-latency-matters`; label. | L | None. |
| C3-016 | Point-to-point limits | Primary: 2.2.1 | RETAIN | Provides the benchmark-validity argument required by the target. | `dimitrov-latency-applications`; label. | L | None. |
| C3-017 | Throughput/errors/concurrency/queues | Primary: 2.2.1 | ADAPT | Retain definitions and equation; update obsolete Chapter 8 reference and keep empirical trends conditional. | Throughput equation; `subsec:throughput-errors-concurrency`. | M | `[TO EXPAND: replace the obsolete Chapter 8 reference with the definitive Chapter 3 evaluation section.]` |
| C3-018 | Percentiles/tails/stability | Primary: 2.2.1 | RETAIN | Directly supplies distribution and temporal-stability theory. | `iorio-when-latency-matters`; label. | L | None. |
| C3-019 | Network/routing/buffering/protocol effects | Primary: 2.2.1 | RETAIN | Directly supports path-wide performance interpretation and non-causal grey-box analysis. | `iorio-when-latency-matters`; label. | L | None. |
| C3-020 | Workload-model intro | Primary: 2.2.2 | MERGE | Opens the workload/traffic model sequence. | `sec:workload-models`. | L | None. |
| C3-021 | Poisson arrivals | Primary: 2.2.2 | ADAPT | Retain theory/equation and preserve the explicit lack of operational calibration. | Probability equation; `subsec:poisson-arrivals`. | H | `[DATA MISSING: observed arrival distribution in real RVE systems.]` |
| C3-022 | Non-stationary profiles | Primary: 2.2.2 | RETAIN | Directly supplies variable-rate theory and scenario-design implications. | Expectation equation; `subsec:nonstationary-traffic`. | L | None. |
| C3-023 | Bursts/overload | Primary: 2.2.2 | ADAPT | Retain the distinction among bursts, sustained rate and saturation; preserve calibration gap. | `subsec:bursts-overload`. | H | `[DATA MISSING: operational traces or domain statistics for RVE burst calibration.]` |
| C3-024 | Synthetic workloads | Primary theory fragment: 2.2.2; current-flow list: DEFER to 3.2.2/3.2.3 | SPLIT | Workload theory is suitable for Chapter 2; implementation coverage cannot populate Chapter 3 without current-code verification. | `subsec:synthetic-workloads`. | H | `[IMPLEMENTATION CHECK: revalidate the current flow map; code prevails over the outdated docstring.]` |
| C3-025 | Literature intro | Primary: 2.2.3 | ADAPT | Retain study-scope separation and update the obsolete Chapter 8 reference. | Three literature keys; `sec:latency-throughput-literature`. | M | `[TO EXPAND: replace the obsolete Chapter 8 reference with the definitive Chapter 3 KPI section.]` |
| C3-026 | Latency/throughput synthesis | Primary: 2.2.3 | RETAIN | Directly matches the target literature synthesis and guards against quantitative transfer. | Three literature keys; label. | L | None. |
| C3-027 | LSW/TIV/TU | Primary: 2.2.3 | RETAIN | The target explicitly requires these concepts and their bounded methodological relevance. | `akram-numerical-latency`; label. | L | None. |
| C3-028 | Quantile rules/means | Primary: 2.2.3 | RETAIN | Directly supports the target comparison between quantile- and mean-based reasoning. | `akram-numerical-latency`; label. | L | None. |
| C3-029 | Local vs end-to-end | Primary: 2.2.3 | RETAIN | Concludes the literature discussion with the exact target design lesson. | Three literature keys; label. | L | None. |
| C3-030 | Design-implications intro | Primary: 2.2.4 | MERGE | Opens the theory-to-method requirements sequence. | `sec:framework-implications`. | L | None. |
| C3-031 | Complete-flow measurement | Primary theoretical fragment: 2.2.4; implementation fragment: DEFER to 3.2.3/3.3.2 | SPLIT | Preserve the design implication while preventing old implementation prose from prematurely filling Chapter 3. | `subsec:measure-complete-flows`. | H | `[IMPLEMENTATION CHECK: revalidate orchestration, execution and failure semantics before Chapter 3 reuse.]` |
| C3-032 | Separate measurement levels | Primary theoretical fragment: 2.2.4; implementation fragment: DEFER to 3.3.3/3.4.3 | SPLIT | Keep the non-causal two-level principle in theory; defer collector/mock implementation. | `iorio-when-latency-matters`; label. | H | `[IMPLEMENTATION CHECK: revalidate join fields and mock-middleware behavior before Chapter 3 reuse.]` |
| C3-033 | Structured/normalised logs | Primary theoretical fragment: 2.2.4; schema implementation: DEFER to 3.3.3 | SPLIT | Chapter 2 needs the requirement for structured logs, not the complete implementation schema. | `subsec:structured-normalized-logs`. | H | `[IMPLEMENTATION CHECK: verify current event and normalized-dataset schemas before Chapter 3 reuse.]` |
| C3-034 | Realistic loads/bursts/mixes | Primary theoretical fragment: 2.2.4; operational scenario details: DEFER to 3.4/3.5 | SPLIT | Retain ex ante design implications and defer configurations/results to the data-gated approach chapter. | `subsec:realistic-loads-bursts-mix`. | H | `[DATA MISSING: calibration of flow mixes and temporal profiles using operational RVE statistics.]` plus `[TO EXPAND: replace obsolete Chapter 9 reference.]` |

## Deferred and non-migrated material

No substantive unit is silently discarded.

| Category | Units | Decision |
|---|---|---|
| Commented template examples | C1-001, C2-001 | `DEFER`: recorded as template residue; not thesis evidence and not migrated into prose. |
| Layout-only page breaks | C1-031, C2-026 | `DEFER`: retain only if required after final pagination. |
| Implementation-specific fragments embedded in theory | C3-008, C3-024, C3-031–C3-034 | `DEFER`: potential Chapter 3 sources only after current-code verification; excluded from current coverage. |
| Data-gated experimental claims | C1-030, parts of C3-034 | `DEFER`: markers remain until real framework outputs support the claims. |

## Coverage estimate by new section

The percentages distinguish:

- **Pre-existing text** — directly reusable material with only local editing;
- **Supported adaptation** — synthesis, splitting, merging or transitions grounded
  entirely in existing text;
- **Still to write** — content not supplied by old Chapters 1–3, including
  evidence-gated material.

Implementation fragments marked `DEFER` are not counted as coverage of new
Chapter 3. Percentages are editorial estimates and sum to 100% per section.

| New section | Pre-existing text | Supported adaptation | Still to write | Main uncovered elements |
|---|---:|---:|---:|---|
| 1.1 General Problem and Thesis Problem Statement | 80% | 15% | 5% | Final concise research question and explicit unit of analysis. |
| 1.2 Territorial Healthcare Context and Regulatory Framework | 75% | 15% | 10% | Final legal bibliography, page references and disclosure validation. |
| 1.3 Industrial Context and Interoperability Ecosystem | 75% | 15% | 10% | Verified internship details, stable module names and approved disclosure depth. |
| 1.4 Scope of the Investigation | 25% | 25% | 50% | Systematic in/out scope lists, production-benchmark exclusion, irreproducibility limits and integrated scope rationale. |
| 1.5 Objectives, Expected Artefacts, and Contributions | 70% | 20% | 10% | Clean separation of objectives/artefacts/contributions and final evidence-gated qualifications. |
| 1.6 Structure of the Thesis | 15% | 45% | 40% | Definitive four-chapter roadmap; old roadmap is structurally obsolete. |
| 2.1 Solution Space, Software Architectures, and Interoperability Standards | 60% | 20% | 20% | Explicit comparison of observational, simulation, synthetic and replay-based alternatives. |
| 2.2 Performance Theory, Workload Models, and Design Implications | 85% | 10% | 5% | Minor synthesis and alignment with the definitive chapter numbering. |
| 2.3 Requirements and Project Constraints | 0% | 5% | 95% | Structured functional/non-functional requirements and consolidated project constraints; Chapter 1 constraints can only be cross-referenced. |
| 2.4 Use Cases, Stakeholders, and Process Dependencies | 10% | 10% | 80% | Full protected-discharge/admission narratives, stakeholders and dependency model. |
| 2.5 Interoperability Architecture and RVE/ITI Transactions | 30% | 20% | 50% | Overall architecture, complete authentication/registry/context mapping and traceability matrix. |
| 2.6 Comparative Approach Selection and Ex Ante Acceptance Criteria | 5% | 10% | 85% | Formal alternative comparison, rejection rationale, ex ante thresholds/classes and scenario–metric–evidence matrix. |
| 3.1 Framework Objectives and Overall Architecture | 0% | 0% | 100% | Current-code-based design and repository organisation. |
| 3.2 Data, Workload, and Transaction Generation | 0% | 0% | 100% | Current implementation, including validated RVE/ScrybaSign coverage. |
| 3.3 Execution, Observability, and Metrics Pipeline | 0% | 0% | 100% | Current execution/analytics implementation. |
| 3.4 Evaluation Methodology and Experimental Design | 0% | 0% | 100% | Evaluation questions, verified setup and grey-box operationalisation. |
| 3.5 Load Scenarios, KPIs, and Data Quality | 0% | 0% | 100% | Executed scenarios, KPI protocol and dataset-quality evidence. |
| 3.6 Results, Discussion, and Guidelines | 0% | 0% | 100% | Real outputs and data-gated experimental results. |
| 4.1 Restatement of the Problem | 0% | 0% | 100% | Requires Chapter 3 evidence. |
| 4.2 Summary of Contributions | 0% | 0% | 100% | Must evaluate achieved, not merely expected, contributions. |
| 4.3 Traceability from Objectives to Evidence | 0% | 0% | 100% | Requires final artefacts, KPIs, thresholds and results. |
| 4.4 Applicability of the Results | 0% | 0% | 100% | Requires validated result boundaries. |
| 4.5 Limitations of the Thesis | 0% | 0% | 100% | Requires consolidated experimental and implementation assessment. |
| 4.6 Evolution of the Problem and Future Directions | 0% | 0% | 100% | Requires completed thesis evidence and residual-gap analysis. |

## Coverage summary by chapter

Weighted only across the six top-level sections of each chapter:

| New chapter | Pre-existing text | Supported adaptation | Still to write |
|---|---:|---:|---:|
| Chapter 1 | 56.7% | 22.5% | 20.8% |
| Chapter 2 | 31.7% | 12.5% | 55.8% |
| Chapter 3 | 0% | 0% | 100% |
| Chapter 4 | 0% | 0% | 100% |

These chapter-level percentages are simple section averages, not page-weighted
estimates. They are intended for migration planning and must not be presented as
experimental completeness metrics.
