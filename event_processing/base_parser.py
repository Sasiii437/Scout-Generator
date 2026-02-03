class BaseParser:
    def __init__(self, series_id: str):
        self.series_id = series_id

    def normalize(self, raw_event: dict):
        raise NotImplementedError("Implement in child parser")
