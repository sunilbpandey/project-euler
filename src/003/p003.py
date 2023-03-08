from typing import Tuple
import math


def divide(num: int, divisor: int) -> Tuple[int, int]:
    exponent = 0
    while num % divisor == 0:
        num //= divisor
        exponent += 1
    return num, exponent


def solve() -> int:
    num = 600851475143
    largest_factor = 0
    num, exponent = divide(num, 2)
    if exponent > 0:
        largest_factor = 2

    limit = int(math.sqrt(num))
    for divisor in range(3, limit + 1, 2):
        num, exponent = divide(num, divisor)
        if exponent > 0:
            largest_factor = divisor
    return largest_factor
