# API Gateway new joiner guide

API Gateway maps public routes to internal services and propagates correlation identifiers. Developer Platform owns this high-tier service.

- Source: `api-gateway/src`; tests: `api-gateway/tests`
- API entry point: `src.app:app`; local port: `8103`
- Primary SME: Jose Nair; backup: Priya Menon
- Dependencies: Loan Service, Payments API, and Identity Service

Begin with `routing.py` and `request_contract.py`. Every route change requires a dependent-service contract check. Preserve valid `X-Correlation-ID` values and generate a safe identifier when absent or invalid. Run route and propagation tests before review.
