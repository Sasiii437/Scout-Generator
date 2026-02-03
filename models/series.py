class Team:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

class Series:
    def __init__(self, id, scheduled_at, team_1, team_2, tournament_name):
        self.id = id
        self.scheduled_at = scheduled_at
        self.team_1 = team_1
        self.team_2 = team_2
        self.tournament_name = tournament_name

    @staticmethod
    def from_graphql(node: dict):
        """
        Convert Central Data GraphQL node → Series object
        """

        teams = node.get("teams", [])
        if len(teams) < 2:
            raise ValueError("Series does not have 2 teams")

        team_1 = Team(
            id=teams[0]["baseInfo"]["id"],
            name=teams[0]["baseInfo"]["name"]
        )

        team_2 = Team(
            id=teams[1]["baseInfo"]["id"],
            name=teams[1]["baseInfo"]["name"]
        )

        tournament = node.get("tournament")
        if not tournament:
            raise ValueError("Tournament data missing")

        return Series(
            id=node["id"],
            scheduled_at=node["startTimeScheduled"],
            team_1=team_1,
            team_2=team_2,
            tournament_name=tournament["name"]
        )
