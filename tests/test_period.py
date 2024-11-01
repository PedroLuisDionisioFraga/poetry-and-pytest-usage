import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from datetime import datetime

import pytest

from hazbin_hotel.src.period import Period


def test_period_initialization_valid():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 2)
    period = Period(start, end)
    assert period.start == start
    assert period.end == end


def test_period_initialization_invalid():
    start = datetime(2023, 1, 2)
    end = datetime(2023, 1, 1)
    with pytest.raises(ValueError):
        Period(start, end)


def test_change_start_valid():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 5)
    period = Period(start, end)
    new_start = datetime(2023, 1, 2)
    result = period.change_start(new_start)
    assert result is True
    assert period.start == new_start


def test_change_start_invalid():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 5)
    period = Period(start, end)
    new_start = datetime(2023, 1, 6)
    result = period.change_start(new_start)
    assert result is False
    assert period.start == start


def test_change_end_valid():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 5)
    period = Period(start, end)
    new_end = datetime(2023, 1, 4)
    result = period.change_end(new_end)
    assert result is True
    assert period.end == new_end


def test_change_end_invalid():
    start = datetime(2023, 1, 1)
    end = datetime(2023, 1, 5)
    period = Period(start, end)
    new_end = datetime(2022, 12, 31)
    result = period.change_end(new_end)
    assert result is False
    assert period.end == end
