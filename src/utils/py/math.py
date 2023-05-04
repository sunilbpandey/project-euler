from collections.abc import Generator
import math
from src.utils.py.prime import factorize


def divisors(num: int) -> Generator[int, None, None]:
    yield 1
    limit = math.floor(math.sqrt(num)) + 1
    for divisor in range(2, limit):
        if num % divisor == 0:
            yield divisor
            if num // divisor != divisor:
                yield num // divisor
    yield num


def proper_divisors(num: int) -> Generator[int, None, None]:
    yield from (d for d in divisors(num) if d != num)


def count_of_divisors(num: int, factors: dict[int, int] | None = None) -> int:
    if factors is None:
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


def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]


def digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(number))


def totient(num: int, primes: list[int]) -> int:
    factors = factorize(num, primes)
    for factor in factors:
        num = (num * (factor - 1)) // factor
    return int(num)
