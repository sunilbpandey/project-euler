from math import factorial


def solve() -> int:
    return sum(int(digit) for digit in str(factorial(100)))
