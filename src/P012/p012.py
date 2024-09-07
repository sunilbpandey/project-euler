import itertools
from src.utils.py.math import count_of_divisors
from src.utils.py.prime import generate_primes, factorize
from src.utils.py.series import triangle_numbers


def solve1() -> int:
    primes = generate_primes(9000)
    for triangle in triangle_numbers():
        factors = factorize(triangle, primes=primes)
        if count_of_divisors(triangle, factors=factors) > 500:
            return triangle
    raise Exception("No solution found")  # pylint: disable=broad-exception-raised


def solve() -> int:
    primes = generate_primes(120)
    for k in itertools.count(1):
        count1 = count_of_divisors(k, factors=factorize(k, primes=primes))

        factors = factorize(2 * k - 1, primes=primes)
        count2 = count_of_divisors(2 * k - 1, factors=factors)
        if count1 * count2 > 500:
            return k * (2 * k - 1)

        factors = factorize(2 * k + 1, primes=primes)
        count2 = count_of_divisors(2 * k + 1, factors=factors)
        if count1 * count2 > 500:
            return k * (2 * k + 1)
    raise Exception("No solution found")  # pylint: disable=broad-exception-raised
