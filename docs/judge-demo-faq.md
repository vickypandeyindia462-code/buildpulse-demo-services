# BuildPulse judge and demo FAQ

## Is the data real?

Integrations are live; domain data is deliberately synthetic. GitHub Actions jobs, GitHub PRs, Jira issues and transitions, and Confluence pages are real platform objects created for the demo.

## How is a fix generated?

BuildPulse combines sanitized CI evidence, repository code context, service ownership, relevant runbooks/KB, and same-service historical Jira resolutions. Deterministic classification and risk scoring remain visible. Gemini or Azure may explain the evidence but may not invent facts.

## Why multiple agents?

CI Collection, Security, Failure Analysis, Knowledge Retrieval, Jira Historical Intelligence, Risk/SME, and Copilot Response are specialized stages coordinated within one backend runtime. Providers are adapters, so Gemini can later be replaced by Azure AI Foundry.

## What happens when a dependency is offline?

GitHub CI can fall back to a labelled fixture. Repository knowledge remains searchable if Confluence is unavailable. Jira and Confluence errors are explicit and never presented as live data.

## Can it prevent a bad merge?

It identifies risky changes and prior same-service incidents, explains contributing evidence, recommends checks and reviewers, and links the source. A human retains the merge decision.

## What should be demonstrated?

Show the live Jira dashboard, thirteen failed GitHub jobs, click-to-expand CI diagnosis, four live PRs in Risk Radar, historical incident influence, multi-source Knowledge Discovery, and a Copilot answer with citations and security/audit metadata.
