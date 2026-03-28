# GitHub Issues Tool

A standalone ZeroHuman tool package for interacting with the GitHub Issues API.

## What this demonstrates

- A **single-tool package** — not everything needs to be a full capability pack
- **API key auth** — simpler than OAuth2, using a Bearer token from a secret store
- **No approval gate** — read/write operations are pre-approved (suitable for developer tooling)
- **Minimal manifest** — `package_type: "tool"` with one object

## Structure

```
standalone-tool/
├── zerohuman.yaml
├── README.md
└── tools/
    └── github-issues/
        └── tool.yaml
```

## Supported operations

| Operation | Description |
|-----------|-------------|
| `list_issues` | List issues in a repository (with optional filters) |
| `get_issue` | Get a single issue by number |
| `create_issue` | Create a new issue with title, body, and labels |
| `add_comment` | Add a comment to an existing issue |
| `close_issue` | Close an issue |

## Install

```bash
npx zerohuman add example-org/zerohuman-github-issues
```

## Validate

```bash
npx zerohuman validate
```
