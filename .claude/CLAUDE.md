# Saltmarsh D&D Campaign

No application code to speak of — this is a Docusaurus site that publishes a D&D campaign wiki. The real content is markdown.

## Campaign Notes

- **System:** D&D 5e
- **Setting:** Ghosts of Saltmarsh (official module + heavy homebrew)
- **Town:** Saltmarsh — fishing town on the Azure Sea, complicated relationships with smugglers, sea elves, and marsh lizardfolk
- **PCs:** Lok, Short Stacks, Snacks. Toro died in Session 10 (killed by Xindrad the Fierce) — don't include him in plans, encounters, or party rosters. His grave at the cottage is a live emotional thread.

## Workspace Structure

- `docs/characters/` — `pcs/`, `allies/`, `enemies/`. One file per character.
- `docs/sessions-recaps/` — one file per session, `session-##-short-title.md`
- `planning/upcoming-sessions/` — session plans, `session-##-short-title.md`
- `planning/battle-maps/`, `planning/tokens/`, `planning/narrative-images/` — image assets
- `build/` — generated. Never edit by hand.

**Published vs. DM-only:** everything under `docs/` is built into the public site and players may read it. `planning/` is DM-only. Never put an unrevealed twist, a villain's real motive, or an upcoming encounter into `docs/`. When a secret becomes known in play, it can move into `docs/` in the recap.

## Writing Style — The Most Important Rule

**Bare bones. Bullet points. Always.**

The DM improvises at the table and does not want details pre-fleshed. Generated content is scaffolding, not a script.

- Bullets over paragraphs everywhere except session recaps (see below).
- Short fragments, not full sentences, wherever a fragment carries the meaning.
- Enough for the DM to know the general story and run it cold — nothing more.
- **Emphasize the paths the PCs could take.** Branches are the point; flavor text is not.
- Leave hooks, not answers. An open thread the DM can resolve at the table beats a resolved detail.
- Don't invent minor NPC names, shop inventories, exact dialogue, room dressing, or DC-by-DC breakdowns unless asked.
- Reference stat blocks by name (e.g. "2× Drider (MM)"). Don't transcribe them.
- Mark unknowns as open questions rather than filling them in.
- If the DM asks for more depth on something specific, go deep on that one thing only.

## Locations

Short bulleted list of details. Target ~5–8 bullets:

```markdown
## The Snapping Line (tavern)

- Dockside, smells like tar and fish
- Owner: one-armed halfling, hates the Primewaters
- Smugglers meet in the back room after dark
- Trapdoor to the water under the bar
- **If PCs push:** owner trades info for protection
```

## NPCs

Same treatment — a short bulleted list, not a biography.

- Role, race, affiliation, where they're found
- 2–3 bullets of appearance/demeanor (traits, not prose)
- What they want
- What they can do for the party
- Open threads / secrets (DM-only ones stay in `planning/`)

Existing files in `docs/characters/` use headed sections. Keep the headings, keep the content bulleted and thin.

## Session Plans

Modular scenes the DM can reorder, skip, or drop. For each scene:

- **Setup:** 1–2 bullets
- **What's here:** short list
- **Paths:** the branches, as `If the PCs X → Y`. This is the section that should be longest.
- **Encounter:** creatures by stat-block name, terrain/hazard bullets, map file if one exists
- **Leaves behind:** what carries into the next session

At most one or two lines of read-aloud text per scene, and only when the exact wording matters (a prophecy, a journal entry, a taunt). Never a wall of boxed text.

Before writing a plan, read the most recent recap so open threads and party state carry forward.

## Session Recaps

**Exception to the bullet rule.** Recaps are the campaign's narrative record — write them as flowing paragraphs, past tense, from what actually happened at the table. See `docs/sessions-recaps/session-18-meeting-lolth.md` for the target voice.

- Frontmatter: `title: Session ## — Title`
- Record player choices as they happened. Never invent PC actions or decisions — ask the DM if a beat is unclear.
- Note unresolved threads at the end.

## Working in This Repo

- Skills exist for the common jobs: `character`, `session-plan`, `session-recap`, `battle-map-search`, `token-generator`. Use them.
- Character files: `firstname-lastname.md` or `firstname.md`, in the right subfolder. New subfolders need a `_category_.json`.
- Asset naming: kebab-case, descriptive (`lolth-cave.jpg`, `captain-hex.png`).
- Verify the site still builds with `npm run build` after structural changes (new folders, sidebar edits, frontmatter changes). Content-only edits don't need it.
- Commit after each recap or major update — the history is the campaign log.
