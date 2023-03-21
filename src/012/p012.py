from src.utils.py.math import count_of_divisors
from src.utils.py.series import triangle_numbers


def solve() -> int:
    for triangle in triangle_numbers():
        if count_of_divisors(triangle) > 500:
            return triangle
    raise Exception("No solution found")  # pylint: disable=broad-exception-raised
