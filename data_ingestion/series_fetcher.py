from data_ingestion.central_data import run_query
from models.series import Series

SERIES_QUERY = """
query AllSeries($tournamentIds: [ID!], $after: String) {
  allSeries(
    filter: {
      tournament: {
        id: { in: $tournamentIds }
        includeChildren: { equals: true }
      }
    }
    orderBy: StartTimeScheduled
    after: $after
  ) {
    pageInfo {
      hasNextPage
      endCursor
    }
    edges {
      node {
        id
        startTimeScheduled
        tournament {
          id
          name
        }
        teams {
          baseInfo {
            id
            name
          }
        }
      }
    }
  }
}
"""


def fetch_recent_series(tournament_ids, max_series=10):
    """
    Fetch recent series from GRID Central Data API
    and return normalized Series objects.
    """

    series_list = []
    cursor = None
    has_next = True

    while has_next and len(series_list) < max_series:
        variables = {
            "tournamentIds": [str(tid) for tid in tournament_ids],
            "after": cursor
        }

        data = run_query(SERIES_QUERY, variables)

        # ---- SAFETY CHECK ----
        if "data" not in data or "allSeries" not in data["data"]:
            raise Exception(f"Unexpected GraphQL response: {data}")

        series_data = data["data"]["allSeries"]

        # ---- NORMALIZATION ----
        for edge in series_data["edges"]:
            node = edge["node"]

            try:
                series = Series.from_graphql(node)
                series_list.append(series)
            except Exception as e:
                print(f"Skipping series {node.get('id')} due to error: {e}")

            if len(series_list) >= max_series:
                break

        # ---- PAGINATION ----
        cursor = series_data["pageInfo"]["endCursor"]
        has_next = series_data["pageInfo"]["hasNextPage"]

        # Optional debug
        print("Fetched batch | Total series:", len(series_list))

    return series_list
