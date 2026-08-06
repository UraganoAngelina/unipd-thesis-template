# Drafting Report

> **Perimetro:** esecuzioni C1 e C2 — Capitoli 1 e 2.
>
> **Marker KB0 irrisolvibili ancora aperti:** M01 (dettagli
> ATNA divulgabili), M02 (dati formali del tirocinio), M03 (nomenclatura
> canonica dei moduli SI.Ter), M04 (perimetro di disclosure tecnologica),
> M05 (attività personali nel team RTI), M06 (milestone ufficiali SI.Ter).
> M07 resta parzialmente risolto per l'assenza di configurazioni run-level
> sanitizzate e di un protocollo interpretativo approvato.

## File letti

- `/home/alberto/Downloads/indice_definitivo_tesi.md`, integralmente.
- `/home/alberto/.codex/attachments/d1aa4341-1143-4270-9487-41dbe1d65ff0/pasted-text.txt`,
  integralmente.
- `knowledge_base/01_master_prompt_and_rules.md`.
- `knowledge_base/02_source_inventory.md`.
- `kb0_resolution_log.md`.
- `thesis/files/chapters/1_introduction.tex`, integralmente.
- `thesis/files/chapters/2_domain.tex` e
  `thesis/files/chapters/3_soa.tex`, per i soli confini narrativi e rinvii.
- `thesis/files/references/bibliography.bib`.
- Fonti originali o estrazioni indicizzate di DM 77/2022, DDR 11922/2026,
  capitolato SI.Ter, relazione tecnica RTI, infrastruttura di sicurezza,
  APMS, Anagrafe Zero, chiamata di contesto e Affinity Domain.
- Codice corrente RDG: `main.py`, `request_dataset_generator.py`,
  `timeline_generator.py`, `traffic_exec_engine.py`,
  `rve_transactions/flow_orchestrator.py`, `log_collector.py`,
  `metric_engine.py`.
- Unified KB, Code KB e Documentation KB tramite query `graphify`.
- Fonti normative ufficiali online: EUR-Lex per il regolamento (UE)
  2016/679 e Gazzetta Ufficiale per il decreto FSE 2.0.

## File modificati

- `thesis/files/chapters/1_introduction.tex`.
- `thesis/files/references/bibliography.bib`.
- `drafting_inventory.md` — inventario iniziale limitato al Capitolo 1.
- `drafting_plan.md` — piano operativo limitato al Capitolo 1.
- `drafting_report.md`.

## Interventi redazionali

### Contenuti estesi dalla bozza

- Inseriti raccordi introduttivi minimi per le sezioni 1.1--1.5.
- Rafforzato il collegamento tra frammentazione informativa e fonti
  istituzionali/progettuali SI.Ter.
- Integrati in 1.2.2 i vincoli applicabili al trattamento dei dati sanitari,
  alla protezione per progettazione, alla sicurezza, ai profili autorizzativi,
  alla tracciabilità e agli audit log.
- Rafforzato il contesto SI.Ter con capitolato e relazione tecnica RTI.
- Precisato in 1.4.1 che copertura implementativa, esecuzione e validazione
  positiva sono categorie distinte.

### Correzioni strutturali

- Convertiti i quindici contenuti figli da `\paragraph` a `\subsection`.
- Riprodotti esattamente tutti i titoli prescritti dall'indice definitivo.
- Promossa *Structure of the Thesis* da paragrafo interno a 1.5 a sezione 1.6.
- Preservate tutte le label esistenti e tutti gli elenchi LaTeX.

### Contenuto rimosso dalla sede corrente

Il paragrafo con i valori della campagna live `20260727T185227` è stato rimosso
da 1.5.3 perché anticipava risultati quantitativi nel Capitolo 1. Non è stato
scartato come evidenza: rimane tracciato in `kb0_resolution_log.md`, M07, e deve
essere collocato nella sede primaria 3.6.3, con limiti di protocollo e
campionamento. Il marker residuo di M07 è stato mantenuto.

