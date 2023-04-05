from collections.abc import Generator
import math


def is_prime(num: int, primes: list[int]) -> bool:
    if num < 2:
        return False

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


def generate_primes(limit: int) -> list[int]:
    primes = [2]
    sieve = [False] * limit
    for i in range(3, limit, 2):
        if not sieve[i]:
            primes.append(i)
            for j in range(i * i, limit, i):
                sieve[j] = True
    return primes


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


def factorize(num: int, primes: list[int] | None = None) -> dict[int, int]:
    factors: dict[int, int] = {}

    def divide_by(divisor: int) -> None:
        nonlocal num
        power = 0
        while num % divisor == 0:
            power += 1
            num //= divisor
        if power > 0:
            factors[divisor] = power

    limit = math.floor(math.sqrt(num))

    if primes is None:
        divide_by(2)
        for divisor in range(3, limit + 1, 2):
            if num == 1:
                break
            divide_by(divisor)
    else:
        for prime in primes:
            if num == 1 or prime > limit:
                break
            divide_by(prime)

    if num > 1:
        factors[num] = 1
    return factors
