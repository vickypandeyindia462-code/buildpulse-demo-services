# API Gateway

Synthetic public edge service. It validates request identity and forwards authenticated requests to internal services.

## Change: correlation identifier contract

This branch requires an `X-Correlation-Id` for service-bound requests. BuildPulse should classify it as an API-contract change and identify Loan Service and Payments API as potential consumers.