## Sezione → fonti effettivamente usate

| Destinazione | Fonti effettive |
|---|---|
| 1.1.1 | Bozza preesistente; DDR 11922/2026; capitolato SI.Ter |
| 1.1.2 | Bozza; Code KB; codice `FlowOrchestrator`, executor e pipeline di osservabilità |
| 1.2.1 | DM 77/2022, Allegato 1; DDR 11922/2026 |
| 1.2.2 | Regolamento (UE) 2016/679, artt. 9, 25 e 32; decreto FSE 2.0, art. 25; specifiche APMS, sicurezza GDL-O, chiamata di contesto, Anagrafe Zero e Affinity Domain |
| 1.3.1 | DDR 11922/2026; capitolato SI.Ter; relazione tecnica RTI; bozza preesistente |
| 1.3.2 | Documentation KB; APMS; Anagrafe Zero; IHE XDS.b; chiamata di contesto; relazione tecnica RTI |
| 1.4.1 | Codice RDG corrente; Unified KB; KB0 M07 |
| 1.4.2--1.4.6 | Bozza preesistente; limiti del protocollo documentati nella Unified KB |
| 1.5.1 | Indice definitivo; bozza preesistente; architettura corrente RDG |
| 1.5.2 | `main.py`; generatori; timeline; executor; collector; metric engine |
| 1.5.3 | KB0 M07; Unified KB empirica, usata solo per delimitare e non per anticipare risultati |
| 1.6 | Indice definitivo dei Capitoli 1--4 |

## Nodi ed entità KB consultati

### Unified KB — codice

- `Request-Dataset-Generator::rve_transactions_flow_orchestrator_floworchestrator`
- `Request-Dataset-Generator::request_dataset_generator_build_workload`
- `Request-Dataset-Generator::timeline_generator_build_timeline`
- `Request-Dataset-Generator::log_collector_frameworklogparser`
- `Request-Dataset-Generator::log_collector_normalizeddatasetbuilder`
- `Request-Dataset-Generator::metric_engine_metricscalculator`
- `Request-Dataset-Generator::fhir_patient_generator`

### Unified KB — documentazione

- `graphify_kb::rti_almaviva_offerta`
- `graphify_kb::rti_epersonam`
- `graphify_kb::rti_sister`
- `graphify_kb::security_iap`
- `graphify_kb::security_iti20_audit`
- `graphify_kb::infra_audit_log`
- `graphify_kb::rti_anagrafica_gateway`
- `graphify_kb::xvalue_xds_repository`

### Unified KB — evidenza empirica

- `experiments::knowledge_base_experiments_20260727t185227_readme_dataset_sperimentale_sanitizzato_20260727t185227`
- `experiments::knowledge_base_experiments_20260727t185227_experiment_summary_esperimento_20260727t185227`
- `experiments::knowledge_base_experiments_20260727t185227_readme_protocollo_live_incompleto`
- entità già registrate da KB0:
  `scenario_metrics.csv#all-scenarios`,
  `provenance.json#execution_mode`,
  `transaction_outcomes.csv#transaction=ITI-18`,
  `transaction_outcomes.csv#transaction=ITI-43`,
  `transaction_outcomes.csv#transaction=SCRYBASIGN-GET-USER-INFO`,
  `transaction_outcomes.csv#transaction=SCRYBASIGN-SIGN-ONE-DOC`.

## Marker residui

