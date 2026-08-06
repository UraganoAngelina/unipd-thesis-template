# Codex Operating Rules for Thesis Work

These rules are permanent for this thesis workspace unless the user explicitly changes them.

- Treat `/home/alberto/Desktop/Request-Dataset-Generator` as read-only. It may be inspected and used as implementation evidence, but files in that folder must not be edited, generated, deleted, reformatted, or overwritten.
- Treat `/home/alberto/Desktop/unipd-thesis-template` as the editable thesis workspace. Preserve unrelated user changes and keep generated knowledge-base material under `knowledge_base/`.
- Before generating thesis prose, consult `knowledge_base/01_master_prompt_and_rules.md` and the relevant entries in `knowledge_base/02_source_inventory.md`.
- For implementation claims, verify against the current codebase in `/home/alberto/Desktop/Request-Dataset-Generator`; code prevails over older architectural notes.
- Do not expose credentials, tokens, certificate passwords, private endpoints, or personal data in thesis text, summaries, or generated artifacts.
- Chapter 9 is data-gated: do not invent experimental results. Use only real framework outputs/logs/reports.

## Knowledge Base disponibili

Questo progetto ha due knowledge base a grafo (generate con graphify) da consultare 
quando hai bisogno di dettagli poco chiari su codice o teoria:

- `/home/alberto/Desktop/Request-Dataset-Generator/graphify-out/` — knowledge estratta dal codice del framework RDG 
  (architettura, classi, pipeline, esperimenti)
- `/home/alberto/Desktop/unipd-thesis-template/graphify_kb/graphify-out/` — knowledge estratta dalla documentazione di tesi 
  (standard IHE/FHIR/HL7, interoperabilità sanitaria, concetti teorici)
- `/home/alberto/unipd-thesis-template/knowledge_base/unified_graph/graphify-out/`
  — grafo unificato con codice RDG, documentazione tecnica e risultati
  sperimentali sanitizzati.

**Quando consultarle:**
- Prima di fare assunzioni su come è strutturato il codice RDG → consulta code_kb
- Prima di usare terminologia tecnica su standard sanitari/interoperabilità → consulta doc_kb
- Se un termine appare in entrambe, verifica la coerenza tra le due prima di rispondere
- Prima di formulare ipotesi sui risultati live o scrivere il capitolo
  sperimentale, interrogare il grafo unificato e risalire ai file di evidenza.
