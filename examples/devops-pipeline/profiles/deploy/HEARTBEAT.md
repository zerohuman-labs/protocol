# Heartbeat

On every wake:

1. **Confirm identity.** Verify active policy and deploy tool availability.
2. **Receive handoff.** Read the structured input from the CI lead — version, commit SHA, CI results.
3. **Create release.** Use the `deploy` tool to create a versioned release.
4. **Promote to staging.** Deploy to staging environment and verify.
5. **Verify staging.** Use the `monitoring` tool to check staging health.
6. **Request production approval.** If staging is healthy, request human approval for production promotion.
7. **Promote to production.** After approval, deploy to production.
8. **Hand off monitoring.** Prepare handoff input for the monitor agent:
   - Deployed version
   - Deployment timestamp
   - Expected metrics baseline
9. **Emit artifacts.** Record `deploy_record` with version, environments, and approval chain.
10. **Stop.**
