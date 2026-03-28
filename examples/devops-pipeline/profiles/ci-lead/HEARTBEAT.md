# Heartbeat

On every wake:

1. **Confirm identity.** Verify active policy and CI tool availability.
2. **Check events.** Fetch new PR events and CI triggers from the queue.
3. **Process PRs.** For each open PR needing review:
   a. Check CI run status via `github_ci` tool.
   b. Activate `pr-review` skill if review is needed.
   c. Emit review artifacts.
4. **Evaluate handoff.** If CI passes and a release is ready:
   a. Prepare handoff input (version, commit SHA, CI results summary).
   b. Hand off to `deploy_agent` for promotion.
5. **Budget check.** If approaching token limit, stop and report pending items.
6. **Summarise.** Report PRs reviewed, CI runs checked, and handoffs initiated.
7. **Stop.**
