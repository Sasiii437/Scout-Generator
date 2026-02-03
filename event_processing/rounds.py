# event_processing/rounds.py

from collections import defaultdict

def group_events_by_round(normalized_events):
    """
    Groups all events into rounds based on start/end events.
    Returns a dictionary: {round_id: [events]}
    """

    rounds = defaultdict(list)
    current_round = None

    for event in normalized_events:
        # Detect round start
        if event['event_type'] == 'game-started-round':
            current_round = event['target_id']  # e.g., round-1
            rounds[current_round].append(event)
            continue

        # Detect round end (could be multiple event types)
        if event['event_type'] in ['round-ended-freezetime', 'team-won-round']:
            if current_round:
                rounds[current_round].append(event)
                current_round = None
            continue

        # All other events
        if current_round:
            rounds[current_round].append(event)

    return dict(rounds)
