# Payments API new joiner guide

Payments API creates synthetic idempotent reservations. It is a critical Tier-1 service owned by Payments Platform.

- Source: `payments-api/src`; tests: `payments-api/tests`
- API entry point: `src.app:app`; local port: `8102`
- Primary SME: Dev Shah; backup: Kavya Thomas
- Core controls: positive amounts, currency normalization, idempotency-key reuse, and bounded transient retries

Run tests before starting `uvicorn src.app:app --reload --port 8102`. A repeated identical request must return the original reservation; conflicting reuse must be rejected. Never retry an unknown result without checking the ledger. Read `docs/kb/idempotency-and-retries.md` before changing authorization or retry behavior.
