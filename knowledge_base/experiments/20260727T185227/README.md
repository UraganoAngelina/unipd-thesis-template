# Dataset sperimentale sanitizzato 20260727T185227

## Identità e perimetro

- Identificativo sperimentale richiesto: `20260727T185227`.
- Identificativo interno del manifest sorgente: `thesis_live_30r`.
- Modalità dichiarata dal manifest: `live`.
- Protocollo pianificato: 10 scenari, 30 repliche per scenario, 300 run.
- Corpus osservato: 145 run avviate e 74 run complete dotate di `execution_log.jsonl`.
- Scansione totale: 1842 file, 8283030295 byte.
- Eventi JSONL analizzati: 757517.
- Righe CSV validate: 877.

L'identificativo della cartella è quello fornito dall'operatore; il diverso
`batch_id` interno del manifest è conservato in `provenance.json` per evitare
una falsa equivalenza tra i due identificativi.

## Sanitizzazione

La derivazione usa una whitelist composta esclusivamente da scenario,
transazione, codice HTTP, esito booleano, indicatore di fault injection,
latenza e contatori operativi. I JSONL grezzi, le configurazioni, le timeline,
i dataset, i body e i messaggi di errore non sono stati copiati nella KB.

Alias stabili riservati per eventuali riferimenti trasversali:

- `KNOWN_LAB_PATIENT`;
- `IAP_LAB`;
- `RVE121_CONTEXT_SERVICE`;
- `MIDDLEWARE_TOKEN_ENDPOINT`.

Nessun valore originale associato agli alias è presente nel dataset.

## Contenuto

- `scenario_metrics.csv`: metriche aggregate sulle sole 74 run complete.
- `transaction_outcomes.csv`: conteggi per scenario, transazione, codice,
  esito e presenza di fault.
- `experiment_summary.md`: conclusioni tracciabili e limiti inferenziali.
- `error_taxonomy.md`: tassonomia derivata senza messaggi di errore grezzi.
- `provenance.json`: commit osservato, hash e audit della scansione.
- `figures/`: tutti i 578 PNG prodotti dalle 74 run complete.

## Definizioni operative

- `total_requests`: numero di eventi `response_received`.
- Percentili di latenza: percentili esatti sulla popolazione pooled degli
  eventi `response_received` delle run complete dello scenario.
- `request_throughput_per_active_second`: richieste divise per la somma delle
  finestre attive delle singole run; non include i tempi tra run.
- `max_observed_concurrency`: massimo osservato tra flussi e step attivi negli
  eventi `request_sent`.
- `flow_success_rate_percent`: quota di eventi `flow_completed` con successo.
- `status_code=0`: nessuna risposta HTTP disponibile; non equivale a HTTP 000.

## Inventario figure

| Scenario | Run con figure | PNG |
|---|---:|---:|
| `baseline` | 5 | 40 |
| `baseline_constant` | 5 | 40 |
| `burst` | 5 | 45 |
| `direct_vs_middleware` | 14 | 112 |
| `error_injection` | 6 | 48 |
| `flow_type_comparison_direct` | 6 | 42 |
| `flow_type_comparison_middleware` | 15 | 105 |
| `live_smoke_small` | 8 | 61 |
| `load_ramp` | 5 | 40 |
| `stress_extreme` | 5 | 45 |

I PNG sono stati validati integralmente. I soli metadati presenti nelle
sorgenti sono `Software` e `dpi`; non sono presenti identificativi o endpoint
nei metadati. Le figure sono evidenza visuale, mentre i conteggi tabellari
derivano dai JSONL.

## Limiti

Il protocollo pianificato non è stato completato: 74 run su 300. Le numerosità
sono inoltre sbilanciate tra scenari (da 5 a 15 run complete). Di conseguenza
il dataset documenta gli esiti osservati, ma non autorizza
confronti prestazionali conclusivi tra scenari o inferenze di capacity
planning. Nel corpus scansionato non compare alcun esito RVE-121 HTTP 400:
la transizione causale da 400 a 200 non è quindi dimostrabile con queste sole
fonti.
