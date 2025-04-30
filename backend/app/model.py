# backend/app/model.py

import requests
from .utils import encode_image_to_base64
import os

OLLAMA_API_URL = os.getenv("OLLAMA_API_URL", "http://localhost:11434/api/generate")

def generate_caption(image_bytes: bytes) -> str:
    """Send image to LLaVA model and get caption."""
    image_base64 = encode_image_to_base64(image_bytes)

    payload = {
        "model": "llava",
        "prompt": "Describe this image in one sentence.",
        "images": [image_base64],
        "stream": False
    }

    response = requests.post(OLLAMA_API_URL, json=payload)
    response.raise_for_status()

    result = response.json()
    return result.get("response", "").strip()
