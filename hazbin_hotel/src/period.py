from datetime import datetime


class Period:
    def __init__(self, start, end):
        if start < end:
            raise ValueError("Start date must be before end date.")

        self.start = start
        self.end = end

    def update_start(self, start):
        if start < self.end:
            raise ValueError("Start date must be after end date.")

        self.start = start

    def update_end(self, end):
        if self.start < end:
            raise ValueError("End date must be before start date.")

        self.end = end
