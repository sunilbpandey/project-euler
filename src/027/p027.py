from itertools import takewhile
from src.utils.py import prime


def is_prime(num: int, primes: list[int], cache: dict[int, bool]) -> bool:
    if num not in cache:
        cache[num] = prime.is_prime(num, primes)
    return cache[num]


def solve() -> int:
    primes = prime.generate_primes(1415)
    is_prime_cache: dict[int, bool] = {}
    max_n = 0
    product = 0
    for a in range(-999, 1000):  # pylint: disable=invalid-name
        for b in takewhile(lambda p: p < 1000, primes):  # pylint: disable=invalid-name
            for n in range(0, b):  # pylint: disable=invalid-name
                number = n * n + a * n + b
                if number < 0 or not is_prime(number, primes, is_prime_cache):
                    if n > max_n:
                        max_n = n
                        product = a * b
                    break
    return product
