# config.py
from dataclasses import dataclass

@dataclass(frozen=True)
class RoundConfig:
    allow_pass_on_lead: bool = False        # default (current behavior)
    equal_beats_equal: bool = False         # default: strictly higher only
    strict_follow_size: bool = True         # default: must match set size

