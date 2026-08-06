# Report finale di migrazione — nuovi Capitoli 1–3

> Aggiornamento C1–C3: il Capitolo 3 è stato sviluppato mediante verifica del
> codice corrente e degli artefatti archiviati. La tracciabilità aggiornata,
> la nuova copertura, i marker residui e i controlli narrativi sono riportati
> in `chapter_adaptation_report.md`. Le sezioni storiche sottostanti restano
> conservate come audit trail delle fasi P3–P7.

**Stato corrente autorevole:** i Capitoli 1–3 sono ora adattati; il Capitolo 3
contiene sei sezioni sostanziali verificate su codice e artefatti. Restano 36
marker (11 nel Capitolo 1, 16 nel Capitolo 2 e 9 nel Capitolo 3). La
compilazione corrente produce un PDF di 93 pagine senza errori, riferimenti o
citazioni indefinite e senza label duplicati.

## 1. Perimetro ed esito

La migrazione P3–P7 ha prodotto:

- il nuovo Capitolo 1 in `thesis/files/chapters/1_introduction.tex`;
- il nuovo Capitolo 2, completo nella parte teorica e strutturato con lacune
  esplicite nelle parti non sostenute, in
  `thesis/files/chapters/2_domain.tex`;
- il nuovo Capitolo 3, sviluppato con contenuto implementativo verificato e
  risultati limitati agli artefatti realmente disponibili, in
  `thesis/files/chapters/3_soa.tex`;
- il presente report, collegato a `migration_inventory.md` e
  `migration_matrix.md`.

Il Capitolo 4 e i capitoli successivi non sono stati modificati. Le eliminazioni
dei residui del vecchio template osservate durante il lavoro appartengono alla
pulizia effettuata dall'utente e non sono state ripristinate.

## 2. File letti, modificati e consultati

### File normativi e di tracciamento

- `/home/alberto/Downloads/indice_definitivo_tesi.md`, letto integralmente;
- `knowledge_base/01_master_prompt_and_rules.md`;
- `knowledge_base/02_source_inventory.md`;
- `migration_inventory.md`;
- `migration_matrix.md`;
- `chapter1_targeted_prompts_report.md`;
- `chapter2_targeted_prompts_report.md`;
- `thesis/files/thesis.tex`, configurazioni e recipe `latexmkrc`.

### File LaTeX modificati

| File | Intervento |
|---|---|
| `thesis/files/chapters/1_introduction.tex` | Migrazione e fusione dei vecchi Capitoli 1–2 nel nuovo Capitolo 1. |
| `thesis/files/chapters/2_domain.tex` | Migrazione del vecchio Capitolo 3 nel nuovo Capitolo 2, separazione teoria/transazioni/criteri e inserimento delle lacune. |
| `thesis/files/chapters/3_soa.tex` | Sostituzione del precedente capitolo teorico con il nuovo approccio selezionato, verificato su codice e artefatti. |
| `thesis/files/references/bibliography.bib` | Aggiunte le fonti primarie per DM 77/2022, DDR 11922/2026, capitolato tecnico SI.Ter e relazione tecnica SI.Ter. |
| `thesis/files/config/packages.tex` | Disabilitato il solo hyperlink dei richiami a piè di pagina per evitare anchor mancanti con `footmisc`; il testo e le note restano invariati. |

### Fonti implementative e Knowledge Base

La Code KB in
`/home/alberto/Desktop/Request-Dataset-Generator/graphify-out/` è stata
interrogata per orientare il controllo di confine del Capitolo 3. Le indicazioni
sono state poi verificate sul codice corrente, in particolare su:

- `main.py`;
- `fhir_patient_generator.py`;
- `request_dataset_generator.py`;
- `timeline_generator.py`;
- `traffic_exec_engine.py`;
- `log_collector.py`;
- `metric_engine.py`;
- `rve_transactions/flow_orchestrator.py`;
- i moduli transazionali RVE, ITI e ScrybaSign richiamati dalla mappa corrente.

