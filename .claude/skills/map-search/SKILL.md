---
description: Search the internet for a D&D battle map for a given location or encounter
---

Find a battle map for the encounter or location described by the user.

Follow the search strategy in BATTLE_MAP_SEARCH.md. Do the following:

1. If the user hasn't described the environment, ask: what type of location is it (dock, ship, cave, tavern, marsh, dungeon, etc.)?
2. Construct 3–5 targeted search queries using the patterns in BATTLE_MAP_SEARCH.md and the specific location they described.
3. Search the web for maps using those queries, prioritizing the top free sources listed in BATTLE_MAP_SEARCH.md (r/battlemaps, 2-Minute Tabletop, Forgotten Adventures, etc.).
4. Return 3–5 specific results with: the map name/title, the source site, a direct URL, and a one-line note on why it fits (size, style, resolution if visible).
5. Recommend the best pick and explain why.
6. Give the filename the user should save it as, following the folder structure in BATTLE_MAP_SEARCH.md (e.g. `maps/sea/sea-ghost-ship-deck.jpg`).

Prefer gridless maps at 4K resolution. Prefer free sources unless the user asks for premium options.
