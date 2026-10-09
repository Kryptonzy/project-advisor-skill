# Illustrative assessment — fictitious small-team SaaS

> **Example only.** No actual codebase was inspected. All observations below are hypothetical and should NOT be reported as verified facts in a real assessment.

## Snapshot

- Product: multi-tenant B2B SaaS (hypothetical)
- Stage: MVP with pilot customers (user-supplied assumption)
- Team: 1 PM, 2 full-stack developers, part-time QA (user-supplied assumption)
- Known evidence: `README.md` documents install steps; CI configuration has not been inspected (hypothetical)
- Unknowns: tenant isolation test coverage, incident response, deployment ownership

## Top bottlenecks

1. **Verification** — tenant boundaries are high impact; whether tests exist is unknown. Confirm before changing process.
2. **Decision ownership** — release approval is unassigned in the hypothetical team map.
3. **Scope ambiguity** — next pilot milestone needs a concrete acceptance test.

## Recommended minimum workflow

| Need | Evidence | Recommendation | Cost / overhead | Owner | Verification |
| --- | --- | --- | --- | --- | --- |
| Scope | Broad milestone description (assumption) | One-page acceptance criteria before coding | 20–30 minutes | PM + developer | Both can explain done/not-done |
| Tenant separation | Regulated customer context (assumption) | Add independent tenant-isolation tests and review | Moderate | Developer + reviewer | Negative tests in CI |
| Release | Release owner missing (assumption) | Assign a release approver and rollback instruction | Low | Team lead | Documented dry run |

**Optional skill references:** One requirements-clarification skill (if installed); one security testing practice. Do **not** install full workflow packs, add daily ceremonies, or auto-merge changes yet.

## Two-week pilot

- Representative task: add an audit-log filter that never leaks records across tenants.
- Success metric: acceptance tests and tenant-isolation negative tests pass in CI.
- Stop condition: process overhead exceeds its benefits or introduces new permissions/security risks.
- Review date: two weeks after pilot starts.

## Approval

Only report recommendations now. Do not change repo files, installs, team permissions, CI, or deployments until the owner approves a concrete proposal.
