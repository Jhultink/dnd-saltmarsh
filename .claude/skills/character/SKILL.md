---
description: Create or update a D&D character file for the Saltmarsh campaign — player characters or NPCs (ally or villain)
---

Create a new character file or update an existing one in `characters/`. Handle player characters (PCs), allied NPCs, and antagonist NPCs.

## Folder Structure

Characters are organized into three subfolders based on type:

| Type | Folder |
|---|---|
| Player characters | `characters/pcs/` |
| Allied NPCs (friendly, neutral, or allied) | `characters/allies/` |
| Villains and antagonists | `characters/enemies/` |

Always place new files in the correct subfolder. When updating, search all three subfolders.

## Workflow

1. **Determine intent** — Is the user creating a new character or updating an existing one?
   - If updating: find the file in `characters/pcs/`, `characters/allies/`, or `characters/enemies/` and edit only the fields the user mentions. Preserve everything else.
   - If new: ask for any missing required fields before writing the file.

2. **Determine character type** — PC, allied NPC, or villain/antagonist. This determines which subfolder and which template to use (see below).

3. **Infer the filename** from the character's name:
   - Use `firstname-lastname.md` if a last name / family name is known, otherwise `firstname.md`.
   - Lowercase, hyphen-separated. Example: `characters/pcs/aelar-swiftwind.md`, `characters/allies/oleander.md`.

4. **Write or update the file** using the appropriate template below. If information is unknown, leave the section blank. Do NOT invent details that the user has not provided.

5. After creating a **new** file, mention the path so the user can find it easily.

---

## PC Template

```markdown
# [Name]

- **Player:** 
- **Race:** 
- **Class & Level:** 
- **Background:** 
- **Alignment:** 

## Appearance

Brief physical description — 2–4 sentences.

## Personality

Traits, ideals, bonds, flaws (D&D background pillars, but prose is fine).

## Backstory

Where they came from and what brought them to Saltmarsh.

## Abilities & Notable Skills

Key strengths, signature spells or abilities, fighting style.

## Equipment & Magic Items

| Item | Notes |
|---|---|
| Shortsword +1 | Found in the haunted house |

## Relationships

| Character | Relationship |
|---|---|
| Oleander | Rival turned reluctant ally |

## Story Notes

Ongoing threads, personal quests, DM hooks.
```

---

## Allied NPC Template

```markdown
# [Name]

- **Role:** (e.g., Harbor Master, Sea Elf Scout, Town Councilmember)
- **Race:** 
- **Affiliation:** 
- **Location:** Where they're usually found

## Appearance

Brief physical description.

## Personality & Demeanor

How they present themselves; what drives them.

## Relationship to the Party

How they know the party and what they think of them.

## Useful To The Party

What services, knowledge, or resources they can provide.

## Story Notes

Ongoing involvement, secrets they hold, future plot hooks.
```

---

## Villain / Antagonist NPC Template

```markdown
# [Name]

- **Role:** (e.g., Smuggling Boss, Sahuagin War-Chief, Cult Leader)
- **Race:** 
- **Affiliation:** 
- **Status:** Active / Defeated / Unknown

## Appearance

Brief physical description — what makes them memorable or unsettling.

## Personality & Motivation

What they want and why. What makes them dangerous beyond raw power.

## Methods & Resources

How they operate — minions, hideouts, schemes.

## Relationship to the Party

Have they met? Does the villain know the party? Any personal grudge?

## Story Notes

DM-only context: true goals, planned appearances, secrets not yet revealed.
```
