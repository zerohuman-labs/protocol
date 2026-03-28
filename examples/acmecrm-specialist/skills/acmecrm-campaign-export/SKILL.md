---
name: crm-campaign-export
description: Export AcmeCRM campaign data for audit and analysis. Use when asked to export campaigns, produce campaign audit reports, or archive campaign results.
metadata:
  semver: 1.0.0
---

# Campaign Export Workflow

## Inputs needed

- Campaign identifier (ID or name)
- Export purpose (audit, analysis, archival)
- Time window (if applicable)

## Steps

1. Confirm campaign identifier and export purpose with the requester.
2. Request human approval — exports can contain sensitive contact data subject to PII policy.
3. Execute export via the `acmecrm_api` tool with operation `export_campaign`.
4. Store export bundle securely; emit an `acmecrm_export_zip` artifact referencing the storage location.
5. Produce a short audit note:
   - What was exported
   - Time window covered
   - Row/record count
   - Known limitations or exclusions

## Rollback

Exports are read-only operations. If the export contains unexpected data:
1. Flag the export artifact as suspect.
2. Do not distribute the export until reviewed.
3. Notify the requester with details.

## Done when

- Export is complete AND `acmecrm_export_zip` artifact is emitted AND `campaign_audit_note` is recorded.
