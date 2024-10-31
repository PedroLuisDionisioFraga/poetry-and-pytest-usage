from hazbin_hotel.src.period import Period


class Schedule:
    instance_counter = 0

    # TODO: Add a Room instance
    def __init__(self, client_name: str, period: Period) -> None:
        self.client_name = client_name
        self.period = period
        # self.room = room

        self.id = Schedule.instance_counter
        Schedule.instance_counter += 1

        @property
        def client_name(self) -> str:
            return self._client_name

        @client_name.getter
        def client_name(self) -> str:
            return self._client_name
