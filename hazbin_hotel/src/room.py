from typing import List

from colorama import Fore, Style

from hazbin_hotel.src.enums.types import ROOM_MULTIPLIERS, RoomTypeEnum
from hazbin_hotel.src.exceptions import InvalidRoomType
from hazbin_hotel.src.period import Period
from hazbin_hotel.src.schedule import Schedule


class Room:
    instance_count = 1

    def __init__(
        self, room_type: str, price: float, schedules: List[Schedule]
    ) -> None:
        self._validate_room_type(room_type)
        self._validate_room_price(price)

        self.number = Room.instance_count
        self._type = room_type
        self._price = price
        self._multiplier_factor_price = 0

        self._schedules = schedules

        self._set_multiplier_factor(room_type)
        Room.instance_count += 1

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, new_price: float):
        self.update_price(new_price)

    @property
    def type(self) -> str:
        return self._type

    @type.setter
    def type(self, new_type: str):
        self._validate_room_type(new_type)
        if self._type == new_type:
            print(
                f"{Fore.YELLOW}[WARNING]: Same type was set!!{Style.RESET_ALL}"
            )
        self._type = new_type

    @property
    def multiplier_factor_price(self) -> str:
        return self._type

    def add_schedule(self, schedule: Schedule):
        if not self.is_period_available(schedule.period):
            raise ValueError()
        self._schedules.append(schedule)

    def is_period_available(
        self,
        period: Period,
        *,
        ignore_schedule: bool = False,
        schedule_id: int = None,
    ):
        if ignore_schedule and schedule_id is None:
            raise ValueError("Schedule Id is missing")

        for scheduled in self._schedules:
            if ignore_schedule and scheduled.id == schedule_id:
                continue

            if (
                (
                    (
                        scheduled.period.start <= period.start
                        and scheduled.period.end <= period.end
                    )
                    and scheduled.period.end >= period.start
                )
                or (
                    scheduled.period.start >= period.start
                    and scheduled.period.end >= period.end
                )
                or (
                    scheduled.period.start <= period.end
                    and scheduled.period.start >= period.end
                )
                # or (scheduled.period.start < period.start and )
            ):
                return False
        return True

    def update_price(self, new_price: float):
        self._validate_room_price(new_price)
        self._price = new_price

    def update_schedule(self, schedule: Schedule, schedule_id: int):
        if not self.is_period_available(
            schedule.period, ignore_schedule=True, schedule_id=schedule_id
        ):
            raise ValueError()

        schedule_index_to_update = -1
        for schedule_index, scheduled in enumerate(self._schedules):
            if scheduled.id == schedule_id:
                schedule_index_to_update = schedule_index

        self._schedules[schedule_index_to_update] = schedule

    def _set_multiplier_factor(self, room_type: RoomTypeEnum) -> None:
        if room_type in ROOM_MULTIPLIERS:
            self._multiplier_factor_price = ROOM_MULTIPLIERS[room_type]
            return
        raise InvalidRoomType(
            f'Invalid room type, please check type "{room_type.value}"'
        )

    def _validate_room_type(self, room_type: RoomTypeEnum) -> None:
        match room_type:
            case _ if room_type in RoomTypeEnum:
                pass
            case _:
                raise InvalidRoomType(
                    f'Invalid room type, please check type "{room_type.value}"'
                )

    def _validate_room_price(self, price: float) -> None:
        if price < 0:
            raise ValueError(f"Price cannot be negative.")
