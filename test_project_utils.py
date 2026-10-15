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


def test_invalid_days_above_seven():
    with pytest.raises(ValueError):
        calculate_weekly_hours(5, 8)


def test_negative_days():
    with pytest.raises(ValueError):
        calculate_weekly_hours(5, -1)


def test_decimal_hours():
    assert calculate_weekly_hours(5.5, 4) == 22


def test_boolean_hours_rejected():
    with pytest.raises(TypeError):
        calculate_weekly_hours(True, 6)


def test_decimal_days_rejected():
    with pytest.raises(TypeError):
        calculate_weekly_hours(5, 6.5)
