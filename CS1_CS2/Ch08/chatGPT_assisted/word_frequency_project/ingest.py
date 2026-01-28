# ingest.py
from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Optional


@dataclass(frozen=True)
class IngestResult:
    """Raw text + minimal metadata about where it came from."""
    text: str
    source: str


class Ingest:
    """
    Responsibility: gather text from different sources.
    Think of this class as the "mouth" of the pipeline.
    """

    def __init__(self) -> None:
        self._samples: Dict[str, str] = {
            "gettysburg": (
                "Four score and seven years ago our fathers brought forth on this continent, "
                "a new nation, conceived in Liberty, and dedicated to the proposition that "
                "all men are created equal."
            ),
            "preamble": (
                "We the People of the United States, in Order to form a more perfect Union, "
                "establish Justice, insure domestic Tranquility, provide for the common defence, "
                "promote the general Welfare, and secure the Blessings of Liberty to ourselves "
                "and our Posterity, do ordain and establish this Constitution for the United States of America."
            ),
            "shakespeare": (
                "To be, or not to be, that is the question: "
                "Whether 'tis nobler in the mind to suffer "
                "The slings and arrows of outrageous fortune..."
            ),
        }

    # ---- Steps / function headings (ingest options) ----

    def list_samples(self) -> Dict[str, str]:
        """Return available sample names and short previews."""
        return {k: (v[:80] + "..." if len(v) > 80 else v) for k, v in self._samples.items()}

    def from_sample(self, name: str) -> IngestResult:
        """Ingest text from a built-in sample."""
        key = name.strip().lower()
        if key not in self._samples:
            available = ", ".join(sorted(self._samples))
            raise ValueError(f"Unknown sample '{name}'. Available: {available}")
        return IngestResult(text=self._samples[key], source=f"sample:{key}")

    def from_file(self, path: str | Path, encoding: str = "utf-8") -> IngestResult:
        """Ingest text from a local file path."""
        p = Path(path)
        if not p.exists():
            raise FileNotFoundError(f"File not found: {p}")
        text = p.read_text(encoding=encoding, errors="replace")
        return IngestResult(text=text, source=f"file:{p.resolve()}")

    def from_stdin(self) -> IngestResult:
        """
        Ingest text from stdin. Useful for pipes:
          cat something.txt | python main.py --stdin
        """
        import sys
        text = sys.stdin.read()
        return IngestResult(text=text, source="stdin")

    def from_paste(self, sentinel: str = "END") -> IngestResult:
        """
        Ingest text by letting the user paste multiple lines.
        Stop when they type the sentinel on its own line (default: END).
        """
        print(f"Paste text. Type {sentinel} on its own line to finish.")
        lines = []
        while True:
            line = input()
            if line.strip() == sentinel:
                break
            lines.append(line)
        return IngestResult(text="\n".join(lines), source="paste")

    def interactive(self) -> IngestResult:
        """Simple interactive menu so students can run without arguments."""
        print("Choose input method:")
        print("  1) Sample text")
        print("  2) File path")
        print("  3) Paste text")
        choice = input("Enter 1/2/3: ").strip()

        if choice == "1":
            samples = self.list_samples()
            print("Available samples:")
            for name, preview in samples.items():
                print(f"  - {name}: {preview}")
            name = input("Sample name: ").strip()
            return self.from_sample(name)

        if choice == "2":
            path = input("File path: ").strip()
            return self.from_file(path)

        if choice == "3":
            return self.from_paste()

        raise ValueError("Invalid choice. Please choose 1, 2, or 3.")
