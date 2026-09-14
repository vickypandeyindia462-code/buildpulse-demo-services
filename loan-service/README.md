# Loan Service

Synthetic loan-origination workflow. It delegates payment authorisation to Payments API and validates identity through Identity Service.

## Change: connection-pool capacity

This branch raises the safe production connection-pool target from 40 to 60 connections. BuildPulse should classify this as a resilience configuration change in a critical service. Required reviewers are the Lending Platform primary and backup owners.
