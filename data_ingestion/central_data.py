import requests
from config.grid_config import CENTRAL_DATA_URL, GRID_API_KEY

HEADERS = {
    "x-api-key": GRID_API_KEY,
    "Content-Type": "application/json"
}

def run_query(query: str, variables: dict = None):
    response = requests.post(
        CENTRAL_DATA_URL,
        headers=HEADERS,
        json={
            "query": query,
            "variables": variables
        }
    )

    try:
        result = response.json()
    except Exception:
        raise Exception(f"Non-JSON response: {response.text}")

    # 🔴 GraphQL error handling
    if "errors" in result:
        raise Exception(f"GraphQL Errors: {result['errors']}")

    if "data" not in result:
        raise Exception(f"No data returned: {result}")

    return result
