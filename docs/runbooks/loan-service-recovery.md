# Loan Service recovery runbook

## Symptoms

- Loan requests time out or return 503.
- Connection-pool utilisation exceeds 90%.
- Payments API latency increases during a traffic spike.

## Safe recovery

1. Confirm the incident commander and notify Lending Platform.
2. Apply a temporary rate limit to non-critical loan-simulation endpoints.
3. Verify Payments API latency and connection-pool utilisation.
4. Increase capacity only after retry and timeout configuration is reviewed.
5. Record the mitigation, owner, and follow-up change in the incident timeline.

Primary: Meera Kulkarni. Backup: Arjun Rao.