La Documentation KB in
`/home/alberto/unipd-thesis-template/graphify_kb/graphify-out/` è stata
consultata per chiarire la classificazione tra IHE IUA, APMS, SAML/JWT e
transazioni RVE e, nella revisione mirata del Capitolo 1, per localizzare le
fonti su DM 77/2022, COT, M6C1 e SI.Ter. Le affermazioni inserite sono state
verificate nei documenti primari; i dettagli non sostenuti sono rimasti marcati.

È stato rilevato un conflitto documentale già registrato nella matrice: una
descrizione interna del generatore non elenca tutta la copertura corrente dei
flow type. Per la futura stesura del Capitolo 3 dovrà prevalere la mappa
effettivamente usata dal codice, non la descrizione obsoleta. Nessun elenco
implementativo è stato trasferito nel testo definitivo prima di tale verifica.

## 3. P3 — Nuovo Capitolo 1

### Mini-report per sezione

| Sezione logica | Esito |
|---|---|
| 1.1 General problem e problem statement | Fusi frammentazione informativa, necessità di orchestrazione, gap sperimentale, domanda di ricerca e unità di analisi. Rimossi dettagli implementativi e roadmap obsoleta. |
| 1.2 Contesto territoriale e vincoli | Integrati sistema veneto, DM 77/2022, PNRR, COT, identità, documenti e audit. Chiusi i marker bibliografici per DM 77 e governance SI.Ter; restano fonti privacy/audit e limiti di divulgazione. |
| 1.3 Contesto industriale ed ecosistema | Fusi tirocinio, ruolo del system integrator, SI.Ter, RTI e mappa degli attori/componenti. Evitate descrizioni aziendali non documentate. |
| 1.4 Scope | Separati in-scope, out-of-scope, esclusione del benchmark di produzione, esclusione della causalità cross-layer e limiti di validità esterna. |
| 1.5 Obiettivi, artefatti e contributi | Riformulati come elementi verificabili; i contributi sperimentali restano condizionati a esecuzioni reali. |
| 1.6 Struttura della tesi | Aggiornata alla progressione approvata in quattro capitoli e declassata a `\paragraph{}` per estensione inferiore a una pagina. |

### Sorgente → destinazione

| Unità sorgente | Destinazione primaria | Azione effettiva |
|---|---|---|
| C1-002, C1-010, C2-002, C2-003, C2-008–C2-012 | 1.1.1 | MERGE/ADAPT |
| C1-016–C1-020 | 1.1.2 e limiti in 1.4 | MERGE/SPLIT |
| C1-007–C1-009, C2-004–C2-006, C2-021–C2-025 | 1.2 | MERGE/SPLIT/ADAPT |
| C1-003–C1-006, C1-011–C1-015, C2-013–C2-020 | 1.3 | MERGE/SPLIT/ADAPT |
| Frammenti di C1-014, C1-019–C1-020 e limiti distribuiti nei vecchi Capitoli 1–2 | 1.4 | SPLIT/ADAPT |
| C1-021–C1-030 | 1.5 | MERGE/SPLIT |
| C1-031 | 1.6 | ADAPT; declassato a paragrafo |
| C1-001, C2-001, C2-026 | Anchor preservati; commenti di esempio e soli spazi/page break non migrati | SPLIT/DEFER |

I commenti LaTeX del template con figure, listing e citazioni dimostrative non
erano apparati attivi della tesi e non sono stati trasformati in contenuto. Il
label attivo `chap:domain` è stato conservato una sola volta come anchor del
blocco territoriale del Capitolo 1.

## 4. P4 — Nuovo Capitolo 2

### Contenuto riutilizzato

- architetture SOA/ROA, gateway, middleware, orchestrazione e disaccoppiamento;
- FHIR R4, IHE IUA, XDS.b, ITI, SOAP/REST/XML/JSON e SAML/JWT;
- teoria di latenza, throughput, error rate, concorrenza, code e percentili;
- processi di Poisson, profili non stazionari, burst e workload sintetici;
- letteratura su latenza applicativa, MPI e load sharing;
- implicazioni metodologiche su workflow completi, livelli osservativi, log e
  controllo del carico.

