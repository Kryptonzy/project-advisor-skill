# Project Advisor Skill

[English](README.md) | [简体中文](README.zh-CN.md)

![Version](https://img.shields.io/badge/version-0.1.0-blue) ![License: MIT](https://img.shields.io/badge/license-MIT-green)

A lightweight, **read-only by default** project onboarding and engineering-workflow advisor for Codex. It inspects a new or unfamiliar codebase, considers your team's size and roles, and recommends the **minimum useful** development practices, checks, and collaboration rules.

It can suggest practices from Matt Pocock's Skills, Poteto/Pstack, and Addy Osmani's Agent Skills **when they are relevant and available**. None of those packages is required for Project Advisor to run.

> **Status:** v0.1.0 experimental. This is an independent community skill, **not** an official extension of or endorsement by Matt Pocock, Poteto, Addy Osmani, or OpenAI. Recommendations are advisory; review them before changing a real project.

## What it does

- Identifies whether the repository is greenfield or already has working conventions.
- Reviews project documentation, relevant config, tests, and CI (only to the extent permitted).
- Separates verified observations from assumptions and unknowns.
- Considers team makeup, ownership, experience, compliance risks, release requirements, and time constraints.
- Recommends up to three useful specialized workflows or Skills, explicitly stating what **not** to add yet.
- Suggests an appropriately lightweight team rhythm, decision ownership, verification gates, and a two-week pilot.
- **Does not** silently install Skills, edit files, make commits, or deploy anything.

## Install in a Codex project

Copy the included skill folder into the project where you want to use it:

```text
<your-project>/
└── .agents/
    └── skills/
        └── project-advisor/
            └── SKILL.md
```

For example, from a local checkout of this repository:

```bash
mkdir -p /path/to/your-project/.agents/skills/project-advisor
cp .agents/skills/project-advisor/SKILL.md /path/to/your-project/.agents/skills/project-advisor/SKILL.md
```

Open the target project in Codex and explicitly invoke the Skill. If your Codex environment has different discovery or skill configuration rules, consult the documentation for that environment.

## Example prompts

You can also start with the [project brief template](examples/project-brief.md), which helps the advisor understand the team without guessing.

```text
Use $project-advisor to assess this unfamiliar repository in read-only mode.
First review its existing conventions, then recommend the smallest useful
engineering workflows and team collaboration practices. Do not modify anything.
```

```text
Use $project-advisor. We have one PM, two junior full-stack engineers, and one
part-time QA tester. This is a multi-tenant compliance AI SaaS. Recommend clear
owners, necessary quality gates, and at most three relevant skills. Distinguish
confirmed installed skills from suggestions.
```

```text
Use $project-advisor. I'm building a solo AI narrative game prototype.
Prioritize iteration speed, a simple verification loop, and a realistic two-week
pilot. Tell me which heavy processes I should avoid.
```

## Expected first-run output

See the [illustrative assessment](examples/sample-assessment.md). All organizations and project details in that example are fictitious.

1. Project snapshot, evidence, and key unknowns.
2. Top three engineering or coordination bottlenecks.
3. Up to three recommended Skills/practices with trade-offs and availability status.
4. Team responsibility map: product decisions, architecture, review, releases.
5. Project-specific Definition of Done.
6. Two-week pilot with one success metric and a stop condition.
7. Explicit approval checkpoint before writing or installing anything.

## Safety

Default behavior is read-only. Do not run the Skill against company repositories, confidential client material, or regulated data unless you have permission to use the selected AI tooling with that information. Inspect proposed commands, file access, external integrations, code changes, and security claims independently. AI-generated assessments are **not** formal compliance or security audits.

## References (independent projects)

- [Matt Pocock — Skills](https://github.com/mattpocock/skills)
- [Poteto/Pstack](https://github.com/cursor/plugins/tree/main/pstack)
- [Addy Osmani — Agent Skills](https://github.com/addyosmani/agent-skills)

Project Advisor describes these as optional reference workflows; it does **not** vendor their code or require their installation.

## Contributing and community

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md), the [Code of Conduct](CODE_OF_CONDUCT.md), and the [Security Policy](SECURITY.md). You can report a bug or suggest an improvement with a GitHub issue. Changes should preserve the read-only default and the distinction between evidence and assumptions.

This is an **instruction-only Skill**, not an autonomous installer or a production-security certification. There is no hosted service, data collection, or telemetry in this repository.

## Validation

Run the packaging checks with Python 3.9 or newer (standard library only):

```bash
python3 -m unittest discover -s tests -v
```

The checks cover the Skill manifest, required documentation, local Markdown links, Issue template metadata, and CI permissions and action pins. They do not evaluate model behavior or provide enterprise security certification.

## License

MIT — see [LICENSE](LICENSE). External projects linked above are independent; their own licenses and trademarks apply. No third-party Skills are redistributed here.
