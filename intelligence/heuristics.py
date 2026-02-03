def rivalry_score(team1, team2, rivalries):
    for a, b in rivalries:
        if (team1 == a and team2 == b) or (team1 == b and team2 == a):
            return 3
    return 0


def team_strength_score(team_name, top_teams):
    return 2 if team_name in top_teams else 0
