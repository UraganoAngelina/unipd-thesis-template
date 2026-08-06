# Tassonomia degli errori — 20260727T185227

La tassonomia deriva esclusivamente da `status_code`, `outcome` e da una
classificazione in memoria del messaggio grezzo. Il testo del messaggio non è
mai scritto nella KB.

| Categoria | Status code | Conteggio | Transazioni | Interpretazione |
|---|---|---:|---|---|
| `output_extraction_failure` | 200 | 35638 | `RVE-TOKEN` | HTTP completato ma output obbligatorio non validato o non estratto; l'esito applicativo resta failure. |
| `transport_timeout` | 0 | 17337 | `ITI-18`, `RVE-121`, `SCRYBASIGN-SIGN-ONE-DOC` | Assenza di risposta HTTP per timeout di trasporto. |
| `semantic_validation_failure` | 422 | 16607 | `RVE-55` | Richiesta ricevuta ma respinta con HTTP 422. |
| `dependency_resolution_failure` | 0 | 3179 | `RVE-100`, `RVE-54`, `RVE-55`, `RVE-57` | Dipendenza runtime non risolta prima dell'invio; nessun codice HTTP disponibile. |
| `service_unavailable` | 503 | 2640 | `ITI-18`, `RVE-54` | Servizio temporaneamente non disponibile, HTTP 503. |
| `remote_internal_error` | 500 | 1267 | `ITI-18`, `RVE-130`, `RVE-55` | Errore interno restituito dal servizio remoto, HTTP 500. |
| `unclassified_transport_failure` | 0 | 1164 | `RVE-1.b` | Errore di trasporto con status_code 0 non ulteriormente classificabile senza conservare il messaggio grezzo. |
| `gateway_timeout` | 504 | 857 | `RVE-121` | Timeout rappresentato come HTTP 504. |
| `upstream_gateway_error` | 502 | 795 | `SCRYBASIGN-SIGN-ONE-DOC` | Errore di gateway/upstream, HTTP 502. |
| `transport_connection_failure` | 0 | 143 | `ITI-43` | Connessione di trasporto non stabilita. |
| `http_4xx_failure` | 408 | 1 | `ITI-18` | Altro errore HTTP 4xx. |

## Regole di lettura

- `status_code=0` indica assenza di risposta HTTP.
- Un HTTP 200 può avere `outcome=failure` quando un output obbligatorio non è
  stato estratto o validato.
- Gli errori con `fault_injected=true` restano identificabili in
  `transaction_outcomes.csv` e non vanno confusi con errori live spontanei.
- Le categorie non ricostruiscono payload, endpoint o messaggi sensibili.
