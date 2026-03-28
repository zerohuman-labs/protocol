# Heartbeat

On every wake:

1. **Confirm identity.** Verify active policy and monitoring tool availability.
2. **Receive context.** If woken by a deploy handoff, note the deployed version and expected baseline.
3. **Check health.** Use the `monitoring` tool to check service health across all critical services.
4. **Review alerts.** Fetch recent alerts and assess severity.
5. **Correlate.** If alerts coincide with a recent deployment:
   a. Activate the `incident-response` skill.
   b. Follow the skill procedure through to completion.
6. **Decide escalation.** Based on assessment:
   - **Nominal** — report healthy status and stop.
   - **Degraded** — hand off to `deploy_agent` with rollback recommendation.
   - **Critical** — escalate to humans immediately with incident report.
7. **Emit artifacts.** Record health check results, alert assessments, and any incident reports.
8. **Stop.**
