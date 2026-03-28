# ZeroHuman Protocol

An open protocol for structured AI operations — defining how agents discover, install, and execute reproducible skills, typed tools, composable capabilities, and governed profiles.

> **Protocol version:** 0.1.0
> **Full specification:** [zerohuman-v0.1.0.md](./zerohuman-v0.1.0.md)

---

## The 8 Primitives

Every ZeroHuman package is built from a small set of file types. Together they define the complete operational model for any agent.

| Primitive | Filename | Purpose |
|-----------|----------|---------|
| **Tool** | `tool.yaml` | Typed integration surface — API schema, auth, permissions, approval gates |
| **Skill** | `SKILL.md` | Reusable procedural knowledge — YAML frontmatter + markdown instructions |
| **Capability** | `capability.yaml` | Versioned composition of tools + skills + policies + evals |
| **Profile** | `profile.yaml` | Role configuration — model, runtime, budgets, concurrency, memory |
| **Heartbeat** | `HEARTBEAT.md` | Run-loop checklist that prevents drift and ensures consistent routines |
| **Soul** | `SOUL.md` | Identity, values, and boundaries that should change rarely |
| **Policy** | `policy.yaml` | Enforceable rules — permissions, approvals, network policy, data sensitivity |
| **Artifact** | `artifact.json` | Immutable record of what was produced, with trace IDs and lineage |

All packages have a root **`zerohuman.yaml`** manifest that declares what's inside and how to find it.

---

## Root Manifest — `zerohuman.yaml`

Every ZeroHuman package starts with this file at the repo root:

```yaml
# zerohuman.yaml — required fields
name: my-package                          # Human-readable name (1-128 chars)
slug: my-package                          # URL-safe identifier (lowercase, hyphens ok)
version: 1.0.0                            # Semantic version
description: What this package does.      # Optional, max 500 chars
package_type: skill                       # skill | tool | capability | profile | policy | pack
objects:                                  # At least one object required
  - type: skill
    id: my-skill                          # Unique within this package
    path: skills/my-skill                 # Directory containing the primitive files

# Optional — enriched metadata for the registry and spec compliance
compatibility:
  agents:
    - claude-code
    - github-copilot
    - cursor
source:
  repo: https://github.com/you/my-package
license: MIT

# Protocol-level fields (informational — used by registry scoring)
protocol: zerohuman
protocol_version: 0.1.0
indexing:
  discoverable: true
  tags: [my-domain]
```

**`package_type`** determines what kind of objects the package contains:
- Use `skill`, `tool`, `capability`, `profile`, or `policy` for single-type packages
- Use `pack` for packages that bundle multiple object types together

---

## Getting Started

### 1. Create the directory structure

```
my-package/
├── zerohuman.yaml
├── README.md
└── skills/
    └── my-skill/
        └── SKILL.md
```

### 2. Write your `zerohuman.yaml`

See the root manifest reference above. Every `objects[].path` must point to a directory that exists.

### 3. Add your primitives

Create the files referenced by your objects. See the [examples](#examples) for each primitive type.

### 4. Validate

```bash
npx zerohuman validate
```

### 5. Publish

```bash
# Others can install your package from GitHub:
npx zerohuman add you/my-package
```

---

## Precedence Rules

When multiple instruction sources exist, ZeroHuman resolves conflicts using this stack (highest wins):

| Priority | Source | Example |
|----------|--------|---------|
| 1 (highest) | Explicit user/task input | Task payload, human steering notes |
| 2 | Task-local overrides | `tasks/<id>/override.md` |
| 3 | Profile overlays | Profile heartbeat + soul + profile policy |
| 4 | Capability package content | capability.yaml → skills/tools/policies |
| 5 | Organisation global policy | Org-level policy files |
| 6 (lowest) | Runtime defaults | Engine safe baselines |

For **permissions**, the rule is always **"most restrictive wins"** — lower scopes cannot broaden permissions granted at higher scopes.

---

## Examples

This repository includes four example packages that demonstrate different use cases. Each example is a **self-contained package** that simulates what a real developer repo looks like.

| Example | What it demonstrates | Complexity |
|---------|---------------------|------------|
| [`minimal-skill`](./examples/minimal-skill/) | Simplest possible ZeroHuman package — one skill, three files | Starter |
| [`acmecrm-specialist`](./examples/acmecrm-specialist/) | Full capability pack — all 8 primitives in a realistic CRM integration | Complete |
| [`support-triage`](./examples/support-triage/) | Multi-agent handoff — ticket routing, specialist delegation, queue ops | Intermediate |
| [`standalone-tool`](./examples/standalone-tool/) | Single tool package — GitHub Issues API integration | Minimal |

### Quick validation

```bash
cd examples/minimal-skill && npx zerohuman validate
cd examples/acmecrm-specialist && npx zerohuman validate
cd examples/support-triage && npx zerohuman validate
cd examples/standalone-tool && npx zerohuman validate
```

---

## Links

- **Full specification:** [zerohuman-v0.1.0.md](./zerohuman-v0.1.0.md)
- **CLI:** [github.com/zerohuman-labs/cli](https://github.com/zerohuman-labs/cli)
- **Registry:** [github.com/zerohuman-labs/registry](https://github.com/zerohuman-labs/registry)
- **Community:** [github.com/zerohuman-labs/community](https://github.com/zerohuman-labs/community)
