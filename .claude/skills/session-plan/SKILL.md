---
description: Plan an upcoming D&D session for the Saltmarsh campaign — generates a loose, modular session plan file in plans/
---

Create a session plan file at `plans/session-##-short-title.md` (zero-padded number, lowercase hyphenated title).

## Inputs to gather before writing

1. **Most recent session recap** — read the latest file in `docs/sessions-recaps/` to understand where the story left off, what hooks were set, and what the party is chasing.
2. **Character files** — read all files in `docs/characters/pcs/`, `docs/characters/allies/`, and `docs/characters/enemies/` to surface relevant motivations, relationships, and ongoing threads.
3. **User's intent** — ask the user for a short description of what they want this session to accomplish or explore. If they provide it upfront as an argument, use that directly.

## Workflow

1. Read the most recent recap and all character files (can be done in parallel).
2. If the user hasn't provided a direction or theme, ask for one before proceeding.
3. Infer the session number from the recaps (next in sequence). Ask the user for a short title if one isn't obvious from the direction they provided.
4. Write the plan file using the template below. Keep it loose and modular — lay out key elements and options without prescribing a rigid sequence. The plan should help the DM improvise, not constrain them.
5. After writing, mention the file path and briefly summarize the through-line in one or two sentences.

## Guidelines

- **Draw on established fiction.** Reference specific characters, places, and threads already in the campaign files. Don't invent details that contradict or ignore established facts.
- **Each element should be optional.** Mark encounters, NPCs, and beats as things that *could* happen, not a checklist to complete.
- **Keep it practical.** The DM should be able to run from this doc with minimal extra prep.
- **Leave room for players.** Don't over-plan. A few clear entry points and meaningful choices beat a fully scripted session.

---

## Session Plan Template

```markdown
# Session ## Plan — Title

**Picking up from:** [one-sentence recap of where the last session ended]
**Session goal:** [what the DM wants players to walk away having experienced]

---

## Story Beats

Key moments or scenes that could anchor the session. Order is loose — let the players drive which of these happen and when.

### Beat 1 — Title
What this scene is about, why it matters, how it might start.

### Beat 2 — Title
...

---

## Encounters

Potential combat or social encounters. None are required — use what fits.

| Encounter | Type | Notes |
|---|---|---|
| Ambush on the coast road | Combat | ~4 bandits, CR 1/8 each |
| Parley with the sea elf scout | Social | She wants proof before she'll trust the party |

---

## NPCs to Feature

| NPC | Goal this session | Potential hook |
|---|---|---|
| Oleander | Warn the party about the council | Approaches them at the docks at nightfall |

---

## Loot & Rewards

Rewards available this session — award based on what the players actually do.

| Item / Reward | Source | Notes |
|---|---|---|
| Potion of Water Breathing | Hidden chest in the cove | Only findable if they search the cave |

---

## DM Notes

Open questions, things to look up, or prep reminders before the session.

- [ ] 
```
