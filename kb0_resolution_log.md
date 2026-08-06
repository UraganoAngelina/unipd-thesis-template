# KB0 Resolution Log

Data di esecuzione: 2026-07-29  
Perimetro: tutti i file `.tex` esistenti sotto
`thesis/files/chapters/`  
Unified KB:
`knowledge_base/unified_graph/graphify-out/graph.json` e sotto-grafo empirico
`knowledge_base/experiments/20260727T185227/`

## Esito sintetico

- Marker totali individuati: **19**
- RISOLTO: **0**
- PARZIALMENTE RISOLTO: **6**
- IRRISOLVIBILE allo stato attuale: **13**
- File `.tex` scansionati integralmente: **4/4**
- File `.tex` modificati: **3**

### Marker irrisolvibili da riportare nei report successivi

1. Requisiti di audit di produzione e dettagli ATNA citabili.
2. Date, ruolo, team, deliverable e attività del tirocinio.
3. Validazione finale dei nomi dei moduli SI.Ter.
4. Autorizzazione alla divulgazione dei componenti tecnologici SI.Ter.
5. Attività dello studente nel team RTI validate dal tutor o dall'azienda.
6. Tabella ufficiale delle milestone SI.Ter.
7. Distribuzione degli arrivi osservata nei sistemi RVE operativi.
8. Statistiche operative per calibrare probabilità, dimensione e durata dei burst RVE.
9. Statistiche operative per calibrare flow mix e profili temporali.
10. Soglie e classi di accettabilità ex ante del §2.6.2.
11. Log middleware Level 2 compatibile e relativa evidenza di join.
12. Soglie di accettazione e regole decisionali ex ante richiamate nel Capitolo 3.
13. Confronto live diretto/middleware riuscito, semanticamente comparabile e corredato da log Level 2.

## Completezza della scansione

| File | Righe originali lette | Marker KB0 originali |
|---|---:|---:|
| `thesis/files/chapters/1_introduction.tex` | 415 | 7 |
| `thesis/files/chapters/2_domain.tex` | 987 | 5 |
| `thesis/files/chapters/3_soa.tex` | 659 | 7 |
| `thesis/files/chapters/4_sysanal.tex` | 159 | 0 |
| **Totale** | **2.220** | **19** |

La scansione è stata effettuata con ricerca multilinea, perché diversi marker
attraversano più righe e non sono enumerabili correttamente con una sola
espressione regolare line-oriented.

L'indice normativo è stato letto integralmente dal file reale
`/home/alberto/Downloads/indice_definitivo_tesi.md`. Il percorso indicato nel
prompt, `/home/alberto/Desktop/unipd-thesis-template`, non esiste in questa
sessione; il workspace effettivo e modificabile è
`/home/alberto/unipd-thesis-template`.

## Ispezione della Unified KB

Prima delle query sono stati letti:

- `knowledge_base/unified_graph/README.md`;
- struttura e attributi di
  `knowledge_base/unified_graph/graphify-out/graph.json`;
- `knowledge_base/experiments/20260727T185227/README.md`;
- `experiment_summary.md`;
- `error_taxonomy.md`;
- schema e contenuto di `scenario_metrics.csv` e
  `transaction_outcomes.csv`;
- campi di audit rilevanti di `provenance.json`.

Il grafo usa il formato node-link JSON di NetworkX, con chiavi `nodes` e
`links`. Al momento dell'interrogazione contiene 664 nodi e 1.152 archi,
suddivisi in tre namespace:

| Namespace | Funzione | Nodi |
|---|---|---:|
| `Request-Dataset-Generator` | codice RDG | 533 |
| `graphify_kb` | documentazione tecnica e di dominio | 108 |
| `experiments` | evidenza empirica sanitizzata | 23 |

La directory della Unified KB non include una CLI o script di query propri:
contiene il grafo precompilato e un README sui ponti semantici. È stata quindi
usata la CLI `graphify` installata nell'ambiente, dopo espansione delle query
contro il vocabolario reale dei nodi; i risultati sono stati verificati sui
file empirici sanitizzati.

