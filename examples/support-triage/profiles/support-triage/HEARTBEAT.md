# Heartbeat

On every wake:

1. **Confirm identity.** Verify active policy name and version. If policy is missing or outdated, stop and report.
2. **Check queue.** Fetch unrouted tickets ordered by urgency (critical first, then by SLA deadline).
3. **Process next ticket.** For each unrouted ticket:
   a. Read the full ticket content and customer context.
   b. Activate the `triage-routing` skill.
   c. Follow the skill procedure through to completion.
   d. Emit all required artifacts before moving to the next ticket.
4. **Respect concurrency.** Do not exceed `max_active_tasks` — if at capacity, wait for a slot.
5. **Budget check.** If token usage is approaching `per_run_tokens_max`, stop processing and report remaining queue depth.
6. **Summarise.** After processing the batch, report:
   - Tickets routed (count by specialist type)
   - Tickets escalated (count with reasons)
   - Remaining queue depth
7. **Stop.** Do not loop — the next wake will handle new tickets.
