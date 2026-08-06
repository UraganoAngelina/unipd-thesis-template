# Esecuzione della libreria mirata — Capitolo 1

## 1. Perimetro ed esito

Sono stati eseguiti congiuntamente i prompt di sezione `1.1`–`1.6` e i
relativi prompt di dettaglio. I prompt padre sono stati trattati come controlli
di completezza e continuità; i prompt figlio hanno governato l'assegnazione
primaria dei singoli frammenti. In questo modo lo stesso testo non è stato
duplicato per soddisfare due prompt gerarchicamente sovrapposti.

Il testo risultante è in
`thesis/files/chapters/1_introduction.tex`. Le cinque sezioni estese usano
`\section`; i blocchi interni, tutti inferiori a una pagina autonoma, usano
`\paragraph` non numerati. Il blocco logico 1.6 è stato declassato a
`\paragraph{Structure of the thesis.}` in applicazione della soglia editoriale
confermata dall'autore.

Le nuove fonti sono state collocate in note con `\footcite` perché lo stile
`verbose-ibid` espande le citazioni complete. In
`thesis/files/config/packages.tex` è stato disabilitato soltanto il link del
richiamo alla nota (`hyperfootnotes=false`), necessario a evitare destinazioni
PDF mancanti causate dall'ordine preesistente di `hyperref` e `footmisc`.

## 2. Fonti candidate individuate prima dell'adattamento

Le righe riportate sono quelle dell'inventario dei capitoli precedenti alla
migrazione; gli identificativi rinviano a `migration_inventory.md`.

