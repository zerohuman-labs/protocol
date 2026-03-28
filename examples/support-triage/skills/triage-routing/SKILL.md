---
name: triage-routing
description: Classify a support request, choose a specialist, and hand off with structured input. Use for any new inbound ticket that needs routing.
metadata:
  semver: 0.8.0
---

# Triage Routing

Route inbound support tickets to the right specialist agent based on intent, urgency, and customer impact.

## Inputs needed

- Ticket ID and full ticket content
- Customer context (account tier, history) if available

## Steps

1. **Identify intent.** Read the ticket and classify into one of:
   - `billing` — payment issues, invoices, plan changes
   - `refunds` — refund requests, credit disputes
   - `technical` — bugs, errors, integration issues, feature questions
   - `account` — login issues, permissions, account settings
2. **Assess urgency.** Rate as `low`, `medium`, `high`, or `critical` based on:
   - Customer impact (affecting production? revenue?)
   - Account tier (enterprise = higher default urgency)
   - Time sensitivity (SLA deadlines approaching?)
3. **Handle ambiguity.** If the intent is unclear or spans multiple categories:
   - Add an internal note with your best assessment and the alternatives
   - Escalate to a human for routing decision
   - Do not guess — ask for clarification
4. **Prepare handoff input.** Create a structured summary for the specialist:
   - `ticket_id`
   - `intent` and `urgency`
   - `summary` — one-paragraph description of the issue
   - `proposed_next_step` — what the specialist should do first
5. **Draft customer reply.** Write an acknowledgment reply for the customer:
   - Confirm receipt
   - Set expectation on response time
   - Do NOT send unless policy allows and approval is granted
6. **Emit artifacts.**
   - `triage_decision` — intent, urgency, routing rationale, chosen specialist
   - `customer_reply_draft` — the draft acknowledgment (not sent)
   - `escalation_note` — if escalated, why and to whom

## Done when

- Ticket is routed to a specialist OR escalated to a human, AND all artifacts are emitted.
