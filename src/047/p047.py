import itertools
from src.utils.py.prime import factorize, generate_primes


def solve() -> int:
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
