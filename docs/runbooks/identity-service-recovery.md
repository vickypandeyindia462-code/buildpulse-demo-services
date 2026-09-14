# Identity Service recovery

1. Page Sandeep Batra and Nisha Kapoor for token acceptance failures.
2. Stop token issuance if signing integrity is uncertain.
3. Never paste a real token or secret into tickets, logs, or BuildPulse prompts.
4. Verify signature, expiry-boundary, and malformed-token tests.
5. Rotate secrets only through the deployment secret store, then monitor rejection rate.
