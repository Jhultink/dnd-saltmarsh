import io
import os
import sys
from google import genai
from google.genai import types
from PIL import Image

if len(sys.argv) != 3:
    print("Usage: generate-token.py <filename> <prompt>")
    sys.exit(1)

filename = sys.argv[1]
prompt = sys.argv[2]

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    print("Error: GEMINI_API_KEY environment variable is not set.")
    sys.exit(1)

client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=prompt,
    config=types.GenerateContentConfig(
        response_modalities=["IMAGE"],
        image_config=types.ImageConfig(
            image_size='1K',
            aspect_ratio='1:1',
        )
    )
)

for part in response.candidates[0].content.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = Image.open(io.BytesIO(part.inline_data.data))
        image = image.resize((300, 300), Image.LANCZOS)
        image.save(f"tokens/{filename}")

print(f"Success: token saved to tokens/{filename}")