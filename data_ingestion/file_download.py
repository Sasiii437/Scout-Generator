import requests
import os
import zipfile
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.grid.gg/file-download"
API_KEY = os.getenv("GRID_API_KEY")


def get_available_files(series_id: str):
    url = f"{BASE_URL}/list/{series_id}"
    headers = {"x-api-key": API_KEY}

    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()["files"]


def download_events_file(file_url: str, save_path: str):
    headers = {"x-api-key": API_KEY}
    response = requests.get(file_url, headers=headers, stream=True)
    response.raise_for_status()

    with open(save_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)


def extract_zip(zip_path: str, extract_to: str):
    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(extract_to)

def fetch_series_events(series_id: str):
    files = get_available_files(series_id)

    for f in files:
        if f["id"] == "events-grid-compressed" and f["status"] == "ready":
            zip_path = f"data/raw/events_{series_id}.zip"
            extract_path = f"data/raw/events_{series_id}"

            os.makedirs("data/raw", exist_ok=True)

            download_events_file(f["fullURL"], zip_path)
            extract_zip(zip_path, extract_path)

            return extract_path

    raise Exception(f"No events-grid-compressed file for series {series_id}")