Il sotto-grafo empirico deriva dalla batteria
`20260727T185227`/`thesis_live_30r`, dichiarata `live`. Il protocollo pianificava
10 scenari e 30 repliche per scenario, cioè 300 run. Il corpus sanitizzato
contiene 145 run avviate e 74 complete, 158.449 flussi completati e 299.534
risposte. I dati quantitativi derivano esclusivamente dalle 74 run complete.

## Query eseguite

Le seguenti espansioni contengono soltanto token presenti nel vocabolario del
grafo:

| ID | Query Graphify espansa | Marker serviti |
|---|---|---|
| Q-GOV | `audit requisiti siter modulo team` | M01--M06 |
| Q-TRAFFIC | `arrivals poisson traffic burst bursts mix live scenario` | M08--M10 |
| Q-EXP | `esperimento protocollo scenario live metriche evidenza transazioni configurazione` | M07, M14, M15, M19 |
| Q-TXN | `transaction live mock iti scrybasign patient context metrics` | M11, M13, M15, M19 |
| Q-MW | `middleware join live metriche scenario` | M16, M18 |
| Q-THRESH | `soglie requisiti protocollo metriche` | M12, M17 |

Sono state inoltre eseguite interrogazioni tabellari mirate:

- aggregazione di `scenario_metrics.csv` per `scenario_id`;
- aggregazione di `transaction_outcomes.csv` per `transaction`,
  `status_code`, `outcome` e `fault_injected`;
- filtro delle transazioni ITI-18, ITI-43,
  `SCRYBASIGN-GET-USER-INFO` e `SCRYBASIGN-SIGN-ONE-DOC`;
- verifica in `provenance.json` di modalità, revisione osservata, completezza
  della scansione e politica di sanitizzazione;
- ricerca negativa nel solo corpus empirico per ATNA, informazioni di
  tirocinio, milestone, warm-up/cool-down, inventario hardware, calibrazione su
  traffico operativo, log middleware e soglie di accettazione.

## Registro dei marker

### M01 — Audit di produzione e ATNA

- File e riga originale:
  `thesis/files/chapters/1_introduction.tex:164`
- Marker originale: `[DATA MISSING: confirmation of which production audit requirements and ATNA-related details may be cited in the final thesis.]`
- Contesto immediato: il paragrafo distingue l'osservabilità sperimentale dai
  requisiti formali di audit dei sistemi di produzione.
- Query: Q-GOV; ricerca mirata di `ATNA` e `audit` nel sotto-grafo empirico.
- Esito: **IRRISOLVIBILE**
- Motivazione: il grafo documentale contiene i nodi
  `graphify_kb::security_iti20_audit` e
  `graphify_kb::infra_audit_log`, ma nessun nodo o artefatto empirico concede
  l'autorizzazione alla divulgazione richiesta dal marker.
- Evidenza necessaria: approvazione aziendale o del tutor e fonte primaria che
  delimiti esplicitamente i requisiti e i dettagli ATNA divulgabili.
- Modifica al `.tex`: nessuna.

### M02 — Dati formali del tirocinio

- File e riga originale:
  `thesis/files/chapters/1_introduction.tex:180`
- Marker originale: `[DATA MISSING: precise internship dates, formal role title, team name, internal deliverables produced, and activities validated by the company tutor.]`
- Contesto immediato: apertura del paragrafo sul tirocinio e sul contesto
  progettuale.
- Query: Q-GOV; ricerca negativa nel sotto-grafo empirico per
  `internship`/`tirocinio`/`tutor`.
- Esito: **IRRISOLVIBILE**
- Motivazione: la Unified KB non contiene una fonte approvata con date, ruolo,
  team, deliverable e validazione del tutor.
- Evidenza necessaria: attestazione di tirocinio, relazione approvata o
  dichiarazione del tutor/azienda.
- Modifica al `.tex`: nessuna.

### M03 — Nomenclatura dei moduli SI.Ter

- File e riga originale:
  `thesis/files/chapters/1_introduction.tex:206`
- Marker originale: `[DATA MISSING: final validation of the SI.Ter module names to use consistently in the submitted thesis.]`
- Contesto immediato: descrizione ad alto livello dell'architettura funzionale
  e tecnologica SI.Ter.
- Query: Q-GOV; nodi documentali SI.Ter e SisTer.
- Esito: **IRRISOLVIBILE**
- Motivazione: il grafo contiene nomi e famiglie di componenti provenienti da
  documenti differenti, ma non una lista canonica approvata per l'elaborato né
  una decisione su eventuali varianti SI.Ter/SisTer.
