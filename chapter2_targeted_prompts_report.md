# Report di esecuzione — libreria mirata del Capitolo 2

## 1. Esito

Sono stati eseguiti tutti i prompt della libreria 2.1–2.6, inclusi i 22 prompt
figli. Il risultato è incorporato in
`thesis/files/chapters/2_domain.tex`.

La struttura risultante contiene le sei sezioni previste dall'indice
definitivo. I blocchi dotati di autonomia e di estensione superiore a una
pagina sono `\subsection`; gli elementi più brevi sono `\paragraph` non
numerati. I titoli interni sono stati resi complementari a quelli delle sezioni
madri per evitare ripetizioni lessicali.

La migrazione non presenta come requisiti approvati le sole proprietà ricavate
dalla teoria, non trasforma la presenza di codice in validazione, non considera
un'esecuzione mock come misura di produzione e non assegna soglie prestazionali
in assenza di una fonte.

## 2. Fonti candidate individuate prima dell'adattamento

| Inventario | Vecchio file e righe | Vecchia collocazione | Destinazione | Classificazione |
|---|---|---|---|---|
| C3-001 | vecchio Capitolo 3, 1–6 | apertura | Capitolo 2 e raccordo 2.1–2.2 | ADAPT |
| C3-002–C3-006 | vecchio Capitolo 3, 8–75 | architetture di integrazione | 2.1, contratti/mediazione/orchestrazione | RETAIN / MERGE / ADAPT |
| C3-007–C3-013 | vecchio Capitolo 3, 77–166 | standard e protocolli sanitari | 2.1 e dettagli concreti in 2.5 | SPLIT / RETAIN / ADAPT |
| C3-014–C3-019 | vecchio Capitolo 3, 168–248 | valutazione dei sistemi distribuiti | 2.2, confini di misura | RETAIN / ADAPT |
| C3-020–C3-024 | vecchio Capitolo 3, 250–317 | modelli di workload | 2.2, traffico stocastico | MERGE / SPLIT / ADAPT |
| C3-025–C3-029 | vecchio Capitolo 3, 319–374 | letteratura latenza/throughput/scheduling | 2.2, sintesi della letteratura | RETAIN / ADAPT |
| C3-030–C3-034 | vecchio Capitolo 3, 376–443 | implicazioni progettuali | 2.2, 2.3 e 2.6 | SPLIT / MERGE / ADAPT |
| C1-018, C1-020, C1-029 | vecchio Capitolo 1, 108–119 e 159–162 | flow multi-step e limiti cross-layer | 2.2, 2.3 e 2.6 | SPLIT / ADAPT |
| C2-007, C2-022–C2-025 | vecchio Capitolo 2, 74–78 e 133–148 | processi territoriali e vincoli | 2.3–2.4 | SPLIT / ADAPT / VERIFY |
| C2-011, C2-015, C2-017–C2-019 | vecchio Capitolo 2, 91–121 | orchestrazione ed ecosistema | 2.1, 2.4 e 2.5 | ADAPT / CROSS-REFERENCE |

Per le parti non contenute nei vecchi capitoli sono state consultate, senza
sostituire le lacune con inferenze:

- specifiche Anagrafe Zero v2.6;
- specifiche GDL-O Sicurezza v2.14;
- specifiche della chiamata di contesto RVE v1.3;
- IHE IUA e IHE XDS.b;
- Affinity Domain Italia v2.6.3 e specifiche XValue;
- capitolato tecnico SI.Ter, in particolare pp. 32–36;
- relazione tecnica SI.Ter, limitatamente alle parti funzionali dei percorsi;
- codice corrente RDG per la sola distinzione tra transazioni analizzate e
  transazioni presenti nel generatore.

## 3. Verifica della matrice e tracciabilità sorgente → destinazione

| Sorgente | Sede primaria risultante | Azione | Apparati preservati |
|---|---|---|---|
| C3-002–C3-006 | 2.1, `Contracts, Mediation, and Orchestration` | MERGE / RETAIN | label SOA/ROA, gateway, flow sincroni e decoupling; citazioni OASIS/FHIR/RVE/IHE |
| C3-007–C3-010, C3-012 | 2.1, `FHIR, IHE, and Security Profiles` | MERGE / RETAIN | label FHIR, IUA, XDS.b, serializzazioni; citazioni originarie |
| C3-008, C3-011, C3-013 | 2.1 panoramica; 2.5 sede transazionale | SPLIT | label ITI spostata in 2.5; rinvii a RVE-1.b, RVE-121/130 e registry |
| C3-014–C3-019 | 2.2.1 logica | RETAIN / ADAPT | equazione del throughput e cinque label |
| C3-020–C3-024 | 2.2.2 logica | RETAIN / SPLIT | equazioni di Poisson e intensità, quattro label, marker di calibrazione |
| C3-025–C3-029 | 2.2.3 logica | RETAIN | tre chiavi bibliografiche e quattro label |
| C3-030–C3-034 | 2.2.4 logica e raccordi 2.3/2.6 | SPLIT / ADAPT | label delle quattro implicazioni e marker di rappresentatività |
| C2-022–C2-025 e principi C3-030–C3-034 | 2.3 | ADAPT | vincoli preservati; requisiti lasciati candidati |
| C2-007 e documenti SI.Ter | 2.4 | ADAPT / DEFER | fonti di progetto aggiunte; catene non validate marcate |
| C3-008, C3-009–C3-013 e codice corrente | 2.5 | SPLIT / ADAPT | matrice transazioni–codice–KPI; nessun risultato anticipato |
| C3-016, C3-031–C3-034 e C1-029 | 2.6 | MERGE / ADAPT | confronto qualitativo e schema ex ante; soglie mantenute mancanti |

