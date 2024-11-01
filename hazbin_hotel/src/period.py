from datetime import datetime


class Period:

    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start date must be before end date.")

        self._start = start
        self._end = end

    def change_start(self, start: datetime) -> bool:
        if start > self._end:
            return False

        self._start = start
        return True

    def change_end(self, end: datetime) -> bool:
        if self._start > end:
            return False

        self._end = end
        return True

    @property
    def start(self) -> datetime:
        return self._start

    @property
    def end(self) -> datetime:
        return self._end
