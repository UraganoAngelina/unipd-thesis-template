# MAPPA COMPLETA: Progetto SI.Ter e Progetto 116117 — Regione Veneto

\---

## PARTE 1: IL QUADRO NORMATIVO DI FONDO

### Il DM 77/2022 — Perché esiste tutto questo

Il Decreto Ministeriale 77 del 23 maggio 2022 è la prima milestone della **Missione 6, Componente 1 del PNRR**. È il documento che ridisegna l'assistenza territoriale italiana. Ha due allegati con valore diverso:

* **Allegato 1** (valore *descrittivo*): descrive modelli organizzativi. Le regioni possono declinarlo con margini di libertà.
* **Allegato 2** (valore *prescrittivo*): fissa standard vincolanti. Le regioni devono adeguarsi entro 6 mesi.

Il monitoraggio è affidato ad **Agenas** (relazione semestrale al Ministero). Il rispetto degli standard è condizione per accedere al **finanziamento integrativo del SSN** — quindi non è opzionale.

**Cosa definisce in concreto il DM 77:**

Il territorio si articola in **Distretti** (\~100.000 abitanti), che sono l'unità organizzativa base dell'ASL sul territorio. All'interno del Distretto operano:

|Struttura|Standard|Ruolo|
|-|-|-|
|**Casa della Comunità hub**|1 ogni 40-50.000 ab.|Punto fisico di accesso del cittadino. Presenza medica H24/7, infermieristica H12-H24/7. PUA, CUP, MMG/PLS integrati.|
|**Casa della Comunità spoke**|Secondo orografia|Satellite della hub. Presenza medica H12/6gg, infermieristica H12/6gg.|
|**COT**|1 ogni 100.000 ab.|Coordinamento presa in carico, raccordo tra setting, tracciamento transizioni. **Connessa con la CO 116117.**|
|**CO 116117**|1 ogni 1-2 milioni ab. (o regionale)|Numero unico cure non urgenti, H24/7, gratuito. Front-office telefonico per il cittadino.|
|**Ospedale di Comunità**|1 (20 PL) ogni 100.000 ab.|Ricovero breve, funzione intermedia tra domicilio e ospedale.|
|**USCA**|1 ogni 100.000 ab.|Équipe mobile distrettuale per casi complessi a domicilio. Sede nella CdC hub.|
|**IFoC**|1 ogni 3.000 ab.|Infermiere di Famiglia/Comunità, impiegato nei diversi setting.|

**Cosa il DM 77 dà per sottinteso e che devi sapere:**

* La COT **non è un front-office per il cittadino**. Il cittadino chiama il 116117. La COT è un *back-office* che coordina professionisti e servizi.
* La CO 116117 è invece il **front-office telefonico** per il cittadino, per tutto ciò che non è emergenza (il 118 resta per le emergenze).
* La COT e la CO 116117 **devono essere informaticamente interconnesse**: il DM 77 lo prescrive esplicitamente negli standard tecnologici della COT.
* Il Fascicolo Sanitario Elettronico (FSE) è il collante informativo: tutti i setting devono alimentarlo e consultarlo.

\---

## PARTE 2: IL PROGETTO 116117 — REGIONE VENETO

### 2.1 Cos'è e perché nasce

Il 116117 è il **Numero Europeo Armonizzato (NEA)** per le cure mediche non urgenti. Nasce dalla Decisione UE 2007/116/CE: stesso numero = stesso servizio in tutta Europa. In Italia recepito con l'Accordo Stato-Regioni del 24/11/2016.

**Non è una semplice sostituzione della Guardia Medica/Continuità Assistenziale (CA).** È un sistema di smistamento intelligente che intercetta la domanda a bassa intensità prima che arrivi in Pronto Soccorso.

**Il dato chiave Veneto**: dall'analisi del flusso EMUR PS 2022, circa il **30% degli accessi** ai servizi di emergenza (SUEM-118 e PS) potrebbe essere intercettato dal 116117. Parliamo di centinaia di migliaia di accessi/anno da deviare verso setting più appropriati.

### 2.2 Architettura organizzativa

**Tre Centrali Operative** per tutta la regione (quasi 5 milioni di abitanti):

