# event_processing/strategy.py

from collections import Counter, defaultdict

def detect_round_strategy(round_events):
    """
    Detects strategy patterns for a single round.
    """
    strategy = {
        "playstyle": None,
        "site_focus": None,
        "ability_heavy": False
    }

    ability_events = []
    site_hits = []

    for e in round_events:
        event_type = e.get("event_type", "")
        target = str(e.get("target", "")).lower()

        if event_type == "player-used-ability":
            ability_events.append(e)

        # crude site inference
        if "site-a" in target or "a-site" in target:
            site_hits.append("A")
        elif "site-b" in target or "b-site" in target:
            site_hits.append("B")

    # ---- Playstyle rules ----
    if len(ability_events) >= 8:
        strategy["playstyle"] = "utility-heavy"
        strategy["ability_heavy"] = True
    elif len(round_events) < 20:
        strategy["playstyle"] = "slow-default"
    else:
        strategy["playstyle"] = "standard"

    # ---- Site focus ----
    if site_hits:
        strategy["site_focus"] = Counter(site_hits).most_common(1)[0][0]

    return strategy


def detect_match_strategies(rounds):
    """
    Aggregates strategy patterns across all rounds.
    """
    summary = {
        "playstyle_distribution": Counter(),
        "site_preferences": Counter(),
        "ability_heavy_rounds": 0,
        "total_rounds": len(rounds)
    }

    per_round_strategies = {}

    for round_id, events in rounds.items():
        strat = detect_round_strategy(events)
        per_round_strategies[round_id] = strat

        if strat["playstyle"]:
            summary["playstyle_distribution"][strat["playstyle"]] += 1

        if strat["site_focus"]:
            summary["site_preferences"][strat["site_focus"]] += 1

        if strat["ability_heavy"]:
            summary["ability_heavy_rounds"] += 1

    return per_round_strategies, summary