| Marker | Esito | Motivazione / evidenza richiesta |
|---|---|---|
| M01 — audit di produzione e ATNA | IRRISOLVIBILE | Serve approvazione aziendale o del tutor sul dettaglio divulgabile. La normativa FSE supporta la categoria generale, non la disclosure dell'architettura di produzione. |
| M02 — dati formali del tirocinio | IRRISOLVIBILE | Serve attestazione o relazione approvata con date, ruolo, team e deliverable. |
| M03 — nomi dei moduli SI.Ter | IRRISOLVIBILE | Serve glossario canonico approvato; i documenti espongono nomenclature non uniformi. |
| M04 — disclosure componenti SI.Ter | IRRISOLVIBILE | Serve autorizzazione esplicita alla pubblicazione. |
| M05 — attività nel team RTI | IRRISOLVIBILE | Serve una descrizione validata dal tutor o dall'azienda. |
| M06 — milestone SI.Ter | IRRISOLVIBILE | Serve il piano ufficiale autorizzato per la tesi. |
| M07 — contributo sperimentale | PARZIALMENTE RISOLTO | Mancano configurazioni run-level sanitizzate e protocollo interpretativo approvato. |
| Capacity-planning model | TO EXPAND | Può essere formulato solo dopo validazione di metriche, envelope degli scenari e ipotesi di calibrazione. |
| Design/evaluation guidelines | TO EXPAND | Devono derivare dai risultati validati nei Capitoli 3--4. |

Marker risolti in C1:

- `SOURCE NEEDED` sui vincoli relativi ai dati sanitari e ai documenti
  clinici, sostituito con GDPR e decreto FSE 2.0.
- `TO EXPAND` sulla matrice di attributi/autorizzazioni, sostituito da una
  delimitazione supportata che esclude valori e matrici non divulgabili.

## Conflitti

1. **Copertura ITI/ScrybaSign:** la bozza affermava che tali percorsi fossero
   soltanto implementati. La Unified KB contiene invece evidenza di esecuzione
   live. La frase è stata corretta senza anticipare esiti o quantità.
2. **Risultati nel Capitolo 1:** il testo riportava run, scenari, flussi e
   risposte della campagna live. I valori sono supportati, ma narrativamente
   appartengono a 3.6.3; sono stati rimossi dalla sede corrente e registrati
   per ricollocazione.
3. **ATNA:** la Documentation KB documenta ITI-20 e infrastrutture di audit,
   ma non autorizza la divulgazione di dettagli produttivi. M01 resta aperto.
4. **Capacity planning:** l'indice lo indica come contributo atteso; il corpus
   non autorizza a presentarlo come risultato conseguito. Il testo mantiene
   una formulazione condizionale.

## Copertura ottenuta

| Sezione | Stato dopo C1 | Copertura stimata |
|---|---|---:|
| 1.1 | COMPLETA | 100% |
| 1.2 | REDATTA SUPPORTATA CON GAP | 90% |
| 1.3 | BOZZA PARZIALE SUPPORTATA | 70% |
| 1.4 | COMPLETA | 100% |
| 1.5 | REDATTA SUPPORTATA CON GAP | 80% |
| 1.6 | COMPLETA | 100% |
| Capitolo 1 complessivo | REDATTO SUPPORTATO CON MARKER RESIDUI | 88% |

Su 16 destinazioni terminali del Capitolo 1, 13 risultano complete e 3
restano parziali: 1.2.2 per M01, 1.3.1 per M02--M06 e 1.5.3 per M07 e per i
contributi che dipendono dai risultati.

## Controlli narrativi

- Progressione verificata: continuità informativa → problem statement →
  contesto territoriale/normativo → contesto industriale/ecosistema → scope →
  obiettivi/artefatti/contributi → struttura della tesi.
- Evitata la descrizione dettagliata dell'implementazione, riservata al
  Capitolo 3.
- Standard, alternative e transazioni dettagliate restano nella sede primaria
  del Capitolo 2.
- Nessuna correlazione causale è attribuita a livelli osservativi non
  sincronizzati.
- Mock, live, produzione e middleware reale/sintetico restano distinti.
- Obiettivi e contributi non predeterminano l'esito sperimentale.
- La struttura 1.1--1.6 e tutti i titoli coincidono con l'indice definitivo.

## Validazione LaTeX

