import pandas as pd
import json
df = pd.read_csv('data/season_2025_26_raw.csv')
df = df.sort_values('Team', key=lambda col: col.str.contains('TM', na=False), ascending=False)
df = df.drop_duplicates(subset='Player', keep='first')
Champion_team = "NYK"
Finals_MVP = "Jalen Brunson"

def parse_awards(awards_str):
    """Pulls MVP / All-Star / All-NBA tier out of the Awards column."""
    if pd.isna(awards_str):
        return {"mvp": False, "all_star": False, "all_nba": None}
    awards = str(awards_str)
    mvp = "MVP-1" in awards
    all_nba = None
    if "NBA1" in awards:
        all_nba = "1st"
    elif "NBA2" in awards:
        all_nba = "2nd"
    elif "NBA3" in awards:
        all_nba = "3rd"
    return {"mvp": mvp, "all_star": "AS" in awards, "all_nba": all_nba}
players = []
for _, row in df.iterrows():
    awards = parse_awards(row['Awards'])
    player = {
        "player": row['Player'],
        "season": "2025-26",
        "team": row['Team'],
        "mvp": awards["mvp"],
        "finals_mvp": row['Player'] == Finals_MVP,
        "all_nba": awards["all_nba"],
        "champion": row['Team'] == Champion_team,
        "all_star": awards["all_star"],
        "ppg": row['PTS'],
        "rpg": row['TRB'],
        "apg": row['AST'],
    }
    players.append(player)
with open('data/season_2025_26.json', 'w') as f:
    json.dump(players, f, indent=2)
print(f"Processed {len(players)} players to data/season_2025_26.json")