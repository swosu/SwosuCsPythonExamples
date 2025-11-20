# Presidents of Virtue – Simulation Playground

This directory contains a small simulation framework for a custom
card game, **Presidents of Virtue (PoV)**, plus tools for logging and
analyzing how different strategies behave.

There are two big ideas here:

1. **Rule-based bots** (Greedy, Cautious, ChaosRevolutionary, PairLover, Random)
2. **LLM-driven bots** (starting with `LLM_Baby`, with room for more)

The goal is to generate rich logs of play histories so we can ask:
> *Which strategies tend to become President? Which ones get “Deathspanked”?*

---

## Layout

```text
jeremy_solution/
├── ch05.txt
├── chapters/
│   ├── ch01.tex
│   ├── ch02.tex
│   ├── ch03.tex
│   ├── ch04.tex
│   └── ch05.tex
├── main.pdf
├── Makefile
├── PresidentDeathspank.fdb_latexmk
├── PresidentDeathspank.fls
├── PresidentDeathspank.pdf
├── PresidentDeathspank.tex
├── presidents_of_virtue_plays.csv
├── README.md      <-- you are here
├── requirements_pov.txt
└── scripts/
    ├── pov_count_actions.py
    ├── pov_count_plays_passes.py
    ├── pov_logging.py
    ├── pov_peek.py
    ├── pov_players.py
    ├── pov_strategies.py
    ├── presidents_engine.py
    ├── presidents_of_virtue_plays.csv
    ├── presidents_of_virtue_round.py
    ├── simulate_game.py
    ├── simulate_game_llm.py
    ├── simulate_game_llm_duel.py   <-- NEW (LLM vs LLM tournament driver)
    └── test_presidents_engine.py


1. Environment setup

From Discrete_Structures/Ch06/jeremy_solution:

python3 -m venv .venv_pov
source .venv_pov/bin/activate

pip install -r requirements_pov.txt



If you add new packages, update the requirements snapshot:

pip freeze > requirements_pov.txt


2. Running the base simulation (no LLM)

To run a standard rule-based match (5 kids, 5 strategies, multiple rounds):


cd scripts
python simulate_game.py


This will:

Print a detailed play-by-play of each trick.

At the end, write / update:

scripts/presidents_of_virtue_plays.csv (per-trick log)

../presidents_of_virtue_plays.csv (summary at project root, depending on how the logger is wired)

You can then analyze that CSV using:

pov_count_actions.py – count total actions per strategy

pov_count_plays_passes.py – break down plays vs passes per strategy

pov_peek.py – quick peek at the log

Example:

cd scripts
python pov_count_actions.py
python pov_count_plays_passes.py



3. LLM_Baby: one LLM vs three bots

simulate_game_llm.py runs a single LLM-controlled player against
three of the classic rule-based strategies (Cautious, Greedy, ChaosRevolutionary).

Configure the model path

By default, the LLM model path is controlled by an environment variable, e.g.:

export POV_LLM_MODEL_1=/mnt/raid60/models/llm_baby.gguf


(If your script currently uses a hard-coded path, you can update it to read
from POV_LLM_MODEL_1 with a sensible default.)

Run a game with the LLM

cd scripts
python simulate_game_llm.py

You should see:

The usual ROUND / Trick output.

Occasional messages from llama.cpp (including warnings about CUDA on non-GPU nodes).

A final “Finishing order” block showing where LLM_Baby ended up
relative to the three bots.


:wq
\
