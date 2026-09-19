# Token validation boundaries

Applies to: `identity-service` · owner: Core Services · severity: critical

The demo identity service uses an HMAC token only to provide deterministic security scenarios. It is not production authentication. Validation must parse safely, compare signatures in constant time, and reject a token when `exp <= now`.

Never log tokens or signing material. Rotate the demo secret if it is disclosed, invalidate existing demo sessions, and inspect BuildPulse security findings for credential-like text before sharing logs.
