# Identity Service new joiner guide

Identity Service provides deterministic token-boundary scenarios for the demo. Core Services owns this critical Tier-1 service.

- Source: `identity-service/src`; tests: `identity-service/tests`
- API entry point: `src.app:app`; local port: `8104`
- Primary SME: Sandeep Batra; backup: Nisha Kapoor

The HMAC format is educational, not production authentication. Never log tokens or signing material. Validate malformed input, constant-time signatures, non-empty subjects, and `exp <= now`. Security-related changes require both owners and all boundary tests.