- Recipe eseguita dalla directory `thesis/files`:
  `latexmk -pdf -shell-escape -synctex=1 -interaction=nonstopmode
  -file-line-error thesis.tex`.
- Esito: **SUCCESSO**, exit code 0.
- Biber: eseguito correttamente; entrambe le nuove chiavi bibliografiche sono
  state risolte.
- Errori LaTeX o di package: nessuno.
- Citazioni o riferimenti indefiniti: nessuno.
- Output: `thesis.pdf`, 94 pagine, 2.114.729 byte.
- Il root document osservato al momento della build include i Capitoli 1--3
  ma non il Capitolo 4. `thesis.tex` non è stato modificato in C1.
- Il corpo del Capitolo 1 non ha prodotto nuovi warning di box. Due titoli
  normativi lunghi generano overfull box nell'indice generale
  (circa 1,73 pt e 11,17 pt); i titoli non sono stati abbreviati perché
  l'indice definitivo ne impone la fedeltà. Gli altri warning di box e i
  duplicate page destination provengono da contenuti o configurazioni esterni
  alla modifica C1.

## Conteggio finale

- Estensione del file: 460 righe, 3.361 parole.
- Gerarchia: 1 capitolo, 6 sezioni, 15 sottosezioni.
- Marker residui: 7 `DATA MISSING`, 2 `TO EXPAND`, 0 `SOURCE NEEDED`,
  0 `EXPERIMENTAL RESULT MISSING`.

# Addendum C2 — Solution Space and Evaluation Criteria

> **Marker KB0 del Capitolo 2 ancora aperti:** M08 (distribuzione degli
> arrivi), M09 (calibrazione dei burst), M10 (flow mix e profili temporali) e
> M12 (soglie e protocollo decisionale) restano irrisolvibili; M11 resta
> parzialmente risolto. Nessun valore è stato stimato, interpolato o derivato
> dai risultati per colmare questi gap.

## Pre-flight specifico

- `kb0_resolution_log.md` copre l'intero albero dei capitoli e, per il
  Capitolo 2, i marker M08--M12.
- Il file C2 è stato letto integralmente prima della modifica: 993 righe,
  11.790 parole, 6 sezioni, 6 sottosezioni, 31 paragrafi, 4 apparati tabellari
  e 35 label.
- La libreria mirata
  `/home/alberto/.codex/attachments/a287d0ad-2482-4726-8e81-d098bf162a2b/pasted-text.txt`
  è stata letta integralmente.
- Sono stati verificati il termine del Capitolo 1 e l'apertura del Capitolo 3
  per controllare la continuità narrativa.

## File letti e modificati

Letti, oltre ai file di pre-flight già indicati:

- `thesis/files/chapters/2_domain.tex`, integralmente;
- `thesis/files/chapters/1_introduction.tex` e
  `thesis/files/chapters/3_soa.tex`, ai confini narrativi;
- `thesis/files/references/bibliography.bib`;
- capitolato SI.Ter e relazione tecnica RTI;
- specifiche APMS, RVE-1.b, Anagrafe Zero, chiamata di contesto, XDS.b,
  XValue e Affinity Domain;
- codice RDG corrente relativo a orchestrazione, costruzione del workload,
  timeline, esecuzione e metriche;
- Unified KB e Documentation KB tramite le query `graphify` descritte sotto;
- Zhu, Chen e Chiueh, *TBBT*, dalla pagina primaria USENIX.

Modificati:

- `thesis/files/chapters/2_domain.tex`;
- `thesis/files/references/bibliography.bib`, con la sola nuova chiave
  `zhu-tbbt-trace-replay` attribuibile a C2;
- `drafting_inventory.md`, addendum dello stato iniziale C2;
- `drafting_plan.md`, addendum gap → fonte C2;
- `drafting_report.md`, presente addendum.

## Contenuti redatti o estesi

