# API Gateway API reference

Base URL: `http://127.0.0.1:8103` · version: `24.3.0`

`GET /health` reports route count. `GET /internal/routes/{route}` resolves a registered route and returns its target service plus correlation ID; unknown routes return 404. `X-Correlation-ID` accepts 3–64 letters, numbers, dots, underscores, or hyphens. Valid identifiers are preserved; invalid or missing values are replaced.
