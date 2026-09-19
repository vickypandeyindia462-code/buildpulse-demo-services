# BuildPulse live-fix demonstration

## Baseline

Run `python -m pytest tests -q` in each service directory. The healthy branch should pass every test. Start a service with `uvicorn src.app:app --reload --port 8101` from its directory and visit `/docs` or `/health`.

## Recommended scenario

Use `BP-DEMO-001`, connection-pool configuration drift:

1. On a disposable `demo/failing-loan-pool` branch, add a test asserting `connection_pool.MAX_CONNECTIONS == config.CONNECTION_POOL_MAX` while retaining the deliberate 40/60 mismatch.
2. Push the branch to produce a genuine failed GitHub Actions job.
3. Open BuildPulse → CI Failures → Loan Service. Show the failed step, classification, risk, owners, KB evidence, and suggested checks.
4. Ask Copilot for a source-grounded diagnosis. The expected minimal fix is to remove the duplicate constant and import `CONNECTION_POOL_MAX` from `src.config`.
5. Apply the fix, rerun tests, push, and refresh BuildPulse to show the transition from failed to passed.

Never run the failure scenario on `main` or a release branch. All people, incidents, metrics, accounts, and transactions in this repository are fictional.
