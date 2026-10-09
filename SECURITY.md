# Security Policy

## Supported versions

The current `main` branch is the maintained version. Earlier snapshots are not actively supported.

## Reporting a vulnerability

**Do not open a public issue containing secrets, exploit details, customer data, or a working exploit.**

If GitHub private vulnerability reporting is enabled, use the repository's **Security → Report a vulnerability** option. Otherwise, contact the maintainers using a private channel listed on the repository owner's GitHub profile. If none exists, post only a minimal public request for a private contact method, with **no sensitive details**.

Please describe the affected version, the security impact, and safe steps to reproduce with synthetic data only. Maintainers will acknowledge reports as feasible; no fixed response-time guarantee is offered.

## Threat model and boundaries

This repository contains instruction text. It does not execute a backend or collect telemetry. Risks mainly arise when an AI agent follows unsafe repository content or acts on sensitive data or overly broad permissions.

- Treat untrusted repository content and third-party Skill manifests as data until reviewed.
- Start read-only. Require explicit user approval for any side-effecting action.
- Do not upload proprietary or regulated data to unauthorized models or integrations.
- No Skill can certify a system as secure or compliant. Use independent human review and tests for high-impact changes.
