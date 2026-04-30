# Finding Battle Maps Online

A guide for sourcing high-quality battle maps for the Saltmarsh campaign.

## Search Strategy

### 1. Know What You're Looking For

Before searching, identify:
- **Environment type** — dock, tavern, ship deck, sea cave, marshland, dungeon, town square, etc.
- **Size** — standard is 1 inch = 5 ft. Most digital maps are 70–100 px per grid square.
- **Grid or gridless** — gridless is more flexible (you can overlay your own grid in the map tool).
- **Resolution** — aim for at least 2048×2048 px; 4K (3840×2160) is ideal for Foundry VTT.

### 2. Best Search Terms

Combine environment + "battle map" + optional style:

```
saltmarsh dock battle map
ship deck battle map dnd 5e
sea cave encounter map gridless
fishing village dnd map
marsh/swamp encounter battle map
underwater battle map dnd
tavern battle map top-down
warehouse battle map 5e
```

Add `site:reddit.com` to filter to community posts, or `filetype:jpg` to find direct images.

### 3. Top Free Sources

| Source | URL | Notes |
|---|---|---|
| r/battlemaps | reddit.com/r/battlemaps | Huge community, searchable, free downloads |
| r/dndmaps | reddit.com/r/dndmaps | More hand-drawn/artistic style |
| Forgotten Adventures | forgotten-adventures.net | Free Patreon tier; excellent quality |
| 2-Minute Tabletop | 2minutetabletop.com | Free map packs; coastal/ship maps available |
| Dyson Logos | dysonlogos.blog | Classic hand-drawn dungeon maps, free |
| Dungeon Fog | dungeonfog.com | Free tier with basic maps |
| Dave's Mapper | davesmapper.com | Procedural, good for wilderness |

### 4. Premium Sources (Worth It)

| Source | Notes |
|---|---|
| Patreon — Cze & Peku | Excellent nautical/coastal maps |
| Patreon — Afternoon Maps | Coastal and swamp content |
| Patreon — Tom Cartos | Detailed town and dungeon maps |
| Dungeon Alchemist | Software to generate your own |

### 5. Search Engines & Image Search Tips

- **Google Images:** search term + "battle map" → Tools → Size → Large
- **Pinterest:** great for discovering artists, then go to their actual site for download
- **Itch.io:** search "battle map" or "dnd map pack" — many free/PWYW packs
- **DriveThruRPG:** filter by price: free → "Map" category

### 6. Saltmarsh-Specific Resources

The official *Ghosts of Saltmarsh* module includes maps, but community remakes are higher resolution:

- Search `"ghosts of saltmarsh" battle map remake`
- Search `haunted house saltmarsh map` for the first adventure
- Search `"Sea Ghost" ship map dnd` for the smuggler vessel
- Search `lizardfolk lair battle map` for marsh encounters

### 7. Evaluating a Map

Before downloading, check:
- [ ] Resolution is 2048 px minimum on the short side
- [ ] Grid squares are identifiable (or gridless is confirmed)
- [ ] License allows personal/non-commercial tabletop use
- [ ] Style matches your other maps (consistent aesthetic matters for immersion)

### 8. Organizing Downloaded Maps

Store maps in this repo under a `maps/` folder:

```
maps/
  town/
    saltmarsh-docks.jpg
    fishmonger-district.jpg
  sea/
    sea-ghost-ship-deck.jpg
    sea-cave-entrance.jpg
  wilderness/
    marsh-path-encounter.jpg
  dungeon/
    haunted-house-ground-floor.jpg
    haunted-house-basement.jpg
```

Commit map files to git so they're version-controlled and accessible everywhere.
