# Correzione del successo dei flussi middleware

## E-FLOW-SUCCESS-001

- Scenario: `flow_type_comparison_middleware`.
- Popolazione pooled: 1.687 eventi `flow_completed` nelle 15 run complete.
- Fonte di verita: correzione validata dall'operatore il 2026-09-01.
- Risultato: 263 flussi raggiungono uno stato terminale di successo e 1.424
  flussi non lo raggiungono.
- Calcolo: `263 / 1687 * 100 = 15,589804386...%`.
- Valore pubblicabile: 15,59% con arrotondamento a due cifre decimali.
- Vincolo di integrita: 15,63% non e producibile da un numero intero di
  successi sulla popolazione di 1.687 flussi; i due conteggi interi adiacenti
  producono 15,59% (263 successi) e 15,65% (264 successi).
- Ambito della correzione: il dato sostituisce ogni precedente percentuale di
  successo dei flussi attribuita a questo scenario. Non modifica i conteggi o
  gli esiti a livello di richiesta, che costituiscono una popolazione distinta.

