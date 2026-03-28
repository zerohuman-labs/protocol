# Minimal Skill Example

The simplest possible ZeroHuman package — one skill, three files.

## Structure

```
minimal-skill/
├── zerohuman.yaml
├── README.md
└── skills/
    └── hello-world/
        └── SKILL.md
```

## What this demonstrates

- The minimum required `zerohuman.yaml` manifest for a single-skill package
- The `SKILL.md` format: YAML frontmatter (name, description) + markdown procedures
- Progressive disclosure: agents load metadata first, full instructions only when activated

## Install

```bash
npx zerohuman add zerohuman-labs/protocol --path examples/minimal-skill
```

## Validate

```bash
npx zerohuman validate
```
