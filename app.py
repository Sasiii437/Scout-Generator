from event_processing.loader import load_events_from_folder
from event_processing.normalizer import normalize_events
from event_processing.rounds import group_events_by_round
from event_processing.round_stats import (
    compute_round_stats,
    summarize_round_events,
    # compute_player_series_stats
)
from event_processing.player_stats import compute_player_summary
from event_processing.strategy import detect_match_strategies


def main():
    # -------------------------------
    # Load & normalize
    # -------------------------------
    raw = load_events_from_folder("data/raw/events_2629390")
    events = normalize_events(raw, game="VAL", series_id="2629390")

    print(f"\nNormalized events: {len(events)}")

    # -------------------------------
    # Step 7: Group by round
    # -------------------------------
    rounds = group_events_by_round(events)
    print(f"Total rounds detected: {len(rounds)}")

    # -------------------------------
    # Step 8: Round stats
    # -------------------------------
    round_stats = compute_round_stats(rounds)

    # -------------------------------
    # Step 8b: Player series stats
    # -------------------------------
    player_stats = compute_player_summary(round_stats)

    print("\n=== PLAYER SERIES SUMMARY ===")
    for player, stats in player_stats.items():
        print(f"\nPlayer {player}")
        print(f"  Kills: {stats['kills']}")
        print(f"  Abilities used: {stats['abilities_used']}")
        print(f"  Plants: {stats['plants']}")
        print(f"  Defuses: {stats['defuses']}")

    # -------------------------------
    # Step 11: Strategy Detection
    # -------------------------------
    per_round_strategies, match_strategy_summary = detect_match_strategies(rounds)

    print("\n=== MATCH STRATEGY SUMMARY ===")
    print("Playstyle distribution:")
    for k, v in match_strategy_summary["playstyle_distribution"].items():
        print(f"  {k}: {v} rounds")

    print("\nSite preferences:")
    for site, count in match_strategy_summary["site_preferences"].items():
        print(f"  Site {site}: {count} rounds")

    print(f"\nAbility-heavy rounds: {match_strategy_summary['ability_heavy_rounds']} / {match_strategy_summary['total_rounds']}")

    # Optional: debug first 3 rounds
    print("\n=== SAMPLE ROUND STRATEGIES ===")
    for round_id in list(per_round_strategies.keys())[:3]:
        print(f"{round_id}: {per_round_strategies[round_id]}")


if __name__ == "__main__":
    main()
