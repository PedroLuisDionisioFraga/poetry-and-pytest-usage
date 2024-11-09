class InvalidPeriodError(Exception):
    def __init__(self, period: str):
        self.period = period
        self.message = f"Invalid period: {period}"
        super().__init__(self.message)
