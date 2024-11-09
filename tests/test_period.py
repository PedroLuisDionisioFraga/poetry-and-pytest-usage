import os
import sys

from tests import BaseTest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime

import pytest

from hazbin_hotel.src.exceptions.room.invalid_period_error import InvalidPeriodError
from hazbin_hotel.src.period import Period


class TestPeriod(BaseTest):
    def test_should_be_able_to_initialize_valid_period(self):
        """
        Test the initialization of a valid Period object.
        """
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 2)
        period = Period(start, end)
        self.assert_equal(period.start, start)
        self.assert_equal(period.end, end)

    def test_should_not_be_able_to_initialize_invalid_period(self):
        """
        Test the initialization of an invalid Period object.
        The start date is after the end date, which should raise a ValueError.
        """
        start = datetime(2023, 1, 2)
        end = datetime(2023, 1, 1)
        with pytest.raises(InvalidPeriodError):
            Period(start, end)

    def test_should_be_able_to_change_start_to_valid_date(self):
        """
        Test changing the start date of a Period object to a valid date.
        """
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 5)
        period = Period(start, end)
        new_start = datetime(2023, 1, 2)
        result = period.change_start(new_start)
        self.assert_equal(result, True)
        self.assert_equal(period.start, new_start)

    def test_should_not_be_able_to_change_start_to_invalid_date(self):
        """
        Test changing the start date of a Period object to an invalid date.
        The new start date is after the end date, which should return False.
        """
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 5)
        period = Period(start, end)
        new_start = datetime(2023, 1, 6)
        result = period.change_start(new_start)
        self.assert_equal(result, False)
        self.assert_equal(period.start, start)

    def test_should_be_able_to_change_end_to_valid_date(self):
        """
        Test changing the end date of a Period object to a valid date.
        """
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 5)
        period = Period(start, end)
        new_end = datetime(2023, 1, 4)
        result = period.change_end(new_end)
        self.assert_equal(result, True)
        self.assert_equal(period.end, new_end)

    def test_should_not_be_able_to_change_end_to_invalid_date(self):
        """
        Test changing the end date of a Period object to an invalid date.
        The new end date is before the start date, which should return False.
        """
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 5)
        period = Period(start, end)
        new_end = datetime(2022, 12, 31)
        result = period.change_end(new_end)
        self.assert_equal(result, False)
        self.assert_equal(period.end, end)

    def test_should_be_able_to_convert_period_to_string(self):
        """
        Test the __str__ method of a Period object.
        """
        start = datetime(2023, 1, 1)
        end = datetime(2023, 1, 2)
        period = Period(start, end)
        self.assert_equal(str(period), f"START: {start} | END: {end}")
