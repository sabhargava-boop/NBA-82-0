# NBA-82-0: Custom GOAT Formula Lineup Game

A lineup-simulation game inspired by the classic "82-0" format — instead of
building a team around raw box-score stats, this project ranks players using
a custom "player quality" formula and simulates how a dream roster would
perform over a season.

## Concept

Rather than judging players purely on points, rebounds, and assists, the
quality score weighs what actually separates all-time great seasons:

1. MVPs
2. Finals MVPs
3. All-NBA selections
4. Championships (and whether the player was a starter on that title team)
5. Statistical production
6. All-Star selections

## Data

- **Prime legends dataset** (`players.json`) — 25 curated "prime era" player
  seasons spanning the 1990s through the 2020s, hand-picked across all five
  positions.
- **2025–26 season dataset** (`data/season_2025_26.json`) — full season
  roster and stats (583 players), converted from a Basketball-Reference CSV
  export (`data_converter.py`).

## Status

- [x] Data layer: legends dataset and current-season dataset complete
- [x] Formula logic (`formula.py`) in progress
- [ ] Draft mode: randomly present player pools, build an 8-player roster
      (5 starters, 3 bench)
- [ ] Simulation: project a win-loss record from the roster's combined
      quality score

## Running it

Open `index.html` in a browser once the draft mode and simulation logic
(`script.js`) are wired up to the datasets.

## Tech

Python (data processing, formula logic), JSON (data storage), HTML/JS
(front-end draft interface).