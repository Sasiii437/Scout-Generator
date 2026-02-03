import os
from dotenv import load_dotenv

load_dotenv()

GRID_API_KEY = os.getenv("GRID_API_KEY")

CENTRAL_DATA_URL = "https://api-op.grid.gg/central-data/graphql"
SERIES_STATE_URL = "https://api-op.grid.gg/live-data-feed/series-state/graphql"
FILE_DOWNLOAD_BASE_URL = "https://api.grid.gg"