- **2.1:** completato il confronto tra osservazione operativa, benchmark
  isolati, generazione sintetica controllata e trace replay. La fonte sul
  replay è usata soltanto per completezza, dipendenze e ricostruzione dello
  stato; non sono trasferiti al dominio sanitario i risultati del file-server
  studiato.
- **2.2:** preservata la teoria già supportata e resi espliciti confini di
  misura, popolazioni, percentili, livelli osservativi e condizioni prudenziali
  per parlare di saturazione. M08--M10 sono rimasti invariati.
- **2.3:** sostituiti requisiti candidati non tracciati con nove requisiti
  funzionali derivati e otto requisiti non funzionali verificabili. Aggiunti
  attore/precondizione, comportamento, esito e limite dell'evidenza; chiarito
  che non costituiscono una baseline contrattuale firmata.
- **2.4:** ricostruita la parte supportata dei percorsi di dimissione e
  ammissione protetta; aggiunte la mappa analitica delle responsabilità e la
  tabella delle dipendenze. Le due catene tecniche complete non documentate
  sono state ristrette a marker `SOURCE NEEDED` precisi.
- **2.5:** consolidata la vista architetturale senza esporre deployment,
  endpoint o ownership non autorizzati; aggiornate le transazioni RVE/ITI e la
  matrice di copertura distinguendo specifica, presenza nel codice, esecuzione
  live osservata e conformità.
- **2.6:** motivata la selezione del framework configurabile mock/live e
  formalizzato ogni criterio come tupla
  scenario--popolazione--metrica--statistica--finestra--direzione--soglia--gate
  di evidenza. Definite le classi non assessabile, accettato, supportato
  condizionalmente e respinto senza introdurre soglie numeriche post hoc.

## Sezione → fonti effettivamente usate

| Sezione | Fonti effettive |
|---|---|
| 2.1 | Bozza preesistente; OASIS SOA RM; HL7 FHIR R4; IHE IUA/XDS.b; specifiche regionali; Zhu, Chen e Chiueh per i soli principi di trace replay |
| 2.2 | Bozza; Iorio et al.; Dimitrov et al.; Akram et al.; Unified KB codice per categorie strumentate e generatori temporali; M08--M10 |
| 2.3 | Capitolato SI.Ter; relazione tecnica RTI; APMS; RVE-1.b; Anagrafe Zero; chiamata di contesto; XDS.b/XValue/Affinity Domain; codice RDG per la verificabilità |
| 2.4 | Capitolato SI.Ter, pp. 35--36; relazione tecnica RTI, pp. 12 e 18--21; specifiche RVE-1.b, RVE-121/130, Anagrafe Zero e XDS.b |
| 2.5 | Specifiche regionali e IHE; relazione RTI, p. 17; codice corrente `FlowOrchestrator`; Unified KB empirica, M11 |
| 2.6 | Analisi delle sezioni 2.1--2.5; letteratura sul replay; categorie KPI confermate dalla Unified KB codice; M12 usato come vincolo, non come fonte di soglie |

## Nodi ed entità KB consultati

### Unified KB — codice

- `FlowOrchestrator`
  (`rve_transactions/flow_orchestrator.py:L126`);
- `build_workload()`
  (`request_dataset_generator.py:L68`);
- `build_timeline()`
  (`timeline_generator.py:L177`) e i generatori `constant_rate`,
  `step_profile`, `daily_clinical_profile`, `inject_bursts`;
- `ConcurrencyTracker`
  (`traffic_exec_engine.py:L772`);
- `MetricsCalculator`
  (`metric_engine.py:L171`);
- `WarningDetector`
  (`metric_engine.py:L698`).

### Unified KB — evidenza empirica

L'unico valore quantitativo empirico introdotto o confermato in C2 è la
copertura di **74 run live complete**. La tracciabilità richiesta è:

- dataset:
  `experiments::knowledge_base_experiments_20260727t185227_readme_dataset_sperimentale_sanitizzato_20260727t185227`;
