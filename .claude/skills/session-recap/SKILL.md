Create a new D&D session recap file for the Saltmarsh campaign.

The user will provide a session number and title (or you can infer from context). Use the template below to create the file at `docs/sessions/session-##-short-title.md` (zero-padded number, lowercase hyphenated title).

If the user provides session details (events, combat, loot, XP), fill in the template with that information. Otherwise, create the file with the template structure ready to fill in, and open it for the user.

If the user provide session details, also update the relevant character files with any new information revealed about the characters during the session (e.g. new relationships, backstory details, personality traits, etc.).

If adding a new character ot session, make sure to update mkdocs.yml to include the new file in the navigation and update the index.md for the particular route to link to the new file.

## Session File Template

```markdown
# Session ## — Title

**Location(s):** 
**DM Notes:**

## Summary

2–4 sentence overview of what happened.

## Events

### Scene 1 — Title
What happened, decisions made, outcomes.

### Scene 2 — Title
...

## Combat Encounters

| Encounter | Result | Notable Moments |
|---|---|---|
| vs. Smugglers | Victory | Aelar's nat 20 intimidation |

## Loot & Rewards

| Item | Recipient |
|---|---|
| +1 Shortsword | Bryndis |

## Milestones

- Milestone: Discovered the smuggling operation

## Cliffhanger / Next Session Hook

What are the players chasing going into next session?