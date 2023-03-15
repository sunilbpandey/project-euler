import itertools
from src.utils.py.prime import primes


def solve1() -> int:
    return sum(itertools.takewhile(lambda num: num < 2000000, primes()))


def solve() -> int:
    # Prime sieve approach is much faster than using a generator
    limit = 2000000
    sieve = [False] * limit
    prime_sum = 2
    for i in range(3, limit, 2):
        if not sieve[i]:
            prime_sum += i
            for j in range(i * i, limit, i):
                sieve[j] = True
    return prime_sum