- entità di dettaglio:
  `transaction_outcomes.csv#all-transactions`;
- transazioni osservate: RVE-1.b, RVE-54, RVE-55, RVE-57, RVE-100,
  RVE-121, RVE-130, RVE-TOKEN, ITI-18, ITI-43,
  SCRYBASIGN-GET-USER-INFO e SCRYBASIGN-SIGN-ONE-DOC.

Questa evidenza è descritta come copertura di esecuzione e di esito, non come
conformità ai profili o come misura di produzione.

### Documentation KB

Consultati i nodi relativi a `Capitolato Tecnico SI.Ter`, `Requisiti COT`,
`Dimissione Protetta End To End`, `RTI AlmavivA Offerta Tecnica`, `APMS`,
`Anagrafe Zero`, `RVE-54 Patient Query`, `RVE-121 GetAccessToken`,
`RVE-130 Chiamata Contesto`, `Identity And Assertion Provider`,
`RVE-1 Authenticate And Get Assertion`, `IHE XDS.b`,
`XDS Document Registry`, `XDS Document Repository` e
`Affinity Domain Italia`.

## Marker e gap residui

| Sede | Stato | Evidenza necessaria |
|---|---|---|
| 2.2, M08 | IRRISOLVIBILE | Distribuzione osservata degli arrivi nei sistemi RVE reali |
| 2.2, M09 | IRRISOLVIBILE | Tracce o statistiche operative per probabilità, dimensione e durata dei burst |
| 2.2, M10 | IRRISOLVIBILE | Statistiche operative per calibrare mix dei flussi e profili temporali |
| 2.4, dimissione protetta | SOURCE NEEDED | Mappatura di processo autorevole che unisca IAP, Anagrafe Zero, XDS.b/SVAMA e COT con condizioni di ramo |
| 2.4, ammissione protetta | SOURCE NEEDED | Mappatura approvata di autenticazione, prescrizione, contesto, anagrafe e notifica ADI |
| 2.5, M11 | PARZIALMENTE RISOLTO | Evidenza mock per transazione, conformance test e decisioni funzionali approvate |
| 2.6, trace replay | SOURCE NEEDED | Traccia RVE autorizzata e sanitizzata con semantica documentata di cattura e replay |
| 2.6, M12 | IRRISOLVIBILE | Soglie esterne, numerosità minima, ripetizioni, regola di saturazione e matrice completa |

Non restano marker `TO EXPAND` nel Capitolo 2.

## Conflitti e decisioni editoriali

1. **Esecuzione e conformità:** M11 documenta esecuzioni live, mentre la bozza
   trattava più percorsi come mera presenza nel codice. La matrice è stata
   aggiornata senza promuovere l'esecuzione a conformance test.
2. **Catene dei casi d'uso:** le specifiche descrivono le singole transazioni,
   ma non autorizzano a unirle nella catena completa richiesta dall'indice. È
   stata redatta solo la sequenza funzionale documentata e mantenuto il gap.
3. **Soglie ex ante:** i default del `WarningDetector` e i valori osservati
   non sono stati usati come soglie. Il conflitto potenziale con una
   valutazione post hoc è risolto rendendo obbligatoria una provenienza esterna.
4. **Titoli adiacenti:** per applicare la regola successiva di non ripetizione,
   2.1 è stato rinominato *Architectural Options and Interoperability
   Foundations* e 2.6 *Experimental Choice and Ex Ante Acceptability*. Funzione,
   ordine e label sono preservati.
5. **Granularità minima:** i blocchi autonomi e superiori a circa una pagina
   restano `\subsection` (2.1.2--2.1.3 e 2.2.1--2.2.4). I blocchi 2.1.1,
   2.3.1--2.3.3, 2.4.1--2.4.4, 2.5.1--2.5.6 e 2.6.1--2.6.2 sono mantenuti come
   paragrafi non numerati dopo fusione e rimozione delle ridondanze. Il loro
   contenuto non è stato eliminato.

