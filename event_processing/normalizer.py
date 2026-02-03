from event_processing.val_parser import ValorantParser
from event_processing.lol_parser import LolParser


# def normalize_events(raw_events, game: str, series_id: str):
#     normalized = []
#
#     parser = (
#         ValorantParser(series_id)
#         if game == "VAL"
#         else LolParser(series_id)
#     )
#
#     for wrapper in raw_events:
#         inner_events = wrapper.get("events", [])
#
#         for event in inner_events:
#             e = parser.normalize(event)
#             if event.get("type") == "player-killed-player":
#                 print("FOUND KILL EVENT")
#                 print(event)
#                 break
#             if e:
#                 print("NORMALIZED:", e)
#                 normalized.append(e)
#
#         for event in inner_events[:3]:
#             print("INNER EVENT KEYS:", event.keys())
#     print("DEBUG sample event:", raw_events[0])
#     return normalized

def normalize_event(raw, game=None, series_id=None):
    return {
        "event_id": raw.get("id"),
        "event_type": raw.get("type"),
        "action": raw.get("action"),

        "actor_type": raw.get("actor", {}).get("type"),
        "actor_id": raw.get("actor", {}).get("id"),

        "target_type": raw.get("target", {}).get("type"),
        "target_id": raw.get("target", {}).get("id"),

        "timestamp": raw.get("occurredAt"),

        # Context
        "game": game,
        "series_id": series_id
            or raw.get("target", {}).get("state", {}).get("seriesId"),
    }


def normalize_events(raw_events, game=None, series_id=None):
    normalized = []

    for event in raw_events:
        n = normalize_event(event, game=game, series_id=series_id)
        if n:
            normalized.append(n)

    return normalized