|CO 116117|AULSS|Bacino|
|-|-|-|
|Centrale 1|AULSS 3 Serenissima (Venezia)|Area metropolitana veneziana|
|Centrale 2|AULSS 6 Euganea (Padova)|Area padovana|
|Centrale 3|AULSS 9 Scaligera (Verona)|Area veronese|

Le centrali sono **fisicamente attigue alle centrali del 118** (SUEM) — questa non è una coincidenza. Condividono infrastrutture telefoniche e IT per garantire il passaggio immediato delle chiamate se emerge un'urgenza.

**Operatività: H24, 7/7 fin dall'apertura.** Nessun IVR (risponditore automatico) — ogni chiamata va a un operatore umano.

### 2.3 Modello a cascata degli operatori

Il personale opera **a cascata**: l'operatore tecnico (laico) è il primo filtro. Solo se non riesce a chiudere la richiesta, passa all'infermiere. Solo se neanche l'infermiere risolve, si coinvolge il medico.

|Profilo|Ruolo|Cosa può fare|
|-|-|-|
|**Operatore tecnico laico**|Primo contatto, triage guidato da algoritmo|Identificazione chiamante, esclusione emergenza (ABC), classificazione problema con schede TAG, prenotazione slot visita CA, deviazione a infermiere/medico|
|**Infermiere di CO**|Secondo livello|Valutazione clinica infermieristica, somministrazione terapia già prescritta, gestione device (cateteri, stomie, PEG, sondini), medicazioni, rimozione punti, vaccinazione antitetanica, gestione stipsi|
|**Medico di CA**|Terzo livello|Consiglio telefonico, certificazioni, prescrizione farmaci/esami urgenti (DEMA), constatazione decesso, ASO, invio in PS, consulto con specialista online, attivazione COT|

### 2.4 Il flusso della chiamata — passo per passo

**FASE 1 — Identificazione del chiamante.** L'operatore classifica chi chiama: paziente (chiama per sé), caregiver/familiare (vede il paziente), altro (vicino di casa, nessun legame continuativo).

**FASE 2 — Esclusione emergenza (Scheda LOC A-B-C).** Prima di qualsiasi altra cosa, l'operatore verifica:

* È cosciente? → No → SUEM 118
* Respira? → No → SUEM 118
* Ha perso coscienza? → Sì → SUEM 118
* Ha cardiopalmo, dolore toracico, trauma capo/collo/torace/addome? → Sì → SUEM 118

Se tutte negative, si procede alla Fase 3.

**FASE 3 — Definizione del problema.** L'operatore usa una **gerarchia di 25 schede problema**, ognuna con:

* Definizione clinica
* Parole di entrata (sinonimi, anche popolari: "colpo della strega", "battarella", "vedo tutto girare"...)
* Parole alert per 118 (trigger di escalation immediata)
* Flow chart decisionale specifico

La gerarchia va dalla più grave alla meno grave: LOC/ABC → Febbre → Dolore addominale → Disturbi neurologici → ... → Problematica non classificabile.

**FASE 3b — Definizione del percorso.** In base alla scheda, l'esito può essere:

* Deviazione al 118
* Deviazione al medico CA (consulto telefonico)
* Deviazione all'infermiere CA
* Prenotazione slot visita CA
* Prenotazione teleconsulto specialista
* Deviazione alla Centrale ADI (se paziente già in carico)
* Chiusura diretta (non pertinente)

**Cosa il manuale protocollo sottintende e che è cruciale:**

* Le "parole alert" sono il meccanismo di safety: se l'operatore laico sente "vomito con sangue" durante una scheda di dolore addominale, deve deviare al 118 immediatamente, senza completare il percorso della scheda.
* Il **fattore tempo** è discriminante in diverse schede: un disturbo neurologico presente da meno di 24h → 118 (possibile ictus). Lo stesso disturbo da più di 24h → medico CA.
* La scheda "Disturbo psichico" include parole di entrata come "mi sento solo", "sono triste", "ho voglia di parlare" — il 116117 è anche un punto di contatto per il disagio psicologico non emergente.
* L'urologico è l'unica scheda senza parole alert per il 118, ma prevede comunque l'invio autonomo in PS (dolore al testicolo < 6h → possibile torsione testicolare).

