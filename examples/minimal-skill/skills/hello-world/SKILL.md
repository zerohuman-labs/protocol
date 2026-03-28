---
name: hello-world
description: A starter skill that greets the user and confirms the agent is operational. Use when asked to verify agent setup or run a basic smoke test.
metadata:
  semver: 0.1.0
---

# Hello World

A minimal skill to confirm the agent runtime is working. Use this as a template for building your own skills.

## When to use

- Agent setup verification
- Smoke testing a new ZeroHuman installation
- Learning the SKILL.md format

## Steps

1. Greet the user by name if available, otherwise use a generic greeting.
2. Confirm which runtime and model you are operating under.
3. List the active capabilities and policies (if any).
4. Report: "ZeroHuman is operational."

## Done when

- The user has received a greeting and operational confirmation.
