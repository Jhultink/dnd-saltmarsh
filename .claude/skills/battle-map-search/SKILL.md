---
description: Find battle map images for a D&D encounter based on search terms (e.g. "swampy area with trees", "tavern interior", "ship deck"). Returns a curated list of image URLs from popular battle map sources.
---

Search for battle map images matching the user's description and return a list of links they can browse.

## Inputs

- **Search terms** — provided by the user as an argument or asked for upfront. Examples: "swamp with ruins", "coastal cave", "ship deck combat", "forest clearing".
- If the user provides no terms, ask: "What kind of environment or scene are you looking for? (e.g. 'dense jungle', 'tavern basement', 'open sea deck')"

## Workflow

1. Extract the core search terms from the user's request.
2. Run searches across the priority sources below. Run as many in parallel as possible.
3. Collect image URLs and page links from the results.
4. Deduplicate and rank by relevance — prefer direct image links over landing pages when available.
5. Present the top ~10 results in the format below.

## Priority sources

Search each of these. Tailor the query with `site:` filters or subreddit targeting where noted.

| Source | Search approach |
|---|---|
| Reddit r/battlemaps | `site:reddit.com/r/battlemaps <terms>` |
| Reddit r/dndmaps | `site:reddit.com/r/dndmaps <terms>` |
| 2-Minute Tabletop | `site:2minutetabletop.com <terms>` |
| Forgotten Adventures | `site:forgottenadventures.net <terms>` |
| Pinterest | `site:pinterest.com battle map <terms>` |
| Broad web | `battle map <terms> D&D 5e` (no site filter) |

Run the Reddit searches together, then the dedicated map sites, then the broad search. You don't need all six to return results — surface what you find.

## Output format

Present results as a numbered list. For each result include:
- A short descriptive title (infer from the page title or context)
- The source name (Reddit, 2-Minute Tabletop, etc.)
- The direct URL

If a result links to a Reddit post rather than a direct image, note that. If a result is a gallery or collection page, say so.

After the list, offer: "Want me to refine the search? I can narrow by grid size, style (hand-drawn vs. digital), or add/remove terrain features."

## Example output shape

```
Here are 10 battle maps matching "swampy area with trees":

1. **Murky Swamp — 30x30** — Reddit r/battlemaps
   https://...

2. **Bog Clearing with Dead Trees** — 2-Minute Tabletop
   https://2minutetabletop.com/...

3. **Swamp Ruin at Night** — Reddit r/dndmaps
   https://...

...

Want me to refine the search? I can filter by grid size, art style, or adjust the terrain.
```
