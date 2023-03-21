import itertools
from src.utils.py.prime import generate_primes, primes


def solve1() -> int:
    return sum(itertools.takewhile(lambda num: num < 2000000, primes()))


def solve() -> int:
    # Prime sieve approach is much faster than using a generator
    return sum(generate_primes(2000000))
