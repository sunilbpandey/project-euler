import math
from src.utils.py.prime import factorize


def count_of_divisors(num: int) -> int:
    factors = factorize(num)
    return math.prod(power + 1 for power in factors.values())


def gcd(a: int, b: int) -> int:  # pylint: disable=invalid-name
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a


def lcm(a: int, b: int) -> int:  # pylint: disable=invalid-name
    return a * (b // gcd(a, b))
