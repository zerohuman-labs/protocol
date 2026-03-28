# DevOps Pipeline

A multi-agent ZeroHuman package demonstrating **code-backed tools**, **shared capabilities across profiles**, and **multi-agent coordination** for CI/CD, deployment, and monitoring.

## What this demonstrates

- **Multiple profiles with handoffs** — CI lead orchestrates, deploy agent handles releases, monitor agent watches production
- **Code-backed tools** — each tool includes a Python implementation file (`handler.py`) alongside its `tool.yaml` definition
- **Shared capabilities** — CI-ops and deploy-ops capabilities share the same tools and skills but are composed differently
- **Reusable skills** — the `incident-response` skill is used by both the deploy and monitor agents
- **Progressive disclosure** — tool metadata is loaded first; the Python handler is loaded only at execution time

## Structure

```
devops-pipeline/
├── zerohuman.yaml                                  # Root manifest (pack)
├── README.md
├── tools/
│   ├── github-ci/
│   │   ├── tool.yaml                               # CI pipeline tool definition
│   │   └── handler.py                              # Python implementation
│   ├── deploy/
│   │   ├── tool.yaml                               # Deployment tool definition
│   │   └── handler.py                              # Python implementation
│   └── monitoring/
│       ├── tool.yaml                               # Monitoring tool definition
│       └── handler.py                              # Python implementation
├── skills/
│   ├── pr-review/
│   │   └── SKILL.md                                # PR review workflow
│   └── incident-response/
│       └── SKILL.md                                # Incident response workflow (shared)
├── capabilities/
│   ├── ci-ops/
│   │   └── capability.yaml                         # CI capability (github-ci + pr-review)
│   └── deploy-ops/
│       └── capability.yaml                         # Deploy capability (deploy + monitoring + incident-response)
├── profiles/
│   ├── ci-lead/                                    # CI orchestrator (entry point)
│   │   ├── profile.yaml
│   │   ├── SOUL.md
│   │   └── HEARTBEAT.md
│   ├── deploy/                                     # Deployment specialist
│   │   ├── profile.yaml
│   │   ├── SOUL.md
│   │   └── HEARTBEAT.md
│   └── monitor/                                    # Production monitor
│       ├── profile.yaml
│       ├── SOUL.md
│       └── HEARTBEAT.md
└── policies/
    └── devops/
        └── policy.yaml                             # Infra controls + approval gates
```

## Code bindings

Each tool includes a `handler.py` file referenced via the `implementation` field in `tool.yaml`:

```yaml
# tool.yaml (excerpt)
implementation:
  language: python
  entrypoint: handler.py
  function: handle
```

The runtime loads the tool schema from `tool.yaml` for progressive disclosure, and only loads `handler.py` at execution time. This keeps the protocol declarative while supporting real application code.

```python
# handler.py (excerpt)
from zerohuman_runtime import ToolContext

async def handle(ctx: ToolContext, operation: str, payload: dict) -> dict:
    """Tool implementation — called by the runtime when the agent invokes this tool."""
    ...
```

## How the agents coordinate

1. **CI Lead** receives a new PR or CI event and activates the `pr-review` skill
2. After CI passes, the CI Lead hands off to the **Deploy Agent** for staging/production release
3. The **Deploy Agent** runs the deployment and hands off to the **Monitor Agent** for post-deploy verification
4. If the **Monitor Agent** detects an issue, it activates the shared `incident-response` skill and can hand back to the Deploy Agent for rollback

## Environment variables

| Variable | Purpose |
|----------|---------|
| `GITHUB_TOKEN` | GitHub API access for CI operations |
| `DEPLOY_API_URL` | Deployment service endpoint |
| `DEPLOY_DOMAIN` | Domain for deploy network allowlist |
| `MONITORING_API_URL` | Monitoring service endpoint |
| `MONITORING_DOMAIN` | Domain for monitoring network allowlist |

## Install

```bash
npx zerohuman add example-org/zerohuman-devops-pipeline
```

## Validate

```bash
npx zerohuman validate
```
