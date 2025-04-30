# backend/app/utils.py

import base64

def encode_image_to_base64(image_bytes: bytes) -> str:
    """Encode image bytes to a Base64 string."""
    return base64.b64encode(image_bytes).decode("utf-8")
