# Payments API

Synthetic payment-authorisation dependency for Loan Service. It receives idempotent reservation requests through API Gateway.

## Change: retry policy

This branch adds bounded retries for idempotent requests that receive 429, 503, or 504 responses. BuildPulse should identify this as a dependency-resilience change affecting Loan Service.
