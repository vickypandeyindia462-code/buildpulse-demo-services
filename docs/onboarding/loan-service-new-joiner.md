# Loan Service new joiner guide

## Mission

Loan Service produces explainable synthetic lending decisions and coordinates payment authorization. It is a critical Tier-1 service owned by Lending Platform.

## First-day map

- Source: `loan-service/src`
- Tests: `loan-service/tests`
- API entry point: `src.app:app`
- Dependencies: Payments API and Identity Service
- Health endpoint: `GET /health`
- Local port: `8101`
- Primary SME: Meera Kulkarni; backup: Arjun Rao

## Run locally

Install root requirements, enter `loan-service`, run `python -m pytest tests -q`, then `uvicorn src.app:app --reload --port 8101`.

## Safety rules

Keep one source of truth for pool capacity. Treat connection-pool, timeout, retry, credit-policy, and downstream-contract changes as high risk. Never use real applicant data.

## First useful change

Add a boundary test to `src.domain.assess`, run the full service suite, review `docs/kb/connection-pool-saturation.md`, and request both primary and backup owner review.
