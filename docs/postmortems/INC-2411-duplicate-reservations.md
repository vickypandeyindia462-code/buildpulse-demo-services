# INC-2411 — duplicate payment reservations

Status: resolved · severity: SEV-1 · data: synthetic

On 2026-08-02 a timeout retry created a second reservation after the first ledger commit. Detection came from a duplicate-reservation invariant, not customer data. The team disabled the retry path in 7 minutes, reconciled affected synthetic reservations, and restored service after 18 minutes.

The direct cause was creating a reservation before consulting the idempotency ledger. The contributing gap was a test that covered retry limits but not repeated request identity. The permanent actions were to make the lookup atomic, add same-key/same-payload and conflicting-payload tests, and document the replay procedure.

This is a blameless training record designed for BuildPulse retrieval and incident-to-change correlation.
