from src.utils.py.math import digit_sum


def solve() -> int:
    # No need to check all values of a and b. Just check the range [90, 100).
    # Source: https://projecteuler.net/action=redirect;post_id=288
    return max(digit_sum(a**b) for a in range(90, 100) for b in range(90, 100))
