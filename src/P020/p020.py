from math import factorial
from src.utils.py.math import digit_sum


def solve() -> int:
    return digit_sum(factorial(100))