Sono state preservate le tre equazioni, tutte le chiavi bibliografiche attive e
tutti i label attivi del vecchio Capitolo 3. Sono state aggiunte soltanto due
chiavi bibliografiche supportate dai documenti primari di progetto per
documentare i percorsi territoriali; le altre chiavi sono rimaste invariate.

### Contenuto adattato o rinviato

- i dettagli di classi, flow type, schema JSONL, collector e metric engine sono
  stati rimossi dal livello teorico e rinviati alla verifica del Capitolo 3;
- i riferimenti obsoleti ai Capitoli 8 e 9 sono stati sostituiti dal confine
  corretto verso il nuovo Capitolo 3;
- la teoria prestazionale definisce dimensioni e popolazioni, mentre le soglie di
  accettazione restano esplicitamente mancanti;
- lo stato dell'arte motiva i criteri di scelta, ma non viene presentato come
  descrizione della soluzione già implementata;
- i casi d'uso sono stati ricostruiti solo per gli step sostenuti dal capitolato
  e dalla relazione tecnica SI.Ter; requisiti approvati, responsabilità e
  catene transazionali non documentate restano marcati.

### Copertura P4

| Sezione logica | Copertura | Nota |
|---|---:|---|
| 2.1 Solution space, architectures, standards | 92% | Manca una fonte per l'alternativa replay e il confronto completo. |
| 2.2 Performance theory, workloads, literature, implications | 98% | Completa sul piano teorico; manca la calibrazione su traffico operativo. |
| 2.3 Requirements and constraints | 55% | Capacità candidate e vincoli sono tracciati, ma manca una specifica approvata e numerata. |
| 2.4 Use cases, stakeholders, dependencies | 45% | Gli step sostenuti dalle fonti SI.Ter sono presenti; catene tecniche, responsabilità e diagrammi restano aperti. |
| 2.5 Architecture and RVE/ITI transactions | 80% | Famiglie e copertura codice sono tracciate; mancano deployment validato, mapping ai casi ed evidenza mock/live. |
| 2.6 Approach selection and ex ante criteria | 65% | Confronto qualitativo e schema ex ante presenti; soglie, classi e fonte replay mancanti. |

## 5. P5 — Controllo di confine del Capitolo 3 (snapshot storico)

### Frammenti potenzialmente migrabili

| Unità | Destinazione futura | Decisione |
|---|---|---|
| C3-008 | 3.2.1 e 3.2.4 | Riutilizzabile solo dopo verifica di Patient, Bundle e serializzazioni nel codice corrente. |
| C3-011, C3-013 | 3.2.3–3.2.4 | Riutilizzabili per composizione ITI/RVE e sicurezza, separando specifica e copertura implementata. |
| C3-017 | 3.3.4 e 3.5.2 | Riutilizzabile per formule e livelli dei KPI, non per soglie o risultati. |
| C3-021–C3-024 | 3.2.2 e 3.3.1 | Riutilizzabili come ponte teorico; algoritmi e flow map devono essere verificati. |
| C3-031 | 3.2.3 e 3.3.2 | Riutilizzabile per dipendenze, sequenzialità interna e concorrenza esterna. |
| C3-032–C3-033 | 3.3.3 e 3.4.3 | Riutilizzabili dopo verifica di eventi, join, dati mancanti e provenienza. |
| C3-034 | 3.4–3.5 | Riutilizzabile come vincolo metodologico; configurazioni presenti non equivalgono a test eseguiti. |

Questo era lo stato al termine di P5. In C3 i frammenti sono stati verificati
contro il codice corrente e migrati nelle sei sezioni definitive. Copertura e
gap correnti sono riportati in `chapter_adaptation_report.md`.

### Gap analysis