## Copertura ottenuta

| Sezione | Stato dopo C2 | Copertura stimata |
|---|---|---:|
| 2.1 | REDATTA SUPPORTATA CON GAP DI INPUT | 95% |
| 2.2 | REDATTA SUPPORTATA CON GAP DI CALIBRAZIONE | 90% |
| 2.3 | COMPLETA COME SPECIFICA ANALITICA | 100% |
| 2.4 | REDATTA SUPPORTATA CON DUE MAPPING APERTI | 80% |
| 2.5 | REDATTA SUPPORTATA CON VALIDAZIONE PARZIALE | 90% |
| 2.6 | REDATTA EX ANTE CON SOGLIE APERTE | 85% |
| Capitolo 2 complessivo | REDATTO SUPPORTATO CON MARKER RESIDUI | 90% |

## Controlli narrativi

- Verificata la progressione: alternative e standard → teoria e workload →
  requisiti → casi d'uso → transazioni → selezione e criteri.
- La teoria generale resta in 2.1--2.2; le transazioni concrete hanno sede
  primaria in 2.5, con rinvii impliciti e senza duplicazioni estese.
- La soluzione RDG è motivata in 2.6, mentre struttura interna e risultati
  restano nel Capitolo 3.
- Ogni riferimento a mock, live, conformance e produzione mantiene categorie
  distinte.
- Nessuna correlazione causale è affermata tra osservazioni client e middleware
  non sincronizzate.
- I criteri ex ante non incorporano risultati osservati né default
  implementativi.
- Il termine del Capitolo 1 anticipa correttamente il solution space; l'apertura
  del Capitolo 3 riprende le dipendenze, i confini di misura e la separazione
  delle evidenze fissati in C2.

## Validazione LaTeX

- Recipe:
  `latexmk -pdf -shell-escape -synctex=1 -interaction=nonstopmode
  -file-line-error thesis.tex`, eseguita da `thesis/files`.
- Esito: **SUCCESSO**, exit code 0; Biber ha risolto anche
  `zhu-tbbt-trace-replay`.
- Nessun errore LaTeX, riferimento o citazione indefinita.
- Nessun float fuori pagina e nessun overfull box attribuibile al Capitolo 2.
- Restano warning preesistenti nel sommario, nel Capitolo 3 e nella
  sitografia; non sono stati modificati perché esterni al perimetro C2.
- Output: `thesis/files/thesis.pdf`, 103 pagine, 2.156.030 byte.
- Estensione finale C2: 1.132 righe, 13.222 parole.
- Gerarchia: 1 capitolo, 6 sezioni, 6 sottosezioni; i blocchi brevi restano
  paragrafi non numerati.
- Apparati: 4 tabelle ordinarie, 3 `longtable`, nessuna figura o listing.
- Marker residui: 5 `DATA MISSING`, 3 `SOURCE NEEDED`, 0 `TO EXPAND`,
  0 `EXPERIMENTAL RESULT MISSING`.

# Addendum — chiusura interattiva di Abstract e Capitolo 1

## Esito

- Scansionati integralmente `thesis/files/preface/4_abstract.tex` e
  `thesis/files/chapters/1_introduction.tex`.
- Marker iniziali nel perimetro: 11.
- Marker chiusi: 11.
- Marker residui nel perimetro: 0.
- Copertura rispetto ai marker: **100%**.

## Informazioni raccolte interattivamente

L'autore ha dichiarato:

- tirocinio dal 09/03/2026 al 30/09/2026;
- ruolo formale `Digital Health Domain Consultant`;
- unità `Digital Health - Nordest`;
- validazione formale del tutor dichiarata al 30/08/2026;
- partecipazione ai SAL, con presentazione di materiale prodotto dall'autore;
- analisi dei requisiti, documentazione, coordinamento e monitoraggio,
  verifica, test e validazione per migrazioni dati e flussi SIOC, SIAR e
  HOSPICE;
