from models.event import GameEvent
from event_processing.base_parser import BaseParser


class LolParser(BaseParser):

    def normalize(self, raw_event: dict):
        event_type = raw_event.get("eventType")

        if event_type == "CHAMPION_KILL":
            return GameEvent(
                game="LOL",
                series_id=self.series_id,
                timestamp=raw_event.get("timestamp", 0),
                event_type="kill",
                actor=raw_event["killerName"],
                target=raw_event["victimName"],
                team=raw_event.get("killerTeam"),
                position={
                    "x": raw_event.get("position", {}).get("x"),
                    "y": raw_event.get("position", {}).get("y")
                }
            )

        if event_type == "ELITE_MONSTER_KILL":
            return GameEvent(
                game="LOL",
                series_id=self.series_id,
                timestamp=raw_event.get("timestamp", 0),
                event_type="objective",
                team=raw_event.get("killerTeam"),
                metadata={
                    "monster": raw_event.get("monsterType")
                }
            )

        return None
