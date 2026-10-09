# Project Advisor Skill

[English](README.md) | [简体中文](README.zh-CN.md)

**一个默认只读的 Codex 项目诊断与工程协作顾问 Skill。** 适合新建项目、接手陌生代码库，或团队人数和分工发生变化的情况。

它先了解项目证据、团队构成和实际风险，然后建议**最少且值得投入的开发流程**。它可以参考 Matt Pocock Skills、Poteto / Pstack、Addy Osmani Agent Skills，但这些**都不是依赖项**，也不会自动安装。

> **状态：v0.1.0 实验版。** 这是独立社区项目，不代表上述作者或 OpenAI 的官方立场或背书。请人工核查推荐内容后，再修改真实项目。

## 主要能力

- 判断新项目和已有项目的不同需求，优先尊重已有约定；
- 从 README、项目配置、测试和 CI 等**被授权**的信息中收集证据；
- 根据产品阶段、交付风险、人员配置和职责划分，判断协作瓶颈；
- 最多建议三个适用的工作流程 / Skill，并指出**暂时不应引入**的流程；
- 提供决策、实现、验证、上线等角色的职责建议和轻量质量门禁；
- 设计两周试运行计划，便于检验建议是否真正减少返工；
- **默认只读**，不会未经授权修改文件、安装 Skill、提交代码或部署。

## 在 Codex 项目中安装

把以下目录拷贝到你要分析的项目中：

```text
<你的项目>/
└── .agents/
    └── skills/
        └── project-advisor/
            └── SKILL.md
```

或者在解压的仓库目录下运行：

```bash
mkdir -p /path/to/your-project/.agents/skills/project-advisor
cp .agents/skills/project-advisor/SKILL.md /path/to/your-project/.agents/skills/project-advisor/SKILL.md
```

然后在 Codex 中明确调用：

```text
Use $project-advisor to assess this unfamiliar repository in read-only mode.
First inspect existing conventions. Recommend the smallest useful workflows
and team responsibilities. Do not modify any files or install anything.
```

如果你是个人游戏项目，也可以使用：

```text
Use $project-advisor. I'm building a solo AI narrative game prototype.
Prioritize iteration speed, smoke tests, and a two-week pilot.
Tell me which heavyweight practices I should NOT adopt.
```

你可以先填写 [项目与团队简报模板](examples/project-brief.md)；[示例诊断报告](examples/sample-assessment.md) 展示输出形式（内容完全虚构）。

## 使用与限制

Skill 的建议应明确区分**证据、推断和未知**。不要只凭岗位头衔评价同事能力；不要把 AI 建议当作正式安全审计或监管合规证明。对公司仓库、客户数据、医疗记录、密钥等敏感材料，先确认是否获准交给对应的 AI 工具。未经许可不要上传或分享。

## 开源协作

欢迎 Issue 与 PR。提交前阅读 [CONTRIBUTING.md](CONTRIBUTING.md)、[行为准则](CODE_OF_CONDUCT.md) 和 [安全政策](SECURITY.md)。请维持“默认只读、最小流程、证据优先、人工审批”的设计原则。

本项目是**纯指令型 Skill**，没有后台服务、遥测或数据收集功能。

## 第三方项目

- [Matt Pocock — Skills](https://github.com/mattpocock/skills)
- [Poteto / Pstack](https://github.com/cursor/plugins/tree/main/pstack)
- [Addy Osmani — Agent Skills](https://github.com/addyosmani/agent-skills)

这些仅作为可选参考，本项目没有打包或复制其代码与 Skill；相关商标和许可证归各自权利人。

## 验证

使用 Python 3.9 或更新版本运行打包检查（仅依赖标准库）：

```bash
python3 -m unittest discover -s tests -v
```

检查覆盖 Skill 元数据、必要文档、本地 Markdown 链接、Issue 模板元数据，以及 CI 权限和 Action 版本固定。这些检查不验证模型实际行为，也不构成企业级安全认证。

## 许可证

[MIT](LICENSE)。
