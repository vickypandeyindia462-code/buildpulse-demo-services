# Identity Service API reference

Base URL: `http://127.0.0.1:8104` · version: `24.3.0`

`POST /v1/tokens` accepts a subject and scopes, then issues a 15-minute synthetic token. `POST /v1/tokens/verify` validates parsing, signature, and expiry; invalid tokens return 401. `GET /health` reports status. The local default secret is demo-only and deployments must inject `IDENTITY_DEMO_SECRET` from a secret store.
