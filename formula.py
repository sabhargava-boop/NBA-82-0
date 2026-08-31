import json
Weights = { 
    "mvp": 10,
    "finals_mvp": 8,
    "all_nba": {"1st":6, "2nd":4, "3rd":2},
    "champion": 4,
    "all_star": 1,
    "stat_ppg": 0.5,
    "stat_rpg": 0.3,
    "stat_apg": 0.3,
}
def quality_score(player):
    score = 0
    if player.get("mvp"):
        score += Weights["mvp"]
    if player.get("finals_mvp"):
        score += Weights["finals_mvp"]
    if player.get("all_nba"):
        all_nba = player.get("all_nba")
        if all_nba == "1st":
            score += Weights["all_nba"]["1st"]
        elif all_nba == "2nd":
            score += Weights["all_nba"]["2nd"]
        elif all_nba == "3rd":
            score += Weights["all_nba"]["3rd"]
    if player.get("champion"):
        score += Weights["champion"]
    if player.get("all_star"):
        score += Weights["all_star"]
    if player.get("stat_ppg"):
        score += player.get("stat_ppg") * Weights["stat_ppg"]
    if player.get("stat_rpg"):
        score += player.get("stat_rpg") * Weights["stat_rpg"]
    if player.get("stat_apg"):
        score += player.get("stat_apg") * Weights["stat_apg"]
    return round(score, 2)
def load_players(path):
    with open(path, "r") as f:
        return json.load(f)
if __name__ == "__main__":
    players = load_players("data/players.json")
    scored = [(p["player"], p["season"], quality_score(p)) for p in players]
    scored.sort(key=lambda x: x[2], reverse=True)
    print(f"{'Player':<25} {'Season':<10} {'Score'}")
    print("-" * 45)
    for name, season, score in scored:
        print(f"{name:<25} {season:<10} {score}")