# Payment idempotency and retries

Applies to: `payments-api` · owner: Payments Platform · severity: critical

Only retry transient statuses 429, 503, and 504, and never exceed three total attempts. Every reservation request must include an idempotency key. An identical key and payload returns the original reservation; the same key with a different payload is rejected.

## Diagnose

Look for repeated correlation IDs, identical account/amount pairs, timeout responses, and different reservation IDs. Confirm whether the retry happened before or after the ledger commit.

## Safe correction

Perform the idempotency lookup before creating a reservation. Preserve the original response, reject conflicting reuse, use bounded exponential backoff, and run reconciliation after any duplicate-payment incident.
