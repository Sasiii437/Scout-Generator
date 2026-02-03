import json
import os


def load_events_from_jsonl(folder_path: str):
    events = []

    for file in os.listdir(folder_path):
        if file.endswith(".jsonl"):
            with open(os.path.join(folder_path, file), "r", encoding="utf-8") as f:
                for line in f:
                    events.append(json.loads(line))

    return events



def extract_basic_stats(events):
    stats = {
        "kills": 0,
        "rounds": 0,
        "first_bloods": 0,
    }

    for e in events:
        if e.get("type") == "KILL":
            stats["kills"] += 1
            if e.get("isFirstKill"):
                stats["first_bloods"] += 1

        if e.get("type") == "ROUND_START":
            stats["rounds"] += 1

    return stats
