import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime

from hazbin_hotel.src.period import Period
from hazbin_hotel.src.schedule import Schedule


class TestSchedule:
    def test_should_be_able_to_initialize_schedule(self):
        """
        Test the initialization of a Schedule object.

        This test verifies that a Schedule object is correctly initialized
        with the given client name and period.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule = Schedule("Client A", period)
        assert schedule.client_name == "Client A"
        assert schedule.period == period
        assert schedule.id == 0

    def test_should_be_able_to_access_and_modify_client_name_property(self):
        """
        Test the client_name property of a Schedule object.

        This test verifies that the client_name property of a Schedule object
        can be correctly accessed and modified.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule = Schedule("Client B", period)
        assert schedule.client_name == "Client B"
        schedule.client_name = "Client C"
        assert schedule.client_name == "Client C"

    def test_should_increment_instance_counter(self):
        """
        Test the instance counter increment of the Schedule class.

        This test verifies that the instance counter of the Schedule class
        is correctly incremented when a new Schedule object is created.
        """
        initial_counter = Schedule.instance_counter
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        Schedule("Client D", period)
        assert Schedule.instance_counter == initial_counter + 1

    def test_should_assign_unique_id_to_each_schedule(self):
        """
        Test that each Schedule object has a unique ID.

        This test verifies that each Schedule object is assigned a unique ID
        when it is created.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule1 = Schedule("Client E", period)
        schedule2 = Schedule("Client F", period)
        assert schedule1.id != schedule2.id

    def test_should_be_able_to_assign_new_period_to_schedule(self):
        """
        Test the assignment of a new period to a Schedule object.

        This test verifies that the period of a Schedule object can be correctly
        assigned to a new Period object.
        """
        period1 = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        period2 = Period(datetime(2023, 2, 1), datetime(2023, 2, 2))
        schedule = Schedule("Client G", period1)
        schedule.period = period2
        assert schedule.period == period2

    def test_should_be_able_to_get_and_set_client_name(self):
        """
        Test the getter and setter for the client_name property of a Schedule object.

        This test verifies that the client_name property of a Schedule object
        can be correctly accessed and modified using the getter and setter methods.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule = Schedule("Client H", period)
        assert schedule.client_name == "Client H"
        schedule.client_name = "Client I"
        assert schedule.client_name == "Client I"
