from dataclasses import dataclass
from typing import Optional, Dict


@dataclass
class GameEvent:
    game: str                  # "LOL" or "VAL"
    series_id: str
    timestamp: int             # ms since game start
    event_type: str            # kill, round_win, objective, etc.

    actor: Optional[str] = None
    target: Optional[str] = None
    team: Optional[str] = None
    position: Optional[Dict] = None
    metadata: Optional[Dict] = None
