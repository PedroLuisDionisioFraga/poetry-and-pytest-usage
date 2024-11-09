from datetime import datetime
from typing import List

from hazbin_hotel.src.enums.types import RoomTypeEnum
from hazbin_hotel.src.exceptions import (
    RoomHasSchedule,
    RoomNotAvailable,
    RoomTypeNotAvailable,
)
from hazbin_hotel.src.period import Period
from hazbin_hotel.src.room import Room
from hazbin_hotel.src.schedule import Schedule
from hazbin_hotel.src.utils import format_date


class Hotel:
    def __init__(self, rooms: List[Room]):
        self._rooms = rooms

    @property
    def rooms(self) -> List[Room]:
        return self._rooms

    def add_room(self, room: Room):
        self._rooms.append(room)

    def remove_room(self, room: Room):
        if len(room.schedules) > 0:
            raise RoomHasSchedule(f'Room "{room.type.value}-{room.number}" cannot be remove because it has schedules.')
        self._rooms.remove(room)

    def check_room_type_availability(self, room_type: RoomTypeEnum) -> Room | None:
        for room in self._rooms:
            if room_type == room.type:
                return room
        raise RoomTypeNotAvailable(f'Room "{room_type.value} is not available in this hotel"')

    def schedule_a_room(
        self,
        client_name: str,
        room_type: RoomTypeEnum,
        start_date: datetime,
        end_date: datetime,
    ):
        room = self.check_room_type_availability(room_type)
        period = Period(start_date, end_date)

        if room.is_period_available(period):
            schedule = Schedule(client_name, period)
            room.add_schedule(schedule)
            return True
        raise RoomNotAvailable(
            f'"{room.type.value}" is not available from {format_date(start_date)} to {format_date(end_date)}'
        )