| Sezione | Gap principale | Evidenza necessaria |
|---|---|---|
| 3.1 | Obiettivi tecnici, architettura e repository non ancora narrati | Codice corrente, configurazione, diagramma verificato e confini della pipeline. |
| 3.2 | Generazione dati/workload e moduli transazionali non documentati nel capitolo | Generator, orchestrator, moduli RVE/ITI/ScrybaSign, artefatti di esempio non sensibili. |
| 3.3 | Execution, observability e metric pipeline non documentati | Executor, timeline, schema eventi, normalizzazione, metriche e report effettivi. |
| 3.4 | Domande di valutazione e setup non definiti | Protocollo approvato, variabili, controlli, ambiente, seed, ripetizioni e versioni. |
| 3.5 | Scenari, KPI operativi e quality gate non fissati | Configurazioni eseguite, formule, popolazioni, finestre, soglie supportate e controlli dati. |
| 3.6 | Validazione e risultati assenti | Log e report reali, inclusi fallimenti e flusso ScrybaSign; nessun risultato simulato come produzione. |

### Roadmap di produzione

1. Congelare commit/versione e configurazione del codice da descrivere.
2. Documentare `main.py` e i confini della pipeline, quindi produrre un diagramma
   verificato.
3. Verificare generatori, flow map e moduli transazionali; distinguere
   analizzato, implementato, validato in mock e validato in live.
4. Documentare timeline ed execution engine, inclusi ordine degli step,
   placeholder, errori e concorrenza.
5. Definire schema eventi, normalizzazione, join opzionali e metriche con
   formule, unità, popolazioni e provenienza.
6. Approvare domande, scenari, controlli, seed, ripetizioni e soglie ex ante.
7. Eseguire la validazione funzionale e gli esperimenti; conservare
   configurazioni, log, artefatti e report.
8. Scrivere risultati e linee guida soltanto dopo i controlli di completezza e
   validità.

## 6. P6 — De-duplicazione e continuità narrativa

| Problema rilevato | Sede primaria e modifica conservativa |
|---|---|
| Frammentazione e continuità ripetute nei vecchi Capitoli 1–2 | Sede primaria in 1.1; nel Capitolo 2 resta solo il presupposto necessario al confronto. |
| Contesto territoriale, progetto SI.Ter e componenti mescolati | Contesto istituzionale in 1.2, origine industriale e mappa dell'ecosistema in 1.3. |
| Standard generici e transazioni regionali duplicati | Teoria primaria in 2.1; semantica concreta e copertura RVE/ITI primaria in 2.5, con soli rinvii tra le due sedi. |
| Teoria prestazionale mescolata a metriche implementate | Teoria e requisiti metodologici in 2.2; implementazione e KPI operativi rinviati a 3.3–3.5. |
| Implicazioni del design trasformate in descrizione dettagliata del codice | Ridotte a requisiti metodologici; i dettagli verificabili sono elencati nella roadmap P5. |
| Causalità implicita tra framework e middleware | Esclusa in 1.4 e richiamata in 2.2/2.6 senza duplicare la spiegazione completa. |
| Roadmap del vecchio indice e riferimenti a Capitoli 8–9 | Sostituiti dalla sequenza definitiva in quattro capitoli e dal rinvio al Capitolo 3. |

### Granularità e titolazione

- Tutte le sottosezioni target brevi del Capitolo 1 sono rese con
  `\paragraph{}`; la breve 1.6 è stata declassata e accodata alla sezione 1.5.
- Nel Capitolo 2, soltanto i blocchi teorici 2.1.2–2.1.3 e 2.2.1–2.2.4 hanno
  estensione sufficiente per `\subsection`.
- Le sezioni 2.3–2.6 hanno acquisito estensione e autonomia sufficienti e sono
  ora `\section`; i relativi elementi interni più brevi restano
  `\paragraph{}` non numerati.
- Le sei sezioni del Capitolo 3 contengono ora prosa verificata sufficiente e
  sono `\section`; i blocchi interni restano paragrafi non numerati.
- I titoli interni dei Capitoli 1–3 sono stati resi complementari ai rispettivi
  livelli superiori, preservando i termini tecnici non sostituibili.

## 7. Marker residui

