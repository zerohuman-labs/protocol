# Support Triage

A ZeroHuman capability package for classifying inbound support tickets and routing them to specialist agents with structured handoffs and approval-gated actions.

## What this demonstrates

- **Multi-agent handoff** — triage agent classifies and routes to billing, refunds, or technical specialists via `handoffs` declarations
- **Multiple profiles in one package** — four agents (triage manager + three specialists) each with their own soul, heartbeat, and budgets
- **Shared capabilities** — all profiles reference the same capability and policy, but each has distinct identity and operational routines
- **Queue-oriented operations** — heartbeat processes tickets in priority order with concurrency limits
- **Granular tool controls** — read and draft operations are allowed; send and update require human approval
- **Empathetic agent identity** — each soul defines role-specific values and escalation-positive culture
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
│   ├── support-triage/                             # Triage manager (entry point)
│   │   ├── profile.yaml                            # Role + runtime + handoffs
│   │   ├── SOUL.md                                 # Empathetic triage identity
│   │   └── HEARTBEAT.md                            # Queue processing routine
│   ├── billing-specialist/                         # Billing specialist
│   │   ├── profile.yaml
│   │   ├── SOUL.md
│   │   └── HEARTBEAT.md
│   ├── refunds-specialist/                         # Refunds specialist
│   │   ├── profile.yaml
│   │   ├── SOUL.md
│   │   └── HEARTBEAT.md
│   └── technical-specialist/                       # Technical specialist
│       ├── profile.yaml
│       ├── SOUL.md
│       └── HEARTBEAT.md
└── policies/
    └── support/
        └── policy.yaml                             # Tool controls + data policy
```

## How handoffs work

The triage agent declares `handoffs` in its profile.yaml pointing to the three specialist profiles. At runtime:

1. The triage agent receives a new ticket and activates the `triage-routing` skill
2. The skill classifies intent → billing, refunds, or technical
3. The runtime transfers control to the matching specialist profile via the handoff mechanism
4. The specialist agent boots with its own soul, heartbeat, capabilities, and budget
5. The specialist resolves the ticket and emits artifacts

Each specialist has a **separate token budget** and **separate identity** — they are distinct agents that share the same tools and policies.

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