| Destinazione | Fonti candidate: file, righe e vecchia collocazione | Trattamento | Citazioni/apparati |
|---|---|---|---|
| 1.1.1 | C1-002, `1_introduction.tex`, 31–34, `Reference Scenario`; C1-010, 73–76, `Information Fragmentation`; C2-002–C2-003, `2_domain.tex`, 53–60; C2-008–C2-012, 79–98 | MERGE/ADAPT; separati gli esempi di ecosistema destinati a 1.3.2 e i limiti osservativi destinati a 1.4.4 | Nessuna citazione attiva nei frammenti; preservato l'anchor di capitolo |
| 1.1.2 | C1-016–C1-020, `1_introduction.tex`, 101–119, `Research Problem` | RETAIN/MERGE/SPLIT; domanda di ricerca e unità di analisi raccordate senza descrivere l'implementazione | Nessun apparato attivo |
| 1.2.1 | C1-007–C1-009, `1_introduction.tex`, 55–72, `Regional Healthcare Context`; C2-003–C2-007, `2_domain.tex`, 57–78 | MERGE/SPLIT; strutture, attori e impatto della digitalizzazione riuniti | Aggiunta la fonte primaria `dm-77-2022` con locator all'Allegato 1 |
| 1.2.2 | C1-009; C2-021–C2-025, `2_domain.tex`, 129–148, `Constraints` | MERGE/ADAPT; separati vincoli normativi, identità, documenti e audit | `chap:domain` preservato; aggiunte fonti normative e tecniche, restano marker puntuali |
| 1.3.1 | C1-003–C1-006, `1_introduction.tex`, 35–53, `Thesis Context`; C1-011–C1-015, 77–100, `SI.Ter` | MERGE/ADAPT; mantenuti distinti contesto industriale, ruolo dell'integratore e fatti personali non documentati | Aggiunta `regione-veneto-ddr-11922-2026`; nessun dettaglio riservato |
| 1.3.2 | C1-005, C1-008, C1-012–C1-014; C2-013–C2-020, `2_domain.tex`, 99–128 | MERGE/SPLIT/ADAPT; ruoli di ecosistema mantenuti qui, transazioni rinviate al Capitolo 2 | Aggiunte le chiavi già esistenti per APMS, Anagrafe Zero, XDS.b e chiamata di contesto |
| 1.4.1 | C1-019, 112–115; C1-024–C1-025, 131–138; C1-028, 146–158 | SPLIT/ADAPT; il perimetro è distinto dalla descrizione interna del framework | Verifica contro `FLOW_TYPES`, configurazioni e run RDG correnti |
| 1.4.2 | C1-014, C1-019–C1-020; C2-021, C2-024–C2-025 | ADAPT; l'elenco sistematico era assente come unità autonoma | Nessuna duplicazione di credenziali, dati sanitari o parametri riservati |
| 1.4.3 | Nessuna unità autonoma; frammenti di controllo sperimentale in C1-019 e di separazione dei layer in C2-010 | ADAPT con raccordo supportato; esplicitata l'esclusione richiesta dall'indice | Nessuna misura o soglia aggiunta |
| 1.4.4 | C1-020, 116–119; C1-029, 159–162; C2-010, 87–90 | MERGE/SPLIT; sede primaria del divieto causale assegnata a 1.4.4 | Preservata la qualificazione grey-box e la separazione delle provenienze |
| 1.4.5 | Nessuna unità autonoma; limiti impliciti in C1-019–C1-020 e nella distinzione mock/live | ADAPT con raccordo supportato | Nessun risultato di produzione simulato |
| 1.4.6 | Nessuna unità autonoma; sintesi di C1-019–C1-020, C2-021 e C2-024–C2-025 | ADAPT; motivazione complessiva costruita solo da inclusioni ed esclusioni già supportate | Nessun apparato aggiunto |
| 1.5.1 | C1-021–C1-025, `1_introduction.tex`, 120–138, `Thesis Objectives` | MERGE/SPLIT; obiettivi separati dagli artefatti e dai contributi | Nessuna promessa di esito prestazionale |
| 1.5.2 | C1-024, 131–134; C1-028, 146–158; C1-030, 163–165 | SPLIT/MERGE; output software distinti dall'evidenza sperimentale | Catena degli artefatti verificata nella codebase e nei run |
| 1.5.3 | C1-026–C1-030, 139–165, `Main Contributions` | MERGE/ADAPT; contributi attesi distinti da quelli dimostrati | Risultati, capacity planning e linee guida restano data-gated |
| 1.6 | C1-031, `1_introduction.tex`, 166–170, `Structure of the Dissertation` | ADAPT; roadmap obsoleta sostituita dalla progressione normativa in quattro capitoli | `sec:thesis-structure` preservato; blocco declassato a `\paragraph` |

## 3. Verifica della matrice

La matrice approvata è stata rispettata:

- i frammenti C1-002/C1-010 e C2-002–C2-012 hanno sede primaria in
  1.1.1;
- C1-016–C1-020 alimentano 1.1.2, con il solo limite osservativo
  formalizzato nuovamente in 1.4.4 senza duplicazione argomentativa;
- C1-007–C1-009 e C2-003–C2-007 alimentano 1.2.1;
- C2-021–C2-025 alimentano 1.2.2;
- C1-003–C1-015 e C2-013–C2-020 alimentano 1.3;
- C1-021–C1-030 alimentano 1.5;
- C1-031 alimenta esclusivamente il blocco logico 1.6.

I marker pianificati per la fonte del DM 77/2022 e per il DDR
11922/2026 sono stati chiusi mediante fonti primarie e nuove chiavi
BibLaTeX. Gli altri marker non sono stati rimossi perché l'evidenza richiesta
non è disponibile o necessita di approvazione alla divulgazione.

## 4. Esito dei singoli prompt

