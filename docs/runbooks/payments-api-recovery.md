# Payments API recovery

1. Declare SEV-1 if duplicate authorisations are confirmed; page Dev Shah and Kavya Thomas.
2. Disable automated retries while preserving idempotency lookups.
3. Query the synthetic ledger by idempotency key and reconcile duplicate reservations.
4. Verify `tests/test_ledger.py` and `tests/test_retry_policy.py` before restoring traffic.
5. Watch error and retry rates for 30 minutes and write a blameless postmortem.