- Evidenza necessaria: glossario o architettura approvata, con validazione del
  tutor sulla nomenclatura da pubblicare.
- Modifica al `.tex`: nessuna.

### M04 — Disclosure dei componenti SI.Ter

- File e riga originale:
  `thesis/files/chapters/1_introduction.tex:209`
- Marker originale: `[DATA MISSING: final disclosure confirmation for any description of SI.Ter technological components beyond component families and architectural responsibilities.]`
- Contesto immediato: delimitazione del livello di dettaglio tecnologico
  pubblicabile.
- Query: Q-GOV.
- Esito: **IRRISOLVIBILE**
- Motivazione: una KB tecnica può documentare componenti, ma non sostituire
  un'autorizzazione alla divulgazione.
- Evidenza necessaria: conferma scritta del perimetro divulgabile.
- Modifica al `.tex`: nessuna.

### M05 — Attività nel team RTI

- File e riga originale:
  `thesis/files/chapters/1_introduction.tex:219`
- Marker originale: `[DATA MISSING: documented description of the student's activities in the RTI team, validated by the tutor or company documentation.]`
- Contesto immediato: il testo limita le affermazioni a quanto supportato
  sull'ambiente RTI e sull'analisi tecnico-funzionale.
- Query: Q-GOV.
- Esito: **IRRISOLVIBILE**
- Motivazione: nessuna entità della Unified KB descrive e valida le attività
  personali dello studente.
- Evidenza necessaria: relazione di tirocinio o dichiarazione approvata dal
  tutor.
- Modifica al `.tex`: nessuna.

### M06 — Milestone SI.Ter

- File e riga originale:
  `thesis/files/chapters/1_introduction.tex:226`
- Marker originale: `[DATA MISSING: official milestone table and dates, if a SI.Ter project timeline is included.]`
- Contesto immediato: il paragrafo vieta di derivare la timeline da note
  secondarie.
- Query: Q-GOV; ricerca di milestone, pianificazione e cronoprogramma nei nodi
  della Unified KB.
- Esito: **IRRISOLVIBILE**
- Motivazione: non è presente una tabella ufficiale, univoca e approvata delle
  milestone da usare nel testo.
- Evidenza necessaria: piano di progetto ufficiale nella versione autorizzata
  per la tesi.
- Modifica al `.tex`: nessuna.

### M07 — Perimetro della contribuzione sperimentale

- File e riga originale:
  `thesis/files/chapters/1_introduction.tex:380`
- Marker originale: `[DATA MISSING: final executed scenarios, dataset sizes, configuration versions, logs, metric reports, robustness evidence, and validated interpretations required to state the experimental contribution.]`
- Contesto immediato: il paragrafo rende la contribuzione sperimentale
  condizionale a esecuzioni e output validati.
- Query: Q-EXP; aggregazione completa di `scenario_metrics.csv`; verifica di
  `provenance.json`.
- Esito: **PARZIALMENTE RISOLTO**
- Valori inseriti: 74 run live complete, 10 scenari, 158.449 flussi completati,
  299.534 risposte, protocollo pianificato di 300 run e campione sbilanciato.
- Fonti:
  - nodo
    `experiments::knowledge_base_experiments_20260727t185227_readme_dataset_sperimentale_sanitizzato_20260727t185227`;
  - nodo
    `experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001`;
  - entità `scenario_metrics.csv#all-scenarios`;
  - entità `provenance.json#execution_mode`.
- Parte residua: configurazioni run-level sanitizzate e protocollo
  interpretativo approvato.
- Marker residuo inserito: `[DATA MISSING: sanitised run-level configuration parameters and an approved interpretive protocol are still required to delimit the final experimental contribution.]`

### M08 — Distribuzione operativa degli arrivi RVE

- File e riga originale: `thesis/files/chapters/2_domain.tex:359`
- Marker originale: `[DATA MISSING: observed arrival distribution in real RVE systems, required to validate the Poisson model against operational traffic.]`
- Contesto immediato: il modello di Poisson viene qualificato come baseline
  parametrica senza validità empirica attribuita.
