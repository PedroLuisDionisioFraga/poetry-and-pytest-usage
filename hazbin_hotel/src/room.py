from typing import List

from colorama import Fore, Style

from hazbin_hotel.src.enums.types import ROOM_MULTIPLIERS, RoomTypeEnum
from hazbin_hotel.src.exceptions import InvalidRoomType
from hazbin_hotel.src.period import Period
from hazbin_hotel.src.schedule import Schedule


class Room:
    """
    Represents a hotel room, containing information about its type, price, and booking schedules.

    Attributes:
        instance_count (int): Class-level counter to assign unique room numbers.
        number (int): Unique room number.
        _type (str): Type of the room, defined as a string.
        _price (float): Base price of the room.
        _multiplier_factor_price (float): Price multiplier based on the room type.
        _schedules (List[Schedule]): List of bookings for the room.
    """

    instance_count = 1

    def __init__(self, room_type: str, price: float, schedules: List[Schedule]) -> None:
        """
        Initializes a Room instance with a specified type, price, and list of schedules.

        Args:
            room_type (str): The type of the room.
            price (float): The base price of the room.
            schedules (List[Schedule]): The list of schedules associated with the room.

        Raises:
            InvalidRoomType: If the provided room type is invalid.
            ValueError: If the price is negative.
        """
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
        """
        Gets the current price of the room.

        Returns:
            float: The price of the room.
        """
        return self._price

    @price.setter
    def price(self, new_price: float):
        """
        Sets a new price for the room.

        Args:
            new_price (float): The new price to set.

        Raises:
            ValueError: If the new price is negative.
        """
        self.update_price(new_price)

    @property
    def type(self) -> str:
        """
        Gets the type of the room.

        Returns:
            str: The type of the room.
        """
        return self._type

    @type.setter
    def type(self, new_type: str):
        """
        Sets a new type for the room, issuing a warning if the type is unchanged.

        Args:
            new_type (str): The new room type.

        Raises:
            InvalidRoomType: If the new type is invalid.
        """
        self._validate_room_type(new_type)
        if self._type == new_type:
            print(f"{Fore.YELLOW}[WARNING]: Same type was set!!{Style.RESET_ALL}")
        self._type = new_type

    @property
    def multiplier_factor_price(self) -> str:
        """
        Gets the multiplier factor price based on the room type.

        Returns:
            str: The multiplier factor for the room price.
        """
        return self._type

    def add_schedule(self, schedule: Schedule):
        """
        Adds a new schedule to the room if the period is available.

        Args:
            schedule (Schedule): The schedule to add.

        Raises:
            ValueError: If the period is already occupied.
        """
        if not self.is_period_available(schedule.period):
            raise ValueError("The period is already occupied.")
        self._schedules.append(schedule)

    def is_period_available(
        self,
        period: Period,
        *,
        ignore_schedule: bool = False,
        schedule_id: int = None,
    ) -> bool:
        """
        Checks if a given period is available for scheduling.

        Args:
            period (Period): The period to check.
            ignore_schedule (bool): If True, ignores a specific schedule by `schedule_id`.
            schedule_id (int): The ID of the schedule to ignore.

        Returns:
            bool: True if the period is available, False otherwise.

        Raises:
            ValueError: If `ignore_schedule` is True but `schedule_id` is not provided.
        """
        if ignore_schedule and schedule_id is None:
            raise ValueError("Schedule Id is missing")

        for scheduled in self._schedules:
            if ignore_schedule and scheduled.id == schedule_id:
                continue

            if (
                (
                    (scheduled.period.start <= period.start and scheduled.period.end <= period.end)
                    and scheduled.period.end >= period.start
                )
                or (scheduled.period.start >= period.start and scheduled.period.end >= period.end)
                or (scheduled.period.start <= period.end and scheduled.period.start >= period.end)
            ):
                return False
        return True

    def update_price(self, new_price: float):
        """
        Updates the room price after validation.

        Args:
            new_price (float): The new price to set.

        Raises:
            ValueError: If the new price is negative.
        """
        self._validate_room_price(new_price)
        self._price = new_price

    def update_schedule(self, schedule: Schedule, schedule_id: int):
        """
        Updates a specific schedule by its ID.

        Args:
            schedule (Schedule): The new schedule to replace the old one.
            schedule_id (int): The ID of the schedule to update.

        Raises:
            ValueError: If the new period is not available.
        """
        if not self.is_period_available(schedule.period, ignore_schedule=True, schedule_id=schedule_id):
            raise ValueError("The period is already occupied.")

        schedule_index_to_update = -1
        for schedule_index, scheduled in enumerate(self._schedules):
            if scheduled.id == schedule_id:
                schedule_index_to_update = schedule_index

        self._schedules[schedule_index_to_update] = schedule

    def _set_multiplier_factor(self, room_type: RoomTypeEnum) -> None:
        """
        Sets the multiplier factor based on the room type.

        Args:
            room_type (RoomTypeEnum): The room type for which to set the multiplier factor.

        Raises:
            InvalidRoomType: If the room type is invalid.
        """
        if room_type in ROOM_MULTIPLIERS:
            self._multiplier_factor_price = ROOM_MULTIPLIERS[room_type]
            return
        raise InvalidRoomType(f'Invalid room type, please check type "{room_type.value}"')

    def _validate_room_type(self, room_type: RoomTypeEnum) -> None:
        """
        Validates the provided room type.

        Args:
            room_type (RoomTypeEnum): The room type to validate.

        Raises:
            InvalidRoomType: If the room type is invalid.
        """
        match room_type:
            case _ if room_type in RoomTypeEnum:
                pass
            case _:
                raise InvalidRoomType(f'Invalid room type, please check type "{room_type.value}"')

    def _validate_room_price(self, price: float) -> None:
        """
        Validates that the room price is non-negative.

        Args:
            price (float): The price to validate.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price cannot be negative.")
