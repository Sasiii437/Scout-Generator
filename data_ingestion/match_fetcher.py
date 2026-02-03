from data_ingestion.central_data import run_query

MATCH_QUERY = """
query MatchesBySeries($seriesId: ID!) {
  matches(filter: { series: { id: { equals: $seriesId }}}) {
    id
    games {
      id
      sequenceNumber
    }
  }
}
"""

def fetch_matches_and_games(series_id: str):
    data = run_query(MATCH_QUERY, {"seriesId": str(series_id)})

    matches = []
    for match in data["data"]["matches"]:
        for game in match["games"]:
            matches.append({
                "match_id": match["id"],
                "game_id": game["id"],
                "map_number": game["sequenceNumber"]
            })

    return matches
