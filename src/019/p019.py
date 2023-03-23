import math


def get_weekday(day: int, month: int, year: int) -> int:
    """Returns the day of the week of the given date using Zeller's congruence."""

    if month < 3:
        month += 12
        year -= 1

    century = year // 100
    year %= 100

    day_of_week = (
        day
        + math.floor(2.6 * (month + 1))
        + year
        + year // 4
        + century // 4
        - 2 * century
    ) % 7
    return day_of_week if day_of_week >= 0 else day_of_week + 7


def solve() -> int:
    sundays = 0
    for year in range(1901, 2001):
        for month in range(1, 13):
            if get_weekday(1, month, year) == 1:
                sundays += 1
    return sundays
