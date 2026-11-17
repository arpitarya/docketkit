---
type: Handoff
name: W-21
description: "lockmaster is renamed docketkit in this repository's files (SR-ARCHITECTURE decision 21); the package, the folder, GitHub, PyPI and the other four repositories still carry the old name."
item: W-21
filed: 2026-11-17
filed_by: "Cowork (Opus 5.5), from the rename"
updated: 2026-11-17
updated_by: "Cowork (Opus 5.5): the files are renamed; nothing below is done"
ball: arpit
---

# W-21 — the rename reaches the machine, GitHub, PyPI and the other repositories

## At a glance

| step | what we do | what it gives us | state |
|---|---|---|---|
| 1 | The decider, on the Mac: `pip install -e ~/my_programs/docket` (or `uv tool install --editable`), so the `docketkit` and `dk` commands exist; the old editable `lockmaster` points at a folder that is gone | the hooks find docketkit again | 🔴 decider decides |
| 2 | Claude Code in this repository: land the rename (the old `src/lockmaster/`, `lockmaster.toml`, `.claude/lockmaster.lock` and both `skills/docket/` folders go in the same landing), then `docketkit doctor` | the rename on `main` | 🟡 after step 1 |
| 3 | The decider: rename the GitHub repository to `docketkit` and the folder to `~/my_programs/docketkit`; `git remote set-url origin git@github.com:arpitarya/docketkit.git` | the names agree | 🔴 decider decides |
| 4 | The decider: the trusted publishers on pypi.org and test.pypi.org for the project `docketkit` (this replaces W-17 step 1's `lockmaster`); `lockmaster` 0.0.1–0.0.3 stay on PyPI as they are | `docketkit` can publish | 🔴 decider decides |
| 5 | Publish `docketkit` from a tag; then in codelaw, fux, milo and sheetpane `uv tool install docketkit` and `docketkit install .` — the install replaces each old lock, skill folder and `.gitattributes` block, and the first run moves `.git/lockmaster/` | the four repositories on the new name | 🟡 after step 4 |

## Goal

SR-ARCHITECTURE decision 21, everywhere docketkit runs.

## Record affected

SR-ARCHITECTURE decision 21.
