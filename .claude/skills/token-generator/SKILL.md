---
name: token-generator
description: Use when the user wants to generate a D&D character token image — accepts a character name (looks up their description from the repo) or a freeform character description, then runs token-sd.py to produce token variants.
---

Generate a circular D&D character token image using the local Stable Diffusion pipeline.

## Inputs

- **Name** — a character name (e.g. "Toro", "Skerrin Wavechaser"). Look up their file in `docs/characters/` to extract a visual description.
- **Description** — a freeform visual description (e.g. "grizzled dwarf sailor with a red beard and eye patch"). Use directly as the prompt.
- **Filename base** — derived from the name or description (lowercase, hyphen-separated). Ask if ambiguous.
- **Variants** — number of image variants to generate. Default: 6. Ask if the user specifies otherwise.

## Workflow

1. **Resolve the prompt.**
   - If the input is a character **name**: search `docs/characters/pcs/`, `docs/characters/allies/`, and `docs/characters/enemies/` for a matching file. Read the **Appearance** section and any other visually relevant details (race, class hints from gear/abilities). Compose a concise visual description (1–3 sentences) from that content.
   - If the input is already a **description**: use it as-is.

2. **Derive the filename base** from the character name or a short slug of the description (lowercase, hyphens). Examples: `toro`, `skerrin-wavechaser`, `grizzled-dwarf-sailor`.

3. **Run the generator.** Execute the script from the repo root:

   ```powershell
   python .scripts/token-sd.py "<prompt>" "<filename-base>" -n <variants>
   ```

   Tokens are saved to `planning/tokens/<filename-base>-1.png` … `<filename-base>-N.png`.

4. **Report results.** Tell the user which files were written and how many variants were generated.

## Example

Character name input → "Toro":
- Read `docs/characters/pcs/toro.md`, extract Appearance section.
- Compose prompt: `"large minotaur warrior, dark brown fur, cracked horns, battle-worn leather armor, intense gaze"`
- Run: `python .scripts/token-sd.py "large minotaur warrior, dark brown fur, cracked horns, battle-worn leather armor, intense gaze" "toro" -n 6`
- Report: "Generated 6 token variants at planning/tokens/toro-1.png through toro-6.png."

## Notes

- The script requires a CUDA GPU. If it fails, mention this to the user.
- Tokens are saved as 300×300 PNG with a circular crop and decorative border.
- Output directory `planning/tokens/` must exist — create it if missing.
