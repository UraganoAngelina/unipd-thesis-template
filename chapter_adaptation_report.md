# Report di adattamento C1–C3

## 1. Esito

I prompt C1, C2 e C3 sono stati applicati ai tre capitoli inclusi dal root
document:

- `thesis/files/chapters/1_introduction.tex`;
- `thesis/files/chapters/2_domain.tex`;
- `thesis/files/chapters/3_soa.tex`.
- `thesis/files/preface/5_table_of_contents.tex`, limitatamente alla profondità
  di numerazione e indice necessaria a rendere `\paragraph{}` non numerato.

Il Capitolo 1 e il Capitolo 2 conservano la migrazione già tracciata
rispettivamente dai vecchi Capitoli 1–2 e dal vecchio Capitolo 3. Il Capitolo 3
è stato sviluppato a partire dai frammenti implementativi rinviati nella
matrice, verificandoli contro il codice corrente e contro gli artefatti di
esecuzione disponibili.

La revisione RDG ispezionata è
`f08fb53fd4ad11ef803642c0a066e9a6d9e2b327`. Il repository RDG è rimasto
read-only. Non sono stati esposti valori di configurazione riservati,
credenziali, token, certificati, endpoint privati o dati personali.

## 2. Struttura risultante

### Capitolo 1

| Destinazione logica | Titolo LaTeX risultante | Granularità |
|---|---|---|
| 1.1 General problem e problem statement | `From Information Continuity to the Research Question` | `\section` con paragrafi interni |
| 1.2 Territorial context e regulatory framework | `Territorial Healthcare and Regulatory Constraints` | `\section` con paragrafi interni |
| 1.3 Industrial context e ecosystem | `Industrial Setting and Interoperability Ecosystem` | `\section` con paragrafi interni |
| 1.4 Scope | `Scope and Limits of the Investigation` | `\section` con paragrafi interni |
| 1.5 Objectives, artefacts, contributions | `Objectives, Artefacts, and Contributions` | `\section` con paragrafi interni |
| 1.6 Structure of the thesis | `Organisation of the thesis` | `\paragraph`, perché inferiore a una pagina |

I titoli sono semanticamente equivalenti alla struttura target, ma sono stati
resi più selettivi per evitare ripetizioni lessicali tra livelli adiacenti.

### Capitolo 2

| Destinazione logica | Titolo LaTeX risultante | Granularità |
|---|---|---|
| 2.1 Solution space, architectures, standards | `Solution Space, Software Architectures, and Interoperability Standards` | `\section`; due blocchi lunghi come `\subsection` |
| 2.2 Performance theory, workload, implications | `Performance Theory, Workload Models, and Design Implications` | `\section`; quattro blocchi lunghi come `\subsection` |
| 2.3 Requirements and constraints | `Requirements and Project Constraints` | `\section`; blocchi interni come `\paragraph` |
| 2.4 Use cases and stakeholders | `Use Cases, Stakeholders, and Process Dependencies` | `\section`; blocchi interni come `\paragraph` |
| 2.5 Architecture and transactions | `Interoperability Architecture and RVE/ITI Transactions` | `\section`; blocchi interni come `\paragraph` |
| 2.6 Selection and criteria | `Comparative Approach Selection and Ex Ante Acceptance Criteria` | `\section`; blocchi interni come `\paragraph` |

La libreria mirata del Capitolo 2 ha fornito a 2.3–2.6 estensione e autonomia
sufficienti per sezioni numerate. I relativi blocchi interni restano paragrafi
non numerati; requisiti approvati, mapping completi e soglie mancanti sono
segnalati senza inventare contenuto.

### Capitolo 3

| Destinazione logica | Titolo LaTeX risultante | Granularità |
|---|---|---|
| 3.1 Framework objectives and architecture | `Technical Objectives and System Architecture` | `\section` |
| 3.2 Data, workload, transactions | `Synthetic Inputs and Executable Transactions` | `\section` |
| 3.3 Execution, observability, metrics | `Traffic Execution and Evidence Pipeline` | `\section` |
| 3.4 Evaluation methodology | `Evaluation Protocol and Experimental Design` | `\section` |
| 3.5 Scenarios, KPIs, data quality | `Executed Scenarios, KPIs, and Quality Controls` | `\section` |
| 3.6 Results, discussion, guidelines | `Evidence, Discussion, and Design Guidelines` | `\section` |

Le sei sezioni dispongono ora di estensione e autonomia sufficienti. I blocchi
interni restano `\paragraph{}` per non moltiplicare sottosezioni inferiori a
una pagina. `secnumdepth` e `tocdepth` sono stati riportati da 5 a 2: il
template forzava altrimenti numerazioni spurie come `3.1.0.0.1` e inseriva
anche i paragrafi nell’indice. Il titolo breve del capitolo è usato solo
nell’intestazione di pagina per evitare problemi tipografici.