- Query: Q-TRAFFIC.
- Esito: **IRRISOLVIBILE**
- Motivazione: la batteria live usa arrivi generati dal framework; non è una
  traccia osservazionale del traffico operativo RVE. Usarla per validare il
  modello generativo sarebbe circolare.
- Esperimento/evidenza necessaria: traccia operativa sanitizzata con timestamp
  di arrivo, finestra di osservazione, copertura dei flow type e regola di
  campionamento; successivo goodness-of-fit contro il modello di Poisson.
- Modifica al `.tex`: nessuna.

### M09 — Calibrazione operativa dei burst RVE

- File e riga originale: `thesis/files/chapters/2_domain.tex:394`
- Marker originale: `[DATA MISSING: operational traces or domain statistics required to calibrate the probability, size, and duration of RVE bursts.]`
- Contesto immediato: il testo dichiara configurabili i burst e nega che le
  dimensioni sintetiche rappresentino automaticamente un processo clinico
  reale.
- Query: Q-TRAFFIC; filtro dello scenario `burst`.
- Esito: **IRRISOLVIBILE**
- Motivazione: lo scenario `burst` contiene burst sintetici configurati, non
  statistiche di burst estratte dal traffico operativo.
- Esperimento/evidenza necessaria: serie temporale operativa sanitizzata e
  criterio documentato per identificare cluster, durata, intensità e frequenza
  dei burst.
- Modifica al `.tex`: nessuna.

### M10 — Calibrazione di flow mix e profili temporali

- File e riga originale: `thesis/files/chapters/2_domain.tex:556`
- Marker originale: `[DATA MISSING: calibration of flow mixes and temporal profiles using operational RVE statistics; until such data become available, the scenarios remain controlled synthetic workloads.]`
- Contesto immediato: conclusione delle implicazioni metodologiche sui carichi,
  sui burst e sui mix di flow.
- Query: Q-TRAFFIC.
- Esito: **IRRISOLVIBILE**
- Motivazione: le frequenze osservate nelle esecuzioni riflettono la
  configurazione generativa del test e non le frequenze dei sistemi operativi.
- Esperimento/evidenza necessaria: conteggi operativi sanitizzati per flow type
  e profilo temporale, con finestra, popolazione e copertura dichiarate.
- Modifica al `.tex`: nessuna.

### M11 — Copertura funzionale per transazione

- File e riga originale: `thesis/files/chapters/2_domain.tex:886`
- Marker originale: `[EXPERIMENTAL RESULT MISSING: per-transaction mock/live execution evidence, conformance outcomes, scenario coverage, and data-quality results required to turn the code-presence column into validated functional coverage.]`
- Contesto immediato: segue la matrice che separa specifica, presenza nel
  codice ed evidenza di esecuzione.
- Query: Q-TXN; aggregazione completa di `transaction_outcomes.csv`.
- Esito: **PARZIALMENTE RISOLTO**
- Valore inserito: copertura live osservata, su 74 run complete, per RVE-1.b,
  RVE-54, RVE-55, RVE-57, RVE-100, RVE-121, RVE-130, RVE-TOKEN, ITI-18,
  ITI-43 e le due operazioni ScrybaSign.
- Fonti:
  - nodo
    `experiments::knowledge_base_experiments_20260727t185227_readme_dataset_sperimentale_sanitizzato_20260727t185227`;
  - entità `transaction_outcomes.csv#all-transactions`.
- Parte residua: evidenza mock per transazione, test di conformità ai profili e
  decisione approvata di validazione funzionale.
- Marker residuo inserito: `[DATA MISSING: transaction-level mock evidence, profile-conformance results, and approved functional-validation decisions are still required to convert observed live execution into validated functional coverage.]`

### M12 — Soglie e criteri ex ante

- File e riga originale: `thesis/files/chapters/2_domain.tex:979`
- Marker originale: `[DATA MISSING: domain-supported transaction- and flow-level thresholds, acceptability classes, minimum sample sizes, repetition policy, saturation decision rule, and the completed scenario--metric--threshold--evidence matrix.]`
- Contesto immediato: §2.6.2 sui criteri di qualità definiti prima
  dell'ispezione dei risultati.
