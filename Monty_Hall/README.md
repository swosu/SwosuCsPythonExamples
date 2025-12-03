classDiagram
  %% Monty Hall Responsibility Map (4-class version)

  class Game {
    +int trial_id
    +list doors
    +RNG rng
    +Contestant contestant
    +Data data
    +Results results
    +greet_user()
    +init_game()
    +place_prize() int
    +host_reveal(prize_door, player_pick) int
    +resolve(final_pick, prize_door) bool
    +run()  %% trial loop + orchestration
  }

  class Contestant {
    +string strategy
    +initial_pick(doors) int
    +decide_switch_or_stay(strategy, player_pick, reveal_door, doors) string
    +final_pick(decision, player_pick, reveal_door, doors) int
  }

  class Data {
    +int n_trials
    +int stay_win
    +int stay_lose
    +int switch_win
    +int switch_lose
    +list records
    +record_trial(trial_fields)
    +update_running_stats(record)
    +win_rate_stay() float
    +win_rate_switch() float
    +confidence_interval(p_hat, n) tuple  %% optional
    +stop_rule_met() bool
  }

  class Results {
    +update_live_view(stats)
    +final_report(data)
    +export_csv(path)
    +export_json(path)
    +plot_convergence(path)
    +plot_buckets(path)
  }

  Game "1" --> "1" Contestant : delegates choices
  Game "1" --> "1" Data : writes trial records
  Game "1" --> "1" Results : displays + exports
  Results ..> Data : reads aggregated stats
