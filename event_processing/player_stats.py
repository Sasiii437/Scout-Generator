from collections import defaultdict

def compute_player_summary(round_stats):
    """
    Aggregates stats across all rounds to compute total per player.
    Returns dict: {player_id: {kills, self_kills, plants, defuses, abilities_used, items_picked, items_dropped}}
    """
    player_summary = defaultdict(lambda: {
        'kills': 0,
        'self_kills': 0,
        'plants': 0,
        'defuses': 0,
        'abilities_used': defaultdict(int),
        'items_picked': defaultdict(int),
        'items_dropped': defaultdict(int)
    })

    for round_id, stats in round_stats.items():
        # Kills
        for player, count in stats.get('kills', {}).items():
            player_summary[player]['kills'] += count
        for player, count in stats.get('self_kills', {}).items():
            player_summary[player]['self_kills'] += count

        # Bomb actions
        for player, count in stats.get('plants', {}).items():
            player_summary[player]['plants'] += count
        for player, count in stats.get('defuses', {}).items():
            player_summary[player]['defuses'] += count

        # Abilities
        for player, abilities in stats.get('abilities_used', {}).items():
            for ability, count in abilities.items():
                player_summary[player]['abilities_used'][ability] += count

        # Items picked/dropped
        for player, items in stats.get('items_picked', {}).items():
            for item, count in items.items():
                player_summary[player]['items_picked'][item] += count
        for player, items in stats.get('items_dropped', {}).items():
            for item, count in items.items():
                player_summary[player]['items_dropped'][item] += count

    # Convert nested defaultdicts to dicts
    for player, data in player_summary.items():
        data['abilities_used'] = dict(data['abilities_used'])
        data['items_picked'] = dict(data['items_picked'])
        data['items_dropped'] = dict(data['items_dropped'])

    return dict(player_summary)
