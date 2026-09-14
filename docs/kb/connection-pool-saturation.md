# Connection-pool saturation

Applies to: `loan-service` · owner: Lending Platform · severity: high

The service is saturated when in-use connections reach 90% of the configured maximum. Typical evidence is rising acquire latency, dependency timeouts, and a healthy process that nevertheless cannot complete requests.

## Diagnose

1. Compare `src.config.CONNECTION_POOL_MAX` with `src.connection_pool.MAX_CONNECTIONS`.
2. Check pool utilisation, request concurrency, timeout rate, and the Payments API health signal.
3. Treat a configuration mismatch as drift; do not raise capacity without checking downstream limits.

## Safe correction

Keep one source of truth for pool capacity, cap worker concurrency, and load-test at 80%, 90%, and 100% utilisation. Roll back if dependency error rate exceeds 2% or p95 latency exceeds 350 ms.

Demo failure `BP-DEMO-001` intentionally creates the two-source configuration mismatch. Its expected minimal fix is importing the configured value in the pool module.