- Query: Q-THRESH, limitata alla verifica delle categorie di KPI strumentate.
- Esito: **IRRISOLVIBILE**
- Motivazione: per regola del Master Prompt, i risultati empirici non possono
  essere usati per derivare retrospettivamente le soglie ex ante. Il
  `WarningDetector` del codice usa valori configurabili, non soglie di dominio
  approvate.
- Evidenza necessaria: fonte clinica/contrattuale/di progetto approvata o
  protocollo sperimentale preregistrato con soglie, campioni, ripetizioni e
  regola di saturazione.
- Modifica al `.tex`: nessuna.

### M13 — Evidenza ScrybaSign

- File e riga originale: `thesis/files/chapters/3_soa.tex:232`
- Marker originale: `[EXPERIMENTAL RESULT MISSING: execute an approved mock validation and a credential-authorised live provider test for \texttt{FLOW\_SCRYBASIGN\_SIGN}; archive the resolved configuration, sanitised logs, outcome, response semantics, and provider-side evidence before assessing functional or performance behaviour.]`
- Contesto immediato: il paragrafo affermava che nessuna run archiviata
  contenesse il flow ScrybaSign.
- Query: Q-TXN; filtro delle due transazioni ScrybaSign per status, outcome e
  fault.
- Esito: **PARZIALMENTE RISOLTO**
- Valori inseriti:
  - `SCRYBASIGN-GET-USER-INFO`: 17.838 successi HTTP 200;
  - `SCRYBASIGN-SIGN-ONE-DOC`: 17.838 outcome, 17.015 successi HTTP 200 e
    823 failure;
  - failure di firma: 28 senza risposta HTTP e 795 HTTP 502 con fault
    iniettato.
- Fonti:
  - entità
    `transaction_outcomes.csv#transaction=SCRYBASIGN-GET-USER-INFO`;
  - entità
    `transaction_outcomes.csv#transaction=SCRYBASIGN-SIGN-ONE-DOC`;
  - nodo
    `experiments::knowledge_base_experiments_20260727t185227_error_taxonomy_transport_timeout`;
  - dataset node
    `experiments::knowledge_base_experiments_20260727t185227_readme_dataset_sperimentale_sanitizzato_20260727t185227`.
- Parte residua: approvazione del mock, prova dell'autorizzazione delle
  credenziali live, semantica della risposta firmata ed evidenza provider-side.
- Marker residuo inserito: `[DATA MISSING: approved mock validation, confirmation that the live execution was credential-authorised, sanitised provider-side evidence, and validation of the signed-response semantics.]`

### M14 — Controlli del protocollo e ambiente

- File e riga originale: `thesis/files/chapters/3_soa.tex:412`
- Marker originale: `[DATA MISSING: approved warm-up and cool-down policy, number of independent repetitions, minimum populations, hardware and operating-system inventory, network path and clock-synchronisation evidence, remote-environment version, run exclusion policy, and final immutable code/configuration revision.]`
- Contesto immediato: protocollo di riproducibilità e catena degli artefatti.
- Query: Q-EXP; `scenario_metrics.csv`; campi di `provenance.json`.
- Esito: **PARZIALMENTE RISOLTO**
- Valori inseriti: 30 repliche pianificate per ciascuno dei 10 scenari; da 5 a
  15 run complete per scenario e 74 complessive; commit RDG osservato
  `f08fb53fd4ad11ef803642c0a066e9a6d9e2b327`, non incorporato nel manifest.
- Fonti:
  - nodo
    `experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001`;
  - entità `scenario_metrics.csv#observed_runs`;
  - entità `provenance.json#source_commit`;
  - entità `provenance.json#source_commit_scope`.
- Parte residua: warm-up/cool-down, popolazioni minime, inventario
  hardware/OS, rete e clock, versione dell'ambiente remoto, esclusioni e
  revisione immutabile incorporata nel manifest.
- Marker residuo inserito con il perimetro ristretto a tali dati.

### M15 — Campagne ITI, ScrybaSign, ramp e stress

- File e riga originale: `thesis/files/chapters/3_soa.tex:462`
- Marker originale: `[EXPERIMENTAL RESULT MISSING: execute the approved ITI, ScrybaSign, load-ramp, stress, and mixed-flow campaigns with independent repetitions and retained artefacts.]`
- Contesto immediato: l'inventario precedente riportava sei run e negava
  copertura ITI, ScrybaSign, ramp e stress.