Nessuna unità inventariata è stata eliminata silenziosamente. I dettagli
implementativi esclusi dal Capitolo 2 conservano la destinazione differita nel
Capitolo 3 definita da `migration_matrix.md`.

## 4. Esito di ogni prompt

| Prompt | Stato | Esito principale |
|---|---|---|
| 2.1 | Parziale | Sezione completa sul piano architetturale; confronto replay ancora privo di fonte. |
| 2.1.1 | Parziale | Tre alternative sostenute; replay e matrice comparativa marcati. |
| 2.1.2 | Completo | SOA/ROA, gateway, orchestrazione, sincronia, statelessness e disaccoppiamento preservati. |
| 2.1.3 | Completo | Standard descritti una sola volta; semantica transazionale concreta spostata in 2.5. |
| 2.2 | Completo con limiti | Percorso teoria → workload → letteratura → implicazioni preservato. |
| 2.2.1 | Completo | Confini di latenza, throughput, errori, concorrenza, code e percentili distinti. |
| 2.2.2 | Parziale | Modelli completi; calibrazione su traffico RVE operativo assente. |
| 2.2.3 | Completo | LSW/TIV/TU e quantili mantenuti entro il perimetro degli studi originari. |
| 2.2.4 | Parziale | Implicazioni complete; realismo temporale non dimostrato senza dati operativi. |
| 2.3 | Parziale | Capability candidate e vincoli tracciati, senza simulare una baseline approvata. |
| 2.3.1 | Parziale | Cinque gruppi funzionali con evidenza e confine aperto. |
| 2.3.2 | Parziale | Attributi di qualità supportati; clausole misurabili ancora da approvare. |
| 2.3.3 | Parziale | Vincoli tecnici/metodologici presenti; baseline organizzativa incompleta. |
| 2.4 | Parziale | Due percorsi distinti; solo gli step realmente documentati sono narrati. |
| 2.4.1 | Parziale | APMS, ADT, consultazione FSE, valutazione e invio COT supportati; RVE/ITI chain aperta. |
| 2.4.2 | Parziale | Origine territoriale/MMG e COT supportati; prescrizione/context/registry/ADI chain aperta. |
| 2.4.3 | Parziale | Livelli di stakeholder distinti; matrice RACI mancante. |
| 2.4.4 | Parziale | Dipendenze tecniche definite; mapping completo processo–transazioni mancante. |
| 2.5 | Parziale | Architettura analitica e famiglie transazionali complete; deployment e validazione aperti. |
| 2.5.1 | Parziale | Vista a livelli supportata; ownership e trust boundary finali mancanti. |
| 2.5.2 | Completo | RVE-1.b separata da APMS e dalle autorizzazioni downstream. |
| 2.5.3 | Parziale | RVE-54/55/57 documentate e confrontate con il codice; ruolo nei casi aperto. |
| 2.5.4 | Completo | Dipendenza RVE-121 → RVE-130 preservata senza valori sensibili. |
| 2.5.5 | Completo | ITI-41/18/43 e ruoli Registry/Repository distinti; copertura codice qualificata. |
| 2.5.6 | Parziale | Matrice prodotta; mock/live, conformance e case mapping ancora da dimostrare. |
| 2.6 | Parziale | Selezione motivata e criteri ex ante separati dalle soglie. |
| 2.6.1 | Parziale | Alternative confrontate; replay dichiarato non valutabile. |
| 2.6.2 | Parziale | Famiglie di criteri e campi obbligatori definiti; soglie e classi mancanti. |

## 5. Modifiche editoriali

- Rinominati i sei titoli di sezione secondo l'indice definitivo.
- Declassato `Definition of the Solution Space` a `Evaluation alternatives`
  perché inferiore a una pagina e lessicalmente ridondante con il titolo madre.
- Rinominati i titoli interni in forma complementare: ad esempio
  `Contracts, Mediation, and Orchestration`, `Stochastic Traffic
  Representations` e `Methodological Consequences`.
- Spostate le descrizioni ITI-41/18/43 da 2.1 a 2.5; in 2.1 resta un rinvio.
- Spostate le semantiche regionali di RVE-54/55 e RVE-1.b/121/130 nella sezione
  transazionale, mantenendo in 2.1 la teoria generale.
