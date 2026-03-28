# AcmeCRM Specialist

A complete ZeroHuman capability package demonstrating all 8 protocol primitives in a realistic CRM integration scenario.

## What this demonstrates

This package models a **marketing operations specialist** that manages contacts, segments, and campaign exports in AcmeCRM. It shows:

- **Tool** — OAuth2-authenticated REST API with typed JSON Schema input/output and approval gates
- **Skills** — Two workflow procedures (segmentation and campaign export) with progressive disclosure
- **Capability** — Composition of tools, skills, and policies with eval requirements
- **Profile** — Runtime configuration with model selection, token budgets, and concurrency limits
- **Soul** — Identity constraints and non-negotiable operating principles
- **Heartbeat** — 9-step operational routine executed on every agent wake
- **Policy** — PII handling, deny-by-default network, operation-level allow/deny with human gates
- **Artifact** — Example runtime output showing trace correlation and approval records

## Structure

```
acmecrm-specialist/
├── zerohuman.yaml                                  # Root manifest (pack)
├── README.md
├── tools/
│   └── acmecrm/
│       └── tool.yaml                               # AcmeCRM REST API tool
├── skills/
│   ├── acmecrm-segmentation/
│   │   └── SKILL.md                                # Segment management workflow
│   └── acmecrm-campaign-export/
│       └── SKILL.md                                # Campaign export workflow
├── capabilities/
│   └── acmecrm-specialist/
│       └── capability.yaml                         # Capability composition
├── profiles/
│   └── acmecrm-specialist/
│       ├── profile.yaml                            # Role + runtime config
│       ├── SOUL.md                                 # Identity + values
│       └── HEARTBEAT.md                            # Operational routine
├── policies/
│   └── pii-and-outbound/
│       └── policy.yaml                             # PII + network policy
└── artefacts/
    └── examples/
        └── campaign-audit-note.json                # Example runtime artifact
```

## Environment variables

This package uses environment variable placeholders for deployment-specific values:

| Variable | Purpose |
|----------|---------|
| `ACMECRM_BASE_URL` | Base URL for the AcmeCRM API |
| `ACMECRM_DOMAIN` | Domain for network allowlist |
| `ACMECRM_OAUTH_AUTH_URL` | OAuth2 authorization endpoint |
| `ACMECRM_OAUTH_TOKEN_URL` | OAuth2 token endpoint |

Tokens are resolved from a secret store at runtime — never embedded in config.

## Install

```bash
npx zerohuman add example-org/zerohuman-acmecrm-specialist
```

## Validate

```bash
npx zerohuman validate
```