- Query: Q-EXP e Q-TXN; righe scenario e transazione dei due CSV.
- Esito: **PARZIALMENTE RISOLTO**
- Valori inseriti: 5 run complete `load_ramp`, 5 `stress_extreme`, 6
  `flow_type_comparison_direct`, 15
  `flow_type_comparison_middleware`; outcome live per ITI-18, ITI-43 e le due
  operazioni ScrybaSign.
- Fonti:
  - entità `scenario_metrics.csv#scenario_id=load_ramp`;
  - entità `scenario_metrics.csv#scenario_id=stress_extreme`;
  - entità
    `scenario_metrics.csv#scenario_id=flow_type_comparison_direct`;
  - entità
    `scenario_metrics.csv#scenario_id=flow_type_comparison_middleware`;
  - entità `transaction_outcomes.csv#transaction=ITI-18`;
  - entità `transaction_outcomes.csv#transaction=ITI-43`;
  - entità `transaction_outcomes.csv#transaction=SCRYBASIGN-*`.
- Parte residua: 226 delle 300 run pianificate non sono complete.
- Marker residuo inserito: `[EXPERIMENTAL RESULT MISSING: 226 of the 300 planned runs were not complete; finish the planned repetitions before treating the campaign as final.]`
- Nota editoriale aggiunta: la tabella delle sei run deve essere riconciliata
  in una successiva fase di redazione, senza modificarla durante KB0.

### M16 — Log middleware e join Level 2

- File e riga originale: `thesis/files/chapters/3_soa.tex:501`
- Marker originale: `[DATA MISSING: verified middleware log with compatible occurrence keys, measurement-boundary documentation, clock evidence, and quantified join coverage.]`
- Contesto immediato: controllo qualità dei dataset e distinzione tra Level 1
  e Level 2.
- Query: Q-MW; inventario dei file empirici e `provenance.json`.
- Esito: **IRRISOLVIBILE**
- Motivazione: il corpus sanitizzato contiene log di esecuzione client e
  aggregati whitelisted, ma nessun log middleware Level 2 verificato. I nodi
  `MiddlewareLogParser` e `LogJoiner` attestano capacità del codice, non
  disponibilità empirica dei dati.
- Esperimento/evidenza necessaria: log middleware sanitizzato con chiavi
  compatibili, definizione delle finestre temporali, evidenza di
  sincronizzazione e percentuale di join.
- Modifica al `.tex`: nessuna.

### M17 — Matrice ex ante di accettazione nel Capitolo 3

- File e riga originale: `thesis/files/chapters/3_soa.tex:514`
- Marker originale: `[DATA MISSING: domain-supported acceptance thresholds, required confidence or uncertainty, minimum sample sizes, repetition count, comparison rules, and the scenario--KPI--population--threshold--evidence matrix defined ex ante.]`
- Contesto immediato: distinzione fra warning configurabili del software e
  limiti clinici, contrattuali o di servizio.
- Query: Q-THRESH.
- Esito: **IRRISOLVIBILE**
- Motivazione: come per M12, le osservazioni del Capitolo 3 non possono
  definire le soglie con cui vengono giudicate.
- Evidenza necessaria: protocollo ex ante o fonte di dominio approvata.
- Modifica al `.tex`: nessuna.

### M18 — Confronto diretto/middleware con Level 2

- File e riga originale: `thesis/files/chapters/3_soa.tex:597`
- Marker originale: `[EXPERIMENTAL RESULT MISSING: execute matched direct and mediated live scenarios with a real, documented middleware log; verify occurrence-level joins and observation boundaries before analysing internal latency or resource relationships.]`
- Contesto immediato: limite del confronto grey-box.
- Query: Q-MW; nodo E-MIDDLEWARE-001; scenari
  `direct_vs_middleware` e `flow_type_comparison_middleware`.
- Esito: **IRRISOLVIBILE**
- Motivazione: le 14 run complete `direct_vs_middleware` contengono 1.590
  richieste e le 15 run `flow_type_comparison_middleware` 1.687 richieste; in
  entrambi i casi l'error rate è 100%. Sono failure path, non percorsi riusciti
  comparabili. Manca inoltre il log middleware reale.
