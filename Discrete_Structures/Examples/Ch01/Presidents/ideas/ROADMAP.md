# Bot Roadmap
- worst_bot: intentionally bad choices (baseline)
- random_bot: pick legal at random
- lazy_bot: pass unless leading or forced
- greedy_bot: current heuristic
- conservative_bot: avoid breaking sets on lead
- shedder_bot: dump largest groups to empty quickly
- counting_bot: track dead ranks / safe plays
- MCTS-lite: rollouts over sampled hidden hands
- CFR-lite / tabular Q: compact features + self-play
- policy-gradient: learn move probabilities from reward

Milestones:
- [ ] Head-to-head harness
- [ ] CSV logging + leaderboard
- [ ] Elo rating across multi-bot tourneys

