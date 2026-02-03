# event_processing/round_stats.py

from collections import defaultdict

def compute_round_stats(rounds):
    """
    Computes stats per round:
    - kills per player
    - self-kills per player
    - plants/defuses per player
    - abilities used per player
    - items picked up/dropped per player
    - round winner (team)
    Returns a dict: {round_id: stats_dict}
    """
    round_stats = {}

    for round_id, events in rounds.items():
        stats = {
            'kills': defaultdict(int),
            'self_kills': defaultdict(int),
            'plants': defaultdict(int),
            'defuses': defaultdict(int),
            'abilities_used': defaultdict(lambda: defaultdict(int)),  # {player: {ability: count}}
            'items_picked': defaultdict(lambda: defaultdict(int)),   # {player: {item: count}}
            'items_dropped': defaultdict(lambda: defaultdict(int)),  # {player: {item: count}}
            'round_winner': None
        }

        for e in events:
            etype = e['event_type']
            actor = e.get('actor_id')
            target = e.get('target_id')

            # Kills
            if etype == 'player-killed-player' and actor:
                stats['kills'][actor] += 1
            elif etype == 'player-selfkilled-player' and target:
                stats['self_kills'][target] += 1

            # Bomb plants
            if etype in ['player-completed-plantBomb', 'team-completed-plantBomb'] and actor:
                stats['plants'][actor] += 1

            # Bomb defuses
            if etype in ['player-completed-defuseBomb', 'team-completed-defuseBomb'] and actor:
                stats['defuses'][actor] += 1

            # Abilities
            if etype == 'player-used-ability' and actor and target:
                stats['abilities_used'][actor][target] += 1

            # Items picked up
            if etype == 'player-pickedUp-item' and actor and target:
                stats['items_picked'][actor][target] += 1

            # Items dropped
            if etype == 'player-dropped-item' and actor and target:
                stats['items_dropped'][actor][target] += 1

            # Round winner
            if etype == 'team-won-round' and target:
                stats['round_winner'] = target  # usually team id

        # Convert all defaultdicts to dicts for readability
        stats['kills'] = dict(stats['kills'])
        stats['self_kills'] = dict(stats['self_kills'])
        stats['plants'] = dict(stats['plants'])
        stats['defuses'] = dict(stats['defuses'])
        stats['abilities_used'] = {p: dict(a) for p, a in stats['abilities_used'].items()}
        stats['items_picked'] = {p: dict(i) for p, i in stats['items_picked'].items()}
        stats['items_dropped'] = {p: dict(i) for p, i in stats['items_dropped'].items()}

        round_stats[round_id] = stats

    return round_stats


def summarize_round_events(rounds):
    """
    Prints a summary of events per round:
    - Event type counts
    """
    for round_id, events in rounds.items():
        summary = defaultdict(int)
        for e in events:
            summary[e['event_type']] += 1
        print(f"\nRound: {round_id} event summary:")
        for etype, count in summary.items():
            print(f"  {etype}: {count}")
