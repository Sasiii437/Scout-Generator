class ScoutReport:
    def __init__(self, series, score, reasons):
        self.series_id = series.id
        self.match = f"{series.team_1.name} vs {series.team_2.name}"
        self.scheduled_at = series.scheduled_at
        self.score = score
        self.reasons = reasons

    def to_dict(self):
        return {
            "series_id": self.series_id,
            "match": self.match,
            "scheduled_at": self.scheduled_at,
            "importance_score": self.score,
            "insights": self.reasons
        }
