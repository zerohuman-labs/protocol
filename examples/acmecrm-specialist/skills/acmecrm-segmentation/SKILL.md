---
name: crm-segmentation
description: Create or update AcmeCRM segments and validate membership counts. Use when asked to segment contacts, adjust segment filters, or audit segment rules.
metadata:
  semver: 1.0.0
---

# AcmeCRM Segmentation Workflow

## Inputs needed

- Segment goal (who should be included/excluded)
- Any required contact fields
- AcmeCRM instance base URL and access approval

## Steps

1. Describe the segment rule in plain English and confirm with the requester.
2. Translate the rule into concrete AcmeCRM filters using available contact fields.
3. Request approval for write operations — segment changes affect campaign targeting.
4. Apply changes via the `acmecrm_api` tool with operation `upsert_contact` or `list_segments`.
5. Validate: retrieve segment membership counts and confirm they match expectations.
6. Emit artifacts:
   - `segment_definition` — the final segment rules and filter criteria
   - `campaign_audit_note` — what changed, why, and the resulting membership count

## Rollback

If segment membership is unexpected:
1. Revert to previous segment rules (document the revert as an artifact).
2. Notify the requester with the discrepancy details.
3. Do not proceed with dependent campaign operations until resolved.

## Done when

- Segment rules are updated AND membership is validated AND artifacts are emitted.
