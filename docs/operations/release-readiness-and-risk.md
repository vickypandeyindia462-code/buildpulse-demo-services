# Release readiness and PR risk

Dashboard readiness starts at 100. Each open Jira `Highest` BuildPulse blocker deducts 8 points and each `High` blocker deducts 3. This is an explainable demo policy, not a universal production formula.

PR Risk Radar scores service criticality, resilience/configuration changes, API contracts, downstream dependencies, pending owner approval, test status, and documentation-only reductions. A same-service historical production incident adds 15 points and a required preventive-control review. Cross-service lexical matches are excluded.

A score at or above 65 is high, 35–64 medium, and below 35 low. The score supports human review; it never merges, deploys, or rejects a PR automatically.
