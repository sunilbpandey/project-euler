import itertools
from src.utils.py.prime import primes


def solve() -> int:
    return next(itertools.islice(primes(), 10000, None))
