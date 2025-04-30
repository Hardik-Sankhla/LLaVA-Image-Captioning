# backend/main.py
import os
from fastapi import FastAPI, UploadFile, File
from app.model import generate_caption
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/caption/")
async def caption_image(file: UploadFile = File(...)):
    image_bytes = await file.read()
    caption = generate_caption(image_bytes)
    return {"caption": caption}