| Prompt | Esito | Modifica editoriale principale | Copertura |
|---|---|---|---|
| 1.1 | Eseguito | Sezione riallineata al titolo normativo e verificata come sequenza problema generale → problema specifico | Completa |
| 1.1.1 | Eseguito | Fusi frammentazione applicativa, informativa e organizzativa, separazione dei layer, orchestrazione e disaccoppiamento | Completa |
| 1.1.2 | Eseguito | Conservati gap sperimentale, limite cross-layer, domanda di ricerca e unità di analisi | Completa |
| 1.2 | Eseguito | Contesto territoriale e vincoli ricondotti a una sola sede primaria | Parziale |
| 1.2.1 | Eseguito | Aggiunti riferimenti puntuali a DM 77 per strutture, COT e collegamento M6C1 | Completa |
| 1.2.2 | Eseguito | Distinte fonte normativa, governance regionale e specifiche tecniche | Parziale: fonti privacy/documenti e audit ancora mancanti |
| 1.3 | Eseguito | Origine industriale raccordata alla mappa dell'ecosistema | Parziale |
| 1.3.1 | Eseguito | Conservati solo fatti documentati; governance SI.Ter ora citata | Parziale: attività personali, milestone e disclosure |
| 1.3.2 | Eseguito | Attori, piattaforme e servizi condivisi mantenuti ad alto livello; transazioni rinviate al Capitolo 2 | Completa al livello introduttivo |
| 1.4 | Eseguito | Perimetro riorganizzato in sei paragrafi complementari e non ripetitivi | Completa |
| 1.4.1 | Eseguito | Esplicitati contratti, famiglie di flusso, dimensioni prestazionali e distinzione capacità/evidenza | Completa |
| 1.4.2 | Eseguito | Elencate esclusioni funzionali, normative, tecniche e informative | Completa |
| 1.4.3 | Eseguito | Motivata l'esclusione del benchmark di produzione | Completa |
| 1.4.4 | Eseguito | Esclusa la causalità fra layer non sincronizzati; ammesso solo confronto descrittivo | Completa |
| 1.4.5 | Eseguito | Qualificata la validità esterna di mock e live | Completa |
| 1.4.6 | Eseguito | Inclusioni ed esclusioni ricondotte a rilevanza, sicurezza, controllo e replicabilità | Completa |
| 1.5 | Eseguito | Obiettivi, artefatti e contributi separati in una catena verificabile | Parziale |
| 1.5.1 | Eseguito | Quattro obiettivi verificabili; esplicitati protected discharge/admission | Completa |
| 1.5.2 | Eseguito | Artefatti software e documentali distinti dall'evidenza di scenario | Completa |
| 1.5.3 | Eseguito | Contributi analitico, tecnico e metodologico formulati; contributi empirici mantenuti condizionali | Parziale: risultati, robustezza, capacity planning e linee guida |
| 1.6 | Eseguito | Roadmap aggiornata ai quattro capitoli; declassamento per granularità | Completa |

## 5. Copertura per sezione

Le percentuali sono stime editoriali e distinguono recupero testuale,
adattamento supportato e contenuto ancora non sostenuto.

| Sezione | Testo preesistente | Adattamento supportato | Ancora da scrivere |
|---|---:|---:|---:|
| 1.1 The General Problem and the Thesis Problem Statement | 80% | 20% | 0% |
| 1.2 Territorial Healthcare Context and Regulatory Framework | 70% | 20% | 10% |
| 1.3 Industrial Context and the Interoperability Ecosystem | 70% | 15% | 15% |
| 1.4 Scope of the Investigation | 30% | 70% | 0% |
| 1.5 Objectives, Expected Artefacts, and Contributions | 65% | 25% | 10% |
| 1.6 Structure of the Thesis | 15% | 85% | 0% |

## 6. Marker e gap residui