- configurazione tecnica e formazione degli operatori per le funzionalità di
  cartella clinica elettronica delle strutture intermedie e di fatturazione;
- produzione di analisi dei requisiti, proof of concept funzionali, flowchart
  di interoperabilità e assessment tecnologici presso Aziende sanitarie
  venete;
- assenza di ulteriori limiti di divulgazione dichiarati.

La prosa distingue partecipazione, produzione documentale, coordinamento,
verifica e configurazione tecnica; non attribuisce allo studente ownership
complessiva dei sistemi o responsabilità aziendali non dichiarate.

## Risoluzioni editoriali e fonti

| Gap | Risoluzione | Fonte |
|---|---|---|
| Audit/ATNA | Dettagli produttivi esclusi; mantenuto il vincolo architetturale sugli audit record | `arsenal-security-v214`, §4.3.15 |
| Dati e attività del tirocinio | Integrati ruolo, unità, periodo, attività e deliverable | Dichiarazione dell'autore e validazione del tutor dichiarata |
| Nomi dei moduli SI.Ter | `SI.Ter` usato per il programma; aree nominate per funzione | Decisione editoriale coerente con il corpus documentale |
| Disclosure tecnologica | Scope limitato a famiglie, responsabilità e interfacce necessarie | Regole di riservatezza e minimizzazione del Master Prompt |
| Milestone | Timeline esclusa perché non necessaria | Decisione di scope |
| Contributo sperimentale | Definito come metodo e catena di evidenza, con risultati nella sede primaria | Unified KB empirica; continuità con Capitolo 3 |
| Capacity planning | Non dichiarato come risultato conseguito; indicati i prerequisiti | Limiti E-PROTOCOL-001 |
| Linee guida | Limitate a evidenza verificata, senza claim di produzione | Capitolo 3 e Unified KB |
| Abstract — Results | Inseriti conteggi esatti e limiti della campagna live | Dataset `20260727T185227`, E-PROTOCOL-001 |
| Abstract — Conclusions | Sintesi prudenziale di contributo e validità | Evidenza e limiti della Unified KB |

## Tracciabilità dei valori dell'abstract

I valori 10 scenari, 300 run pianificate, 74 run complete, 158.449 flussi,
299.534 risposte e 5--15 run complete per scenario provengono da:

- `experiments::knowledge_base_experiments_20260727t185227_experiment_summary_e_protocol_001`;
- `experiments::knowledge_base_experiments_20260727t185227_readme_dataset_sperimentale_sanitizzato_20260727t185227`;
- `scenario_metrics.csv#all-scenarios`;
- `provenance.json`.

Non sono state introdotte latenze, soglie, stime o aggregazioni ulteriori.

## Nota temporale da verificare

L'autore ha chiesto di redigere il testo dal punto di vista della versione
finale, trattando il tirocinio come concluso. Al 29/07/2026 la validazione
dichiarata del tutor (30/08/2026) e il termine del tirocinio (30/09/2026) sono
ancora futuri. Entrambe le date devono essere verificate prima del deposito.

## Validazione

- Recipe:
  `latexmk -pdf -shell-escape -synctex=1 -interaction=nonstopmode
  -file-line-error thesis.tex`.
- Esito: **SUCCESSO**, exit code 0.
- Nessun errore LaTeX, riferimento o citazione indefinita.
- Nessun nuovo overfull box attribuibile all'abstract o al Capitolo 1.
- Gli overfull residui provengono dal sommario, dal Capitolo 3 e dalla
  sitografia e sono esterni a questa chiusura.
- Output: `thesis/files/thesis.pdf`, 104 pagine, 2.167.298 byte.
- Abstract: 41 righe, 802 parole.
- Capitolo 1: 491 righe, 3.685 parole.
- Verifica finale dei marker nel perimetro: **0 occorrenze**.
