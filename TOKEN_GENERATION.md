# Generating Player Tokens with nano-banana

[nano-banana](https://github.com/nicohirtt/nano-banana) (also accessible at **https://nana.banana.style**) is a free browser-based D&D token maker. Use it to create round portrait tokens for player characters and important NPCs.

## Step-by-Step

1. **Open nano-banana** in your browser at `https://nana.banana.style`.

2. **Upload an image**
   - Click the image area or drag-and-drop a portrait onto the canvas.
   - Good sources for portraits:
     - AI-generated art (Midjourney, DALL-E, Stable Diffusion)
     - Official D&D art books scanned/shared legally
     - Hero Forge miniature screenshot (front-facing)
     - Pinterest boards tagged `dnd character portrait`

3. **Adjust the crop**
   - Drag to reposition the face inside the circle.
   - Zoom with the scroll wheel or pinch gesture.
   - Aim for the face centered with a little shoulder visible.

4. **Pick a border style**
   - **Players:** choose a colored ring that matches their class (blue = wizard, red = fighter, green = ranger, etc.) — be consistent across the campaign.
   - **NPCs:** use a neutral gold or silver ring.
   - **Enemies/monsters:** use a red or dark border.

5. **Add a name label** (optional but recommended)
   - Type the character's first name in the label field.
   - Keep it short — it appears below the token on most map tools.

6. **Export**
   - Click **Download** — saves as a `.png` (transparent background, ~512×512 px).
   - Save to a shared folder or directly import into your map tool.

## File Naming Convention

```
tokens/
  pc-aelar.png
  pc-bryndis.png
  npc-captain-xendros.png
  enemy-sahuagin-baron.png
```

Create a `tokens/` folder in this repo and commit token PNGs there so they're always available.

## Importing into Common Map Tools

| Tool | How to import |
|---|---|
| Owlbear Rodeo | Scene → Add Token → Upload image |
| Foundry VTT | File Browser → upload to `Data/tokens/` → drag onto scene |
| Roll20 | Art Library → Upload → drag onto map |
| Inkarnate | My Assets → Upload |
| Dungeondraft | Assets panel → Custom Assets folder |

## Tips

- Use the same portrait source style for all PCs so tokens look cohesive.
- Export at 2× zoom for Foundry VTT (it handles high-res better).
- Re-export with a red tint overlay when a character is cursed, polymorphed, or dead — quick visual indicator for players.