| Destinazione | Tipo | Gap |
|---|---|---|
| 1.2.2 | `SOURCE NEEDED` | Fonti autoritative per trattamento dei dati sanitari e ciclo di vita dei documenti clinici |
| 1.2.2 | `TO EXPAND` | Eventuale sottoinsieme divulgabile di attributi di identità e matrici autorizzative |
| 1.2.2 | `DATA MISSING` | Requisiti di audit di produzione e dettagli ATNA divulgabili |
| 1.3.1 | `DATA MISSING` | Date, ruolo, team, deliverable e attività di tirocinio validate |
| 1.3.1 | `DATA MISSING` | Nomi definitivi dei moduli SI.Ter |
| 1.3.1 | `DATA MISSING` | Profondità divulgabile dei componenti tecnologici SI.Ter |
| 1.3.1 | `DATA MISSING` | Attività dello studente nel team RTI validate |
| 1.3.1 | `DATA MISSING` | Milestone e date, soltanto se la timeline sarà mantenuta |
| 1.5.3 | `DATA MISSING` | Scenari, dataset, configurazioni, report, robustezza e interpretazioni validate |
| 1.5.3 | `TO EXPAND` | Modello di capacity planning dopo validazione di metriche e calibrazione |
| 1.5.3 | `TO EXPAND` | Linee guida derivate dai risultati dei Capitoli 3 e 4 |

## 7. Fonti e KB consultate

- Documentation KB:
  `graphify_kb/graphify-out/graph.json`, interrogata per DM 77/2022, COT,
  M6C1, contesto veneto e separazione tra requisiti normativi e vincoli di
  progetto.
- Fonti documentali primarie:
  `graphify_kb/DM_77_2022.pdf`, in particolare preambolo, art. 1 e
  Allegato 1, pp. 12 e 20–21; `graphify_kb/DDR 11922 del
  16.03.2026_SITER.pdf`, pp. 1–3.
- Code KB:
  `/home/alberto/Desktop/Request-Dataset-Generator/graphify-out/graph.json`,
  interrogata per famiglie di flusso, artefatti e confini di osservabilità.
- Codice e artefatti correnti, in sola lettura:
  `rve_transactions/flow_orchestrator.py`,
  `request_dataset_generator.py` e le directory `runs/`.

Le query Graphify hanno orientato la verifica; le formulazioni definitive su DM
77 e SI.Ter sono state controllate nei documenti primari, mentre le affermazioni
sul perimetro RDG sono state controllate nel codice, che prevale sulla KB.

## 8. Controlli narrativi ed editoriali

- La progressione è: continuità informativa → domanda di ricerca → contesto
  vincolante → origine empirica → perimetro → obiettivi e verificabilità.
- Il Capitolo 1 non confronta le alternative, non descrive classi o moduli e non
  anticipa risultati: questi contenuti restano nei Capitoli 2 e 3.
- Ogni frammento ha una sola sede primaria; i richiami ai capitoli successivi
  sostituiscono la duplicazione.
- I titoli delle cinque sezioni estese coincidono con l'indice definitivo. I
  titoli dei `\paragraph` sono complementari e non ripetono meccanicamente il
  lessico del livello superiore.
- La ripetizione di “Problem Statement” tra capitolo e sezione 1.1 è mantenuta
  come eccezione perché imposta esplicitamente dall'indice normativo.
- I label `chap:introduction`, `chap:domain`,
  `sec:problem-to-question`, `sec:territorial-regulatory`,
  `sec:industrial-ecosystem`, `sec:scope-investigation`,
  `sec:objectives-artefacts-contributions` e `sec:thesis-structure` sono
  preservati. Nei frammenti migrati non erano presenti figure, tabelle o
  listing attivi.

## 9. Validazione LaTeX

- Recipe: `latexmk -pdf -shell-escape thesis.tex`, dalla directory
  `thesis/files/`.
- Esito: riuscito; `thesis.pdf` prodotto in 86 pagine.
- Nessuna citation o reference indefinita e nessun label duplicato nei capitoli
  inclusi.
- Nessun overfull box attribuito al Capitolo 1 nello stato finale.
- Restano warning preesistenti del template o di altri capitoli: opzione
  `xcolor`, destinazioni pagina duplicate nel backmatter e overfull box fuori
  dal Capitolo 1.
