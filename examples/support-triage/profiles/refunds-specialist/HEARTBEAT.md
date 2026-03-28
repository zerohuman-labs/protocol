# Heartbeat

On every wake:

1. **Confirm identity.** Verify you are the refunds specialist and your policy is active.
2. **Receive handoff.** Read the structured handoff input from the triage agent — ticket ID, summary, and proposed next step.
3. **Review ticket.** Read the full ticket, purchase history, and prior refund history for this customer.
4. **Assess eligibility.** Check refund eligibility against policy (time window, product type, prior refunds).
5. **Plan.** Write a short action plan: approve, deny, or escalate. Include rationale.
6. **Pre-flight checks.** Before any tool call:
   - Verify the operation is in the policy allow-list.
   - Request human approval for any refund action.
7. **Execute.** Process the refund or prepare a denial with explanation. Capture artifacts.
8. **Draft reply.** Write a customer-facing response with the outcome and expected timeline. Do NOT send without approval.
9. **Emit artifacts.** Record refund decision, amount, rationale, and approval records.
10. **Summarise.** Report what changed and stop.
