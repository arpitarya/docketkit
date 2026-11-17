---
type: Standing Record
kind: process
name: SR-WORK-LANDING
title: "SR-WORK-LANDING (0063) — a change reaches main only through docketkit"
description: "No agent session commits to main; docketkit lands each change after this repository's checks. The four landing hooks are docketkit's kit, specified in docketkit's own records."
status: accepted
date: 2026-11-08
feature: landing on main
owns:
  - .claude/hooks/claim-guard.py
  - .claude/hooks/block-main.py
  - .claude/hooks/auto-land.py
  - .claude/hooks/work-files.py
laws: [L0]
timestamp: 2026-11-08T12:00:00Z
content_sha: ""
---

# SR-WORK-LANDING — a change reaches main only through docketkit

## §1 — For humans

**`main` moves only through docketkit.** A session claims the paths it will
change, works in its own worktree, and docketkit lands the change after the
checks in `docketkit.toml` — one change at a time, as a plain git commit. A
surface that cannot commit (the Cowork bridge) hands its edits to the next
Claude Code session with `docketkit save`. How it works is docketkit's, not
this repository's: its specification is SR-ARCHITECTURE, in the docketkit
repository.

```mermaid
flowchart LR
    S["a session's change"] -->|claimed paths| W["its worktree"]
    W -->|end of every turn| L["docketkit lands it"]
    C["Cowork"] -->|docketkit save| H["handoff"] --> L
    L -->|checks pass| M["main"]
```

<details>
<summary><b>ASCII twin</b></summary>

```text
   a session's change --claimed paths--> its worktree --end of every turn--> docketkit lands it
   Cowork --docketkit save--> handoff --> docketkit lands it
   docketkit lands it --checks pass--> main
```

</details>

---

## §2 — For agents

### Context

Several sessions — Claude Code and Cowork, often at once — change this
repository. Commits made straight to `main` by each of them collide, and work
is lost or landed half-checked. docketkit serialises the landings.

### Decision

1. **No agent session commits or pushes to `main`.** The kit's `block-main.py`
   refuses it.
2. **Work is a change:** `docketkit start <item> --paths <path> …` claims the
   paths and makes a worktree; `claim-guard.py` warns on a write outside the
   claim; `docketkit submit -m "<item>: …"` lands it and removes the worktree.
3. **Nothing waits for `submit`:** the kit's `auto-land.py` lands what a change
   holds at the end of every turn, and lands what Cowork handed over.
4. **From Cowork, never commit:** `docketkit save -m "<item>: …" <path> …`
   lands the edits or hands them off. The `landing` skill
   (`.claude/skills/landing/`) has the rest.
5. **The four hooks this record owns are docketkit's kit.** They are changed
   in the docketkit repository's `kit/` and reinstalled with
   `docketkit install .`; an edit made here is reported by `docketkit doctor`
   and overwritten by the next install. `work-files.py` reminds a session, once
   at `Stop`, that it changed files but no work file (docketkit's law L10).

### Consequences

- This record changes when docketkit's landing contract changes, never because
  a hook's code moved: the code's specification lives in docketkit.
- What a landing checks is this repository's own, in `docketkit.toml`.

### Alternatives considered

- Restating docketkit's architecture here — rejected under L0: one home per
  rule, and that home is in the docketkit repository.

### Reference (required)

- `.claude/docketkit.lock` — the kit version these hooks were installed from.
- `docketkit.toml` — this repository's checks and merge drivers.

### Veto condition

**Reopen this decision if:** `main` carries a commit no docketkit landing
made, or a kit hook differs from the version pinned in `.claude/docketkit.lock`.

**How to check it:** `docketkit doctor` reports no changed kit file, and
`docketkit queue` accounts for every recent landing.

---

## References

**Records** — [SR-LAW-0](0002_LAW-0-authority.md) · [SR-WORK-SESSION](0054_WORK-session.md) · [SR-WORK-OWNERSHIP](0058_WORK-ownership.md)

**Code** — `.claude/hooks/claim-guard.py` · `.claude/hooks/block-main.py` · `.claude/hooks/auto-land.py` · `.claude/hooks/work-files.py`
