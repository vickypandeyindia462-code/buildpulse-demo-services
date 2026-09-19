# API Gateway recovery

1. Page Jose Nair; involve Priya Menon for a trace-contract regression.
2. Verify `/health`, route mappings, and identity-service health.
3. Sample ingress and upstream logs using one correlation ID.
4. Roll back when routing is wrong; patch header propagation when routing is healthy.
5. Require route and request-contract tests before deployment.
