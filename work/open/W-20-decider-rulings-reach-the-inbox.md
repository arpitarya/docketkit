---
type: Handoff
name: W-20
description: "Rulings owed to the decider get written into item files and never reach the Blocked-on-the-decider inbox — research why, using three codelaw cases from 2026-11-09, and propose a check that refuses a landing until each one is an inbox row, including decisions that are not blocking yet."
item: W-20
filed: 2026-11-09
filed_by: "Arpit (voice, via Cowork, Opus 5.5)"
updated: 2026-11-09
updated_by: "Cowork (Opus 5.5): filed from the codelaw docket walk-through"
ball: cowork
---

# W-20 — rulings owed to the decider reach the inbox, every time

**Model:** Cowork (research, SR-WORK-OPEN-QUEUE rule 37a).

## At a glance

| step | what we do | what it gives us | state |
|---|---|---|---|
| 1 | Read the three codelaw cases below. For each, find where the decision was written, what words it used, and why the inbox check let it through | the cause, from the files, not a guess | ⏳ |
| 2 | Read every repository lockmaster is installed in for the same pattern: decisions for the decider in `work/open/*.md` with no inbox row naming the item | how common it is | ⏳ |
| 3 | Propose 2–3 designs for a check: what counts as "owed to the decider" in an item file, where the check runs (the inbox script, the guard hook, a pre-land check in lockmaster), and how a decision that is **not blocking yet** is filed | a shape the decider can pick | ⏳ |
| 4 | The decider picks a design | a build item | 🔴 decider decides, after step 3 |

## Why this exists

Arpit, 2026-11-09 (voice, walking through codelaw's queue): *"If there is a ruling pending on me, why isn't it in block status?"* · *"We need a work item for lock master so that this never happens again."* · then, on the second case: *"Again, had a work item for lock master to do the research for the previous item as well as this item."* · on decisions marked "not blocking": *"It isn't non-blocking, but it'll become non-blocking at some point of time."* — read with him as *not blocking today, blocking later*, which must still reach the inbox.

## The cases (codelaw, 2026-11-09)

1. **codelaw W-139** — Ruff's rows by class and the Airflow data package. The item file's table for the fourth Ruff round proposed a class per row "so one pass of the decider closes them", and *Slice 28* put the `data-airflow` package "to the decider". Neither was in the inbox, which read *empty since 2026-11-08*, when Arpit was shown the queue at 13:20 IST. A concurrent session filed both at 13:28 (codelaw `4407cd3a`, `87247294`, "go to the inbox (21a)") — after the fact, by hand.
2. **codelaw W-174** — SR-PY-INFERENCE decision 8. The item's *Blockers* and its queue row both said *"For the decider (not blocking)"*: a decision that blocks the cross-file rows once the in-file rows are built. Never filed. Filed by this session on 2026-11-09.
3. **codelaw W-172** — a budget that optimisation is not expected to meet. The item said plainly that no lever left is likely to close `peak_memory_10k`'s ~14 MiB, and L8 says a budget is never loosened. That is a fork only the decider can settle, and it was not in the inbox: Arpit settled it when it was read to him (*amend L8*). Filed by this session on 2026-11-09.

## Questions the research answers

- Why an agent writes "for the decider" in an item and not in the inbox: does a rule allow it (a "not blocking" exemption read into rules 21, 42–45), is the cost of a row too high, or does the agent not see the decision as one?
- What markers in an item file mean "owed to the decider" — `🔴 decider decides` in an at-a-glance table, "for the decider", "to the decider", "the decider's call", a `**for the decider:**` label — and how many false positives a scan of them gives across the installed repositories.
- How a not-blocking-yet decision is filed: an inbox row with the point it starts blocking (`blocks from: …`), or a separate list — and rule 44 (an inbox row is always 🔴) against it.
- Where the check lives so every repository gets it: `scripts/check-open-work-inbox.py`, `kit/claude/hooks/guard-open-work-inbox.sh`, or a land-time check in lockmaster itself (L10: the work files are current wherever lockmaster is used).
- Whether a fork an item calls unlikely to close under a law (case 3) can be detected at all, or stays a judgment rule.

## Record affected

SR-WORK-OPEN-QUEUE (§F, the inbox) and SR-WORK-BLOCKERS — named now, changed only after the decider picks; the kit's copies in `kit/scaffold/records/` with them.
