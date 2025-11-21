#!/usr/bin/env python3
"""
chat_cli.py
Simple local chat demo using GPT4All.

Usage:
    python chat_cli.py
Then type messages at the prompt. Type /quit to exit.
"""

import json
from datetime import datetime
from gpt4all import GPT4All

# You can swap this out for another GPT4All model you have / prefer.
MODEL_NAME = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"


def section(title: str) -> None:
    """Print a big pretty section header."""
    print("\n" + "=" * 80)
    print(f"  {title}".center(80))
    print("=" * 80 + "\n")


def divider() -> None:
    """Print a smaller divider."""
    print("\n" + "-" * 80 + "\n")


def main() -> None:
    section("LOCAL GPT4ALL CHAT DEMO")

    print(f"[step] Loading model: {MODEL_NAME}")
    print("[info] The first run may download the model; this can take a while.\n")

    model = GPT4All(MODEL_NAME)

    conversation_log = {
        "model": MODEL_NAME,
        "started_at": datetime.now().isoformat(timespec="seconds"),
        "turns": [],
    }

    print("[info] Model loaded. Starting chat session...")
    print("[hint] Type /quit or /exit to stop.\n")

    # chat_session() keeps conversational context across generate() calls
    # using the model’s chat template. :contentReference[oaicite:1]{index=1}
    with model.chat_session():
        while True:
            user_text = input("You > ").strip()

            if not user_text:
                continue

            if user_text.lower() in {"/quit", "/exit"}:
                section("ENDING CHAT")
                break

            divider()
            print("[step] Sending message to the model...\n")
            print(f"USER: {user_text}\n")

            # Main generation call – you can tweak max_tokens, temperature, etc.
            response = model.generate(
                user_text,
                max_tokens=512,
            )

            print("[assistant]")
            print(response)

            # Log the turn as structured JSON
            turn = {
                "timestamp": datetime.now().isoformat(timespec="seconds"),
                "user": user_text,
                "assistant": response,
            }
            conversation_log["turns"].append(turn)

            print("\n[debug] JSON representation of this turn:\n")
            print(json.dumps(turn, indent=2))
            divider()

    section("FULL CONVERSATION LOG JSON")
    print(json.dumps(conversation_log, indent=2))


if __name__ == "__main__":
    main()
