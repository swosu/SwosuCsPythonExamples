```mermaid
flowchart LR
  Start([Start: greet user]) --> Prize[Game: randomly choose winning door (prize)]
  Prize --> Pick[Contestant: choose initial door]

  Pick --> Reveal[Game: reveal a non-winning door<br/>(not contestant's pick, not prize)]
  Reveal --> Decide{Contestant switches?}

  Decide -- "No (stay)" --> FinalStay[Final door = initial door]
  Decide -- "Yes (switch)" --> FinalSwitch[Final door = the remaining unopened door]

  FinalStay --> Outcome[Game: determine win/lose]
  FinalSwitch --> Outcome

  Outcome --> RecStrategy[Data: record strategy (switch/stay)]
  RecStrategy --> RecOutcome[Data: record outcome (win/lose)]
  RecOutcome --> CSV[Data: append trial to CSV]

  CSV --> CI[Data: update running stats<br/>and compute confidence interval]
  CI --> StopCheck{CI half-width &lt; ε ?}

  StopCheck -- "No, keep going" --> Prize
  StopCheck -- "Yes, stop" --> Graph[Data: graph/report results]
  Graph --> End([End])

```