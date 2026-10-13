
from project_utils import (
    calculate_weekly_hours,
    safe_calculate_weekly_hours,
)


def test_weekly_hours():
    assert calculate_weekly_hours(5, 6) == 30


def test_zero_hours():
    assert calculate_weekly_hours(0, 6) == 0


def test_negative_hours():
    try:
        calculate_weekly_hours(-1, 6)
    except ValueError:
        return

    raise AssertionError("Negatif saatler hata vermeliydi.")


if __name__ == "__main__":
    test_weekly_hours()
    test_zero_hours()
    test_negative_hours()
    print("Tum testler basarili!")