- Fonti del limite:
  - nodo
    `experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_middleware_001`;
  - entità `scenario_metrics.csv#scenario_id=direct_vs_middleware`;
  - entità
    `scenario_metrics.csv#scenario_id=flow_type_comparison_middleware`.
- Esperimento/evidenza necessaria: run live corrette e semanticamente
  comparabili per entrambi i percorsi, con log Level 2 e join verificati.
- Modifica al `.tex`: nessuna.

### M19 — Campagna live ripetuta e copertura ITI/ScrybaSign

- File e riga originale: `thesis/files/chapters/3_soa.tex:652`
- Marker originale: `[EXPERIMENTAL RESULT MISSING: complete the approved repeated live campaign, including ITI-18, ITI-43 and \texttt{FLOW\_SCRYBASIGN\_SIGN}, and integrate sanitised Level~2 middleware evidence where available.]`
- Contesto immediato: limiti residui e confine della contribuzione.
- Query: Q-EXP e Q-TXN.
- Esito: **PARZIALMENTE RISOLTO**
- Valori inseriti:
  - ITI-18: 21.722 outcome, 3.395 successi;
  - ITI-43: 21.514 outcome, 21.371 successi;
  - ScrybaSign GetUserInfo: 17.838 successi;
  - ScrybaSign SignOneDoc: 17.838 outcome, 17.015 successi.
- Fonti:
  - entità `transaction_outcomes.csv#transaction=ITI-18`;
  - entità `transaction_outcomes.csv#transaction=ITI-43`;
  - entità
    `transaction_outcomes.csv#transaction=SCRYBASIGN-GET-USER-INFO`;
  - entità
    `transaction_outcomes.csv#transaction=SCRYBASIGN-SIGN-ONE-DOC`;
  - nodo
    `experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001`.
- Parte residua: protocollo incompleto e assenza di dati middleware Level 2.
- Marker residuo inserito: `[EXPERIMENTAL RESULT MISSING: complete the remaining planned repetitions and integrate sanitised Level~2 middleware evidence before drawing final cross-layer or capacity conclusions.]`

## File `.tex` modificati

- `thesis/files/chapters/1_introduction.tex`
- `thesis/files/chapters/2_domain.tex`
- `thesis/files/chapters/3_soa.tex`

`thesis/files/chapters/4_sysanal.tex` è stato letto integralmente e non è stato
modificato.

## Conflitti e disallineamenti rilevati

1. **Inventario sperimentale superato nel Capitolo 3.** La tabella
   `tab:archived-rdg-runs` e il testo adiacente descrivono sei run, in gran
   parte mock. La Unified KB più recente documenta 74 run live complete su
   dieci scenari. KB0 ha segnalato il superamento nel punto del marker M15, ma
   non ha riscritto tabella e paragrafi fuori-marker.
2. **Copertura ITI/ScrybaSign.** Il Capitolo 1 afferma che ITI e firma
   costituiscono sola copertura implementativa; il Capitolo 3 afferma che
   nessuna run archiviata contiene ScrybaSign e che il corpus non copre ITI.
   `transaction_outcomes.csv` documenta invece esecuzioni live di ITI-18,
   ITI-43 e delle due transazioni ScrybaSign. Le frasi fuori-marker devono
   essere riconciliate in Fase D.
3. **Confronto middleware non valido.** La presenza di run
   `direct_vs_middleware` non autorizza un confronto nominale: E-MIDDLEWARE-001
   documenta il 100% di errori nei due scenari middleware disponibili.
4. **Revisione del codice.** Il commit
   `f08fb53fd4ad11ef803642c0a066e9a6d9e2b327` è il checkout osservato durante
   l'estrazione, ma non è incorporato nel manifest della batteria. Non è stato
   presentato come revisione immutabile della run.
5. **Soglie del Capitolo 2.** Non sono presenti soglie numeriche ex ante
   approvate da confrontare con le misure. I valori configurabili del warning
   engine non sono stati trattati come criteri di accettazione. Non è quindi
   emerso un conflitto numerico misura-soglia; persiste invece una lacuna di
   definizione ex ante.
6. **Mock e live.** I nuovi valori inseriti sono sempre qualificati come
   provenienti dalla batteria `live`; i risultati mock già presenti non sono
   stati aggregati con essi.

