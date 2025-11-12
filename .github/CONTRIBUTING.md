# Contributing

Thank you for helping improve this repository. Two high-priority contribution requests:

1. Review control mappings and usage patterns
2. Red-team critique of IaC and patterns for inefficiencies

## How to contribute

- Read relevant files:
  - CONTROL_MAPPING.md files under iac/*
  - Terraform and module code under iac/*
  - Pattern docs and examples under patterns/*
- Prefer small, focused PRs. Link to the exact file(s) you changed and include a short rationale.

## Issue labels to use
- help-wanted
- review
- security
- enhancement
- bug

When opening an issue, include:
- Title prefix: [REVIEW] or [REDTEAM]
- Files or paths affected
- Short reproduction or examples (if applicable)
- Suggested remediation or PR proposal

Suggested issue titles
- [REVIEW] CONTROL_MAPPING: <short description>
- [REDTEAM] IaC inefficiency: <short description>

Suggested templates (copy into new issue or use the `New issue` form)

- Review request example body:
  Please review CONTROL_MAPPING.md under iac/* and the pattern docs under patterns/*. Add comments, propose corrections, and open PRs implementing fixes or clarifications. Reference file paths and use labels `help-wanted` and `review`.

- Red-team critique example body:
  Requesting a red-team style critique of IaC and patterns for inefficiencies (performance, cost, idempotency, maintainability, security). Identify hotspots in iac/* and patterns/*, provide concrete examples and repro steps, and propose PRs or issues to remediate. Prioritize reproducible steps and minimal repros.

## Creating PRs
- Fork the repo and create a branch per change.
- Use clear commit messages and include the issue number in the PR description when applicable.
- Add tests or validation steps if you change IaC or automation.

## Communication
- Prefer GitHub issues and PRs for traceability.
- For larger design discussions, open an issue and use the PR to implement agreed changes.

Thank you for contributing.