## 3. Tracciabilità sorgente → destinazione

### C1

| Sorgenti inventariate | Destinazione primaria | Azione |
|---|---|---|
| C1-002, C1-010, C2-002–C2-003, C2-008–C2-012 | 1.1 | MERGE / ADAPT |
| C1-016–C1-020 | 1.1 e limiti in 1.4 | SPLIT / MERGE |
| C1-007–C1-009, C2-004–C2-006, C2-021–C2-025 | 1.2 | MERGE / SPLIT |
| C1-003–C1-006, C1-011–C1-015, C2-013–C2-020 | 1.3 | MERGE / ADAPT |
| C1-014, C1-019–C1-020 e limiti distribuiti | 1.4 | SPLIT / ADAPT |
| C1-021–C1-030 | 1.5 | MERGE / SPLIT |
| C1-031 | 1.6 | ADAPT; declassato a paragrafo |

La verifica corrente del codice ha chiuso i due marker
`IMPLEMENTATION CHECK` relativi al perimetro software e agli artefatti prodotti.
Il testo distingue ora flow implementati, flow coperti dagli artefatti e output
effettivamente generati.

### C2

| Sorgenti inventariate | Destinazione primaria | Azione |
|---|---|---|
| C3-002–C3-013 | 2.1 e sintesi transazionali in 2.5 | RETAIN / SPLIT / ADAPT |
| C3-014–C3-034 | 2.2 | RETAIN / MERGE / ADAPT |
| Principi da C1/C2 e C3-030–C3-034 | 2.3–2.6 | ADAPT; lacune marcate |

Le citazioni, le equazioni e i label del vecchio Capitolo 3 restano nella sede
teorica del Capitolo 2. Le descrizioni di classi, moduli, eventi e risultati
sono state mantenute fuori dal Capitolo 2 e collocate nel Capitolo 3.

### C3

| Sorgente o evidenza | Destinazione primaria | Azione |
|---|---|---|
| C1-024, C1-028; C3-030–C3-034 | 3.1 | ADAPT con verifica del dispatcher e dei confini di pipeline |
| C3-008, C3-024, C3-031 | 3.2 | SPLIT / ADAPT con verifica di Patient, flow map e dipendenze |
| C3-031–C3-033 | 3.3 | ADAPT con verifica di scheduler, eventi, collector e metric engine |
| C3-017, C3-021–C3-024, C3-032–C3-034 | 3.4–3.5 | ADAPT; separazione tra teoria, variabili operative e dati mancanti |
| `main.py`, generatori, orchestrator, executor, collector e metric engine | 3.1–3.5 | Evidenza implementativa corrente |
| Configurazioni risolte e run directory archiviate | 3.5–3.6 | Evidenza di esecuzione, distinta per mock/live |
| Test correnti dei flow e di ScrybaSign | 3.2 e 3.6 | Validazione funzionale, non risultato prestazionale |

Nessuna unità del vecchio inventario è stata cancellata silenziosamente. I
commenti di esempio del template e i soli page break restano esclusi come già
motivato in `migration_matrix.md`.

## 4. Copertura editoriale

Le percentuali sono stime editoriali e distinguono testo preesistente,
adattamento supportato e contenuto ancora da produrre. L’adattamento supportato
del Capitolo 3 comprende verifiche sul codice e su artefatti reali, non
invenzione di risultati.

| Sezione | Testo preesistente | Adattamento supportato | Ancora da scrivere |
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

Principali motivi della copertura residua:

- riferimenti normativi e dettagli industriali non ancora forniti;
- requisiti, use case e stakeholder non ricostruibili dai vecchi Capitoli 1–3;
- soglie e matrice di accettazione ex ante non approvate;
- assenza di una campagna live ripetuta e documentata;
- assenza di middleware log correlabili;
- assenza di run archiviati per ITI-18, ITI-43 e
  `FLOW_SCRYBASIGN_SIGN`.

## 5. Marker residui

Sono presenti 36 marker:

| Capitolo | DATA MISSING | SOURCE NEEDED | TO EXPAND | EXPERIMENTAL RESULT MISSING | Totale |
|---|---:|---:|---:|---:|---:|
| 1 | 7 | 1 | 3 | 0 | 11 |
| 2 | 4 | 2 | 9 | 1 | 16 |
| 3 | 3 | 1 | 1 | 4 | 9 |

### Gap principali del Capitolo 3

- fonte primaria e mapping approvato per RVE-57;
- run mock e live autorizzato del flow ScrybaSign;
- protocollo finale di warm-up, ripetizioni, popolazioni minime e ambiente;
- run ITI, ramp, stress e mixed-flow;
- log middleware reale, boundary e copertura del join;
- soglie e matrice ex ante;
- campagna live ripetuta e discussione finale contro i criteri approvati.