## Criterio di selezione dei valori

Non sono state selezionate singole run “migliori” o più recenti. Sono stati
usati:

- i conteggi complessivi dichiarati da E-PROTOCOL-001 per il perimetro della
  batteria;
- le aggregazioni pooled già sanitizzate in `scenario_metrics.csv` sulle sole
  74 run complete;
- la somma esatta delle righe di `transaction_outcomes.csv` per transazione,
  status, outcome e fault;
- i campi di provenance esplicitamente qualificati.

Non sono stati arrotondati, interpolati o stimati valori mancanti. Le latenze e
gli altri KPI disponibili non sono stati introdotti in questa fase perché
nessun marker richiedeva un valore prestazionale puntuale e perché le
limitazioni del campione impediscono confronti conclusivi.

## Addendum — chiusura interattiva di Abstract e Capitolo 1

Data: 2026-07-29. Questo addendum registra lo stato corrente senza modificare
retroattivamente gli esiti della scansione KB0 originale.

| ID | Destinazione | Esito corrente | Base della risoluzione |
|---|---|---|---|
| M01 | §1.2.2, audit e ATNA | RISOLTO | Specifica regionale di sicurezza, §4.3.15; esclusione definitiva di configurazioni e record di produzione |
| M02 | §1.3.1, dati formali del tirocinio | RISOLTO | Dichiarazione dell'autore: 09/03/2026--30/09/2026, ruolo e unità; validazione del tutor dichiarata al 30/08/2026 |
| M03 | §1.3.1, nomenclatura SI.Ter | RISOLTO | Decisione editoriale: `SI.Ter` per il programma e denominazioni funzionali, senza tassonomia di prodotto non canonica |
| M04 | §1.3.1, disclosure tecnologica | RISOLTO | Scope definitivo limitato a famiglie di componenti, responsabilità e interfacce necessarie |
| M05 | §1.3.1, attività dello studente | RISOLTO | Dichiarazione dell'autore e validazione del tutor dichiarata; responsabilità formulate per livello di coinvolgimento |
| M06 | §1.3.1, milestone | RISOLTO | Timeline esclusa perché non necessaria alla funzione narrativa del capitolo |
| M07 | §1.5.3, contributo sperimentale | RISOLTO NEL CAPITOLO 1 | Contributo delimitato come metodo e catena di evidenza; risultati e limiti rinviati alla sede primaria del Capitolo 3 |
| C1-EXP-01 | §1.5.3, capacity planning | RISOLTO | Dichiarato esplicitamente non conseguito; identificati i prerequisiti per uno studio successivo |
| C1-EXP-02 | §1.5.3, linee guida | RISOLTO | Limitate a conclusioni supportate da implementazione verificata ed evidenza trattenuta |
| ABS-01 | Abstract, Results | RISOLTO | Dataset sanitizzato `20260727T185227`, E-PROTOCOL-001 e `scenario_metrics.csv` |
| ABS-02 | Abstract, Conclusions | RISOLTO | Sintesi prudenziale dell'artefatto e dei limiti documentati; nessuna inferenza di capacità o produzione |

### Tracciabilità quantitativa dell'abstract

- 10 scenari pianificati, 300 run pianificate, 74 run complete,
  158.449 flussi completati e 299.534 risposte:
  `experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001`
  e `scenario_metrics.csv#all-scenarios`.
- Intervallo da 5 a 15 run complete per scenario e assenza di un log
  middleware Level 2 compatibile:
  `experiments::knowledge_base_experiments_20260727t185227_readme_dataset_sperimentale_sanitizzato_20260727t185227`
  e `provenance.json`.

### Nota temporale

Su istruzione esplicita dell'autore, la prosa adotta il punto di vista della
versione finale successiva al 30/09/2026 e tratta il tirocinio come concluso.
Alla data tecnica di questa modifica, 29/07/2026, sia la validazione dichiarata
del tutor (30/08/2026) sia il termine del tirocinio (30/09/2026) sono futuri.
Le date devono essere ricontrollate prima del deposito definitivo.

### Conteggio corrente nel perimetro interattivo

- File scansionati integralmente: 2/2.
- Marker iniziali: 11.
- Marker risolti: 11.
- Marker residui in `4_abstract.tex` e `1_introduction.tex`: 0.
