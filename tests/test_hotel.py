import datetime

import pytest

from hazbin_hotel.src.enums.types import RoomTypeEnum
from hazbin_hotel.src.exceptions import (
    RoomHasSchedule,
    RoomNotAvailable,
    RoomTypeNotAvailable,
)
from hazbin_hotel.src.hotel import Hotel
from hazbin_hotel.src.period import Period
from hazbin_hotel.src.room import Room
from hazbin_hotel.src.schedule import Schedule
from tests import BaseTest


class TestHotel(BaseTest):
    def setup_method(self, _):
        self.start_date = datetime.datetime.now()
        self.end_date = self.start_date + datetime.timedelta(days=5)
        self.period = Period(self.start_date, self.end_date)
        self.schedule = Schedule("Chris", self.period)

        self.presidential_room = Room(RoomTypeEnum.PRESIDENTIAL_SUITE, 2200, [])

        self.hotel = Hotel([self.presidential_room])

    @staticmethod
    def teardown_method(_):
        Room.instance_count = 1
        Schedule.instance_counter = 0

    def test_should_have_room_type_available(self):
        room_type = RoomTypeEnum.PRESIDENTIAL_SUITE
        assert self.hotel.check_room_type_availability(room_type) == self.presidential_room

    def test_should_not_have_room_type_available(self):
        room_type = RoomTypeEnum.BUNGALOW

        with pytest.raises(RoomTypeNotAvailable):
            self.hotel.check_room_type_availability(room_type)

    def test_should_add_room(self, mocker):
        room_type = RoomTypeEnum.FAMILY
        room = mocker.Mock(spec=Room)
        room.type = room_type
        room.price = 1200
        room.schedules = []

        self.hotel.add_room(room)

        self.assert_equal(len(self.hotel.rooms), 2)
        self.assert_equal(self.hotel.rooms[1], room)

    def test_should_remove_room(self):
        room = self.hotel.rooms[0]
        self.hotel.remove_room(room)

        self.assert_equal(len(self.hotel.rooms), 0)

    def test_should_not_remove_room_because_it_has_schedules(self):
        room = self.hotel.rooms[0]
        room.add_schedule(self.schedule)

        with pytest.raises(RoomHasSchedule):
            self.hotel.remove_room(room)

    def test_should_schedule_a_room(self):
        room_type = RoomTypeEnum.PRESIDENTIAL_SUITE

        is_it_scheduled = self.hotel.schedule_a_room("Chris", room_type, self.start_date, self.end_date)

        self.assert_equal(is_it_scheduled, True)

    def test_should_not_schedule_because_room_is_not_available_at_period(self):
        room_type = RoomTypeEnum.PRESIDENTIAL_SUITE
        room = self.hotel.rooms[0]

        room.add_schedule(self.schedule)

        with pytest.raises(RoomNotAvailable):
            self.hotel.schedule_a_room("Chris", room_type, self.start_date, self.end_date)
