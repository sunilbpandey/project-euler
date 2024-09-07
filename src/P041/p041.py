import itertools
from src.utils.py.prime import generate_primes, is_prime


def solve() -> int:
    primes = generate_primes(2800)
    pandigitals = [int("".join(s)) for s in itertools.permutations("7654321")]
    return next(n for n in sorted(pandigitals, reverse=True) if is_prime(n, primes))
