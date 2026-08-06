# Esperimento 20260727T185227

## E-PROTOCOL-001

- Transazione: tutte le transazioni della batteria.
- Osservazione: il manifest pianifica 300 run, mentre sono disponibili 145 run avviate e 74 run complete.
- Classificazione: protocollo live incompleto e campione sbilanciato tra scenari.
- Modifica: nessuna; questa voce registra il perimetro realmente osservato.
- Risultato: 158449 flussi completati e 299534 risposte registrate nelle run complete.
- Deduzione: i risultati descrivono il campione osservato ma non supportano confronti conclusivi tra tutti gli scenari pianificati.
- Confidenza: alta per conteggi e completezza dei file; bassa per generalizzazioni oltre il campione.
- Evidenza: `scenario_metrics.csv`, `provenance.json`.
- Stato: corrente.

## E-RVE121-001

- Transazione: RVE-121.
- Osservazione: sono presenti 19091 esiti HTTP 200 non associati a fault, 857 esiti HTTP 504 con fault iniettato e 1 failure senza risposta HTTP.
- Classificazione: successo applicativo prevalente nel traffico non sottoposto a fault; i 504 sono evidenza di fault injection.
- Modifica: il manifest registra una riparazione runtime delle sezioni di configurazione, ma non consente di attribuire il risultato a uno specifico campo senza evidenza pre/post dedicata.
- Risultato: nessun HTTP 400 RVE-121 compare nel corpus `thesis_live_30r`.
- Deduzione: la batteria dimostra l'esecuzione di RVE-121 con HTTP 200, ma non dimostra la trasformazione causale da HTTP 400 a HTTP 200.
- Confidenza: alta sui conteggi; non determinabile sulla causalità della modifica.
- Evidenza: `transaction_outcomes.csv`, `provenance.json`.
- Stato: corrente; `[DATO MANCANTE]` per la catena pre-correzione HTTP 400 → modifica → verifica HTTP 200.

## E-RVE55-001

- Transazione: RVE-55.
- Osservazione: 16607 risposte non sottoposte a fault terminano con HTTP 422.
- Classificazione: errore di validazione semantica della richiesta.
- Modifica: nessuna modifica correttiva verificabile nel corpus.
- Risultato: l'HTTP 422 è distinto dagli errori di trasporto e dai fault iniettati.
- Deduzione: il codice HTTP localizza il rifiuto a livello applicativo, ma non identifica da solo il campo o il vincolo responsabile.
- Confidenza: alta sulla classificazione HTTP; bassa su una causa di payload non osservabile nel dataset sanitizzato.
- Evidenza: `transaction_outcomes.csv`, `error_taxonomy.md`.
- Stato: aperta; richiede evidenza applicativa sanitizzata per una diagnosi causale.

## E-RVETOKEN-001

- Transazione: RVE-TOKEN.
- Osservazione: 35638 risposte HTTP 200 sono marcate come failure dal framework.
- Classificazione: fallimento di estrazione o validazione di un output obbligatorio dopo una risposta HTTP riuscita.
- Modifica: nessuna modifica correttiva verificata.
- Risultato: il codice HTTP non coincide sempre con l'esito applicativo dello step.
- Deduzione: le analisi devono mantenere separati `status_code` e `outcome`.
- Confidenza: alta; la regola è verificata nell'implementazione corrente del logger/esecutore.
- Evidenza: `transaction_outcomes.csv`, `error_taxonomy.md`, commit sorgente in `provenance.json`.
- Stato: corrente.

## E-FAULT-001

- Transazione: transazioni soggette a fault injection.
- Osservazione: 12808 richieste sono marcate con fault iniettato; 4265 risultano failure e le restanti rappresentano fault non bloccanti, come spike di latenza.
- Classificazione: evidenza sintetica controllata, distinta dagli errori live non iniettati.
- Modifica: applicazione deterministica delle regole di fault injection configurate.
- Risultato: gli outcome con `fault_injected=true` sono separabili nel dataset.
- Deduzione: i fault iniettati non devono essere sommati agli errori spontanei quando si stima l'affidabilità live.
- Confidenza: alta.
- Evidenza: `transaction_outcomes.csv`, `scenario_metrics.csv`.
- Stato: corrente.

## E-MIDDLEWARE-001

- Transazione: flussi degli scenari `direct_vs_middleware` e `flow_type_comparison_middleware`.
- Osservazione: entrambi gli scenari hanno un tasso di errore richiesta del 100% nelle run complete disponibili.
- Classificazione: campione non valido per un confronto prestazionale tra percorsi riusciti.
- Modifica: nessuna correzione verificata nel corpus.
- Risultato: rispettivamente 1590 e 1687 richieste osservate senza successi.
- Deduzione: le latenze di questi scenari descrivono failure path e non possono essere interpretate come overhead nominale del middleware.
- Confidenza: alta sul limite metodologico.
- Evidenza: `scenario_metrics.csv`.
- Stato: aperta; richiede run corrette con richieste riuscite su entrambi i percorsi.
