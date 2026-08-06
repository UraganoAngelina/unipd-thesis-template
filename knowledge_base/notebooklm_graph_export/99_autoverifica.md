# Autoverifica della conversione Graphify

## Metadati

- Data di verifica: 2026-07-31.
- Esito complessivo: **SUPERATO**.
- Nodi fisici attesi e verificati: 1305; nodi canonici: 664.
- Archi fisici attesi: 2275; verbalizzazioni direzionali verificate: 4550.
- Iperarchi fisici attesi e verificati: 10.
- Proprietà verificate: 55325 occorrenze di proprietà strutturali.

## Checklist obbligatoria

- [x] Ogni nodo dei JSON di input compare in almeno un documento.
- [x] Ogni arco dei JSON di input è tradotto presso la sorgente e presso il destinatario.
- [x] Ogni iperarco annidato in `graph.hyperedges` è tradotto in prosa.
- [x] Ogni proprietà top-level, di nodo, di arco e di iperarco è stata elaborata.
- [x] Nessun alias con forma `MAIUSCOLO_CON_UNDERSCORE` è stato alterato o risolto.
- [x] Nessuna relazione è stata aggiunta senza un arco o iperarco sorgente; le semantiche non mappate ricevono `[DA VERIFICARE: ...]`.
- [x] La terminologia canonica dei nodi è univoca e riutilizzata in tutti i documenti.

## Dettaglio dei controlli di proprietà

- Proprietà graph: copertura completa su 22 occorrenze attese.
- Proprietà node: copertura completa su 12659 occorrenze attese.
- Proprietà edge: copertura completa su 42574 occorrenze attese.
- Proprietà hyperedge: copertura completa su 70 occorrenze attese.

## Controllo degli alias

Il controllo ha individuato 5 token distinti con forma `MAIUSCOLO_CON_UNDERSCORE` negli input. Tutti i token sono presenti senza sostituzione nei documenti generati.

## Limiti dichiarati

L'autoverifica dimostra la copertura strutturale dei JSON, non la completezza delle fonti originarie da cui Graphify ha estratto il grafo. In particolare, il grafo sperimentale non contiene sette nodi di esperimento né proprietà numeriche sufficienti per ricostruire integralmente i sette esperimenti o un confronto quantitativo dell'Esperimento 5; tali contenuti non vengono inventati. [DA VERIFICARE: rigenerare o arricchire il grafo se questi dettagli devono diventare sorgenti NotebookLM].
