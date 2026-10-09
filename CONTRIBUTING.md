# Contributing

Thanks for considering a contribution to Project Advisor! The goal is not to add the most features, but to help people make **better, lighter-weight engineering decisions**.

## Before you open a pull request

1. For substantial changes, open an issue describing the actual project/onboarding problem and the smallest proposed improvement.
2. Keep the Skill **read-only by default** and require explicit approval for modifications, installations, commands with side effects, and deployments.
3. Preserve the distinction between evidence, assumptions, and unknowns. Avoid instructions that automatically rate employees or claim regulatory certification.
4. Prefer concise guidance and small examples rather than copying third-party Skill packs. Do **not** submit secrets, company source code, private project documents, personal information, or copyrighted material without permission.
5. Run `python3 -m unittest discover -s tests -v` (Python 3.9+, standard library only).
6. Explain user-visible changes in the PR and add a line to `CHANGELOG.md` if relevant.

## Review criteria

- Does the change solve a concrete developer or team problem?
- Does it avoid unnecessary new rituals, skills, prompts, and dependencies?
- Does it keep users in control and protect sensitive repository content?
- Could a newcomer understand when **not** to use it?
- Does the relevant example or automated validation still pass?

## Scope and licensing

Unless stated otherwise, contributions are submitted under the repository's MIT License. You must have rights to contribute the content. The named external Skill projects are references, not dependencies or endorsed collaborators.

Please follow our [Code of Conduct](CODE_OF_CONDUCT.md). For security issues, see [SECURITY.md](SECURITY.md) instead of creating public issues.
