from intelligence.heuristics import rivalry_score, team_strength_score
from config.teams import TOP_TEAMS, RIVALRIES
from config.tournaments import TOURNAMENT_IMPORTANCE

def evaluate_series(series):
    score = 0
    reasons = []

    # Team strength
    score += team_strength_score(series.team_1.name, TOP_TEAMS)
    score += team_strength_score(series.team_2.name, TOP_TEAMS)

    if series.team_1.name in TOP_TEAMS or series.team_2.name in TOP_TEAMS:
        reasons.append("Features a top-tier team")

    # Rivalry
    rivalry = rivalry_score(series.team_1.name, series.team_2.name, RIVALRIES)
    if rivalry:
        score += rivalry
        reasons.append("Historic rivalry matchup")

    # Tournament importance
    for key, weight in TOURNAMENT_IMPORTANCE.items():
        if key.lower() in series.tournament_name.lower():
            score += weight
            reasons.append(f"High-stakes {key} tournament")

    return score, reasons
