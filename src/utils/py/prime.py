from typing import Generator
import math


def is_prime(num: int, primes: list[int]) -> bool:
    limit = math.sqrt(num)
    for prime in primes:
        if prime > limit:
            break
        if num % prime == 0:
            return False
    return True


def primes() -> Generator[int, None, None]:
    primes = [2]
    yield 2

    num = 3
    while True:
        if is_prime(num, primes):
            primes.append(num)
            yield num
        num += 2
