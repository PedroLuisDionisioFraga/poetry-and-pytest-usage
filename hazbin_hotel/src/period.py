from datetime import datetime


class Period:

    def __init__(self, start, end):
        if start > end:
            raise ValueError("Start date must be before end date.")

        self.start = start
        self.end = end

    def change_start(self, start: datetime) -> bool:
        if start > self.end:
            return False

        self.start = start
        return True

    def change_end(self, end: datetime) -> bool:
        if self.start > end:
            return False

        self.end = end
        return True
