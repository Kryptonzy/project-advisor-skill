"""Lightweight structural checks for the instruction-only Codex Skill.

These tests do not assert that an AI model will follow the instructions; they
only catch packaging mistakes before release.
"""

from pathlib import Path
import re
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / '.agents' / 'skills' / 'project-advisor' / 'SKILL.md'


class SkillManifestTest(unittest.TestCase):
    def test_skill_exists_and_is_unique(self):
        self.assertTrue(SKILL.is_file())
        matches = list(ROOT.rglob('SKILL.md'))
        self.assertEqual(matches, [SKILL])

    def test_frontmatter_has_name_and_description(self):
        content = SKILL.read_text(encoding='utf-8')
        self.assertTrue(content.startswith('---\n'))
        parts = content.split('---\n', 2)
        self.assertGreaterEqual(len(parts), 3)
        frontmatter = parts[1]
        fields = dict(re.findall(r'^(name|description):\s*(.+)$', frontmatter, flags=re.M))
        self.assertEqual(fields.get('name'), 'project-advisor')
        self.assertTrue(40 <= len(fields.get('description', '')) <= 1024)

    def test_read_only_and_human_approval_are_explicit(self):
        content = SKILL.read_text(encoding='utf-8').lower()
        self.assertIn('read-only', content)
        self.assertIn('explicit user approval', content)
        self.assertIn('unknown', content)
        self.assertIn('at most 3', content)

    def test_documentation_and_license(self):
        for file in ('README.md', 'README.zh-CN.md', 'LICENSE', 'CONTRIBUTING.md',
                     'CODE_OF_CONDUCT.md', 'SECURITY.md', 'CHANGELOG.md',
                     'examples/project-brief.md', 'examples/sample-assessment.md'):
            with self.subTest(file=file):
                self.assertTrue((ROOT / file).is_file())

    def test_markdown_local_links_resolve(self):
        for document in sorted(ROOT.rglob('*.md')):
            if '.git' in document.relative_to(ROOT).parts:
                continue
            content = document.read_text(encoding='utf-8')
            for link in re.findall(r'!?\[[^\]]*\]\(([^\s)]+)\)', content):
                target = urlsplit(link)
                if target.scheme or target.netloc or not target.path:
                    continue
                with self.subTest(document=document.relative_to(ROOT), link=link):
                    path = (document.parent / unquote(target.path)).resolve()
                    self.assertTrue(path.is_relative_to(ROOT), 'Link leaves the repository')
                    self.assertTrue(path.exists(), 'Missing local link target')

    def test_markdown_issue_templates_have_required_metadata(self):
        templates = sorted((ROOT / '.github' / 'ISSUE_TEMPLATE').glob('*.md'))
        self.assertTrue(templates)
        for template in templates:
            with self.subTest(template=template.name):
                content = template.read_text(encoding='utf-8')
                self.assertTrue(content.startswith('---\n'))
                frontmatter = content.split('---\n', 2)[1]
                for field in ('name', 'about'):
                    self.assertRegex(frontmatter, rf'(?m)^{field}:\s*\S.+$')

    def test_ci_permissions_and_action_pins(self):
        workflow = (ROOT / '.github' / 'workflows' / 'validate.yml').read_text(encoding='utf-8')
        self.assertRegex(workflow, r'(?m)^permissions:\n  contents: read\n')
        self.assertNotIn('pull_request_target:', workflow)
        actions = re.findall(r'(?m)^\s*uses:\s*(\S+)', workflow)
        self.assertTrue(actions)
        for action in actions:
            with self.subTest(action=action):
                self.assertRegex(action, r'^[\w./-]+@[0-9a-f]{40}$')


if __name__ == '__main__':
    unittest.main()
