#!/usr/bin/env python3
"""
01_extract_latex_to_json.py
────────────────────────────
Converts a LaTeX podcast script (like ch11.tex) into structured JSON for TTS.

Input:
    chapters/ch11.tex
    data/personas.json

Output:
    data/episode_1.json

Each dialogue line becomes a JSON object:
{
    "speaker": "Amina",
    "role": "Philosopher",
    "text": "Hello, friends — and welcome..."
}

Author: Jeremy Evert + ChatGPT (2025)
"""

import json
import re
from pathlib import Path


# ---------- File Paths ----------
BASE_DIR = Path(__file__).resolve().parent.parent
LATEX_FILE = BASE_DIR / "chapters" / "ch11.tex"
PERSONAS_FILE = BASE_DIR / "data" / "personas.json"
OUTPUT_FILE = BASE_DIR / "data" / "episode_1.json"


# ---------- Helpers ----------
def load_personas():
    """Load personas and build a name lookup dictionary."""
    with open(PERSONAS_FILE, "r", encoding="utf-8") as f:
        personas = json.load(f)
    lookup = {}
    for p in personas:
        short_name = p["name"].split()[0]  # e.g., "Dr. Amina Reyes" → "Amina"
        lookup[short_name] = p
    return lookup


def parse_latex_dialogue(text, persona_lookup):
    """
    Extract dialogue from LaTeX.
    Matches lines like:
        \textbf{Amina (Philosopher):} Hello...
        \textbf{Jake:} “Brave” or “confused,” depending on the day.
    """

    dialogue_pattern = re.compile(
        r"\\textbf\{(?P<speaker>[A-Za-z]+)(?:\s*\((?P<role>[^)]+)\))?:\}\s*(?P<dialogue>[^\\]+)",
        re.MULTILINE,
    )

    entries = []
    for match in dialogue_pattern.finditer(text):
        speaker = match.group("speaker").strip()
        role = match.group("role")
        dialogue = match.group("dialogue").strip()
        dialogue = re.sub(r"\s+", " ", dialogue)

        persona = persona_lookup.get(speaker)
        if not persona:
            persona = {"name": speaker, "role": role or "Unknown", "tts_voice": "default"}

        entries.append(
            {
                "speaker": speaker,
                "role": role or persona.get("role", "Unknown"),
                "text": dialogue,
                "tts_voice": persona.get("tts_voice", "default"),
            }
        )

    return entries


def save_json(entries):
    """Write parsed dialogue to JSON."""
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(entries, f, indent=2, ensure_ascii=False)
    print(f"✅ Episode JSON created: {OUTPUT_FILE}")


# ---------- Main ----------
def main():
    print(f"📖 Reading LaTeX file: {LATEX_FILE}")
    text = LATEX_FILE.read_text(encoding="utf-8")

    persona_lookup = load_personas()
    entries = parse_latex_dialogue(text, persona_lookup)

    print(f"🎙️ Extracted {len(entries)} dialogue lines.")
    save_json(entries)


if __name__ == "__main__":
    main()

