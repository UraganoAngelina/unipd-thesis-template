---
type: "query"
date: "2026-08-02T13:43:56.633180+00:00"
question: "Genera una Tabella degli Standard di Interoperabilità basata sui nodi del grafo SI.Ter Integration Stack. La tabella deve avere tre colonne: Standard, Protocollo/Formato, Funzione nel Progetto. Includi IHE XDS.b per i documenti, FHIR R4 per i dati paziente e SAML/JWT per la sicurezza."
contributor: "graphify"
outcome: "useful"
source_nodes: ["SI.Ter Integration Stack", "IHE XDS.b", "Anagrafe Zero", "IHE IUA SAML Security", "JWT Authentication"]
---

# Q: Genera una Tabella degli Standard di Interoperabilità basata sui nodi del grafo SI.Ter Integration Stack. La tabella deve avere tre colonne: Standard, Protocollo/Formato, Funzione nel Progetto. Includi IHE XDS.b per i documenti, FHIR R4 per i dati paziente e SAML/JWT per la sicurezza.

## Answer

Expanded from original query via graph vocab: [siter, integration, ihe, xds, document, fhir, patient, saml, jwt, security, rest, token]. IHE XDS.b: SOAP/XML ed ebXML, transazioni ITI-41, ITI-18 e ITI-43 per pubblicazione, ricerca e recupero dei documenti clinici nel FSEr. HL7 FHIR R4: HTTP REST e risorse Patient/Bundle in XML, con JSON nei flussi previsti, per ricerca, assegnazione e aggiornamento dei dati paziente tramite Anagrafe Zero. SAML 2.0 e JWT RFC 7519: asserzioni XML e token JSON su HTTP/REST per identità, autorizzazione e accesso ai servizi, incluse RVE-121 e RVE-130.

## Outcome

- Signal: useful

## Source Nodes

- SI.Ter Integration Stack
- IHE XDS.b
- Anagrafe Zero
- IHE IUA SAML Security
- JWT Authentication