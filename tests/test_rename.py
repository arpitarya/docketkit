"""lockmaster was renamed docketkit (2026-11-17). A repository set up under the
old name keeps working: its config, its state, its kit lock and its
.gitattributes block are read, and moved to the new name without losing anything."""
import json
import unittest

from support import ScratchCase, git

from docketkit import config, install
from docketkit.repo import Repo

OLD_TOML = '[merge]\n"work/WORKLOG.md" = "append-newest-first"\n'


class OldName(ScratchCase):
    def test_the_old_config_file_is_read_until_renamed(self):
        (self.root / "lockmaster.toml").write_text('[main]\nbranch = "trunk"\n')
        self.assertEqual(config.path(self.root).name, "lockmaster.toml")
        self.assertEqual(Repo(self.root).main, "trunk")
        (self.root / "docketkit.toml").write_text('[main]\nbranch = "main"\n')
        self.assertEqual(config.path(self.root).name, "docketkit.toml")

    def test_the_old_state_directory_moves_with_its_contents(self):
        old = self.root / ".git" / "lockmaster" / "changes"
        old.mkdir(parents=True)
        (old / "W-1.json").write_text("{}")
        repo = Repo(self.root)
        self.assertEqual(repo.state.name, "docketkit")
        self.assertEqual((repo.state / "changes" / "W-1.json").read_text(), "{}")
        self.assertFalse((self.root / ".git" / "lockmaster").exists())

    def test_install_over_an_old_kit_replaces_its_lock_and_its_renamed_skill(self):
        self.assertEqual(self.cli("install", str(self.root))[0], 0)
        new_lock = self.root / install.LOCK
        lock = json.loads(new_lock.read_text())
        # Make it look like the old name's install: the old lock, the old skill path.
        skill = self.root / ".claude/skills/docket/SKILL.md"
        skill.parent.mkdir(parents=True)
        skill.write_text("old skill\n")
        lock["files"][".claude/skills/docket/SKILL.md"] = install.sha(skill)
        (self.root / install.LEGACY_LOCK).write_text(json.dumps(lock))
        new_lock.unlink()
        code, out, err = self.cli("install", str(self.root))
        self.assertEqual(code, 0, err)
        self.assertTrue(new_lock.is_file())
        self.assertFalse((self.root / install.LEGACY_LOCK).exists())
        self.assertFalse(skill.exists())  # untouched, so the install that wrote it removes it
        self.assertTrue((self.root / ".claude/skills/inbox-review/SKILL.md").is_file())

    def test_drivers_replace_the_old_block_rather_than_add_a_second(self):
        (self.root / "docketkit.toml").write_text(OLD_TOML)
        attrs = self.root / ".gitattributes"
        attrs.write_text("*.png binary\n\n# lockmaster:begin — old\nwork/WORKLOG.md merge=lockmaster-append-newest-first\n"
                         "# lockmaster:end\n")
        self.cli("drivers")
        text = attrs.read_text()
        self.assertNotIn("lockmaster", text)
        self.assertEqual(text.count("docketkit:begin"), 1)
        self.assertTrue(text.startswith("*.png binary\n"))

    def test_both_commands_are_declared(self):
        from support import ROOT
        text = (ROOT / "pyproject.toml").read_text()
        self.assertIn('docketkit = "docketkit.cli:main"', text)
        self.assertIn('dk = "docketkit.cli:main"', text)


if __name__ == "__main__":
    unittest.main()