### 2.5 Integrazione con gli altri sistemi (aspetto tecnico)

Il documento "Cantiere 116117" specifica che la CO 116117 **deve** essere nativamente integrata con:

1. **Centrale 118** — passaggio bidirezionale delle chiamate
2. **Continuità Assistenziale** — prenotazione slot, deviazione chiamata
3. **PUA (Punto Unico di Accesso)** — per bisogni sociosanitari, tramite interoperabilità applicativa
4. **COT** — attivazione percorsi di presa in carico
5. **Piattaforma regionale di telemedicina** — teleconsulti specialistici
6. **Cartelle MMG/PLS** — sistema di notifiche (ogni contatto 116117 viene notificato al curante)
7. **Anagrafe regionale** — dati aggiornati degli assistiti residenti

Il software deve essere **certificato EN ISO 13485:2016** per gli algoritmi di triage (è un dispositivo medico).

L'infrastruttura telefonica è **centralizzata su due sedi** (ridondanza) e usa tecnologia **IP** — gli operatori di qualsiasi centrale possono supportare le altre in caso di caduta o picchi.

\---

## PARTE 3: IL PROGETTO SI.Ter (SISTEMA INFORMATIVO TERRITORIALE)

### 3.1 Cos'è e perché nasce

Il SI.Ter è il progetto di Azienda Zero (l'ente regionale che governa il SSR veneto) per dotare **tutti i 12 Enti Sanitari del Veneto** di un unico sistema informativo per i servizi territoriali.

Nasce dalla constatazione che il territorio veneto è **frammentato**: ogni AULSS ha applicativi diversi per COT, ADI, Consultori, CSM, etc. La DGR 72/2024 ha assegnato ad Azienda Zero l'obiettivo di realizzare il SI.Ter.

Il veicolo contrattuale è un **Appalto Specifico** sull'Accordo Quadro CONSIP "Sanità Digitale" ID 2365, Lotto 3. Durata massima **48 mesi**. L'offerta è datata 22/09/2025.

### 3.2 Chi è l'RTI aggiudicatario

Un RTI (Raggruppamento Temporaneo di Imprese) di **13 aziende**:

* **Mandataria**: AlmavivA S.p.A.
* **Mandanti principali**: GPI S.p.A., Accenture, ATS (Accenture Technology Solutions)
* **Altre mandanti**: AlmavivA DigitalTec, AI4Health, Doctolib, A-thon, TAS, IQVIA, ISED, Onit Sanità, Postel

### 3.3 I moduli software

La soluzione è composta da **due suite applicative principali** + un modulo trasversale:

|Suite|Vendor|Moduli|Già in uso nel Veneto|
|-|-|-|-|
|**ePersonam** (Advenias, sub di AlmavivA)|AlmavivA/Advenias|COT, ADI, ODC, URT, Hospice|COT: 8 AULSS su 9; ADI: AULSS 2, 3, 4, 9; ODC/URT/Hospice: AULSS 2, 3, 9|
|**SisTer** (GPI S.p.A.)|GPI|Consultori, Età Evolutiva, NPI, CSM|Consultori+DSM: AULSS 2, 3. Vecchio sistema GPI: AULSS 5, 7, 9|
|**Prescrizione Elettronica**|RTI (trasversale)|Ricetta dematerializzata farmaceutica e specialistica|Integrato con SAR regionale|

**Cosa questo implica e che devi capire:**

La strategia non è "buttiamo tutto e rifacciamo". La maggior parte del software è **già installato** in molte aziende. Il progetto SI.Ter è soprattutto:

1. **Estensione** dei moduli alle AULSS che non li hanno ancora
2. **Omogeneizzazione** delle configurazioni tra AULSS diverse
3. **Aggiunta di nuove funzionalità** richieste dal Capitolato (es. nuovi flussi NSIS)
4. **Migrazione su cloud PSN** (Polo Strategico Nazionale)
5. **Integrazione con il SIO regionale** (Sistema Informativo Ospedaliero unico) dove già avviato

### 3.4 Architettura tecnica

L'architettura è **multi-layer, a microservizi, cloud-native, multitenant**:

* **Layer Presentazione**: Angular, React (SPA), HTML5/CSS3, responsive
* **Layer Interoperabilità**: WSO2 Micro Integrator (orchestrazione), RabbitMQ (messaging asincrono), Drools (transformation engine), supporto HL7/FHIR/XDS.b/REST
* **Layer Process Automation**: Camunda v7 (engine BPMN/DMN) — gestisce i workflow clinici complessi come dimissione/ammissione protetta
* **Layer Business Logic**: Java (OpenJDK 11 e 21), Spring Boot 2.x/3, NodeJS, microservizi containerizzati
* **Layer Persistenza**: DB relazionali (suite applicative) + NoSQL (messaggi HL7 FHIR, log, audit, knowledge base)
* **Layer BI**: Almaviva Helios.Data (Data Lake)
* **Layer DevSecOps**: Azure DevOps, GitLab, SonarQube, CAST MRI, Selenium, JMeter, OWASP ZAP
* **Layer Monitoraggio**: Zabbix + stack ELK (Elasticsearch, Kibana, Logstash)

**Infrastruttura**: PSN (Polo Strategico Nazionale) o altro cloud del Committente. Due ambienti: Produzione e Test/Collaudo, disaccoppiati.

**Multitenancy**: un'unica istanza software serve tutti gli ES, con **segregazione logica** dei dati per AULSS. Un'anomalia in un ES non si propaga agli altri.

### 3.5 Integrazioni chiave

Il SI.Ter si integra con un ecosistema vasto:

|Sistema|Cosa fa|Standard/Transazione|
|-|-|-|
|**APMS**|Autenticazione operatori (SSO federato)|\[RVE-142] + Cognito|
|**Anagrafe Zero**|Ricerca/aggiornamento anagrafica pazienti|\[RVE-54] Patient Query, \[RVE-55], \[RVE-57], \[RVE-100] (FHIR)|
|**SAR**|Prescrizione dematerializzata|\[MEF-1] Invio Prescritto, \[MEF-6] Annulla Prescritto|
|**CUP**|Liste di lavoro ambulatoriali, cambi stato erogato|HL7 SIU|
|**ADT**|Notifiche ricovero/dimissione per dimissione protetta|HL7 v2.5.1|
|**XDS Repository/Registry**|Pubblicazione referti nel FSEr|ITI-41, ITI-57, Affinity Domain v2.30|
|**FSE/Visualizzatore**|Consultazione documenti paziente|\[RVE-121], \[RVE-130] Chiamata Contesto|
|**Firma digitale regionale**|Firma documenti clinici|Provider regionale|
|**CO 116117**|Smistamento richieste sociosanitarie dalla CO al PUA/COT|Integrazione nativa con PUA|
|**SIO-RVE**|Quando disponibile, sostituisce integrazioni legacy|Specifiche RVE|
|**Telemedicina RVE**|Teleconsulti|Chiamata contesto|

**L'elemento critico sottinteso**: dove il SIO regionale non è ancora attivo, il SI.Ter deve integrarsi con i **sistemi legacy** di ciascun ES (anagrafi locali, ADT locali, repository locali). Poi, quando il SIO arriva, deve switchare sulle specifiche regionali. Questo raddoppio di integrazioni è un'enorme complessità progettuale.

### 3.6 I tre interventi della fornitura

|Intervento|Cosa|Importo|Durata|
|-|-|-|-|
|**N°1**|Implementazione moduli Consultorio, OdC, URT, Cure Domiciliari + flussi NSIS (SIAR, SICOF, SIOC)|\~2,25M€|10 mesi|
|**N°2**|Completamento, diffusione, formazione, import dati, presidio locale, MEV di tutti i moduli su tutti gli ES|\~2,38M€|40 mesi|
|**N°3**|Help-Desk dedicato + Manutenzione Ordinaria (MAD-MAC) per tutti i moduli|\~2,54M€|36 mesi + opzione 12|
|**TOTALE**||**\~7,18M€**|Fino a 48 mesi|

### 3.7 Cronoprogramma (milestone PNRR-driven)

|Data|Milestone|
|-|-|
|Entro 30/11/2025|Assessment e Piano di Lavoro di Obiettivo|
|Entro 31/03/2026|Completamento migrazione cloud (milestone PNRR)|
|Entro 03/2026|Test e collaudo Consultorio, OdC, URT, Cure Domiciliari|
|Entro 06/2026|Formazione e avvio Consultorio, OdC, URT su tutti gli ES|
|Entro 30/06/2026|Conclusione iniziative flussi NSIS (milestone PNRR M6C2)|
|Entro 12/2026|Avvio Cure Domiciliari + Test/Collaudo CSM, Prescrizione, Hospice, COT|
|Entro 06/2027|Avvio CSM, Prescrizione, Hospice, COT su tutti gli ES|

### 3.8 I casi d'uso concreti (come funziona in pratica)

**Caso 1 — Dimissione protetta con attivazione ADI:**

1. L'infermiere del reparto Geriatria (Ospedale dell'Angelo, Mestre) decide, dopo consulto col medico, di dimettere il paziente con ADI
2. Accede a **ePersonam**, si autentica via APMS, cerca il paziente su Anagrafe Zero o ADT
3. Il sistema importa automaticamente: reparto, nosologico, data ricovero, diagnosi, data prevista dimissione
4. L'infermiere consulta il **Visualizzatore FSE** per documentazione da altri ES
5. Compila: anamnesi, patologie, rischio infettivo, allergie, scala BRASS
6. Seleziona setting proposto: "ADI Infermieristica", centrale: "ADI Distretto 2 - Mestre"
7. Clicca "Inoltra" → stato diventa "Inoltrata"
8. **L'operatore COT** riceve la segnalazione, la valuta, compila scheda Cure Domiciliari, assegna setting definitivo "ADI FAVARO"
9. **L'operatore ADI** di Favaro vede il paziente nella lista d'attesa, apre la cartella, programma le attività sul **Pianificatore** (agenda calendarizzata tipo Google Calendar)
10. Ogni accesso domiciliare viene tracciato, con km percorsi, orario effettivo, note. Disponibile anche via **app mobile**.

