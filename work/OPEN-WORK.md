---
type: Queue
description: "The single live work queue, three lanes, plus the Blocked-on-the-decider inbox. The list only — its rules live in the record below."
governed_by: SR-WORK-OPEN-QUEUE
governed_by_path: records/0051_WORK-open-queue.md
---

# OPEN-WORK — what is still open

**This file is the LIST, plus the legend below.** Everything else — what the
queue is, an item's lifecycle, the shape of a row, ball precedence, ordering,
how the inbox works, and what every session owes — is stated once in
**[SR-WORK-OPEN-QUEUE](../records/0051_WORK-open-queue.md)** and is not repeated
here. Read that record before changing anything below it.

**A ball on every row, always one:** 🔴 blocked on the decider, directly or through another item · 🟣 gated on a named date, directly or through another item · 🟡 waiting on another item, named right after the id — `waits on **W-mm**`, or `**<project> W-mm**` for another project's · 🟢 no blockers.
**Optional, after the ball:** 🧨 broken or getting worse · 🔺 do first (the decider only). Full legend: [SR-WORK-OPEN-QUEUE](../records/0051_WORK-open-queue.md) rules 20–34.

---

## Blocked on the decider

| what the decider decides | filed |
|---|---|
| 🔴 **W-175** — keep or drop each worktree in [the item](open/W-175-session-cleanup.md): removing it would lose data (SR-WORK-CLEANUP decision 3) | 2026-11-09 |
| ↳ **blocks:** nothing else in the queue | |
| 🔴 **W-21** — finish the rename to docketkit: reinstall the package on the Mac, rename the GitHub repo and the folder, add `docketkit`'s trusted publishers ([the item](open/W-21-rename-to-docketkit.md)) | 2026-11-17 |
| ↳ **blocks:** W-17 (publishing is now `docketkit`'s) | |
| 🔴 **Publish from a tag; rule the repo's visibility** — add the trusted publishers and the two GitHub environments (CONTRIBUTING.md §Releasing); GitHub shows the repo public, decision 17 says private until 0.1.0 ([W-17](open/W-17-release-from-a-tag.md)) | 2026-11-08 |
| ↳ **blocks:** nothing else in the queue | |

---

## Open items (4)

### build (3)

🔴 **W-21** `arpit` The rename to docketkit reaches the machine, GitHub, PyPI and the other four repositories. Filed by Arpit (Cowork). [detail](open/W-21-rename-to-docketkit.md)

🔴 **W-175** `arpit` Worktrees left by session 641d8f75-a5c6-4dfb-8130-fcf5cc1675e0 would lose data if removed. Filed by now-ledger.py (Claude Code). [detail](open/W-175-session-cleanup.md)

🔴 **W-17** `arpit` Releases publish from a tag: the trusted publishers and environments, then the local tags `v0.0.1`–`v0.0.3` pushed; and the repository's visibility ruled. Filed by Claude Code (from W-08). [detail](open/W-17-release-from-a-tag.md)


### testing (0)

### record update (0)

### research (1)

🟢 **W-20** `cowork` Rulings owed to the decider stay in item files, never in the inbox (**codelaw W-139**, **codelaw W-174**, **codelaw W-172**, 11-09): why, and a check that refuses it — not-yet-blocking ones too. Filed by Arpit (Cowork). [detail](open/W-20-decider-rulings-reach-the-inbox.md)

---
