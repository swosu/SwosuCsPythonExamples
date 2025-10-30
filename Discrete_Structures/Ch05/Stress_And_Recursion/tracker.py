# tracker.py
import time
from dataclasses import dataclass, field

@dataclass
class Tracker:
    adds: int = 0
    subs: int = 0
    comps: int = 0
    reads: int = 0
    writes: int = 0
    func_calls: int = 0
    start_time: float = field(default_factory=time.time)
    end_time: float = 0.0

    def start(self):
        self.start_time = time.time()

    def stop(self):
        self.end_time = time.time()

    def elapsed(self):
        return self.end_time - self.start_time

    # counting helpers
    def add(self): self.adds += 1
    def sub(self): self.subs += 1
    def comp(self): self.comps += 1
    def read(self): self.reads += 1
    def write(self): self.writes += 1
    def call(self): self.func_calls += 1

    def summary(self):
        return {
            "adds": self.adds, "subs": self.subs, "comps": self.comps,
            "reads": self.reads, "writes": self.writes,
            "func_calls": self.func_calls, "time": self.elapsed()
        }