I marker dei Capitoli 1 e 2 sono elencati puntualmente nel
`migration_report.md`; i relativi testi non sono stati completati per
intuizione.

## 6. Evidenze e Knowledge Base consultate

### Code KB

È stata interrogata la KB Graphify in
`/home/alberto/Desktop/Request-Dataset-Generator/graphify-out/` per ricostruire
la pipeline corrente e localizzare i nodi implementativi. La query è stata
seguita da verifica diretta del codice, che prevale sui riassunti.

File verificati:

- `main.py`;
- `fhir_patient_generator.py`;
- `request_dataset_generator.py`;
- `timeline_generator.py`;
- `traffic_exec_engine.py`;
- `log_collector.py`;
- `metric_engine.py`;
- `rve_transactions/flow_orchestrator.py`;
- moduli RVE, ITI e ScrybaSign richiamati dalla flow map;
- `tests/test_core.py`;
- configurazioni scenario e `config.resolved.json` delle run archiviate.

L’uso della skill Graphify ha orientato la verifica sulle dipendenze tra i nodi
della pipeline; ogni affermazione trasferita nel capitolo è stata poi
controllata sul sorgente o sull’artefatto primario.

### Documentation KB

La Documentation KB è stata usata nell’inventario e nelle revisioni mirate per
classificare IHE, FHIR, APMS, SAML/JWT e transazioni regionali, localizzare DM
77/2022 e il decreto regionale SI.Ter e distinguere i processi documentati
dalle catene tecniche soltanto plausibili. Le formulazioni sono state poi
controllate sui documenti primari, incluse le specifiche RVE/ITI, il capitolato
SI.Ter e la relazione tecnica; dove manca una fonte primaria, una baseline
approvata o una conferma di divulgabilità, il marker è rimasto.

### Artefatti di esecuzione

Sono state ispezionate sei directory sotto `runs/`, ognuna con configurazione
risolta e dataset normalizzato:

- cinque run in modalità mock;
- una run live di smoke test con tre flow di patient query;
- zero eventi middleware in tutte le run;
- nessuna occorrenza ITI o ScrybaSign.

I risultati numerici riportati nel Capitolo 3 provengono esclusivamente dai
rispettivi `metrics_report.json`. I valori mock sono qualificati come misura
del framework e delle risposte sintetiche, mai come misura di produzione.

## 7. Controlli narrativi

- Il Capitolo 1 passa dal problema generale alla domanda di ricerca, poi
  delimita scope, obiettivi e artefatti senza introdurre dettagli di classe.
- Il Capitolo 2 mantiene teoria, alternative e criteri metodologici separati
  dalla descrizione interna del framework.
- Il Capitolo 2 distingue requisiti candidati, requisiti approvati, presenza nel
  codice e validazione sperimentale.
- Il Capitolo 3 rende operativi i criteri del Capitolo 2 e distingue
  implementazione, validazione funzionale ed evidenza sperimentale.
- I concetti di latenza, throughput, percentili, workload e grey-box hanno sede
  primaria nel Capitolo 2; il Capitolo 3 li richiama solo per definirne
  l’operazionalizzazione.
- Il confronto direct/middleware è chiamato “apparent overhead” e non riceve
  interpretazione causale.
- Mock e live non sono uniti nella stessa popolazione.
- La piccola run live è usata solo come evidenza funzionale limitata.
- ScrybaSign è descritto come flow implementato e testato a livello di
  contratto, non come scenario sperimentale eseguito.
- Le sei sezioni del Capitolo 3 hanno estensione autonoma; i blocchi minori sono
  `\paragraph{}`.
- Le sei sezioni del Capitolo 2 hanno ora estensione autonoma; i blocchi brevi
  restano `\paragraph{}` e i dettagli ITI/RVE hanno sede primaria in 2.5.

## 8. Validazione

### Test RDG

Comando eseguito in modalità read-only:

`PYTHONDONTWRITEBYTECODE=1 python3 -m unittest -q tests.test_core`

Esito: 29 test eseguiti, 28 senza errori; un errore ambientale nella generazione
dei grafici per assenza del pacchetto opzionale `matplotlib`. Non sono state
installate dipendenze e il repository RDG non è stato modificato.

### LaTeX

Recipe:

`latexmk -pdf -shell-escape thesis.tex`

Esito: compilazione riuscita e PDF di 93 pagine generato. Non risultano errori
LaTeX bloccanti, citazioni o riferimenti indefiniti. Restano warning tipografici
nelle tabelle e warning PDF preesistenti o non connessi alla semantica della
migrazione; il controllo finale viene registrato anche in
`migration_report.md`.
