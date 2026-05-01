---
description: Generate a 300x300 D&D character token using natural-language description
---

When asked to generate a token (e.g. "Generate a token for an elvish woman with black hair"):

1. Extract the character description from the user's request.
2. Build an image generation prompt for a D&D character portrait:
   - Use the description as the subject
   - Append: "fantasy RPG portrait, circular vignette, painterly illustration style, detailed face, neutral background"
   - Keep it concise and visual
3. Run the Python script: `python .scripts/generate-token.py file_name.png "prompt text here"`. If there are any errors, stop and report them to the user. If the user did not provide a file name, generate a slug based on the description
4. If the image is generated successfully, you are done!