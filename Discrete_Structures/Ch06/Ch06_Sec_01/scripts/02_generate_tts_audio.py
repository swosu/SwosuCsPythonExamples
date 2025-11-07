#!/usr/bin/env python3
"""
02_generate_tts_audio.py
────────────────────────────
Generates audio clips from episode JSON using OpenAI TTS voices.
Adds safe voice mapping and graceful fallback for unsupported names.
"""

import json
import os
from pathlib import Path
from time import sleep
from openai import OpenAI

# ---------- Setup ----------
BASE_DIR = Path(__file__).resolve().parent.parent
EPISODE_JSON = BASE_DIR / "data" / "episode_1.json"
OUTPUT_DIR = BASE_DIR / "audio" / "episode_1"
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

client = OpenAI()

# ---------- Voice Mapping ----------
VOICE_MAP = {
    "default": "alloy",
    "opal": "shimmer",   # Zahra → soft, artistic tone
    "alloy": "alloy",    # Amina → clear and authoritative
    "verse": "verse",    # Lin → energetic
    "sage": "sage",      # Jake → grounded male
}

def resolve_voice(voice):
    """Return a valid TTS voice."""
    if voice in VOICE_MAP:
        return VOICE_MAP[voice]
    # try to fall back to alloy if not found
    print(f"⚙️ Unknown voice '{voice}', using fallback 'alloy'")
    return "alloy"

# ---------- Core Functions ----------
def load_script():
    with open(EPISODE_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def synthesize_speech(text, voice, filename):
    """Generate a TTS audio file for a given line."""
    output_path = OUTPUT_DIR / filename
    if output_path.exists():
        print(f"⏩ Skipping existing: {output_path.name}")
        return

    voice = resolve_voice(voice)
    print(f"🎤 Generating voice '{voice}' → {output_path.name}")

    try:
        response = client.audio.speech.create(
            model="gpt-4o-mini-tts",
            voice=voice,
            input=text
        )
        with open(output_path, "wb") as f:
            f.write(response.read())
        sleep(0.5)
    except Exception as e:
        print(f"⚠️ Error generating {filename}: {e}")

def main():
    entries = load_script()
    print(f"🎙️ Loaded {len(entries)} lines from episode JSON.")
    for i, entry in enumerate(entries, start=1):
        speaker = entry["speaker"]
        voice = entry.get("tts_voice", "default")
        text = entry["text"]
        filename = f"{i:03d}_{speaker}.mp3"
        synthesize_speech(text, voice, filename)
    print(f"✅ All audio saved to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()

