#!/usr/bin/env python3
"""
magic8_demo.py
Automatically ask a local GPT4All model 8 Magic-8-ball style questions.

Usage:
    python magic8_demo.py
"""

import json
import random
from datetime import datetime
from gpt4all import GPT4All

MODEL_NAME = "Meta-Llama-3-8B-Instruct.Q4_0.gguf"


def section(title: str) -> None:
    print("\n" + "=" * 80)
    print(f"  {title}".center(80))
    print("=" * 80 + "\n")


def divider() -> None:
    print("\n" + "-" * 80 + "\n")


def build_question_pool():
    """Return a pool of Magic-8-ish questions."""
    return [
        "Will today turn out better than I expect?",
        "Is now a good time to start a new project?",
        "Should I focus on rest or productivity this evening?",
        "Is collaboration my secret weapon this week?",
        "Will I learn something surprising today?",
        "Is this a moment to be bold or cautious?",
        "Will my students connect with my next lesson?",
        "Is it wise to say yes to the next opportunity I’m offered?",
        "Will a small change today lead to big results later?",
        "Is my intuition trying to tell me something important?",
        "Should I trust my first idea or the second one?",
        "Will intentional rest help me think more clearly tomorrow?",
    ]


def main() -> None:
    section("MAGIC 8-BALL GPT4ALL DEMO")

    print(f"[step] Loading model: {MODEL_NAME}")
    model = GPT4All(MODEL_NAME)
    print("[info] Model loaded.\n")

    question_pool = build_question_pool()
    selected_questions = random.sample(question_pool, 8)

    run_log = {
        "model": MODEL_NAME,
        "run_started_at": datetime.now().isoformat(timespec="seconds"),
        "selected_questions": selected_questions,
        "turns": [],
    }

    print("[debug] Selected questions (randomized order):")
    print(json.dumps(selected_questions, indent=2))
    divider()

    with model.chat_session():
        for idx, question in enumerate(selected_questions, start=1):
            section(f"QUESTION {idx} / 8")

            print("[step] Sending question to model...\n")
            print(f"QUESTION: {question}\n")

            response = model.generate(
                question,
                max_tokens=256,
            )

            print("[assistant]")
            print(response)

            turn = {
                "index": idx,
                "question": question,
                "answer": response,
                "timestamp": datetime.now().isoformat(timespec="seconds"),
            }
            run_log["turns"].append(turn)

            print("\n[debug] JSON for this Q/A pair:\n")
            print(json.dumps(turn, indent=2))
            divider()

    section("FINAL RUN LOG JSON")
    print(json.dumps(run_log, indent=2))


if __name__ == "__main__":
    main()
