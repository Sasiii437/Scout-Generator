import json
import os


def load_events_from_folder(folder_path: str):
    all_events = []

    for file in os.listdir(folder_path):
        if not file.endswith(".jsonl"):
            continue

        file_path = os.path.join(folder_path, file)

        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                wrapper = json.loads(line)

                # 🔥 THIS IS THE FIX
                inner_events = wrapper.get("events", [])

                for e in inner_events:
                    # Attach occurredAt from wrapper if missing
                    if "occurredAt" not in e:
                        e["occurredAt"] = wrapper.get("occurredAt")

                    all_events.append(e)

    print("DEBUG: Total raw inner events:", len(all_events))
    print("DEBUG sample inner event:", all_events[0] if all_events else None)

    return all_events
