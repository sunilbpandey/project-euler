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


def factorize_using_primes(num: int) -> dict[int, int]:
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


def factorize(num: int) -> dict[int, int]:
    factors: dict[int, int] = {}

    def divide_by(divisor: int) -> None:
        nonlocal num
        power = 0
        while num % divisor == 0:
            power += 1
            num //= divisor
        factors[divisor] = power

    divide_by(2)

    limit = math.floor(math.sqrt(num))
    for divisor in range(3, limit + 1, 2):
        if num == 1:
            break
        divide_by(divisor)
    if num > 1:
        factors[num] = 1
    return factors
