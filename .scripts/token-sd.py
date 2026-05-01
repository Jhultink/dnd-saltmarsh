import argparse
import logging
import os
import warnings
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

os.environ["TRANSFORMERS_VERBOSITY"] = "error"
os.environ["DIFFUSERS_VERBOSITY"] = "error"
os.environ["TQDM_DISABLE"] = "1"
logging.disable(logging.WARNING)
warnings.filterwarnings("ignore")

from diffusers import AutoPipelineForText2Image, DPMSolverMultistepScheduler
from PIL import Image, ImageDraw
import torch

TOKEN_STYLE = (
    "fantasy portrait, D&D character token, centered subject, bust, "
    "oil painting style, loose brushstrokes, soft edges, painterly, "
    "simple dark muted background, no busy patterns, no text, no watermark, "
)

NEGATIVE_PROMPT = (
    "blurry, low quality, text, watermark, signature, multiple subjects, "
    "busy background, landscape, crowd, modern, sci-fi, photograph, "
    "hyperrealistic, sharp edges, digital art, cg render, 3d, anime"
)

NUM_VARIANTS = 10


BORDER_PATH = Path(__file__).parent / "token-border.png"


def draw_fallback_border(image: Image.Image, size: int, thickness: int = 12) -> Image.Image:
    ring = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(ring)
    draw.ellipse((0, 0, size - 1, size - 1), outline=(180, 140, 50, 255), width=thickness)
    draw.ellipse(
        (thickness // 2, thickness // 2, size - thickness // 2 - 1, size - thickness // 2 - 1),
        outline=(220, 190, 100, 200),
        width=2,
    )
    image.alpha_composite(ring)
    return image


def make_token(image: Image.Image, size: int) -> Image.Image:
    image = image.resize((size, size), Image.LANCZOS)
    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)
    result = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    result.paste(image, mask=mask)

    if BORDER_PATH.exists():
        border = Image.open(BORDER_PATH).convert("RGBA").resize((size, size), Image.LANCZOS)
        result.alpha_composite(border)
    else:
        result = draw_fallback_border(result, size)

    return result

def save_token(args):
    image, path = args
    token = make_token(image, 300)
    token.save(path)

def main():
    parser = argparse.ArgumentParser(description="Generate D&D character tokens")
    parser.add_argument("prompt", nargs="?", help="Character description")
    parser.add_argument("filename", nargs="?", help="Output filename base (e.g. 'thorin')")
    cli = parser.parse_args()

    user_prompt = cli.prompt or input("Describe your character: ").strip()
    filename = cli.filename or input("Output filename base: ").strip()

    full_prompt = f"{user_prompt}, {TOKEN_STYLE}"

    print(f"Generating {NUM_VARIANTS} token variants for: {user_prompt}")

    pipe = AutoPipelineForText2Image.from_pretrained(
        "lykon/dreamshaper-xl-v2-turbo",
        torch_dtype=torch.float16,
        variant="fp16",
    )
    pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)
    pipe = pipe.to("cuda")

    images = pipe(
        full_prompt,
        negative_prompt=NEGATIVE_PROMPT,
        num_inference_steps=8,
        guidance_scale=1,
        width=512,
        height=512,
        num_images_per_prompt=NUM_VARIANTS,
    ).images

    output_paths = [f"./tokens/{filename}-{i + 1}.png" for i in range(NUM_VARIANTS)]

    with ThreadPoolExecutor() as executor:
        executor.map(save_token, zip(images, output_paths))

    print("Done.")

if __name__ == "__main__":
    main()
