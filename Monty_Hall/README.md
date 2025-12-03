flowchart LR
  %% Monty Hall (3-door) Activity / FSM View
  %% Focus: responsibilities split across Game, Contestant, Data, Results

  %% -------------------- GAME --------------------
  subgraph GAME["Game class (MontyHallGame)\nOrchestrates the whole trial loop"]
    direction TB
    g_start([start])
    g_greet["greet_user()\n- choose mode: interactive vs simulation\n- choose strategy: stay/switch/coinflip\n- configure stopping rule (n or CI)"]
    g_init["init_game()\n- doors = {1,2,3}\n- rng/seed policy\n- reset counters"]
    g_new_trial["new_trial(trial_id)\n- place_prize()\n- snapshot trial seed\n- prepare concealed state"]
    g_reveal["host_reveal(prize, player_pick)\n- choose reveal_door\n- must NOT be prize\n- must NOT be player_pick"]
    g_resolve["resolve(final_pick, prize)\n- win = (final_pick == prize)\n- announce outcome (optional)"]
    g_loop_ctrl{"more trials?"}
    g_end([end])
  end

  %% -------------------- CONTESTANT --------------------
  subgraph CONTESTANT["Contestant class\nMakes picks using a strategy"]
    direction TB
    c_pick["initial_pick(doors)\n- returns player_pick\n- may be random or user-chosen"]
    c_decide["decide_switch_or_stay(strategy,\nplayer_pick, revealed, doors)\n- returns decision: STAY/SWITCH"]
    c_final["final_pick(decision,\nplayer_pick, revealed, doors)\n- if STAY: keep player_pick\n- if SWITCH: choose remaining door"]
  end

  %% -------------------- DATA --------------------
  subgraph DATA["Data class (DataCollector)\nRecords trials + computes running stats / stopping"]
    direction TB
    d_record_trial["record_trial(fields)\ntrial_id, seed,\nprize_door, player_pick,\nreveal_door, decision,\nfinal_pick, win"]
    d_update["update_running_stats(record)\n- buckets:\n  stay_win, stay_lose,\n  switch_win, switch_lose\n- running win% by strategy\n- optional CI/halfwidth"]
    d_stop{"stop_rule_met()?\n- fixed N OR\n- CI halfwidth < eps\n- max_trials safety cap"}
  end

  %% -------------------- RESULTS --------------------
  subgraph RESULTS["Results class (ResultsReporter)\nSummarizes + visualizes + exports"]
    direction TB
    r_live["update_live_view(stats)\n- optional live plot\n- convergence trace"]
    r_finalize["final_report(data)\n- win% stay vs switch\n- counts per bucket\n- confidence intervals (if used)\n- write CSV/JSON\n- render plots/tables"]
  end

  %% -------------------- FLOW --------------------
  g_start --> g_greet --> g_init --> g_new_trial
  g_new_trial --> c_pick
  c_pick --> g_reveal
  g_reveal --> c_decide --> c_final
  c_final --> g_resolve

  g_resolve --> d_record_trial --> d_update --> r_live --> d_stop
  d_stop -- "no" --> g_loop_ctrl
  d_stop -- "yes" --> r_finalize --> g_end

  g_loop_ctrl -- "continue" --> g_new_trial
  g_loop_ctrl -- "stop (user / ctrl-c / config)" --> r_finalize
