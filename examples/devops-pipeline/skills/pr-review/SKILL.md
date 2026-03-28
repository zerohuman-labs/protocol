---
name: pr-review
description: Review a pull request for code quality, test coverage, and CI status. Use when a PR is opened or updated and needs automated review feedback.
metadata:
  semver: 0.3.0
---

# PR Review Workflow

Analyze a pull request and provide structured review feedback based on CI results, code changes, and test coverage.

## Inputs needed

- PR number and repository
- CI run status (pass/fail/pending)
- Changed files list

## Steps

1. **Fetch PR details.** Use the `github_ci` tool to get check run results and CI status.
2. **Analyze changes.** Review the diff summary for:
   - Breaking changes or API modifications
   - Missing test coverage for new code paths
   - Security-sensitive changes (auth, secrets, network)
3. **Check CI status.** If CI is failing:
   - Fetch run logs to identify the failure
   - Categorize: test failure, lint error, build error, flaky test
4. **Produce review.** Write a structured review with:
   - Summary of changes
   - CI status and any failures
   - Recommendations (approve, request changes, or needs discussion)
5. **Emit artifacts.**
   - `pr_review_summary` — structured review with recommendations
   - `ci_status_report` — CI results snapshot

## Done when

- Review is posted as an internal note AND all artifacts are emitted.
