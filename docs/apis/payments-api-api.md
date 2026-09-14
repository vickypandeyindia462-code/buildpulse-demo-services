# Payments API reference

Base URL: `http://127.0.0.1:8102` · version: `24.3.0`

`POST /v1/reservations` requires `Idempotency-Key` plus `account_id`, positive `amount_minor`, and ISO-like currency. Identical key and payload return the original reservation. Conflicting key reuse returns HTTP 409. Only 429, 503, and 504 are transient, with no more than three attempts. `GET /health` returns service status.