Lo snapshot P7 conteneva 36 marker. Lo stato corrente ne contiene ancora 36:
11 nel Capitolo 1, 16 nel Capitolo 2 e 9 nel Capitolo 3. L’elenco autorevole è in
`chapter_adaptation_report.md`; le tabelle seguenti sono conservate come audit
trail dello snapshot precedente.

### Capitolo 1

| Linea | Tipo | Lacuna |
|---:|---|---|
| 131 | SOURCE NEEDED | Fonti autoritative su trattamento dei dati sanitari e ciclo di vita dei documenti clinici. |
| 144 | TO EXPAND | Attributi e regole di autorizzazione divulgabili, solo se mantenuti. |
| 164 | DATA MISSING | Requisiti di audit/ATNA divulgabili. |
| 180 | DATA MISSING | Dati formali del tirocinio. |
| 206 | DATA MISSING | Nomi definitivi dei moduli SI.Ter. |
| 209 | DATA MISSING | Limite di divulgazione dei componenti SI.Ter. |
| 219 | DATA MISSING | Attività personali nel team RTI. |
| 226 | DATA MISSING | Milestone ufficiali, se mantenute. |
| 380 | DATA MISSING | Scenari, dataset, versioni, log, robustezza e risultati reali. |
| 384 | TO EXPAND | Modello di capacity planning dopo calibrazione. |
| 387 | TO EXPAND | Linee guida derivate dai risultati validati. |

### Capitolo 2

| Linea | Tipo | Lacuna |
|---:|---|---|
| 23 | TO EXPAND | Replay e matrice delle alternative. |
| 359 | DATA MISSING | Distribuzione osservata degli arrivi. |
| 394 | DATA MISSING | Calibrazione dei burst. |
| 556 | DATA MISSING | Calibrazione di mix e profili. |
| 602 | TO EXPAND | Requisiti funzionali approvati. |
| 623 | TO EXPAND | Requisiti non funzionali testabili. |
| 643 | SOURCE NEEDED | Vincoli di progetto approvati. |
| 678 | TO EXPAND | Catena approvata della dimissione protetta. |
| 699 | TO EXPAND | Catena approvata dell'ammissione protetta. |
| 719 | TO EXPAND | Responsabilità degli stakeholder. |
| 737 | TO EXPAND | Diagrammi e dipendenze dei processi. |
| 765 | TO EXPAND | Architettura funzionale/deployment validata. |
| 801 | TO EXPAND | Ruolo di RVE-54/55/57 nei casi d'uso. |
| 886 | EXPERIMENTAL RESULT MISSING | Evidenza mock/live e conformance per transazione. |
| 937 | SOURCE NEEDED | Fonte replay o decision record. |
| 979 | DATA MISSING | Soglie, classi, campioni, ripetizioni e matrice ex ante. |

### Capitolo 3

| Linea | Tipo | Lacuna |
|---:|---|---|
| 13 | IMPLEMENTATION CHECK | Obiettivi, architettura, moduli e configurazione. |
| 19 | IMPLEMENTATION CHECK | Dati, workload, flow map e transazioni. |
| 26 | IMPLEMENTATION CHECK | Execution, osservabilità, metriche e report. |
| 33 | TO EXPAND | Protocollo e setup sperimentale. |
| 39 | TO EXPAND | Scenari, KPI e quality gate. |
| 45 | EXPERIMENTAL RESULT MISSING | Validazione, risultati e linee guida. |

## 8. Copertura complessiva per nuova sezione

Le percentuali sono stime editoriali della funzione richiesta dall'indice, non
misure automatiche del numero di righe. “Adattamento supportato” comprende
fusioni, raccordi e delimitazioni ottenuti senza introdurre nuovi fatti.

