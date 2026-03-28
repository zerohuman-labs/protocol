# Heartbeat

On every wake:

1. **Confirm identity.** Verify active policy name and version. If policy is missing or outdated, stop and report.
2. **Fetch task.** Retrieve the highest-priority assigned task from the queue.
3. **Match skills.** Identify which skills may apply by comparing task description to skill metadata.
4. **Gather inputs.** Check that all required inputs are available. If any are missing, stop and ask — do not guess.
5. **Plan.** Write a short checklist with a clear "done" condition before executing.
6. **Pre-flight tool checks.** Before any tool call:
   - Verify the operation is in the policy allow-list.
   - Verify the target domain is in the network allow-list.
   - Request human approval if the operation requires it.
7. **Execute.** Run the plan, capturing artifacts for every meaningful output.
8. **Verify.** Check the outcome against the "done" condition. Record failures as artifacts with error details.
9. **Summarise.** Report what changed with IDs and links. Stop.
