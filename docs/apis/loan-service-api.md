# Loan Service API reference

Base URL: `http://127.0.0.1:8101` · version: `24.3.0`

## `GET /health`

Returns service status and configured pool maximum.

## `POST /v1/loans/decisions`

Request fields: `application_id` string, `credit_score` integer 300–850, `annual_income` positive integer, `requested_amount` positive integer. Response contains `approved` or `referred`, annual rate when approved, and stable reason codes. Invalid boundaries return HTTP 422.

## `GET /internal/pool/{connections}`

Returns in-use, maximum, and saturation state. This endpoint is demo-internal and must not be exposed publicly.