| Sezione | Testo preesistente | Adattamento supportato | Da scrivere |
|---|---:|---:|---:|
| 1.1 | 80% | 20% | 0% |
| 1.2 | 70% | 20% | 10% |
| 1.3 | 70% | 15% | 15% |
| 1.4 | 30% | 70% | 0% |
| 1.5 | 65% | 25% | 10% |
| 1.6 | 15% | 85% | 0% |
| 2.1 | 82% | 10% | 8% |
| 2.2 | 90% | 8% | 2% |
| 2.3 | 20% | 35% | 45% |
| 2.4 | 10% | 35% | 55% |
| 2.5 | 50% | 30% | 20% |
| 2.6 | 30% | 35% | 35% |
| 3.1 | 20% | 75% | 5% |
| 3.2 | 25% | 60% | 15% |
| 3.3 | 30% | 65% | 5% |
| 3.4 | 15% | 50% | 35% |
| 3.5 | 10% | 45% | 45% |
| 3.6 | 5% | 40% | 55% |

La copertura del Capitolo 3 comprende soltanto implementazione verificata e
artefatti reali; non conteggia come risultati le configurazioni non eseguite.

## 9. P7 — Validazione LaTeX

### Controlli statici

- gerarchia dei tre capitoli migrati coerente con la regola di granularità;
- nessun label duplicato nei file attualmente inclusi e disponibili;
- 36 label attivi originari preservati; i soli label non migrati erano esempi
  commentati del template;
- nessuna chiave bibliografica attiva originaria persa; aggiunte quattro chiavi
  derivate da fonti primarie: DM 77/2022, DDR 11922/2026, capitolato tecnico
  SI.Ter e relazione tecnica SI.Ter;
- tre equazioni del vecchio Capitolo 3 preservate;
- nessuna figura, tabella o listing attivo era presente nei vecchi Capitoli 1–3;
- nella compilazione isolata non risultano riferimenti o citazioni indefiniti.

### Compilazione

Recipe:

```text
cd /home/alberto/unipd-thesis-template/thesis/files
latexmk -pdf -shell-escape thesis.tex
```

Un primo tentativo si era arrestato sugli include di capitoli del vecchio
template eliminati durante la pulizia effettuata dall'utente. Dopo
l'allineamento del root ai tre file correntemente disponibili, una precedente
compilazione interrotta aveva inoltre lasciato un file ausiliario troncato. È
stata quindi eseguita la pulizia necessaria con `latexmk -C thesis.tex`, senza
modificare i sorgenti.

La compilazione corrente dalla root reale con la recipe dichiarata ha concluso
con codice 0 e ha generato `thesis.pdf` di 93 pagine. Il log finale non contiene
errori LaTeX, citazioni indefinite, riferimenti indefiniti o label duplicati. La
compilazione temporanea dei soli Capitoli 1–3, usata in precedenza per isolare la
migrazione dagli include obsoleti, aveva prodotto lo stesso esito.

Restano warning non bloccanti: metadati PDF/A incompleti, destinazioni pagina
duplicate e righe overfull fuori dal Capitolo 1. La
profondità dell’indice è stata corretta a 2 affinché `\paragraph{}` risulti
effettivamente non numerato e non compaia nell’indice.

## 10. Rischi aperti e prossime attività minime

1. Aggiungere il nuovo Capitolo 4 al root quando verrà prodotto, mantenendo
   l'attuale struttura senza reintrodurre i capitoli del vecchio template.
2. Acquisire le fonti privacy/audit e le conferme aziendali richieste dai marker
   residui del Capitolo 1.
3. Approvare requisiti, casi d'uso, stakeholder, processi e matrici richiesti in
   2.3–2.5.
4. Definire prima dei risultati soglie, classi, campioni, ripetizioni e matrice
   ex ante di 2.6.
5. Completare le parti data-gated del Capitolo 3: ITI, ScrybaSign, ripetizioni,
   ambiente, soglie e layer middleware.
6. Eseguire gli esperimenti mancanti mantenendo separati mock, live e dati middleware;
   senza tali artefatti non scrivere risultati, capacità o linee guida
   quantitative.
7. Solo dopo il Capitolo 3 aggiornare il nuovo Capitolo 4 e chiudere la catena
   obiettivi → artefatti → criteri → KPI → risultati.
