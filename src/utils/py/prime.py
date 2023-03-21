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


def factorize(num: int) -> dict[int, int]:
    factors: dict[int, int] = {}
    limit = math.floor(math.sqrt(num))
    for prime in primes():
        if num == 1 or prime > limit:
            break
        while num % prime == 0:
            factors.setdefault(prime, 0)
            factors[prime] += 1
            num //= prime
    if num > 1:
        factors[num] = 1
    return factors
