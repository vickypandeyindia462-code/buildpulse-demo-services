# Synthetic service architecture

```text
Clients → API Gateway → Loan Service → Payments API
                 │             │
                 └─────────────┴→ Identity Service
```

1. API Gateway validates access tokens through Identity Service.
2. Loan Service validates loan requests and reserves payment authorisation through Payments API.
3. Loan Service uses a bounded connection pool for dependency calls. Saturation can cause elevated timeouts.

BuildPulse should flag connection-pool, timeout, retry, authentication, migration, and API-contract changes as elevated risk. A critical-service change requires both the primary and backup owner review.