**Caso 2 — Accesso al Consultorio (percorso coppia salute riproduttiva):**

1. La paziente ha prenotato tramite CUP
2. L'operatore accede a **SisTer**, trova la prenotazione nella worklist
3. Apre cartella: tipo percorso "B – Salute Riproduttiva", motivo "Consulenza", inviante "MMG"
4. Associa il compagno → il percorso diventa **di coppia**
5. La paziente chiede oscuramento → visibile solo all'équipe in carico
6. Il percorso attraversa fasi: Accoglienza → Valutazione → Trattamento → Chiusura
7. Alla chiusura, è possibile attivare **automaticamente** un nuovo percorso (es. adozione/affido)

**Caso 3 — CSM (assunzione in cura psichiatrica):**

1. Il paziente accede al CSM di Treviso con prenotazione CUP
2. Fase di accoglienza articolata in sottofasi: Contatto (amministrativo) → Sociale (assistente sociale) → Sanitario (infermiere) → Valutazione clinica (medico) → Esito
3. L'esito può essere: consulenza, presa in carico multidisciplinare, assunzione in cura (psichiatra), invio ad altri servizi
4. Nel trattamento: terapia con somministrazione diretta (il farmaco viene dato dall'infermiere al CSM), con worklist di somministrazione
5. Inserimento in struttura residenziale/semiresidenziale con progetto di obiettivi
6. **Se il paziente viene ricoverato in ospedale** durante il percorso, il sistema ADT notifica automaticamente ePersonam/SisTer → sospensione del percorso

### 3.9 Servizi di presidio on-site

L'RTI propone **8 risorse di presidio** distribuite sul territorio:

* 5 stanziali (1 per macro-area geografica)
* 3 aggiuntive per picchi/copertura assenze

Distribuzione basata su affinità di fornitura: dove ePersonam è già presente per COT+ADI, una stessa risorsa copre le AULSS contigue.

### 3.10 SLA migliorativi

|Categoria|Descrizione|Presa in carico RTI|Risoluzione RTI|Risoluzione da AQ|
|-|-|-|-|-|
|1 - Critica|Sospensione/grave degrado, tutti gli utenti|30 min|2h lavorative|8h lavorative|
|2 - Alta|Sospensione/grave degrado, uno o più utenti|1h|4h lavorative|12h lavorative|
|3 - Media|Parziale degrado|2h|8h lavorative|2gg lavorativi|
|4 - Bassa|Marginale, workaround disponibile|2h|2gg lavorativi|4gg lavorativi|

Assistenza: **8:00-20:00, 365gg/anno** + reperibilità.

\---

## PARTE 4: IL LEGAME TRA 116117 E SI.Ter

Questo è il punto che molti danno per scontato ma che è fondamentale capire:

1. La **CO 116117** è il front-office telefonico del cittadino. Quando il cittadino chiama e ha un bisogno sociosanitario (es. attivazione ADI, bisogno di servizi distrettuali), la CO 116117 **invia un alert al PUA** tramite interoperabilità applicativa.
2. Il **PUA** (Punto Unico di Accesso) è il punto dove si formalizza la domanda. Azienda Zero ha già acquisito un software PUA separato (gestito da AlmavivA), che è **nativamente integrato con ePersonam** (il software COT/ADI del SI.Ter).
3. La **COT** riceve le segnalazioni dal PUA (e da reparti ospedalieri, servizi territoriali, etc.) e le gestisce attraverso ePersonam, smistando verso il setting definitivo appropriato (ADI, ODC, URT, Hospice, etc.).
4. Il **SI.Ter** (ePersonam + SisTer) è lo strumento che gestisce l'intero percorso dal momento in cui la COT assegna il setting definitivo fino alla conclusione del percorso di cura.

**In sintesi il flusso è**: Cittadino → 116117 → triage → bisogno sociosanitario → PUA → COT (ePersonam) → setting definitivo → gestione percorso (ePersonam per ADI/ODC/URT/Hospice, SisTer per Consultori/CSM).

\---

## PARTE 5: L'INFRASTRUTTURA DI SICUREZZA

Il documento "Infrastruttura di sicurezza GDL-O Sicurezza v2.14" definisce le regole del gioco per l'autenticazione e la sicurezza nell'ecosistema digitale di Azienda Zero. I punti chiave:

* **APMS** (Application Profile Management System) è il gateway di autenticazione centralizzato, basato su AWS Cognito
* Ogni ES ha il proprio **Identity \& Assertion Provider (IAP)** — APMS fa da federatore
* Profilo **IHE ATNA** per audit trail: ogni azione viene loggata e inviata a un ARR (Audit Record Repository) regionale
* **Privacy by design e by default** sono obbligatori (artt. 25 e 32 GDPR)
* Il Fornitore è nominato **Responsabile del trattamento** ex art. 28 GDPR
* Security Manager reperibile **24x7x365**
* Connessione remota **solo** via VPN site-to-site o dedicata. VPN-Client solo in casi eccezionali e con IP statico
* **Mai dati reali in ambienti non produttivi**
* Vulnerability assessment/penetration test periodici obbligatori
* Disaster Recovery con test **almeno 2 volte l'anno**

\---

## PARTE 6: GLOSSARIO OPERATIVO ESSENZIALE

|Termine|Significato|Contesto d'uso|
|-|-|-|
|**Azienda Zero**|Ente regionale di governance del SSR veneto|Committente del SI.Ter, coordina tutti gli ES|
|**ES**|Ente Sanitario|Le 9 AULSS + 2 AO + IOV = 12 ES totali|
|**COT**|Centrale Operativa Territoriale|Back-office di coordinamento, non parla col cittadino|
|**CO 116117**|Centrale Operativa 116117|Front-office telefonico per il cittadino|
|**CA**|Continuità Assistenziale|Ex "Guardia Medica"|
|**PUA**|Punto Unico di Accesso|Sportello dove si formalizza la domanda sociosanitaria|
|**ADI**|Assistenza Domiciliare Integrata|Cure a domicilio multiprofessionali|
|**ODC**|Ospedale di Comunità|Ricovero breve post-acuzie|
|**URT**|Unità Riabilitativa Territoriale|Riabilitazione intermedia|
|**SVAMA**|Scheda Valutazione Multidimensionale Adulto/Anziano|Strumento per determinare bisogni assistenziali|
|**VMD/UVMD**|Valutazione Multidimensionale / Unità di VMD|Équipe che valuta il paziente complesso|
|**PAI**|Piano Assistenziale Individualizzato|Documento che definisce obiettivi e interventi|
|**Setting proposto**|Destinazione suggerita dal richiedente|Es. "ADI infermieristica"|
|**Setting definitivo**|Destinazione finale assegnata dalla COT|Es. "ADI FAVARO Distretto 2"|
|**BRASS**|Blaylock Risk Assessment Screening Score|Scala per identificare pazienti a rischio di dimissione complessa|
|**Dimissione protetta**|Dimissione ospedaliera con attivazione servizi territoriali|Ospedale → COT → setting territoriale|
|**Ammissione protetta**|Ingresso in ospedale da setting territoriale|Territorio → COT → ospedale|
|**Parole alert**|Termini che triggerano il passaggio al 118|Es. "sincope", "vomito con sangue"|
|**Parole di entrata/TAG**|Sinonimi che identificano il problema|Es. per febbre: "brividi", "è tanto caldo"|
|**FHIR**|Fast Healthcare Interoperability Resources|Standard di interoperabilità sanitaria|
|**XDS.b**|Cross-Enterprise Document Sharing|Profilo IHE per condivisione documenti|
|**FSEr**|Fascicolo Sanitario Elettronico regionale|Repository dei documenti clinici del paziente|
|**SIO-RVE**|Sistema Informativo Ospedaliero Regionale Veneto|Il progetto parallelo per l'ospedale unico regionale|
|**PSN**|Polo Strategico Nazionale|Cloud della PA italiana|
|**Labeling**|Processo di certificazione regionale|Ogni integrazione deve superare labeling e collaudo|
|**SICOF**|Sistema Informativo Consultori Familiari|Flusso NSIS obbligatorio|
|**SISM**|Sistema Informativo Salute Mentale|Flusso NSIS obbligatorio|
|**SIAD**|Sistema Informativo Assistenza Domiciliare|Flusso NSIS obbligatorio|
|**SIAR**|Sistema Informativo Assistenza Riabilitativa|Nuovo flusso NSIS (PNRR)|
|**CVP**|Catalogo Veneto del Prescrivibile|Codifica regionale delle prestazioni|
|**Farmadati**|Banca dati farmaceutica|Sincronizzata con AIFA|
|**DEMA**|Prescrizione dematerializzata|Ricetta elettronica|

\---

## PARTE 7: ZONE GRIGIE E PUNTI DI ATTENZIONE

1. **Il PUA non è nel perimetro SI.Ter ma è integrato.** Il software PUA è acquisito separatamente da Azienda Zero, ma è di AlmavivA — la stessa mandataria del SI.Ter. L'integrazione nativa è un vantaggio competitivo dichiarato.
2. **Il SIO regionale è in corso di deployment.** Dove non c'è ancora, il SI.Ter deve integrarsi con i sistemi legacy. Questo crea una complessità a doppio binario durante il transitorio.
3. **La Prescrizione Elettronica ha una clausola di flessibilità.** L'RTI offre la possibilità di mantenere il sistema di prescrizione già in uso presso gli ES, oppure adottare quello offerto. Questo per non forzare un cambio dove non serve.
4. **I flussi NSIS sono milestone PNRR con deadline giugno 2026.** SICOF (consultori), SIAR (riabilitazione), SIOC (ospedali di comunità) sono nuovi e hanno specifiche ancora in evoluzione. Il fornitore deve adeguarsi anche a flussi futuri (es. NPI — Neuropsichiatria Infantile).
5. **La questione della continuità operativa durante la migrazione.** Il Capitolato è esplicito: la sostituzione degli attuali software deve avvenire **senza interruzione delle attività cliniche**. Serve un piano di avvicendamento che garantisca continuità.
6. **Il dato storico.** Ogni ES ha anni di dati nei sistemi uscenti. La migrazione dello storico è compresa nella fornitura (il SI.Ter mette a disposizione le interfacce di import), ma l'export e la bonifica sono a carico degli ES. Questo è un potenziale collo di bottiglia.
7. **Le 3 centrali 116117 non sono ancora pienamente operative.** Il documento "Cantiere 116117" è datato giugno 2024 e contiene ancora "quesiti aperti" (come si interfaccerà con le attività assistenziali già in essere? Il pediatra è uno specialista online?). Il cronoprogramma di attivazione è "da definirsi".