- Separate capacità candidate, requisiti approvati e copertura implementativa.
- Aggiunte tre tabelle: capability candidate, copertura transazionale e criteri
  ex ante, oltre al confronto qualitativo degli approcci.
- Conservate le tre equazioni e tutte le label/citazioni del vecchio Capitolo 3.

## 6. Copertura per sezione

Le percentuali sono stime editoriali della funzione richiesta, non conteggi
automatici delle righe.

| Sezione | Testo preesistente | Adattamento supportato | Ancora da scrivere |
|---|---:|---:|---:|
| 2.1 | 82% | 10% | 8% |
| 2.2 | 90% | 8% | 2% |
| 2.3 | 20% | 35% | 45% |
| 2.4 | 10% | 35% | 55% |
| 2.5 | 50% | 30% | 20% |
| 2.6 | 30% | 35% | 35% |

## 7. Marker residui

Restano 16 marker: 9 `TO EXPAND`, 4 `DATA MISSING`, 2 `SOURCE NEEDED` e
1 `EXPERIMENTAL RESULT MISSING`.

| Linea corrente | Tipo | Gap |
|---:|---|---|
| 23 | TO EXPAND | Fonte replay e criteri completi del solution space. |
| 359 | DATA MISSING | Distribuzione osservata degli arrivi RVE. |
| 394 | DATA MISSING | Calibrazione dei burst. |
| 556 | DATA MISSING | Calibrazione di mix e profili temporali. |
| 602 | TO EXPAND | Baseline funzionale approvata e numerata. |
| 623 | TO EXPAND | Requisiti non funzionali testabili. |
| 643 | SOURCE NEEDED | Baseline di progetto su accesso, deployment, responsabilità e disclosure. |
| 678 | TO EXPAND | Catena approvata della dimissione protetta. |
| 699 | TO EXPAND | Catena approvata dell'ammissione protetta. |
| 719 | TO EXPAND | Matrice delle responsabilità. |
| 737 | TO EXPAND | Diagrammi e dipendenze processo–transazioni. |
| 765 | TO EXPAND | Deployment, ownership e trust boundary finali. |
| 801 | TO EXPAND | Ruolo di RVE-54/55/57 nei due casi d'uso. |
| 886 | EXPERIMENTAL RESULT MISSING | Evidenza mock/live e conformance per transazione. |
| 937 | SOURCE NEEDED | Fonte replay o decision record. |
| 979 | DATA MISSING | Soglie, classi, campioni, ripetizioni e matrice ex ante. |

## 8. Controlli narrativi e tecnici

- Il Capitolo 1 introduce contesto e problema; il Capitolo 2 non li ripete.
- Il confronto delle alternative precede la descrizione dell'approccio scelto.
- Teoria prestazionale e criteri di accettazione restano distinti.
- Stato dell'arte, presenza nel codice e validazione sperimentale sono tre stati
  separati.
- Nessun risultato sperimentale è anticipato.
- Le misure framework e middleware non sono correlate causalmente senza chiavi,
  clock e popolazioni compatibili.
- ITI-41 è analiticamente rilevante ma non attribuita al generatore corrente.
- RVE-57 è presente nel percorso middleware del codice, ma non assegnata per
  intuizione ai due casi d'uso.
- ScrybaSign è segnalato come flow implementativo esterno alla mappa primaria
  dei due processi e rinviato al Capitolo 3.

## 9. Knowledge Base e fonti consultate

La Documentation KB è stata interrogata con i termini del suo vocabolario
relativi a autenticazione, FHIR, IUA, XDS, SAML/JWT, RVE/ITI e patient
registry. La Code KB è stata interrogata su flow, workload, mock/live, metriche,
log, Poisson, burst e transazioni. Le indicazioni dei grafi sono state
controllate sui documenti estratti e sul codice primario.

È stato rilevato un conflitto tra il docstring iniziale di
`flow_orchestrator.py`, che non elenca tutti i flow, e la costante `FLOW_TYPES`
con `_FLOW_MODULES`. È prevalsa la mappa eseguibile: sette famiglie, incluse
ITI-18, ITI-43 e ScrybaSign. Il repository RDG è rimasto read-only.

## 10. Validazione LaTeX

Controlli statici:

- nessuna label duplicata;
- nessun `\ref` privo di label;
- nessuna chiave bibliografica mancante;
- sei sezioni target presenti;
- blocchi brevi mantenuti come `\paragraph`.

Recipe:

`latexmk -pdf -shell-escape thesis.tex`

Esito: compilazione conclusa con codice 0 e PDF generato. Il log finale non
contiene citazioni o riferimenti indefiniti. I warning residui comprendono
underfull box nelle tabelle, il titolo lungo di 2.1 nell'indice e warning già
presenti nella lista delle tabelle, nel Capitolo 3, nella sitografia e nella
numerazione delle pagine di backmatter.
