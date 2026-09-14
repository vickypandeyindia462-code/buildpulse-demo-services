# Security, data, and AI boundaries

All service records, customers, transactions, incidents, metrics, owners, and histories are synthetic. Credentials remain in local `.env` or managed secret stores and are never published to GitHub or Confluence.

CI logs and questions are scanned for credential and PII patterns before model use. Downloads are bounded, only actionable tails are retained, and audit IDs are returned. Gemini or Azure receives only the sanitized question and top retrieved evidence. If evidence is insufficient, the system must say so. BuildPulse recommends reversible fixes but cannot edit, merge, deploy, or close production incidents automatically.
