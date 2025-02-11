from google import genai
import os
# from google.genai import types

# import pathlib
from PIL import Image

YOUR_GEMINI_API_KEY = 'AIzaSyBS3RZlU6phkxlQvKIL-3x2xtnSV112TOs'
YOUR_MODEL_NAME = 'gemini-2.0-flash'
YOUR_IMAGE_PATH = 'extracted-images'
YOUR_IMAGE_MIME_TYPE = 'image/png'

PROMPT="""
You are a skilled narrator describing scenes from a manga. Each image I provide is a panel from the manga.

For each panel, provide a detailed, atmospheric narration that could be read aloud as the scene is shown. Focus on:
- The visual details and composition of the scene
- The emotional weight and mood
- Any text or dialogue present, incorporating it naturally
- The implied action or movement

Write in a calm, measured tone that draws the viewer in. Avoid overly dramatic language - let the gravity of each scene speak for itself.

Describe each panel as a separate scene, numbered in sequence. Take your time with each description, building the atmosphere and helping the viewer understand both what they're seeing and what it means in the story's context.
"""

client = genai.Client(api_key = YOUR_GEMINI_API_KEY)

# example pillow image
# pil_img = Image.open(YOUR_IMAGE_PATH)
# from the image-path read all images with pillow image
images = []
for filename in sorted(os.listdir(YOUR_IMAGE_PATH)):
    if filename.endswith('.png'):
        img_path = os.path.join(YOUR_IMAGE_PATH, filename)
        pil_img = Image.open(img_path)
        images.append(pil_img)


for chunk in client.models.generate_content_stream(
    model = YOUR_MODEL_NAME,
    contents = [
        PROMPT,
        *images
    ],
):
    print(chunk.text, end='')