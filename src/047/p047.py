import itertools
from src.utils.py.prime import factorize, generate_primes


def solve1() -> int:
    primes = generate_primes(1500)
    factors1 = factorize(2, primes=primes)
    factors2 = factorize(3, primes=primes)
    factors3 = factorize(4, primes=primes)

    for number in itertools.count(start=5):
        factors4 = factorize(number, primes=primes)
        if (
            len(factors1) >= 4
            and len(factors2) >= 4
            and len(factors3) >= 4
            and len(factors4) >= 4
        ):
            return number - 3
        factors1 = factors2
        factors2 = factors3
        factors3 = factors4
    raise RuntimeError("No solution found")


def solve() -> int:
    # Sieve of Eratosthenes implementation
    # Adapted from https://code.activestate.com/recipes/117119/

    # Build a sieve, collecting the prime factors so we don't have to factorize numbers
    sieve: dict[int, list[int]] = {}

    # Number of numbers with 4 factors left to find
    remaining = 4

    for num in itertools.count(start=2):
        if num in sieve:
            # num is composite and sieve[num] contains its prime factors
            factors = sieve[num]
            del sieve[num]
        else:
            # num is prime
            factors = [num]

        if len(factors) == 4:
            remaining -= 1
            if remaining == 0:
                return num - 3
        else:
            # Either num is prime or it doesn't have exactly 4 prime factors
            remaining = 4

        # Mark next multiple of each factor
        for prime in factors:
            sieve.setdefault(num + prime, []).append(prime)
    raise RuntimeError("No solution found")
