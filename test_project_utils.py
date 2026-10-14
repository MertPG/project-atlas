
import pytest

from project_utils import (
    calculate_weekly_hours,
    safe_calculate_weekly_hours,
)


def test_weekly_hours():
    assert calculate_weekly_hours(5, 6) == 30


def test_zero_hours():
    assert calculate_weekly_hours(0, 6) == 0


def test_negative_hours():
    with pytest.raises(ValueError):
        calculate_weekly_hours(-1, 6)


def test_invalid_input():
    result = safe_calculate_weekly_hours("bes", 6)
    assert result is None
