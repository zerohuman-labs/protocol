---
name: incident-response
description: Respond to a production incident — assess impact, coordinate rollback if needed, and document the incident. Use when monitoring alerts indicate a service degradation or outage.
metadata:
  semver: 0.3.0
---

# Incident Response Workflow

Coordinate the response to a production incident, from initial assessment through resolution and documentation.

## Inputs needed

- Alert details (service, severity, time of detection)
- Current deployment version
- Recent deployment history

## Steps

1. **Assess impact.** Use the `monitoring` tool to check service health and gather metrics.
   - Which services are affected?
   - What is the user impact (error rate, latency, availability)?
   - When did the degradation start?
2. **Correlate with deploys.** Check if a recent deployment correlates with the incident timeline.
   - Use `deploy` tool to get recent deploy status
   - If correlation is strong, prepare for rollback
3. **Decide action.** Based on severity and correlation:
   - **Rollback** — if a deploy is the likely cause and impact is high
   - **Investigate** — if cause is unclear, gather more data
   - **Monitor** — if impact is low and self-recovering
4. **Execute.** If rolling back:
   - Request human approval for production rollback
   - Execute rollback via the `deploy` tool
   - Verify recovery via the `monitoring` tool
5. **Document.** Emit artifacts:
   - `incident_report` — timeline, impact, root cause, actions taken
   - `rollback_record` — if rollback was performed, before/after versions

## Done when

- Service health is restored (or escalated to humans) AND incident artifacts are emitted.
