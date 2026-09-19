# Correlation ID contract

Applies to: `api-gateway` · owner: Developer Platform · severity: medium

The gateway accepts `X-Correlation-ID` values containing 3–64 letters, numbers, dots, underscores, or hyphens. It preserves valid values and creates a `bp-` identifier when the value is absent or invalid. The header must be forwarded to every upstream service and included in structured logs.

If trace completeness drops, compare gateway ingress and upstream request logs for the same time window. Fix propagation at the adapter boundary and verify both supplied and generated identifiers.
