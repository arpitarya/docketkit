---
type: Handoff
name: W-175
description: "Worktrees left by session 641d8f75-a5c6-4dfb-8130-fcf5cc1675e0 would lose data if removed"
item: W-175
filed: 2026-11-09
filed_by: "now-ledger.py (Claude Code)"
updated: 2026-11-09
updated_by: "now-ledger.py (Claude Code)"
ball: arpit
---

# W-175 — Worktrees left by session 641d8f75-a5c6-4dfb-8130-fcf5cc1675e0 would lose data if removed

## At a glance

| what | state |
|---|---|
| Worktrees left by session 641d8f75-a5c6-4dfb-8130-fcf5cc1675e0 would lose data if removed | ⏳ |

Filed at the end of session `641d8f75-a5c6-4dfb-8130-fcf5cc1675e0`.

These worktrees were left untouched. Rule per worktree: **keep** (merge it or commit the files; the next cleanup removes it) or **drop** (only then may an agent force the removal and delete the unmerged branch).

- `/Users/arpitarya/my_programs/lockmaster/.claude/worktrees/W-19` — removed /Users/arpitarya/my_programs/lockmaster/.claude/worktrees/W-19; git refused to delete branch lm/W-19: warning: not deleting branch 'lm/W-19' that is not yet merged to
         'refs/remotes/origin/lm/W-19', even though it is merged to HEAD
error: the branch 'lm/W-19' is not fully merged
hint: If you are sure you want to delete it, run 'git branch -D lm/W-19'
hint: Disable this message with "git config set advice.forceDeleteBranch false"

## Record affected

No SR affected — the rule is SR-WORK-CLEANUP.
