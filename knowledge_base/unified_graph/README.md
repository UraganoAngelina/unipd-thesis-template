# Ponti del grafo unificato

Il grafo unificato conserva i namespace dei tre grafi sorgente. I seguenti
ponti collegano entità omonime della transazione RVE-121 e sono marcati
`INFERRED`, perché derivano dall'allineamento semantico tra corpus distinti:

- il modulo `rve_transactions/rve_121.py` implementa la transazione
  rappresentata dal concetto documentale `RVE-121 GetAccessToken`;
- la conclusione sperimentale `E-RVE121-001` riguarda la stessa transazione
  `RVE-121 GetAccessToken`;
- la conclusione sperimentale è quindi collegabile al modulo di
  implementazione, senza attribuire causalità a una modifica non dimostrata.

Il documento *Scryba Sign 3.x Developer's Guide V16* introduce inoltre quattro
ponti `INFERRED` con confidenza 0,95, verificati contro l'implementazione RDG:

- `rve_transactions/scrybasign_get_user_info.py` implementa il metodo
  documentato `GetUserInfo4`;
- `rve_transactions/scrybasign_sign_one_doc.py` implementa il metodo
  documentato `SignOneDoc`;
- `rve_transactions/scrybasign_common.py` realizza le utilità comuni della
  superficie SOAP/WSDL;
- `resolve_auth_header()` realizza l'header Basic Authentication richiesto dal
  contratto HTTPS documentato.

Fonti dei nodi: grafo del codice RDG, grafo documentale, *Scryba Sign 3.x
Developer's Guide V16* e
`knowledge_base/experiments/20260727T185227/experiment_summary.md`.
