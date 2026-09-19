# BuildPulse Demo Services

A runnable, synthetic financial-services ecosystem for demonstrating BuildPulse repository intelligence, live CI diagnosis, grounded AI assistance, ownership discovery, and safe fixes.

| Service | Purpose | Team | Tier | Port |
| --- | --- | --- | --- | --- |
| Loan Service | Explainable loan decisions and dependency-pool signals | Lending Platform | critical | 8101 |
| Payments API | Idempotent payment reservations and retry policy | Payments Platform | critical | 8102 |
| API Gateway | Route resolution and correlation propagation | Developer Platform | high | 8103 |
| Identity Service | Deterministic token-boundary demonstrations | Core Services | critical | 8104 |

## Run locally

```powershell
python -m pip install -r requirements.txt
cd loan-service
python -m pytest tests -q
uvicorn src.app:app --reload --port 8101
```

Repeat from another service directory with its assigned port. Interactive API documentation is available at `/docs`; health is at `/health`.

## Demo assets

- `service-catalog.yaml`: ownership, tier, dependencies, SLOs, runbooks, and KB links.
- `demo-data/failure-scenarios.json`: four deterministic failures with expected diagnoses and fixes.
- `demo-data/incidents.json`, `releases.json`, and `telemetry-snapshot.json`: synthetic operational history.
- `docs/kb/`: source-grounding articles used by BuildPulse Copilot.
- `docs/runbooks/` and `docs/postmortems/`: recovery and learning material.
- `docs/demo-guide.md`: end-to-end failed-build → diagnosis → fix → green-build script.

All identities, applications, accounts, incidents, metrics, and operational events are fictional. There is no customer data, credential, production code, or copied third-party application dataset in this repository.
