import itertools
from src.utils.py.prime import generate_primes, is_prime


def solve() -> int:
    primes = generate_primes(30000)
    count = 1
    count_primes = 0

    last = 1
    for sidelen in itertools.count(start=3, step=2):
        for _ in range(3):
            last += sidelen - 1
            if is_prime(last, primes):
                count_primes += 1
        count += 4
        last += sidelen - 1
        if count_primes / count < 0.1:
            return sidelen
    raise RuntimeError("No solution found")
