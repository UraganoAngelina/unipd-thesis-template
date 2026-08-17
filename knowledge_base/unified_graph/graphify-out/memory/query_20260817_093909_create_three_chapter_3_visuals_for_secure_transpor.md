---
type: "query"
date: "2026-08-17T09:39:09.376055+00:00"
question: "Create three Chapter 3 visuals for secure transport, semantic dependencies, and the UI persistence bridge, using the current RDG implementation as evidence."
contributor: "graphify"
outcome: "useful"
source_nodes: ["MtlsContextFactory", "SSLContext", "resolve_placeholders()", "SAML 2.0 Assertion", "ui_config_bridge.py", "ConfigTab", "RunTab", "main.py"]
---

# Q: Create three Chapter 3 visuals for secure transport, semantic dependencies, and the UI persistence bridge, using the current RDG implementation as evidence.

## Answer

Expanded from the original request via graph vocabulary: [mtls, ssl, context, factory, certificate, pkcs, aiohttp, session, gateway], [placeholder, assertion, saml, output, extract, occurrence, resolve, rve, iti], and [config, bridge, tab, dashboard, json, load, save, pipeline]. The source confirms that MtlsContextFactory loads and caches profile-specific SSLContext objects and send_request injects them into aiohttp; ITI-18 resolves the exact occurrence-local placeholder step_0.saml_assertion_xml_linearized after RVE-1.b extraction; ConfigTab and RunTab access config/experiment.json through ui_config_bridge.py, while main.py remains independent and resolves its own runtime configuration. Three source-grounded TikZ figures were integrated and compiled successfully.

## Outcome

- Signal: useful

## Source Nodes

- MtlsContextFactory
- SSLContext
- resolve_placeholders()
- SAML 2.0 Assertion
- ui_config_bridge.py
- ConfigTab
- RunTab
- main.py