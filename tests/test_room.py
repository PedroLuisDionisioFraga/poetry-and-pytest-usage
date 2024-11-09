import datetime
import enum
import os
import sys

import pytest

from hazbin_hotel.src.enums.types import RoomTypeEnum
from hazbin_hotel.src.exceptions import InvalidRoomType
from hazbin_hotel.src.period import Period
from hazbin_hotel.src.room import Room
from hazbin_hotel.src.schedule import Schedule
from tests import BaseTest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestRoom(BaseTest):
    def setup_method(self, _):
        self.start_period = datetime.datetime.now()
        self.end_period = self.start_period + datetime.timedelta(days=5)
        self.period = Period(self.start_period, self.end_period)

        self.schedule = Schedule("Cliente A", self.period)
        self.room = Room(
            price=1000.00,
            room_type=RoomTypeEnum.PRESIDENTIAL_SUITE,
            schedules=[self.schedule],
        )

    def teardown_method(self, _):
        Room.instance_count = 1
        Schedule.instance_counter = 0

    def test_should_be_able_to_create_a_room(self):
        Room.instance_count = 1

        start_period = datetime.datetime.now()
        end_period = start_period + datetime.timedelta(days=5)
        period = Period(start_period, end_period)

        schedule = Schedule("Cliente A", period)

        room = Room(
            price=1000.00,
            room_type=RoomTypeEnum.PRESIDENTIAL_SUITE,
            schedules=[schedule],
        )

        self.assert_equal(room.number, 1)
        self.assert_equal(room.type, RoomTypeEnum.PRESIDENTIAL_SUITE)

    def test_should_be_able_to_add_schedule_in_room(self):
        start_period = self.end_period + datetime.timedelta(days=1)
        end_period = start_period + datetime.timedelta(hours=1, days=3)

        schedule_to_add = Schedule("Cliente A", Period(start_period, end_period))

        self.room.add_schedule(schedule_to_add)
        self.assert_equal(len(self.room._schedules), 2)
        self.assert_equal(self.room._schedules[-1].id, 1)

    def test_should_be_able_to_update_a_schedule_of_specific_room(self):
        self.schedule.period.change_start(self.period.start + datetime.timedelta(days=4))

        self.room.update_schedule(self.schedule, self.schedule.id)
        self.assert_equal(
            self.room._schedules[0].period.start.day,
            datetime.datetime.now().day + 4,
        )

    def test_should_be_able_to_change_price_of_specific_room(self):
        self.room.update_price(200)
        self.assert_equal(self.room.price, 200)

    def test_should_be_able_to_change_room_type_specific_room(self):
        self.room.type = RoomTypeEnum.DELUXE
        self.assert_equal(self.room.type, RoomTypeEnum.DELUXE)

    def test_should_not_be_able_to_change_room_type_specific_room_with_invalid_room_type(
        self,
    ):
        unknown_room_type = enum.Enum("UNKNOWN", "UNKNOWN")

        with pytest.raises(InvalidRoomType):
            self.room.type = unknown_room_type.UNKNOWN

    def test_should_not_be_able_to_change_price_of_specific_room_with_negative_price(
        self,
    ):
        with pytest.raises(ValueError):
            self.room.update_price(-1)

    def test_should_not_be_able_to_add_schedule_in_scheduled_date(self):
        start_period = self.start_period + datetime.timedelta(days=1)
        end_period = start_period + datetime.timedelta(hours=1, days=7)

        schedule = Schedule("Cliente A", Period(start_period, end_period))
        with pytest.raises(ValueError):
            self.room.add_schedule(schedule)

    def test_should_not_be_able_to_update_schedule_to_scheduled_date(self):
        start_period = self.start_period + datetime.timedelta(days=7)
        end_period = start_period + datetime.timedelta(hours=1, days=7)

        schedule = Schedule("Cliente A", Period(start_period, end_period))
        self.room.add_schedule(schedule)

        schedule = Schedule(
            "Cliente A",
            Period(start_period + datetime.timedelta(days=2), end_period),
        )
        with pytest.raises(ValueError):
            self.room.update_schedule(schedule, schedule.id)
