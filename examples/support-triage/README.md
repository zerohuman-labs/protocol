# Support Triage

A ZeroHuman capability package for classifying inbound support tickets and routing them to specialist agents with structured handoffs and approval-gated actions.

## What this demonstrates

- **Multi-agent handoff** — triage agent classifies and routes to billing, refunds, or technical specialists
- **Queue-oriented operations** — heartbeat processes tickets in priority order with concurrency limits
- **Granular tool controls** — read and draft operations are allowed; send and update require human approval
- **Empathetic agent identity** — soul defines customer-first values and escalation-positive culture
- **Redis session memory** — higher-throughput memory strategy for queue processing workloads

## Structure

```
support-triage/
├── zerohuman.yaml                                  # Root manifest (pack)
├── README.md
├── tools/
│   └── ticketing/
│       └── tool.yaml                               # Ticketing system API
├── skills/
│   └── triage-routing/
│       └── SKILL.md                                # Intent classification + routing
├── capabilities/
│   └── support-triage/
│       └── capability.yaml                         # Capability composition
├── profiles/
│   └── support-triage/
│       ├── profile.yaml                            # Role + runtime config
│       ├── SOUL.md                                 # Identity + values
│       └── HEARTBEAT.md                            # Queue processing routine
└── policies/
    └── support/
        └── policy.yaml                             # Tool controls + data policy
```

## Key differences from AcmeCRM Specialist

| Aspect | AcmeCRM Specialist | Support Triage |
|--------|-------------------|----------------|
| Memory | SQLite (session) | Redis (session) |
| Concurrency | 2 tasks | 5 tasks |
| Token budget | 120k per run | 60k per run |
| Primary pattern | Tool execution | Routing + handoff |
| Auth | OAuth2 | API key |

## Environment variables

| Variable | Purpose |
|----------|---------|
| `TICKETING_BASE_URL` | Base URL for the ticketing API |
| `TICKETING_DOMAIN` | Domain for network allowlist |

## Install

```bash
npx zerohuman add example-org/zerohuman-support-triage
```

## Validate

```bash
npx zerohuman validate
```
