#!/usr/bin/env python3
"""
03_trim_music_tracks.py
────────────────────────
Trims raw background tracks into short podcast-ready segments.
"""

from pydub import AudioSegment
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
SRC = BASE / "audio" / "music"
DEST = BASE / "audio" / "music_prepped"
DEST.mkdir(parents=True, exist_ok=True)

tracks = [
    {"src": "soft-background-music-424109.mp3", "dest": "intro_soft.mp3", "start": 0, "end": 20_000},
    {"src": "soft-background-music-427252.mp3", "dest": "background_light.mp3", "start": 0, "end": 30_000},
    {"src": "energetic-background-music-431085.mp3", "dest": "outro_reflective.mp3", "start": 40_000, "end": 65_000},
]

for t in tracks:
    src_path = SRC / t["src"]
    dest_path = DEST / t["dest"]
    print(f"🎧 Trimming {src_path.name} → {dest_path.name}")
    song = AudioSegment.from_file(src_path)
    clip = song[t["start"]:t["end"]].fade_in(1500).fade_out(1500)
    clip.export(dest_path, format="mp3")
    print(f"✅ Saved {dest_path.name} ({(t['end']-t['start'])/1000:.1f}s)")

print(f"\n🎶 All music clips saved to: {DEST}")

