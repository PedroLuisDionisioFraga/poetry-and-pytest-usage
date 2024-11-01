import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime

from hazbin_hotel.src.period import Period
from hazbin_hotel.src.schedule import Schedule


class TestSchedule:
    def test_schedule_initialization(self):
        """
        Test the initialization of a Schedule object.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule = Schedule("Client A", period)
        assert schedule.client_name == "Client A"
        assert schedule.period == period
        assert schedule.id == 0

    def test_client_name_property(self):
        """
        Test the client_name property of a Schedule object.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule = Schedule("Client B", period)
        assert schedule.client_name == "Client B"
        schedule.client_name = "Client C"
        assert schedule.client_name == "Client C"

    def test_instance_counter_increment(self):
        """
        Test the instance counter increment of the Schedule class.
        """
        initial_counter = Schedule.instance_counter
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        Schedule("Client D", period)
        assert Schedule.instance_counter == initial_counter + 1

    def test_schedule_id_unique(self):
        """
        Test that each Schedule object has a unique ID.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule1 = Schedule("Client E", period)
        schedule2 = Schedule("Client F", period)
        assert schedule1.id != schedule2.id

    def test_period_assignment(self):
        """
        Test the assignment of a new period to a Schedule object.
        """
        period1 = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        period2 = Period(datetime(2023, 2, 1), datetime(2023, 2, 2))
        schedule = Schedule("Client G", period1)
        schedule.period = period2
        assert schedule.period == period2

    def test_client_name_getter_setter(self):
        """
        Test the getter and setter for the client_name property of a Schedule object.
        """
        period = Period(datetime(2023, 1, 1), datetime(2023, 1, 2))
        schedule = Schedule("Client H", period)
        assert schedule.client_name == "Client H"
        schedule.client_name = "Client I"
        assert schedule.client_name == "Client I"
