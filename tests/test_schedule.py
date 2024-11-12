import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime

from hazbin_hotel.src.period import Period
from hazbin_hotel.src.schedule import Schedule
from tests import BaseTest


class TestSchedule(BaseTest):
    def setup_method(self, method):
        Schedule.instance_counter = 0

    def test_should_be_able_to_initialize_schedule(self, mocker):
        """
        Test the initialization of a Schedule object.

        This test verifies that a Schedule object is correctly initialized
        with the given client name and period.
        """
        period = mocker.Mock(spec=Period)
        period.start = datetime(2023, 1, 1)
        period.end = datetime(2023, 1, 2)
        schedule = Schedule("Client A", period)
        self.assert_equal(Schedule.instance_counter, 1)
        self.assert_equal(schedule.client_name, "Client A")
        self.assert_equal(schedule.period, period)
        self.assert_equal(schedule.id, 0)

    def test_should_be_able_to_access_and_modify_client_name_property(self, mocker):
        """
        Test the client_name property of a Schedule object.

        This test verifies that the client_name property of a Schedule object
        can be correctly accessed and modified.
        """
        period = mocker.Mock(spec=Period)
        period.start = datetime(2023, 1, 1)
        period.end = datetime(2023, 1, 2)
        schedule = Schedule("Client B", period)
        self.assert_equal(schedule.client_name, "Client B")
        schedule.client_name = "Client C"
        self.assert_equal(schedule.client_name, "Client C")

    def test_should_increment_instance_counter(self, mocker):
        """
        Test the instance counter increment of the Schedule class.

        This test verifies that the instance counter of the Schedule class
        is correctly incremented when a new Schedule object is created.
        """
        initial_counter = Schedule.instance_counter
        period = mocker.Mock(spec=Period)
        period.start = datetime(2023, 1, 1)
        period.end = datetime(2023, 1, 2)
        Schedule("Client D", period)
        self.assert_equal(Schedule.instance_counter, initial_counter + 1)

    def test_should_assign_unique_id_to_each_schedule(self, mocker):
        """
        Test that each Schedule object has a unique ID.

        This test verifies that each Schedule object is assigned a unique ID
        when it is created.
        """
        period = mocker.Mock(spec=Period)
        period.start = datetime(2023, 1, 1)
        period.end = datetime(2023, 1, 2)
        schedule1 = Schedule("Client E", period)
        schedule2 = Schedule("Client F", period)
        assert schedule1.id != schedule2.id
        self.assert_not_equal(schedule1.id, schedule2.id)

    def test_should_be_able_to_assign_new_period_to_schedule(self, mocker):
        """
        Test the assignment of a new period to a Schedule object.

        This test verifies that the period of a Schedule object can be correctly
        assigned to a new Period object.
        """
        period1 = mocker.Mock(spec=Period)
        period1.start = datetime(2023, 1, 1)
        period1.end = datetime(2023, 1, 2)

        period2 = mocker.Mock(spec=Period)
        period2.start = datetime(2023, 2, 1)
        period2.end = datetime(2023, 2, 2)
        schedule = Schedule("Client G", period1)
        schedule.period = period2
        self.assert_equal(schedule.period, period2)

    def test_should_be_able_to_get_and_set_client_name(self, mocker):
        """
        Test the getter and setter for the client_name property of a Schedule object.

        This test verifies that the client_name property of a Schedule object
        can be correctly accessed and modified using the getter and setter methods.
        """
        period = mocker.Mock(spec=Period)
        period.start = datetime(2023, 1, 1)
        period.end = datetime(2023, 1, 2)
        schedule = Schedule("Client H", period)
        self.assert_equal(schedule.client_name, "Client H")
        schedule.client_name = "Client I"
        self.assert_equal(schedule.client_name, "Client I")
