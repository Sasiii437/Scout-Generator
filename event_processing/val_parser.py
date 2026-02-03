from models.event import GameEvent
from event_processing.base_parser import BaseParser


class ValorantParser(BaseParser):

    def normalize(self, raw_event: dict):
        event_type = raw_event.get("type")

        # PLAYER KILL
        if event_type == "player-killed-player":
            return GameEvent(
                game="VAL",
                series_id=self.series_id,
                timestamp=raw_event.get("occurredAt"),
                event_type="kill",
                actor=raw_event.get("actor", {}).get("id"),
                target=raw_event.get("target", {}).get("id"),
                metadata={
                    "action": raw_event.get("action")
                }
            )

        # ROUND WIN
        if event_type == "team-won-round":
            return GameEvent(
                game="VAL",
                series_id=self.series_id,
                timestamp=raw_event.get("occurredAt"),
                event_type="round_win",
                team=raw_event.get("actor", {}).get("id")
            )

        return None
