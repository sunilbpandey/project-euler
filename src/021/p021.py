from typing import Generator
import math


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


def is_amicable(num: int) -> bool:
    divisor_sum = sum(proper_divisors(num))
    return divisor_sum != num and sum(proper_divisors(divisor_sum)) == num


def solve() -> int:
    return sum(num for num in range(2, 10001) if is_amicable(num))
